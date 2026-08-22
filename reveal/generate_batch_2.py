#!/usr/bin/env python3
import os

OUTPUT_DIR = "/home/ml/Documents/00 Job Seeking Tools/Consultancy/DemandJourneys/reveal"
os.makedirs(OUTPUT_DIR, exist_ok=True)

REMAINING_WORKSHOPS = [
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
              <li><strong>Result:</strong> <span class="metric-badge">Lined overall website conversion from 0.68% to 2.25%</span> while reducing customer booking steps from 10 to 5.</li>
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
            <p>$$\\text{TrevPAR} = \\frac{\\text{Total Room Rev} + \\text{F&B} + \\text{Spa} + \\text{Ancillary}}{\\text{Total Available Rooms}}$$ Incorporating total on-property spend changes commercial prioritization.</p>
          </div>
          <div class="dense-card">
            <h4>2. Predictive Churn Triggers</h4>
            <p>If a corporate traveler who averages 12 nights/year has no reservations by day 120, automated alerts notify the account manager to intervene before account attrition.</p>
          </div>
          <div class="dense-card">
            <h4>3. Acquisition Cost Amortization</h4>
            <p>Spending S$120 CAC on a guest is ruinous for a single S$250 stay, but highly accretive if that guest returns 4 times over 24 months via Brand.com ($S$1,000+ Net LTV).</p>
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
    }
]

for ws in REMAINING_WORKSHOPS:
    filename = os.path.join(OUTPUT_DIR, f"{ws['id']}.html")
    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(generate_html(ws))
    print(f"Generated {filename}")

