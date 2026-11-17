#!/usr/bin/env python3
"""
Cruises & Maritime Expeditions Presentation Generator — 52 Slides
Generates:
1. /run/media/ml/Storage/Labs/cruises/presentation.html
2. /run/media/ml/Storage/Labs/cruises/PRESENTATION_FRAMEWORK_COMPENDIUM.md
"""

import os
import sys
import json

BASE_DIR = "/run/media/ml/Storage/Labs"
sys.path.append(BASE_DIR)
import generate_presentation_engine as engine
import visual_slide_components as vsc

meta = {
    "title": "Maritime & Cruise Systems Architecture",
    "short_code": "CRUISES",
    "sector": "Cruises, Maritime Expeditions & Mega-Yachts",
    "scale": "$48.0B Passenger GBV • 35.0M Cruisers • $1,371 Blended Ticket • $16.8B Onboard Spend"
}

slides = [
    # PART 1: MACROECONOMICS, SIZING & REVENUE MODELS (1-5)
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Maritime Enterprise Architecture Masterclass",
        "subtitle": "Systems Architecture, Technology Stacks, and Operational Orchestration across 13 Enterprise Dimensions",
        "content": """
        <div class="grid-2" style="margin-top: 1rem;">
          <div class="glass-card">
            <div class="card-header">Executive Briefing Scope</div>
            <p>Comprehensive architectural blueprint analyzing the mission-critical systems governing modern ocean cruise lines, expedition vessels, and river operators ($48B global market, 35M passengers). Designed for Maritime CIOs, Chief Commercial Officers, VP Fleet Operations, and Enterprise Architects.</p>
            <div style="margin-top: 1rem;">
              <span class="pill pill-blue">13 Enterprise Layers</span>
              <span class="pill pill-green">3 Stack Variations</span>
              <span class="pill pill-purple">52 Master Slides</span>
              <span class="pill pill-amber">Ship-to-Shore Edge Topology</span>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Core Themes Covered</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Requirements & Governance:</strong> Edge-disconnected resilience at sea, IMO SOLAS safety, STCW crew scheduling, and CLIA standards.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>13-Layer Master Architecture:</strong> Maritime PMS, Central Reservation Systems (CRS), POS, IoT Wearables, CRM, Loyalty, CDP, Lakehouse, AI.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>End-to-End Passenger Journeys:</strong> Travel advisor B2B2C booking, digital e-muster, biometric embarkation, stateroom automation, and folio settlement.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>AI-Assisted Efficiency:</strong> Agentforce maritime concierge, Palantir AIP fuel/route optimization, and autonomous shore excursion dispatch.</div></div>
          </div>
        </div>
        """,
        "notes": "Welcome executive stakeholders. This deck provides an unbroken technical and commercial chain of logic across all cruise technology layers."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Global Cruise Sizing & Revenue Architecture",
        "subtitle": "Macroeconomic baseline: $48.0B Passenger Gross Booking Value across 35.0 Million annual cruisers",
        "content": """
        <div class="grid-4" style="margin-bottom: 1rem;">
          <div class="glass-card">
            <div class="metric-hero">$48.0B</div>
            <div class="metric-label">Passenger GBV</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Global cruise ticket + onboard revenue</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">35.0M</div>
            <div class="metric-label">Annual Cruisers</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Ocean, river, and expedition passengers</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">$1,371</div>
            <div class="metric-label">Blended Yield / Pax</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">$891 ticket + $480 onboard spend</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">$16.8B</div>
            <div class="metric-label">Onboard Spend Pool</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">35.0% of total revenue pool</p>
          </div>
        </div>
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Revenue Breakdown Dynamics</div>
            <table class="data-table">
              <thead><tr><th>Revenue Stream</th><th>Share</th><th>USD Total</th><th>Primary Driver</th></tr></thead>
              <tbody>
                <tr><td>Ticket Fare (Gross)</td><td>65.0%</td><td>$31.2B</td><td>Cabin category, itinerary, seasonality</td></tr>
                <tr><td>Beverage Packages</td><td>14.0%</td><td>$6.72B</td><td>All-inclusive drink packages, premium spirits</td></tr>
                <tr><td>Shore Excursions</td><td>9.5%</td><td>$4.56B</td><td>Guided tours, adventure excursions</td></tr>
                <tr><td>Casino & Gaming</td><td>6.0%</td><td>$2.88B</td><td>Slots, table games, VIP tournaments</td></tr>
                <tr><td>Spa, Retail & Dining</td><td>5.5%</td><td>$2.64B</td><td>Specialty restaurants, duty-free retail</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Macro Operational Economics</div>
            <div class="flow-step"><div class="step-num">$</div><div><strong>High Operating Leverage:</strong> Ships operate with 70%+ fixed operating costs (capital depreciation, fuel, marine crew). Every incremental passenger and onboard dollar flows directly to EBITDA.</div></div>
            <div class="flow-step"><div class="step-num">%</div><div><strong>105%+ Occupancy Dynamics:</strong> Cruises routinely achieve >100% double-occupancy capacity via 3rd and 4th berth guests (families, children).</div></div>
            <div class="flow-step"><div class="step-num">⚡</div><div><strong>Onboard Monetization Velocity:</strong> Captive onboard audience generates 35% of total top-line revenue in 7 days, demanding ultra-low friction POS and contactless payment.</div></div>
          </div>
        </div>
        """,
        "notes": "Cruises represent the highest capital-intensity and operating leverage in travel. Onboard spend is the engine of net profitability."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Economic Friction: Direct vs Travel Advisor Consortia",
        "subtitle": "Distribution channel analysis: $33.6B booked via travel advisor consortia vs $14.4B direct web/call center",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Channel Distribution Mix</div>
            <table class="data-table">
              <thead><tr><th>Channel</th><th>GBV Share</th><th>Volume</th><th>Commission / Cost</th></tr></thead>
              <tbody>
                <tr><td><strong>Travel Advisor Consortia</strong><br>(Virtuoso, Signature, Expedia Cruises)</td><td>70.0%</td><td>$33.6B</td><td>11.0% - 17.0% blended commissions + overrides ($4.37B - $5.71B)</td></tr>
                <tr><td><strong>Direct Web / Brand App</strong><br>(Direct-to-Consumer)</td><td>22.0%</td><td>$10.56B</td><td>1.5% - 3.0% merchant processing + search ad spend</td></tr>
                <tr><td><strong>Direct Call Center / Inbound</strong><br>(Personal Vacation Planners)</td><td>8.0%</td><td>$3.84B</td><td>4.5% - 6.5% fully loaded agent labor & telephony</td></tr>
              </tbody>
            </table>
            <div style="margin-top: 1rem;">
              <span class="pill pill-red">$6.24B Annual Distribution Friction</span>
              <span class="pill pill-green">$41.76B Net Retained Revenue</span>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">The B2B2C Architectural Imperative</div>
            <p>Unlike airlines (direct-dominated) or hotels (OTA-dominated), the cruise industry is deeply anchored in B2B travel advisor networks due to high ticket complexity ($3,000+ per cabin, multi-destination itineraries, cabin deck plans).</p>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Advisor Extranets & APIs:</strong> Cruise lines must expose rich XML/JSON booking engines (CruisingPower, Polar Online, SeaWeb) to thousands of external agencies.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Commission Automation:</strong> Real-time override tracking, co-op marketing fund reconciliation, and group allotment management.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Direct Channel Shift:</strong> Every 5% shift from consortia to direct digital booking reclaims ~$312M in annual EBITDA margin for a major cruise holding company.</div></div>
          </div>
        </div>
        """,
        "notes": "Notice the 70% share of travel advisors. B2B partner portals and group booking APIs are mission-critical in maritime architecture."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Cost & ROI Benchmark across 3 Variations",
        "subtitle": "Total Cost of Ownership (TCO) and 3-year commercial return comparison across architectural strategies",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-blue">Variation 1</span><br>With Salesforce</div>
            <div class="metric-hero" style="font-size: 1.8rem; margin: 0.5rem 0;">$7.8M - $13.2M</div>
            <div class="metric-label">Annual Software ACV</div>
            <div style="margin-top: 1rem; font-size: 0.85rem;">
              <p><strong>Implementation CapEx:</strong> $9.5M - $16.5M</p>
              <p><strong>Annual Run Cost:</strong> $3.0M - $5.2M / yr</p>
              <p><strong>3-Year ROI:</strong> <span style="color: var(--accent-green); font-weight: 700;">320%</span></p>
              <p><strong>Payback Horizon:</strong> 11 Months</p>
              <p><strong>Core Advantage:</strong> Zero-Copy Data Cloud guest synchronization, turnkey Agentforce concierge, and native MuleSoft connectors to Fidelio & Versonix.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-green">Variation 2</span><br>Without Salesforce (Open)</div>
            <div class="metric-hero" style="font-size: 1.8rem; margin: 0.5rem 0;">$6.2M - $10.5M</div>
            <div class="metric-label">Annual Software ACV</div>
            <div style="margin-top: 1rem; font-size: 0.85rem;">
              <p><strong>Implementation CapEx:</strong> $10.5M - $18.0M</p>
              <p><strong>Annual Run Cost:</strong> $4.2M - $6.8M / yr</p>
              <p><strong>3-Year ROI:</strong> <span style="color: var(--accent-blue); font-weight: 700;">250%</span></p>
              <p><strong>Payback Horizon:</strong> 15 Months</p>
              <p><strong>Core Advantage:</strong> Zero vendor lock-in, open-source lakehouse (Databricks/Snowflake), local Kafka edge resilience, and custom fine-tuned LLM agents.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-purple">Variation 3</span><br>Best Money Can Buy</div>
            <div class="metric-hero" style="font-size: 1.8rem; margin: 0.5rem 0;">$24M - $40M</div>
            <div class="metric-label">Annual Software ACV</div>
            <div style="margin-top: 1rem; font-size: 0.85rem;">
              <p><strong>Implementation CapEx:</strong> $32.0M - $58.0M</p>
              <p><strong>Annual Run Cost:</strong> $10.5M - $16.5M / yr</p>
              <p><strong>3-Year ROI:</strong> <span style="color: var(--accent-purple); font-weight: 700;">430%</span></p>
              <p><strong>Payback Horizon:</strong> 13 Months</p>
              <p><strong>Core Advantage:</strong> Palantir Foundry fleet twin, OceanMedallion IoT wearable ecosystem, Adobe Experience Cloud, and Dual Starlink LEO + O3b mPOWER GEO satellite WAN.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Comparing the 3 variations. Variation 3 has high upfront costs but drives extraordinary ROI through onboard spend capture and fuel savings."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Maritime Macro Drivers & Tech Imperatives",
        "subtitle": "Five structural forces transforming modern fleet operations, guest experience, and technology architecture",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Structural Industry Drivers</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>LEO Satellite Revolution:</strong> Starlink Maritime and OneWeb provide 200+ Mbps per ship at 50ms latency, ending decades of satellite bandwidth rationing and enabling real-time cloud sync.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Demographic Shift & Experience Travel:</strong> Median cruiser age dropped from 57 to 46. Millennials and Gen Z demand high-speed Wi-Fi, app-based stateroom controls, and experiential excursions.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Cashless & Frictionless Onboard Economy:</strong> Wearable RFID/BLE (OceanMedallion, WOWBand) enables hands-free stateroom entry and walk-through POS payment.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Decarbonization & Environmental Compliance:</strong> IMO 2030/2050 targets, EU ETS maritime carbon pricing, and shore power (cold ironing) mandate telematics data collection.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Architectural Implications</div>
            <table class="data-table">
              <thead><tr><th>Driver</th><th>Legacy Approach</th><th>Modern Architecture</th></tr></thead>
              <tbody>
                <tr><td>Ship Connectivity</td><td>C-band/Ku-band GEO (512 Kbps, 700ms lag)</td><td>Multi-orbit LEO/MEO/GEO hybrid (300+ Mbps, 45ms lag)</td></tr>
                <tr><td>Guest Access</td><td>Plastic magstripe cruise cards</td><td>BLE/NFC wearable IoT + Apple/Google Wallet NFC</td></tr>
                <tr><td>Data Sync</td><td>Nightly batch flat-file SFTP transfer</td><td>Bi-directional Kafka event mesh & CDC streaming</td></tr>
                <tr><td>Guest Service</td><td>Long queues at Guest Services Desk</td><td>Autonomous mobile Agentforce concierge + chat</td></tr>
                <tr><td>Safety Drill</td><td>Crowded physical muster drill at lifeboats</td><td>Digital e-muster on personal phone + tap check-in</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Starlink Maritime has been the biggest game-changer in cruise tech history, shifting vessels from isolated islands to connected enterprise nodes."
    },

    # PART 2: ASSUMED REQUIREMENTS & CONSTRAINTS (6-10)
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Maritime Functional Requirements Matrix",
        "subtitle": "Operational capabilities required across fleet management, guest experience, and shoreside operations",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Functional Domains</div>
            <table class="data-table">
              <thead><tr><th>Domain</th><th>Critical Capabilities</th><th>Priority</th></tr></thead>
              <tbody>
                <tr><td><strong>Fleet Reservation (CRS)</strong></td><td>Global stateroom inventory, dynamic packaging, multi-currency pricing, agency commissions</td><td><span class="pill pill-red">P0 Critical</span></td></tr>
                <tr><td><strong>Shipboard PMS</strong></td><td>Stateroom allocation, guest folios, gangway security (A-PASS), keycard encoding</td><td><span class="pill pill-red">P0 Critical</span></td></tr>
                <tr><td><strong>Safety & SOLAS</strong></td><td>Electronic muster drill tracking, life raft seat allocation, real-time onboard headcount</td><td><span class="pill pill-red">P0 Life-Safety</span></td></tr>
                <tr><td><strong>Onboard Commerce</strong></td><td>Cashless dining, bar, spa, casino POS, dynamic gratuities, split-folio management</td><td><span class="pill pill-blue">P1 Revenue</span></td></tr>
                <tr><td><strong>Shore Excursion (ShoreEx)</strong></td><td>Tour booking, operator voucher generation, tender boat scheduling, weather waivers</td><td><span class="pill pill-blue">P1 Revenue</span></td></tr>
                <tr><td><strong>Crew Management</strong></td><td>STCW rest-hour compliance, berth allocation, multi-national payroll, marine certifications</td><td><span class="pill pill-amber">P1 Compliance</span></td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Edge vs Terrestrial Functional Split</div>
            <div class="flow-step"><div class="step-num">⚓</div><div><strong>Shipboard Edge Autonomy:</strong> The vessel must operate completely autonomously for up to 14 days without satellite connectivity. Guest folio billing, gangway embarkation/disembarkation, stateroom access, and POS transactions cannot depend on the cloud.</div></div>
            <div class="flow-step"><div class="step-num">☁️</div><div><strong>Shoreside Cloud Centralization:</strong> Global revenue management, marketing campaigns, loyalty tier calculation, travel advisor commission settlement, and corporate reporting run centrally in the cloud.</div></div>
            <div class="flow-step"><div class="step-num">🔄</div><div><strong>Bi-directional Replication:</strong> High-priority transaction deltas replicate ship-to-shore in near real-time whenever satellite WAN is active.</div></div>
          </div>
        </div>
        """,
        "notes": "Notice the life-safety classification of SOLAS muster tracking. In maritime, IT systems literally have life-safety implications."
    },
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Non-Functional & Maritime SLA Requirements",
        "subtitle": "Performance, availability, latency, and disaster recovery thresholds for maritime environments",
        "content": """
        <div class="grid-4" style="margin-bottom: 1rem;">
          <div class="glass-card">
            <div class="metric-hero">&lt;50ms</div>
            <div class="metric-label">Local POS Latency</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Shipboard bar/dining transaction speed</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">99.999%</div>
            <div class="metric-label">Shipboard Edge SLA</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Five-nines onboard server cluster uptime</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">15,000</div>
            <div class="metric-label">Peak Trans / Min</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Turnaround day embarkation rush</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">&lt;3 sec</div>
            <div class="metric-label">Gangway Scan Time</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Biometric or RFID passenger check</p>
          </div>
        </div>
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Maritime High Availability Architecture</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Hyper-Converged Infrastructure (HCI):</strong> Nutanix or VMware vSAN dual-node/three-node clusters installed in shipboard data center with automatic VM failover.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Dual-Ring Marine Fiber:</strong> Redundant optical fiber backbones routed port and starboard to survive hull breach or localized fire.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Uninterruptible Marine Power:</strong> Dual N+1 marine UPS systems backed by emergency diesel generators (EDG) ensuring zero brownouts during main engine power transients.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Satellite SLA & WAN Management</div>
            <table class="data-table">
              <thead><tr><th>Link Type</th><th>Throughput</th><th>Latency</th><th>Role</th></tr></thead>
              <tbody>
                <tr><td>Starlink Maritime (LEO)</td><td>100 - 350 Mbps</td><td>35 - 60 ms</td><td>Primary guest Wi-Fi & real-time cloud data sync</td></tr>
                <tr><td>SES O3b mPOWER (MEO)</td><td>50 - 150 Mbps</td><td>120 - 180 ms</td><td>Secondary high-throughput operational link</td></tr>
                <tr><td>Inmarsat Global Xpress (GEO)</td><td>5 - 20 Mbps</td><td>600 - 800 ms</td><td>Tertiary backup for voice and critical safety data</td></tr>
                <tr><td>4G/5G Cellular Port WAN</td><td>500+ Mbps</td><td>15 - 30 ms</td><td>In-port heavy data synchronization and software updates</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Maritime IT is a masterclass in edge computing: physical redundancy, dual-hull fiber routing, and multi-orbit satellite management."
    },
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Maritime Constraints & Legacy Technical Debt",
        "subtitle": "Overcoming the unique challenges of floating edge data centers and decades of legacy software",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Unique Maritime Physical & Network Constraints</div>
            <div class="flow-step"><div class="step-num">🌊</div><div><strong>Harsh Marine Environment:</strong> Constant salt-fog exposure, extreme engine vibration, ambient temperature swings in Caribbean vs Alaska, and pitch/roll motion affecting spinning disk arrays (mandating all-flash NVMe storage).</div></div>
            <div class="flow-step"><div class="step-num">📡</div><div><strong>Satellite Shadowing & Polar Deadzones:</strong> Ship superstructures, terrain in Norwegian fjords, and high-latitude voyages (>70° North/South) cause satellite line-of-sight dropouts.</div></div>
            <div class="flow-step"><div class="step-num">🔒</div><div><strong>Steel Hull RF Attenuation:</strong> Steel bulkheads and fire doors severely attenuate Wi-Fi and Bluetooth signals, requiring hundreds of marine-grade APs per deck.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Legacy Technical Debt Hotspots</div>
            <table class="data-table">
              <thead><tr><th>System / Protocol</th><th>Debt Description</th><th>Modern Remediation</th></tr></thead>
              <tbody>
                <tr><td><strong>Fidelio Cruise OXI / FIAS</strong></td><td>Legacy serial/TCP socket protocols with rigid, synchronous ASCII message formats.</td><td>MuleSoft / Kafka Edge Microservices wrapping FIAS into modern REST/gRPC.</td></tr>
                <tr><td><strong>Night Audit Monolith</strong></td><td>End-of-day PMS batch process locking down folios for 60-90 minutes at 3:00 AM.</td><td>Continuous ledger accounting with sub-second immutable ledger updates.</td></tr>
                <tr><td><strong>Point-to-Point Interfaces</strong></td><td>Over 40 brittle point-to-point connections between PMS, Casino, Spa, POS, and TV systems.</td><td>Event-Driven Architecture (EDA) with localized Kafka pub/sub messaging.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Steel bulkheads turn every cruise ship cabin into a mini-Faraday cage. Modern APs and BLE beacons must be engineered into ceiling raceways."
    },
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Maritime Regulatory & Compliance Framework",
        "subtitle": "Navigating international maritime law, safety of life at sea, and global data privacy jurisdictions",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Maritime Safety & Maritime Labor Regulations</div>
            <div class="flow-step"><div class="step-num">🚨</div><div><strong>IMO SOLAS (Safety of Life at Sea):</strong> Mandatory electronic muster verification within 24 hours of embarkation. Systems must generate certified lifeboat manifests for Coast Guard inspection.</div></div>
            <div class="flow-step"><div class="step-num">⏱️</div><div><strong>MLC 2006 & STCW Rest Hours:</strong> Crew work hours (max 14 hours/day, 72 hours/week) must be digitally logged. Violations trigger port state control detention of the vessel.</div></div>
            <div class="flow-step"><div class="step-num">🚢</div><div><strong>Jones Act & PVSA Compliance:</strong> US Passenger Vessel Services Act mandates foreign port calls (e.g., Ensenada, Victoria) for foreign-flagged ships. Itinerary systems must enforce regulatory rules.</div></div>
            <div class="flow-step"><div class="step-num">🧼</div><div><strong>USPHS / CDC Vessel Sanitation Program (VSP):</strong> Automated logging of potable water chlorine levels, galley refrigeration temps, and gastrointestinal illness tracking.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Global Data Privacy & Financial Compliance</div>
            <table class="data-table">
              <thead><tr><th>Regulation</th><th>Scope at Sea</th><th>Architectural Requirement</th></tr></thead>
              <tbody>
                <tr><td><strong>EU GDPR / UK GDPR</strong></td><td>European cruisers & EU port calls</td><td>Consent telemetry, RTBF (Right to be Forgotten) across shipboard edge and cloud</td></tr>
                <tr><td><strong>PCI-DSS 4.0</strong></td><td>Onboard cashless folios & casino</td><td>P2PE tokenization at POS terminals; no PAN stored on shipboard databases</td></tr>
                <tr><td><strong>US CBP APIS / e-NOA/D</strong></td><td>Automated Passenger Information</td><td>Electronic manifest transmission to border authorities 96 hours before US arrival</td></tr>
                <tr><td><strong>Flag State Maritime Law</strong></td><td>Bahamas, Panama, Malta, Bermuda</td><td>Dual jurisdictional compliance for criminal logging and onboard births/deaths</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Maritime IT compliance is complex because the ship changes legal jurisdictions as it sails between territorial waters and the high seas."
    },
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Maritime Architectural Trade-offs & Decisions",
        "subtitle": "Strategic architectural compromises between edge autonomy, cloud agility, cost, and guest friction",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header">Edge vs Cloud Decoupling</div>
            <p><strong>Trade-off:</strong> Autonomous local shipboard execution vs centralized cloud management.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-green">Choice: Edge-First Hybrid</span></p>
              <p>Critical guest-facing transactions (POS, stateroom entry, muster) execute 100% locally. Cloud handles analytics, reservations, and cross-voyage marketing via Kafka sync.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Wearable IoT vs Mobile BYOD</div>
            <p><strong>Trade-off:</strong> Dedicated wearable token (OceanMedallion) vs guest smartphone app (BYOD).</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-blue">Choice: Converged Hybrid</span></p>
              <p>Wearable RFID/BLE eliminates guest friction (no phone needed at pool/spa), while smartphone app provides rich UI for booking excursions and reviewing folios.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Monolith vs Composable Edge</div>
            <p><strong>Trade-off:</strong> Legacy all-in-one Fidelio PMS vs modern containerized microservices.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-purple">Choice: API-Wrapped Core</span></p>
              <p>Keep battle-tested Fidelio as the immutable System of Record, wrap with MuleSoft/Kafka edge APIs to enable fast modern front-end development.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Notice the converged hybrid approach for guest devices. Wearables win on friction (poolside/beach), phones win on rich content (excursions/menus)."
    },

    # PART 3: IT STANDARDS & GOVERNANCE (11-15)
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "Enterprise Architecture Framework: TOGAF & C4",
        "subtitle": "Structuring dual-realm maritime architecture across Cloud Hyperscaler and Shipboard Edge Containers",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">C4 Model Architecture in Maritime</div>
            <div class="flow-step"><div class="step-num">C1</div><div><strong>System Context:</strong> Cruiser, Travel Advisor, Shipboard Crew interacting with shoreside booking systems, onboard vessel operations, and satellite telemetry.</div></div>
            <div class="flow-step"><div class="step-num">C2</div><div><strong>Containers:</strong> Terrestrial Cloud (AWS/Azure/Salesforce), Edge Shipboard HCI (Nutanix/VMware), Mobile Native Apps (iOS/Android), and Wearable IoT Beacons.</div></div>
            <div class="flow-step"><div class="step-num">C3</div><div><strong>Components:</strong> Reservation Engine, Edge Folio Service, Biometric Gangway Validator, Kafka Sync Connector, Agentforce Concierge Engine.</div></div>
            <div class="flow-step"><div class="step-num">C4</div><div><strong>Code:</strong> Microservices, gRPC protobufs, OpenAPI specifications, and Apex/Python AI agent tooling.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">TOGAF Architecture Domains</div>
            <table class="data-table">
              <thead><tr><th>TOGAF Domain</th><th>Maritime Fleet Focus</th></tr></thead>
              <tbody>
                <tr><td><strong>Business Architecture</strong></td><td>Unified passenger lifecycle: Travel advisor consortia booking, cruise turnaround, onboard monetization, loyalty retention.</td></tr>
                <tr><td><strong>Data Architecture</strong></td><td>Dual-realm canonical schema: Golden Guest 360 in Data Cloud; synchronized local partition in shipboard MySQL/PostgreSQL.</td></tr>
                <tr><td><strong>Application Architecture</strong></td><td>Event-driven, loosely coupled microservices fronted by API gateways on shore and edge.</td></tr>
                <tr><td><strong>Technology Architecture</strong></td><td>Multi-cloud shoreside infrastructure, Starlink/MEO hybrid SD-WAN, and hardened shipboard HCI clusters.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Applying TOGAF and C4 gives maritime architects a rigorous framework to manage the complexity of floating edge data centers."
    },
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "Maritime API Standards & Data Formats",
        "subtitle": "Standardizing integration protocols: OpenTravel Alliance (OTA), NMEA maritime data, and OpenAPI 3.0",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Industry Standard Protocols</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>OpenTravel Alliance (OTA) 2014B/2020A:</strong> Standardized XML/JSON schemas for cruise reservations (OTA_CruiseBookRQ, OTA_CruiseCabinAvailRS, OTA_CruisePriceRQ).</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>NMEA 0183 / NMEA 2000:</strong> Standard electrical and data specification for marine electronics (GPS coordinates, vessel speed, wind, heading, depth) streamed to the cloud for real-time fleet tracking.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>OpenAPI 3.0 (REST/JSON):</strong> Modern microservices API definitions powering mobile apps, guest portals, and partner extranets.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>gRPC & Protocol Buffers:</strong> Low-bandwidth, binary serialization used for ship-to-shore sync over constrained satellite channels.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Protocol Translation Architecture</div>
            <table class="data-table">
              <thead><tr><th>Source System</th><th>Native Protocol</th><th>Target Architecture</th><th>Payload Standard</th></tr></thead>
              <tbody>
                <tr><td>Fidelio Cruise PMS</td><td>FIAS / TCP Sockets</td><td>MuleSoft Edge Adapter</td><td>JSON over HTTPS / Kafka</td></tr>
                <tr><td>Bridge Navigation</td><td>NMEA 0183 Serial</td><td>Edge IoT Gateway</td><td>MQTT / Apache Kafka</td></tr>
                <tr><td>Travel Agency GDS</td><td>OTA XML (SOAP)</td><td>Cloud API Gateway</td><td>RESTful OpenAPI 3.0</td></tr>
                <tr><td>Onboard Simphony POS</td><td>Direct SQL / OXI</td><td>Edge CDC (Debezium)</td><td>Avro / Kafka Event Stream</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Protocol translation is the secret sauce of maritime IT: turning 30-year-old serial NMEA and FIAS streams into modern cloud events."
    },
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "Event-Driven Architecture & Messaging Topology",
        "subtitle": "High-throughput asynchronous messaging across ship and shore using Kafka and priority queues",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Multi-Tier Priority Message Queue</div>
            <p>Satellite bandwidth varies dynamically based on latitude and weather. Messages must be strictly prioritized across four Quality of Service (QoS) classes:</p>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-red);">P0</div><div><strong>Life Safety & Security:</strong> Gangway A-PASS headcounts, SOLAS muster confirmations, emergency alarms. Instant transmission, zero drop allowed.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-amber);">P1</div><div><strong>Financial & Transactions:</strong> Credit card pre-authorizations, folio closures, high-value casino drops. Real-time sync with offline buffering.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-blue);">P2</div><div><strong>Operational Telematics:</strong> Marine engine RPM, fuel flow, HVAC power consumption, water production. Batched and compressed every 5 minutes.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-purple);">P3</div><div><strong>Marketing & Engagement:</strong> Guest app clickstream, spa survey responses, photo gallery views. Transmitted during off-peak night hours.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Ship-to-Shore Kafka MirrorMaker Topology</div>
            <div class="mermaid">
            flowchart TD
              subgraph Ship["Shipboard Edge Cluster"]
                POS["Simphony POS"] -->|CDC| LK["Local Kafka Broker"]
                PMS["Fidelio PMS"] -->|CDC| LK
                IOT["Engine/IoT"] -->|MQTT| LK
                LK --> MM_E["MirrorMaker Edge Agent"]
              end
              subgraph Sat["Satellite WAN"]
                MM_E -->|QoS Prioritized gRPC| SAT["Starlink / O3b Hybrid"]
              end
              subgraph Cloud["Cloud Hyperscaler"]
                SAT --> MM_C["MirrorMaker Cloud Agent"]
                MM_C --> CK["Enterprise Cloud Kafka"]
                CK --> DC["Data Cloud / Snowflake"]
                CK --> SAP["SAP Finance Core"]
              end
            </div>
          </div>
        </div>
        """,
        "notes": "Kafka MirrorMaker with priority QoS guarantees that a guest buying a martini or taking a safety drill never gets dropped even in a storm."
    },
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "Maritime Cybersecurity & Zero-Trust Architecture",
        "subtitle": "Defending ocean vessels against cyber attacks, ransomware, and unauthorized network intrusion",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Network Segmentation (IEC 62443 Standard)</div>
            <table class="data-table">
              <thead><tr><th>Zone</th><th>Network Segment</th><th>Isolation & Security Policy</th></tr></thead>
              <tbody>
                <tr><td><span class="pill pill-red">Zone 4: OT</span></td><td>Bridge & Propulsion</td><td>Completely air-gapped from internet; physical isolation, read-only telemetry diodes.</td></tr>
                <tr><td><span class="pill pill-amber">Zone 3: Safety</span></td><td>SOLAS & Fire Alarms</td><td>Dedicated VLAN, redundant fiber, strict port-security MAC filtering.</td></tr>
                <tr><td><span class="pill pill-blue">Zone 2: Corporate</span></td><td>PMS, POS, Crew Admin</td><td>Zero-Trust Network Access (ZTNA), EDR on all endpoints, MFA required.</td></tr>
                <tr><td><span class="pill pill-green">Zone 1: Guest</span></td><td>Passenger Wi-Fi & TV</td><td>Dynamic client isolation, DNS filtering, captive portal, bandwidth shaping per cabin.</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Zero-Trust Maritime Enforcement</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Micro-Segmentation:</strong> Illumio / Cisco TrustSec enforcing granular firewall policies between onboard stateroom IoT locks and guest Wi-Fi.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Identity-Centric Access:</strong> Crew access to PMS and safety systems governed by Okta / Entra ID with certificate-based smartcard authentication.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Satellite SD-WAN Tunneling:</strong> All ship-to-shore communications encrypted via IPsec / WireGuard tunnels with automated multi-path failover.</div></div>
          </div>
        </div>
        """,
        "notes": "The bridge and propulsion controls are strictly air-gapped according to IEC 62443. A hacker on guest Wi-Fi cannot steer the vessel."
    },
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "Maritime Data Governance & Master Data Management",
        "subtitle": "Architecting the Golden Passenger Record across voyages, brands, and travel agencies",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">The Maritime Master Data Challenge</div>
            <p>Cruise lines face unique identity challenges: passengers book through travel agencies using nicknames, travel in varying family groupings, and sail across multiple sister brands within a cruise holding company (e.g., Carnival Corp, Royal Caribbean Group, Norwegian Cruise Line Holdings).</p>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Deterministic Matching:</strong> Passport number, Date of Birth, Full Legal Name, and Loyalty Account ID.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Probabilistic Matching:</strong> Email address, mobile phone, billing address, and travel companion co-travel history.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Household Graph:</strong> Modeling family groups across staterooms to allow shared folio billing and consolidated loyalty perks.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Data Catalog & Privacy Governance</div>
            <table class="data-table">
              <thead><tr><th>Tool</th><th>Role in Maritime Enterprise</th><th>Key Policy Enforced</th></tr></thead>
              <tbody>
                <tr><td><strong>Collibra / Informatica</strong></td><td>Enterprise Data Catalog & Lineage</td><td>Single definition of "Net Yield", "APIS Manifest", and "Loyalty Tier" across all brands.</td></tr>
                <tr><td><strong>Salesforce Data Cloud / AEP</strong></td><td>Real-time Customer Data Platform</td><td>Harmonized Guest 360 profile synchronized shipboard 48h before embarkation.</td></tr>
                <tr><td><strong>OneTrust</strong></td><td>Privacy & Consent Automation</td><td>Automated consent propagation (cookie, app, marketing) adhering to EU GDPR and California CCPA.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Household matching is crucial in cruising. When parents and kids are booked in separate cabins, the system must link them seamlessly."
    },

    # PART 4: 13-LAYER ARCHITECTURE & 3 VARIATIONS (16-20)
    {
        "part": "PART 4: 13-LAYER ARCHITECTURE",
        "title": "13-Layer Master Architecture Blueprint",
        "subtitle": "The definitive enterprise technology taxonomy powering global cruise operations",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">The 13 Enterprise Architecture Layers</div>
            <div style="font-size: 0.85rem; line-height: 1.6;">
              <p><strong>1. Core Maritime Ops:</strong> Fidelio Cruise PMS, Versonix CRS, SOLAS muster</p>
              <p><strong>2. Contact Center:</strong> Service Cloud Voice / Genesys Cloud CX</p>
              <p><strong>3. CRM & B2B Portals:</strong> Sales Cloud, Advisor Extranets, Group Bookings</p>
              <p><strong>4. Loyalty Engine:</strong> Tier status, onboard amenities, co-brand credit cards</p>
              <p><strong>5. CDP & Identity:</strong> Salesforce Data Cloud / Twilio Segment / Adobe AEP</p>
              <p><strong>6. API & Integration:</strong> MuleSoft / Kafka / Confluent ship-to-shore event mesh</p>
              <p><strong>7. Cloud & Edge Infra:</strong> AWS/Azure shoreside + Nutanix shipboard HCI</p>
              <p><strong>8. Satellite WAN:</strong> Starlink Maritime LEO + O3b GEO hybrid SD-WAN</p>
              <p><strong>9. Onboard IoT:</strong> OceanMedallion BLE wearables, smart locks, digital signage</p>
              <p><strong>10. Digital App & CMS:</strong> Mobile guest app, stateroom interactive IPTV</p>
              <p><strong>11. Marketing Automation:</strong> Marketing Cloud / Braze real-time messaging</p>
              <p><strong>12. Finance & Marine ERP:</strong> SAP S/4HANA, marine fuel/parts procurement</p>
              <p><strong>13. AI & Automation:</strong> Agentforce maritime concierge, Palantir AIP</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Architectural Cohesion & Handoffs</div>
            <div class="flow-step"><div class="step-num">⚡</div><div><strong>Unbroken Digital Thread:</strong> From the moment a traveler or travel advisor inquires about an Alaska cruise to post-voyage loyalty retention, data flows seamlessly across all 13 layers.</div></div>
            <div class="flow-step"><div class="step-num">⚓</div><div><strong>Edge Resiliency:</strong> Layers 1, 8, 9, and 10 maintain full operational capability during deep-sea satellite blackout periods.</div></div>
            <div class="flow-step"><div class="step-num">🎯</div><div><strong>Commercial Optimization:</strong> Layers 4, 5, 11, and 13 maximize pre-cruise package sales and onboard impulse spend.</div></div>
          </div>
        </div>
        """,
        "notes": "Here is the comprehensive 13-layer taxonomy. Every modern cruise enterprise must solve all 13 layers to be competitive."
    },
    {
        "part": "PART 4: 13-LAYER ARCHITECTURE",
        "title": "Variation 1: The Salesforce-Centric Ecosystem",
        "subtitle": "Unified maritime architecture anchored on Salesforce Data Cloud, Agentforce, and MuleSoft",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Stack Specification</div>
            <table class="data-table">
              <thead><tr><th>Layer</th><th>Selected Platform</th><th>Deployment Mode</th></tr></thead>
              <tbody>
                <tr><td>CRM & B2B Portals</td><td>Salesforce Sales & Service Cloud</td><td>Multi-cloud SaaS (Shoreside)</td></tr>
                <tr><td>CDP & Guest 360</td><td>Salesforce Data Cloud</td><td>Hyperscale Lakehouse (Zero-Copy)</td></tr>
                <tr><td>Integration Fabric</td><td>MuleSoft Anypoint + Edge Runtimes</td><td>Cloud Control Plane + Edge Gateways</td></tr>
                <tr><td>AI Concierge</td><td>Salesforce Agentforce</td><td>Autonomous reasoning over guest profiles</td></tr>
                <tr><td>Marketing</td><td>Salesforce Marketing Cloud (SFMC)</td><td>Journey Builder & MobileConnect Push</td></tr>
                <tr><td>Core Maritime Ops</td><td>Oracle Fidelio Cruise + Versonix CRS</td><td>Onboard HCI + Shoreside Cloud</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic & Commercial Evaluation</div>
            <div class="flow-step"><div class="step-num">✓</div><div><strong>Native Data Harmony:</strong> Zero-copy integration between Data Cloud, Agentforce, and Service Cloud eliminates costly custom ETL pipelines.</div></div>
            <div class="flow-step"><div class="step-num">✓</div><div><strong>B2B Advisor Enablement:</strong> Experience Cloud powers agency portals with real-time stateroom availability, group allotments, and commission tracking.</div></div>
            <div class="flow-step"><div class="step-num">⚠️</div><div><strong>Edge Dependency Risk:</strong> Agentforce requires satellite connectivity for advanced reasoning unless quantized models are deployed to shipboard edge runtimes.</div></div>
            <div style="margin-top: 1rem;">
              <span class="pill pill-blue">ACV: $7.8M - $13.2M / yr</span>
              <span class="pill pill-green">3-Year ROI: 320%</span>
            </div>
          </div>
        </div>
        """,
        "notes": "Variation 1 provides the tightest integration and lowest friction between marketing, travel agents, and guest operations."
    },
    {
        "part": "PART 4: 13-LAYER ARCHITECTURE",
        "title": "Variation 2: Without Salesforce (Open Modern)",
        "subtitle": "Decoupled, edge-resilient architecture utilizing Snowflake, Braze, Dynamics 365, and Kafka",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Stack Specification</div>
            <table class="data-table">
              <thead><tr><th>Layer</th><th>Selected Platform</th><th>Deployment Mode</th></tr></thead>
              <tbody>
                <tr><td>Lakehouse / Storage</td><td>Snowflake / Databricks</td><td>Multi-cloud Data Cloud (Shoreside)</td></tr>
                <tr><td>CDP & Streaming</td><td>Twilio Segment / mParticle</td><td>Real-time event collection & routing</td></tr>
                <tr><td>CRM & Contact Center</td><td>Microsoft Dynamics 365 / Zendesk</td><td>Enterprise SaaS + Omnichannel Voice</td></tr>
                <tr><td>Marketing Engine</td><td>Braze</td><td>Mobile-first real-time streaming campaigns</td></tr>
                <tr><td>Event Mesh</td><td>Confluent Apache Kafka</td><td>Shipboard local brokers + cloud cluster</td></tr>
                <tr><td>Core Maritime Ops</td><td>Oracle Fidelio Cruise + Versonix CRS</td><td>Onboard HCI + Shoreside Cloud</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic & Commercial Evaluation</div>
            <div class="flow-step"><div class="step-num">✓</div><div><strong>Vendor Independence:</strong> Open standards prevent platform lock-in. Any layer can be replaced independently.</div></div>
            <div class="flow-step"><div class="step-num">✓</div><div><strong>Edge Optimization:</strong> Local Kafka brokers natively cache events during satellite drops and burst-replicate upon reconnect.</div></div>
            <div class="flow-step"><div class="step-num">⚠️</div><div><strong>Integration Overhead:</strong> Requires a larger internal engineering team to maintain custom glue-code, APIs, and data models across 10+ vendors.</div></div>
            <div style="margin-top: 1rem;">
              <span class="pill pill-green">ACV: $6.2M - $10.5M / yr</span>
              <span class="pill pill-blue">3-Year ROI: 250%</span>
            </div>
          </div>
        </div>
        """,
        "notes": "Variation 2 appeals to engineering-heavy organizations that want full control over their code and zero vendor lock-in."
    },
    {
        "part": "PART 4: 13-LAYER ARCHITECTURE",
        "title": "Variation 3: The Best Platforms Money Can Buy",
        "subtitle": "Sovereign-grade maritime architecture: Palantir Foundry, OceanMedallion IoT, and Adobe Experience Cloud",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Stack Specification</div>
            <table class="data-table">
              <thead><tr><th>Layer</th><th>Selected Platform</th><th>Deployment Mode</th></tr></thead>
              <tbody>
                <tr><td>Fleet Intelligence Twin</td><td>Palantir Foundry & AIP</td><td>Sovereign multi-cloud + Edge AIP runtimes</td></tr>
                <tr><td>Onboard IoT Wearables</td><td>Carnival OceanMedallion / BLE Beacons</td><td>Vessel-wide sensor mesh & smart staterooms</td></tr>
                <tr><td>Digital Experience & CDP</td><td>Adobe Experience Cloud (AEP + AJO + AEM)</td><td>Sub-50ms streaming edge personalization</td></tr>
                <tr><td>Contact Center</td><td>Genesys Cloud CX + Google CCAI</td><td>AI-orchestrated global contact center</td></tr>
                <tr><td>Satellite WAN</td><td>Dual Starlink Maritime + SES O3b mPOWER</td><td>Active-active bonded multi-orbit SD-WAN</td></tr>
                <tr><td>Core Maritime Ops</td><td>Oracle Fidelio Cruise + Versonix Seaware</td><td>Onboard Nutanix HCI + Shoreside Cloud</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic & Commercial Evaluation</div>
            <div class="flow-step"><div class="step-num">★</div><div><strong>Frictionless Wearable Ecosystem:</strong> OceanMedallion unlocks doors automatically as guests approach and enables waitstaff to deliver drinks directly to a pool lounger via real-time BLE location.</div></div>
            <div class="flow-step"><div class="step-num">★</div><div><strong>Kinetic Fleet Optimization:</strong> Palantir Foundry models ocean currents, weather, engine telemetry, and hotel power loads, cutting fleet fuel burn by 4-7% ($50M+ annual savings).</div></div>
            <div style="margin-top: 1rem;">
              <span class="pill pill-purple">ACV: $24M - $40M / yr</span>
              <span class="pill pill-green">3-Year ROI: 430%</span>
            </div>
          </div>
        </div>
        """,
        "notes": "Variation 3 represents the pinnacle of cruise technology, as proven by Carnival Corporation's multi-hundred-million-dollar OceanMedallion investment."
    },
    {
        "part": "PART 4: 13-LAYER ARCHITECTURE",
        "title": "Layer-by-Layer Architectural Comparative Matrix",
        "subtitle": "Side-by-side benchmark of all 13 enterprise layers across the three variations",
        "content": """
        <div style="overflow-x: auto;">
          <table class="data-table" style="font-size: 0.75rem;">
            <thead>
              <tr><th>Layer</th><th>Variation 1: With Salesforce</th><th>Variation 2: Without Salesforce (Open)</th><th>Variation 3: Best Money Can Buy</th></tr>
            </thead>
            <tbody>
              <tr><td>1. Core Ops</td><td>Oracle Fidelio Cruise + Versonix CRS</td><td>Oracle Fidelio Cruise + Versonix CRS</td><td>Fidelio Cruise + Versonix + Palantir Ops</td></tr>
              <tr><td>2. Contact Center</td><td>Service Cloud Voice + Amazon Connect</td><td>Genesys Cloud CX / Zendesk Talk</td><td>Genesys Cloud CX + Google CCAI</td></tr>
              <tr><td>3. CRM / B2B</td><td>Salesforce Sales Cloud + Experience Cloud</td><td>Microsoft Dynamics 365 + Custom Portal</td><td>Salesforce Unlimited + Custom Bespoke Portal</td></tr>
              <tr><td>4. Loyalty</td><td>Salesforce Loyalty Management</td><td>Talon.One / SessionM</td><td>Kobie / Custom Sovereign Engine</td></tr>
              <tr><td>5. CDP / Data</td><td>Salesforce Data Cloud (Zero-Copy)</td><td>Snowflake + Twilio Segment</td><td>Adobe Experience Platform (AEP)</td></tr>
              <tr><td>6. Integration</td><td>MuleSoft Anypoint Platform</td><td>Confluent Apache Kafka + Kong Gateway</td><td>Confluent Kafka + Apigee + MuleSoft</td></tr>
              <tr><td>7. Infra / Edge</td><td>AWS Cloud + Nutanix Shipboard HCI</td><td>Azure/AWS + VMware vSAN Edge</td><td>AWS/GCP Dedicated + Nutanix All-NVMe HCI</td></tr>
              <tr><td>8. Satellite WAN</td><td>Starlink Maritime + Inmarsat Fleet Xpress</td><td>Starlink Maritime + Speedcast Peplink</td><td>Dual Starlink LEO + SES O3b mPOWER GEO</td></tr>
              <tr><td>9. Onboard IoT</td><td>Standard RFID Keycards + BLE Beacons</td><td>Standard RFID + Assa Abloy Mobile Key</td><td>OceanMedallion BLE Mesh + Smart Sensors</td></tr>
              <tr><td>10. Digital App</td><td>Salesforce Mobile SDK / React Native</td><td>Native iOS / Android + Next.js</td><td>Adobe AEM + Native Swift/Kotlin Apps</td></tr>
              <tr><td>11. Marketing</td><td>Marketing Cloud (SFMC) + Einstein</td><td>Braze + Iterable</td><td>Adobe Journey Optimizer (AJO)</td></tr>
              <tr><td>12. Finance / ERP</td><td>SAP S/4HANA Cloud</td><td>Microsoft Dynamics 365 Finance</td><td>SAP S/4HANA Dedicated + Ariba</td></tr>
              <tr><td>13. AI & Automation</td><td>Salesforce Agentforce Maritime Concierge</td><td>Custom LLM on Databricks / Bedrock</td><td>Palantir AIP + OpenAI Enterprise Tier</td></tr>
            </tbody>
          </table>
        </div>
        """,
        "notes": "This comparative matrix gives an immediate, comprehensive overview of the vendor choices across all three variations."
    },

    # PART 5: TOOL COMPLEMENTARITY & SYSTEM HANDOFFS (21-25)
    {
        "part": "PART 5: TOOL COMPLEMENTARITY",
        "title": "Four Spheres of Enterprise Technology",
        "subtitle": "Organizing maritime platforms into Systems of Record, Intelligence, Engagement, and Action",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">The Four Spheres Taxonomy</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Systems of Record (SoR):</strong> Immutable single source of truth for transactions. Fidelio Cruise PMS (onboard folios, cabin state), Versonix Seaware (fleet reservations), SAP S/4HANA (financial general ledger).</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Systems of Intelligence (SoI):</strong> Data ingestion, identity resolution, machine learning. Salesforce Data Cloud, Snowflake, Databricks, and Palantir Foundry.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Systems of Engagement (SoE):</strong> Omnichannel touchpoints connecting with cruisers and agents. Service Cloud Voice, Marketing Cloud, Mobile Guest App, Advisor Portal.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Systems of Action (SoA):</strong> Operational execution engines. Oracle Simphony POS, OceanMedallion IoT stateroom locks, A-PASS gangway biometric scanners, HotSOS crew dispatch.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Architectural Interlock Dynamics</div>
            <div class="mermaid">
            flowchart TD
              SoI["Systems of Intelligence<br>(Data Cloud / Snowflake)"] -->|Audiences & AI Context| SoE["Systems of Engagement<br>(Marketing Cloud / Agentforce)"]
              SoE -->|Booking & Requests| SoR["Systems of Record<br>(Versonix CRS / Fidelio PMS)"]
              SoR -->|Replication & Manifests| SoA["Systems of Action<br>(Shipboard POS / Gangway / IoT)"]
              SoA -->|CDC Transactions| SoI
            </div>
          </div>
        </div>
        """,
        "notes": "Understanding how the four spheres interact prevents architectural overlap and ensures clean separation of concerns."
    },
    {
        "part": "PART 5: TOOL COMPLEMENTARITY",
        "title": "Core System Handoffs: Booking to Manifest",
        "subtitle": "Sequence diagram from initial travel advisor booking to shipboard PMS manifest allocation",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">Booking to Manifest Synchronization Sequence</div>
          <div class="mermaid">
          sequenceDiagram
            autonumber
            actor Advisor as Travel Advisor
            participant Portal as Advisor Extranet
            participant CRS as Versonix Seaware CRS
            participant Mule as MuleSoft Integration
            participant Kafka as Cloud Kafka Mesh
            participant Sat as Satellite WAN
            participant ShipK as Shipboard Kafka
            participant PMS as Fidelio Cruise PMS

            Advisor->>Portal: Search Cabin Availability & Price
            Portal->>CRS: Check Stateroom Deck Allotment
            CRS-->>Portal: Return Cabin 10242 (Balcony)
            Advisor->>Portal: Confirm Booking & Deposit
            Portal->>CRS: Commit Reservation (PNR Created)
            CRS->>Mule: Publish BookingEvent (JSON)
            Mule->>Kafka: Ingest to topic 'cruise.bookings'
            Kafka->>Sat: Route via Starlink to Ship
            Sat->>ShipK: Ingest to Shipboard Broker
            ShipK->>PMS: Create Guest Profile & Stateroom Hold
            PMS-->>ShipK: ACK Manifest Entry Committed
          </div>
        </div>
        """,
        "notes": "Notice how the booking is safely replicated from terrestrial CRS to shipboard PMS via Kafka over satellite WAN."
    },
    {
        "part": "PART 5: TOOL COMPLEMENTARITY",
        "title": "Onboard Guest Engagement & Service Dispatch",
        "subtitle": "Sequence diagram of real-time mobile/wearable order dispatch and cashless folio charging",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">Poolside Drink Order to Lounger Delivery Sequence</div>
          <div class="mermaid">
          sequenceDiagram
            autonumber
            actor Guest as Cruiser (at Pool Lounger)
            participant App as Mobile Guest App
            participant Agent as Agentforce / AI Butler
            participant IoT as OceanMedallion / BLE Mesh
            participant POS as Simphony POS
            participant Crew as Crew Mobile Handheld
            participant Folio as Fidelio Folio Service

            Guest->>App: "Order Mojito to my lounger"
            App->>Agent: Parse Natural Language Intent
            Agent->>IoT: Query Guest Real-Time BLE Coordinates
            IoT-->>Agent: Deck 11, Sun Deck Lounger #42
            Agent->>POS: Inject Order with Location Metadata
            POS->>Crew: Dispatch to Nearest Pool Bar Server
            Crew->>Guest: Deliver Drink to Lounger #42
            Crew->>POS: Confirm Delivery via Wearable Tap
            POS->>Folio: Post $14.00 Charge to Stateroom Folio
            Folio-->>App: Push Real-Time Folio Update
          </div>
        </div>
        """,
        "notes": "This sequence illustrates the power of real-time location combined with autonomous order dispatch and instant folio settlement."
    },
    {
        "part": "PART 5: TOOL COMPLEMENTARITY",
        "title": "Ship-to-Shore Disconnection & Re-Sync",
        "subtitle": "Architectural handling of satellite blackouts, local edge buffering, and post-reconnection sync",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">Offline Disconnection and Reconciliation Flow</div>
          <div class="mermaid">
          sequenceDiagram
            autonumber
            participant ShipEdge as Shipboard Edge (Kafka/PMS)
            participant SatLink as Satellite WAN (Starlink)
            participant CloudSync as Cloud Gateway (MuleSoft/Kafka)
            participant CloudCore as Shoreside Core (Data Cloud/SAP)

            Note over SatLink: Satellite Signal Lost (Heavy Weather / Fjord Shadowing)
            ShipEdge->>ShipEdge: Switch to Local Autonomous Buffer Mode
            ShipEdge->>ShipEdge: Process 4,500 Onboard POS Charges (Buffered in RocksDB/Kafka)
            ShipEdge->>ShipEdge: Process 120 Stateroom Upgrades & Spa Bookings Locally
            Note over SatLink: Satellite Signal Restored (Multi-Orbit Link Active)
            ShipEdge->>SatLink: Initiate Priority Burst Re-sync (P0 Safety -> P1 Financial)
            SatLink->>CloudSync: Stream Batched Avro Payloads
            CloudSync->>CloudCore: Apply Vector Clocks / CRDT Reconciliation
            CloudCore->>CloudCore: Reconcile General Ledger & Credit Card Authorizations
            CloudCore-->>ShipEdge: Return ACK & Sync State Verification
          </div>
        </div>
        """,
        "notes": "Vector clocks and Conflict-Free Replicated Data Types (CRDTs) ensure that offline edits never cause data corruption upon reconnection."
    },
    {
        "part": "PART 5: TOOL COMPLEMENTARITY",
        "title": "Maritime Integration Friction Points & Mitigation",
        "subtitle": "Overcoming operational friction across edge synchronization, bandwidth, and inventory conflicts",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header">Bandwidth Starvation</div>
            <p><strong>Problem:</strong> Guest Wi-Fi consumption (streaming Netflix/YouTube) consumes all satellite bandwidth, starving critical PMS sync.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-green">Mitigation</span></p>
              <p>Hardware SD-WAN traffic shaping (Peplink/Cisco) with strict QoS carving: 25% bandwidth hard-reserved for operational VLANs; guest Wi-Fi rate-limited per stateroom.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Double-Booking at Sea</div>
            <p><strong>Problem:</strong> A shore excursion is sold simultaneously by shoreside web and shipboard excursion desk during an offline window.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-blue">Mitigation</span></p>
              <p>Inventory Partitioning: 70% allocated to shoreside pre-cruise sales, 30% hard-reserved for onboard booking desk. Zero shared unallocated pools during sailings.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Credit Card Fraud at Sea</div>
            <p><strong>Problem:</strong> Guests using stolen or maxed cards for high-value onboard casino and luxury retail while offline.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-purple">Mitigation</span></p>
              <p>Mandatory Pre-Authorization: $500 - $1,000 credit hold placed during shoreside online check-in prior to embarkation. Onboard charges capped to pre-auth buffer.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Inventory partitioning and pre-authorization buffering are classic maritime IT strategies to prevent real-world financial losses."
    },

    # PART 6: DATA INGESTION, MODELING & LAKEHOUSE (26-30)
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Maritime Data Ingestion Architecture",
        "subtitle": "Handling four distinct ingestion modalities: IoT streaming, transactional CDC, batch, and satellite burst",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Four Ingestion Modalities</div>
            <table class="data-table">
              <thead><tr><th>Modality</th><th>Data Sources</th><th>Protocol / Engine</th><th>Frequency</th></tr></thead>
              <tbody>
                <tr><td><strong>High-Frequency IoT</strong></td><td>OceanMedallion BLE, engine NMEA sensors, HVAC</td><td>MQTT / Apache Kafka</td><td>100ms - 1 sec</td></tr>
                <tr><td><strong>Transactional CDC</strong></td><td>Fidelio PMS, Simphony POS, Casino Gaming</td><td>Debezium / Kafka Connect</td><td>Sub-second event</td></tr>
                <tr><td><strong>Batch Integrations</strong></td><td>CBP APIS manifests, supplier provisioning</td><td>SFTP / Apache Airflow</td><td>Every 4 - 24 hours</td></tr>
                <tr><td><strong>Satellite Burst Sync</strong></td><td>Buffered offline charges, guest surveys</td><td>gRPC / Kafka MirrorMaker</td><td>Opportunistic / Continuous</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Shipboard Edge Ingestion Pipeline</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Local Ingestion Tier:</strong> Edge Kafka cluster running on shipboard HCI receives events from POS, PMS, and BLE gateways.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Local Deduplication & Compression:</strong> Payloads are deduplicated, serialized into Apache Avro, and compressed (zstd) to minimize satellite byte transmission.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Shoreside Landing:</strong> Data lands in Cloud Object Storage (Amazon S3 / Azure ADLS) for lakehouse processing.</div></div>
          </div>
        </div>
        """,
        "notes": "Deduplication and zstd compression cut satellite WAN payload sizes by up to 80%, saving tens of thousands of dollars in satellite usage."
    },
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Canonical Maritime Data Model & Entities",
        "subtitle": "Standardized entity-relationship model covering guest, booking, stateroom, folio, and safety domains",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Maritime Entities</div>
            <table class="data-table">
              <thead><tr><th>Entity</th><th>Key Attributes</th><th>Relationships</th></tr></thead>
              <tbody>
                <tr><td><strong>Cruiser</strong></td><td>CruiserID, PassportNo, LoyaltyTierID, CasinoRating, DietaryPrefs</td><td>1:M Bookings, 1:M Folios</td></tr>
                <tr><td><strong>VoyageBooking</strong></td><td>BookingID, PNR, ShipID, SailDate, StateroomID, ChannelID</td><td>M:1 Cruiser, 1:M Guests</td></tr>
                <tr><td><strong>Stateroom</strong></td><td>StateroomID, ShipID, DeckNo, Category (Suite/Balcony), MaxBerth</td><td>1:M Bookings</td></tr>
                <tr><td><strong>OnboardFolio</strong></td><td>FolioID, BookingID, CruiserID, CurrentBalance, PreAuthLimit</td><td>1:M FolioLineItems</td></tr>
                <tr><td><strong>ShoreExBooking</strong></td><td>ExcursionID, BookingID, TourCode, DepartureTime, WaiverSigned</td><td>M:1 Booking</td></tr>
                <tr><td><strong>MusterRecord</strong></td><td>MusterID, BookingID, StationCode, LifeboatNo, CompletedAt</td><td>1:1 Cruiser per Voyage</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Data Model Design Principles</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Voyage-Scoped vs Enterprise-Scoped:</strong> Folios and muster records are strictly voyage-scoped. Loyalty tiers, guest preferences, and casino ratings are enterprise-scoped and persist across lifetimes.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Party Model:</strong> Cruisers, travel advisors, emergency contacts, and crew members are modeled as roles on a unified Party entity.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Immutable Financial Ledger:</strong> Folio line items are append-only. Voiding a bar charge creates a compensating negative credit entry.</div></div>
          </div>
        </div>
        """,
        "notes": "Notice the separation between voyage-scoped operational data (folios, muster) and enterprise-scoped lifetime data (loyalty, casino rating)."
    },
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Identity Resolution & Unified Profile Engine",
        "subtitle": "Creating the persistent Golden Guest Record across disparate bookings, agencies, and onboard tokens",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Identity Resolution Architecture</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Cross-Brand Harmonization:</strong> Passenger who sailed on Celebrity Cruises books a Royal Caribbean cruise via a travel agency. Identity engine reconciles different IDs to a single Master Party ID.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Deterministic Rules:</strong> Matches exact Passport Hash + DOB or Government ID.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Probabilistic Machine Learning:</strong> Jaro-Winkler string distance on Name + fuzzy address matching + co-traveler graph linkage.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Ephemeral Token Association:</strong> Onboard OceanMedallion BLE beacon MAC address linked to Golden Profile for the duration of the 7-day sailing.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Identity Resolution Flowchart</div>
            <div class="mermaid">
            flowchart TD
              Raw1["Agency Booking (OTA XML)"] --> Matcher["Identity Resolution Engine<br>(Data Cloud / AEP)"]
              Raw2["Web Direct Booking (JSON)"] --> Matcher
              Raw3["Past Voyage History (PMS)"] --> Matcher
              Raw4["Casino VIP Card"] --> Matcher
              Matcher --> Rules{"Deterministic Rule Match?"}
              Rules -->|Yes| Merge["Merge to Unified Golden ID"]
              Rules -->|No| Prob{"Probabilistic ML Score > 0.85?"}
              Prob -->|Yes| Merge
              Prob -->|No| New["Create New Cruiser Record"]
              Merge --> Sync["Sync Profile to Shipboard Edge 48h Pre-Cruise"]
            </div>
          </div>
        </div>
        """,
        "notes": "Ephemeral token association allows the cruise line to link temporary physical tokens (wearables) to permanent guest profiles seamlessly."
    },
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Medallion Lakehouse Architecture for Maritime",
        "subtitle": "Transforming raw ship-to-shore telemetry into commercial and operational data products",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-amber">Bronze Layer</span><br>Raw & Streaming Ingestion</div>
            <div style="font-size: 0.85rem; margin-top: 0.8rem;">
              <p><strong>Sources:</strong> Raw Kafka events, NMEA navigation strings, POS transaction logs, satellite status pings.</p>
              <p><strong>Format:</strong> Raw JSON / Avro / Parquet stored in S3/ADLS.</p>
              <p><strong>Retention:</strong> 7 years immutable audit trail.</p>
              <p><strong>Characteristics:</strong> Append-only, unvalidated, schema-on-read.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-blue">Silver Layer</span><br>Cleansed & Conformed</div>
            <div style="font-size: 0.85rem; margin-top: 0.8rem;">
              <p><strong>Transformations:</strong> Data deduplication, currency normalization, time-zone alignment to Ship Local Time, PII masking.</p>
              <p><strong>Tables:</strong> CleanedVoyageBookings, StandardizedFolioCharges, ValidatedMusterEvents.</p>
              <p><strong>Engine:</strong> dbt / Databricks Delta Lake / Snowflake.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-purple">Gold Layer</span><br>Curated Data Products</div>
            <div style="font-size: 0.85rem; margin-top: 0.8rem;">
              <p><strong>Business Products:</strong></p>
              <p>• <strong>Guest Lifetime Value (CLV):</strong> Predictive repeat booking score.</p>
              <p>• <strong>Casino Theoretical Win:</strong> Real-time VIP comping.</p>
              <p>• <strong>Fuel Efficiency Twin:</strong> Nautical mile per ton of LNG/MGO.</p>
              <p>• <strong>Excursion Yield:</strong> Profit margin per tour operator.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "The Medallion architecture ensures that raw, messy telemetry from 30+ ships is systematically refined into actionable business products."
    },
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Data Governance, Lineage & Privacy Automation",
        "subtitle": "Ensuring regulatory compliance, PII protection, and automated consent enforcement at sea",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Cross-Jurisdictional Privacy Controls</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Automated PII Masking:</strong> Credit card numbers (PAN) tokenized via P2PE before ever hitting the data lake. Passport numbers encrypted with AES-256 with key rotation.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Right to be Forgotten (RTBF):</strong> Automated deletion propagation from shoreside OneTrust/Data Cloud across all shipboard edge databases upon completion of voyage audit lock.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Medical & Dietary Data Isolation:</strong> Special dietary requirements and medical mobility needs stored in encrypted, restricted-access tables adhering to HIPAA / GDPR Article 9.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Data Lineage & Auditability</div>
            <table class="data-table">
              <thead><tr><th>Data Asset</th><th>Lineage Tracking</th><th>Compliance Target</th></tr></thead>
              <tbody>
                <tr><td>Lifeboat Manifest</td><td>Fidelio PMS -> Gangway Scan -> Lifeboat Assignment</td><td>IMO SOLAS / USCG Inspection</td></tr>
                <tr><td>Casino Folio Drop</td><td>Gaming Table Sensor -> Simphony POS -> SAP GL</td><td>Nevada / Curacao Gaming Board</td></tr>
                <tr><td>Guest Consent</td><td>Mobile App Checkbox -> OneTrust -> SFMC / Braze</td><td>EU GDPR / UK DPA / CCPA</td></tr>
                <tr><td>Marine Fuel Burn</td><td>Mass Flow Meters -> NMEA -> Palantir / Snowflake</td><td>IMO DCS / EU MRV Carbon Audit</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Data governance at sea must satisfy both shoreside data privacy laws and rigorous maritime safety/environmental audits."
    },

    # PART 7: END-TO-END CUSTOMER JOURNEYS (31-36)
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 1: Inspiration, Discovery & Search",
        "subtitle": "The cruiser journey begins: AI voyage recommendation, itinerary search, and advisor engagement",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Guest & Advisor Search Experience</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Inspiration & Discovery:</strong> Cruiser browses 7-day Western Caribbean itineraries on brand website, Instagram ads, or visits a local travel agency.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>AI Voyage Matchmaker:</strong> Agentforce / Web Recommender suggests specific ship class (e.g., Oasis Class vs Expedition) based on family size and past vacation preferences.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Dynamic Deck Plan Visualizer:</strong> 3D interactive cabin tour showing exact balcony view, proximity to elevators, and obstructed view warnings.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">System Interactions & Data Flow</div>
            <div class="mermaid">
            flowchart TD
              Guest["Cruiser / Travel Advisor"] --> Web["Web Portal / Agency Extranet"]
              Web --> Search["Elasticsearch / Algolia Itinerary Engine"]
              Search --> CRS["Versonix Seaware CRS"]
              CRS --> RMS["Dynamic Pricing Engine"]
              RMS --> Cache["Redis Availability Cache"]
              Cache --> Web
              Web --> CDP["Data Cloud / Segment Clickstream"]
            </div>
          </div>
        </div>
        """,
        "notes": "Cabin selection in cruising is far more visual and complex than hotel room booking. Guests want to see the exact deck, side of ship, and balcony angle."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 2: Booking, Dynamic Packaging & Merchandising",
        "subtitle": "Locking the cabin, bundling beverage packages, specialty dining, and travel insurance",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Merchandising & Ancillary Bundling</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Cabin Lock & PNR Creation:</strong> Stateroom 8214 locked in CRS with a 15-minute countdown timer to prevent race conditions across agencies.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Dynamic Package Recommendation:</strong> "Deluxe Beverage Package" + "3-Night Specialty Dining" offered at a 20% bundle discount during checkout.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Travel Protection Underwriting:</strong> Real-time insurance policy generation via API integration with Allianz / Chubb.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Deposit & Payment Splitting:</strong> Deposit paid via credit card; option to split payments across multiple travel companions.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Checkout Architecture & Ancillary Lift</div>
            <table class="data-table">
              <thead><tr><th>Ancillary Item</th><th>Conversion Rate</th><th>Average Value</th><th>Margin</th></tr></thead>
              <tbody>
                <tr><td>Beverage Package</td><td>42.0%</td><td>$560 / cabin</td><td>82% gross margin</td></tr>
                <tr><td>Specialty Dining Pass</td><td>28.5%</td><td>$220 / cabin</td><td>74% gross margin</td></tr>
                <tr><td>Shore Excursions</td><td>36.0%</td><td>$480 / cabin</td><td>38% gross margin</td></tr>
                <tr><td>Wi-Fi Package</td><td>51.0%</td><td>$140 / cabin</td><td>91% gross margin</td></tr>
              </tbody>
            </table>
            <div style="margin-top: 1rem;">
              <span class="pill pill-green">+$1,400 Avg Pre-Cruise Ancillary Lift</span>
            </div>
          </div>
        </div>
        """,
        "notes": "Pre-cruise merchandising is critical: guests who purchase beverage and dining packages prior to sailing spend 30% more onboard."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 3: Pre-Cruise, Digital Check-in & E-Muster",
        "subtitle": "Frictionless readiness: passport OCR, health questionnaire, arrival slot, and digital safety briefing",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Mobile Pre-Cruise Preparation</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Mobile Passport OCR & Selfie:</strong> Guest scans passport and captures facial biometric selfie in the mobile app 30 days before sailing.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Arrival Time Slot Selection:</strong> Guests select staggered 30-minute port arrival windows (11:00 AM - 2:30 PM) to eliminate terminal crowding.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Digital E-Muster Briefing:</strong> Guest watches the mandatory SOLAS safety video on their phone and listens to the emergency horn sound prior to boarding.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Digital Boarding Pass:</strong> Boarding pass with QR code and terminal directions saved to Apple / Google Wallet.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">System Integration Sequence</div>
            <div class="mermaid">
            flowchart TD
              GuestApp["Guest Mobile App"] --> OCR["Microblink Passport OCR"]
              GuestApp --> Face["Biometric Face Capture"]
              OCR --> PMS["Fidelio Cruise Manifest"]
              Face --> APIS["US CBP APIS Gateway"]
              GuestApp --> Muster["E-Muster Video Engine"]
              Muster --> SOLAS["SOLAS Safety Compliance Table"]
              PMS --> Wallet["Apple / Google Wallet Pass"]
            </div>
          </div>
        </div>
        """,
        "notes": "E-muster revolutionized cruise operations post-2020. Guests no longer stand for an hour in the heat wearing life jackets."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 4: Turnaround Day & Embarkation",
        "subtitle": "The terminal turnstile: curbside luggage RFID tagging, biometric boarding, and stateroom access",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Frictionless Embarkation Journey</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Curbside Luggage Ingestion:</strong> Porters scan RFID luggage tags; bags routed to automated sorting conveyor system for shipboard delivery.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Facial Biometric Turnstile:</strong> Guest walks through the cruise terminal gate without presenting physical documents; facial recognition matches CBP gallery in &lt;2 seconds.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Gangway A-PASS Scan:</strong> Final security scan registers guest as "Onboard" in shipboard Fidelio PMS.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Muster Station Check-in:</strong> Guest walks directly to their assigned assembly station (e.g., Lounge B), taps their phone/wearable, confirming physical presence.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Terminal Operations KPIs</div>
            <table class="data-table">
              <thead><tr><th>Metric</th><th>Legacy Process</th><th>Biometric E-Muster</th><th>Improvement</th></tr></thead>
              <tbody>
                <tr><td>Curb-to-Ship Time</td><td>45 - 75 minutes</td><td>8 - 12 minutes</td><td><span style="color: var(--accent-green); font-weight: 700;">80% Faster</span></td></tr>
                <tr><td>Check-in Desk Agents</td><td>65 agents</td><td>18 roaming agents</td><td><span style="color: var(--accent-green); font-weight: 700;">72% Labor Cut</span></td></tr>
                <tr><td>Muster Completion</td><td>60 min ship-wide drill</td><td>Individual 2-min tap</td><td><span style="color: var(--accent-green); font-weight: 700;">97% Time Saved</span></td></tr>
                <tr><td>Luggage Delivery</td><td>By 8:00 PM</td><td>By 3:30 PM</td><td><span style="color: var(--accent-green); font-weight: 700;">4.5 hrs Earlier</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Biometric curb-to-ship boarding transformed the cruise embarkation experience from a dreaded airport-like queue into an 8-minute breeze."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 5: Onboard Voyage Delivery, Dining & ShoreEx",
        "subtitle": "The 7-day sailing experience: stateroom automation, poolside ordering, and tender boat dispatch",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Onboard Digital Touchpoints</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Keyless Stateroom Entry:</strong> Wearable token (OceanMedallion) unlocks stateroom door automatically when guest is 3 feet away; greets guest on digital door screen.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Smart Stateroom Climate:</strong> HVAC and lighting automatically adjust based on guest presence, balcony door sensor state, and solar heat gain.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Autonomous ShoreEx Dispatch:</strong> Real-time push notification updates excursion meeting time and tender boat boarding group based on sea swell conditions.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>VIP Casino Rating:</strong> Table games RFID sensors track chips wagered; instantly feeds real-time comping rules (free drinks, specialty dinner).</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Onboard Commerce Flow</div>
            <div class="flow-step"><div class="step-num">💳</div><div><strong>100% Cashless Environment:</strong> All bars, restaurants, duty-free boutiques, and spas operate via wearable tap or facial verification.</div></div>
            <div class="flow-step"><div class="step-num">📊</div><div><strong>Live Folio Transparency:</strong> Guest views itemized charges on mobile app or interactive stateroom IPTV; can dispute charges with Agentforce in real-time.</div></div>
            <div class="flow-step"><div class="step-num">🎯</div><div><strong>Contextual In-Voyage Upsell:</strong> Rainy sea day triggers automated push notification offering a 25% spa hydrotherapy pass discount.</div></div>
          </div>
        </div>
        """,
        "notes": "Onboard IoT delivers the magic: hands-free door opening, personalized greetings, and drinks delivered directly to your lounger."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 6: Disembarkation, Loyalty & Re-booking",
        "subtitle": "Closing the loop: express digital checkout, customs clearance, and future cruise bounce-back offers",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Seamless Disembarkation & Retention</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Automated Digital Folio Settlement:</strong> Credit card charged automatically at 4:00 AM on turnaround morning; final PDF receipt delivered via email and app. Zero queue at Guest Services.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Facial Biometric Debarkation:</strong> Cruiser taps off the gangway and walks through port customs using US CBP Facial Comparison.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Loyalty Points Credited:</strong> Cruise points and tier upgrades calculated within 24 hours in Data Cloud / Loyalty Management.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>NextCruise Bounce-Back Offer:</strong> Automated personalized offer: "$100 deposit + $300 onboard credit if booked within 14 days."</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Re-booking & Retention Economics</div>
            <table class="data-table">
              <thead><tr><th>Metric</th><th>Industry Average</th><th>AI-Personalized</th><th>Impact</th></tr></thead>
              <tbody>
                <tr><td>NextCruise Onboard Bookings</td><td>12.0% of cabins</td><td>24.5% of cabins</td><td><span style="color: var(--accent-green); font-weight: 700;">+104% Lift</span></td></tr>
                <tr><td>Post-Cruise Survey Completion</td><td>18.0%</td><td>46.0% (In-app)</td><td><span style="color: var(--accent-green); font-weight: 700;">+155% Data</span></td></tr>
                <tr><td>Repeat Cruiser Share</td><td>48.0%</td><td>62.0%</td><td><span style="color: var(--accent-green); font-weight: 700;">+14 pts Share</span></td></tr>
                <tr><td>Direct Re-booking Rate</td><td>22.0%</td><td>38.0%</td><td><span style="color: var(--accent-green); font-weight: 700;">-$18M Commissions</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Capturing the re-booking while the cruiser is still on the ship or within 14 days of returning home is the highest-ROI marketing in travel."
    },

    # PART 8: PROCESS OPTIMIZATION & WORKFLOWS (37-41)
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "As-Is vs To-Be Operational Transformation",
        "subtitle": "Re-engineering legacy maritime operations into an automated, digital-first operational model",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Legacy As-Is Operational State</div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-red);">1</div><div><strong>Paper Manifests & Queues:</strong> Embarkation queues stretching 2 hours; physical paper boarding passes, manual passport checks at desks.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-red);">2</div><div><strong>Mandatory Lifeboat Drills:</strong> 4,000 passengers crowded on exterior promenade decks for 60 minutes, delaying vacation start.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-red);">3</div><div><strong>Disembarkation Paperwork:</strong> Paper folios slipped under stateroom doors at 2:00 AM; massive lines of angry guests at front desk disputing mini-bar charges.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Modern To-Be Digital Ecosystem</div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-green);">1</div><div><strong>Biometric Walk-Through:</strong> 8-minute curb-to-ship boarding with zero physical document handling; automated CBP facial match.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-green);">2</div><div><strong>Personalized E-Muster:</strong> Self-paced safety video on mobile phone + 30-second assembly station tap.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-green);">3</div><div><strong>Autonomous Folio Management:</strong> Continuous real-time ledger on app; Agentforce instant dispute resolution; zero front-desk queues.</div></div>
          </div>
        </div>
        """,
        "notes": "The operational transformation in cruising over the last 5 years has been greater than any other sector in travel."
    },
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "Automated Turnaround Day Orchestration",
        "subtitle": "The 10-hour critical operational window: disembarking 4,000 guests, provisioning 50 tons, and embarking 4,000 guests",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">Turnaround Day Master Orchestration Timeline</div>
          <div class="mermaid">
          gantt
            title 10-Hour Ship Turnaround Critical Path (06:00 to 16:00)
            dateFormat HH:mm
            axisFormat %H:%M

            section Port & Clearance
            Ship Docking & USCG Clearance   :06:00, 07:00
            section Disembarkation
            Luggage Offload to Terminal     :06:30, 09:30
            Express Self-Assist Walkoff    :07:00, 08:30
            Staggered Group Disembarkation :08:00, 10:00
            Ship Zero-Headcount Cleared    :10:00, 10:15
            section Housekeeping & Galley
            2,000 Stateroom Turnaround      :08:30, 13:00
            Galley Deep Sanitization        :09:00, 11:30
            50-Ton Food/Bunker Provisioning :08:00, 13:30
            section Embarkation
            VIP & Early Embarkation         :11:00, 12:30
            General Passenger Embarkation   :12:00, 15:30
            All-Aboard & Manifest Close     :15:30, 16:00
          </div>
        </div>
        """,
        "notes": "Turnaround day is a high-wire operational act. 4,000 guests leave, 4,000 arrive, 2,000 rooms cleaned, all in 10 hours."
    },
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "Maritime Dynamic Revenue & Cabin Yield",
        "subtitle": "Algorithmic cabin category upgrade bids, dynamic beverage package pricing, and excursion yield",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Algorithmic Stateroom Upgrade Bidding</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Empty Suite Identification:</strong> 14 days before sailing, RMS identifies 24 unsold Balcony Suites and 12 Owner's Suites.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Bid Invitations (Plusgrade / Custom Engine):</strong> Cruisers booked in Oceanview and Interior cabins receive targeted invitations to bid for higher categories.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Cascading Upgrade Allocation:</strong> Highest bids accepted 48 hours prior to embarkation; their vacated lower cabins are auctioned to entry-level guests.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Incremental Revenue Capture:</strong> Generates $120,000 - $250,000 in pure margin per sailing with zero additional variable cost.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Dynamic Pre-Cruise Pricing Algorithms</div>
            <table class="data-table">
              <thead><tr><th>Product</th><th>Pricing Driver</th><th>Dynamic Rule Enforced</th></tr></thead>
              <tbody>
                <tr><td>Beverage Packages</td><td>Booking Window & Ship Capacity</td><td>Price increases from $65/day (60 days out) to $89/day (onboard).</td></tr>
                <tr><td>Shore Excursions</td><td>Operator Capacity & Weather</td><td>Tours with &lt;10 seats remaining priced at 15% premium.</td></tr>
                <tr><td>Specialty Dining</td><td>Prime Time Slot Demand</td><td>Peak 7:30 PM slots priced at full rate; 5:30 PM / 9:00 PM discounted 20%.</td></tr>
                <tr><td>High-Speed Wi-Fi</td><td>Pre-Cruise Bundle vs Daily</td><td>Pre-cruise multi-device bundle discounted 25% vs onboard daily rate.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Cascading upgrade bidding is one of the highest-margin innovations in cruise tech, capturing pure incremental profit."
    },
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "Maritime Workforce & Crew Management (STCW)",
        "subtitle": "Scheduling 1,500+ multinational crew members, automated STCW rest hours, and tip distribution",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Crew Operations Complexity</div>
            <p>A mega-cruise ship is a floating city staffed by 1,200 to 2,200 crew members representing over 60 nationalities, working on 6 to 9-month maritime contracts under strict international labor conventions.</p>
            <div class="flow-step"><div class="step-num">1</div><div><strong>STCW & MLC 2006 Rest Hours:</strong> Adonis / MXP MarineXchange tracks daily work/rest hours. System alerts supervisors before a crew member exceeds the 14-hour daily limit.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Automated Gratuity Distribution:</strong> Automated allocation of daily hotel service charges across stateroom attendants, dining staff, and galley teams.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Cabin Allocation & Turnaround:</strong> Crew cabin assignments optimized based on rank, departmental shifts, and language pairings.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Crew Systems Architecture</div>
            <table class="data-table">
              <thead><tr><th>System</th><th>Domain</th><th>Critical Capability</th></tr></thead>
              <tbody>
                <tr><td><strong>Adonis Maritime HR</strong></td><td>Crewing & STCW</td><td>Biometric time clocks, rest-hour compliance, contract rotations</td></tr>
                <tr><td><strong>MXP MarineXchange</strong></td><td>Food & Beverage Ops</td><td>Galley recipe scaling, inventory requisitions, nutrition labeling</td></tr>
                <tr><td><strong>HotSOS / Service Cloud</strong></td><td>Maintenance & Housekeeping</td><td>Stateroom maintenance dispatch, AC repair tracking</td></tr>
                <tr><td><strong>Brightwell / ShipMoney</strong></td><td>Crew Payroll & Remittance</td><td>Multi-currency digital wallets allowing crew to remit earnings home</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "STCW rest-hour compliance is legally binding. Port state authorities will impound a ship if crew rest hours are falsified."
    },
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "Safety, Emergency Response & Environmental",
        "subtitle": "Automated SOLAS muster compliance, lifeboat allocation, and environmental monitoring",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Emergency Systems & SOLAS Compliance</div>
            <div class="flow-step"><div class="step-num">🚨</div><div><strong>Real-Time Lifeboat Allocation:</strong> System dynamically calculates life raft and lifeboat capacity (125% of total souls on board required by SOLAS) based on stateroom deck assignments.</div></div>
            <div class="flow-step"><div class="step-num">📱</div><div><strong>Emergency Mustering Dashboard:</strong> Bridge safety console displays real-time headcounts per muster station during emergency drills or incidents.</div></div>
            <div class="flow-step"><div class="step-num">🦺</div><div><strong>Missing Souls Locator:</strong> Instantly queries OceanMedallion / Wi-Fi telemetry to pinpoint the last known deck location of any un-mustered passenger.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Environmental Compliance & Telematics</div>
            <table class="data-table">
              <thead><tr><th>Environmental Domain</th><th>Monitoring Tech</th><th>Compliance Mandate</th></tr></thead>
              <tbody>
                <tr><td><strong>Oily Water Separator (OWS)</strong></td><td>White Box tamper-proof digital data recorder</td><td>MARPOL Annex I (Zero discharge &gt;15ppm)</td></tr>
                <tr><td><strong>Advanced Wastewater (AWTS)</strong></td><td>Automated effluent turbidity & pH sensors</td><td>Alaska / Baltic Sea Special Area rules</td></tr>
                <tr><td><strong>Exhaust Gas Cleaning (Scrubbers)</strong></td><td>Continuous Emissions Monitoring (CEMS)</td><td>IMO 0.50% Global Sulphur Cap</td></tr>
                <tr><td><strong>Cold Ironing (Shore Power)</strong></td><td>High-voltage shore connection telemetry</td><td>Port of Los Angeles / EU Fit for 55</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "The bridge missing souls locator is a lifesaver: it can tell the captain within seconds where an un-accounted passenger was last seen."
    },

    # PART 9: AI & AGENTIC SYSTEMS (42-46)
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Maritime Enterprise AI Architecture",
        "subtitle": "Hierarchical agentic fabric balancing shipboard edge inference with cloud foundation models",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Dual-Realm AI Architecture</div>
            <div class="flow-step"><div class="step-num">☁️</div><div><strong>Cloud Foundation Tier (Shoreside):</strong> Large frontier models (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro) running in cloud hyperscalers for complex marketing journey generation, global yield optimization, and IT code development.</div></div>
            <div class="flow-step"><div class="step-num">⚓</div><div><strong>Edge Quantized Tier (Shipboard):</strong> Quantized 8B/14B parameter models (Llama 3, Mistral NeMo) hosted on shipboard GPU servers (NVIDIA A10/A30) delivering zero-latency guest service during satellite blackouts.</div></div>
            <div class="flow-step"><div class="step-num">🛡️</div><div><strong>Maritime Guardrails:</strong> Strict safety filters preventing AI agents from giving unauthorized navigation advice, promising safety exemptions, or committing unauthorized financial refunds.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">AI Architecture Topology</div>
            <div class="mermaid">
            flowchart TD
              Guest["Cruiser Mobile App / In-Room TV"] --> Gateway["Edge API Gateway"]
              Gateway --> Router{"Satellite Link Active?"}
              Router -->|Yes| CloudLLM["Cloud Frontier Model<br>(Agentforce / Azure OpenAI)"]
              Router -->|No / Latency Sensitive| EdgeLLM["Shipboard Quantized LLM<br>(Local vLLM / Ollama Cluster)"]
              CloudLLM --> Tools["Enterprise Tool Execution"]
              EdgeLLM --> EdgeTools["Local PMS / POS Tools"]
              Tools --> Response["Action / Response to Cruiser"]
              EdgeTools --> Response
            </div>
          </div>
        </div>
        """,
        "notes": "Edge LLMs on shipboard GPUs guarantee that the virtual butler never goes silent just because the ship is sailing through a storm."
    },
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Multi-Agent Systems & Role Specialization",
        "subtitle": "Autonomous AI agents collaborating across guest concierge, excursion dispatch, and fleet yield",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Specialized Maritime AI Agents</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Autonomous Stateroom Butler:</strong> Answers guest questions about daily ship activities, books specialty dining, adjusts room temperature, and orders room service.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>ShoreEx Weather Adaptation Agent:</strong> Monitors satellite weather feeds; if rain is predicted in Cozumel, automatically suggests alternative indoor cultural tours to booked guests.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Casino VIP Host Agent:</strong> Analyzes real-time table drop and slot play; dispatches personalized comps (bottle of champagne, steakhouse invite) directly to the high-roller.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Turnaround Operations Agent:</strong> Tracks luggage offload progress and stateroom cleaning velocity, alerting hotel directors to bottlenecks.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Multi-Agent Collaboration Architecture</div>
            <div class="mermaid">
            flowchart TD
              Butler["Stateroom Butler Agent"] <--> Supervisor["Shipboard Agent Supervisor"]
              ShoreEx["ShoreEx Dispatch Agent"] <--> Supervisor
              Casino["Casino Host Agent"] <--> Supervisor
              Ops["Turnaround Ops Agent"] <--> Supervisor
              Supervisor --> PMS["Fidelio PMS"]
              Supervisor --> POS["Simphony POS"]
              Supervisor --> Weather["NOAA Weather API"]
            </div>
          </div>
        </div>
        """,
        "notes": "Agent specialization prevents prompt bloat and allows each agent to operate with laser-focused domain tools and permissions."
    },
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Model Context Protocol & Maritime Tooling",
        "subtitle": "Connecting agentic AI to shipboard and shoreside systems via standardized MCP tool servers",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">MCP Tool Catalog for Maritime</div>
            <table class="data-table">
              <thead><tr><th>MCP Tool Name</th><th>Target System</th><th>Parameters & Function</th></tr></thead>
              <tbody>
                <tr><td><code>check_cabin_availability</code></td><td>Versonix CRS</td><td>VoyageID, DeckNo, Category; returns vacant staterooms.</td></tr>
                <tr><td><code>post_folio_charge</code></td><td>Fidelio PMS</td><td>BookingID, Amount, DepartmentCode; charges guest stateroom.</td></tr>
                <tr><td><code>query_guest_location</code></td><td>OceanMedallion BLE</td><td>CruiserID; returns Deck, Zone, nearest BeaconID.</td></tr>
                <tr><td><code>book_shore_excursion</code></td><td>ShoreEx Engine</td><td>BookingID, TourCode, PaxCount; generates digital voucher.</td></tr>
                <tr><td><code>dispatch_maintenance_ticket</code></td><td>HotSOS</td><td>StateroomID, IssueType (Plumbing/AC), Priority; creates work order.</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">MCP Tool Execution Example</div>
            <pre style="background: rgba(0,0,0,0.4); padding: 0.8rem; border-radius: 6px; font-size: 0.75rem; color: #a5d6a7;">
// Stateroom Butler MCP Tool Execution
{
  "tool": "book_specialty_dining",
  "arguments": {
    "booking_id": "CRU-948210",
    "restaurant": "Crown Grill Steakhouse",
    "reservation_time": "2026-10-14T19:30:00Z",
    "party_size": 2,
    "special_requests": "Anniversary table near window"
  }
}
// Response from Shipboard Simphony POS
{
  "status": "CONFIRMED",
  "table_number": "Table 14 (Window)",
  "cover_charge_total": 98.00,
  "folio_transaction_id": "TXN-881920"
}
            </pre>
          </div>
        </div>
        """,
        "notes": "Model Context Protocol (MCP) gives AI agents structured, auditable, and secure programmatic access to enterprise systems."
    },
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Predictive ML & Maritime Operational Forecasting",
        "subtitle": "Data-driven optimization of fuel consumption, galley food waste, and stateroom turnaround",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header">Fuel & Trim Optimization</div>
            <p><strong>Model:</strong> Physics-informed neural networks trained on NMEA hull speed, draft, wave height, and engine RPM.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-green">Impact</span></p>
              <p>Recommends optimal vessel trim (ballast water distribution) and speed profiles, saving 4.5% in fleet fuel burn ($38M+ annually).</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Galley Food Waste Reduction</div>
            <p><strong>Model:</strong> Computer vision cameras over galley waste chutes + predictive passenger consumption models.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-blue">Impact</span></p>
              <p>Forecasts exact buffet and dining prep quantities based on passenger demographics, cutting food waste by 28% and provisioning costs by $14M.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Predictive HVAC Control</div>
            <p><strong>Model:</strong> Gradient boosted decision trees predicting stateroom thermal load based on sun angle and ship heading.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-purple">Impact</span></p>
              <p>Pre-cools staterooms during off-peak generator cycles, reducing peak electrical load by 12% across 2,000 cabins.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Predictive ML in maritime delivers massive ESG and financial wins: fuel and food waste savings pay for the entire software stack."
    },
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Deflection, Resolution & Maritime AI ROI",
        "subtitle": "Quantifying the financial and operational impact of AI automation across fleet and contact centers",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">AI Operational Impact Metrics</div>
            <table class="data-table">
              <thead><tr><th>Domain</th><th>Pre-AI Baseline</th><th>AI-Assisted State</th><th>Net Business Value</th></tr></thead>
              <tbody>
                <tr><td>Contact Center Deflection</td><td>15.0% (Basic IVR)</td><td>68.5% (Agentforce / CCAI)</td><td>$16.5M annual labor savings</td></tr>
                <tr><td>Front Desk Queue Length</td><td>25 minutes avg wait</td><td>4 minutes avg wait</td><td>+18 points in Guest NPS</td></tr>
                <tr><td>Onboard Incremental Spend</td><td>$480 / passenger</td><td>$545 / passenger</td><td>+$65M gross onboard margin</td></tr>
                <tr><td>ShoreEx Late Cancellations</td><td>8.5% cancellation</td><td>2.2% cancellation</td><td>$6.8M recovered tour revenue</td></tr>
                <tr><td>Turnaround Time Overruns</td><td>14% of sailings</td><td>1.5% of sailings</td><td>$8.2M port congestion fee savings</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">The $116M Annual Value Creation Engine</div>
            <div class="flow-step"><div class="step-num">$</div><div><strong>Direct Revenue Lift:</strong> +$65M in incremental onboard spend generated via personalized AI recommendations (dining, spa, excursions).</div></div>
            <div class="flow-step"><div class="step-num">⚙️</div><div><strong>Operational Efficiency:</strong> $24.7M in contact center labor and port delay savings.</div></div>
            <div class="flow-step"><div class="step-num">🌱</div><div><strong>Fuel & Food Savings:</strong> $26.3M in fuel trim optimization and food waste reduction.</div></div>
            <div style="margin-top: 1rem;">
              <span class="pill pill-green">Total Annual Value: $116.0M across fleet</span>
            </div>
          </div>
        </div>
        """,
        "notes": "The ROI of AI in cruising is extraordinary because it impacts both sides of the P&L: boosting high-margin onboard revenue while cutting fuel and labor."
    },

    # PART 10: MASTER INTEGRATION & ROADMAP (47-52)
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Master Enterprise Integration Topology",
        "subtitle": "End-to-end integration topology connecting shipboard edge data centers with shoreside cloud hyperscalers",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">Master Fleet-to-Cloud Integration Topology</div>
          <div class="mermaid">
          flowchart LR
            subgraph Vessel["Shipboard Edge Environment (per Ship)"]
              HCI["Nutanix Dual-Node HCI"]
              PMS_E["Fidelio Cruise PMS"]
              POS_E["Simphony POS"]
              IOT_E["OceanMedallion Beacons"]
              KF_E["Local Kafka Broker"]
              GW_E["MuleSoft Edge Gateway"]
              HCI --- PMS_E & POS_E & IOT_E & KF_E & GW_E
            end
            subgraph WAN["Satellite SD-WAN Hybrid"]
              STAR["Starlink Maritime LEO (250 Mbps)"]
              O3B["SES O3b mPOWER GEO (100 Mbps)"]
              PEP["Peplink SD-WAN Router"]
              PEP --- STAR & O3B
            end
            subgraph Cloud["Shoreside Cloud Enterprise Core"]
              DC["Salesforce Data Cloud / Snowflake"]
              CRM["Salesforce Core / Dynamics 365"]
              MULE["Enterprise MuleSoft Anypoint"]
              ERP["SAP S/4HANA Cloud"]
              KF_C["Confluent Cloud Kafka Mesh"]
            end
            Vessel <-->|Encrypted WireGuard Tunnel| WAN
            WAN <-->|Direct Connect / ExpressRoute| Cloud
          </div>
        </div>
        """,
        "notes": "This master topology summarizes the complete hybrid edge-to-cloud architecture for a modern cruise fleet."
    },
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Ship-to-Shore Protocol Translation & Edge Sync",
        "subtitle": "Detailed architecture of satellite bandwidth optimization, compression, and deduplication",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Optimization Pipeline Stages</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>In-Memory Change Data Capture:</strong> Debezium captures database row deltas from Fidelio MySQL and Simphony Oracle DB without polling overhead.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Schema Evolution with Confluent Schema Registry:</strong> Avro binary serialization enforces strict backward-compatible schemas between ship and shore.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Sliding-Window Deduplication:</strong> Identical telemetry events (e.g., unchanged GPS coordinates, duplicate RFID taps) dropped prior to transmission.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Adaptive Bitrate Throttling:</strong> Transmission rates automatically scale up or down based on real-time satellite ping latency and packet loss.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Compression & Bandwidth Benchmark</div>
            <table class="data-table">
              <thead><tr><th>Data Stream</th><th>Raw JSON / hr</th><th>Avro + Zstandard / hr</th><th>Bandwidth Saved</th></tr></thead>
              <tbody>
                <tr><td>POS Transaction Logs</td><td>145 MB</td><td>18 MB</td><td><span style="color: var(--accent-green); font-weight: 700;">87.6%</span></td></tr>
                <tr><td>PMS Guest State Deltas</td><td>85 MB</td><td>12 MB</td><td><span style="color: var(--accent-green); font-weight: 700;">85.9%</span></td></tr>
                <tr><td>NMEA Vessel Telematics</td><td>320 MB</td><td>38 MB</td><td><span style="color: var(--accent-green); font-weight: 700;">88.1%</span></td></tr>
                <tr><td>IoT Location Beacons</td><td>1.2 GB</td><td>110 MB</td><td><span style="color: var(--accent-green); font-weight: 700;">90.8%</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Saving 88% on bandwidth makes the difference between a sluggish satellite connection and a responsive real-time cloud data pipeline."
    },
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Phased Implementation Roadmap (24 Months)",
        "subtitle": "Strategic four-phase execution timeline mitigating operational risk across an active sailing fleet",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Four Implementation Phases</div>
            <div class="flow-step"><div class="step-num">P1</div><div><strong>Months 1-6: Foundation & Edge Infrastructure:</strong> Upgrade shipboard HCI to Nutanix, install Starlink Maritime terminals, deploy local Kafka brokers and Peplink SD-WAN across lead vessels.</div></div>
            <div class="flow-step"><div class="step-num">P2</div><div><strong>Months 7-12: Core Data Fabric & Guest 360:</strong> Stand up Salesforce Data Cloud / Snowflake lakehouse, configure identity resolution, and establish bi-directional CDC replication between PMS and cloud.</div></div>
            <div class="flow-step"><div class="step-num">P3</div><div><strong>Months 13-18: Mobile, Wearables & Turnaround:</strong> Roll out new guest mobile app with e-muster, biometric terminal gates, and cashless wearable tap-to-pay.</div></div>
            <div class="flow-step"><div class="step-num">P4</div><div><strong>Months 19-24: Autonomous AI & Fleet Twin:</strong> Deploy Agentforce concierge, Palantir fuel optimization twin, and algorithmic cabin upgrade auction.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Fleet Rollout Phasing Strategy</div>
            <div class="mermaid">
            flowchart TD
              Pilot["Phase 1: Pilot Lead Vessel (1 Ship)"] --> DryDock["Phase 2: Scheduled Dry Dock Retrofits (5 Ships)"]
              DryDock --> FleetWave1["Phase 3: Wave 1 Active Sailing Fleet (12 Ships)"]
              FleetWave1 --> FleetWave2["Phase 4: Wave 2 Global Fleet Completion (All 30+ Ships)"]
            </div>
            <div style="margin-top: 1rem; font-size: 0.85rem; color: var(--text-muted);">
              <p><strong>Critical Risk Mitigation:</strong> New software deployments scheduled during designated dry-dock periods or turnaround days to avoid impacting active guest cruises.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Phasing retrofits around scheduled dry-dock periods is essential in maritime IT; you cannot install new core infrastructure while passengers are on board."
    },
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Target Operating Model & Change Management",
        "subtitle": "Structuring organization, shipboard crew enablement, and cross-functional agile squads",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Target Operating Model (BCG Framework)</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Fleet Digital Product Squads:</strong> Cross-functional agile squads (Product Owner, Cloud Architect, Marine Systems Engineer, UX Designer) dedicated to specific passenger journeys (e.g., Turnaround Squad, Onboard Commerce Squad).</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Shipboard Systems Officers (SSO):</strong> Elevated role for onboard IT officers, transitioning from break-fix hardware technicians to edge reliability engineers (SREs).</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Shoreside Maritime Operations Center (MOC):</strong> 24/7 centralized monitoring facility tracking satellite WAN latency, shipboard PMS sync, and fuel telematics in real time.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Crew Change Management Principles</div>
            <table class="data-table">
              <thead><tr><th>Stakeholder Group</th><th>Primary Resistance</th><th>Change Strategy</th></tr></thead>
              <tbody>
                <tr><td>Stateroom Attendants</td><td>Fear of digital mobile housekeeping apps replacing paper checklists.</td><td>Intuitive pictorial mobile UI, multilingual support (Tagalog, Hindi, Spanish), automatic gratuity bonuses.</td></tr>
                <tr><td>Front Desk Crew</td><td>Anxiety over AI deflection eliminating customer service jobs.</td><td>Reposition agents as "Guest Experience Ambassadors" with mobile tablets resolving VIP requests.</td></tr>
                <tr><td>Marine Engineers</td><td>Skepticism toward AI fuel/trim recommendations.</td><td>Transparent explanation of physics-based models; captain retains final override authority.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Crew enablement is the #1 predictor of cruise IT success. If the crew finds the mobile tool confusing, they will revert to paper."
    },
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Architecture Evaluation Scorecard & Benchmark",
        "subtitle": "Objective multi-criteria evaluation comparing the three architectural variations across five dimensions",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Evaluation Dimension Scorecard (1 to 5 Scale)</div>
            <table class="data-table">
              <thead><tr><th>Evaluation Dimension</th><th>Var 1: Salesforce</th><th>Var 2: Open Stack</th><th>Var 3: Best Money</th></tr></thead>
              <tbody>
                <tr><td><strong>Edge Autonomy & Offline Resilience</strong></td><td>4.2 / 5.0</td><td>4.8 / 5.0</td><td>4.9 / 5.0</td></tr>
                <tr><td><strong>Speed of Implementation (Time-to-Value)</strong></td><td>4.6 / 5.0</td><td>3.2 / 5.0</td><td>3.6 / 5.0</td></tr>
                <tr><td><strong>Guest Experience & Frictionless IoT</strong></td><td>4.3 / 5.0</td><td>3.9 / 5.0</td><td>5.0 / 5.0</td></tr>
                <tr><td><strong>Total Cost of Ownership (TCO)</strong></td><td>3.8 / 5.0</td><td>4.2 / 5.0</td><td>2.4 / 5.0</td></tr>
                <tr><td><strong>AI Automation & Multi-Agent Maturity</strong></td><td>4.7 / 5.0</td><td>3.8 / 5.0</td><td>4.9 / 5.0</td></tr>
                <tr style="font-weight: 700; background: rgba(255,255,255,0.05);">
                  <td><strong>Blended Composite Score</strong></td>
                  <td><span style="color: var(--accent-blue);">4.32 / 5.00</span></td>
                  <td><span style="color: var(--accent-green);">3.98 / 5.00</span></td>
                  <td><span style="color: var(--accent-purple);">4.16 / 5.00</span></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Architectural Recommendation</div>
            <div class="flow-step"><div class="step-num">🏆</div><div><strong>Best Commercial Balance: Variation 1 (With Salesforce):</strong> Delivers the highest time-to-value and commercial agility, bridging the gap between B2B travel advisor networks, guest personalization, and shipboard operations.</div></div>
            <div class="flow-step"><div class="step-num">🚀</div><div><strong>Ultra-Tier Luxury / Sovereign: Variation 3:</strong> Recommended for mega-cruise operators ($5B+ revenue) where wearable IoT (OceanMedallion) and fleet digital twins (Palantir) unlock hundreds of millions in EBITDA.</div></div>
          </div>
        </div>
        """,
        "notes": "Variation 1 wins on speed-to-value and commercial harmony, while Variation 3 is the ultimate technological weapon for massive global fleets."
    },
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Executive Conclusion & Maritime North Star",
        "subtitle": "The definitive architectural vision for the future of ocean travel and maritime hospitality",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Architectural Takeaways</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>The Ship is an Autonomous Edge Node:</strong> Never compromise shipboard edge independence. Every core guest transaction must function when disconnected at sea.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>LEO Satellite is the Great Enabler:</strong> Starlink Maritime has unlocked real-time cloud data harmony, turning vessels into active participants in the enterprise data fabric.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Onboard Spend is the Profit Engine:</strong> Technology investments must focus on reducing transaction friction at bars, restaurants, spas, and shore excursions.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>AI Multi-Agent Systems are the Frontier:</strong> Autonomous concierges and operational agents will drive the next $100M+ in cruise line value creation.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic North Star Architecture</div>
            <div style="text-align: center; padding: 1.5rem 0;">
              <div class="metric-hero" style="font-size: 2.2rem; color: var(--accent-green);">Connected • Autonomous • Frictionless</div>
              <p style="margin-top: 1rem; color: var(--text-muted); font-size: 0.95rem;">A unified enterprise maritime ecosystem connecting shoreside commercial agility with shipboard edge excellence, delivering unforgettable guest memories and superior shareholder returns.</p>
              <div style="margin-top: 1.5rem;">
                <span class="pill pill-blue">52 Master Slides Complete</span>
                <span class="pill pill-purple">Full Enterprise Compendium</span>
              </div>
            </div>
          </div>
        </div>
        """,
        "notes": "Thank you executive team. We are now open for architecture review and deep-dive technical discussions."
    }
]

if __name__ == "__main__":
    html_output_path = os.path.join(BASE_DIR, "cruises", "presentation.html")
    md_output_path = os.path.join(BASE_DIR, "cruises", "PRESENTATION_FRAMEWORK_COMPENDIUM.md")

    # Apply visual enhancements (interactive charts, Mermaid architectures, CLI suites)
    slides = vsc.apply_visual_enhancements("CRUISES", slides)

    engine.render_reveal_html(meta, slides, html_output_path)
    engine.render_presentation_markdown(meta, slides, md_output_path)
    print("Cruises presentation generation complete. Total slides:", len(slides))
