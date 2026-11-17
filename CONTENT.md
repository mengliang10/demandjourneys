# Managing presentations

The canonical presentation catalogue is now `src/content/presentations/*.json`. Do not add new catalogue entries to the historical HTML in `_source/site`: it remains an unchanged content snapshot.

Copy an existing JSON record for a new presentation. Use a unique filename. Set:

- `title`, `topic`, `format`, `summary`, `author`
- `href`: existing deck path, beginning with `/`
- `pdf` and `downloadLabel` when a PDF is available
- `tags`: consistent topic names; the search filters and counts build automatically
- `thumbnail`: path relative to the JSON file, usually `../../assets/presentations/your-deck.jpg`
- `published`: optional real publication date, `YYYY-MM-DD`; do not invent dates
- `order`: fallback display order for undated entries (lower first)
- `draft`: true hides the entry from the catalogue and homepage

Add the deck and downloads at their intended public routes. Add the preview source to `src/assets/presentations/`. Astro validates the record and image, generates responsive preview variants, and updates the catalogue and homepage's latest three when you run `npm run build`. Dated entries sort newest first; undated entries follow in `order` order.

The shared document layout is `src/layouts/SiteLayout.astro`. It owns metadata, navigation, footer, the site runtime, and Astro's ClientRouter. Page content stays in its existing page/component. Legacy decks retain their own full document and runtime; presentation cards explicitly navigate to them with a full page load.

Main-page navigation uses a 140ms fade and honours reduced motion. The menu, enquiry form and library initialise on `astro:page-load` with guards against duplicate event listeners. New interactive components must follow that pattern. Native browser navigation remains available when JavaScript is disabled.

Optimised photos and previews originate in `src/assets`. HeroImage selects separate desktop/mobile crops using responsive WebP variants. PresentationCard and the portrait use Astro Picture, with width-specific WebP and JPEG fallbacks. Original public files remain available for existing URLs, downloads and legacy decks.

Before the migration: `design-backups/before-astro-enhancements/src`. QA results: `qa/browser-report.json` and `qa/astro-enhancements-preservation.json`.

## Subject and date browsing

Subject groups and their topic tags live in `src/data/presentation-subjects.json`. The dropdown only displays topics present in published catalogue entries. A presentation belongs to each subject containing one of its tags; unrecognised tags appear under Other topics until assigned to a subject.

Search terms, selected subjects, selected topics and publication date are combined. Multiple subjects match ANY selected subject; multiple topics match ANY selected topic. Dates use a confirmed `published` field only, never a file modification date. On a date is exact; ranges include both endpoints and can have an open start or end. Undated entries appear in Any date and Undated only, and are excluded when an actual date boundary is selected. The three current entries do not have confirmed publication dates.

Filter state is encoded in `q`, `subject`, `tag`, `date`, `on`, `from`, `to` and `page` URL parameters. Clear filters resets search, selections, dates and pagination. Original collection context is retained under About this collection.

The catalogue now prioritises navigation: compact keyword/subject/date controls, 16:9 previews, titles, slide counts and Open/PDF links. Summaries, authors and topic metadata remain in content records and are searchable, but are not repeated on the browsing page. The introductory copy and promotional callout have been removed from the catalogue display.

Latest date simplification: publication filtering now uses a single native month/year input (`month=YYYY-MM` in shared URLs). It matches the month of a recorded publication date. Clearing it shows all presentations, including undated entries. This replaces the previous day/range/undated controls. The Subjects dropdown uses reduced padding and tighter topic spacing.

## Added dates and available months (current)

The three initial presentations are dated **16 November 2026**, as explicitly confirmed by the owner. Their `published` field now serves as the catalogue's added date. New JSON entries without this field are stamped automatically when the collection first loads (build/dev); additions during dev are also watched. The date uses Asia/Singapore and is saved into the JSON file. Existing dates are preserved, including across later builds and edits. Commit the stamped JSON along with the presentation.

The custom month/year picker disables and greys out months with no matching presentations. Availability responds to keyword, subject and topic selections. Clear or All months removes the month filter. Each card shows its added date beside the slide count.
