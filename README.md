# Demand Journeys

**Make demand more profitable.** An independent Singapore-based advisory practice connecting digital marketing, direct distribution, conversion, marketing technology and commercial decision-making.

**Public website:** https://www.demandjourneys.com/

## Start here

| Destination | Public URL |
| --- | --- |
| Advisory engagements | https://www.demandjourneys.com/services/engagements/ |
| Hospitality & Travel | https://www.demandjourneys.com/hospitality/ |
| AEO / GEO | https://www.demandjourneys.com/ai-search/ |
| Growth Marketing | https://www.demandjourneys.com/services/growth-marketing/ |
| Platforms & Analytics | https://www.demandjourneys.com/services/platforms-analytics/ |
| Selected work and evidence | https://www.demandjourneys.com/selected-work/ |
| Interactive Tools | https://www.demandjourneys.com/interactive-tools/ |
| Page Scanner & SEO Lab | https://www.demandjourneys.com/interactive-tools/page-scanner/ |
| Presentation library | https://www.demandjourneys.com/hospitality-presentations/ |
| Professional profile | https://www.demandjourneys.com/profile/ |

## Current architecture

Astro 7 static site, GitHub Pages deployment, custom domain via `public/CNAME`. Core public routes use shared Astro layouts; historical decks, demonstrations and preserved source HTML have specialist routes. The presentation catalogue is defined in `src/content/presentations/*.json`.

```text
src/pages/                 Public page routes
src/components/            Shared navigation, enquiry and editorial components
src/styles/                Editorial, services and dedicated tools styles
src/content/presentations/ Current presentation records
public/                    Published assets, legacy deck files and downloads
_source/site/              Preserved original site content for legacy routes
design-backups/            Historical design reference (not current source of truth)
scripts/                   Build finalisation and QA utilities
qa/                        Preserved browser and audit evidence
.github/workflows/pages.yml  Build and deploy to GitHub Pages
```

Do not treat `_source/site/`, `design-backups/`, and old `qa/` screenshots as current site pages. Retain legacy files until their dependencies and live links are audited; avoid deleting archived materials simply to reduce file count.

## Local development

Requires Node.js 22.12 or later.

```bash
npm ci
npm run dev
npm run build
npm run audit
npm run preview
```

The audit checks critical public routes, navigation, page metadata, sitemap entries and the Interactive Tools catalogue. Browser QA can be run with `node scripts/browser-qa.cjs` in an environment with its required Chromium setup.

## Publishing

Every push to `main` triggers the [GitHub Pages workflow](.github/workflows/pages.yml). The published domain is **https://www.demandjourneys.com/**. A GitHub Actions green check confirms the build and deployment pipeline, not that every external service, contact delivery path or DNS client is functioning.

## Content and claims

Notion is the internal authority for Demand Journeys service specifications and professional evidence boundaries. Published content must:

- Distinguish implemented outcomes from approved plans, specifications, independent advice and prototype work.
- Avoid invented client names, testimonials, causal claims or attributable client outcomes.
- Never publish internal consultancy prices or assumed financial performance claims.
- Treat illustrative calculator outputs as **visitor-entered assumptions**, not estimates of a client's actual results.
- Attribute prior employer work correctly; it is not automatically a Demand Journeys client case study.

See [CONTENT.md](CONTENT.md) for presentation record authoring and [DESIGN.md](DESIGN.md) for design history and reference.

## Interactive Tools

`/interactive-tools/` uses a separate topic navigation rail, inspired by the presentation library but with its own independent categories. All input and calculations execute client-side. No customer financial figures are transmitted to the server. Models are deliberately directional and disclose their assumptions.

Current tools:

**DM_Tools browser-only analyzers:** HTML page-source scanner, technical/on-page SEO checks, heading and link analysis, image alt inspection, structured-data extraction and validation, content/keyword analysis, and a search-result appearance preview. These modules are adapted from the source project, [DM_Tools](https://github.com/mengliang10/DM_Tools). They perform no LLM calls and require no server-side Python.

**Scan limitations:** pasted/uploaded HTML works offline; URL fetch only works for same-origin or CORS-enabled endpoints. No cross-origin bypass, HTTP header/security audit, robots.txt retrieval, JavaScript rendering, real-time PageSpeed, live search index inspection, or server-stored history is claimed. The Page Scanner produces a locally downloaded JSON summary with no raw page content beyond a short excerpt. 

Commercial decision tools:

1. Channel distribution cost comparison.
2. Booking funnel conversion scenario.
3. Acquisition efficiency index.
4. AI search readiness checklist.
5. Contribution-based ROI scenario using only visitor-supplied inputs.
6. MarTech and platform decision readiness.

## Measurement and privacy

The live site uses its existing GTM container and FormSubmit integration. Local previews do not submit enquiries. A successful local build is **not** proof the externally hosted form endpoint is correctly configured. Never transmit calculator input values in analytics events. Review [privacy policy](https://www.demandjourneys.com/privacy/) when changing collection practices.

## Operations

- Run `npm run build && npm run audit` before merging changes.
- Check the GitHub Actions result and live public route after deployment.
- Keep the sitemap updated when adding editorial landing pages.
- Verify external redirects and live form delivery separately, without publishing private contacts or user data.
- Prefer changing shared components over copying new layouts or styles into legacy static pages.

**Repository:** https://github.com/mengliang10/demandjourneys
