# Demand Journeys — local redesign review

Prepared 11 September 2026.

## Review the site

- Homepage: http://127.0.0.1:8766/
- Hospitality: http://127.0.0.1:8766/hospitality/
- Working copy: `/home/ml/Documents/demandjourneys-review`
- Branch: `review/profitability-redesign`
- Downloaded from: `https://github.com/mengliang10/demandjourneys`
- Source revision: `d5a449a7f7ddc2d3784adb218dbda6ae2e463bb6`
- Screenshots: `/home/ml/Documents/demandjourneys-review-artifacts`

The preview server serves only the repository folder. These notes, portfolio source documents and screenshots are outside that folder. Nothing was pushed or deployed.

## Design and content decisions

Following the adversarial content review, the homepage opens with “Win customers. Keep them. Grow profitably.” It states how Meng Liang can help before explaining his analytical approach. Warm ivory, forest green, serif typography, fine borders and a restrained hospitality illustration establish a light, classic visual style.

The page sequence is practical help → recognisable business situations → specific work → diagnostic → relevant operator evidence → hospitality application → advisory and fractional leadership → founder → enquiry. Services cover analysis, B2B/B2C demand generation, marketing and branding, SEO/AEO/GEO, MarTech, travel and hospitality platforms, AI, customer economics and operating models. See `/home/ml/Documents/demandjourneys-content-review.md` for the objections and resulting copy changes.

The diagnostic offers a demand map, leakage points, measurement gaps and maturity scorecard. Preparation is optional; discovery is possible. Detailed roadmaps, deeper analysis and implementation are separate. No pricing or dollar figures appear in the new pages.

The hospitality page addresses booking contribution, direct/OTA economics, demand and brand, search/AI discovery, metasearch, Brand.com conversion, guest value, CRM/CDP, platform selection and coordination across commercial teams.

Visitors can request a diagnostic, request a call, submit a business question, discuss advisory/fractional leadership or email directly. Calls are requests arranged by email, rather than an invented calendar booking integration. The contact destination is `ml@demandjourneys.com`.

## Recommended portfolio sources

1. **Portfolio 04 — The Transformation Physician** is the best starting structure for the website: problem, diagnosis, work and outcome. Its medical metaphor and stronger claims were not copied into the executive-facing site.
   `/home/ml/Documents/00 Job Seeking Tools/Portfolio_Versions/Portfolio_04_the_transformation_physician.md`
2. **Portfolio 11 — The Master Record** is the best evidence reference because it separates outcomes, scope, projections and claims requiring verification.
   `/home/ml/Documents/00 Job Seeking Tools/Portfolio_Versions/Portfolio_11_the_master_record.md`
3. **Portfolio 02 — The ROI Ledger** has a useful commercial focus, but its emphasis on monetary scale is less appropriate for this public version. Some metric labels also need the corrections recorded in the Master Record.
   `/home/ml/Documents/00 Job Seeking Tools/Portfolio_Versions/Portfolio_02_the_roi_ledger.md`

Additional sources reviewed: `past_career_metrics.md`, the portfolio and campaign indexes, and `Campaign_11_accor_sem_apac_consolidation_2015.md` in the same portfolio folder.

## Evidence used

| Published item | Source and treatment |
|---|---|
| 20+ years of experience | Career chronology beginning in 2003. |
| Frasers: 70+ properties | User confirmed; also in the career metrics and Master Record. Presented as role scope. |
| Frasers: +56% website room nights, 2023 YoY | Master Record §05.1 and §13, reproducing the COO recommendation letter. Corrected from “revenue growth” used in some older portfolios. No claim that the result measures profitability. |
| HomeAway: APAC performance marketing and experimentation | Master Record §06.4. Used specific work descriptions without selecting among conflicting efficiency, ROAS, CAC and CPA versions. |
| Accor: 13 APAC markets | Master Record §05.3 and §06.5. Presented as regional search and analytics scope. Replaces the fee-rate example following user review. |
| TripAdvisor: search and market development across 10 APAC markets | Master Record §05.4 and §06.6. Used role scope and analytical work; omitted conflicting keyword/entity counts. |

All four companies are labelled as prior employers. No former employer is represented as a Demand Journeys client. The user identified the work from these four roles as the desired evidence, so no separate client-work claims or testimonials were invented. Dollar amounts, forecasts presented as realised outcomes, and claims that the Frasers CDP was fully live at departure were excluded.

## Validation and practical limits

- Desktop/mobile checks at 1440, 768, 390 and 320 pixels, with no horizontal overflow.
- Browser checks for navigation, Escape-to-close mobile menu, expandable questions, topic selection and local form acknowledgement.
- Internal links, anchors, duplicate IDs, JSON-LD parsing and JavaScript syntax checked.
- Form success, service rejection, HTTP failure and network failure tested with intercepted responses. No messages sent; actual inbox delivery remains unverified.
- No-JavaScript navigation and email fallback checked.
- Existing Google Tag Manager container retained only on production hostnames.
- Existing `reveal/` decks and backup files retained. The decks contain older positioning and offers, so they are not promoted by the redesigned pages. This round updates the two website pages, not the presentation archive.

## Suggested review order

Review update: replaced the Accor agency-fee example with its 13-market regional search and analytics remit. Removed the COO recommendation-letter references from both public pages; private evidence provenance remains in these notes.

Review the hero and overall tone first, then the four operator examples, then the diagnostic offer and hospitality page. All changes remain local and editable.

User review update: removed the homepage Selected operator experience section and its navigation links. The hospitality cross-link now points to the founder section. The removed section is saved outside the site in demandjourneys-review-artifacts/selected-operator-experience-removed.html.
