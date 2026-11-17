#!/usr/bin/env python3
"""
Airlines Presentation Generator — 52 Slides
Generates:
1. /run/media/ml/Storage/Labs/airlines/presentation.html
2. /run/media/ml/Storage/Labs/airlines/PRESENTATION_FRAMEWORK_COMPENDIUM.md
"""

import os
import sys
import json

BASE_DIR = "/run/media/ml/Storage/Labs"
sys.path.append(BASE_DIR)
import generate_presentation_engine as engine
import visual_slide_components as vsc

meta = {
    "title": "Commercial Aviation & Airlines Systems Architecture",
    "short_code": "AIRLINES",
    "sector": "Commercial Aviation & Airline Technology",
    "scale": "$800.0B Passenger GBV • 4.6B Departures • $160B Ancillary"
}

slides = [
    # PART 1: MACROECONOMICS, SIZING & REVENUE MODELS (1-5)
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Commercial Aviation Enterprise Architecture Masterclass",
        "subtitle": "Systems Architecture, Technology Stacks, and Operational Orchestration across 13 Enterprise Dimensions",
        "content": """
        <div class="grid-2" style="margin-top: 1rem;">
          <div class="glass-card">
            <div class="card-header">Executive Briefing Scope</div>
            <p>Comprehensive architectural blueprint analyzing the mission-critical systems governing modern commercial aviation ($800B global market, 4.6B passengers). Designed for Chief Information Officers, Chief Commercial Officers, and Enterprise Architects.</p>
            <div style="margin-top: 1rem;">
              <span class="pill pill-blue">13 Enterprise Layers</span>
              <span class="pill pill-green">3 Stack Variations</span>
              <span class="pill pill-purple">52 Master Slides</span>
              <span class="pill pill-amber">End-to-End Journeys</span>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Core Themes Covered</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Assumed Requirements & IT Standards:</strong> TOGAF, C4 Model, Zero-Trust, EDA, and IATA NDC standards.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>13-Layer Master Architecture:</strong> PSS, Marketing, CRM, Loyalty, CDP, Integration, Lakehouse, AI/ML, ERP.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>End-to-End Customer Journeys:</strong> Inspiration, NDC booking, biometrics, in-flight, and autonomous IROPS recovery.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>AI-Assisted Operational Efficiency:</strong> Agentforce, Palantir AIP, frontier LLMs, and Model Context Protocol.</div></div>
          </div>
        </div>
        """,
        "notes": "Welcome executive stakeholders. This deck provides an unbroken technical and commercial chain of logic across all airline technology layers."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Global Aviation Sizing & Revenue Architecture",
        "subtitle": "Macroeconomic baseline: $800.0B Passenger Gross Booking Value across 4.6 Billion annual departures",
        "content": """
        <div class="grid-4" style="margin-bottom: 1rem;">
          <div class="glass-card">
            <div class="metric-hero">$800.0B</div>
            <div class="metric-sub">Global Passenger GBV</div>
            <p style="margin-top: 0.4rem; color: var(--text-muted);">4.6B annual passengers at $173.91 blended ticket + ancillary spend.</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero" style="color: #10b981;">$640.0B</div>
            <div class="metric-sub">Base Airfare Revenue</div>
            <p style="margin-top: 0.4rem; color: var(--text-muted);">80.0% of total revenue. High price sensitivity, yield management driven.</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero" style="color: #8b5cf6;">$160.0B</div>
            <div class="metric-sub">Ancillary Revenue</div>
            <p style="margin-top: 0.4rem; color: var(--text-muted);">20.0% of revenue. Bags, seats, Wi-Fi, lounges, and co-brand credit cards.</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero" style="color: #f59e0b;">$55.6B</div>
            <div class="metric-sub">Operating Profit (EBIT)</div>
            <p style="margin-top: 0.4rem; color: var(--text-muted);">7.0% of GBV / 7.4% margin on net revenue. Razor-thin margin environment.</p>
          </div>
        </div>
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Fleet & Carrier Segmentation</div>
            <table class="data-table">
              <tr><th>Carrier Segment</th><th>Share</th><th>Annual GBV</th><th>Core Systems</th></tr>
              <tr><td>Network Legacy Carriers</td><td>60.0%</td><td>$480.0B</td><td>Amadeus Altéa, SabreSonic, SITA</td></tr>
              <tr><td>Low-Cost Carriers (LCCs)</td><td>30.0%</td><td>$240.0B</td><td>Navitaire New Skies, Radixx</td></tr>
              <tr><td>Regional & Hybrid</td><td>6.9%</td><td>$55.0B</td><td>SabreSonic, Hitit Crane</td></tr>
              <tr><td>Charter & Private</td><td>3.1%</td><td>$25.0B</td><td>Amadeus Charter, bespoke</td></tr>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic Takeaway</div>
            <p>Airlines operate on hyper-compressed operating margins (7.4% EBIT). Every 1% reduction in distribution friction saves $464M globally. Ancillary revenue ($160B) represents over 100% of net industry profit—without ancillaries, the global airline industry operates at a net loss.</p>
          </div>
        </div>
        """,
        "notes": "Establish the high-stakes financial reality: airlines cannot afford IT waste or failed integrations with 7.4% EBIT."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Distribution Friction & Unit Economics",
        "subtitle": "Detailed financial waterfall tracking every dollar from gross ticket purchase to net airline operating profit",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Passenger Journey Unit Economics ($173.91 Average Fare)</div>
            <table class="data-table">
              <tr><th>Component</th><th>Amount ($)</th><th>% of GBV</th><th>Operational Cost Driver</th></tr>
              <tr><td><strong>Gross Booking Value</strong></td><td><strong>$173.91</strong></td><td><strong>100.0%</strong></td><td>Base Fare ($139.13) + Ancillaries ($34.78)</td></tr>
              <tr><td>GDS Segment Fees</td><td>-$3.48</td><td>-2.0%</td><td>Legacy EDIFACT booking fee ($3.50-$6/seg)</td></tr>
              <tr><td>Credit Card Interchange</td><td>-$3.91</td><td>-2.25%</td><td>Merchant acquiring and scheme fees</td></tr>
              <tr><td>TMC & Agency Overrides</td><td>-$1.74</td><td>-1.0%</td><td>Corporate contract incentive overrides</td></tr>
              <tr><td>Tech Stack & PSS Fee</td><td>-$0.96</td><td>-0.55%</td><td>Per-passenger boarded PSS/DCS charge</td></tr>
              <tr><td><strong>Net Airline Revenue</strong></td><td><strong>$163.82</strong></td><td><strong>94.2%</strong></td><td><strong>Retained Passenger Revenue</strong></td></tr>
              <tr><td>Jet Fuel (28% of OpEx)</td><td>-$42.42</td><td>-24.4%</td><td>Bunker fuel indexation and burn rate</td></tr>
              <tr><td>Flight Crew Labor (24%)</td><td>-$36.36</td><td>-20.9%</td><td>Pilots, cabin crew, union contracts</td></tr>
              <tr><td>Aircraft Leases & CapEx (12%)</td><td>-$18.18</td><td>-10.5%</td><td>Airframe financing and depreciation</td></tr>
              <tr><td>Airport & ATC Fees (9%)</td><td>-$13.64</td><td>-7.8%</td><td>Landing slots, passenger facility charges</td></tr>
              <tr><td>Maintenance & MRO (8%)</td><td>-$12.12</td><td>-7.0%</td><td>Engine overhauls, line maintenance</td></tr>
              <tr><td><strong>Operating Profit (EBIT)</strong></td><td><strong>$12.09</strong></td><td><strong>7.0%</strong></td><td><strong>Net Margin Per Passenger</strong></td></tr>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Key Architectural Insights</div>
            <p><strong>The $10.09 Friction Barrier:</strong> Total intermediary and payment friction consumes $10.09 per passenger ($46.4B globally). This equals nearly 85% of total airline operating profit ($12.09).</p>
            <div style="margin-top: 0.8rem;">
              <div class="card-header" style="color: #10b981;">The Direct & NDC Imperative</div>
              <p>Shifting a booking from GDS EDIFACT to Direct Brand.com saves $3.48 in GDS fees and recaptures $14.20 in personalized ancillary upsell, increasing per-passenger net EBIT by <strong>146%</strong>.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Show the audience where the money leaks. The GDS fee is nearly equal to half the entire operating profit per seat."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Channel Share Dynamics: The Direct & NDC Mandate",
        "subtitle": "The ongoing battle between Direct Web/Mobile (52.5%), IATA NDC (12.5%), and Legacy GDS EDIFACT (22.5%)",
        "content": """
        <div class="grid-3" style="margin-bottom: 1rem;">
          <div class="glass-card" style="border-left: 3px solid #10b981;">
            <div class="card-header">Direct Channels (52.5% / $420B)</div>
            <p><strong>Airline.com, Mobile Apps, Airport Kiosks:</strong> Lowest distribution cost (0% GDS fees). Highest ancillary attachment rate (34% vs 8% in GDS). Direct customer relationship and first-party data capture.</p>
          </div>
          <div class="glass-card" style="border-left: 3px solid #8b5cf6;">
            <div class="card-header">IATA NDC Direct Connect (12.5% / $100B)</div>
            <p><strong>Open XML/JSON APIs:</strong> Bypasses legacy EDIFACT green-screens. Enables dynamic bundle creation, rich media seat maps, personalized loyalty fare bundles, and continuous pricing.</p>
          </div>
          <div class="glass-card" style="border-left: 3px solid #f59e0b;">
            <div class="card-header">Legacy GDS EDIFACT (22.5% / $180B)</div>
            <p><strong>Sabre, Amadeus, Travelport:</strong> High segment fees ($4.50-$6.00). Rigid 26 booking classes (A-Z). Zero rich content. Airlines actively applying GDS surcharges ($15-$25/ticket) to force transition.</p>
          </div>
        </div>
        <div class="glass-card">
          <div class="card-header">The Architectural Transition Matrix</div>
          <table class="data-table">
            <tr><th>Capability</th><th>Legacy GDS EDIFACT</th><th>IATA NDC (New Distribution Capability)</th><th>Direct Digital (Brand.com / App)</th></tr>
            <tr><td>Pricing Granularity</td><td>Rigid 26 ATPCO Fare Buckets</td><td>Algorithmic Continuous Pricing (Dynamic)</td><td>Personalized Willingness-to-Pay Pricing</td></tr>
            <tr><td>Ancillary Merchandising</td><td>Static EMDs, text-only description</td><td>Rich media, 3D seat views, bundles</td><td>Full dynamic cart, one-click Apple Pay</td></tr>
            <tr><td>Distribution Cost / Pax</td><td>$4.50 - $6.50 per segment</td><td>$0.80 - $1.50 per booking</td><td>$0.20 - $0.45 per booking</td></tr>
            <tr><td>Customer Identity</td><td>Anonymous PNR until check-in</td><td>Known traveler via loyalty number / email</td><td>100% authenticated first-party profile</td></tr>
          </table>
        </div>
        """,
        "notes": "Explain why airlines are aggressively penalizing legacy GDS. NDC is not just a protocol change; it is an economic power shift."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Strategic Business Imperatives for the Next Decade",
        "subtitle": "The four existential battlegrounds defining airline commercial and operational software investments",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header" style="color: #3b82f6;">1. Direct Channel & Ancillary Maximization</div>
            <p>Airlines must expand direct digital share past 60% while growing ancillaries to 30%+ of total revenue. This requires sub-second dynamic pricing engines, personalized bundle generation, and seamless one-click payments across mobile wallets.</p>
            <div style="margin-top: 0.5rem;"><span class="pill pill-blue">Dynamic Bundling</span><span class="pill pill-blue">Continuous Pricing</span><span class="pill pill-blue">Apple Wallet</span></div>
          </div>
          <div class="glass-card">
            <div class="card-header" style="color: #10b981;">2. Autonomous IROPS & Disruption Recovery</div>
            <p>Extreme weather and air traffic control delays cost global airlines $30B+ annually in hotel vouchers, crew duty timeouts, and EU261 penalties. Moving from manual phone queues to multi-agent autonomous rebooking is the #1 operational priority.</p>
            <div style="margin-top: 0.5rem;"><span class="pill pill-green">Multi-Agent AI</span><span class="pill pill-green">EU261 Compliance</span><span class="pill pill-green">Automated Vouchers</span></div>
          </div>
          <div class="glass-card">
            <div class="card-header" style="color: #8b5cf6;">3. Servicing Cost Deflection & Contact Center Modernization</div>
            <p>Handling passenger calls during flight cancellations costs $4.50 to $7.00 per interaction. Airlines must deflect 60%+ of routine inquiries to generative AI agents across WhatsApp, SMS, and in-app chat, driving cost-per-contact below $0.30.</p>
            <div style="margin-top: 0.5rem;"><span class="pill pill-purple">Agentforce</span><span class="pill pill-purple">WhatsApp Commerce</span><span class="pill pill-purple">Sub-$0.30 Cost</span></div>
          </div>
          <div class="glass-card">
            <div class="card-header" style="color: #f59e0b;">4. Data Sovereignty & Sovereign Enterprise AI</div>
            <p>With tightening cross-border data privacy regulations (GDPR, Singapore PDPA, Indonesia UU PDP, and FAA cybersecurity mandates), airlines must adopt zero-copy data architectures that process passenger data within sovereign geographic boundaries.</p>
            <div style="margin-top: 0.5rem;"><span class="pill pill-amber">Zero-Copy</span><span class="pill pill-amber">Sovereign Cloud</span><span class="pill pill-amber">PCI-DSS Tokenization</span></div>
          </div>
        </div>
        """,
        "notes": "Summarize Part 1. These 4 imperatives establish the requirements for the architecture we explore in Parts 2-10."
    }
]

# Generate slides 6 to 52 programmatically with high domain precision
# PART 2: ASSUMED REQUIREMENTS & CONSTRAINTS (6-10)
slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Enterprise Baseline Persona: Network Flagship + LCC",
    "subtitle": "Assumed operating model: Dual-brand aviation group with 300 aircraft and 45 Million annual passengers",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Fleet & Operational Scale Assumptions</div>
        <table class="data-table">
          <tr><th>Parameter</th><th>Network Flagship (Full-Service)</th><th>LCC Subsidiary</th></tr>
          <tr><td>Fleet Size</td><td>210 Aircraft (A350, B777, B787, A321)</td><td>90 Aircraft (A320, B737 MAX)</td></tr>
          <tr><td>Annual Departures</td><td>240,000 Flights / Year</td><td>160,000 Flights / Year</td></tr>
          <tr><td>Passenger Volume</td><td>28 Million Passengers</td><td>17 Million Passengers</td></tr>
          <tr><td>Average Sector Length</td><td>3,400 km (Long-haul + Regional)</td><td>1,200 km (Short-haul Point-to-Point)</td></tr>
          <tr><td>Hub Airport</td><td>Primary Mega-Hub (Tier 1 Airport)</td><td>Secondary Low-Cost Terminals</td></tr>
          <tr><td>Core PSS</td><td>Amadeus Altéa (Reservations/DCS)</td><td>Navitaire New Skies</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Commercial & Organization Topology</div>
        <p><strong>The Dual-Brand Operational Paradox:</strong> The enterprise operates under a single holding company board, sharing frequent flyer programs, corporate sales teams, and ground handling infrastructure, while maintaining completely segregated brand identities, fare rules, and customer expectations.</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #3b82f6;">Key Business Constraint</div>
          <p>The solution must provide a single unified passenger data fabric across both brands without forcing the LCC to pay legacy PSS transaction fees or diluting the flagship carrier's premium service tiers.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "Ground the audience in concrete reality. We are modeling a dual-brand group like Singapore Airlines/Scoot, Qantas/Jetstar, or IAG."
})

slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Functional Requirements Matrix (Commerce, DCS, Ops)",
    "subtitle": "Decomposition of 85+ functional capabilities across 5 operational domains",
    "content": """
    <div class="grid-3">
      <div class="glass-card">
        <div class="card-header">1. Commercial & Retailing</div>
        <p>• <strong>Continuous Pricing:</strong> Algorithmic fare calculation across 100+ fare classes.</p>
        <p>• <strong>Dynamic Ancillaries:</strong> Personalized seat map, baggage, and meal merchandising.</p>
        <p>• <strong>Omni-Channel Cart:</strong> Persistent reservation state across web, app, and contact center.</p>
        <p>• <strong>Corporate Portal:</strong> B2B contracted discounts and corporate travel manager self-service.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">2. Airport & Departure Control</div>
        <p>• <strong>Biometric Boarding:</strong> Walk-through facial recognition curb-to-gate (ICAO 9303).</p>
        <p>• <strong>Automated Bag-Drop:</strong> CUSS/CUTE kiosk integration and RFID baggage tag generation.</p>
        <p>• <strong>Weight & Balance:</strong> Real-time aircraft trim sheet calculation and load control.</p>
        <p>• <strong>Standby / Gate Upgrades:</strong> Automated revenue-maximizing gate upgrade auctioning.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">3. Operations & Crew</div>
        <p>• <strong>Disruption Orchestration:</strong> Automated recovery during diversions and weather groundings.</p>
        <p>• <strong>Crew Legality:</strong> FAA Part 117 and EASA FTL fatigue and duty time tracking.</p>
        <p>• <strong>ACARS Telemetry:</strong> Real-time aircraft engine and fuel burn streaming.</p>
        <p>• <strong>Baggage Reconciliation:</strong> IATA Resolution 753 compliance at transfer hubs.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Cross-Functional Operational Matrix</div>
      <p>Every commercial transaction (e.g. purchasing an extra bag 2 hours before flight) must instantly propagate across 4 systems: Revenue Accounting (ASC 606), Departure Control (Weight & Balance), Baggage Handling (BHS RFID sortation), and the Mobile App Wallet.</p>
    </div>
    """,
    "notes": "Emphasize cross-functional dependencies. A simple bag purchase impacts aircraft balance and baggage sortation."
})

slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Non-Functional Requirements (NFRs) & Operational SLAs",
    "subtitle": "Strict enterprise performance, throughput, resilience, and recovery benchmarks",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Throughput & Latency SLAs</div>
        <table class="data-table">
          <tr><th>System Interaction</th><th>Peak Throughput</th><th>Latency SLA</th><th>Business Impact</th></tr>
          <tr><td>Flight Search / Shopping</td><td>120,000 requests/sec</td><td>< 250 ms</td><td>Every 100ms delay drops booking conversion by 1.2%</td></tr>
          <tr><td>Booking & Payment Settlement</td><td>2,500 bookings/sec</td><td>< 800 ms</td><td>Prevents shopping cart abandonment during flash sales</td></tr>
          <tr><td>Departure Control Boarding</td><td>450 scans/second</td><td>< 50 ms</td><td>Avoids gate bottleneck; guarantees 35-minute turnaround</td></tr>
          <tr><td>Real-Time Identity Resolution</td><td>15,000 events/sec</td><td>< 100 ms</td><td>Enables instant personalized greeting on mobile app</td></tr>
          <tr><td>Agentforce Autonomous Prompt</td><td>8,000 concurrent chats</td><td>< 1,200 ms</td><td>Maintains natural conversational flow during IROPS</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">High Availability & Disaster Recovery (RTO / RPO)</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Five-Nines Availability (99.999%):</strong> Maximum unplanned downtime of under 5.26 minutes per year across mission-critical PSS and DCS systems.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Zero Recovery Point Objective (RPO = 0):</strong> Zero transactional data loss permitted for issued tickets, baggage tags, or payment tokens.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Recovery Time Objective (RTO < 5 min):</strong> Automated multi-region cloud failover in under 5 minutes in event of primary data center failure.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div><strong>Offline Kiosk / Gate Survivability:</strong> Airport check-in desks and boarding gates must operate locally for up to 4 hours during WAN blackouts.</div></div>
      </div>
    </div>
    """,
    "notes": "Airlines cannot tolerate downtime. If the DCS goes down for 30 minutes, an entire terminal grinds to a halt."
})

slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Regulatory & Data Sovereignty Mandates",
    "subtitle": "Navigating GDPR, Singapore PDPA, Indonesia UU PDP, PCI-DSS Level 1, and Aviation Safety Regulations",
    "content": """
    <div class="grid-3">
      <div class="glass-card" style="border-left: 3px solid #3b82f6;">
        <div class="card-header">Global Data Privacy Compliance</div>
        <p>• <strong>GDPR (EU):</strong> Strict consent for passenger tracking; right to be forgotten (DSAR) within 30 days; cross-border transfer mechanisms (SCCs).</p>
        <p>• <strong>Singapore PDPA:</strong> Stringent NRIC and passport handling; mandatory data breach notification within 72 hours.</p>
        <p>• <strong>Indonesia UU PDP:</strong> Mandatory domestic processing for Indonesian citizen personal data and explicit consent for marketing profiling.</p>
      </div>
      <div class="glass-card" style="border-left: 3px solid #10b981;">
        <div class="card-header">Aviation Regulatory Standards</div>
        <p>• <strong>EU261 / UK261:</strong> Mandatory passenger compensation (€250-€600) for delays > 3 hours not caused by extraordinary circumstances.</p>
        <p>• <strong>IATA Resolution 753:</strong> Mandatory tracking of baggage at 4 key milestones (passenger handover, loading, transfer, arrival).</p>
        <p>• <strong>APIS / iAPI:</strong> Advance Passenger Information System streaming passenger manifests to border authorities pre-departure.</p>
      </div>
      <div class="glass-card" style="border-left: 3px solid #f59e0b;">
        <div class="card-header">Payment & Cybersecurity Governance</div>
        <p>• <strong>PCI-DSS v4.0 Level 1:</strong> Mandatory point-to-point encryption (P2PE) and tokenization of all credit card data; zero cleartext PAN storage.</p>
        <p>• <strong>FAA / EASA Cybersecurity:</strong> DO-326A / ED-202A airworthiness security process for aircraft systems and electronic flight bags (EFBs).</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Architectural Implication</div>
      <p>Data Cloud and AI systems must implement strict <strong>Field-Level Encryption (FLE)</strong> and <strong>Object-Level Security (OLS)</strong>. Sensitive passport, payment, and biometric data must never be passed unmasked into public foundation model prompts.</p>
    </div>
    """,
    "notes": "Highlight compliance. Failure to comply with EU261 or GDPR can wipe out millions in operating profit."
})

slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Multi-Brand & Alliance Interline Complexity",
    "subtitle": "Managing Star Alliance / SkyTeam / oneworld partnerships, code-shares, and interline revenue proration",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Interline & Alliance Data Flows</div>
        <table class="data-table">
          <tr><th>Alliance Interaction</th><th>Protocol / Standard</th><th>Data Exchanged</th><th>Friction Point</th></tr>
          <tr><td>Code-Share Booking</td><td>IATA Interline EDIFACT / NDC</td><td>Operating carrier PNR, seat availability</td><td>Inventory desynchronization across carriers</td></tr>
          <tr><td>Through Check-in</td><td>IATA Resolution 766 (IATCI)</td><td>Multi-sector boarding passes, bag tags</td><td>Mismatched baggage allowances across airlines</td></tr>
          <tr><td>Alliance Tier Recognition</td><td>Star Alliance / SkyTeam API</td><td>Elite status, lounge access entitlement</td><td>Latency in partner tier verification at lounge</td></tr>
          <tr><td>Revenue Proration</td><td>IATA Clearing House (ICH) / Prorate</td><td>Multilateral Proration Agreement (MPA)</td><td>Delayed financial settlement (30-60 days)</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Architectural Solution: Zero-Copy Clean Rooms</div>
        <p>Historically, interline partnerships required clumsy batched file exchanges via SITA teletype networks. Today, modern airline groups deploy <strong>Snowflake Sovereign Clean Rooms</strong>:</p>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Secure Data Sharing:</strong> Query partner booking availability without moving raw customer PII across borders.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Instant Tier Validation:</strong> Validate alliance Gold/Diamond status in under 20ms at airport lounge turnstiles.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Automated Proration:</strong> Real-time coupon proration calculating exact dollar entitlement upon flight departure.</div></div>
      </div>
    </div>
    """,
    "notes": "Explain how modern clean rooms solve 40-year-old alliance friction points."
})

# PART 3: IT STANDARDS & ARCHITECTURAL GOVERNANCE (11-15)
slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "Enterprise Architecture Governance: TOGAF & C4 Model",
    "subtitle": "Structuring complex aviation systems across Context, Container, Component, and Code tiers",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">C4 Architectural Hierarchy</div>
        <div class="flow-step"><div class="step-num">L1</div><div><strong>Context Tier:</strong> Passenger, Travel Advisor, Airport Staff, and Partner Airlines interacting with the Airline Enterprise System.</div></div>
        <div class="flow-step"><div class="step-num">L2</div><div><strong>Container Tier:</strong> Web/Mobile Front-ends, MuleSoft API Gateways, Data Cloud, Altéa PSS, Kafka Event Mesh, and Snowflake Lakehouse.</div></div>
        <div class="flow-step"><div class="step-num">L3</div><div><strong>Component Tier:</strong> PNR State Manager, Booking Cart Engine, Identity Resolution Graph, and Agentforce Reasoning Engine.</div></div>
        <div class="flow-step"><div class="step-num">L4</div><div><strong>Code Tier:</strong> Microservices, TypeScript SDKs, Model Context Protocol (MCP) JSON-RPC tool schemas, and SQL DMO models.</div></div>
      </div>
      <div class="glass-card">
        <div class="card-header">Architecture Review Board (ARB) Standards</div>
        <table class="data-table">
          <tr><th>Governance Domain</th><th>Mandated Standard</th><th>Enforcement Mechanism</th></tr>
          <tr><td>API Design</td><td>OpenAPI 3.0 / REST & gRPC</td><td>Automated linting in CI/CD pipeline</td></tr>
          <tr><td>Event Streaming</td><td>CloudEvents 1.0 / Apache Avro</td><td>Schema Registry validation on Kafka topics</td></tr>
          <tr><td>Data Modeling</td><td>TM Forum & Salesforce DMOs</td><td>Enterprise Data Governance gate in Collibra</td></tr>
          <tr><td>Security Standards</td><td>OAuth 2.1 / mTLS / OIDC</td><td>API Gateway token validation policy</td></tr>
          <tr><td>Cloud Deployment</td><td>Infrastructure-as-Code (Terraform)</td><td>Automated policy-as-code via HashiCorp Sentinel</td></tr>
        </table>
      </div>
    </div>
    """,
    "notes": "Establish architectural rigor. Every tool must fit neatly into a well-defined C4 container."
})

slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "API-First Standard & Universal API Management",
    "subtitle": "Decoupling 50-year-old mainframe protocols from cloud microservices via 3-Tier API Architecture",
    "content": """
    <div class="grid-3">
      <div class="glass-card" style="border-top: 3px solid #3b82f6;">
        <div class="card-header">1. System APIs (Foundation)</div>
        <p><strong>Direct Connection to Systems of Record:</strong> Encapsulates underlying complexity of Altéa PSS, SabreSonic, SITA WorldTracer, and SAP S/4HANA.</p>
        <div style="margin-top: 0.5rem; font-family: monospace; font-size: 0.7rem; color: #93c5fd;">• altea-pnr-sys-api<br>• sita-baggage-sys-api<br>• sap-gl-sys-api</div>
      </div>
      <div class="glass-card" style="border-top: 3px solid #10b981;">
        <div class="card-header">2. Process APIs (Orchestration)</div>
        <p><strong>Business Logic & Workflow Coordination:</strong> Combines multiple System APIs to execute complex composite airline processes.</p>
        <div style="margin-top: 0.5rem; font-family: monospace; font-size: 0.7rem; color: #a7f3d0;">• flight-booking-proc-api<br>• irops-rebooking-proc-api<br>• bag-claim-proc-api</div>
      </div>
      <div class="glass-card" style="border-top: 3px solid #8b5cf6;">
        <div class="card-header">3. Experience APIs (Consumption)</div>
        <p><strong>Tailored Payloads for Specific Front-Ends:</strong> Formats data specifically for Mobile App, Kiosks, Travel Advisor Extranet, and Agentforce.</p>
        <div style="margin-top: 0.5rem; font-family: monospace; font-size: 0.7rem; color: #ddd6fe;">• mobile-app-exp-api<br>• agentforce-mcp-exp-api<br>• kiosk-cuss-exp-api</div>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Universal API Management & Flex Gateway</div>
      <p>MuleSoft Flex Gateway is deployed directly on airport on-premise Kubernetes clusters and cloud VPCs, providing sub-millisecond policy enforcement, rate limiting, and zero-trust mTLS encryption across all 3 tiers.</p>
    </div>
    """,
    "notes": "The 3-tier API-led connectivity model is the cornerstone of enterprise agility in airlines."
})

slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "Event-Driven Architecture (EDA) & Flight Telemetry",
    "subtitle": "Real-time event streaming spine processing 100,000+ flight, passenger, and baggage events per second",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Enterprise Event Streaming Topologies</div>
        <table class="data-table">
          <tr><th>Event Topic</th><th>Source System</th><th>Consumer Systems</th><th>Latency SLA</th></tr>
          <tr><td><code>flight.status.updated</code></td><td>Flight Operations / ACARS</td><td>Data Cloud, Mobile Push, Airport FIDS</td><td>< 50 ms</td></tr>
          <tr><td><code>pnr.ticket.issued</code></td><td>Altéa PSS / Booking Engine</td><td>Revenue Accounting, Loyalty, CDP</td><td>< 100 ms</td></tr>
          <tr><td><code>baggage.scanned</code></td><td>SITA BagMessage / RFID</td><td>Service Cloud, Passenger Mobile App</td><td>< 200 ms</td></tr>
          <tr><td><code>disruption.flight.cancelled</code></td><td>Dispatch / FlightAware</td><td>Agentforce IROPS Orchestrator</td><td>< 10 ms</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Dual-Tier Broker Architecture (Kafka + Solace)</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Solace PubSub+ (Hardware Mesh):</strong> Deployed for mission-critical flight operations and radar telemetry requiring sub-millisecond deterministic delivery.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Confluent Cloud Kafka (Enterprise Backbone):</strong> Multi-region managed Kafka handling business events, clickstreams, and customer profile updates.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Salesforce Pub/Sub API (gRPC):</strong> Bi-directional Change Data Capture streaming updates between Data Cloud and external enterprise systems.</div></div>
      </div>
    </div>
    """,
    "notes": "Airlines cannot rely on batch processing. When a flight is cancelled, downstream systems must react within milliseconds."
})

slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "Zero-Trust Security & Identity Governance",
    "subtitle": "Defense-in-depth architecture: CyberArk PAM, Okta CIAM, mTLS, and HSM Key Management",
    "content": """
    <div class="grid-3">
      <div class="glass-card">
        <div class="card-header">1. Identity & Access (IAM)</div>
        <p>• <strong>Okta Workforce Identity:</strong> SSO and adaptive MFA for 35,000+ airline employees and flight crews.</p>
        <p>• <strong>Auth0 / Okta CIAM:</strong> Frictionless biometric passkey login for 40M+ frequent flyers on mobile apps.</p>
        <p>• <strong>Contextual Access:</strong> Enforces geographic and device health checks before granting access to PSS.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">2. Privileged Access (PAM)</div>
        <p>• <strong>CyberArk Enterprise:</strong> Dynamic credential rotation and keystroke recording for all cloud infrastructure admins.</p>
        <p>• <strong>Zero Standing Privileges:</strong> Just-in-Time (JIT) access elevation for flight dispatch and database engineers.</p>
        <p>• <strong>Air-Gapped Vaults:</strong> Critical flight safety control credentials stored in offline physical vaults.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">3. Cryptographic Governance</div>
        <p>• <strong>HashiCorp Vault + HSM:</strong> FIPS 140-2 Level 3 hardware security modules protecting root cryptographic keys.</p>
        <p>• <strong>Salesforce Shield:</strong> Bring Your Own Key (BYOK) tenant-level encryption for all passenger PII at rest.</p>
        <p>• <strong>Microsegmentation:</strong> Zscaler Zero Trust Exchange eliminating corporate VPN vulnerabilities.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Zero-Trust Principle in Practice</div>
      <p>Never trust, always verify. An airport check-in contractor in Manila cannot see the passenger's corporate credit card details; a marketing analyst in London cannot export unmasked passport numbers. Every access is logged immutably.</p>
    </div>
    """,
    "notes": "Aviation is critical national infrastructure. CyberArk and HSMs protect against state-sponsored attacks."
})

slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "Cloud-Native Principles & Hybrid Sovereign Deployments",
    "subtitle": "Balancing hyperscaler agility with sovereign data residency and airport edge survivability",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Hybrid Multi-Cloud Topology</div>
        <table class="data-table">
          <tr><th>Deployment Tier</th><th>Platform</th><th>Workloads Hosted</th><th>Sovereignty Scope</th></tr>
          <tr><td>Terrestrial Hyperscaler Cloud</td><td>AWS & Google Cloud (Multi-Region)</td><td>Web booking, Marketing Cloud, Snowflake Lakehouse, Bedrock AI</td><td>Global elastic scale</td></tr>
          <tr><td>Sovereign Regional Enclaves</td><td>AWS European Sovereign / Hyperforce</td><td>Passenger PII, loyalty accounts, payments, Data Cloud</td><td>GDPR / Singapore PDPA compliance</td></tr>
          <tr><td>Airport Edge Kiosks & Gates</td><td>On-Premise Kubernetes (EKS Anywhere)</td><td>CUSS check-in kiosks, biometric boarding gate scanners, DCS local cache</td><td>4-hour WAN blackout survival</td></tr>
          <tr><td>In-Flight Avionics</td><td>Aircraft Server (ARINC 834 / ACARS)</td><td>Electronic Flight Bags (EFBs), In-Flight Entertainment (IFE)</td><td>DO-178C aviation safety certified</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Edge Survivability Architecture</div>
        <p><strong>The Disconnected Airport Problem:</strong> If an undersea fiber cable breaks and Changi or Frankfurt Airport loses connection to AWS, flights must still depart on time.</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #10b981;">Local DCS Cache Protocol</div>
          <p>Flight manifests and seat allocations are pushed to local airport edge servers 4 hours prior to departure. Boarding gates continue scanning passes locally and reconcile asynchronously once connectivity restores.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "Show the audience the edge architecture. Flights must depart even if the entire internet goes down."
})

# Now let's append remaining slides 16 to 52 for Airlines
# PART 4: 13-LAYER ARCHITECTURE & VARIATIONS (16-20)
slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "13-Layer Architectural Topology Overview",
    "subtitle": "The complete enterprise stack from mission-critical operations to customer touchpoints",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The 13 Enterprise Dimensions</div>
        <table class="data-table">
          <tr><th>#</th><th>Layer Name</th><th>Core Capability</th></tr>
          <tr><td>1</td><td>Core Operational Stack</td><td>PSS, DCS, MRO, FlightOps, Crew Tracking</td></tr>
          <tr><td>2</td><td>Marketing Automation & AdTech</td><td>Journey orchestration, dynamic pricing, adtech</td></tr>
          <tr><td>3</td><td>CRM & Service Desk</td><td>Omni-channel desktop, telephony CTI, messaging</td></tr>
          <tr><td>4</td><td>Loyalty Management</td><td>Frequent flyer miles ledger, tier status, co-brand</td></tr>
          <tr><td>5</td><td>Customer Data Platform (CDP)</td><td>Real-time ingestion, identity graph, golden record</td></tr>
          <tr><td>6</td><td>Integration & Event Mesh</td><td>API gateway, iPaaS, Kafka event streaming</td></tr>
          <tr><td>7</td><td>Cloud & Lakehouse</td><td>Compute, Snowflake/Databricks, relational DBs</td></tr>
          <tr><td>8</td><td>AI & Agentic Systems</td><td>Frontier LLMs, autonomous agents, predictive ML</td></tr>
          <tr><td>9</td><td>Web & Mobile Front-Ends</td><td>Next.js booking, native iOS/Android, Apple Wallet</td></tr>
          <tr><td>10</td><td>Headless CMS & DAM</td><td>Contentful/AEM, Cloudinary DAM, 40+ locales</td></tr>
          <tr><td>11</td><td>Finance & ERP</td><td>ASC 606 revenue accounting, SAP S/4HANA, Adyen</td></tr>
          <tr><td>12</td><td>HR & Crew Scheduling</td><td>Workday HCM, Jeppesen crew legality, payroll</td></tr>
          <tr><td>13</td><td>Governance & Security</td><td>CyberArk PAM, HashiCorp Vault HSM, OneTrust</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Architectural Cohesion Principles</div>
        <p><strong>Decoupled but Harmonized:</strong> No single software vendor can or should supply all 13 layers. The winning enterprise architecture establishes clean data contracts and API boundaries between Core Operations (Amadeus/Sabre), Commercial Retailing (Salesforce/Adobe), and Analytical Intelligence (Snowflake/Databricks).</p>
        <div style="margin-top: 1rem;">
          <div class="card-header" style="color: #3b82f6;">Next Slides: The 3 Stack Variations</div>
          <p>We evaluate this 13-layer topology across 3 strategic variations: <strong>With Salesforce</strong>, <strong>Without Salesforce</strong>, and <strong>The Best Money Can Buy</strong>.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "Frame the 13 layers. This provides the blueprint for the deep-dive comparisons that follow."
})

slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "Variation 1: The Salesforce-Centric Ecosystem",
    "subtitle": "Unified customer data fabric and autonomous agentic workflows layered on industry core",
    "content": """
    <div class="grid-3" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="metric-hero">$12.5M - $18.8M</div>
        <div class="metric-sub">Annual Software ACV</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">MuleSoft + Data Cloud + Agentforce + Service Cloud + Marketing Cloud.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #10b981;">11 Months</div>
        <div class="metric-sub">Payback Period</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Fastest time-to-value via out-of-the-box Travel & Hospitality DMOs.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #8b5cf6;">310%</div>
        <div class="metric-sub">3-Year Projected ROI</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">$48M in cumulative benefits from deflection, upselling, and retention.</p>
      </div>
    </div>
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Core Stack Components</div>
        <p>• <strong>Data Cloud for Travel:</strong> Ingests Altéa PSS events via MuleSoft; creates unified golden passenger profiles with Zero-Copy Snowflake sharing.</p>
        <p>• <strong>Agentforce & Atlas Engine:</strong> Autonomous agents handling storm rebooking, baggage tracking, and ancillary upselling.</p>
        <p>• <strong>Service Cloud Voice (Amazon Connect):</strong> Unified CTI telephony and digital messaging (WhatsApp, SMS).</p>
        <p>• <strong>Marketing Cloud Engagement & Personalization:</strong> Pre-flight ancillary offers and triggered alerts.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Primary Strategic Moat</div>
        <p><strong>Zero-Copy Data Harmonization + Pre-Built DMOs:</strong> Eliminates millions in custom ETL pipeline engineering. Native Agentforce agents operate directly against grounded enterprise metadata with full OLS/FLS security enforcement.</p>
      </div>
    </div>
    """,
    "notes": "Highlight the Salesforce advantage: fast time-to-value and pre-built industry data models."
})

slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "Variation 2: Composable Best-of-Breed (No Salesforce)",
    "subtitle": "Decoupled open cloud architecture: Snowflake, Braze, Dynamics 365, Talon.One, and Kafka",
    "content": """
    <div class="grid-3" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="metric-hero">$9.8M - $15.2M</div>
        <div class="metric-sub">Annual Software ACV</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Lower initial SaaS licensing costs; higher internal engineering overhead.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #10b981;">15 Months</div>
        <div class="metric-sub">Payback Period</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Requires custom data platform engineering and custom agent development.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #8b5cf6;">245%</div>
        <div class="metric-sub">3-Year Projected ROI</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">$38M cumulative benefits with maximum architectural flexibility.</p>
      </div>
    </div>
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Core Stack Components</div>
        <p>• <strong>Snowflake & Databricks:</strong> Central lakehouse with Apache Iceberg / Delta Lake tables.</p>
        <p>• <strong>Twilio Segment / mParticle:</strong> Warehouse-native CDP with reverse ETL (RudderStack).</p>
        <p>• <strong>Braze Enterprise:</strong> Streaming push/SMS/email messaging with sub-second delivery.</p>
        <p>• <strong>Microsoft Dynamics 365 / Zendesk:</strong> Omni-channel service desk with Genesys Cloud CX.</p>
        <p>• <strong>Talon.One & OpenLoyalty:</strong> Headless rule-based promotion and loyalty engine.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Primary Strategic Moat</div>
        <p><strong>Zero Platform Lock-in:</strong> Complete developer autonomy. Every component is replaceable via open APIs. In-house AI engineering teams fine-tune custom LLM models on AWS Bedrock and Databricks Mosaic AI without paying SaaS platform markups.</p>
      </div>
    </div>
    """,
    "notes": "Be fair to the composable stack. It offers great flexibility, but requires high engineering headcount."
})

slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "Variation 3: The Best Platforms Money Can Buy",
    "subtitle": "Unconstrained budget, sovereign-grade pinnacle: Palantir Foundry, Adobe AEP, and Altéa Private Cloud",
    "content": """
    <div class="grid-3" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="metric-hero">$28.5M - $45.0M</div>
        <div class="metric-sub">Annual Software ACV</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">The apex of enterprise technology; sovereign dedicated deployments.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #10b981;">14 Months</div>
        <div class="metric-sub">Payback Period</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Rapid payback driven by massive fuel savings and premium yield capture.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #8b5cf6;">420%</div>
        <div class="metric-sub">3-Year Projected ROI</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">$145M+ cumulative benefits via total IROPS cost avoidance and VIP yield.</p>
      </div>
    </div>
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Core Stack Components</div>
        <p>• <strong>Palantir Foundry & AIP:</strong> Enterprise operational digital twin fusing avionics, crew, radar, and PNRs.</p>
        <p>• <strong>Adobe Experience Cloud (AEP + AJO + AEM):</strong> Sub-50ms streaming personalization globally.</p>
        <p>• <strong>Amadeus Altéa Dedicated Private Cloud:</strong> 99.999% SLA with dedicated hardware isolation.</p>
        <p>• <strong>Genesys Sovereign + Google CCAI + Nuance:</strong> Instant voice biometrics (< 3s) and zero fraud.</p>
        <p>• <strong>CyberArk + HashiCorp HSM + Zscaler:</strong> Military-grade defense-in-depth zero-trust security.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Primary Strategic Moat</div>
        <p><strong>Military-Grade Operational Supremacy:</strong> Palantir AIP simulates 500 crisis permutations in 30 seconds during typhoon shutdowns; Adobe AEP captures $45M in premium direct bookings; zero breach risk across biometric passenger registries.</p>
      </div>
    </div>
    """,
    "notes": "The ultra-tier stack is what Emirates, Singapore Airlines, or Delta deploy when failure is not an option."
})

slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "Cross-Variation Financial & TCO Comparison Matrix",
    "subtitle": "Complete 3-year Total Cost of Ownership (TCO) breakdown across all 3 variations",
    "content": """
    <div class="glass-card">
      <table class="data-table">
        <tr><th>Cost / Value Dimension</th><th>Variation 1: With Salesforce</th><th>Variation 2: Without Salesforce</th><th>Variation 3: Best Money Can Buy</th></tr>
        <tr><td><strong>Annual Software Licensing (ACV)</strong></td><td>$14.5M / year</td><td>$12.2M / year</td><td>$35.0M / year</td></tr>
        <tr><td>Implementation CapEx (Year 1)</td><td>$16.5M</td><td>$20.5M (higher custom build)</td><td>$45.0M (sovereign custom build)</td></tr>
        <tr><td>Annual Internal Engineering Payroll</td><td>$4.8M / year (32 engineers)</td><td>$8.2M / year (55 engineers)</td><td>$14.0M / year (85 elite engineers)</td></tr>
        <tr><td>Annual Cloud Infra & Compute Run Cost</td><td>$1.8M / year</td><td>$3.5M / year (custom Spark/Kafka)</td><td>$7.5M / year (NVIDIA DGX clusters)</td></tr>
        <tr><td><strong>Total 3-Year TCO</strong></td><td><strong>$66.8M</strong></td><td><strong>$75.6M</strong></td><td><strong>$194.5M</strong></td></tr>
        <tr><td>Cumulative 3-Year Financial Benefit</td><td>$158.0M</td><td>$142.0M</td><td>$425.0M</td></tr>
        <tr><td><strong>Net Economic Value Generated</strong></td><td><strong>+$91.2M</strong></td><td><strong>+$66.4M</strong></td><td><strong>+$230.5M</strong></td></tr>
        <tr><td><strong>Time-to-Production-Value</strong></td><td><strong>9 Months</strong></td><td><strong>16 Months</strong></td><td><strong>14 Months</strong></td></tr>
      </table>
    </div>
    <div class="grid-2" style="margin-top: 1rem;">
      <div class="glass-card">
        <div class="card-header">The Hidden Engineering Payroll Trap</div>
        <p>While Variation 2 appears cheaper on software licensing ($12.2M vs $14.5M), it requires 23 additional data and integration engineers ($3.4M/year payroll), making its total 3-year TCO <strong>$8.8M higher</strong> than Variation 1.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Variation 3's Asymmetric Return</div>
        <p>Variation 3 costs nearly 3x more ($194.5M TCO), but generates <strong>$230.5M in net economic value</strong> by eliminating fuel waste, automating complex IROPS recovery, and maximizing ultra-premium cabin pricing power.</p>
      </div>
    </div>
    """,
    "notes": "Show the CFO the math. Cheap software with expensive custom engineering is the most expensive mistake in enterprise IT."
})

# PART 5: TOOL COMPLEMENTARITY & SYSTEM HANDOFFS (21-25)
slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "The Four Systems Framework in Aviation",
    "subtitle": "Classifying enterprise tools across Record, Intelligence, Engagement, and Action",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header" style="color: #3b82f6;">1. System of Record (Source of Truth)</div>
        <p>• <strong>Amadeus Altéa / SabreSonic:</strong> Master record for seat inventory, PNRs, and e-Tickets.</p>
        <p>• <strong>SAP S/4HANA Finance:</strong> Master general ledger and revenue recognition.</p>
        <p>• <strong>Swiss-AS AMOS:</strong> Master aircraft technical logbook and airworthiness records.</p>
        <p>• <strong>Workday HCM:</strong> Master pilot and flight attendant employee records.</p>
      </div>
      <div class="glass-card">
        <div class="card-header" style="color: #10b981;">2. System of Intelligence (The Brain)</div>
        <p>• <strong>Salesforce Data Cloud / Snowflake:</strong> Unified Passenger 360 data lakehouse.</p>
        <p>• <strong>PROS Dynamic Pricing:</strong> Real-time willingness-to-pay revenue management.</p>
        <p>• <strong>Palantir Foundry / AIP:</strong> Operational fleet and disruption simulation engine.</p>
        <p>• <strong>Databricks Mosaic AI:</strong> Predictive maintenance and fuel optimization models.</p>
      </div>
      <div class="glass-card">
        <div class="card-header" style="color: #8b5cf6;">3. System of Engagement (The Interfaces)</div>
        <p>• <strong>Salesforce Service Cloud:</strong> Unified omni-channel contact center agent desktop.</p>
        <p>• <strong>Marketing Cloud / Braze:</strong> Mobile push, email, SMS, and WhatsApp alerts.</p>
        <p>• <strong>Native iOS/Android Apps:</strong> Passenger digital boarding pass and trip companion.</p>
        <p>• <strong>SITA Smart Path:</strong> Airport check-in kiosks and biometric boarding gates.</p>
      </div>
      <div class="glass-card">
        <div class="card-header" style="color: #f59e0b;">4. System of Action (Autonomous Execution)</div>
        <p>• <strong>Agentforce Atlas Engine:</strong> Autonomous multi-agent IROPS rebooking execution.</p>
        <p>• <strong>MuleSoft Anypoint:</strong> Universal API execution and protocol translation.</p>
        <p>• <strong>Adyen Unified Commerce:</strong> Automated payment capture, refund, and voucher issuance.</p>
        <p>• <strong>Jeppesen Crew Tracking:</strong> Automated pilot re-rostering during duty hour timeouts.</p>
      </div>
    </div>
    """,
    "notes": "The Four Systems framework clarifies architecture: tools should not try to be everything to everyone."
})

slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "Detailed System Synergy & Hand-Off Matrix",
    "subtitle": "Mapping exact data hand-offs, triggers, and protocols between core aviation platforms",
    "content": """
    <div class="glass-card">
      <table class="data-table">
        <tr><th>Source Platform</th><th>Target Platform</th><th>Trigger Event</th><th>Protocol / Payload</th><th>Handoff Outcome</th></tr>
        <tr><td>Amadeus Altéa PSS</td><td>MuleSoft ➔ Data Cloud</td><td>PNR Created / Modified</td><td>Type X / JSON CDC stream</td><td>Unified Passenger profile updated in real-time</td></tr>
        <tr><td>Data Cloud</td><td>Marketing Cloud</td><td>Segment Membership Change</td><td>Native Zero-Copy Sync</td><td>Triggers personalized 72-hour pre-flight upsell email</td></tr>
        <tr><td>FlightAware / ACARS</td><td>Confluent Kafka</td><td>Flight Delayed > 120 min</td><td>CloudEvents JSON</td><td>Broadcasts disruption event to all operational systems</td></tr>
        <tr><td>Confluent Kafka</td><td>Agentforce Service Agent</td><td>Disruption Event Ingested</td><td>gRPC / Pub/Sub API</td><td>Agentforce initiates autonomous passenger rebooking workflow</td></tr>
        <tr><td>Agentforce</td><td>Amadeus Altéa PSS</td><td>Rebooking Selected</td><td>REST via MuleSoft (OAS3)</td><td>Modifies PNR seat, re-issues e-Ticket coupon (EMD)</td></tr>
        <tr><td>Agentforce</td><td>Adyen Payment Gateway</td><td>Compensation Entitlement</td><td>HTTPS REST / OAuth2</td><td>Disburses instant digital meal voucher to Apple Wallet</td></tr>
        <tr><td>SITA WorldTracer</td><td>Service Cloud</td><td>Baggage Scan Mismatch</td><td>SITA Type B / MQ Series</td><td>Creates proactive baggage recovery case for airport concierge</td></tr>
      </table>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Architectural Principle: Event-Driven Handoffs</div>
      <p>Notice that no operational system directly polls another database. All handoffs are <strong>event-driven</strong>, asynchronous, and mediated by enterprise integration layers (MuleSoft / Kafka), guaranteeing fault isolation.</p>
    </div>
    """,
    "notes": "Walk through the exact mechanics of how Altéa, Data Cloud, Agentforce, and Adyen collaborate."
})

slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "Data Contracts & State Transition Architecture",
    "subtitle": "Formalizing PNR and Ticket lifecycles to prevent race conditions and inventory corruption",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">PNR State Machine Transitions</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>BOOKED (Open):</strong> Reservation created, seat held, fare quotation active, ticketing time limit (TTL) running.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>TICKETED (Confirmed):</strong> 13-digit e-Ticket and EMD issued; revenue recognized as unearned liability (UPR).</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>CHECKED-IN (Airport):</strong> Seat confirmed in DCS; boarding pass issued; baggage tags printed; APIS sent.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div><strong>BOARDED (Gate):</strong> Biometric facial scan matched at gate; passenger marked on-board; trim sheet finalized.</div></div>
        <div class="flow-step"><div class="step-num">5</div><div><strong>FLOWN (Lifted):</strong> Flight wheels-up; e-Ticket coupon lifted; revenue recognized in General Ledger (ASC 606).</div></div>
      </div>
      <div class="glass-card">
        <div class="card-header">Data Contract Schema (CloudEvents Avro)</div>
        <pre style="background: rgba(0,0,0,0.5); padding: 0.6rem; border-radius: 6px; font-size: 0.68rem; color: #93c5fd;"><code>{
  "specversion": "1.0",
  "type": "com.airline.pnr.state_changed",
  "source": "/altea/sin/reservation",
  "id": "A6B8C9-9876-4321",
  "time": "2026-09-20T14:32:00Z",
  "datacontenttype": "application/json",
  "data": {
    "pnr_locator": "X7K9LP",
    "previous_state": "TICKETED",
    "new_state": "CHECKED_IN",
    "passenger_id": "IND-884920",
    "flight_number": "SQ322",
    "seat_assignment": "14K",
    "checked_bags": 2
  }
}</code></pre>
      </div>
    </div>
    """,
    "notes": "State transitions must be strict. A passenger cannot be marked 'Flown' without passing through 'Boarded'."
})

slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "Real-Time Operational Handoff Sequence Diagram",
    "subtitle": "End-to-end trace of an autonomous IROPS flight delay rebooking interaction",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
sequenceDiagram
    autonumber
    participant FO as Flight Operations (ACARS)
    participant K as Confluent Kafka Mesh
    participant DC as Salesforce Data Cloud
    participant AF as Agentforce Atlas Engine
    participant PSS as Amadeus Altéa PSS
    participant P as Passenger Mobile / WhatsApp

    FO->>K: Publish flight.delay.exceeds_threshold (SQ322 delayed 4h)
    K->>DC: Ingest delay event via Kafka connector
    DC->>AF: Trigger IROPS Rebooking Agent for affected passengers
    AF->>DC: Query Passenger 360 (Tier: PPS Solitaire, Lifetime Spend: $180k)
    AF->>PSS: Check seat inventory on next best flight (SQ324) via MuleSoft
    PSS-->>AF: Seat available in Business Class (12A)
    AF->>P: Send personalized WhatsApp message with 1-click rebook option
    P->>AF: Clicks "Accept Rebooking on SQ324"
    AF->>PSS: Execute PNR re-accommodation & reissue e-Ticket coupon
    PSS-->>AF: PNR updated successfully (Locator: X7K9LP)
    AF->>P: Send updated Apple Wallet boarding pass & $50 lounge credit QR
      </div>
    </div>
    <div class="glass-card" style="margin-top: 0.8rem;">
      <p style="font-size: 0.75rem; color: var(--text-muted);"><strong>Elapsed Time:</strong> Entire sequence executes in <strong>4.2 seconds</strong> without human call center agent intervention, eliminating phone hold queues during storm groundings.</p>
    </div>
    """,
    "notes": "Walk through this sequence step by step. This demonstrates true multi-agent operational autonomy."
})

slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "Distributed State Consistency & Race Conditions",
    "subtitle": "Preventing double-booking and inventory corruption across simultaneous digital channels",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The Aviation Race Condition Problem</div>
        <p><strong>The Simultaneous Update Dilemma:</strong> During a flight disruption, a passenger is trying to rebook on their mobile app, while an airport customer service agent at the transfer desk opens the same PNR, and an automated rebooking bot executes in the background.</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #ef4444;">Consequences of Unmanaged State</div>
          <p>• PNR lockouts in Altéa PSS (error: <em>"Record in Use by Another Agent"</em>).<br>• Duplicate seat assignments on alternative flights.<br>• Mismatched e-Ticket coupons and uncollected fare differences.</p>
        </div>
      </div>
      <div class="glass-card">
        <div class="card-header">Architectural Solution: Optimistic Locking & Mutex</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Distributed Redis Lock (Redlock):</strong> Acquire a 15-second distributed mutex lock on the PNR locator across all digital channels before initiating modification.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Optimistic Concurrency Control (OCC):</strong> Pass the current PNR version timestamp. If the version changed during user review, reject the write and refresh the UI.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Idempotency Keys:</strong> Every payment and ticket issuance API request carries a unique UUID idempotency key to prevent double charging.</div></div>
      </div>
    </div>
    """,
    "notes": "Technical depth: Distributed locking and idempotency are mandatory when multiple channels touch a PNR."
})

# PART 6: DATA INGESTION, MODELING, SORTING & LAKEHOUSE (26-30)
slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Multi-Tier Ingestion Architecture",
    "subtitle": "Harmonizing 4 distinct ingestion velocities: Batch, Micro-Batch, Streaming CDC, and Real-Time gRPC",
    "content": """
    <div class="grid-4" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="card-header">1. Real-Time gRPC / Pub/Sub</div>
        <div class="metric-hero" style="font-size: 1.2rem; color: #3b82f6;">< 10 ms</div>
        <p style="color: var(--text-muted);">Flight radar tracking, gate boarding scans, and passenger panic alerts.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">2. Streaming CDC (Kafka)</div>
        <div class="metric-hero" style="font-size: 1.2rem; color: #10b981;">< 100 ms</div>
        <p style="color: var(--text-muted);">PNR state changes, ticket issuance, baggage tracking, and web clickstreams.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">3. Micro-Batch (5-15 min)</div>
        <div class="metric-hero" style="font-size: 1.2rem; color: #8b5cf6;">5 - 15 min</div>
        <p style="color: var(--text-muted);">Co-brand credit card swipe authorizations and partner hotel stay accruals.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">4. Batch ETL / Nightly</div>
        <div class="metric-hero" style="font-size: 1.2rem; color: #f59e0b;">Daily / 24h</div>
        <p style="color: var(--text-muted);">IATA BSP/ARC settlement files, fuel burn logs, and crew payroll files.</p>
      </div>
    </div>
    <div class="glass-card">
      <div class="card-header">Ingestion Flow Architecture</div>
      <p>All streaming sources feed into <strong>Confluent Cloud Kafka</strong> topics. Kafka streams raw JSON/Avro payloads into <strong>Salesforce Data Cloud</strong> for sub-second operational profile unification, while simultaneously sinking raw parquet data into the <strong>Snowflake Analytical Lakehouse</strong> via Kafka Connect Snowpipe Streaming.</p>
    </div>
    """,
    "notes": "Explain data velocity. Not all data needs to be sub-second; separating streaming from batch saves millions in compute."
})

slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Domain Data Model Objects (DMOs) & Schemas",
    "subtitle": "Standardized canonical data models for aviation customer and operational entities",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Core Aviation DMO Entities</div>
        <table class="data-table">
          <tr><th>DMO Name</th><th>Key Attributes</th><th>Primary Relationships</th></tr>
          <tr><td><code>Individual</code></td><td>PartyId, FirstName, LastName, PassportHash, DateOfBirth</td><td>ContactPoints, LoyaltyAccounts</td></tr>
          <tr><td><code>FlightLeg</code></td><td>FlightNumber, DepartureAirport, ArrivalAirport, STD, STA</td><td>AircraftTail, PassengerBookings</td></tr>
          <tr><td><code>PassengerBooking</code></td><td>PNRLocator, TicketNumber, CabinClass, SeatNumber</td><td>Individual, FlightLeg</td></tr>
          <tr><td><code>LoyaltyAccount</code></td><td>ProgramId, TierStatus, LifetimeSpend, MilesBalance</td><td>Individual, Transactions</td></tr>
          <tr><td><code>BaggageItem</code></td><td>BagTagNumber, WeightKg, RFIDStatus, CurrentLocation</td><td>PassengerBooking, FlightLeg</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Calculated Insights & Real-Time Aggregations</div>
        <p>Data Cloud runs continuous real-time aggregations on top of DMOs to generate high-value operational metrics:</p>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Customer Lifetime Value (CLTV):</strong> 36-month gross passenger revenue across flights, ancillaries, and co-brand spend.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Disruption Propensity Score:</strong> Historical count of delays experienced in past 12 months (used to prioritize VIP recovery).</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Upgrade Willingness Index:</strong> Machine learning score indicating probability of buying a premium economy/business upgrade.</div></div>
      </div>
    </div>
    """,
    "notes": "Show the data model. DMOs standardize messy PSS and GDS formats into clean enterprise entities."
})

slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Identity Resolution: Deterministic vs Probabilistic",
    "subtitle": "Unifying fragmented anonymous browsing, corporate booking codes, and loyalty profiles into a Golden Record",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Identity Matching Hierarchy</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Tier 1: Deterministic Exact Match (100% Confidence):</strong> Verified Frequent Flyer Number + Last Name, or SHA-256 Hashed Passport Number + Country Code.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Tier 2: Strong Semi-Deterministic Match (95% Confidence):</strong> Hashed Email Address + Mobile Phone Number (with international dialing code).</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Tier 3: Probabilistic Fuzzy Match (80% Confidence):</strong> First Name + Last Name + Billing Postal Code + Device ID graph.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div><strong>Tier 4: Anonymous Session (Cookie / Device ID):</strong> Anonymous browsing on Airline.com until booking or sign-in occurs.</div></div>
      </div>
      <div class="glass-card">
        <div class="card-header">The OTA Passenger Re-Identification Miracle</div>
        <p><strong>The Problem:</strong> When a corporate traveler books an airline ticket through Expedia or Amex GBT, the OTA frequently withholds the passenger's real email address, passing a masked relay email (e.g. <code>sq.83920@expedia-relay.com</code>).</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #10b981;">Data Cloud Resolution Engine</div>
          <p>Data Cloud matches the passenger's <strong>First Name + Last Name + Mobile Phone Number</strong> entered during mobile check-in to their existing loyalty profile, instantly merging the OTA booking into the Golden Record and unlocking personalized service.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "This is a massive commercial moat. Re-identifying OTA bookers allows airlines to reclaim the direct relationship."
})

slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Lakehouse Data Layering: Medallion Architecture",
    "subtitle": "Structuring aviation big data across Bronze (Raw), Silver (Harmonized), and Gold (Business 360) tiers",
    "content": """
    <div class="grid-3">
      <div class="glass-card" style="border-top: 3px solid #f59e0b;">
        <div class="card-header">Bronze Tier (Raw Ingestion)</div>
        <p>• Unaltered append-only raw data lakes (S3 / GCS).</p>
        <p>• Stores raw Type B teletype messages, SITA BagMessage streams, and web server clickstreams.</p>
        <p>• Retained for 7+ years for regulatory compliance and audit trails.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #9ca3af;">
        <div class="card-header">Silver Tier (Cleaned & Harmonized)</div>
        <p>• Schema validated, deduplicated, and enriched.</p>
        <p>• Delta Lake / Iceberg tables matching canonical DMOs.</p>
        <p>• PNR changes harmonized into unified flight leg records; currency conversions normalized to USD/EUR.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #eab308;">
        <div class="card-header">Gold Tier (Business & AI Ready)</div>
        <p>• Aggregated, feature-engineered tables for BI and ML.</p>
        <p>• Passenger 360 view, route profitability dashboards, and dynamic pricing training feature stores.</p>
        <p>• High-performance sub-second SQL querying via Snowflake and Databricks SQL.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Zero-Copy Federation: Bridging Gold to Salesforce</div>
      <p>Salesforce Data Cloud queries Snowflake Gold tables in-place using <strong>Zero-Copy Open Data Sharing</strong>. The CRM never copies petabytes of historical flight logs, eliminating data synchronization lag and storage egress fees.</p>
    </div>
    """,
    "notes": "Explain the Medallion architecture. Zero-copy federation between Snowflake Gold and Data Cloud is the holy grail."
})

slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Data Governance, Cataloging & Lineage",
    "subtitle": "End-to-end data tracking from cockpit ACARS sensor to C-Suite financial earnings reports",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Collibra Enterprise Data Catalog</div>
        <table class="data-table">
          <tr><th>Governance Pillar</th><th>Implementation</th><th>Regulatory Requirement</th></tr>
          <tr><td>Business Glossary</td><td>Standardized definitions for 1,200+ aviation terms (e.g. RevPAS, ASK, RPK)</td><td>Eliminates boardroom reporting discrepancies</td></tr>
          <tr><td>Data Lineage</td><td>Visual DAG tracking data flow from Altéa PSS through Kafka to SAP General Ledger</td><td>Mandatory for Sarbanes-Oxley (SOX) audit compliance</td></tr>
          <tr><td>Sensitive Data Tagging</td><td>Automated classification of PII, PCI, and biometric attributes</td><td>Enforces GDPR and Singapore PDPA encryption rules</td></tr>
          <tr><td>Data Quality Scoring</td><td>Automated Great Expectations tests validating PNR schema completeness</td><td>Prevents dirty data from entering AI model training sets</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Automated Data Lineage in Practice</div>
        <p>When the Chief Commercial Officer reviews the monthly revenue report showing a $4.2M ancillary yield uplift, Collibra provides click-through lineage showing the exact 12 SQL transformations, 4 Kafka topics, and raw Altéa EMD transactions that produced that metric.</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #3b82f6;">Audit Defense Moat</div>
          <p>Reduces annual financial and regulatory audit preparation time from 6 weeks to 3 hours, saving $2.5M in external consulting audit fees.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "Data governance is not glamorous, but it is what prevents multi-million-dollar SOX compliance failures."
})

# PART 7: END-TO-END CUSTOMER JOURNEYS (31-36)
slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 1: Inspiration, Metasearch Bidding & Search",
    "subtitle": "Capturing traveler intent across Google Flights, Skyscanner, and direct brand discovery",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Metasearch Bidding Architecture (Google Flights / Skyscanner)</div>
        <p>• <strong>The Problem:</strong> Metasearch engines query airline shopping APIs billions of times per day with look-to-book ratios exceeding 1,000:1. If an airline cannot respond in < 250ms, Google drops the airline from results.</p>
        <p>• <strong>Architectural Solution:</strong> Deploy <strong>Vercel Edge Caching</strong> and <strong>Amadeus Instant Search</strong> pre-computed fare caches at the CDN edge, absorbing 95% of shopping volume without hitting core PSS inventory servers.</p>
        <p>• <strong>Algorithmic Bidding (Koddi / AI):</strong> Dynamically adjust CPC bids on Google Flights based on real-time flight load factors—bid aggressively on empty flights, bid zero on sold-out flights.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 1: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Traveler searches "SIN to LHR" on Google Flights.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>Amadeus Instant Search API responds in 85ms with verified live fare ($1,150).</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>Traveler clicks deep-link directly into Airline.com Next.js booking engine.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>Client-side SDK captures anonymous session cookie and registers intent topic in Kafka.</div></div>
      </div>
    </div>
    """,
    "notes": "Explain how look-to-book caching protects the PSS core from being overwhelmed by Google Flights bots."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 2: Booking, Dynamic Pricing & Ancillaries",
    "subtitle": "Converting shoppers into booked passengers with personalized willingness-to-pay bundles",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Continuous Pricing & Merchandising Engine</div>
        <p>• <strong>AI-Driven Dynamic Pricing:</strong> Replaces rigid 26-bucket ATPCO fares with continuous pricing curves powered by PROS. Evaluates competitor fares, remaining seat inventory, and days-to-departure in real time.</p>
        <p>• <strong>Contextual Ancillary Bundling:</strong> If the traveler is flying with a family (2 adults, 2 children), the booking engine automatically bundles adjacent seats and 2 checked bags at a 20% bundle discount.</p>
        <p>• <strong>Frictionless Payment:</strong> Adyen Unified Commerce presents localized payment methods (Apple Pay, Google Pay, GrabPay in Singapore, WeChat Pay in China, iDEAL in Netherlands).</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 2: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Traveler selects flight; PROS computes dynamic fare ($1,142.50).</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>Agentforce recommends extra legroom seat bundle based on user height/travel history.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>Traveler completes purchase with Apple Pay in 4 seconds.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>MuleSoft orchestrates simultaneous writes: Altéa issues PNR/EMD; Adyen settles payment; Data Cloud creates Passenger 360 profile.</div></div>
      </div>
    </div>
    """,
    "notes": "Dynamic bundling and Apple Pay can increase booking conversion by up to 18%."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 3: Pre-Departure Engagement & Upsell",
    "subtitle": "Automated 72-hour pre-flight journeys: Seat upgrade bidding, lounge passes, and baggage",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Automated Pre-Flight Journey Trigger</div>
        <p>• <strong>T-72 Hours:</strong> Marketing Cloud sends personalized email/WhatsApp: <em>"Your flight to London is in 3 days. Bid for a Business Class upgrade starting at $350."</em></p>
        <p>• <strong>Plusgrade / Dynamic Upgrade Auction:</strong> Passengers submit bids for unsold premium cabin seats; algorithm accepts optimal bids 24 hours prior to departure to maximize RevPAS.</p>
        <p>• <strong>T-24 Hours:</strong> Mobile check-in opens. Automated push notification directs passenger to native app for 1-click check-in and Apple Wallet boarding pass download.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 3: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Data Cloud triggers Marketing Cloud Journey Builder at exact T-72h timestamp.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>Passenger submits $420 upgrade bid via Plusgrade embedded mobile webview.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>At T-24h, revenue management algorithm clears bid; Altéa updates PNR cabin class from Economy (Y) to Business (J).</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>Apple Wallet boarding pass automatically updates via APNS push notification showing new seat (14K).</div></div>
      </div>
    </div>
    """,
    "notes": "Apple Wallet boarding passes update automatically via push notification. This delights customers and saves gate agent time."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 4: Day-of-Travel & Biometric Gate Boarding",
    "subtitle": "Curb-to-gate frictionless terminal navigation: SITA Smart Path, bag-drop, and facial recognition",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">SITA Smart Path Biometric Workflow</div>
        <p>• <strong>Curb Check-in / Bag-Drop:</strong> Traveler scans passport at kiosk; camera captures high-resolution facial template matched against ICAO e-Passport chip.</p>
        <p>• <strong>Tokenized Biometric Token:</strong> A temporary single-day cryptographic token is generated, linking the passenger's face to their PNR and boarding pass.</p>
        <p>• <strong>Security & Lounge:</strong> Passenger walks through automated security turnstiles and airline lounge doors without showing physical passport or boarding pass.</p>
        <p>• <strong>Biometric Gate Boarding:</strong> Camera at gate matches face in < 300ms, marks passenger as 'Boarded' in Altéa DCS, and opens the e-Gate.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 4: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Passenger arrives at Changi Terminal 3; biometric token verified at automated bag-drop.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>SITA BagMessage streams RFID bag tag scan (SQ849201) to Kafka topic.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>Passenger approaches Gate B4; SITA e-Gate camera captures face, verifies token, opens gate.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>Altéa DCS marks seat 14K 'BOARDED'; trim sheet load control updates weight & balance instantly.</div></div>
      </div>
    </div>
    """,
    "notes": "Biometrics cut boarding time for an A350 from 40 minutes to 18 minutes, directly improving aircraft utilization."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 5: In-Flight Experience & Connected Crew",
    "subtitle": "Real-time in-flight Wi-Fi, crew tablet intelligence, and personalized cabin service",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Connected Crew Tablet Application</div>
        <p>• <strong>Offline-First Cabin Tablet:</strong> Flight attendants carry secure iPads loaded with the passenger manifest, dietary requirements, and loyalty status.</p>
        <p>• <strong>Contextual Recognition:</strong> Tablet alerts cabin crew: <em>"Seat 14K is Dr. Tan, a Solitaire PPS member celebrating his wedding anniversary. His favorite drink is Singapore Sling."</em></p>
        <p>• <strong>In-Flight Problem Resolution:</strong> If an in-flight entertainment screen malfunctions, the purser immediately issues a $100 travel voucher or 10,000 KrisFlyer miles directly from the tablet.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 5: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Crew iPads synchronize final boarding manifest via gate Wi-Fi 5 minutes before door close.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>In-flight: Passenger connects to satellite Wi-Fi; portal authenticates loyalty status via Starlink link.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>Purser logs IFE malfunction on seat 14K via Service Cloud offline tablet app.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>Upon landing, tablet syncs via cellular; 10,000 miles post instantly to passenger's account with an automated apology email.</div></div>
      </div>
    </div>
    """,
    "notes": "Service recovery in the air turns angry passengers into loyal brand advocates before they even step off the plane."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 6: Disruption Recovery & Autonomous IROPS",
    "subtitle": "Automated multi-agent crisis orchestration during severe weather groundings and EU261 events",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The Severe Weather Crisis Scenario</div>
        <p><strong>The Incident:</strong> A super-typhoon shuts down Hong Kong International Airport (HKG) for 18 hours. 42 inbound flights are diverted; 65 outbound flights are cancelled; 16,000 passengers are stranded.</p>
        <p><strong>The Old Way (Manual Collapse):</strong> 6-hour phone wait times, transfer desk queues spilling into airport corridors, lost luggage, and $8M in avoidable EU261 compensation claims.</p>
        <p><strong>The New Way (Agentforce Autonomous IROPS):</strong> Multi-agent AI resolves 85% of stranded passengers in 20 minutes without human intervention.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 6: Autonomous Recovery Sequence</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Triage Agent:</strong> Categorizes 16,000 passengers by loyalty tier, connecting flights, and visa eligibility.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Rebooking Agent:</strong> Autonomously reserves seats on alternative partner flights via Altéa PSS and Star Alliance APIs.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Logistics Agent:</strong> Provisions hotel vouchers at airport transit hotels via automated API integration.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div><strong>Compensation Agent:</strong> Disburses digital meal QR codes to Apple Wallet and files automated EU261 claims.</div></div>
      </div>
    </div>
    """,
    "notes": "Autonomous IROPS is the single highest ROI use case for AI in aviation. It saves tens of millions during crises."
})

# PART 8: BUSINESS PROCESS OPTIMIZATION & WORKFLOWS (37-41)
slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "Core Operational Process: As-Is vs To-Be Turnaround",
    "subtitle": "Compressing aircraft ground turnaround time from 55 minutes to 35 minutes",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header" style="color: #ef4444;">As-Is Process (55 Minutes - Fragmented & Manual)</div>
        <p>• <strong>Choke Point 1:</strong> Ground handlers wait for printed paper load sheets from flight dispatch.</p>
        <p>• <strong>Choke Point 2:</strong> Catering and cabin cleaning crews communicate via two-way radios with zero visibility into passenger deplaning progress.</p>
        <p>• <strong>Choke Point 3:</strong> Standby passengers manually processed at gate by single agent, delaying boarding door closure.</p>
        <p>• <strong>Result:</strong> 18% of flights suffer ground delays, costing $75 per minute of delay ($42M annually across fleet).</p>
      </div>
      <div class="glass-card">
        <div class="card-header" style="color: #10b981;">To-Be Process (35 Minutes - IoT & AI Synchronized)</div>
        <p>• <strong>IoT Milestones:</strong> Computer vision cameras at gate detect wheel chocks, jet bridge connection, and baggage belt loader in real time.</p>
        <p>• <strong>Automated Dispatch:</strong> Catering, fueling, and cleaning crews dispatched automatically via mobile push based on precise touchdown time.</p>
        <p>• <strong>Digital Trim Sheets:</strong> Electronic flight bags receive digital weight & balance updates via ACARS/gRPC in 2 seconds.</p>
        <p>• <strong>Result:</strong> Turnaround compressed by 20 minutes; enables 1 additional daily flight per aircraft across fleet.</p>
      </div>
    </div>
    """,
    "notes": "Aircraft only make money when they are in the air. 20 minutes saved on turnaround equals an entire extra flight per day."
})

slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "35-Minute Aircraft Turnaround Workflow Gantt",
    "subtitle": "Synchronizing 8 ground handling workflows in parallel across the critical path",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
gantt
    title 35-Minute Turnaround Critical Path (A321neo)
    dateFormat mm
    axisFormat %M min

    section Pax Movement
    Deboarding (180 pax)        :a1, 00, 10m
    Boarding (Biometric Gate)    :a2, 18, 14m
    Door Closure & Pushback      :a3, 32, 03m

    section Baggage & Cargo
    Unloading Bags (Belt 1)      :b1, 02, 12m
    Loading Bags (Belt 2)        :b2, 15, 14m

    section Servicing
    Cabin Cleaning               :c1, 08, 10m
    Catering Exchange            :c2, 10, 10m
    Fueling (12,000 Liters)      :c3, 05, 18m

    section Flight Deck
    Flight Plan & Weight Sheet   :d1, 20, 10m
      </div>
    </div>
    <div class="glass-card" style="margin-top: 0.8rem;">
      <p style="font-size: 0.75rem; color: var(--text-muted);"><strong>Critical Path:</strong> Fueling (18 min) and Cabin Cleaning/Boarding overlap perfectly. If cabin cleaning slips by 3 minutes, the entire flight misses its ATC departure slot, resulting in a 45-minute ground delay.</p>
    </div>
    """,
    "notes": "The Gantt chart illustrates why parallel task execution managed by IoT and automated dispatch is critical."
})

slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "Automated SLA Tracking & Escalation Matrix",
    "subtitle": "Real-time SLA monitoring across ground handlers, catering suppliers, and fueling contractors",
    "content": """
    <div class="glass-card">
      <table class="data-table">
        <tr><th>Operational Milestone</th><th>Mandated SLA</th><th>Warning Threshold (Amber)</th><th>Breach Escalation (Red)</th><th>Contractual Penalty</th></tr>
        <tr><td>Jet Bridge Docking</td><td>Within 2 min of on-chocks</td><td>> 2 min 30 sec</td><td>> 4 min (Alert Airport Duty Mgr)</td><td>$250 per occurrence</td></tr>
        <tr><td>First Bag to Carousel</td><td>Within 12 min of on-chocks</td><td>> 14 min</td><td>> 18 min (Alert Baggage Ops)</td><td>$500 per occurrence</td></tr>
        <tr><td>Last Bag to Carousel</td><td>Within 25 min of on-chocks</td><td>> 27 min</td><td>> 32 min (Alert Ground Handling VP)</td><td>$1,000 per occurrence</td></tr>
        <tr><td>Cabin Cleaning Complete</td><td>Within 10 min of deboarding</td><td>> 11 min</td><td>> 13 min (Alert Turnaround Mgr)</td><td>$150 / min of delay</td></tr>
        <tr><td>Fueling Complete</td><td>At least 15 min before STD</td><td>> 12 min before STD</td><td>> 8 min before STD (Priority Alert)</td><td>$1,500 per delay</td></tr>
      </table>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Automated Contractor Scorecarding</div>
      <p>Data Cloud automatically calculates supplier SLA performance across 150 airports worldwide. Penalty deductions are calculated automatically and applied directly to monthly supplier invoices in SAP S/4HANA Finance, recovering $18M in performance rebates annually.</p>
    </div>
    """,
    "notes": "Automated SLA enforcement creates operational accountability across third-party ground handling contractors."
})

slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "Flight Operations & Crew Legality Recovery",
    "subtitle": "Optimizing pilot and flight attendant rosters to prevent illegal duty-hour flight cancellations",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The Crew Duty Hour Trap (FAA Part 117 / EASA)</div>
        <p>• <strong>Strict Legal Ceilings:</strong> Commercial pilots cannot exceed 10 to 14 hours of daily flight duty period (FDP) depending on start time and sector count.</p>
        <p>• <strong>The Cascade Collapse:</strong> If a flight is delayed on the tarmac for 2 hours due to thunderstorms, the pilots may 'time out' mid-flight. The flight must be cancelled even if the weather clears, leaving 300 passengers stranded.</p>
        <p>• <strong>Cost per Crew Timeout:</strong> Over $250,000 in passenger accommodations, replacement aircraft repositioning, and flight rebooking.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Jeppesen + Palantir AIP Autonomous Crew Recovery</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Predictive Legality Alert:</strong> 3 hours before crew timeout, Jeppesen detects risk and alerts flight operations.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Standby Crew Matching:</strong> Palantir AIP queries standby pilot reserve pools, matching ratings (B777 type rating) and airport proximity.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Automated Dispatch:</strong> Replacement pilot notified via mobile app with an automated Uber/taxi dispatch to airport.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div><strong>Seamless Handoff:</strong> Flight departs with zero cancellation; saves $250K+ per incident.</div></div>
      </div>
    </div>
    """,
    "notes": "Crew duty time outs are the silent killer of airline operational reliability. Predictive alerting prevents them."
})

slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "Safety Incident Management & Regulatory Audit Trails",
    "subtitle": "Permanent cryptographic audit trails for FAA, EASA, and ICAO safety compliance",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Mandatory Safety Incident Reporting</div>
        <table class="data-table">
          <tr><th>Incident Category</th><th>Regulatory Authority</th><th>Mandated Reporting SLA</th><th>Data Vaulting Requirement</th></tr>
          <tr><td>Bird Strike / Foreign Object Debris (FOD)</td><td>FAA / ICAO</td><td>Within 24 hours of landing</td><td>Permanently archived in digital aircraft logbook</td></tr>
          <tr><td>Cabin Turbulence Injury</td><td>FAA / NTSB / EASA</td><td>Immediate within 2 hours</td><td>100% voice/data flight recorder preservation</td></tr>
          <tr><td>Unruly Passenger / Security Threat</td><td>TSA / National Police</td><td>Immediate upon landing</td><td>Cabin CCTV footage and witness statements</td></tr>
          <tr><td>Component In-Flight Shut Down (IFSD)</td><td>Engine OEM & FAA</td><td>Within 12 hours</td><td>Full ACARS engine telemetry bus dump</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Cryptographic Evidence Vault</div>
        <p>All incident reports, cockpit voice recorder (CVR) transcripts, and maintenance sign-offs are cryptographically sealed in <strong>HashiCorp Vault HSM</strong> with immutable write-once-read-many (WORM) storage.</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #10b981;">Regulatory Trust Moat</div>
          <p>Guarantees total legal defensibility during aviation accident investigations and national civil aviation authority (CAA) safety audits.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "Aviation safety data cannot be altered. WORM storage and cryptographic hashing are required by law."
})

# PART 9: AI-ASSISTED EFFECTIVENESS & AGENTIC SYSTEMS (42-46)
slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "Agentic Reasoning Architecture: Atlas Engine vs LangGraph vs AIP",
    "subtitle": "Comparing the three leading enterprise agentic reasoning paradigms in commercial aviation",
    "content": """
    <div class="grid-3">
      <div class="glass-card" style="border-top: 3px solid #3b82f6;">
        <div class="card-header">Salesforce Agentforce (Atlas Engine)</div>
        <p>• <strong>Metadata-Grounded Reasoning:</strong> Autonomous decision loop operating against enterprise DMOs and business policies.</p>
        <p>• <strong>Deterministic Guardrails:</strong> Salesforce Trust Layer prevents hallucinations; enforces OLS/FLS security.</p>
        <p>• <strong>Primary Use Case:</strong> Customer service deflection, passenger rebooking, and personalized ancillary upselling.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #10b981;">
        <div class="card-header">Open Source (LangGraph / CrewAI)</div>
        <p>• <strong>Stateful Multi-Agent Graphs:</strong> Python-native cyclic graphs for complex custom workflows.</p>
        <p>• <strong>Custom Guardrails:</strong> NeMo Guardrails or Llama Guard; requires extensive custom engineering.</p>
        <p>• <strong>Primary Use Case:</strong> RAG over complex engineering manuals, contract of carriage analysis, and pilot training simulators.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #f59e0b;">
        <div class="card-header">Palantir AIP (Artificial Intelligence Platform)</div>
        <p>• <strong>Ontology-Driven Decisioning:</strong> Connects frontier LLMs directly to the enterprise operational digital twin.</p>
        <p>• <strong>Deterministic Action Execution:</strong> Generates provably safe operational commands with human-in-the-loop approvals.</p>
        <p>• <strong>Primary Use Case:</strong> IROPS flight simulation, fleet re-routing, and multi-hub operational command.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Architectural Synthesis</div>
      <p>Enterprises deploy a <strong>dual-agent strategy</strong>: Agentforce powers the commercial front-office (customer-facing rebooking and service), while Palantir AIP or LangGraph powers the operational back-office (fleet dispatch and crew legality).</p>
    </div>
    """,
    "notes": "Clarify the difference between front-office agentic AI (Agentforce) and back-office operational AI (Palantir AIP)."
})

slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "Multi-Agent Orchestration Patterns & Task Handoffs",
    "subtitle": "How specialized autonomous agents collaborate during complex aviation disruptions",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
flowchart TD
    A[Disruption Ingested: SQ322 Cancelled] --> B[Supervisor Agent: Triage & Coordination]
    B --> C[Passenger Rebooking Agent]
    B --> D[Hotel & Voucher Agent]
    B --> E[Baggage Reroute Agent]
    B --> F[EU261 Compensation Agent]

    C -->|Query Inventory| G[(Amadeus Altéa PSS)]
    D -->|Book Rooms| H[(Hotelbeds / Agoda API)]
    E -->|Update Tags| I[(SITA WorldTracer)]
    F -->|Disburse Cash| J[(Adyen / Stripe Direct)]

    C & D & E & F --> K[Customer Communication Agent]
    K -->|Unified Itinerary| L[Passenger WhatsApp / Mobile App]
      </div>
    </div>
    <div class="grid-2" style="margin-top: 0.8rem;">
      <div class="glass-card">
        <div class="card-header">Supervisor Agent Pattern</div>
        <p>The Supervisor Agent acts as the operational conductor: it breaks the complex disaster recovery problem into 4 discrete sub-tasks, delegates to specialized agents in parallel, and reconciles results before sending a single unified communication to the passenger.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Prevents Agent Hallucination Cascades</div>
        <p>Each specialized agent operates under strict deterministic boundaries: the Voucher Agent cannot modify flight seats; the Rebooking Agent cannot disburse refunds. This guarantees enterprise safety.</p>
      </div>
    </div>
    """,
    "notes": "Multi-agent architecture prevents single-agent prompt bloat. Specialization is the key to enterprise reliability."
})

slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "RAG Pipelines & Model Context Protocol (MCP)",
    "subtitle": "Connecting frontier LLMs (Claude 3.7) to real-time airline systems using open JSON-RPC standards",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Model Context Protocol (MCP) in Aviation</div>
        <p>• <strong>The Open Standard:</strong> Announced by Anthropic and adopted by Salesforce, MCP is the open JSON-RPC standard that exposes enterprise tools and databases directly to AI reasoning agents.</p>
        <p>• <strong>Eliminates Brittle Screen Scraping:</strong> Instead of building custom REST wrappers, airline systems expose standardized MCP servers:</p>
        <div style="margin-top: 0.5rem; font-family: monospace; font-size: 0.7rem; color: #93c5fd;">
          • mcp-server-altea-pnr (get_pnr, update_seat)<br>
          • mcp-server-sita-baggage (trace_bag, get_status)<br>
          • mcp-server-weather-ops (get_radar, check_sigmet)
        </div>
      </div>
      <div class="glass-card">
        <div class="card-header">MCP Tool Invocation Schema Example</div>
        <pre style="background: rgba(0,0,0,0.5); padding: 0.6rem; border-radius: 6px; font-size: 0.68rem; color: #a7f3d0;"><code>{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "rebook_passenger_flight",
    "arguments": {
      "pnr_locator": "X7K9LP",
      "current_flight": "SQ322",
      "target_flight": "SQ324",
      "cabin_class": "J",
      "seat_preference": "WINDOW",
      "waive_reissue_fee": true
    }
  },
  "id": "mcp-call-89421"
}</code></pre>
      </div>
    </div>
    """,
    "notes": "Model Context Protocol (MCP) is the future. It standardizes how LLMs talk to airline tools."
})

slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "Predictive Machine Learning Models in Aviation",
    "subtitle": "Supervised, unsupervised, and reinforcement learning models deployed across commercial and flight operations",
    "content": """
    <div class="glass-card">
      <table class="data-table">
        <tr><th>ML Model Domain</th><th>Algorithm / Model Type</th><th>Input Features / Datasets</th><th>Inference Latency</th><th>Business Value</th></tr>
        <tr><td>Dynamic Willingness-to-Pay</td><td>Reinforcement Learning (RL) + XGBoost</td><td>Competitor fares, search velocity, days to departure, season</td><td>< 25 ms</td><td>+3.5% to +5.2% passenger yield expansion ($42M)</td></tr>
        <tr><td>Passenger No-Show Prediction</td><td>Gradient Boosted Decision Trees (LightGBM)</td><td>Booking lead time, fare type, loyalty tier, historical no-shows</td><td>< 50 ms</td><td>Enables safe overbooking, reducing spoiled empty seats by 22%</td></tr>
        <tr><td>Turnaround Delay Prediction</td><td>LSTM Recurrent Neural Networks</td><td>Incoming flight delay, gate congestion, weather, baggage count</td><td>< 200 ms</td><td>Alerts dispatch 45 minutes prior to gate arrival, preventing delays</td></tr>
        <tr><td>Predictive Engine Maintenance</td><td>Random Forest + Anomaly Detection</td><td>ACARS engine vibration, EGT exhaust temp, fuel flow sensors</td><td>Batch / 10 min</td><td>Detects turbine blade wear 50 hours before failure, preventing AOG</td></tr>
        <tr><td>Customer Churn Scoring</td><td>Logistic Regression + Survival Analysis</td><td>Recency of flight, NPS score, customer service sentiment</td><td>Daily Batch</td><td>Triggers retention offers to high-value corporate travelers</td></tr>
      </table>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Model Governance & Drift Monitoring</div>
      <p>All production models are tracked in <strong>MLflow / Databricks Unity Catalog</strong> with continuous monitoring for concept drift (e.g. sudden geopolitical oil price spikes invalidate historical pricing models). Retraining is triggered automatically.</p>
    </div>
    """,
    "notes": "Detail the ML models. Predictive models generate hundreds of millions in yield and cost avoidance."
})

slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "AI Deflection Economics & ROI Business Case",
    "subtitle": "Quantifying the hard-dollar savings of generative AI contact center deflection",
    "content": """
    <div class="grid-3" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="metric-hero" style="color: #ef4444;">$5.50</div>
        <div class="metric-sub">Human Contact Cost</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Fully loaded cost of an 8-minute human agent phone call.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #10b981;">$0.22</div>
        <div class="metric-sub">Agentforce Cost</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Consumption credit cost of autonomous conversational resolution.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #3b82f6;">96.0%</div>
        <div class="metric-sub">Servicing Cost Reduction</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">$5.28 saved on every deflected interaction.</p>
      </div>
    </div>
    <div class="glass-card">
      <div class="card-header">Annual Deflection Savings Calculator (3.5M Inbound Contacts)</div>
      <table class="data-table">
        <tr><th>Inbound Contact Category</th><th>Annual Volume</th><th>Current Human Cost ($5.50)</th><th>Autonomous Deflection Rate</th><th>Deflected Contacts</th><th>Net Annual Savings</th></tr>
        <tr><td>Flight Status & Schedule Changes</td><td>1,200,000</td><td>$6,600,000</td><td>78%</td><td>936,000</td><td>$4,942,080</td></tr>
        <tr><td>Baggage Tracing & Allowances</td><td>750,000</td><td>$4,125,000</td><td>65%</td><td>487,500</td><td>$2,574,000</td></tr>
        <tr><td>Seat Selection & Meal Requests</td><td>600,000</td><td>$3,300,000</td><td>82%</td><td>492,000</td><td>$2,597,760</td></tr>
        <tr><td>Loyalty Balance & Missing Miles</td><td>550,000</td><td>$3,025,000</td><td>85%</td><td>467,500</td><td>$2,468,400</td></tr>
        <tr><td>Complex IROPS Rebooking</td><td>400,000</td><td>$2,200,000</td><td>55%</td><td>220,000</td><td>$1,161,600</td></tr>
        <tr><td><strong>TOTALS</strong></td><td><strong>3,500,000</strong></td><td><strong>$19,250,000</strong></td><td><strong>74.4% (Blended)</strong></td><td><strong>2,603,000</strong></td><td><strong>+$13,743,840 / Year</strong></td></tr>
      </table>
    </div>
    """,
    "notes": "This table is the executive business case. Deflecting 74% of contacts saves $13.7M annually, completely paying for the platform."
})

# PART 10: MASTER INTEGRATION & ROADMAP (47-52)
slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Master Integration Architecture Blueprint",
    "subtitle": "The end-to-end integration topology connecting all 13 enterprise layers",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
flowchart LR
    subgraph Core["Core Systems of Record"]
        ALTEA["Amadeus Altéa PSS"]
        SITA["SITA WorldTracer"]
        AMOS["Swiss-AS AMOS MRO"]
        SAP["SAP S/4HANA Finance"]
    end

    subgraph Integration["Integration & Event Mesh"]
        MULE["MuleSoft Anypoint Platform"]
        KAFKA["Confluent Cloud Kafka"]
        SOLACE["Solace PubSub+ Mesh"]
    end

    subgraph DataAI["Data & Intelligence"]
        DC["Salesforce Data Cloud"]
        SNOW["Snowflake Lakehouse"]
        AF["Agentforce Atlas AI"]
        PAL["Palantir AIP Ops"]
    end

    subgraph Channels["Engagement Front-Ends"]
        WEB["Next.js Web / App"]
        KIOSK["SITA Smart Path"]
        SVC["Service Cloud Voice"]
        MKT["Marketing Cloud"]
    end

    ALTEA & SITA & AMOS & SAP --> MULE & KAFKA & SOLACE
    MULE & KAFKA --> DC & SNOW
    DC --> AF & PAL
    AF & DC --> SVC & MKT & WEB & KIOSK
      </div>
    </div>
    <div class="glass-card" style="margin-top: 0.8rem;">
      <p style="font-size: 0.75rem; color: var(--text-muted);"><strong>Decoupled Multi-Tier Topology:</strong> The integration layer completely insulates legacy Core Systems from web traffic spikes, while Data Cloud feeds real-time context to Agentforce and external front-ends.</p>
    </div>
    """,
    "notes": "Walk through the master integration blueprint. This summarizes the entire enterprise topology."
})

slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Legacy Protocol Translation: EDIFACT & Type B",
    "subtitle": "How MuleSoft and Kafka bridge 1970s teletype protocols to modern JSON-RPC microservices",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Legacy Protocol vs Modern Protocol Mapping</div>
        <table class="data-table">
          <tr><th>Legacy Aviation Protocol</th><th>Modern Target Standard</th><th>Transformation Engine</th><th>Latency Impact</th></tr>
          <tr><td>IATA EDIFACT PNRGOV / PADIS</td><td>JSON-RPC 2.0 / REST OpenAPI 3.0</td><td>MuleSoft Altéa Connector (Flex Gateway)</td><td>+12 ms</td></tr>
          <tr><td>SITA Type B Teletype (BTM, BSM)</td><td>CloudEvents JSON / Kafka Topic</td><td>SITA Message Broker to Kafka Bridge</td><td>+18 ms</td></tr>
          <tr><td>ARINC 429 Avionics Bus</td><td>gRPC / Protocol Buffers</td><td>On-Aircraft ARINC 834 Server</td><td>+5 ms</td></tr>
          <tr><td>IATA NDC XML (17.2 / 21.3)</td><td>GraphQL / Next.js Storefront API</td><td>MuleSoft GraphQL Federation Gateway</td><td>+8 ms</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">The Type B Teletype Translation Example</div>
        <p>A baggage barcode scan on the tarmac produces a 50-year-old teletype message:</p>
        <pre style="background: rgba(0,0,0,0.5); padding: 0.5rem; border-radius: 4px; font-size: 0.65rem; color: #f87171;"><code>BSM
.V/1FSQ
.F/SQ322/20SEP/SIN/LHR
.N/0016849201001
.S/14K/TAN/M
ENDBSM</code></pre>
        <p style="margin-top: 0.5rem;">MuleSoft transforms this into structured JSON in 4ms, triggering a mobile push to Dr. Tan: <em>"Your bag (0016849201) has been loaded onto SQ322."</em></p>
      </div>
    </div>
    """,
    "notes": "Show the concrete code. Transforming legacy Type B messages into mobile push notifications demonstrates mastery."
})

slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Phase 1 & 2 Implementation Roadmap (Months 1–12)",
    "subtitle": "Foundational integration, Data Cloud deployment, and quick-win contact center deflection",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
gantt
    title Enterprise Aviation Transformation: Year 1
    dateFormat MM
    axisFormat Month %m

    section Phase 1: Foundations
    MuleSoft Altéa & SITA Integration   :p1_1, 01, 3M
    Kafka Event Mesh Deployment          :p1_2, 02, 3M
    Data Cloud Zero-Copy Ingestion       :p1_3, 03, 3M

    section Phase 2: Quick-Win Value
    Service Cloud Voice (Amazon Connect) :p2_1, 04, 3M
    Agentforce Tier-1 Deflection Agent   :p2_2, 06, 3M
    Marketing Cloud Dynamic Upsell       :p2_3, 07, 3M
    Apple Wallet Boarding Pass Push      :p2_4, 09, 3M
      </div>
    </div>
    <div class="grid-2" style="margin-top: 1rem;">
      <div class="glass-card">
        <div class="card-header">Key Milestones: Phase 1 (Months 1–6)</div>
        <p>• Establish core MuleSoft API connectivity to Altéa PSS and SITA.<br>• Deploy Confluent Kafka event mesh across primary AWS regions.<br>• Harmonize initial 10M passenger profiles in Salesforce Data Cloud.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Key Milestones: Phase 2 (Months 7–12)</div>
        <p>• Launch Agentforce Tier-1 deflection on WhatsApp and Mobile App (deflecting 45%+ calls).<br>• Activate pre-flight ancillary upsell journeys, generating $1.8M/month in incremental revenue.<br>• Deploy Apple Wallet automated boarding pass updates.</p>
      </div>
    </div>
    """,
    "notes": "A phased roadmap builds executive confidence. Phase 2 starts delivering hard-dollar ROI within 9 months."
})

slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Phase 3 & 4 Implementation Roadmap (Months 13–24)",
    "subtitle": "Autonomous IROPS recovery, biometric gate boarding, and sovereign AI lakehouse",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
gantt
    title Enterprise Aviation Transformation: Year 2
    dateFormat MM
    axisFormat Month %m

    section Phase 3: Autonomous IROPS
    Multi-Agent IROPS Orchestration     :p3_1, 13, 4M
    Adyen Instant Voucher Disbursement  :p3_2, 15, 3M
    SITA Smart Path Biometric Gates     :p3_3, 16, 4M

    section Phase 4: Sovereign AI
    Snowflake Sovereign Clean Rooms     :p4_1, 18, 4M
    Palantir AIP Flight Operations Twin :p4_2, 20, 5M
    Full Enterprise Cutover & Sign-Off   :p4_3, 23, 2M
      </div>
    </div>
    <div class="grid-2" style="margin-top: 1rem;">
      <div class="glass-card">
        <div class="card-header">Key Milestones: Phase 3 (Months 13–18)</div>
        <p>• Launch Multi-Agent Autonomous IROPS rebooking across primary hubs.<br>• Deploy Adyen automated digital compensation vouchers to Apple Wallet.<br>• Roll out SITA Smart Path biometric walk-through gates at 20 departure gates.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Key Milestones: Phase 4 (Months 19–24)</div>
        <p>• Activate Snowflake Sovereign Clean Rooms for interline alliance revenue sharing.<br>• Deploy Palantir AIP fleet and crew operations digital twin.<br>• Full operational handover to internal Center of Excellence (CoE).</p>
      </div>
    </div>
    """,
    "notes": "Year 2 unlocks the advanced agentic and biometric capabilities, achieving the full 310% to 420% ROI."
})

slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Change Management: BCG 'People + Agents' Model",
    "subtitle": "Aligning human talent, operating models, and autonomous agents for sustainable transformation",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The BCG 'People + Agents' Operating Model</div>
        <p>• <strong>The 85% Failure Gap:</strong> BCG research reveals that 85% of enterprise AI POCs fail to deliver production value because organizations treat AI as a technology project rather than an operating model redesign.</p>
        <p>• <strong>Human-in-the-Loop Supervision:</strong> Contact center agents transition from repetitive data entry to 'Agent Supervisors', monitoring autonomous Agentforce interactions and handling complex emotional escalations.</p>
        <p>• <strong>Prompt & Tool Engineering CoE:</strong> Establish an internal Center of Excellence dedicated to continuous prompt optimization, MCP tool evaluation, and safety guardrail governance.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Organizational Transformation Pillars</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Role Evolution:</strong> Front-desk and contact center staff retrained as 'Experience Concierges', measured on CSAT and relationship building rather than AHT.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Incentive Alignment:</strong> Compensation tied to customer lifetime value (CLTV) and digital adoption rather than call duration.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Safety & Ethics Board:</strong> Cross-functional committee (Legal, IT, CX, Operations) reviewing AI autonomous action logs bi-weekly.</div></div>
      </div>
    </div>
    """,
    "notes": "Reference BCG's People + Agents framework. Transformation fails if you do not retrain the human workforce."
})

slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Executive Summary & C-Suite Decision Scorecard",
    "subtitle": "Final architectural recommendation: Path forward for the Chief Information Officer and Board",
    "content": """
    <div class="grid-3" style="margin-bottom: 1rem;">
      <div class="glass-card" style="border-top: 3px solid #3b82f6;">
        <div class="card-header">Recommended Path: Hybrid Var 1 + Var 3</div>
        <p>Deploy <strong>Salesforce Data Cloud + Agentforce</strong> for commercial agility, paired with <strong>Palantir AIP</strong> for operational flight ops and <strong>Amadeus Altéa</strong> for core PSS.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #10b981;">
        <div class="card-header">Financial Return</div>
        <p><strong>3-Year Net Benefit: +$91.2M</strong><br>Payback achieved in 11 months via $13.7M annual servicing deflection and $24M incremental ancillary upsell.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #f59e0b;">
        <div class="card-header">Strategic Moat</div>
        <p>Transforms the airline from a vulnerable commodity seat carrier into a high-margin travel retailer with industry-leading operational resilience.</p>
      </div>
    </div>
    <div class="glass-card">
      <div class="card-header">Immediate Next Steps (30-Day Execution Plan)</div>
      <div class="flow-step"><div class="step-num">1</div><div><strong>Week 1–2:</strong> Form Enterprise Architecture Steering Committee and finalize Data Cloud DMO schemas.</div></div>
      <div class="flow-step"><div class="step-num">2</div><div><strong>Week 3:</strong> Authorize MuleSoft Altéa and SITA connector pilot on staging environment.</div></div>
      <div class="flow-step"><div class="step-num">3</div><div><strong>Week 4:</strong> Launch 30-day Agentforce WhatsApp deflection pilot for flight delay alerts.</div></div>
    </div>
    """,
    "notes": "Close the presentation with a decisive, actionable call to action. The business case is indisputable."
})

# Render HTML and Markdown
out_html = os.path.join(BASE_DIR, "airlines", "presentation.html")
out_md = os.path.join(BASE_DIR, "airlines", "PRESENTATION_FRAMEWORK_COMPENDIUM.md")

# Apply visual enhancements (interactive charts, Mermaid architectures, CLI suites)
slides = vsc.apply_visual_enhancements("AIRLINES", slides)

engine.render_reveal_html(meta, slides, out_html)
engine.render_presentation_markdown(meta, slides, out_md)

print("Airlines presentation generation complete. Total slides:", len(slides))
