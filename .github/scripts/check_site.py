#!/usr/bin/env python3
"""Check static-site links, structured data, and deferred media behavior."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
SITE_HOSTS = {"connectingahmad.info", "www.connectingahmad.info"}
URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
IMPORT_RE = re.compile(r"@import\s+(?:url\()?['\"]([^'\"]+)['\"]", re.IGNORECASE)


class PageParser(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids: set[str] = set()
        self.elements: dict[str, tuple[str, dict[str, str | None]]] = {}
        self.refs: list[tuple[str, str]] = []
        self.json_ld: list[str] = []
        self.inline_scripts: list[str] = []
        self.styles: list[str] = []
        self.errors: list[str] = []
        self._active_script: list[str] | None = None
        self._active_script_is_json_ld = False
        self._active_style: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.errors.append(f"duplicate id #{element_id}")
            self.ids.add(element_id)
            self.elements[element_id] = (tag, values)

        if tag in {"a", "area", "link"}:
            self._add_ref(values.get("href"), tag)
        for attr in ("src", "poster"):
            self._add_ref(values.get(attr), f"{tag}[{attr}]")
        if values.get("srcset"):
            for candidate in values["srcset"].split(","):
                self._add_ref(candidate.strip().split()[0], f"{tag}[srcset]")

        if tag == "img":
            if "alt" not in values:
                self.errors.append("image is missing alt text")
            if values.get("loading") not in {"lazy", "eager"}:
                self.errors.append("image must declare loading=lazy or loading=eager")
            if values.get("decoding") != "async":
                self.errors.append("image must declare decoding=async")
        if tag in {"audio", "video"} and values.get("preload") != "none":
            self.errors.append(f"{tag} must use preload=none")

        if tag == "script":
            script_type = values.get("type", "").lower()
            if script_type == "application/ld+json":
                self._active_script = []
                self._active_script_is_json_ld = True
            elif not values.get("src") and script_type not in {
                "application/json",
                "importmap",
                "speculationrules",
            }:
                self._active_script = []
                self._active_script_is_json_ld = False
        elif tag == "style":
            self._active_style = []

        style = values.get("style")
        if style:
            self.styles.append(style)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if self._active_script is not None:
            self._active_script.append(data)
        if self._active_style is not None:
            self._active_style.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._active_script is not None:
            script = "".join(self._active_script)
            if self._active_script_is_json_ld:
                self.json_ld.append(script)
            else:
                self.inline_scripts.append(script)
            self._active_script = None
            self._active_script_is_json_ld = False
        elif tag == "style" and self._active_style is not None:
            self.styles.append("".join(self._active_style))
            self._active_style = None

    def _add_ref(self, value: str | None, context: str) -> None:
        if value and value.strip():
            self.refs.append((value.strip(), context))


def local_target(raw_url: str, source: Path) -> tuple[Path, str] | None:
    parsed = urlsplit(raw_url)
    if parsed.scheme and parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc and parsed.hostname not in SITE_HOSTS:
        return None
    if raw_url.startswith("//") and parsed.hostname not in SITE_HOSTS:
        return None

    raw_path = unquote(parsed.path)
    target = ROOT / raw_path.lstrip("/") if raw_path.startswith("/") else source.parent / raw_path
    if not raw_path:
        target = source

    target = target.resolve()
    if target.is_dir() or (not target.exists() and not target.suffix):
        target /= "index.html"
    return target, unquote(parsed.fragment)


def css_references(css: str) -> list[str]:
    values = [match.group(2).strip() for match in URL_RE.finditer(css)]
    values.extend(match.group(1).strip() for match in IMPORT_RE.finditer(css))
    return values


def main() -> int:
    errors: list[str] = []
    pages: dict[Path, PageParser] = {}
    html_files = sorted(
        path for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() == ".html" and ".git" not in path.parts
    )
    node = shutil.which("node")

    for path in html_files:
        parser = PageParser(path)
        try:
            parser.feed(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as error:
            errors.append(f"{path.relative_to(ROOT)}: cannot read HTML: {error}")
            continue
        pages[path.resolve()] = parser
        errors.extend(f"{path.relative_to(ROOT)}: {message}" for message in parser.errors)
        for script in parser.json_ld:
            try:
                json.loads(script)
            except json.JSONDecodeError as error:
                errors.append(f"{path.relative_to(ROOT)}: invalid JSON-LD: {error}")
        if parser.inline_scripts and not node:
            errors.append("Node.js is required to validate inline JavaScript")
        elif node:
            for number, script in enumerate(parser.inline_scripts, start=1):
                result = subprocess.run(
                    [node, "--check", "--input-type=module"],
                    input=script,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if result.returncode:
                    detail = result.stderr.strip().splitlines()[-1]
                    errors.append(
                        f"{path.relative_to(ROOT)}: inline JavaScript block {number}: {detail}"
                    )

    checked_css: set[Path] = set()
    for path, parser in pages.items():
        nav = parser.elements.get("nav")
        burger = parser.elements.get("navBurger")
        nav_links = parser.elements.get("navLinks")
        if not nav or not burger or not nav_links:
            errors.append(f"{path.relative_to(ROOT)}: missing shared navigation elements")
        elif (
            nav[0] != "nav"
            or nav_links[0] != "ul"
            or burger[0] != "button"
            or burger[1].get("type") != "button"
            or burger[1].get("aria-controls") != "navLinks"
            or burger[1].get("aria-expanded") not in {"true", "false"}
        ):
            errors.append(f"{path.relative_to(ROOT)}: navigation toggle is missing button accessibility attributes")

        sources = [(raw_url, context, path) for raw_url, context in parser.refs]
        for style in parser.styles:
            sources.extend((url, "inline CSS", path) for url in css_references(style))

        while sources:
            raw_url, context, base_path = sources.pop()
            result = local_target(raw_url, base_path)
            if result is None:
                continue
            target, fragment = result
            if not target.is_file():
                errors.append(
                    f"{path.relative_to(ROOT)}: missing {context} target {raw_url}"
                )
                continue
            if fragment and target.suffix.lower() in {".html", ".htm"}:
                target_parser = pages.get(target.resolve())
                if target_parser and fragment not in target_parser.ids:
                    errors.append(
                        f"{path.relative_to(ROOT)}: missing #{fragment} in {target.relative_to(ROOT)}"
                    )
            if target.suffix.lower() == ".css" and target.resolve() not in checked_css:
                checked_css.add(target.resolve())
                try:
                    css = target.read_text(encoding="utf-8")
                except (OSError, UnicodeError) as error:
                    errors.append(f"{target.relative_to(ROOT)}: cannot read CSS: {error}")
                    continue
                sources.extend((url, "CSS", target) for url in css_references(css))

    required_routes = (
        "index.html",
        "research/index.html",
        "teaching/index.html",
        "certifications/index.html",
        "contact/index.html",
    )
    for route in required_routes:
        if not (ROOT / route).is_file():
            errors.append(f"missing required page route: {route}")

    sitemap = ROOT / "sitemap.xml"
    if sitemap.is_file():
        try:
            sitemap_root = ET.parse(sitemap).getroot()
            for element in sitemap_root.iter():
                if element.tag.endswith("loc") and element.text:
                    result = local_target(element.text.strip(), sitemap)
                    if result is not None and not result[0].is_file():
                        errors.append(f"sitemap.xml: missing local page {element.text.strip()}")
        except ET.ParseError as error:
            errors.append(f"sitemap.xml: invalid XML: {error}")
    else:
        errors.append("missing sitemap.xml")

    if errors:
        print(f"Site check failed with {len(errors)} issue(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Site check passed: {len(html_files)} HTML pages, links, assets, "
        "navigation, inline JavaScript, JSON-LD, and media loading."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
