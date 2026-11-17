const initialized = new WeakSet();
let navigationEvents;
function initializeSite() {
 if(initialized.has(document.body)) return;
 initialized.add(document.body);
 navigationEvents?.abort();
 navigationEvents=new AbortController();
/* No analytics or form requests leave a local preview. */
const isLive = ['demandjourneys.com', 'www.demandjourneys.com'].includes(location.hostname);

// Mobile navigation toggle
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-navigation');
if (menuButton && navigation) {
  const closeMenu = () => {
    navigation.classList.remove('is-open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.textContent = 'Menu';
  };
  menuButton.addEventListener('click', () => {
    const open = navigation.classList.toggle('is-open');
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.textContent = open ? 'Close' : 'Menu';
  });
  navigation.addEventListener('click', event => { 
    if (event.target.closest('a')) closeMenu(); 
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && navigation.classList.contains('is-open')) {
      closeMenu(); 
      menuButton.focus();
    }
  }, {signal: navigationEvents.signal});
}

// Pre-fill enquiry topic from data-enquiry triggers
const form = document.querySelector('#enquiry-form');
document.querySelectorAll('[data-enquiry]').forEach(control => {
  control.addEventListener('click', (e) => {
    if (!form) return;
    const targetVal = control.dataset.enquiry;
    const select = form.elements.help_with || form.elements.issue || form.elements.topic;
    if (select) {
      select.value = targetVal;
    }
    const nameField = form.elements.name;
    if (nameField) {
      setTimeout(() => nameField.focus(), 150);
    }
  });
});

// Enquiry Form submission handler
if (form) {
  const submit = form.querySelector('button[type="submit"]');
  const status = document.querySelector('#form-status');
  submit.disabled = false;
  const showStatus = (message, error = false) => {
    status.textContent = message;
    status.classList.toggle('error', error);
    status.hidden = false;
  };
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    if (!isLive) {
      showStatus('Local preview: your enquiry is ready, but nothing has been sent. The live form will send enquiries to ml@demandjourneys.com.');
      return;
    }
    if (form.elements._honey && form.elements._honey.value) return;
    submit.disabled = true;
    submit.textContent = 'Sending…';
    status.hidden = true;
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 15000);
    try {
      const response = await fetch('https://formsubmit.co/ajax/ml@demandjourneys.com', {
        method: 'POST', 
        body: new FormData(form),
        headers: { Accept: 'application/json' }, 
        signal: controller.signal
      });
      const result = await response.json();
      if (!response.ok || ![true, 'true'].includes(result.success)) throw new Error('Enquiry not accepted');
      showStatus('Thank you. Your enquiry has been sent.');
      form.reset();
      window.dataLayer?.push({ event: 'enquiry_submitted', page_type: document.body.dataset.page });
    } catch {
      showStatus('Your enquiry could not be sent. Please try again.', true);
    } finally {
      clearTimeout(timeout);
      submit.disabled = false;
      submit.textContent = 'Send Enquiry';
    }
  });
}

// Live tracking
if (isLive) {
  window.dataLayer = window.dataLayer || [];
  if (!document.querySelector('script[src*="googletagmanager.com/gtm.js"]')) {
  window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
  const tag = document.createElement('script');
  tag.async = true;
  tag.src = 'https://www.googletagmanager.com/gtm.js?id=GTM-WRNWZSKD';
  document.head.appendChild(tag);
  }
  document.querySelectorAll('[data-enquiry]').forEach(control => {
    control.addEventListener('click', () => window.dataLayer.push({
      event: 'enquiry_cta_click', 
      enquiry_type: control.dataset.enquiry,
      page_type: document.body.dataset.page
    }));
  });
}

// Carry the chosen service into the homepage enquiry without sending any data.
if (form) {
  const requestedService = new URLSearchParams(location.search).get('service');
  const serviceField = form.elements.help_with;
  if (requestedService && serviceField && [...serviceField.options].some(option => option.value === requestedService)) {
    serviceField.value = requestedService;
  }
}

}
document.addEventListener('astro:page-load',initializeSite);
initializeSite();
