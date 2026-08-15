/**
 * Demand Journeys Reveal.js Services Deck Initialization
 */

document.addEventListener('DOMContentLoaded', () => {
  if (typeof Reveal !== 'undefined') {
    Reveal.initialize({
      width: 1140,
      height: 680,
      margin: 0.05,
      minScale: 0.2,
      maxScale: 2.0,
      
      // Navigation & Behaviour
      controls: true,
      progress: true,
      slideNumber: 'c/t',
      hash: true,
      keyboard: true,
      touch: true,
      overview: true,
      center: true,
      
      // Transitions
      transition: 'slide',
      transitionSpeed: 'fast',
      backgroundTransition: 'fade',
      
      // Auto-slide off
      autoSlide: 0,
      loop: false
    });

    console.log('[Demand Journeys] Services Deck Initialized Successfully.');
  } else {
    console.error('[Demand Journeys] Reveal.js library not loaded.');
  }
});
