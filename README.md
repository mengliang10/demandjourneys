# Demand Journeys

Static website for Demand Journeys, an independent commercial and marketing consultancy led by Meng Liang Tan.

## Local preview

No build or package installation is required. From this folder, run:

```sh
python3 -m http.server 8766 --bind 127.0.0.1
```

Open `http://127.0.0.1:8766/` for the homepage or `http://127.0.0.1:8766/hospitality/` for the hospitality practice. Use a local server rather than opening the HTML files directly: asset and navigation paths are relative to the site root.

## Files

- `index.html`: homepage and commercial positioning.
- `hospitality/index.html`: dedicated hospitality practice page.
- `index.css`: shared responsive design, including reduced-motion support.
- `site.js`: mobile navigation, enquiry selection, form handling and production analytics.
- `favicon.svg`: brand monogram.
- `robots.txt`, `sitemap.xml`, `CNAME`: search discovery and existing custom domain.
- `reveal/`: existing presentation archive, retained from the source repository. Its copy has not been updated as part of the website redesign and is not linked from the new pages.

## Enquiries and analytics

Enquiries are addressed to `ml@demandjourneys.com` using the existing FormSubmit service. Only the two production hostnames, `www.demandjourneys.com` and `demandjourneys.com`, enable form delivery and the existing Google Tag Manager container. Other hosts show a local-preview acknowledgement and make no form or analytics requests. Google Fonts remains an external, read-only asset dependency; system fonts provide a fallback.

The form retains input after a failed or unconfirmed response and checks the service's success field before confirming submission. The submit button is enabled by JavaScript; without JavaScript, an email fallback is displayed.

Browser verification covers 320px, 390px, 768px and 1440px widths; navigation, accordion and enquiry interactions; no-JavaScript fallback; and simulated form success, rejection, HTTP failure and network failure. No test enquiry was sent. Live inbox delivery and FormSubmit account activation have not been verified.

The redesign is maintained on `review/profitability-redesign` for review before merging.
