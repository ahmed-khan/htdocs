/* ============================================================
   Language switcher (English / Arabic / French)
   The English markup in index.html stays the single source of
   content. Each translatable block is looked up by its English
   HTML (whitespace-collapsed) in js/i18n/<lang>.js; anything not
   in the dictionary simply stays in English.
   ============================================================ */
(function () {
    "use strict";

    var LANGS = { en: { dir: 'ltr' }, ar: { dir: 'rtl' }, fr: { dir: 'ltr' } };
    var STORE_KEY = 'siteLang';
    var ATTRS = ['placeholder', 'aria-label', 'title', 'alt'];
    var SKIP = 'script, style, noscript, svg, template, textarea, select, iframe, audio, video, #typewriter, [data-count], [data-i18n-skip]';

    var dicts = { en: {} };
    var units = null;          // [{ el, key, html }]
    var attrUnits = null;      // [{ el, name, key, value }]
    var current = 'en';
    var originalTitle = document.title;
    var metaDesc = document.querySelector('meta[name="description"]');
    var originalDesc = metaDesc ? metaDesc.getAttribute('content') : '';

    function norm(s) { return String(s).replace(/\s+/g, ' ').trim(); }

    function hasOwnText(el) {
        for (var n = el.firstChild; n; n = n.nextSibling) {
            if (n.nodeType === 3 && /\S/.test(n.nodeValue)) return true;
        }
        return false;
    }

    /* A translation unit is the outermost element of a run of
       text-bearing elements, so "text <strong>x</strong> text"
       is translated as one sentence, not three fragments.
       Buttons always stay their own unit so their listeners survive. */
    function unitFor(textNode) {
        var el = textNode.parentElement;
        while (el.tagName !== 'BUTTON' && el.parentElement && el.parentElement !== document.body && hasOwnText(el.parentElement)) {
            el = el.parentElement;
        }
        return el;
    }

    function collect() {
        units = [];
        attrUnits = [];
        var seen = new Set();
        var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
            acceptNode: function (n) {
                if (!/\S/.test(n.nodeValue)) return NodeFilter.FILTER_REJECT;
                if (n.parentElement.closest(SKIP)) return NodeFilter.FILTER_REJECT;
                return NodeFilter.FILTER_ACCEPT;
            }
        });
        var n;
        while ((n = walker.nextNode())) {
            var el = unitFor(n);
            if (seen.has(el)) continue;
            seen.add(el);
            units.push({ el: el, key: norm(el.innerHTML), html: el.innerHTML });
        }
        document.querySelectorAll('[placeholder], [aria-label], [title], img[alt]').forEach(function (el) {
            if (el.closest('svg, [data-i18n-skip]')) return;
            ATTRS.forEach(function (name) {
                var v = el.getAttribute(name);
                if (v && /\S/.test(v)) attrUnits.push({ el: el, name: name, key: norm(v), value: v });
            });
        });
    }

    /* Translate a string built at runtime by page scripts; {name} placeholders are filled from vars. */
    function t(str, vars) {
        var d = dicts[current] || {};
        var v = d[norm(str)];
        v = v != null ? v : str;
        if (vars) v = v.replace(/\{(\w+)\}/g, function (m, k) { return k in vars ? vars[k] : m; });
        return v;
    }

    function apply(lang) {
        var d = dicts[lang] || {};
        if (!units) collect();
        units.forEach(function (u) {
            var v = lang === 'en' ? null : d[u.key];
            // untranslated units are never rewritten, so nested buttons keep their state
            if (v != null) { u.el.innerHTML = v; u.translated = true; }
            else if (u.translated) { u.el.innerHTML = u.html; u.translated = false; }
        });
        attrUnits.forEach(function (u) {
            var v = lang === 'en' ? null : d[u.key];
            u.el.setAttribute(u.name, v != null ? v : u.value);
        });
        current = lang;
        var root = document.documentElement;
        root.setAttribute('lang', lang);
        root.setAttribute('dir', LANGS[lang].dir);
        document.title = t(originalTitle);
        if (metaDesc) metaDesc.setAttribute('content', t(originalDesc));
        document.querySelectorAll('.lang-switch [data-lang]').forEach(function (b) {
            var on = b.getAttribute('data-lang') === lang;
            b.classList.toggle('is-active', on);
            b.setAttribute('aria-pressed', on ? 'true' : 'false');
        });
        try { localStorage.setItem(STORE_KEY, lang); } catch (e) { /* storage unavailable */ }
        document.dispatchEvent(new CustomEvent('i18n:change', { detail: { lang: lang } }));
    }

    function load(lang, done) {
        if (dicts[lang]) { done(); return; }
        var s = document.createElement('script');
        s.src = 'js/i18n/' + lang + '.js?v=1';
        s.onload = function () { dicts[lang] = (window.I18N && window.I18N[lang]) || {}; done(); };
        s.onerror = function () { dicts[lang] = {}; done(); };
        document.head.appendChild(s);
    }

    var ARABIC_FONT = 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&display=swap';
    function loadArabicFont() {
        if (document.getElementById('font-ar')) return;
        var l = document.createElement('link');
        l.id = 'font-ar'; l.rel = 'stylesheet'; l.href = ARABIC_FONT;
        document.head.appendChild(l);
    }

    function setLang(lang) {
        if (!LANGS[lang]) lang = 'en';
        if (lang === 'ar') loadArabicFont();
        load(lang, function () { apply(lang); });
    }

    window.i18n = {
        t: t,
        setLang: setLang,
        get lang() { return current; },
        _collect: function () { collect(); return { units: units, attrs: attrUnits }; }
    };

    document.addEventListener('click', function (e) {
        var b = e.target.closest && e.target.closest('.lang-switch [data-lang]');
        if (!b) return;
        e.preventDefault();
        setLang(b.getAttribute('data-lang'));
    });

    /* Initial language: ?lang= in the URL, then the saved choice. */
    var initial = 'en';
    try {
        var q = new URLSearchParams(location.search).get('lang');
        initial = (q && LANGS[q]) ? q : (localStorage.getItem(STORE_KEY) || 'en');
    } catch (e) { /* storage unavailable */ }
    collect();
    if (initial !== 'en' && LANGS[initial]) setLang(initial);
})();
