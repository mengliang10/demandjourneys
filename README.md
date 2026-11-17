# Demand Journeys — local Astro editorial redesign

The current homepage follows the selected photographic ulBo reference: a full-screen image, centred message, overlaid navigation, compact services and a visible Enquire action. DESIGN.md records the observed reference and the adaptation. The earlier editorial design is preserved in design-backups/editorial-before-ulbo/. The original repository was downloaded first and remains in ../original. No changes have been pushed or deployed.

## Preview

```bash
npm ci
npm run build
npm run preview -- --port 4321
```

Open http://localhost:4321. Use the preview after building to verify the exact preserved legacy .html URLs. The build finalisation step converts Astro directory-style outputs back to the original .html file paths. Node 22.12+ is required.

## Source structure

- src/pages/index.astro — new homepage.
- src/styles/home.css — homepage-only visual system.
- src/components/Enquiry.astro — retained form fields and markup.
- _source/site/ — preserved original content, read at build time by Astro routes.
- src/pages/[...route].astro — full directory-index pages, with the relocated homepage biography and context appended to Profile.
- Other .html.astro pages — retained presentation/file routes.
- public/ — original CSS, scripts, downloads and assets, plus the selected logo and self-hosted font.
- scripts/finalize-routes.mjs — preserves legacy file URLs in the built output.
- qa/ — browser screenshots, preservation report and source commit.

The full inner-page markup and text are retained. The homepage biography, employer history and original introductory paragraph remain available on Profile. All three services retain their descriptions and preselect the existing form topic. The menu includes Profile, Presentations, Methodology, Substack and GitHub; the footer retains LinkedIn, privacy and profile download access.

## Contact behaviour

The existing FormSubmit endpoint and site.js are preserved. Local previews cannot send enquiries or load live GTM. Tests use synthetic form inputs and verify the local status message. Live delivery was not tested or changed; it still depends on the existing FormSubmit configuration. On the live domain, the original GTM integration remains in place.

## Local validation

```bash
node scripts/browser-qa.cjs
```

The script uses Chromium and a temporary local server to check desktop and mobile layouts, menu behaviour, service prefill, internal homepage links and local form handling. It writes screenshots and JSON results to qa/.

## GitHub Pages readiness

.github/workflows/pages.yml builds the Astro project and deploys dist using GitHub Actions. CNAME is preserved. This is a prepared workflow only. Replacing the live repository or enabling a deployment is a separate publishing action; none has been performed.

The original assets and all 55 legacy HTML routes remain available. The migration deliberately keeps detailed page HTML inside Astro routes so the homepage can change without compressing the rest of the site.

## Consistent main website

Home, Profile, Methodology, Presentations and Privacy now share Header.astro and Footer.astro. Interior.astro preserves the original main content while applying the shared visual system in interior.css. Header links, active states, breadcrumbs, self-hosted fonts, buttons and enquiry routes are consistent. Original slides, demos, historical snapshots and downloads remain intact; their specialist layouts are not converted into article pages.

Before this pass: design-backups/before-site-consistency/src. Browser QA now covers all five main pages at 1440, 390 and 320 pixels, internal links, menu controls and the safe local form. Results: qa/browser-report.json. Content preservation: qa/site-consistency-preservation.json. Nothing has been deployed.

## Editorial refinement

`src/styles/refinement.css` adds the below-the-fold service diagrams, split enquiry panel, publication covers, numbered methodology rows and profile reading hierarchy. `Interior.astro` adds section links and decorative publication covers while retaining the source copy. Earlier version: `design-backups/before-editorial-refinement/src`. Preservation results: `qa/editorial-preservation.json` (55 routes, no missing routes or inner-page text). Desktop and mobile screenshots are in `qa/`.

## Tag library and simple profile

Substack links have been removed from the shared navigation, footer and homepage. The library now derives selectable tags from each presentation's `research-tags` list, supports case-insensitive keyword search, matches ANY selected tag, and paginates at 12 entries. Search/tag/page state is shareable in the URL. With JavaScript disabled all entries remain readable and linked; nonfunctional controls stay hidden.

To add a presentation, add an `article.research-card` entry to `_source/site/hospitality-presentations/index.html` using an existing entry as the template. Supply its title, summary, author, presentation URL, PDF download and `research-tags` spans. Tags and counts regenerate automatically at build time. Keep tag spelling consistent to avoid duplicates. Only the two already-published entries are currently indexed; historical demo/workshop files have not been silently promoted into the public catalogue.

Profile now uses one reading column with plain sections and quieter download links; its original paragraphs remain intact. Backup: `design-backups/before-tag-library/src`. QA: `qa/tag-library-preservation.json` and `qa/browser-report.json`.

## Widescreen previews

Presentation entries now have 16:9 linked preview panels, using first-page JPEGs rendered from the existing PDFs in `public/presentation-previews/`. The library is up to 1400px wide, with two columns on desktop and one on mobile. Copy and tags flow below the fixed-ratio preview. Add a preview named after the presentation URL's final path segment (for example `personal-portfolio.jpg`); entries without an image receive a typographic fallback. QA measures the preview ratio at desktop, mobile and small-mobile widths and checks image loading.

Profile and Methodology also use the 1400px-wide layout with 16:9 opening panels on desktop. Profile details use a two-column reading layout and four capability columns; methodology uses three chapter columns. At 760px and below, opening panels return to natural height and content stacks into one column so text is never squeezed into a fixed ratio.

## Compact Profile (latest)

Profile now uses `ProfileOverview.astro` and `profile-overview.css`, superseding its former 16:9 title panel. The opening contains the name, positioning and contact actions; expertise appears in four responsive cards. Growth and engagement details sit below, with the full introductory background and practice information preserved in native expandable details. Original paragraph preservation and desktop/mobile browser checks passed.

The presentation library introduction is now compact: a two-column title/summary row on desktop and a stacked intro on mobile. Search, tags and 16:9 previews appear earlier, with all original introductory copy retained.

## Proof and selected work

The homepage now moves from the offer to evidence before the enquiry. A forest practice band introduces Meng Liang with a portrait, the existing positioning paragraph and prior roles (employers, not clients), linking to Profile. A selected-thinking section surfaces the two interactive decks with their 16:9 covers, summaries and direct links, and carries the all-presentations and AEO/GEO links. The enquiry panel adds a three-step "How it starts" note. The hero photograph is preloaded per breakpoint, and the structured data now lists service areas and topics.

Copy is drawn from the existing Profile and Methodology material; no results, clients or testimonials were added. Backup: `design-backups/before-practice-thinking/`. Verified with a production build (55 pages), HTML parse, duplicate-ID and local-link checks. Chromium QA covers the homepage at 1440, 390 and 320, including the mobile menu and local form safeguard.

## Presentations library: deck cards

The library now uses the homepage's deck-card treatment: a full-bleed 16:9 cover, a topic and format meta line, an Outfit title, a quiet summary and an "Open the deck" link. Tags, the PDF download and the byline remain as secondary metadata. Search, tag filters, pagination and the editorial-scope note are unchanged.

## AI search service page

`/ai-search/` expands the GEO deck into a sales page: positioning, the five problems worth solving, SEO/AEO/GEO definitions, the two anonymised financial-services diagnostics and their evidence boundary, the 90-day programme and deliverables, three engagement levels, and measurement definitions. All copy is drawn from the deck and the existing profile; no results, clients or guarantees are added. The page is in the header and footer navigation and the sitemap, and the browser QA covers it at 1440, 390 and 320.

The narrow-phone browser pass also fixed the 320px header, made the enquiry fields single-column below 520px, and raised the contrast of the engagement step numbers.

## Methodology, now a deck

The standalone `/methodology/` page is retired. Its content is now the first presentation in the library: `/hospitality-presentations/commercial-system/`, a 10-slide interactive deck in the same format as the other two, covering the seven-stage commercial flow, the eleven chapters, the measurement loop and three ways to start. It has a 16:9 preview, a downloadable PDF and a `noindex` deck page. `/methodology/` redirects to the deck, the sitemap entry is removed, and no navigation link points at the old page.

The AI Search entry in the header, footer and breadcrumb is now labelled AEO/GEO. The page URL remains `/ai-search/`.

## Final navigation and homepage structure

Primary navigation: Profile, Presentations, Services (AEO/GEO, Growth Marketing, Platforms & Analytics), Enquire. Logo returns home. GitHub, downloads, privacy and methodology remain available in the footer. Existing AEO/GEO detail is retained at `/ai-search/`; the service hub is `/services/`, with `/services/growth-marketing/` and `/services/platforms-analytics/`.

Homepage now has a short headline and one compact enquiry form in the opening section, then three service links, engagement formats, a brief practice introduction and a presentation-library link. Service enquiries prefill the homepage topic using a `service` query parameter. Desktop fits the form above the fold; mobile stacks the opening content and form. Local submission remains disabled by hostname. Prior source is retained at `design-backups/final-structure/`. No deployment was performed.

Navigation refinement: the Services dropdown is replaced by direct AEO/GEO, Growth Marketing and Platforms & Analytics links alongside Profile and Presentations. Shared navigation uses a larger semibold font. Below 1120px it uses the responsive menu to avoid crowding; the services hub remains linked from the footer.

Latest homepage trim: Services is a larger bold navigation label; its three service links use the same normal type as Profile and Presentations. Removed the redundant hero “Let’s talk” link, the three service cards/engagement row, and the thinking-library strip from the homepage. The enquiry form and practice introduction remain. Service and presentation pages are unchanged. Previous homepage: `design-backups/before-home-trim/index.astro`.

## Automated homepage presentations

The translucent homepage panel uses `latestPresentations(3)` from `src/lib/presentations.mjs`; the library uses the same parser. Both update on each Astro build. Add presentations to `_source/site/hospitality-presentations/index.html`. An optional `data-published="YYYY-MM-DD"` on `article.research-card` sorts dated entries newest first, before undated entries. Undated entries retain library order: insert new undated presentations at the top. No publication dates were invented for existing entries. The homepage displays up to three titles and links plus a More presentations button.

Visual refinement: latest-presentations panel reduced to a 490px maximum width with smaller type, compact rows and lighter translucency. The shared header groups Services and its three direct links inside a translucent container, with a subtle green tint on light inner pages and wrapping in the responsive menu.

## Astro enhancements — current authoring workflow

**This section supersedes earlier catalogue instructions.** Presentation data is now validated with Astro Content Collections in `src/content/presentations/*.json`. The website no longer parses legacy HTML for catalogue entries. See [CONTENT.md](CONTENT.md) for adding presentations, publication-date sorting, drafts, images and shared layouts.

The main website uses one `SiteLayout.astro` with Astro ClientRouter and a subtle, reduced-motion-aware fade. Interactive behaviour is reinitialised on page changes. Responsive WebP variants are generated for hero photography, portrait and presentation previews. Existing slide decks keep their original runtime and URL.
