# Demand Journeys — photographic homepage direction

Reference: https://template.ulna520.top/ (ulBo Astro Theme), captured 16 November 2026. The reference HTML, CSS and an inspected desktop screenshot are saved in reference/. Firecrawl branding extraction and a direct Chromium capture were used. This is an independently implemented adaptation, not an imported theme.

## Observed reference

The inspected desktop first view fills the screen with a forest photograph, a dark overlay, white navigation and a modest centred heading. A bottom chevron invites scrolling. Reference CSS confirms a 100dvh hero, cover-positioned background, overlaid content and responsive sizes. Heading font: Outfit; body: Plus Jakarta Sans. The stylesheet defines a light background #f4f5f6, white surfaces, 16px card rounding, restrained shadows and numbered sections below the hero. Its blue accent is #2337ff.

Only the desktop screenshot was visually inspected; responsive reference rules were read from CSS. No reference hover, theme-switch or search interactions were exercised. Their presence does not establish a requirement for this advisory homepage.

## Adaptation

- Full-viewport photograph and centred message, with Enquire immediately below it.
- Existing Demand Journeys splash photography, original logo assets and self-hosted fonts. No reference image assets were copied into public/.
- Forest/white accents replace the reference blue to fit the supplied identity; #315b4b is a proposed choice.
- Outfit for headings and the existing Inter Tight body font, rather than adding a new remote font dependency.
- Three services in a white, lightly rounded block; a separate compact enquiry section on a pale background.
- Keep all menu destinations, full inner content, legacy routes and the existing form handler.
- No typewriter delay: the business promise and action are readable immediately, with reduced-motion support.

## Content and CTA

Headline: Make demand more profitable.
Support: Digital marketing advice and leadership. With the commercial perspective to connect it all.
Personal identity: Meng Liang Tan · Independent advisor.
Primary action: Enquire → existing enquiry form.
Secondary actions: Profile, Methodology, Presentations, Substack and GitHub.

The previous editorial design is saved in design-backups/editorial-before-ulbo/. The live site has not been modified.
