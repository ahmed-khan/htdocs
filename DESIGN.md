---
name: Dr. Ahmad Raza Khan — Academic Portfolio
description: The Global Academic Leader — authority, expertise, and human warmth in one connected portfolio
colors:
  cybersea-blue: "#408EC6"
  academic-navy: "#00246B"
  near-black: "#222222"
  mid-gray: "#666666"
  ghost-blue: "#D8E1E4"
  section-paper: "#F5F5F5"
  signal-red: "#FF5252"
  white: "#FFFFFF"
typography:
  display:
    fontFamily: "Raleway, sans-serif"
    fontSize: "clamp(1.75rem, 5vw, 2.5rem)"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "5px"
  headline:
    fontFamily: "Raleway, sans-serif"
    fontSize: "30px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "3px"
  body:
    fontFamily: "Raleway, sans-serif"
    fontSize: "14px"
    fontWeight: 300
    lineHeight: 1.8
  label:
    fontFamily: "Raleway, sans-serif"
    fontSize: "13px"
    fontWeight: 700
    letterSpacing: "1px"
rounded:
  sm: "3px"
  md: "4px"
  lg: "8px"
spacing:
  xs: "5px"
  sm: "15px"
  md: "30px"
  lg: "60px"
  xl: "120px"
components:
  button-primary:
    backgroundColor: "{colors.cybersea-blue}"
    textColor: "{colors.white}"
    rounded: "{rounded.sm}"
    padding: "8px 26px"
  button-primary-hover:
    backgroundColor: "{colors.academic-navy}"
    textColor: "{colors.white}"
  button-dark:
    backgroundColor: "#111111"
    textColor: "{colors.white}"
    rounded: "{rounded.sm}"
    padding: "10px 25px"
  button-cta:
    backgroundColor: "rgba(255,255,255,0.85)"
    textColor: "{colors.near-black}"
    rounded: "{rounded.sm}"
    padding: "8px 26px"
  iconbox:
    backgroundColor: "{colors.white}"
    textColor: "{colors.near-black}"
    rounded: "{rounded.sm}"
    padding: "40px 20px"
---

# Design System: Dr. Ahmad Raza Khan — Academic Portfolio

## 1. Overview

**Creative North Star: "The Global Academic Leader"**

This system is the design equivalent of a well-produced university departmental page — except actually well-designed. It carries the credibility of peer-reviewed publication (clean grid, earned whitespace, disciplined typography) while remaining warm enough that a prospective PhD student wants to reach out and an industry partner feels confident engaging. Authority is signaled through structure and hierarchy, not through decoration.

The palette is anchored in Cybersea Blue: a contemporary, slightly saturated institutional blue that reads as both technical and internationally credible. It carries across sections without becoming monotonous. White and a cool light gray alternate as section backgrounds, giving the long-scroll layout rhythm without drama. Near-black headings and mid-gray body text maintain a clean contrast hierarchy throughout.

Crucially, this system does not perform expertise — it expresses it. No hero metrics. No gradient overlays. No icon-grid-of-twelve that says "this template is for a professor." Every section exists because the content demands it, and the design makes that content easy to scan, trust, and remember.

**Key Characteristics:**
- Open, well-spaced layouts with clear section-to-section rhythm
- Strong typographic hierarchy: one weight-scale relationship, committed uppercase for headings, never for body
- Cybersea Blue as the connective tissue — present in links, accents, active states, and the navigation
- Restrained elevation: almost everything flat, shadows reserved for focus states and modals
- Motion that acknowledges scroll without choreographing it

## 2. Colors: The Cybersea Palette

A primarily neutral palette with one strong institutional blue as the connective tissue. Depth comes from near-black headings against white and paper surfaces, not from additional accent colors.

### Primary
- **Cybersea Blue** (`#408EC6`): The primary accent. Used for links, list markers, active navigation states, button backgrounds, section dividers, and any interactive element at rest. Its saturation is calibrated to read as trustworthy and technical — not corporate-generic, not aggressively startup-blue.
- **Academic Navy** (`#00246B`): Cybersea Blue's deep form. Used for hover states on links and buttons, giving interactive elements clear directionality without contrast-ratio failure. Also appropriate as a hero overlay or dark-section background in full-bleed treatments.

### Neutral
- **Near-Black** (`#222222`): All headings. The near-black (not pure black) softens the contrast to editorial rather than stark.
- **Mid-Gray** (`#666666`): Body copy, secondary text, meta information. At 14px on white this exceeds WCAG AA (approximately 5.7:1 against white). Do not lighten further.
- **Ghost Blue** (`#D8E1E4`): Borders, input outlines, and subtle dividers. The blue tint keeps it from reading as warm — it stays on-brand without asserting itself.
- **Section Paper** (`#F5F5F5`): Alternating section backgrounds. The cool near-white creates visual rhythm in the long-scroll page without introducing a second accent.
- **White** (`#FFFFFF`): Primary canvas, card surfaces, modal backgrounds.
- **Signal Red** (`#FF5252`): Reserved exclusively for the animated heart in the footer copyright. Not to be used elsewhere.

### Named Rules
**The One Voice Rule.** Cybersea Blue is the only color that carries meaning. Signal Red is decorative and strictly contained to one animated element. Adding a second accent anywhere else dilutes the authority of the primary color and fragments the visual system.

**The Paper Rule.** Alternating sections use White and Section Paper (#F5F5F5) only. Adding tinted, colored, or patterned backgrounds to standard content sections is prohibited — reserve full-bleed color treatments for designated hero or call-to-action sections where the dark overlay is part of the content intent.

## 3. Typography

**Primary Font:** Raleway (Google Fonts), sans-serif fallback

Raleway does all the work here — one family in committed weight contrast: 300 for body, 700-800 for headings. The uppercase treatment on headings is consistent and deliberate; it reads as academic formality rather than tech-brand shouting because the letter-spacing is tight enough to feel structured, not loosened to the point of decoration.

**Character:** Geometric at light weight, assertive at heavy weight. The wide aperture keeps it readable at small sizes; the weight range gives the hierarchy enough contrast to function without a second typeface.

### Hierarchy
- **Display** (800 weight, clamp(1.75rem, 5vw, 2.5rem), line-height 1.2, letter-spacing 5px, uppercase): Hero headings and the name treatment in full-bleed sections. Test at narrow viewports — clamp must never produce overflow.
- **Headline** (700 weight, 30px, line-height 1.3, letter-spacing 3px, uppercase): Primary section headings (Biography, Publications, Certifications). Sets the section's authority.
- **Title** (700 weight, 13px, line-height 1.5, letter-spacing 1px, uppercase): Sub-headings within sections, card titles, iconbox labels. Compact and structured.
- **Body** (300 weight, 14px, line-height 1.8, color #666): All prose content. Line length capped at 70ch in single-column layouts. The light weight at 14px on white (#666) passes WCAG AA; do not reduce further.
- **Label** (700 weight, 13px, letter-spacing 1px, uppercase): Buttons, navigation items, badges. Always uppercase when it appears in interactive controls.

### Named Rules
**The Uppercase Ceiling Rule.** Uppercase is used only in headings (Headline and above) and Labels (buttons, nav). Body copy, descriptions, captions, and meta text are never uppercased. Sentences in uppercase at 14px are unreadable; they are prohibited.

**The Lobster Rule.** Lobster is imported but should not be used in new components. It belongs to an earlier version of the visual identity. If it appears, scope it to the original element it was applied to; do not extend it to new surfaces.

## 4. Elevation

This system is flat by default. Depth is expressed through color alternation (white vs. section-paper backgrounds), typographic weight, and spatial separation — not through shadows or blur.

Shadows appear only in two contexts: ambient form wrappers and interactive overlays. They are light and diffuse, not structural.

### Shadow Vocabulary
- **Form Ambient** (`box-shadow: 0 2px 10px rgba(0,0,0,0.10)`): Contact form and iframes only. Signals that the element is an interactive surface distinct from the page canvas.
- **Footer Lift** (`box-shadow: 0 2px 15px rgba(0,0,0,0.08)`): Footer separator. Barely perceptible; marks the end of content.
- **Social Glow** (`box-shadow: 0 0 10px 2px rgba(0,255,0,0.70)` on hover): Currently applied to fixed social buttons on hover. This is the one exception to the otherwise restrained elevation vocabulary — it reads as playful and technical. Acceptable on this element only.

### Named Rules
**The Flat-By-Default Rule.** No component renders with a shadow at rest. Shadows appear only on form wrappers and as hover states on designated interactive elements. A new card, panel, or section that introduces a shadow without a state trigger violates the system.

## 5. Components

### Buttons

Structured, uppercase, Raleway — consistent with the typographic system. No rounded corners beyond 3px.

- **Shape:** Near-square corners (3px radius)
- **Primary:** Cybersea Blue background (#408EC6), white text, 8px 26px padding, uppercase Raleway 13px, letter-spacing 1px
- **Primary Hover:** Academic Navy (#00246B), white text — clear directional shift without a color leap
- **Dark / CTA (dark section):** #111 background, white text, 10px 25px padding
- **CTA on dark background:** rgba(255,255,255,0.85) background, near-black text — reversed for legibility on image or video overlays
- **Transition:** 0.125s ease-in-out — fast enough to feel responsive, not so fast it goes unnoticed

### Iconbox (Service Cards)

- **Shape:** 3px radius (matches global button radius)
- **Background:** White
- **Border:** 1px solid #d4d4d4 on bottom only
- **Icon:** 32px, Near-Black (#222) — not accented; the icon is structural, not decorative
- **Padding:** 40px 20px
- **Do not nest iconboxes.** Iconboxes in a grid are already the system's maximum card density.

### Forms and Inputs

- **Style:** 1px solid Ghost Blue (#D8E1E4) border, white background, 3px radius
- **Font:** 12px Raleway (label-scale), 14px body scale for larger inputs
- **Focus:** Border shifts to rgba(135,135,135,0.7) or #007bff (contact form). Standardize to Cybersea Blue (#408EC6) in future updates for brand coherence.
- **Wrapper shadow:** Form Ambient shadow marks the contact form as an interactive surface
- **No custom checkbox or radio styles currently.** Bootstrap 3 defaults apply; flag for future standardization.

### Navigation

- **Style:** Raleway uppercase, transparent or white background depending on scroll position
- **Default link color:** Inherited near-black or white on dark sections
- **Active/hover:** Cybersea Blue
- **Border:** 1px solid #f5f5f5 at bottom (on light background)
- **Mobile:** Bootstrap 3 responsive collapse; no custom treatment documented

### Social Links (Fixed Sidebar)

- **Shape:** 50px × 50px circle
- **Background:** rgba(0,118,181,0.55) (LinkedIn-adjacent blue-alpha) at rest
- **Hover:** Darker solid blue (#005582) with scale(1.1) + green glow shadow
- **Transition:** 0.3s ease for background, transform, and shadow
- **Notes:** The green glow on hover is the system's one deliberate piece of visual play — it signals the cybersecurity domain. Do not reproduce this treatment on other interactive elements.

### Section Header (pfblock-header)

- **Alignment:** Center by default; left-aligned variant exists (.pfblock-header-left)
- **Structure:** Section title (Headline weight) + 1px gray rule (100px wide, centered) + optional subtitle
- **Margin below:** 60px before content
- **The pfblock-line separator:** rgba(135,135,135,0.5), 100px wide, 1px tall. Thin and geometric — part of the typographic grid, not a decorative divider.

## 6. Do's and Don'ts

### Do
- **Do** use Cybersea Blue (#408EC6) as the single link and interactive-element color across all sections.
- **Do** alternate White and Section Paper (#F5F5F5) for section backgrounds to give the long-scroll page rhythm.
- **Do** keep body text at 300 weight, 14px, #666 minimum — this is the floor for WCAG AA at this size.
- **Do** uppercase headings and button labels only. Reserve uppercase for Headline, Display, and Label typographic roles.
- **Do** use 3px border-radius on all interactive elements (buttons, inputs, chips) for visual consistency.
- **Do** cap single-column body text at 70ch to prevent lines from becoming unreadable on wide viewports.
- **Do** transition interactive elements at 0.125s ease-in-out for links and buttons; 0.4s for navbar and form state changes.
- **Do** test heading copy at mobile viewports — the display font's clamp scale must not overflow at 320px width.

### Don't
- **Don't** use the off-the-shelf Bootstrap blue (#007bff) as the primary brand color. It is present in legacy form styles; consolidate to Cybersea Blue (#408EC6) in future updates.
- **Don't** build a page that looks like a generic Bootstrap professor site — identical blue headers, identical card grid, identical section order with no visual differentiation. That is the primary anti-reference for this project.
- **Don't** use gradient text, glassmorphism panels, dark-mode gradient hero backgrounds, or hero metric grids. These are SaaS/startup aesthetics that are off-register for an academic portfolio.
- **Don't** create wall-of-links sections with no visual hierarchy. Every list of links (publications, certifications) needs typographic hierarchy, spacing, and a clear scan path.
- **Don't** add heavy scroll choreography or oversized display typography that competes with the content. Motion should acknowledge scroll; it should not perform it.
- **Don't** add `border-left` thicker than 1px as a colored stripe on cards or list items. This is a visual shortcut that undercuts the system's structured authority.
- **Don't** introduce a second accent color. Signal Red (#FF5252) is a single decorative element (the footer heart). Extending it — or any other color — as a content accent violates the One Voice Rule.
- **Don't** use all-caps body copy, descriptions, or section subtitles. The Uppercase Ceiling Rule applies: sentences in uppercase at body scale are unreadable and out of register.
- **Don't** extend Lobster to new components. It is legacy; new typography decisions use Raleway exclusively.
