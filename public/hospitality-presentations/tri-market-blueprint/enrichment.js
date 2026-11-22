/* Progressive enhancement. Vanilla JS, no hydration framework required. */
(() => {
  const params = new URLSearchParams(location.search);
  let requestSerial = 0;
  let restoringHistory = false;

  const updateURL = id => {
    const url = new URL(location.href);
    if (id) url.searchParams.set('node', id);
    else url.searchParams.delete('node');
    history.pushState({ node: id || null }, '', url);
  };

  async function attach(id) {
    if (!['sg1','hk1','cn1'].includes(id)) { ++requestSerial; return; }
    const body = document.getElementById('dBody');
    if (!body) return;
    const serial = ++requestSerial;
    const indicator = document.createElement('p');
    indicator.className = 'research-loading';
    indicator.textContent = 'Loading research…';
    body.append(indicator);
    try {
      const response = await fetch(`/hospitality-presentations/tri-market-blueprint/fragments/${encodeURIComponent(id)}/index.html`);
      if (serial !== requestSerial) return;
      if (response.status === 404) {
        indicator.remove(); // Legacy nodes without MDX retain their original dossiers.
        return;
      }
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const doc = new DOMParser().parseFromString(await response.text(), 'text/html');
      if (serial !== requestSerial) return;
      const extra = doc.querySelector('#research-extension');
      indicator.remove();
      if (extra) body.append(document.importNode(extra, true));
    } catch (err) {
      if (serial !== requestSerial) return;
      indicator.className = 'research-error';
      indicator.textContent = 'Research could not be loaded. The original dossier remains available.';
      console.warn('Atlas research fetch:', err);
    }
  }

  document.addEventListener('atlas:select', e => {
    const id = e.detail.id;
    if (!restoringHistory) updateURL(id);
    attach(id);
  });
  document.addEventListener('atlas:clear', () => {
    ++requestSerial;
    if (!restoringHistory) updateURL(null);
  });

  document.addEventListener('click', event => {
    const link = event.target.closest('[data-research-node]');
    if (!link || !window.MarketBlueprintAtlas?.hasNode(link.dataset.researchNode)) return;
    event.preventDefault();
    window.MarketBlueprintAtlas.select(link.dataset.researchNode, true);
  });

  function initialSelection() {
    const id = params.get('node');
    if (id && window.MarketBlueprintAtlas?.hasNode(id)) {
      restoringHistory = true;
      try { window.MarketBlueprintAtlas.select(id, true); } finally { restoringHistory = false; }
    }
  }
  // The original non-module script finishes before this addon loads.
  if (window.MarketBlueprintAtlas) initialSelection();
  else document.addEventListener('atlas:ready', initialSelection, { once: true });

  window.addEventListener('popstate', () => {
    const id = new URLSearchParams(location.search).get('node');
    restoringHistory = true;
    try {
      if (id && window.MarketBlueprintAtlas?.hasNode(id)) window.MarketBlueprintAtlas.select(id, true);
      else window.MarketBlueprintAtlas?.clearSel();
    } finally { restoringHistory = false; }
  });
})();
