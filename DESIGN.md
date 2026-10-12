---
name: Dr. Ahmad Raza Khan — Academic Portfolio
description: Spectrum — a deep indigo base carrying a full six-colour palette, set in Archivo
colors:
  ink: "oklch(0.21 0.06 278)"
  bg: "oklch(0.985 0.005 278)"
  bg-2: "oklch(0.955 0.014 278)"
  surface: "#FFFFFF"
  line: "oklch(0.9 0.02 278)"
  muted: "oklch(0.44 0.04 278)"
  on-dark: "oklch(0.97 0.01 278)"
  on-dark-muted: "oklch(0.85 0.03 278)"
  cobalt: "oklch(0.52 0.22 266)"
  cobalt-deep: "oklch(0.38 0.19 268)"
  magenta: "oklch(0.55 0.23 352)"
  coral: "oklch(0.72 0.17 40)"
  coral-ink: "oklch(0.55 0.19 35)"
  sun: "oklch(0.88 0.16 92)"
  lime: "oklch(0.9 0.19 125)"
  teal: "oklch(0.74 0.13 185)"
  teal-ink: "oklch(0.48 0.1 195)"
  violet: "oklch(0.52 0.2 300)"
typography:
  display:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(48px, 8vw, 96px)"
    fontWeight: 850
    fontStretch: "112%"
    lineHeight: 0.96
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Archivo"
    fontSize: "clamp(32px, 4.4vw, 56px)"
    fontWeight: 800
    fontStretch: "110%"
    lineHeight: 1.04
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Archivo"
    fontSize: "22-25px"
    fontWeight: 800
    fontStretch: "108%"
  body:
    fontFamily: "Archivo"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Archivo"
    fontSize: "13.5-14.5px"
    fontWeight: 700
  mono:
    fontFamily: "Spline Sans Mono"
    usage: "Hero typewriter line only"
rounded:
  control: "999px"
  field: "14px"
  card: "24px"
  panel: "clamp(28px, 4vw, 48px)"
spacing:
  section: "120px (72px on mobile)"
  wrap: "min(1180px, 100% - 48px)"
components:
  button-primary:
    backgroundColor: "{colors.cobalt}"
    textColor: "#FFFFFF"
    hover: "ink background + 5px solid offset shadow in magenta"
  button-secondary:
    backgroundColor: "{colors.surface}"
    border: "2px solid {colors.ink}"
    hover: "lime background + 5px solid ink offset shadow"
  card:
    backgroundColor: "{colors.surface}"
    border: "1-1.5px solid {colors.line}"
    rounded: "{rounded.card}"
---

# Design System: Spectrum

## 1. Overview

**Creative North Star: "A research profile in full colour."**

The page reads as one long scroll of distinct worlds that share a single voice. A deep indigo **ink** anchors the top (hero) and the bottom (footer); in between, light sections alternate with fully **drenched colour panels**. Six saturated hues (cobalt, magenta, coral, sun, lime, teal, plus violet as a seventh accent) each take ownership of a section, so colour carries navigation and identity rather than decoration.

Credibility comes from structure and type: one typeface (Archivo) used with committed width and weight contrast, generous spacing, solid surfaces, and no glass, blur, or gradient text.

**Key characteristics**
- Dark ink hero and footer as bookends, both rounded panels with a spectrum strip.
- Three drenched mid-page panels: Research Interests (cobalt), Books (sun), Services (magenta).
- Every light section has its own accent via the `--sec` custom property.
- Solid white cards with hairline borders; colour appears in icon tiles, number badges, tags and hover states.
- Hover feedback uses lift plus a hard, solid offset shadow in a palette colour.

## 2. Colour

All colours are OKLCH tokens on `:root` in the `<style>` block of `index.html`.

### Base
- **Ink** — hero, footer, nav, dock, contact "Direct lines" card, headings on light backgrounds.
- **Bg / Bg-2** — page canvas (near-white, tinted toward the ink hue, never cream) and input fills.
- **Surface** — cards, form, modal.
- **Muted** — body copy on light backgrounds (≈8:1 on bg).
- **On-dark / On-dark-muted** — text on ink and drenched panels.

### Palette roles
| Token | Solid use | Text-safe partner on white |
|---|---|---|
| cobalt | primary buttons, Interests panel, stat tile 1 | cobalt / cobalt-deep |
| magenta | Services panel, contact accent, video pill | magenta |
| coral | stat tile, certification accent fills | coral-ink |
| sun | Books panel, Top 2% badge | ink text only |
| lime | active nav, hero highlight, selection | ink text only |
| teal | stat tile, conference-paper section tint | teal-ink |
| violet | professional services, reviewer section | violet |

**Contrast rule.** White text only on cobalt, cobalt-deep, magenta, violet, teal-ink and ink. Coral, sun, lime and teal always take ink text. When a colour is needed as *text* on white, use its `-ink` variant.

### The spectrum strip
`--spectrum` is a hard-stop six-segment bar (no blending). It is the brand motif and appears in exactly four places: under the nav once scrolled, bottom edge of the hero, top edge of the footer, and top edge of modal cards. Do not add it elsewhere.

### Section accents
Each section sets `--sec` (text-safe accent) and `--sec-solid` (fill). `--sec-soft` is derived with `color-mix`. Eyebrow tags, `<em>` in headings, and links inside the section pick these up automatically. Current mapping:

| Section | Accent | Background |
|---|---|---|
| hero | lime | ink panel |
| biography | cobalt | bg |
| researchintersts | lime | cobalt panel |
| publicationimage | magenta | bg |
| books | ink | sun panel |
| researchpaper | cobalt | bg |
| conferresearchpaper | teal | teal tint |
| certifications | coral | bg |
| servicesimage | sun | magenta panel |
| professionalservices | violet | bg |
| journalsreviewer | violet | violet tint |
| contact | magenta | bg |
| appointments | teal | lime tint |
| footer | lime | ink panel |

## 3. Typography

**Archivo** (Google Fonts, variable `wdth 62–125`, `wght 300–900`) does everything. Hierarchy comes from width and weight, not from a second family.

- **Display** (hero name, footer brand): 850 weight, 112% width, tight tracking. The second line ("Raza Khan") flips to 300 weight, 125% width, in lime: a deliberate thick/thin, narrow/wide contrast.
- **Headline** (`.h-display`): 800 / 110%, max 22ch, `text-wrap: balance`. `<em>` is upright, coloured with the section accent and sits on a soft highlighter band (not gradient text).
- **Title** (card and modal headings): 800 / 108%.
- **Body**: 400, 17px, line-height 1.65, max 70ch, `text-wrap: pretty`.
- **Label** (buttons, tags, nav, form labels): 600–700, sentence case. No tracked uppercase except the small Video/Audio overview pills.
- **Mono** (Spline Sans Mono 500): the hero typewriter only.

## 4. Elevation and shape

- Flat by default. Cards use a hairline border plus a very soft shadow (`--shadow-soft`).
- Interactive hover uses a **solid offset shadow** in a palette colour (buttons: 5px below; certificate and reviewer cards: 10px coloured underline).
- Radii: pills 999px, fields 14px, cards 24px, panels `clamp(28px, 4vw, 48px)`.
- The portrait carries two stacked solid offsets (cobalt, then lime).
- No glassmorphism. `backdrop-filter` is used only on the fixed nav and modal backdrop, for legibility.

## 5. Components

- **Nav** — ink pill, white brand with lime surname, muted links; active link is a lime pill with ink text.
- **Social dock** (≥1380px) — ink pill; each icon hovers to a different palette colour.
- **Eyebrow** — rounded tag with a coloured dot, tinted by `--sec-soft`. White-on-translucent inside dark/drenched panels.
- **Hero stats** — five solid tiles, one hue each, lift and tilt slightly on hover.
- **Interest cards** — white on cobalt; each has its own coloured icon tile that rounds to a circle on hover, and a bottom bar that wipes in.
- **Photo cards** — ink veil over image, coloured tag pill, white CTA pill that fills with the card colour on hover.
- **Publication rows** — white rows; the number sits in a coloured square cycling through five hues; hover shifts right and borders in that hue.
- **Certificate filters** — coral-tinted bar, white selects, coral focus ring.
- **Contact** — ink "Direct lines" card with coloured icon squares; form fields fill `bg-2`, focus to white with a magenta ring; submit is magenta.
- **Modals** — white card, spectrum strip on top, ink round close button that turns magenta and rotates on hover; arrows in magenta, nested bullets in teal.

## 6. Motion

- Easing: `cubic-bezier(0.22, 1, 0.36, 1)` everywhere. No bounce.
- Reveal-on-scroll (`.rv`), hero shape float/spin, card tilt (JS), animated stat icons, pulsing video/audio pills.
- `prefers-reduced-motion` disables all animation and shows reveals immediately; hover lifts are disabled on touch devices.

## 7. Do's and Don'ts

**Do**
- Add a new section by giving it an id and a `--sec` / `--sec-solid` pair; everything inside inherits.
- Keep drenched panels to the current three mid-page; more dilutes them.
- Pair light fills (coral, sun, lime, teal) with ink text.
- Test headings at 320px; the hero clamp bottoms out at 40px.

**Don't**
- Use gradient text, glass cards, or blurred decorative panels.
- Add side-stripe borders (`border-left` accents) to cards or list items.
- Introduce a second typeface for headings.
- Use the cream/beige warm-neutral band for any section background.
- Put white text on coral, sun, lime or teal.
