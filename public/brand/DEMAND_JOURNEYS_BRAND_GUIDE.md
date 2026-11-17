# Demand Journeys Brand Guide
**Version:** 1.0 | **Date:** 2026-10-15 | **Status:** Source-aligned specifications + proposed extensions

> This guide is based on the live Demand Journeys portfolio at https://www.demandjourneys.com/hospitality-presentations/personal-portfolio/#/9 and its GitLab source: `hospitality-presentations/personal-portfolio/index.html` and `portfolio.css`. Values marked **SOURCE** are directly specified by the existing CSS. Values marked **STANDARD** are new guidelines for consistent future production, not claims about the original. The vector logo is a **proposed master**, not an extracted historic logo. No custom typeface files are created; use the specified licensed/system fonts.

## 1. Brand identity
- **Name:** Demand Journeys (two words, Title Case in editorial contexts; uppercase for navigation).
- **Core promise (source portfolio):** “More value from the demand you earn.”
- **Descriptor:** Marketing · Commerce · Technology · Customer.
- **Personality:** Insightful, evidence-led, commercially focused, composed, approachable.
- **Visual grammar:** Editorial serif headlines, modern sans-serif detail, restrained palette, warm paper canvas, structured information hierarchy, decisive but limited accents.
- **Do not** imply a case-study result is causal without supporting evidence. Label scenario data illustrative.

## 2. Colour tokens: exact source values

| Role | Token | HEX | RGB | Source / usage |
|---|---|---|---|---|
| Primary ink | `--ink` | **#203E3A** | 32, 62, 58 | SOURCE: headings, body, dark panels, primary button |
| Primary accent | `--teal` | **#237E72** | 35, 126, 114 | SOURCE: eyebrow, chart highlights, interactive controls |
| Canvas | `--paper` | **#F5F2E9** | 245, 242, 233 | SOURCE: slide/background |
| Supporting text | `--muted` | **#60716A** | 96, 113, 106 | SOURCE: annotations, secondary copy |
| Divider | `--line` | **#D5DCD1** | 213, 220, 209 | SOURCE: borders, rules |
| Warm accent | `--orange` | **#B45A34** | 180, 90, 52 | SOURCE: minor emphasis, focus outline |

Additional **SOURCE** contextual fills: panel `#E8EDE4`; cards `#E9EDE3`; light card `#E3E9DE`; highlighted outcome `#D4E4D9`; navigation hover `#D9E5D9`; dark-box secondary lines `#B7C6B8`; muted bars `#93AB91`; highlight bars `#237E72`. These are *not* additional primary brand colours.

### Colour operating rules (STANDARD)
- Paper background is the default; ink is default text.
- Ink background with paper type is reserved for opening/closing slides and emphasis panels.
- Teal is an accent, not the background of every page.
- Terracotta is an occasional point of difference: small rule, warning/decision marker, or accessibility focus. Avoid using it for entire paragraphs.
- Use neutral or sage fills for secondary comparison categories, teal only for the emphasized series; provide labels and legends, not colour-only meaning.
- For accessibility, do not rely on muted colours for tiny text; confirm contrast on actual output (print, projector, browser).

## 3. Type system

| Level | Typeface | Reveal.js exact SOURCE | PowerPoint STANDARD | Documents STANDARD |
|---|---|---|---|---|
| Display / hero | Georgia Regular | 65px on `.dark h2` | 42pt | 24pt cover heading |
| Slide/page H1 | Georgia Regular | 53px, line-height 1.06, tracking -1.7px | 34pt | 20pt |
| H2 / section | Arial Regular | 23px, line-height 1.2 | 22pt | 15pt |
| Main body | Arial Regular | 21px, line-height 1.42 | 18pt | 10.5–11pt |
| Lead / intro | Arial Regular | 23px, line-height 1.45 | 20pt | 12pt |
| Card body | Arial Regular | 18px (common) | 16pt | 10.5pt |
| Source note | Arial Regular | 11px, line-height 1.4 | 9pt | 8–9pt |
| Eyebrow / label | Arial Semi/Bold | 11px; letter-spacing 2px | 10pt; +1pt tracking | 9pt; +0.5pt tracking |
| Numerical metric | Arial Regular | 59px; letter-spacing -2px | 40pt | 18–24pt |

**SOURCE details:** default body font `Arial, Helvetica, sans-serif`; heading family `Georgia, serif`; base Reveal font-size 22px; h2 400 weight; h3 500 weight; paragraph margins 14px vertical; subtitle and eyebrow use restrained tracking. Font sizes above are CSS sizes prior to Reveal's automatic presentation scaling, *not measured physical size on a display*. PowerPoint and documents are deliberate translations rather than pixel-to-point conversions.

**Rules (STANDARD):** no more than two font families per deliverable; use Georgia for distinctive editorial headings and italic callouts only, Arial for navigation, tables, formulas, labels and body. Use sentence case for headings. Keep numeric tables right-aligned with consistent precision. Avoid faux decorative scripts and 3D text. If Georgia/Arial are unavailable, substitute a licensed metrically similar serif/sans; check line wraps before export. Do not redistribute font files.

## 4. Reveal.js layout system

### Source geometry
- `.reveal .slides section`: **650px high**, **28px top / 26px left-right / 44px bottom** padding (SOURCE).
- Heading margin **14px top, 28px bottom**, line-height **1.06** (SOURCE).
- Source footer: absolute bottom **5px**, left/right **26px**, padding-top **11px**, 1px divider (SOURCE).
- Fixed site header: top **24px**, left/right **4%**, 11px text, 1.8px tracking (SOURCE).
- Fixed navigation footer: bottom **19px**, left/right **4%** (SOURCE).
- Two-column split uses **1fr / 1fr** with **56px** gap (SOURCE).
- Most cards use **20–24px** internal padding; panel **30px** (SOURCE).
- Body sections are **650px** tall, but **do not infer a fixed horizontal slide width from the CSS alone**. Check Reveal initialization or rendering before declaring an exact width.
- Source HTML contains ordered slides and a single `section` at hash `#/9`, showing “09 / DEMAND QUALITY”; numeric hashes index from zero.

### New 16:9 design grid (STANDARD)
Use a 1920 × 1080 **design-space grid**, or PowerPoint 13.333 × 7.5in. Margins **96px / 0.667in** left and right; top content safe area **100px / 0.694in**; bottom safe area **80px / 0.556in**. Baseline grid **8px / 0.056in**. Keep slide title aligned to left grid and leave a minimum **32px** gap after heading. All key content must fit within the safe area at native presentation size. Use fixed consistent chapter label at top left and quiet footer with source/page on bottom.

### Diagram / chart spacing (STANDARD)
- Vertical rhythm: 8 / 16 / 24 / 32 / 48px.
- Border: 1px line token, cards 2px teal/sage top rule when needed.
- Avoid text in charts smaller than 15px on the 1920px design canvas; 18px preferred for projected labels.
- Prefer direct labels, zero-baseline bars where appropriate, units and source dates.
- Clearly flag modeled, hypothetical and actual series; show assumptions and exclusions below chart.
- If a scenario is interactive, display current inputs and effective units on the slide.

## 5. PowerPoint implementation (STANDARD)
- Canvas: **16:9 widescreen, 13.333 × 7.5in**.
- Theme colours: Ink `203E3A`; Teal `237E72`; Paper `F5F2E9`; Muted `60716A`; Line `D5DCD1`; Terracotta `B45A34`.
- Theme fonts: Georgia for headings, Arial for body.
- Logo: recommended on cover and closing; optional micro-lockup in top-left header on content slides. No logo behind chart data.
- Content slide geometry: chapter eyebrow x=0.67in y=0.45in; title x=0.67in y=0.86in, max width=12.0in; body begins no higher than y=2.00in; footer source x=0.67in y=7.02in.
- Cover: oversized Georgia headline starting x=0.67in y=1.15in; supporting text starts after title. Primary logo top-left.
- Tables: Arial 14–16pt minimum, 18pt if projected; 1pt border, no heavy grid. Use paper rows with sage alternating shading.
- Default paragraph line-height 1.2–1.35 (PowerPoint equivalents vary); keep 0.08–0.16in spacing between paragraphs.
- Use vector SVG logo where supported and embed fonts only if licensing permits. Inspect in PowerPoint and PDF because rendering varies.
- Speaker notes should carry assumptions, source links, figure provenance and narrative not fit for a slide.

## 6. Documents and reports (STANDARD)
- Page: A4 **210 × 297mm**, portrait, margins **22mm** sides, **20mm** top and bottom.
- Header: wordmark at x=22mm, top=14mm; optional document classification at right.
- H1 Georgia 20pt, H2 Georgia 15pt or Arial Bold 15pt, H3 Arial Bold 12pt.
- Body Arial 10.5–11pt, line spacing 1.25–1.35; 6pt paragraph after. Text colour ink.
- Executive summary panel: warm neutral fill `#E8EDE4`, left border teal 2pt; do not flood page with boxes.
- Tables: Arial 9–10pt, left-align descriptions, right-align numerics; use clear label rows.
- Source notes: Arial 8–9pt muted, include date/source and assumptions where relevant.
- Footer: page number and “DEMAND JOURNEYS” in 8pt muted. Keep header/footer outside body margin.
- Use logo on cover and major section starts; otherwise rely on a restrained wordmark.

## 7. Logo master and lockups

**Status:** NEW PROPOSED VECTOR LOGO SYSTEM. The existing reference presentation uses a text-based “DEMAND JOURNEYS” identification in navigation; it does not provide a verified downloadable master logo. This proposal formalizes a reusable identity without pretending an already approved symbol exists.

### Primary logo concept
- A geometric continuous *journey path* symbol: three nodes connected by a gently rising route, ending in a destination arrow; speaks to measurable progression from demand to value.
- Wordmark: **DEMAND** above **JOURNEYS**, Arial Bold, tightly constructed and aligned on a shared left edge.
- Master asset: [`assets/demand-journeys-logo.svg`](assets/demand-journeys-logo.svg). Its exact SVG vectors are the proposed source of truth. Use the SVG rather than tracing a PNG.
- Approved starting lockups: coloured logo on paper, monochrome ink on paper, paper monochrome on ink. Never place teal on a visually similar background.
- **Clear space:** at least **1 × the symbol node diameter** around all edges (STANDARD).
- **Minimum sizes:** full lockup 160px wide for screen, 35mm print; standalone icon 24px screen, 7mm print (STANDARD). Assess legibility before final signoff.
- Do not stretch, skew, rotate, shadow, gradient-fill, separate nodes, change path stroke ratios or rearrange wordmark without creating a new approved master.
- The logo is an **original proposed vector mark**, not proof of trademark clearance or final brand approval.

### Naming
Use `Demand Journeys` on document covers and in sentences; `DEMAND JOURNEYS` in small caps style for wordmark/header. Avoid “Demand Journey” singular when naming the company.

## 8. Reveal.js implementation snippet

```css
:root {
  --ink:#203e3a; --teal:#237e72; --paper:#f5f2e9;
  --muted:#60716a; --line:#d5dcd1; --orange:#b45a34;
  --dj-heading: Georgia, "Times New Roman", serif;
  --dj-body: Arial, Helvetica, sans-serif;
}
body, .reveal { background:var(--paper); color:var(--ink); font-family:var(--dj-body); }
.reveal h1,.reveal h2 {font-family:var(--dj-heading);font-weight:400;}
.reveal h2 {font-size:53px;line-height:1.06;letter-spacing:-1.7px;}
.reveal p {font-size:21px;line-height:1.42;}
.dj-eyebrow{font:600 11px/1.4 Arial,sans-serif;letter-spacing:2px;color:var(--teal);}
.dj-source{font:400 11px/1.4 Arial,sans-serif;color:var(--muted);border-top:1px solid var(--line);}
.dj-brand-logo {width:210px;height:auto;}
```

Example:
```html
<img class="dj-brand-logo" src="/assets/demand-journeys-logo.svg"
     alt="Demand Journeys">
```

If copying into a presentation subfolder, adjust the asset path. Do not replace existing styles globally without regression-testing its slides.

## 9. Quality and accessibility checklist
1. Match the six primary HEX codes exactly.
2. Use Georgia / Arial hierarchy consistently; test font availability and overflow.
3. Confirm logo clear space, white-space, monochrome reproduction and export.
4. Check projected chart readability, axis labels, units, scenario assumptions and provenance.
5. Check keyboard focus, keyboard slide navigation, reduced-motion user preference, alt text and contrast.
6. Review slide typography at 100% native size, PowerPoint slideshow mode and exported PDF.
7. Keep all source figures traceable; never imply illustrative modelling is client performance.
8. Do not use GitLab CI/CD for style-only changes when zero runner minutes is required.

## 10. Provenance and change control
- **Reference page:** https://www.demandjourneys.com/hospitality-presentations/personal-portfolio/#/9
- **Source project:** https://gitlab.com/mengliang.online/demandjourneys
- **Source files inspected:** `hospitality-presentations/personal-portfolio/index.html`, `hospitality-presentations/personal-portfolio/portfolio.css`; ref `main`, inspected 2026-10-15.
- **SOURCE** values are authoritative **for that portfolio implementation**, not necessarily for every existing Demand Journeys page.
- **STANDARD** values are prospective cross-format specifications, subject to owner approval.
- Before replacing the portfolio's styles with a shared token file, perform screenshot comparisons of all slides.
