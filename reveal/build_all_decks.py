#!/usr/bin/env python3
import os

OUTPUT_DIR = "/home/ml/Documents/00 Job Seeking Tools/Consultancy/DemandJourneys/reveal"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

ALL_WORKSHOPS = [
    # 06
    {
        "id": "ws06-hotel-personalization-realtime-offers",
        "number": "06",
        "title": "NEXT-GEN HOTEL PERSONALIZATION & REAL-TIME OFFERS",
        "subtitle": "Transforming Brand.com from a Static Brochure into an Intent-Driven Conversion Engine",
        "descriptor": "How to deploy real-time behavioral triggers, dynamic room packaging, and localized personalization on direct hotel booking engines to lift direct conversion from 0.68% to 2.25%.",
        "target": "VP Digital, E-Commerce Directors, Commercial Leads, Web Product Managers",
        "framework": "The Dynamic Intent-to-Offer Engine™",
        "mermaid": """graph LR
    A[Visitor Lands on Brand.com] --> B[Real-Time Intent Scorer<br/>GeoIP, Referrer, Device, History]
    B --> C{Contextual Segmentation}
    C -->|Long-Haul Leisure Traveler| D[Dynamic Merchandising:<br/>Stay Longer & Save + Airport Transfer]
    C -->|Short-Notice Corporate| E[Dynamic Merchandising:<br/>Flexible Cancellation + Executive Breakfast]
    C -->|Known Loyalty Member| F[Dynamic Merchandising:<br/>Complimentary Suite Upgrade Offer]
    D --> G[Optimized 1-Click Checkout]
    E --> G
    F --> G
    G --> H[Direct Revenue Realization (+56% YoY Direct Room Nights)]""",
        "plotly_script": """
          setTimeout(() => {
            const visitorTypes = ['First-Time Visitor (Generic)', 'Returning Geo-Targeted', 'Corporate Business Intent', 'Loyalty Member (Logged-In)'];
            const staticConversion = [0.65, 0.95, 1.20, 2.40];
            const personalizedConversion = [1.45, 2.65, 3.85, 6.20];

            const trace1 = { x: visitorTypes, y: staticConversion, name: 'Static Brand.com Template (%)', type: 'bar', marker: { color: '#64748B' } };
            const trace2 = { x: visitorTypes, y: personalizedConversion, name: 'Real-Time Dynamic Personalization (%)', type: 'bar', marker: { color: '#10B981' } };

            const layout = {
              barmode: 'group', paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'Booking Engine Conversion Rate (%)', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-personalization-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-personalization-chart",
        "cards_title_1": "Personalization Architecture",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Sub-Second Real-Time Edge Processing</h4>
            <p>Evaluating incoming guest context at the CDN edge (Cloudflare/Akamai) to render personalized room hero banners before DOM load, preventing layout shift.</p>
          </div>
          <div class="dense-card">
            <h4>2. Dynamic Currency & Localized Payment Gateways</h4>
            <p>Presenting local currencies and native payment instruments (Alipay, WeChat Pay, KakaoPay, GrabPay, Apple Pay) boosts checkout completion by +31%.</p>
          </div>
          <div class="dense-card">
            <h4>3. Behavioral Exit-Intent Recovery</h4>
            <p>Detecting cursor drift towards close buttons with non-intrusive value guarantees (Best Rate Guarantee + Free Breakfast confirmation) to save 14% of abandoners.</p>
          </div>
        """,
        "cards_title_2": "Case Study & Commercial Metrics",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Frasers Hospitality Adobe Target Rollout</h4>
            <ul>
              <li><strong>Scope:</strong> Multi-market deployment across 70+ properties in APAC, EMEA, and UK.</li>
              <li><strong>Execution:</strong> Deployed Adobe Analytics and Adobe Target experimentation workflows across search and room selection funnels.</li>
              <li><strong>Result:</strong> <span class="metric-badge">Lifted overall website conversion from 0.68% to 2.25%</span> while reducing customer booking steps from 10 to 5.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Workshop Audit Topics</h4>
            <ul>
              <li>Auditing the 5 most common personalization friction points on Brand.com.</li>
              <li>Setting up automated price comparison widgets against OTAs directly on room detail pages.</li>
              <li>Designing the 30-day Adobe Target / Google Optimize migration playbook.</li>
            </ul>
          </div>
        """
    },
    # 07
    {
        "id": "ws07-guest-ltv-trevpar-optimization",
        "number": "07",
        "title": "GUEST LIFETIME VALUE & TREVPAR OPTIMIZATION",
        "subtitle": "Shifting Hotel Commercial Strategy from Single-Stay RevPAR to Multi-Year Total Guest Yield",
        "descriptor": "A quantitative executive masterclass on calculating true Guest LTV, total revenue per available room (TrevPAR), predictive churn probability, and VIP retention economics across multi-property hospitality portfolios.",
        "target": "Chief Commercial Officers, CFOs, Asset Managers, Revenue Directors, Marketing Heads",
        "framework": "The Total Guest Equity Model™",
        "mermaid": """graph TD
    A[Raw PMS Guest Transaction Log] --> B[Guest Value Stratification<br/>RFM Analysis: Recency, Frequency, Monetary]
    B --> C[Tier 1: High-Net-Worth VIPs<br/>Top 5% generate 38% Gross Margin]
    B --> D[Tier 2: Core Frequent Business<br/>Next 20% generate 42% Margin]
    B --> E[Tier 3: Transitory 1-Time OTA Bookers<br/>Bottom 75% generate 20% Margin]
    C --> F[Dedicated VIP Retention Desk &amp; Bespoke Privileges]
    D --> G[Automated B2B Repeat Stay Incentives]
    E --> H[First-Party Data Capture &amp; Direct Channel Conversion]
    F --> I[+310% Multi-Year LTV Realization]
    G --> I
    H --> I""",
        "plotly_script": """
          setTimeout(() => {
            const tiers = ['Top 5% (VIP Champions)', 'Next 20% (Core Frequent)', 'Next 25% (Occasional Direct)', 'Bottom 50% (1-Time OTA)'];
            const guestCount = [5, 20, 25, 50];
            const grossMarginContribution = [38, 42, 14, 6];

            const trace1 = { x: tiers, y: guestCount, name: '% of Guest Base', type: 'bar', marker: { color: '#64748B' } };
            const trace2 = { x: tiers, y: grossMarginContribution, name: '% of Total Portfolio Profit', type: 'bar', marker: { color: '#FBBF24' } };

            const layout = {
              barmode: 'group', paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'Percentage (%)', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.15 }
            };
            Plotly.newPlot('plotly-ltv-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-ltv-chart",
        "cards_title_1": "LTV & TrevPAR Calculation Models",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Total Revenue per Guest Formula</h4>
            <p>TrevPAR includes Total Room Rev + F&B + Spa + Ancillary divided by Total Available Rooms. Incorporating total on-property spend changes commercial prioritization.</p>
          </div>
          <div class="dense-card">
            <h4>2. Predictive Churn Triggers</h4>
            <p>If a corporate traveler who averages 12 nights/year has no reservations by day 120, automated alerts notify the account manager to intervene before account attrition.</p>
          </div>
          <div class="dense-card">
            <h4>3. Acquisition Cost Amortization</h4>
            <p>Spending S$120 CAC on a guest is ruinous for a single S$250 stay, but highly accretive if that guest returns 4 times over 24 months via Brand.com (S$1,000+ Net LTV).</p>
          </div>
        """,
        "cards_title_2": "Case Study & Executive Rubric",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Executive Portfolio Analysis</h4>
            <ul>
              <li><strong>Finding:</strong> 68% of marketing acquisition spend was allocated to acquiring low-margin, one-time OTA bookers who never returned.</li>
              <li><strong>Reallocation:</strong> Reinvested 40% of media budget into high-touch onboarding sequences and corporate loyalty perks.</li>
              <li><strong>Result:</strong> Boosted 24-month customer retention from 18% to 39%, generating <span class="metric-badge">+S$1.2M in annual net profit</span>.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Executive Questions for the Board</h4>
            <ul>
              <li>What is the exact LTV difference between a direct booker and an OTA booker across your properties?</li>
              <li>Do your property GMs have real-time visibility into the multi-year portfolio value of guests checking in today?</li>
            </ul>
          </div>
        """
    },
    # 08
    {
        "id": "ws08-hotel-loyalty-transformation",
        "number": "08",
        "title": "MODERNIZING HOTEL LOYALTY: MOVING BEYOND POINTS",
        "subtitle": "Restructuring Hospitality Loyalty Economics from Margin-Eroding Liabilities into Instant Direct Booking Drivers",
        "descriptor": "How independent hotels and regional hotel groups can dismantle archaic points-based programs and deploy modern instant-gratification loyalty mechanics that elevate direct bookings from 28% to 70%+.",
        "target": "Chief Executive Officers, Chief Commercial Officers, VP Loyalty, Directors of Marketing",
        "framework": "The Instant Gratification Loyalty Architecture™",
        "mermaid": """graph TD
    A[Guest Views Rate on Brand.com] --> B{Loyalty Value Proposition}
    B -->|Archaic Model: Earn 100 Points| C[Points Bank Liability<br/>Deferred reward in 18 months<br/>High Churn Rate]
    B -->|Modern Model: Instant Value| D[Instant Direct Recognition<br/>Guaranteed 10% Member Rate<br/>Free High-Speed WiFi<br/>Early Check-in Priority]
    C --> E[Guest Abandons to OTA for Convenience]
    D --> F[Immediate Direct Booking Conversion]
    F --> G[Direct Guest Relationship Captured]
    G --> H[Direct Loyalty Share Expands from 28% to 74%]""",
        "plotly_script": """
          setTimeout(() => {
            const channels = ['Direct Brand.com Member', 'Direct Non-Member', 'OTA (Expedia/Booking)', 'Wholesale / Bedbank'];
            const netContributionADR = [248, 215, 172, 145];
            const repeatStayProbability = [58, 22, 9, 4];

            const trace1 = { x: channels, y: netContributionADR, name: 'Net ADR Realization (S$)', type: 'bar', marker: { color: '#10B981' } };
            const trace2 = { x: channels, y: repeatStayProbability, name: 'Repeat Stay Rate (%)', type: 'scatter', mode: 'lines+markers', yaxis: 'y2', line: { color: '#FBBF24', width: 3 } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 50, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'Net ADR Realized (S$)', gridcolor: '#334155' },
              yaxis2: { title: 'Repeat Stay %', overlaying: 'y', side: 'right', range: [0, 100], showgrid: false },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-loyalty-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-loyalty-chart",
        "cards_title_1": "Loyalty Program Economics",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Eradicating Balance Sheet Liabilities</h4>
            <p>Traditional points programs accumulate significant unredeemed financial liabilities on hotel balance sheets. Instant reward programs eliminate accounting debt completely.</p>
          </div>
          <div class="dense-card">
            <h4>2. Zero-Friction Social Login Sign-Up</h4>
            <p>Replacing 15-field registration forms with 1-click Google/Apple ID sign-up directly inside the booking flow achieves 65%+ loyalty member conversion on first visit.</p>
          </div>
          <div class="dense-card">
            <h4>3. Experiential vs Discount Perks</h4>
            <p>Offering late check-out, welcome cocktails, and room upgrades costs the hotel minimal marginal cashflow while delivering perceived luxury value of S$80+ to the guest.</p>
          </div>
        """,
        "cards_title_2": "Case Study & Proven Growth",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Frasers Hospitality Global Loyalty Transformation</h4>
            <ul>
              <li><strong>Challenge:</strong> Direct channel loyalty penetration was stagnant at 28% of direct revenue, with high OTA leakage.</li>
              <li><strong>Restructuring:</strong> Overhauled the digital membership proposition around instant member rates, unified CDP recognition, and experiential rewards.</li>
              <li><strong>Outcome:</strong> <span class="metric-badge">Expanded loyalty contribution from 28% to 74% of direct bookings</span> over 36 months.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Diagnostic Action Items</h4>
            <ul>
              <li>Auditing the true cost per redeemed point across your current program.</li>
              <li>Establishing strict rate fences for closed-user-group (CUG) member rates.</li>
            </ul>
          </div>
        """
    },
    # 09
    {
        "id": "ws09-total-distribution-mix-brand-vs-ota",
        "number": "09",
        "title": "TOTAL DISTRIBUTION MIX: BALANCING BRAND.COM VS OTAS",
        "subtitle": "Deconstructing True Channel Acquisition Costs, Net ADR Realization, and Margin Leakage",
        "descriptor": "A rigorous financial workshop for hotel asset managers and commercial directors on auditing OTA commission structures, merchant models, and engineering a profitable direct distribution mix.",
        "target": "Asset Managers, Hotel Owners, Managing Directors, Director of Revenue Management (DORM)",
        "framework": "The Net Channel Contribution Matrix™",
        "mermaid": """graph TD
    A[Gross Booking Revenue: S$300] --> B{Channel Breakdown}
    B -->|Direct Brand.com| C[Tech + Merchant Cost: 4%<br/>Cost: S$12<br/>Net ADR: S$288]
    B -->|OTA Retail Model 18%| D[Commission: 18%<br/>Cost: S$54<br/>Net ADR: S$246]
    B -->|OTA Merchant / Package 25%| E[Margin Discount: 25%<br/>Cost: S$75<br/>Net ADR: S$225]
    B -->|Wholesale Bedbank 30%| F[Net Rate Discount: 30%<br/>Cost: S$90<br/>Net ADR: S$210]
    C --> G[Profit Contribution: +37% higher than Wholesale]
    D --> H[Margin Leakage to Third Parties]
    E --> H
    F --> H""",
        "plotly_script": """
          setTimeout(() => {
            const channels = ['Direct Brand.com', 'Corporate Negotiated', 'GHA Metasearch Direct', 'OTA Standard (18%)', 'OTA Preferred (22%)', 'Wholesaler (30%)'];
            const netADR = [288, 270, 262, 246, 234, 210];
            const channelShare = [32, 24, 8, 20, 10, 6];

            const trace1 = { x: channels, y: netADR, name: 'Net Realized ADR (S$)', type: 'bar', marker: { color: '#10B981' } };
            const trace2 = { x: channels, y: channelShare, name: 'Portfolio Volume Share (%)', type: 'scatter', mode: 'lines+markers', yaxis: 'y2', line: { color: '#FBBF24', width: 3 } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 50, l: 50, b: 60 }, font: { color: '#94A3B8', family: 'Inter', size: 10 },
              xaxis: { gridcolor: '#334155', tickangle: -15 }, yaxis: { title: 'Net ADR (S$)', gridcolor: '#334155' },
              yaxis2: { title: 'Volume Share %', overlaying: 'y', side: 'right', range: [0, 50], showgrid: false },
              legend: { orientation: 'h', y: 1.18, x: 0.1 }
            };
            Plotly.newPlot('plotly-dist-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-dist-chart",
        "cards_title_1": "Distribution Economics Principles",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. The Billboard Effect Myth vs Reality</h4>
            <p>While OTAs provide global discovery, relying on them for repeat domestic or corporate guests results in paying 18–25% commission on guests who already know your brand.</p>
          </div>
          <div class="dense-card">
            <h4>2. Dynamic Channel Inventory Shuttering</h4>
            <p>When high-demand compression dates exceed 80% occupancy, automatically closing high-cost OTA channels channels forces remaining demand into high-margin direct channels.</p>
          </div>
          <div class="dense-card">
            <h4>3. Comprehensive Cost-per-Acquisition (CPA)</h4>
            <p>Direct channel cost is never zero (hosting, payment gateway, brand media). Calculating the true fully-loaded CPA allows objective channel comparison.</p>
          </div>
        """,
        "cards_title_2": "Case Study & Owner Value",
        "cards_body_2": """
          <div class="dense-card">
            <h4>AccorHotels APAC Agency & Channel Consolidation</h4>
            <ul>
              <li><strong>Action:</strong> Consolidated decentralized agency operations across 13 APAC markets and 350+ properties.</li>
              <li><strong>Savings:</strong> Generated <span class="metric-badge">US$1.4M in annual recurring OpEx savings</span> while realigning direct acquisition economics.</li>
              <li><strong>Result:</strong> Boosted direct room-night production by +14% YoY across regional properties.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Asset Manager Checklist</h4>
            <ul>
              <li>Does your monthly P&L display Gross Revenue or Net Realized Revenue after distribution commissions?</li>
              <li>Are you paying override commissions to OTAs for volume during peak seasons when the hotel would sell out anyway?</li>
            </ul>
          </div>
        """
    },
    # 10
    {
        "id": "ws10-metasearch-bidding-economics",
        "number": "10",
        "title": "METASEARCH BIDDING ECONOMICS: GOOGLE HOTEL ADS & TRIPADVISOR",
        "subtitle": "Rate Parity Governance, Algorithmic Bidding Strategies, and Direct Acquisition at Lower Cost Than OTAs",
        "descriptor": "How to structure and govern profitable metasearch campaigns across Google Hotel Ads (GHA), TripAdvisor, and Trivago, winning top placement against OTAs while protecting profit margins.",
        "target": "Digital Marketing Directors, E-Commerce Managers, Revenue Managers, Performance Leads",
        "framework": "The Metasearch Parity & Bidding Engine™",
        "mermaid": """graph TD
    A[Guest Searches Hotel on Google Maps / Search] --> B{Google Hotel Ads Auction}
    B -->|OTA 1 Bid: CPC S$2.20| C[Booking.com Listed at S$250]
    B -->|OTA 2 Bid: CPC S$1.90| D[Agoda Listed at S$248 Parity Breach]
    B -->|Direct Brand.com Bid: CPS 10%| E[Official Hotel Site Listed at S$245 Member Rate]
    E --> F[Direct Rate Advantage Highlighted]
    F --> G[Guest Clicks Direct Official Link]
    G --> H[Direct Booking Secured at 10% Net Cost vs 20% OTA Commission]""",
        "plotly_script": """
          setTimeout(() => {
            const bidModels = ['Standard CPC (Manual)', 'Enhanced CPC (ML Bidding)', 'Commission per Stay (Pay-per-Stay)', 'Standard OTA (18% Flat)'];
            const effectiveCPA = [14.8, 9.2, 10.0, 18.0];
            const cancelAdjustedROAS = [6.8, 10.9, 10.0, 5.5];

            const trace1 = { x: bidModels, y: effectiveCPA, name: 'Effective Cost % of Revenue', type: 'bar', marker: { color: '#EF4444' } };
            const trace2 = { x: bidModels, y: cancelAdjustedROAS, name: 'ROAS Multiple (x)', type: 'scatter', mode: 'lines+markers', yaxis: 'y2', line: { color: '#10B981', width: 3 } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 50, l: 50, b: 60 }, font: { color: '#94A3B8', family: 'Inter', size: 10 },
              xaxis: { gridcolor: '#334155', tickangle: -10 }, yaxis: { title: 'Cost % of Booking', gridcolor: '#334155' },
              yaxis2: { title: 'ROAS Multiple (x)', overlaying: 'y', side: 'right', range: [0, 15], showgrid: false },
              legend: { orientation: 'h', y: 1.18, x: 0.1 }
            };
            Plotly.newPlot('plotly-meta-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-meta-chart",
        "cards_title_1": "Metasearch Mechanics",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Rate Parity as Bidding Pre-Condition</h4>
            <p>If an OTA is undercutting Brand.com by even $1, your metasearch click-through rate collapses by 65%. Automated parity monitoring must pause bids when out of parity.</p>
          </div>
          <div class="dense-card">
            <h4>2. Commission per Stay (CPS) De-Risking</h4>
            <p>Using Google Commissions (Pay-per-Stay) eliminates financial risk on guest cancellations and no-shows, guaranteeing a predictable 10–12% acquisition cost.</p>
          </div>
          <div class="dense-card">
            <h4>3. Free Booking Links Optimization</h4>
            <p>Google offers organic Free Booking Links below the paid auction. Ensuring accurate XML price feed connectivity captures zero-cost direct room nights.</p>
          </div>
        """,
        "cards_title_2": "TripAdvisor & APAC History",
        "cards_body_2": """
          <div class="dense-card">
            <h4>TripAdvisor APAC & ML Bidding Leadership</h4>
            <ul>
              <li><strong>Background:</strong> Inaugural digital hire establishing acquisition infrastructure across 10 APAC territories.</li>
              <li><strong>Engineering Collab:</strong> Partnered with HQ engineering teams to translate commercial optimization logic into an automated ML-based algorithmic bidding engine.</li>
              <li><strong>Impact:</strong> Scaled regional acquisition efficiency while querying large-scale SQL datasets for competitive benchmarking.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Operational Playbook</h4>
            <ul>
              <li>Configuring ARI (Availability, Rates, Inventory) XML cache feeds.</li>
              <li>Setting up multiplier bid rules by device, length of stay, and country.</li>
            </ul>
          </div>
        """
    },
    # 11
    {
        "id": "ws11-corporate-mice-demand-digitization",
        "number": "11",
        "title": "CORPORATE & MICE DEMAND DIGITIZATION",
        "subtitle": "Automating Group RFPs, Negotiated Rate Portals, and API-Driven B2B2C Hospitality Sales",
        "descriptor": "How modern hotels transform sluggish manual sales inquiries into automated instant corporate booking engines, digital voucher ecosystems, and API partner integrations.",
        "target": "Director of Sales (DOS), Director of MICE, Chief Commercial Officers, Revenue Directors",
        "framework": "The B2B2C Hospitality Automation Pipeline™",
        "mermaid": """graph LR
    A[Corporate Travel Manager / Meeting Planner] --> B{B2B Digital Booking Portal}
    B -->|Contracted Negotiated Rate| C[Instant 1-Click Corporate Booking]
    B -->|Group / Meeting RFP Request| D[Automated Meeting Yield Engine<br/>Checks Room Block + F&amp;B Minimum]
    B -->|Digital Incentive Vouchers| E[API Voucher Distribution Engine<br/>Mezzofy Platform Integration]
    C --> F[Direct PMS Confirmation &amp; Folio Billing]
    D --> G[Dynamic Custom PDF Proposal in 3 Minutes]
    E --> H[Corporate Employee Self-Service Redemption]
    F --> I[Zero GDS Switch Fee Leakage]
    G --> J[+45% RFP Conversion Velocity]
    H --> K[Incremental High-Margin F&amp;B Spend]""",
        "plotly_script": """
          setTimeout(() => {
            const processStages = ['RFP Received to Proposal Sent', 'Contract Finalization', 'Direct Corporate Booking Time', 'Group Block Invoicing', 'Voucher Distribution'];
            const legacyManualHours = [48, 72, 8, 24, 16];
            const digitalAutomatedHours = [0.1, 4.0, 0.05, 1.0, 0.01];

            const trace1 = { x: processStages, y: legacyManualHours, name: 'Traditional Sales Operations (Hours)', type: 'bar', marker: { color: '#EF4444' } };
            const trace2 = { x: processStages, y: digitalAutomatedHours, name: 'Digital B2B Automation (Hours)', type: 'bar', marker: { color: '#10B981' } };

            const layout = {
              barmode: 'group', paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 60 }, font: { color: '#94A3B8', family: 'Inter', size: 10 },
              xaxis: { gridcolor: '#334155', tickangle: -10 }, yaxis: { title: 'Elapsed Time (Hours)', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-b2b-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-b2b-chart",
        "cards_title_1": "B2B Digitization Pillars",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Dynamic Negotiated Rate Access</h4>
            <p>Providing corporate travel managers with secure, customized company portals where agreed rates are loaded in real-time, eliminating manual email bookings.</p>
          </div>
          <div class="dense-card">
            <h4>2. API-Driven Voucher Commercialization</h4>
            <p>Deploying API voucher platforms (such as Mezzofy) enables hospitality brands to sell corporate gifting packages, dining vouchers, and suite stays directly to MNCs.</p>
          </div>
          <div class="dense-card">
            <h4>3. Automated Event Space Yielding</h4>
            <p>Meeting rooms are perishable inventory. Automated systems price MICE space based on expected delegate headcount, catering spend, and bedroom pickup.</p>
          </div>
        """,
        "cards_title_2": "Case Study & B2B Outcomes",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Mezzofy & Enterprise Hospitality Integration</h4>
            <ul>
              <li><strong>Platform:</strong> API-driven digital voucher and distribution platform connecting corporate demand directly to hotel merchant systems.</li>
              <li><strong>Result:</strong> Reduced administrative settlement overhead by 80% while creating high-velocity direct corporate incentive channels.</li>
              <li><strong>Impact:</strong> Enabled 300+ corporate clients to issue digital staycation and dining rewards seamlessly.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Corporate Sales Audit Questions</h4>
            <ul>
              <li>What percentage of your corporate contracted clients still book via phone or unencrypted email spreadsheets?</li>
              <li>Do you offer API-connected booking tools for travel management companies (TMCs)?</li>
            </ul>
          </div>
        """
    },
    # 12
    {
        "id": "ws12-wholesaler-governance-rate-leakage",
        "number": "12",
        "title": "WHOLESALER GOVERNANCE & RATE LEAKAGE PREVENTION",
        "subtitle": "Auditing Bedbanks, Ending Rogue OTA Undercutting, and Protecting Direct Price Integrity",
        "descriptor": "A diagnostic masterclass on auditing static wholesale contracts, tracing unauthorized unbundled bedbank inventory to rogue OTAs, and enforcing strict dynamic rate distribution agreements.",
        "target": "General Managers, Asset Owners, Commercial VPs, Revenue Directors",
        "framework": "The Anti-Leakage Distribution Firewall™",
        "mermaid": """graph TD
    A[Hotel Issues 30% Wholesale Discount<br/>Intended for Bundled Flight+Hotel Package] --> B[Wholesaler / Bedbank<br/>Hotelbeds, WebBeds, GTA]
    B -->|Unlawful Unbundling of Standalone Room| C[B2B Rate Aggregator Switch]
    C -->|Feed Injected into Rogue Online Sellers| D[Rogue OTAs / Trip.com / Amoma clones]
    D -->|Listed Publicly on Google Metasearch| E[Undercuts Hotel Official Rate by $35]
    E --> F[Brand.com Direct Conversion Collapses by 60%]
    E --> G[Hotel Pays Wholesaler 30% Margin on Direct Booker Cannibalization]
    F --> H[Demand Journeys Audit: Test Booking &amp; Distributor Code Trace]
    H --> I[Contract Breach Notice &amp; Dynamic API Rate Transition]""",
        "plotly_script": """
          setTimeout(() => {
            const months = ['Month 1 (Audit)', 'Month 2 (Tracing)', 'Month 3 (Enforcement)', 'Month 4 (Dynamic API)', 'Month 5 (Controlled)'];
            const rateDiscrepancyIncidents = [142, 118, 42, 12, 3];
            const directBrandConversion = [0.72, 0.88, 1.45, 1.95, 2.30];

            const trace1 = { x: months, y: rateDiscrepancyIncidents, name: 'Monthly Parity Breaches Detected', type: 'bar', marker: { color: '#EF4444' } };
            const trace2 = { x: months, y: directBrandConversion, name: 'Brand.com Direct Conversion (%)', type: 'scatter', mode: 'lines+markers', yaxis: 'y2', line: { color: '#10B981', width: 3 } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 50, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'Parity Breach Incidents', gridcolor: '#334155' },
              yaxis2: { title: 'Brand.com Conversion %', overlaying: 'y', side: 'right', range: [0, 3], showgrid: false },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-leakage-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-leakage-chart",
        "cards_title_1": "Wholesale Governance Protocol",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Mystery Test-Booking Trace Protocol</h4>
            <p>Executing live test bookings on undercutting OTAs to extract the specific 8-digit booking voucher identifier, pinning the exact wholesaler distributor in breach.</p>
          </div>
          <div class="dense-card">
            <h4>2. Transitioning from Static to Dynamic Net Rates</h4>
            <p>Eliminating static contracted allotments. Wholesale partners must connect via dynamic APIs with contracted maximum discount caps linked directly to BAR.</p>
          </div>
          <div class="dense-card">
            <h4>3. Strict Non-Opaque Package Clauses</h4>
            <p>Inserting strict contractual penalties into bedbank agreements that forfeit distribution rights if rooms are distributed without dynamic flight bundling.</p>
          </div>
        """,
        "cards_title_2": "Financial Recovery & Impact",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Frasers Hospitality Commission Protection</h4>
            <ul>
              <li><strong>Challenge:</strong> Rogue third-party aggregators were displaying unbundled wholesale rates across metasearch, eroding direct booking integrity.</li>
              <li><strong>Action:</strong> Implemented systematic parity audits, test bookings, and restructured wholesale agreements to dynamic API models.</li>
              <li><strong>Result:</strong> Generated <span class="metric-badge">Approx. S$550K in annual commission savings</span> while boosting direct web ADR by +18%.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Audit Readiness Checklist</h4>
            <ul>
              <li>Do your wholesale contracts allow third-party B2B onward redistribution?</li>
              <li>When was the last time your team audited meta rates across European and North Asian IPs?</li>
            </ul>
          </div>
        """
    },
    # 13
    {
        "id": "ws13-marketing-mix-modeling-mmm-hotels",
        "number": "13",
        "title": "MARKETING MIX MODELING (MMM) FOR HOTEL GROUPS",
        "subtitle": "Econometric Measurement, Adstock Decay, and Multi-Market Capital Allocation Without Attribution Bias",
        "descriptor": "A top-down econometric masterclass for hospitality executives on measuring the true offline and online media contribution, channel saturation thresholds, and optimal cross-market marketing budget allocation.",
        "target": "Chief Marketing Officers, CFOs, Commercial Directors, Regional Marketing Leads",
        "framework": "The Hospitality Econometric MMM Framework™",
        "mermaid": """graph TD
    A[Marketing Spend Inputs<br/>Search, Meta, Social, PR, OOH, Sponsorships] --> E{Econometric Regression Engine}
    B[Exogenous Macro Variables<br/>Aviation Capacity, FX Rates, Seasonality] --> E
    C[Internal Property Variables<br/>Pricing, RevPAR Index, CompSet Rates] --> E
    D[Adstock Decay &amp; Diminishing Returns Curves] --> E
    E --> F[Decomposed Revenue Contribution by Channel]
    F --> G[Marginal Return on Ad Spend (mROAS) by Market]
    G --> H[Optimal Budget Reallocation Across 13 APAC Markets]
    H --> I[+20% Baseline Marketing Efficiency Gain]""",
        "plotly_script": """
          setTimeout(() => {
            const spendLevels = ['S$10K', 'S$25K', 'S$50K', 'S$75K', 'S$100K', 'S$150K', 'S$200K'];
            const searchRevenue = [80, 180, 310, 390, 430, 460, 470];
            const metaRevenue = [90, 210, 380, 510, 600, 680, 710];
            const brandSocial = [20, 60, 140, 240, 350, 480, 560];

            const trace1 = { x: spendLevels, y: searchRevenue, name: 'Paid Brand Search (Early Saturation)', type: 'scatter', mode: 'lines+markers', line: { color: '#EF4444', width: 3 } };
            const trace2 = { x: spendLevels, y: metaRevenue, name: 'Google Hotel Ads (High Linear Yield)', type: 'scatter', mode: 'lines+markers', line: { color: '#10B981', width: 3 } };
            const trace3 = { x: spendLevels, y: brandSocial, name: 'Video / Social Brand (Delayed Adstock)', type: 'scatter', mode: 'lines+markers', line: { color: '#FBBF24', width: 3 } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { title: 'Monthly Channel Spend', gridcolor: '#334155' }, yaxis: { title: 'Incremental Room Revenue (S$k)', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.05 }
            };
            Plotly.newPlot('plotly-mmm-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-mmm-chart",
        "cards_title_1": "MMM Econometric Core",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Overcoming Digital Last-Click Bias</h4>
            <p>Last-click digital attribution over-rewards brand paid search (taking credit for guests already intending to book) while under-valuing upper-funnel PR and brand campaigns.</p>
          </div>
          <div class="dense-card">
            <h4>2. Calculating Adstock Half-Life Decay</h4>
            <p>Luxury travel decisions have a 45–90 day booking window. Modeling the half-life decay of advertising awareness ensures marketing capital is timed ahead of seasonal booking surges.</p>
          </div>
          <div class="dense-card">
            <h4>3. Diminishing Marginal Returns Curves</h4>
            <p>Identifying the exact spend threshold where each additional marketing dollar generates less than $1 in incremental gross operating profit, preventing media waste.</p>
          </div>
        """,
        "cards_title_2": "Credentials & Executive Results",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Practical Multi-Market MMM Application</h4>
            <ul>
              <li><strong>Credential:</strong> Fundamentals of Marketing Mix Modeling certification (Udemy ID: UC-532c8e2b-7345-4113-9cff-90d39802d545).</li>
              <li><strong>Execution:</strong> Applied Excel-based econometric modeling and regression analysis to optimize media budgets across 70+ properties.</li>
              <li><strong>Impact:</strong> Reallocated US$15M regional media spend, reducing wasted ad spend by 22% while accelerating direct room nights.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Executive Questions for CMOs</h4>
            <ul>
              <li>What is your marginal return on advertising spend (mROAS) on your final $100,000 of digital budget?</li>
              <li>How much of your reported Google Ads revenue would have occurred organically without ad spend?</li>
            </ul>
          </div>
        """
    },
    # 14
    {
        "id": "ws14-media-incrementality-geo-testing",
        "number": "14",
        "title": "MEDIA INCREMENTALITY & GEO-TESTING IN HOSPITALITY",
        "subtitle": "Eliminating Brand Search Cannibalization, Setting Up Ghost Bids, and Measuring True Media Lift",
        "descriptor": "A practical experimental design workshop for commercial leaders on setting up matched-market geo-holdout tests to verify whether digital advertising generates incremental room nights or merely taxes existing demand.",
        "target": "VP Marketing, Heads of Growth, Performance Marketing Leads, Asset Analysts",
        "framework": "The Matched-Market Incrementality Testing Framework™",
        "mermaid": """graph TD
    A[Total Portfolio Markets: 20 Geographies] --> B[Synthetic Control Matching<br/>Pairing statistically identical markets by booking velocity]
    B --> C[Control Group: 10 Geographies<br/>0% Paid Brand Search Spend]
    B --> D[Treatment Group: 10 Geographies<br/>100% Paid Brand Search Spend]
    C --> E[Measure Total Direct Bookings: Organic + Paid]
    D --> F[Measure Total Direct Bookings: Organic + Paid]
    E --> G{Calculate Incremental Lift}
    F --> G
    G -->|Case 1: No Statistical Difference| H[Brand Cannibalization Proven: Cut Paid Spend]
    G -->|Case 2: Statistically Significant Lift| I[True Incrementality Confirmed: Scale Spend]""",
        "plotly_script": """
          setTimeout(() => {
            const weeks = ['W1 (Baseline)', 'W2 (Baseline)', 'W3 (Test Start)', 'W4 (Holdout)', 'W5 (Holdout)', 'W6 (Holdout)', 'W7 (Post-Test)'];
            const treatmentMarket = [100, 104, 108, 112, 115, 118, 116];
            const controlMarket = [98, 102, 105, 109, 111, 114, 112];
            const adSpendTreatment = [5000, 5000, 5000, 5000, 5000, 5000, 5000];

            const trace1 = { x: weeks, y: treatmentMarket, name: 'Treatment Market (Ads Active)', type: 'scatter', mode: 'lines+markers', line: { color: '#10B981', width: 3 } };
            const trace2 = { x: weeks, y: controlMarket, name: 'Control Market (Zero Ads)', type: 'scatter', mode: 'lines+markers', line: { color: '#EF4444', width: 3, dash: 'dash' } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'Indexed Direct Room Bookings', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-inc-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-inc-chart",
        "cards_title_1": "Incrementality Testing Methodologies",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Matched-Market Geo-Testing</h4>
            <p>Pairing geographic territories (e.g. Sydney vs Melbourne, or Singapore vs Hong Kong) based on historical booking correlation, pausing ads in one while holding the other constant.</p>
          </div>
          <div class="dense-card">
            <h4>2. Ghost Bidding & PSA Holdouts</h4>
            <p>Simulating ad auctions to log when ads would have won without serving them, measuring conversion differences between exposed and unexposed audiences.</p>
          </div>
          <div class="dense-card">
            <h4>3. Retargeting Cannibalization Audits</h4>
            <p>Standard retargeting often serves ads to guests who were already in the final checkout flow, claiming artificial 1000%+ ROAS while providing zero incremental lift.</p>
          </div>
        """,
        "cards_title_2": "HomeAway / Expedia Experience",
        "cards_body_2": """
          <div class="dense-card">
            <h4>HomeAway / VRBO APAC Performance Leadership</h4>
            <ul>
              <li><strong>Scale:</strong> Managed US$15M annual media portfolio across 7 APAC markets with an 8-member regional team.</li>
              <li><strong>Data Science Collab:</strong> Partnered with data science and engineering teams on experimental design, holdouts, geo-testing, and spend forecasting.</li>
              <li><strong>Outcome:</strong> Scaled Japan from zero to US$3M annual revenue within 12 months through localized acquisition strategy.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Practical Workshop Deliverables</h4>
            <ul>
              <li>Step-by-step statistical power calculator for hotel geo-tests.</li>
              <li>Brand Search Defense vs Elimination decision tree.</li>
            </ul>
          </div>
        """
    },
    # 15
    {
        "id": "ws15-hotel-digital-unit-economics-mer",
        "number": "15",
        "title": "HOTEL DIGITAL MARKETING UNIT ECONOMICS: CAC & MER",
        "subtitle": "Setting Rigorous Marketing Efficiency Ratios, Cost per Acquisition Caps, and Booking Payback Curves",
        "descriptor": "How hotel CFOs and commercial directors eliminate vanity metrics (impressions, clicks, ROAS) and establish strict unit-economic guardrails linking every digital marketing dollar to GOPPAR and EBITDA.",
        "target": "Chief Financial Officers, Asset Managers, General Managers, VP Marketing",
        "framework": "The Hotel Unit Economics Financial Guardrail™",
        "mermaid": """graph TD
    A[Total Digital Marketing Spend: S$100,000] --> B{Calculate Marketing Efficiency Ratio MER}
    B -->|Direct Brand.com Revenue: S$1,000,000| C[MER = 10.0x / Blended Cost 10%]
    C --> D[Fully-Loaded Customer Acquisition Cost CAC]
    D --> E[Room Night Production: 4,000 Nights]
    E --> F[Blended CAC per Room Night = S$25]
    F --> G{Compare Against Channel Alternatives}
    G -->|Direct CAC S$25 on S$250 ADR = 10%| H[Accretive: Outperforms 18% OTA Commission]
    G -->|Direct CAC S$60 on S$250 ADR = 24%| I[Dilutive: Underperforms OTA Commission - Immediate Intervention]""",
        "plotly_script": """
          setTimeout(() => {
            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'];
            const directCAC = [32, 28, 24, 22, 21, 19, 18, 17];
            const otaEffectiveCAC = [45, 45, 45, 45, 45, 45, 45, 45];
            const directRevenueShare = [22, 26, 31, 38, 44, 49, 52, 56];

            const trace1 = { x: months, y: directCAC, name: 'Direct Channel CAC per Booking (S$)', type: 'scatter', mode: 'lines+markers', line: { color: '#10B981', width: 3 } };
            const trace2 = { x: months, y: otaEffectiveCAC, name: '18% OTA Commission Benchmark (S$)', type: 'scatter', mode: 'lines', line: { color: '#EF4444', width: 2, dash: 'dot' } };
            const trace3 = { x: months, y: directRevenueShare, name: 'Direct Booking Revenue Share %', type: 'bar', yaxis: 'y2', opacity: 0.3, marker: { color: '#FBBF24' } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 50, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'Cost per Acquisition (S$)', gridcolor: '#334155' },
              yaxis2: { title: 'Direct Share %', overlaying: 'y', side: 'right', range: [0, 100], showgrid: false },
              legend: { orientation: 'h', y: 1.15, x: 0.05 }
            };
            Plotly.newPlot('plotly-mer-chart', [trace1, trace2, trace3], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-mer-chart",
        "cards_title_1": "Unit Economic Financial Metrics",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Marketing Efficiency Ratio (MER)</h4>
            <p>$$\\text{MER} = \\frac{\\text{Total Direct Digital Room Revenue}}{\\text{Total Fully-Loaded Marketing Spend}}$$ A healthy luxury hotel portfolio target is 8.0x–12.0x MER.</p>
          </div>
          <div class="dense-card">
            <h4>2. Fully-Loaded Acquisition Cost</h4>
            <p>Must include agency retainers, technology platform SaaS fees, metasearch commissions, and creative asset production—not just media ad spend.</p>
          </div>
          <div class="dense-card">
            <h4>3. Cashflow Payback Velocity</h4>
            <p>Tracking the exact lag between media cash outflow and guest deposit realization, ensuring marketing expansion does not strain property operating cashflow.</p>
          </div>
        """,
        "cards_title_2": "Case Study & Financial Results",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Dell APACJ & GroupM Governance Case</h4>
            <ul>
              <li><strong>Scope:</strong> Managed an 8-market APACJ digital acquisition portfolio across complex multi-currency commercial structures.</li>
              <li><strong>Governance:</strong> Implemented strict unit economic acquisition thresholds and bidding guardrails.</li>
              <li><strong>Result:</strong> Drove a <span class="metric-badge">20% baseline acquisition efficiency improvement</span> across the regional portfolio.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>CFO Audit Framework</h4>
            <ul>
              <li>Setting monthly property-level CAC caps based on seasonal room ADR.</li>
              <li>Designing executive compensation incentives tied to Net Revenue after acquisition costs.</li>
            </ul>
          </div>
        """
    },
    # 16
    {
        "id": "ws16-csuite-commercial-dashboards-powerbi",
        "number": "16",
        "title": "C-SUITE COMMERCIAL DASHBOARDS: POWER BI FOR GMS & OWNERS",
        "subtitle": "Synthesizing Multi-Market Commercial Data, Channel Attribution, and RevPAR into Decision-Ready Executive Intelligence",
        "descriptor": "How to design, architect, and deploy automated Power BI executive reporting that eliminates manual weekly reporting and provides Board members with transparent commercial decision velocity.",
        "target": "General Managers, Asset Owners, Chief Financial Officers, Commercial Directors",
        "framework": "The C-Suite Decision Cockpit Architecture™",
        "mermaid": """graph TD
    A[Property PMS Feeds] --> E{Automated SQL &amp; Power BI Semantic Model}
    B[CRS &amp; Channel Manager Feeds] --> E
    C[Digital Marketing &amp; Metasearch APIs] --> E
    D[Financial Accounting &amp; Payroll] --> E
    E --> F[Board &amp; ExCo Executive Summary<br/>RevPAR Index, GOPPAR, Direct Mix %]
    E --> G[General Manager Operational Cockpit<br/>Daily Pace, Pickup, Parity Alerts]
    E --> H[Commercial &amp; Revenue Action Dashboard<br/>Channel CPA, Net ADR Realization]
    F --> I[Faster Capital Allocation &amp; Strategic Decision Velocity]
    G --> I
    H --> I""",
        "plotly_script": """
          setTimeout(() => {
            const properties = ['Property A (SG)', 'Property B (Tokyo)', 'Property C (London)', 'Property D (Sydney)', 'Property E (Paris)'];
            const revPARIndex = [118, 124, 108, 114, 122];
            const directChannelShare = [68, 54, 72, 61, 58];
            const gopparMargin = [42, 46, 38, 41, 44];

            const trace1 = { x: properties, y: revPARIndex, name: 'RevPAR Index (CompSet Benchmark = 100)', type: 'bar', marker: { color: '#10B981' } };
            const trace2 = { x: properties, y: directChannelShare, name: 'Direct Revenue Mix (%)', type: 'scatter', mode: 'lines+markers', yaxis: 'y2', line: { color: '#FBBF24', width: 3 } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 50, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'RevPAR Index', gridcolor: '#334155' },
              yaxis2: { title: 'Direct Mix %', overlaying: 'y', side: 'right', range: [0, 100], showgrid: false },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-pbi-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-pbi-chart",
        "cards_title_1": "Dashboard Architecture Standards",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Single Source of Truth Semantic Layer</h4>
            <p>Ingesting raw SQL data models to establish uniform KPI definitions (e.g. Net ADR, Direct Booking %, Pickup) across all properties in the portfolio.</p>
          </div>
          <div class="dense-card">
            <h4>2. Exception-Based Executive Alerting</h4>
            <p>Automated push notifications trigger when forward pace drops 10% below budget or when OTA share spikes unexpectedly on a high-demand date.</p>
          </div>
          <div class="dense-card">
            <h4>3. Mobile-Optimized Executive View</h4>
            <p>Designing thumb-friendly Power BI mobile layouts allowing GMs and Asset Managers to review live morning figures in under 60 seconds.</p>
          </div>
        """,
        "cards_title_2": "Frasers Hospitality Leadership",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Global Power BI Dashboard Deployment</h4>
            <ul>
              <li><strong>Scope:</strong> Multi-market executive reporting across 70+ properties, synthesizing US$50M+ direct channel data.</li>
              <li><strong>Execution:</strong> Developed custom Power BI dashboards translating complex digital and commercial performance data into actionable insights for ExCo and Board.</li>
              <li><strong>Result:</strong> Reduced monthly commercial reporting preparation time by 85% while accelerating yield decisions.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Workshop Takeaway Assets</h4>
            <ul>
              <li>The 5 Core C-Suite Power BI Dashboard Wireframe Templates.</li>
              <li>SQL Data Schema for Automated PMS and Channel Manager Ingestion.</li>
            </ul>
          </div>
        """
    },
    # 17
    {
        "id": "ws17-hotel-booking-engine-cro-funnel",
        "number": "17",
        "title": "HOTEL BOOKING ENGINE OPTIMIZATION: 10 TO 5 STEPS",
        "subtitle": "Eliminating Friction, Mobile Acceleration (<3.0s), and Room-Rate Merchandising Psychology",
        "descriptor": "A granular digital product masterclass on re-architecting hotel booking funnels, eliminating abandoned checkout steps, speeding up mobile load times, and optimizing direct conversion rates.",
        "target": "Digital Product Managers, E-Commerce Leads, UX Designers, VP Digital",
        "framework": "The 5-Step Frictionless Reservation Funnel™",
        "mermaid": """graph TD
    A[Legacy 10-Step Funnel<br/>Drop-off Rate: 99.32% | Conversion: 0.68%] --> B[1. Property Search]
    B --> C[2. Date Picker Clutter]
    C --> D[3. 15 Confusing Rate Plans]
    D --> E[4. Add-on Upsell Wall]
    E --> F[5. Mandatory 18-Field Form]
    F --> G[6. Payment Gateway Redirect]
    G --> H[7. Slow Page Reload (7.1s)]
    
    I[Modern 5-Step Frictionless Funnel<br/>Drop-off Rate: 97.75% | Conversion: 2.25%] --> J[1. Seamless Search &amp; Auto-Dates]
    J --> K[2. Clear 3-Tier Room Merchandising]
    K --> L[3. 1-Click Social / Google Login]
    L --> M[4. Apple Pay / Local Fast Checkout]
    M --> N[5. Instant Sub-3.0s Confirmation (+230% Lift)]""",
        "plotly_script": """
          setTimeout(() => {
            const steps = ['Step 1: Room Search', 'Step 2: Room Selection', 'Step 3: Guest Details', 'Step 4: Payment Info', 'Step 5: Confirmation'];
            const legacyDropoff = [100, 32, 14, 4.2, 0.68];
            const optimizedDropoff = [100, 58, 36, 18.5, 2.25];

            const trace1 = { x: steps, y: legacyDropoff, name: 'Legacy 10-Step Booking Funnel (%)', type: 'scatter', mode: 'lines+markers', line: { color: '#EF4444', width: 3 } };
            const trace2 = { x: steps, y: optimizedDropoff, name: 'Optimized 5-Step Frictionless Engine (%)', type: 'scatter', mode: 'lines+markers', line: { color: '#10B981', width: 4 } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: '% of Visitors Remaining in Funnel', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-funnel-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-funnel-chart",
        "cards_title_1": "Frictionless UX Principles",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Mobile Performance Acceleration</h4>
            <p>Every 1-second delay in mobile booking page load decreases conversion by 12%. Reducing mobile load times from 7.1s to 3.0s creates an immediate revenue lift.</p>
          </div>
          <div class="dense-card">
            <h4>2. Eliminating Rate Plan Choice Paralysis</h4>
            <p>Presenting 12 rate plans (Room Only, B&B, Non-Ref, Advance Saver, Stay-3, Package) overwhelms guests. Grouping into 3 clear tabs increases room selection velocity.</p>
          </div>
          <div class="dense-card">
            <h4>3. Native Digital Wallet Integration</h4>
            <p>Integrating Apple Pay and Google Pay eliminates manual credit card number typing on mobile devices, capturing impulse bookers seamlessly.</p>
          </div>
        """,
        "cards_title_2": "Proven Platform Impact",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Frasers Hospitality Enterprise Booking Re-Platforming</h4>
            <ul>
              <li><strong>Baseline:</strong> 0.68% conversion, 10 booking steps, 7.1s mobile load time.</li>
              <li><strong>Transformation:</strong> Re-architected direct digital booking path with Sabre and Adobe Target, cutting steps from 10 to 5 and mobile load time to 3.0s.</li>
              <li><strong>Outcome:</strong> <span class="metric-badge">Delivered 2.25% conversion (+230% lift)</span> and +56% YoY direct room-night growth.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>CRO Audit Checklist</h4>
            <ul>
              <li>How many required form fields does your mobile checkout demand? (Target: ≤ 4).</li>
              <li>Does your booking engine force guests to navigate to an external domain?</li>
            </ul>
          </div>
        """
    },
    # 18
    {
        "id": "ws18-high-velocity-ab-testing-hotels",
        "number": "18",
        "title": "HIGH-VELOCITY A/B TESTING FOR HOTEL ASSETS",
        "subtitle": "Structuring Scientific Experimentation Roadmaps, Urgency Triggers, and Room Merchandising",
        "descriptor": "How hotel commercial teams design, run, and scale high-velocity A/B testing programs across Brand.com to systematically increase conversion rates and average booking value.",
        "target": "E-Commerce Managers, CRO Specialists, VP Digital, Marketing Directors",
        "framework": "The Scientific Hospitality Testing Cycle™",
        "mermaid": """graph LR
    A[Data Audit: Funnel Analytics Drop-off] --> B[Behavioral Hypothesis Formulation]
    B --> C[Experiment Design &amp; Statistical Power Calculation]
    C --> D{Run A/B Test in Adobe Target / Optimizely}
    D -->|Variant A: Control (Standard Rate Grid)| E[Measure Conversion &amp; ADR]
    D -->|Variant B: Dynamic Urgency + Room Upgrade Bundle| F[Measure Conversion &amp; ADR]
    E --> G[Statistical Significance Check (p < 0.05)]
    F --> G
    G -->|Winner Confirmed| H[Permanent Production Rollout]
    G -->|No Lift| I[Archive Learning &amp; Iterate Hypothesis]""",
        "plotly_script": """
          setTimeout(() => {
            const experiments = ['Room Photo Hierarchy', 'Best Rate Guarantee Badge', 'Cancellation Policy Clarity', 'Instant Member Pricing Banner', 'Room Upgrade Merchandising'];
            const baselineConv = [1.10, 1.15, 1.25, 1.30, 1.45];
            const winningConv = [1.32, 1.40, 1.58, 1.82, 2.15];

            const trace1 = { x: experiments, y: baselineConv, name: 'Control (Baseline %)', type: 'bar', marker: { color: '#64748B' } };
            const trace2 = { x: experiments, y: winningConv, name: 'Winning Variant (%)', type: 'bar', marker: { color: '#10B981' } };

            const layout = {
              barmode: 'group', paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 60 }, font: { color: '#94A3B8', family: 'Inter', size: 10 },
              xaxis: { gridcolor: '#334155', tickangle: -10 }, yaxis: { title: 'Conversion Rate (%)', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.18, x: 0.1 }
            };
            Plotly.newPlot('plotly-ab-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-ab-chart",
        "cards_title_1": "Experimentation Protocols",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Statistical Power & Sample Sizing</h4>
            <p>Running tests without sufficient sample size leads to false positives. Calculating minimum detectable effects (MDE) ensures high confidence before declaring winners.</p>
          </div>
          <div class="dense-card">
            <h4>2. Authentic vs Artificial Urgency</h4>
            <p>Fake countdown timers damage luxury brand credibility. Real-time authentic inventory flags ("Only 2 suites remaining for your dates") drive high-trust conversion.</p>
          </div>
          <div class="dense-card">
            <h4>3. Room Image Sequencing Tests</h4>
            <p>Testing bathroom photo prominence vs bedroom lifestyle views reveals that luxury guests prioritize bathroom finish quality more than standard bedding shots.</p>
          </div>
        """,
        "cards_title_2": "Case Study & Program Results",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Multi-Property A/B Testing Program</h4>
            <ul>
              <li><strong>Cadence:</strong> Executed 24 structured A/B tests over 12 months across global booking paths.</li>
              <li><strong>Top Win:</strong> Restructuring the room upgrade step during checkout lifted average booking value by <span class="metric-badge">+S$42 per reservation</span>.</li>
              <li><strong>Impact:</strong> Cumulative conversion improvements accounted for +28% of overall direct revenue expansion.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Workshop Playbook</h4>
            <ul>
              <li>The 20 High-Impact Hotel Booking Engine A/B Testing Ideas.</li>
              <li>Statistical Significance & Sample Size Calculator in Excel/Google Sheets.</li>
            </ul>
          </div>
        """
    },
    # 19
    {
        "id": "ws19-hotel-tech-stack-vendor-rfp",
        "number": "19",
        "title": "HOTEL TECH STACK EVALUATION & VENDOR RFP GOVERNANCE",
        "subtitle": "Navigating PMS, CRS, Booking Engines, CDP and Channel Managers Without Accumulating Technical Debt",
        "descriptor": "A comprehensive procurement and architecture guide for hospitality leaders on structuring vendor evaluation scorecards, calculating total cost of ownership (TCO), and avoiding vendor lock-in.",
        "target": "Chief Information Officers, Chief Commercial Officers, Asset Managers, Procurement Leads",
        "framework": "The Hospitality Enterprise Tech Evaluation Matrix™",
        "mermaid": """graph TD
    A[Business Strategy &amp; Commercial Growth Requirements] --> B[Technical Architecture Blueprint]
    B --> C{Structured Vendor RFP Process}
    C -->|PMS Core: Opera Cloud vs Infor vs Cloudbeds| D[Property Operations &amp; Folio Billing]
    C -->|CRS &amp; Booking: Sabre SynXis vs Amadeus vs TravelClick| E[Central Distribution &amp; ARI]
    C -->|CDP &amp; CRM: Adobe AEP vs Salesforce vs Cendyn| F[Guest Intelligence &amp; Personalization]
    D --> G[Open API Integration &amp; Real-Time Webhooks]
    E --> G
    F --> G
    G --> H[Unified Modern Hospitality Ecosystem<br/>Zero Vendor Lock-in | High Agility]""",
        "plotly_script": """
          setTimeout(() => {
            const categories = ['SaaS License Fees', 'Implementation & Migration', 'Custom Integration Dev', 'Maintenance & Support', 'Hidden Transaction Fees'];
            const unmanagedTCO = [100, 85, 95, 45, 65];
            const governedTCO = [85, 40, 25, 30, 15];

            const trace1 = { x: categories, y: unmanagedTCO, name: 'Unmanaged Vendor RFP (High Tech Debt)', type: 'bar', marker: { color: '#EF4444' } };
            const trace2 = { x: categories, y: governedTCO, name: 'Demand Journeys Governed RFP (S$k)', type: 'bar', marker: { color: '#10B981' } };

            const layout = {
              barmode: 'group', paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 60 }, font: { color: '#94A3B8', family: 'Inter', size: 10 },
              xaxis: { gridcolor: '#334155', tickangle: -10 }, yaxis: { title: '5-Year TCO Cost (S$k)', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-tco-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-tco-chart",
        "cards_title_1": "RFP Evaluation Criteria",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. Open API & Webhook Capabilities</h4>
            <p>Vendors that charge proprietary fees for every API call trap hotel groups. Modern platforms must offer open, documented REST/GraphQL APIs with real-time webhooks.</p>
          </div>
          <div class="dense-card">
            <h4>2. Total Cost of Ownership (5-Year TCO)</h4>
            <p>Evaluating total financial commitment including implementation fees, custom integration labor, transaction charges, and annual maintenance escalators.</p>
          </div>
          <div class="dense-card">
            <h4>3. Global Partner Management</h4>
            <p>Negotiating enterprise terms across Adobe, SAP, Sabre, Cendyn, and Microsoft to secure volume discounting and dedicated service level agreements (SLAs).</p>
          </div>
        """,
        "cards_title_2": "Frasers Hospitality RFP Experience",
        "cards_body_2": """
          <div class="dense-card">
            <h4>Enterprise Partner & RFP Leadership</h4>
            <ul>
              <li><strong>Experience:</strong> Led business-side RFP evaluations and vendor negotiations with Adobe, SAP, Sabre, Cendyn, and Microsoft.</li>
              <li><strong>Governance:</strong> Stabilized the enterprise website and platform transformation ahead of launch across 70+ properties.</li>
              <li><strong>Result:</strong> Eliminated redundant software platforms, saving <span class="metric-badge">over S$800K in duplicate licensing</span> over 3 years.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Procurement Toolkit</h4>
            <ul>
              <li>The 100-Point Hospitality Vendor RFP Evaluation Scorecard.</li>
              <li>SLA and Data Ownership Contract Clause Templates.</li>
            </ul>
          </div>
        """
    },
    # 20
    {
        "id": "ws20-board-approval-hotel-digital-capex",
        "number": "20",
        "title": "SECURING BOARD & OWNER APPROVAL FOR DIGITAL CAPEX",
        "subtitle": "Building Irrefutable Financial Business Cases, ROI Hurdle Rates, and Valuation Alignment",
        "descriptor": "How hospitality executives build Board-grade investment cases (e.g. S$5.5M transformation budgets) that connect digital technology investments directly to property valuation, gross operating profit, and shareholder returns.",
        "target": "Chief Executive Officers, Chief Commercial Officers, Asset Managers, Hotel Owners",
        "framework": "The Board-Grade Capital Justification Model™",
        "mermaid": """graph TD
    A[Digital Transformation Vision] --> B[Translate into Board-Level Financial Metrics]
    B --> C[Revenue Uplift Hurdle: 2.5x Performance Target]
    B --> D[Operating Efficiency: US$1.4M OpEx Reduction]
    B --> E[Asset Valuation: +12% Capitalized Value at 6% Exit Yield]
    C --> F{Board Investment Committee Presentation}
    D --> F
    E --> F
    F --> G[S$5.5M Capital Funding Approved]
    G --> H[Phased Milestone Governance &amp; Post-Launch Value Audits]""",
        "plotly_script": """
          setTimeout(() => {
            const years = ['Year 0 (CapEx)', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'];
            const cumulativeCapEx = [-5.5, -5.5, -5.5, -5.5, -5.5, -5.5];
            const cumulativeCashflow = [-5.5, -1.8, 3.2, 8.9, 15.4, 22.8];

            const trace1 = { x: years, y: cumulativeCapEx, name: 'CapEx Investment (S$M)', type: 'bar', marker: { color: '#EF4444' } };
            const trace2 = { x: years, y: cumulativeCashflow, name: 'Cumulative Net Cashflow Contribution (S$M)', type: 'scatter', mode: 'lines+markers', line: { color: '#10B981', width: 4 } };

            const layout = {
              paper_bgcolor: 'transparent', plot_bgcolor: 'transparent',
              margin: { t: 30, r: 30, l: 50, b: 50 }, font: { color: '#94A3B8', family: 'Inter', size: 11 },
              xaxis: { gridcolor: '#334155' }, yaxis: { title: 'Net Cashflow Impact (S$ Millions)', gridcolor: '#334155' },
              legend: { orientation: 'h', y: 1.15, x: 0.1 }
            };
            Plotly.newPlot('plotly-capex-chart', [trace1, trace2], layout, { responsive: true, displayModeBar: false });
          }, 300);
        """,
        "plotly_id": "plotly-capex-chart",
        "cards_title_1": "Board Presentation Pillars",
        "cards_body_1": """
          <div class="dense-card">
            <h4>1. The 2.5x Revenue Performance Hurdle</h4>
            <p>Boards reject technology proposals framed as IT infrastructure upgrades. Framing investments around concrete commercial hurdle rates guarantees executive sponsorship.</p>
          </div>
          <div class="dense-card">
            <h4>2. Direct Channel Margin Expansion</h4>
            <p>Every dollar shifted from 20% OTA commission to direct Brand.com drops straight to the bottom-line, boosting Net Operating Income (NOI).</p>
          </div>
          <div class="dense-card">
            <h4>3. Impact on Hotel Capitalized Valuation</h4>
            <p>A S$1M increase in annual Net Operating Income at a 6% capitalization rate increases hotel asset valuation by <strong>S$16.6 Million</strong> upon exit.</p>
          </div>
        """,
        "cards_title_2": "Project Meta Board Victory",
        "cards_body_2": """
          <div class="dense-card">
            <h4>S$5.5M Project Meta Board Case Study</h4>
            <ul>
              <li><strong>Achievement:</strong> Led the Project Meta transformation business case that secured S$5.5M in Board-approved funding.</li>
              <li><strong>Hurdle:</strong> Built around a 2.5x revenue performance hurdle and consolidated 2.3M+ customer records across 12 legacy source systems.</li>
              <li><strong>Delivery:</strong> Delivered +56% YoY direct room-night growth and +18% net ADR growth, exceeding Board targets.</li>
            </ul>
          </div>
          <div class="dense-card">
            <h4>Boardroom Toolkit</h4>
            <ul>
              <li>The 10-Slide Board-Approved Capital Proposal Deck Template.</li>
              <li>CapEx vs OpEx Financial Sensitivity Model in Excel.</li>
            </ul>
          </div>
        """
    }
]

for ws in ALL_WORKSHOPS:
    filename = os.path.join(OUTPUT_DIR, f"{ws['id']}.html")
    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(generate_html(ws))
    print(f"Generated {filename}")

# Generate Master Workshops Portal
ALL_TITLES = [
    ("01", "ws01-ai-discoverability-geo.html", "Hospitality AI Discoverability (GEO / AEO)", "Winning Generative Travel Search & Zero-Click Demand"),
    ("02", "ws02-agentic-workflows-hotel-ops.html", "Autonomous AI & Agentic Workflows", "Scaling Hotel Commercial Operations, Rate Intelligence & Guest Ops"),
    ("03", "ws03-predictive-demand-dynamic-pricing.html", "Predictive Demand & Dynamic Pricing", "Augmenting RMS with Machine Learning & Real-Time Demand"),
    ("04", "ws04-ai-virtual-concierge-ancillary.html", "AI Virtual Concierge & In-Stay Monetization", "Driving TrevPAR, F&B Spend and Ancillary Revenue"),
    ("05", "ws05-single-guest-profile-cdp.html", "The Single Guest Profile: Enterprise CDP", "Consolidating Fragmented PMS, CRS, POS and Website Data"),
    ("06", "ws06-hotel-personalization-realtime-offers.html", "Next-Gen Hotel Personalization", "Transforming Brand.com into an Intent-Driven Engine"),
    ("07", "ws07-guest-ltv-trevpar-optimization.html", "Guest Lifetime Value & TrevPAR Optimization", "Shifting from Single-Stay RevPAR to Multi-Year Total Yield"),
    ("08", "ws08-hotel-loyalty-transformation.html", "Modernizing Hotel Loyalty", "Moving from Margin-Eroding Points to Instant Gratification"),
    ("09", "ws09-total-distribution-mix-brand-vs-ota.html", "Total Distribution Mix: Brand.com vs OTAs", "Deconstructing Channel Costs, Net ADR, and Margin Leakage"),
    ("10", "ws10-metasearch-bidding-economics.html", "Metasearch Bidding Economics", "Rate Parity Governance and Google Hotel Ads Optimization"),
    ("11", "ws11-corporate-mice-demand-digitization.html", "Corporate & MICE Demand Digitization", "Automating Group RFPs, Negotiated Rates & B2B Vouchers"),
    ("12", "ws12-wholesaler-governance-rate-leakage.html", "Wholesaler Governance & Rate Leakage", "Auditing Bedbanks and Protecting Direct Price Integrity"),
    ("13", "ws13-marketing-mix-modeling-mmm-hotels.html", "Marketing Mix Modeling (MMM) for Hotels", "Econometric Measurement and Multi-Market Budget Allocation"),
    ("14", "ws14-media-incrementality-geo-testing.html", "Media Incrementality & Geo-Testing", "Eliminating Brand Search Cannibalization & Measuring Lift"),
    ("15", "ws15-hotel-digital-unit-economics-mer.html", "Hotel Digital Marketing Unit Economics", "Setting Rigorous MER, CAC Caps, and Payback Velocity"),
    ("16", "ws16-csuite-commercial-dashboards-powerbi.html", "C-Suite Commercial Dashboards (Power BI)", "Synthesizing Commercial Data into Decision Intelligence"),
    ("17", "ws17-hotel-booking-engine-cro-funnel.html", "Hotel Booking Engine Optimization", "Reducing 10-Step Drop-Offs to 5 Frictionless Steps"),
    ("18", "ws18-high-velocity-ab-testing-hotels.html", "High-Velocity A/B Testing for Hotels", "Structuring Scientific Experimentation Roadmaps"),
    ("19", "ws19-hotel-tech-stack-vendor-rfp.html", "Hotel Tech Stack & Vendor RFP Governance", "Navigating PMS, CRS, CDP and Channel Managers"),
    ("20", "ws20-board-approval-hotel-digital-capex.html", "Securing Board & Owner Approval for CapEx", "Building Irrefutable Financial Business Cases & 2.5x Hurdles")
]

catalog_cards = ""
for num, link, title, sub in ALL_TITLES:
    catalog_cards += f"""
      <div class="dense-card" style="display: flex; flex-direction: column; justify-content: space-between; border-left: 3px solid #D97706;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span class="metric-badge">Workshop {num}</span>
            <span style="font-size: 0.72rem; color: #94A3B8;">90-Min Masterclass</span>
          </div>
          <h4 style="font-size: 1.05rem; line-height: 1.25; margin-bottom: 4px; color: #FFFFFF;">{title}</h4>
          <p style="font-size: 0.8rem; color: #94A3B8; margin-bottom: 12px;">{sub}</p>
        </div>
        <a href="{link}" target="_blank" style="display: inline-block; text-align: center; background: #D97706; color: #FFFFFF; text-decoration: none; padding: 6px 12px; border-radius: 4px; font-weight: 600; font-size: 0.8rem; transition: background 0.2s;">Launch Slide Deck &rarr;</a>
      </div>
    """

portal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Demand Journeys | Executive Masterclass Workshop Series (20 Decks)</title>
  <meta name="description" content="Master Catalog of 20 Interactive Reveal.js Executive Masterclasses for Hospitality Leaders, Hotel Owners, General Managers, and Commercial Executives.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/demand-journeys.css">
  <style>
    body {{ background: radial-gradient(circle at 50% 20%, #1E293B 0%, #0F172A 100%); color: #F8FAFC; font-family: 'Inter', sans-serif; padding: 30px 20px; }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    .header {{ text-align: center; margin-bottom: 35px; }}
    .header h1 {{ font-family: 'Newsreader', serif; font-size: 2.6rem; color: #FFFFFF; margin-bottom: 8px; font-weight: 500; }}
    .header p {{ color: #FBBF24; font-size: 1.1rem; max-width: 800px; margin: 0 auto; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 20px; }}
    .metric-badge {{ display: inline-block; background: rgba(217, 119, 6, 0.2); border: 1px solid #D97706; color: #FBBF24; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }}
    .dense-card {{ background: rgba(30, 41, 59, 0.85); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 8px; padding: 18px; }}
    .dense-card:hover {{ border-color: #D97706; box-shadow: 0 8px 24px rgba(0,0,0,0.4); }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div style="display: inline-block; background: rgba(217, 119, 6, 0.15); border: 1px solid #D97706; padding: 4px 12px; border-radius: 50px; font-size: 0.75rem; font-weight: 700; color: #FBBF24; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 12px;">Demand Journeys Executive Practice</div>
      <h1>Hospitality Executive Masterclass Series</h1>
      <p>20 Specialized Reveal.js Masterclasses for Hotel Asset Owners, General Managers, Chief Commercial Officers &amp; Revenue Directors</p>
    </div>

    <div class="grid">
      {catalog_cards}
    </div>

    <div style="text-align: center; margin-top: 50px; padding: 24px; background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px;">
      <p style="color: #94A3B8; font-size: 0.9rem; margin: 0;">Facilitated by <strong>Tan Meng Liang</strong> &bull; Founder, Demand Journeys &bull; Singapore &bull; Global</p>
    </div>
  </div>
</body>
</html>"""

with open(os.path.join(OUTPUT_DIR, "workshops.html"), "w", encoding="utf-8") as fp:
    fp.write(portal_html)
print("Generated workshops.html master portal.")
