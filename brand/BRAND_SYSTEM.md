# Demand Journeys | Unified Hybrid Brand System
Version 1.0 · Decision approved: 15 October 2026 · Implementation: staged

## Decision
The agreed system combines the editorial sophistication of the homepage and the analytical clarity of the Reveal.js portfolio:
- **Newsreader** for editorial headings, **DM Sans** for body, labels, UI, numerical charts. Fallbacks: Georgia / Arial.
- **Deep forest #203E3A** as primary ink; **warm paper #F5F2E9** as canvas.
- **Teal #237E72** as analytical/accent colour; **gold #927448** only for premium editorial detailing.
- Muted **#60716A**, lines **#D5DCD1**, terracotta **#B45A34** for sparse secondary emphasis and keyboard focus.
- These are owner-approved *brand choices*, not a claim that every existing page already implements them.

## Canonical assets
- [brand-tokens.json](brand-tokens.json): machine-readable colour, font and layout choices.
- [brand-tokens.css](brand-tokens.css): prefixed CSS variables and opt-in brand component styles. No current site page imports this file until migration and review.
- Current existing homepage logo treatment and favicon must be audited against the proposed logo from GitLab before deciding the master. **Do not replace the site's existing D/J emblem without approval.**
- The previous presentation-aligned guide remains at GitLab `mengliang.online/demandjourneys/brand/DEMAND_JOURNEYS_BRAND_GUIDE.md`, but this GitHub guide supersedes its *proposed brand direction*.

## Colour and usage

| Role | HEX | Recommended use |
|---|---|---|
| Ink | `#203E3A` | Primary text, dark backgrounds, key callouts |
| Teal | `#237E72` | Links, analytics, highlighted data, eyebrows |
| Gold | `#927448` | Premium hospitality detailing, subtle rules and highlights |
| Paper | `#F5F2E9` | Default page and slide background |
| Muted | `#60716A` | Secondary labels and explanatory metadata, subject to contrast |
| Line | `#D5DCD1` | Hairlines, chart guides, card borders |
| Terracotta | `#B45A34` | Rare secondary emphasis and focus ring |
| Panel | `#E8EDE4` | Low-contrast card and summary background |

Do not use teal and gold as equal competing accent colours on the same panel. Teal communicates decisions and data; gold signals premium or human hospitality context. Use text labels in addition to colour for figures.

## Typeface hierarchy
**Website (recommended default, staged):** Newsreader H1 `clamp(58px, 6.1vw, 88px)` with 1.01 line height; H2 `clamp(38px,4vw,54px)`; H3 29px; DM Sans body 16px at 1.65 line height. These headline sizes preserve the current homepage rhythm but unify the families.

**Reveal.js (16:9 recommended specification):**
- Hero: Newsreader 65px / 1.06, regular.
- Slide title: Newsreader 53px / 1.06, regular.
- Subheading: DM Sans 23px / 1.2, medium.
- Body: DM Sans 21px / 1.42.
- Eyebrow: DM Sans 11px uppercase, 2px tracking.
- Source note: DM Sans 11px / 1.4. Avoid if projected readability is poor.
- Chart labels: ideally 16–18px; charts require labelled units, data source and an explicit illustrative/actual distinction.
The typography sizing retains the portfolio CSS values but substitutes the new chosen brand fonts. The original slide height is 650px; overall Reveal rendering uses its own scaling and layout.

**PowerPoint (16:9, 13.333 × 7.5in):** Newsreader 42pt hero, 34pt slide heading; DM Sans 22pt subheading, 18pt body, 10pt eyebrow, 9pt source. Left/right safe margins 0.67in. Keep minimum projected table text 14pt and preferably 16–18pt.

**Documents (A4):** Newsreader 24pt cover, 20pt H1, 15pt H2; DM Sans 10.5–11pt body at 1.3 line spacing, 8–9pt footnotes. Side margins 22mm, top/bottom 20mm. Headings left aligned, never stretched.

The website, Reveal.js, PowerPoint and document values are *format-specific*, not numerical unit conversions.

## Placement and grids
- Web container max 1200px; use responsive left/right spacing and existing section rhythm pending regression tests.
- Reveal and PowerPoint design grid: 16:9 with 5% horizontal safe margin and consistent left edge across cover, main slides and footer.
- Use 8px increments for component gaps where practical; allow generous content breathing room.
- Keep navigation predictable: logo top-left, section markers at top, sources/footer at bottom.
- Cards should be calm and flat, not gradient-heavy; 1px lines and subtle panels.
- Keep content accessible: visible focus, reduced-motion behaviour, scalable type, no colour-only chart legend.

## Logo decision still outstanding
A legacy D/J symbol exists in GitHub `favicon.svg` (forest background and pale strokes). A new journey-path SVG was added to GitLab. They are different identities and must **not** be deployed interchangeably. Until logo choice is made, retain the current homepage branding and favicon. A future approved logo needs horizontal, stacked, monochrome, reverse, favicon and social versions with clear space and minimum sizing rules.

## Migration strategy (no live changes in this commit)
1. Inventory CSS/HTML styles on homepage, hospitality site and Reveal presentations; list overrides that might break.
2. Compare the existing legacy D/J mark to the proposed journey-path symbol.
3. Get logo-master decision before replacing any visible identity.
4. Integrate prefixed tokens incrementally in a separate branch, using page-level opt-in.
5. Review at desktop/mobile, export slides and PDFs, then merge.
6. Preserve links, routes, claims, content and functions; do not run GitLab CI/CD.
7. Single authority: GitHub `mengliang10/demandjourneys` is the intended production source for domain-linked assets; do not assume GitLab and GitHub automatically synchronize.

## Provenance
- GitHub `index.css`: legacy homepage tokens #233D34/#F7F5EE/#927448 and Newsreader/DM Sans.
- GitHub `hospitality-presentations/personal-portfolio/portfolio.css`: #203E3A/#237E72/#F5F2E9 and Georgia/Arial.
- GitHub `favicon.svg`: existing D/J emblem.
- Owner choice in ChatGPT, 2026-10-15: **Unified hybrid identity**.
