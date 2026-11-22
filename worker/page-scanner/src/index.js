/**
 * Demand Journeys Page Scanner fetch gateway.
 * The browser receives HTML as JSON but never displays it as raw source.
 * This is a public URL fetcher: restrict use and add Cloudflare WAF rate limits.
 */
const ALLOWED_ORIGINS = new Set(['https://www.demandjourneys.com', 'https://demandjourneys.com']);
const MAX_BYTES = 3_000_000;
const MAX_REDIRECTS = 3;
const REQUEST_TIMEOUT_MS = 12_000;

const json = (data, status = 200, origin = '') => new Response(JSON.stringify(data), {
  status,
  headers: {
    'content-type': 'application/json; charset=utf-8',
    'cache-control': 'no-store',
    'x-content-type-options': 'nosniff',
    'access-control-allow-origin': ALLOWED_ORIGINS.has(origin) ? origin : 'null',
    'vary': 'Origin'
  }
});

function targetUrl(input) {
  if (typeof input !== 'string' || input.length > 2048) throw Error('URL is missing or too long.');
  let url;
  try { url = new URL(input); } catch { throw Error('Enter a valid URL.'); }
  if (!['https:', 'http:'].includes(url.protocol)) throw Error('Only HTTP and HTTPS URLs are supported.');
  if (url.username || url.password) throw Error('Credential-bearing URLs are not supported.');
  if (url.port && !['80', '443'].includes(url.port)) throw Error('Non-standard ports are not supported.');
  const host = url.hostname.toLowerCase().replace(/\.$/, '');
  if (!host || host.length > 253 || !host.includes('.')) throw Error('Enter a public hostname.');
  // Reject IP-literal URLs, unusual numeric hostnames, internal and metadata destinations.
  if (host.startsWith('[') || /^[\d.]+$/.test(host) ||
      /(^|\.)(localhost|local|internal|intranet|test|invalid)$/.test(host) ||
      host === 'metadata.google.internal' || host.endsWith('.localhost') ||
      host.endsWith('.home.arpa') || host.endsWith('.onion')) {
    throw Error('Only public websites can be scanned.');
  }
  if (!/^[a-z0-9.-]+$/i.test(host) || host.split('.').some(label => !label || label.length > 63 || label.startsWith('-') || label.endsWith('-'))) {
    throw Error('Hostname format is not supported.');
  }
  url.hash = '';
  return url;
}

async function fetchHtml(url, signal) {
  const visited = new Set();
  for (let i = 0; i <= MAX_REDIRECTS; i++) {
    // Validate every redirect to avoid following redirects toward private endpoints.
    url = targetUrl(url.href);
    if (visited.has(url.href)) throw Error('Redirect loop.');
    visited.add(url.href);
    const response = await fetch(url.href, {
      method: 'GET',
      redirect: 'manual',
      signal,
      headers: { 'Accept': 'text/html,application/xhtml+xml;q=0.9', 'User-Agent': 'DemandJourneysPageScanner/1.0' },
      cf: { cacheTtl: 0 }
    });
    if ([301, 302, 303, 307, 308].includes(response.status)) {
      const location = response.headers.get('location');
      if (!location) throw Error('Redirect target missing.');
      url = targetUrl(new URL(location, url).href);
      continue;
    }
    if (!response.ok) throw Error('Target returned HTTP ' + response.status + '.');
    const type = response.headers.get('content-type') || '';
    if (!/text\/html|application\/xhtml\+xml/i.test(type)) throw Error('Target did not return an HTML page.');
    const advertised = Number(response.headers.get('content-length') || 0);
    if (advertised > MAX_BYTES) throw Error('Page HTML exceeds the 3 MB scan limit.');
    if (!response.body) throw Error('No page source was returned.');
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let html = '', byteCount = 0;
    try {
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        byteCount += value.byteLength;
        if (byteCount > MAX_BYTES) throw Error('Page HTML exceeds the 3 MB scan limit.');
        html += decoder.decode(value, { stream: true });
      }
      html += decoder.decode();
    } finally { await reader.cancel().catch(() => {}); }
    return { url: url.href, html, bytes: byteCount };
  }
  throw Error('Too many redirects.');
}

export default {
  async fetch(request) {
    const origin = request.headers.get('origin') || '';
    const path = new URL(request.url).pathname;
    if (path === '/health' && request.method === 'GET') return json({ status: 'ok', service: 'demandjourneys-page-scanner' }, 200, origin);
    if (!ALLOWED_ORIGINS.has(origin)) return json({ error: 'Origin not permitted.' }, 403, origin);
    if (path !== '/scan') return json({ error: 'Not found.' }, 404, origin);
    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: {
      'access-control-allow-origin': origin,
      'access-control-allow-methods': 'POST, OPTIONS',
      'access-control-allow-headers': 'content-type',
      'access-control-max-age': '600',
      'vary': 'Origin'
    } });
    if (request.method !== 'POST') return json({ error: 'Use POST.' }, 405, origin);
    if (!request.headers.get('content-type')?.toLowerCase().startsWith('application/json')) return json({ error: 'Expected JSON.' }, 415, origin);
    if (Number(request.headers.get('content-length') || 0) > 4096) return json({ error: 'Request too large.' }, 413, origin);
    try {
      const body = await request.json();
      const url = targetUrl(body?.url);
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
      try {
        const result = await fetchHtml(url, controller.signal);
        return json({ ...result, source: 'server-side' }, 200, origin);
      } finally { clearTimeout(timer); }
    } catch (error) {
      const message = error?.name === 'AbortError' ? 'The destination timed out.' : String(error?.message || error);
      const status = /URL|hostname|port|credential|public websites|format|too long|missing/i.test(message) ? 400 : 422;
      return json({ error: message }, status, origin);
    }
  }
};
