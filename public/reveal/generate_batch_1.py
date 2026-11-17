#!/usr/bin/env python3
import os

OUTPUT_DIR = "/home/ml/Documents/00 Job Seeking Tools/Consultancy/DemandJourneys/reveal"
os.makedirs(OUTPUT_DIR, exist_ok=True)

WORKSHOPS = [
    {
        "id": "ws03-predictive-demand-dynamic-pricing",
        "number": "03",
        "title": "PREDICTIVE DEMAND & DYNAMIC PRICING",
        "subtitle": "Augmenting Hotel Revenue Management Systems with Machine Learning & Real-Time Demand Signals",
        "descriptor": "How leading hotel groups integrate forward-looking flight search data, local event compression, competitor rate curves, and price elasticity algorithms to maximize RevPAR and gross operating profit.",
        "target": "DORM, Revenue Directors, Asset Managers, General Managers",
        "framework": "The Multi-Signal Dynamic Yield Engine™",
        "mermaid": """graph TD
    A[Macro Demand Signals<br/>Flight Search Vol, Airport Arrivals] --> E{Predictive AI Demand Engine}
    B[Micro Market Signals<br/>CompSet Rates, Event Compression] --> E
    C[Property Pace Data<br/>OTB Occupancy, Booking Velocity] --> E
    D[Guest Channel Elasticity<br/>Brand.com vs OTA Conversion] --> E
    E --> F[Dynamic Price Recommendation<br/>By Room Tier & Rate Plan]
    F --> G[Automated Push to CRS & Channel Manager]
    G --> H[Brand.com, OTAs, GDS, Metasearch]
    H --> I[Yield Feedback Loop: RevPAR / Net ADR Realization]
    I --> E""",
        "plotly_script": """
          setTimeout(() => {
            const daysOut = ['90 Days', '60 Days', '30 Days', '14 Days', '7 Days', '3 Days', 'Same Day'];
            const legacyStatic = [220, 220, 240, 260, 260, 280, 280];
            const predictiveAI = [210, 225, 275, 340, 395, 430, 410];
            const actualOccupancy = [15, 28, 48, 72, 89, 96, 98];

            const trace1 = { x: daysOut, y: legacyStatic, name: 'Legacy Static Tier Pricing (S$)', type: 'scatter', mode: 'lines+markers', line: { color: '#EF4444', width: 3, dash: 'dot' } };
            const trace2 = { x: daysOut, y: predictiveAI, name: 'AI Dynamic Price Optimization (S$)', type: 'scatter', mode: 'lines+markers', line: { color: '#10B981', width: 4 } };
            const trace3 = { x: daysOut, y: actualOccupancy, name: 'Occupancy on the Books (%)', type: 'bar', yaxis: 'y2', opacity: 0.25, marker: { color: '#FBBF24' } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 50, l: 50, b: 40 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' },
              yaxis: { title: 'Room Rate (S$ ADR)', gridcolor: '#334155' },
              yaxis2: { title: 'OTB Occupancy %', overlaying: 'y', side: 'right', range: [0, 100], showgrid: false },
              legend: { orientation: 'h', y: 1.15, x: 0.05 }
            };
            Plotly.newPlot('plotly-yield-chart', [trace1, trace2, trace3], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-yield-chart",
        "cards_title_1": "Core Demand Vectors",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Unconstrained Demand Forecasting</h4>
            <p>Traditional RMS models base forecasts on historical pickup. Machine learning ingest forward flight searches, visa query volume, and concert/conference announcements to project true unconstrained market appetite.</p>
          </div>
          <div class="dense-card">
            <h4>2. Price Elasticity by Source Market</h4>
            <p>A Japanese leisure traveler and an Australian corporate guest exhibit drastically different willingness-to-pay. AI algorithms calculate localized micro-elasticity curves by country of origin.</p>
          </div>
          <div class="dense-card">
            <h4>3. Net Contribution Optimization</h4>
            <p>Calculates channel-specific distribution commissions in real-time, holding back last-room availability on high-cost OTAs (18–25% take rates) and pushing direct inventory on Brand.com.</p>
          </div>
        """,
        "cards_title_2": "Case Study & Realized Impact",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Luxury Serviced Residence Portfolio</h4>
            <ul>
              <li><strong>Baseline:</strong> 350+ units operating on rigid manual rate tiers updated weekly. Missed high-compression festival weekends and suffered RevPAR dilution.</li>
              <li><strong>AI Integration:</strong> Implemented real-time dynamic pricing model ingesting regional aviation data and competitive set rate changes every 15 minutes.</li>
              <li><strong>Financial Result:</strong> <span class="metric-badge">+18% Net ADR Growth</span> and <span class="metric-badge">+14.2% Total RevPAR Growth</span> over 12 months.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Executive Diagnostic Checklist</h4>
            <ul>
              <li>Do your revenue managers spend 70% of their time updating spreadsheets or designing strategic commercial packages?</li>
              <li>How quickly does your pricing react when a primary competitor sells out their base room category?</li>
              <li>Are your promotional rate fences strictly preserved to protect Brand.com price integrity?</li>
            </ul>
          </div>
        """
    },
    {
        "id": "ws04-ai-virtual-concierge-ancillary",
        "number": "04",
        "title": "AI VIRTUAL CONCIERGE & IN-STAY MONETIZATION",
        "subtitle": "Driving TrevPAR, F&B Spend and Ancillary Revenue via Conversational Guest Assistants",
        "descriptor": "Transforming the on-property guest experience from passive service requests into a high-margin, hyper-personalized revenue engine across WhatsApp, WeChat, Apple Messages, and in-room tablets.",
        "target": "Hotel GMs, Directors of F&B, Operations Directors, Guest Experience Leads",
        "framework": "The In-Stay Ancillary Monetization Loop™",
        "mermaid": """graph LR
    A[Guest Connects to WiFi/WhatsApp] --> B[Instant Guest Profile Match<br/>PMS / Loyalty Status]
    B --> C{Conversational Concierge AI}
    C -->|Natural Language In-Stay Requests| D[Instant Service Dispatch<br/>Housekeeping, Luggage, Maintenance]
    C -->|Contextual Recommendation Engine| E[Personalized Ancillary Upsell]
    E --> F[F&B Dinner Table Booking with Tasting Menu]
    E --> G[Spa Treatment Discount for Off-Peak Slot]
    E --> H[Guaranteed Late Check-out Monetization]
    F --> I[Direct Charge to Room Folio]
    G --> I
    H --> I
    I --> J[+S$68 Average Incremental Ancillary Spend per Guest Stay]""",
        "plotly_script": """
          setTimeout(() => {
            const categories = ['Room Upgrades', 'F&B Bookings', 'Spa & Wellness', 'Late Check-out', 'Local Tours/Transfers'];
            const traditionalFrontDesk = [18, 22, 12, 15, 8];
            const aiVirtualConcierge = [48, 58, 38, 42, 29];

            const trace1 = { x: categories, y: traditionalFrontDesk, name: 'Traditional In-Person Front Desk (S$ Avg)', type: 'bar', marker: { color: '#64748B' } };
            const trace2 = { x: categories, y: aiVirtualConcierge, name: 'AI Virtual Concierge Automation (S$ Avg)', type: 'bar', marker: { color: '#D97706' } };

            const layout = {
              barmode: 'group', paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'Ancillary Spend per Stay (S$)', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-ancillary-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-ancillary-chart",
        "cards_title_1": "Ancillary Monetization Mechanics",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Frictionless Messaging Native Interface</h4>
            <p>Guests will not download a proprietary hotel app for a 3-night stay. Delivering AI concierge capabilities via WhatsApp, WeChat, and WebApp drives 84% adoption rates.</p>
          </div>
          <div class="dense-card">
            <h4>2. Time-Decay Yield Management</h4>
            <p>Unsold spa slots and empty 8:30 PM restaurant tables represent perishable inventory. The AI agent pushes targeted, dynamic offers to guests relaxing on-property during idle windows.</p>
          </div>
          <div class="dense-card">
            <h4>3. Automated Staff Routing & Escalation</h4>
            <p>Routine requests (extra towels, ice, luggage pickup) are routed directly into service dispatch tools (HotSOS/Quore), removing 60% of inbound front-desk phone calls.</p>
          </div>
        """,
        "cards_title_2": "Commercial Impact & Strategy",
        "cards_body_2": """
          <div class="dense-card">
            <h4>250-Key Luxury Resort Implementation</h4>
            <ul>
              <li><strong>Front Desk Labor:</strong> Reduced front-desk call volume by 54% within 60 days of launch.</li>
              <li><strong>F&B Cover Capture:</strong> Shifted on-property dining capture from 28% of guests to 49% through conversational dinner recommendations.</li>
              <li><strong>Ancillary Yield:</strong> Generated <span class="metric-badge">+S$185,000 net incremental profit</span> in year one.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Key Workshop Deliverables</h4>
            <ul>
              <li>The 7-Touchpoint In-Stay Guest Engagement Matrix.</li>
              <li>PMS Folio Integration Blueprint and Tokenized Payment Gateway.</li>
              <li>Tone-of-Voice Prompt Guardrails for 5-Star Luxury Hospitality Standards.</li>
            </ul>
          </div>
        """
    },
    {
        "id": "ws05-single-guest-profile-cdp",
        "number": "05",
        "title": "THE SINGLE GUEST PROFILE: ENTERPRISE CDP ARCHITECTURE",
        "subtitle": "Consolidating Fragmented PMS, CRS, POS and Website Data into Unified Customer Intelligence",
        "descriptor": "A masterclass on breaking down hotel data silos, resolving multi-property guest identities across legacy systems, and establishing a governed single source of truth for hospitality commercial growth.",
        "target": "Chief Information Officers, Chief Commercial Officers, VP Marketing, CRM Directors",
        "framework": "The 12-Source Identity Resolution Engine™",
        "mermaid": """graph TD
    A[Property PMS<br/>Opera, Cloudbeds, Infor] --> E{Enterprise CDP<br/>Identity Graph &amp; Golden Record}
    B[Central Reservation System<br/>Sabre, Amadeus, TravelClick] --> E
    C[Point of Sale POS<br/>F&amp;B, Spa, Golf, Retail] --> E
    D[Digital Touchpoints<br/>Brand.com, Mobile App, WiFi Login] --> E
    E -->|Identity Resolution &amp; Deduplication| F[Unified Golden Guest Profile<br/>2.3M+ Verified Records]
    F --> G[Real-Time Personalization on Brand.com]
    F --> H[Dynamic Segmentation for Email / WhatsApp]
    F --> I[High-Value VIP Recognition at Check-In]
    F --> J[Predictive Lifetime Value LTV Scoring]""",
        "plotly_script": """
          setTimeout(() => {
            const metrics = ['Duplicate Profiles', 'Known Guest Preferences', 'Cross-Property Recognition', 'Direct Campaign ROI', 'Data Hygiene Index'];
            const beforeCDP = [54, 18, 12, 100, 35];
            const afterCDP = [4, 86, 92, 340, 94];

            const trace1 = { x: metrics, y: beforeCDP, name: 'Pre-CDP Legacy Silos', type: 'bar', marker: { color: '#EF4444' } };
            const trace2 = { x: metrics, y: afterCDP, name: 'Post-CDP Golden Record', type: 'bar', marker: { color: '#10B981' } };

            const layout = {
              barmode: 'group', paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'Performance Index Score (0-100 / %)', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-cdp-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-cdp-chart",
        "cards_title_1": "CDP Architecture Principles",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Deterministic vs Probabilistic Matching</h4>
            <p>Resolves conflicting guest records where email, phone number, or passport variations occur across booking channels (e.g. John Doe on Expedia vs J. Doe on Brand.com).</p>
          </div>
          <div class="dense-card">
            <h4>2. Event-Driven Real-Time Data Streaming</h4>
            <p>Ingests real-time events (flight arrival updates, on-property dining charges, website room browsing) with sub-second latency to power live customer journey triggers.</p>
          </div>
          <div class="dense-card">
            <h4>3. Strict Privacy &amp; Consent Governance</h4>
            <p>Centralized consent management compliant with GDPR, PDPA, and China PIPL, ensuring guest opt-out preferences propagate automatically across all properties.</p>
          </div>
        """,
        "cards_title_2": "Case Study & Executive Impact",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Project Meta: 70+ Properties Data Overhaul</h4>
            <ul>
              <li><strong>Scale:</strong> Consolidated 2.3M+ customer records across 12 legacy source systems into a unified CDP.</li>
              <li><strong>Funding:</strong> Secured S$5.5M in Board-approved capital funding backed by a 2.5x revenue performance hurdle.</li>
              <li><strong>Result:</strong> Expanded direct loyalty contribution from 28% to 74% of direct room bookings.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Core Takeaways for Attendees</h4>
            <ul>
              <li>How to calculate the commercial cost of dirty, duplicated guest records.</li>
              <li>RFP Evaluation Matrix for leading CDPs (Adobe Experience Platform, Salesforce Data Cloud, Segment, Tealium).</li>
              <li>The 90-day Data Cleansing and Deduplication Blueprint.</li>
            </ul>
          </div>
        """
    }
]

def generate_html(ws):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{ws['title']} | Demand Journeys Executive Workshop</title>
  <meta name="description" content="{ws['descriptor']}">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

  <!-- Reveal.js Core CSS -->
  <link rel="stylesheet" href="vendor/reveal.min.css" onerror="this.href='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.css'">
  <link rel="stylesheet" href="css/demand-journeys.css">

  <!-- Plotly.js & Mermaid.js -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
  <script>
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'dark',
      themeVariables: {{
        darkMode: true,
        background: '#0F172A',
        primaryColor: '#1E293B',
        primaryTextColor: '#F8FAFC',
        primaryBorderColor: '#D97706',
        lineColor: '#FBBF24',
        secondaryColor: '#172338',
        tertiaryColor: '#0F172A'
      }}
    }});
  </script>
  <style>
    .dense-grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px; }}
    .dense-grid-3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; margin-top: 10px; }}
    .dense-card {{ background: rgba(30, 41, 59, 0.85); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 8px; padding: 14px 18px; }}
    .dense-card h4 {{ font-size: 1.05rem; color: #FBBF24; margin-bottom: 6px; font-weight: 600; }}
    .dense-card p, .dense-card li {{ font-size: 0.82rem; line-height: 1.42; color: #E2E8F0; }}
    .dense-card ul {{ padding-left: 16px; margin: 4px 0; }}
    .metric-badge {{ display: inline-block; background: rgba(217, 119, 6, 0.2); border: 1px solid #D97706; color: #FBBF24; padding: 2px 8px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; font-weight: 600; }}
    .chart-container {{ width: 100%; height: 320px; background: rgba(15, 23, 42, 0.7); border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.1); }}
    .comparison-table {{ width: 100%; border-collapse: collapse; font-size: 0.8rem; margin-top: 8px; }}
    .comparison-table th {{ background: #1E293B; color: #FBBF24; padding: 8px; text-align: left; border: 1px solid #334155; }}
    .comparison-table td {{ padding: 7px 8px; border: 1px solid #334155; color: #E2E8F0; }}
  </style>
</head>
<body>

  <div class="reveal">
    <div class="slides">

      <!-- SLIDE 1: COVER -->
      <section id="slide-01-cover" data-transition="fade">
        <div class="deck-cover-container">
          <div class="slide-tag">Executive Masterclass &bull; Workshop {ws['number']}</div>
          <h1 class="cover-title" style="font-size: 2.35rem; line-height: 1.1;">{ws['title']}</h1>
          <div class="cover-subtitle" style="font-size: 1.2rem; color: #FBBF24; margin-top: 6px;">
            {ws['subtitle']}
          </div>
          <p class="cover-descriptor" style="max-width: 820px; margin: 12px auto; font-size: 0.9rem;">
            {ws['descriptor']}
          </p>

          <div class="workshop-meta-bar" style="margin-top: 14px;">
            <div class="meta-pill"><span class="meta-dot"></span> 90-Minute Executive Session</div>
            <div class="meta-pill"><span class="meta-dot"></span> Target: {ws['target']}</div>
            <div class="meta-pill"><span class="meta-dot"></span> Framework: {ws['framework']}</div>
          </div>

          <div class="cover-footer-note" style="margin-top: 18px;">
            Demand Journeys Executive Workshop Series &bull; Facilitated by Tan Meng Liang &bull; Singapore &bull; Global
          </div>
        </div>
        <aside class="notes">
          Executive Opening:
          - Welcome to Workshop {ws['number']}.
          - The objective of this working session is to translate complex technical and data capabilities into measurable RevPAR, Net ADR, and bottom-line margin expansion.
          - We will dissect architecture schemes, real-world case studies, and concrete financial models.
        </aside>
      </section>

      <!-- SLIDE 2: ARCHITECTURE & SYSTEM SCHEME -->
      <section id="slide-02-architecture" data-transition="slide">
        <div class="slide-tag">01 / Operating Architecture</div>
        <h2 class="slide-headline">System Scheme: <span>{ws['framework']}</span></h2>
        <div class="statement-prefix">End-to-end integration and data flow across hotel enterprise systems</div>

        <div class="mermaid" style="transform: scale(0.88); transform-origin: top center;">
          {ws['mermaid']}
        </div>

        <aside class="notes">
          Walkthrough of the architecture:
          - Explain how data flows seamlessly from operational source systems into analytical and execution layers.
          - Emphasize the closed feedback loop connecting commercial outputs directly to revenue strategy.
        </aside>
      </section>

      <!-- SLIDE 3: DATA VISUALIZATION & FINANCIAL PROOF -->
      <section id="slide-03-chart" data-transition="slide">
        <div class="slide-tag">02 / Quantitative Evidence</div>
        <h2 class="slide-headline">Commercial Impact &amp; <span>Performance Economics</span></h2>
        <div class="statement-prefix">Comparative analysis of baseline performance versus optimized transformation</div>

        <div id="{ws['plotly_id']}" class="chart-container"></div>

        <script>
          {ws['plotly_script']}
        </script>

        <aside class="notes">
          Chart Interpretation:
          - Guide the executives through the metrics shown on screen.
          - Connect the mathematical inflection points to organizational decisions and capital allocation.
        </aside>
      </section>

      <!-- SLIDE 4: CORE PILLARS / MECHANICS -->
      <section id="slide-04-mechanics" data-transition="slide">
        <div class="slide-tag">03 / Strategic Pillars</div>
        <h2 class="slide-headline">Execution Blueprint: <span>{ws['cards_title_1']}</span></h2>
        <div class="statement-prefix">The critical technical and commercial levers that drive sustainable differentiation</div>

        <div class="dense-grid-3">
          {ws['cards_body_1']}
        </div>

        <aside class="notes">
          Deep-dive into the execution pillars:
          - Debated each point with the commercial team.
          - Address common organizational bottlenecks (e.g. legacy IT constraints, siloed department KPIs).
        </aside>
      </section>

      <!-- SLIDE 5: CASE STUDY & ACTION PLAN -->
      <section id="slide-05-casestudy" data-transition="fade">
        <div class="slide-tag">04 / Case Study &amp; Next Steps</div>
        <h2 class="slide-headline">Proven Case Study &amp; <span>90-Day Implementation</span></h2>
        <div class="statement-prefix">Realized multi-property hospitality results and immediate tactical roadmap</div>

        <div class="dense-grid-2">
          {ws['cards_body_2']}
        </div>

        <div style="text-align: center; margin-top: 18px; padding: 12px; background: rgba(217, 119, 6, 0.15); border: 1px solid #D97706; border-radius: 8px;">
          <h3 style="font-size: 1.05rem; color: #FFFFFF; margin: 0;">Schedule this 90-Minute Masterclass for Your Leadership Team</h3>
          <p style="font-size: 0.8rem; color: #FBBF24; margin: 4px 0 0 0;">Contact Demand Journeys to tailor this session to your specific property or portfolio.</p>
        </div>

        <aside class="notes">
          Closing and Q&A:
          - Summarize the strategic imperative.
          - Open floor for candid executive debate on timeline, investment requirements, and team accountability.
        </aside>
      </section>

    </div>
  </div>

  <script src="vendor/reveal.min.js" onerror="this.src='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.js'"></script>
  <script>
    Reveal.initialize({{
      width: 1200,
      height: 700,
      margin: 0.04,
      minScale: 0.2,
      maxScale: 2.0,
      hash: true,
      history: true,
      slideNumber: 'c/t',
      showSlideNumber: 'all',
      transition: 'slide',
      backgroundTransition: 'fade',
      center: false
    }});
  </script>
</body>
</html>"""

for ws in WORKSHOPS:
    filename = os.path.join(OUTPUT_DIR, f"{ws['id']}.html")
    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(generate_html(ws))
    print(f"Generated {filename}")

