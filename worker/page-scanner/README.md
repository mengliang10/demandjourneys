# Demand Journeys Page Scanner Worker

Server-side source retrieval for the existing GitHub Pages URL scanner. This removes **browser-side CORS limitations**, but it does not bypass authentication, Cloudflare challenges or anti-bot restrictions.

## One-time deployment

1. Create or sign into a Cloudflare account. Install/run Wrangler from this directory with `npx wrangler deploy` (or `npx wrangler login` first).
2. Wrangler will return the actual deployed URL, such as `https://demandjourneys-page-scanner.<your-subdomain>.workers.dev`. Do not guess the subdomain.
3. In `src/pages/interactive-tools/page-scanner.astro`, set the page's `data-scanner-api` attribute to `<your deployed URL>/scan`; commit and push.
4. Alternatively, if the demandjourneys.com DNS zone is managed in the same Cloudflare account, enable the commented `routes` custom domain line in `wrangler.toml` and use `https://scanner.demandjourneys.com/scan`. Confirm domain provisioning before publishing the endpoint.
5. Verify `<worker URL>/health` and then test the scanner with a public HTML site.

## Security and operations

- Accepts only requests with Origin `https://www.demandjourneys.com` or `https://demandjourneys.com`. **Origin is not authentication**. Add a Cloudflare WAF rate-limit rule to protect the public endpoint from non-browser abuse.
- Only public HTTP(S) hostnames on standard ports are allowed. IP-literal URLs, local hosts, credentials and internal-looking names are rejected; redirects are checked again.
- Time limit 12 seconds, 3 redirects, 3 MB HTML, no cookies, no scripts executed, no stored HTML.
- This is a source scanner, not a browser rendering service; client-side rendered content and authenticated pages may not be captured.
- Private DNS resolution / DNS rebinding defenses rely partly on Cloudflare's subrequest isolation. For a hardened public commercial scanner, add server-side DNS validation and request budgets at the edge.

## Local

`npx wrangler dev` within `worker/page-scanner` and use an approved Origin header for testing. Local testing from another origin needs a separate, explicit dev origin allowance.
