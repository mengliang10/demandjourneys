/**
 * Demand Journeys Executive Workshop Deck Initialization
 * Proprietary methodology presentation for hospitality & growth advisory
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
      controlsTutorial: false,
      controlsLayout: 'bottom-right',
      controlsBackArrows: 'faded',
      progress: true,
      slideNumber: 'c/t',
      showSlideNumber: 'all',
      hash: true,
      history: true,
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
      loop: false,
      
      // PDF & Print
      pdfMaxPagesPerSlide: 1,
      pdfSeparateFragments: false
    });

    console.log('[Demand Journeys] Executive Workshop Deck Initialized (28 Slides).');
    console.log('Shortcuts: [Space / Arrow Keys] Navigate | [S] Speaker Notes | [O / ESC] Slide Overview | [F] Fullscreen | [?] Help');
  } else {
    console.error('[Demand Journeys] Reveal.js library not loaded.');
  }
});
