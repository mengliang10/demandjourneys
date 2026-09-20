#!/usr/bin/env python3
"""
Tours, Activities & Experiences Presentation Generator — 52 Slides
Generates:
1. /run/media/ml/Storage/Labs/tours/presentation.html
2. /run/media/ml/Storage/Labs/tours/PRESENTATION_FRAMEWORK_COMPENDIUM.md
"""

import os
import sys
import json

BASE_DIR = "/run/media/ml/Storage/Labs"
sys.path.append(BASE_DIR)
import generate_presentation_engine as engine
import visual_slide_components as vsc

meta = {
    "title": "Tours, Activities & Experiences Systems Architecture",
    "short_code": "TOURS",
    "sector": "Tours, Attractions, Activities & Experiential Travel",
    "scale": "$220.0B Tour & Activity GBV • 1.8B Experiences • $122.22 Blended Ticket • $132.0B OTA Share"
}

slides = [
    # PART 1: MACROECONOMICS, SIZING & REVENUE MODELS (1-5)
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Tours & Experiences Architecture Masterclass",
        "subtitle": "Systems Architecture, Technology Stacks, and Operational Orchestration across 13 Enterprise Dimensions",
        "content": """
        <div class="grid-2" style="margin-top: 1rem;">
          <div class="glass-card">
            <div class="card-header">Executive Briefing Scope</div>
            <p>Comprehensive architectural blueprint analyzing the mission-critical systems governing modern tour operators, attractions, day excursions, and adventure experiences ($220B global market, 1.8B experiences sold). Designed for Experience CIOs, Chief Commercial Officers, VP Operations, and Enterprise Architects.</p>
            <div style="margin-top: 1rem;">
              <span class="pill pill-blue">13 Enterprise Layers</span>
              <span class="pill pill-green">3 Stack Variations</span>
              <span class="pill pill-purple">52 Master Slides</span>
              <span class="pill pill-amber">OCTO API Connectivity</span>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Core Themes Covered</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Requirements & Governance:</strong> ResTech fragmentation, high OTA commission friction (15-25%), field offline constraints, and waiver legal enforceability.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>13-Layer Master Architecture:</strong> ResTech booking engines (Bokun/FareHarbor), OCTO distribution APIs, Samsara fleet telematics, Smartwaiver, CRM, CDP, AI.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>End-to-End Traveler Journeys:</strong> In-destination mobile discovery, instant OTA booking, automated digital waiver completion, turnstile check-in, and photo upsell.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>AI-Assisted Efficiency:</strong> Agentforce weather disruption rebooking, Palantir guide/fleet dispatch, and dynamic pricing yield algorithms.</div></div>
          </div>
        </div>
        """,
        "notes": "Welcome executive stakeholders. This deck provides an unbroken technical and commercial chain of logic across all tour and activity technology layers."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Global Tour & Activity Sizing & Revenue Architecture",
        "subtitle": "Macroeconomic baseline: $220.0B Gross Booking Value across 1.8 Billion annual experiences",
        "content": """
        <div class="grid-4" style="margin-bottom: 1rem;">
          <div class="glass-card">
            <div class="metric-hero">$220.0B</div>
            <div class="metric-label">Experiences GBV</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Global tours, activities & attractions</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">1.8B</div>
            <div class="metric-label">Annual Experiences</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Tickets and participant bookings</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">$122.22</div>
            <div class="metric-label">Blended Ticket Price</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Average spend per participant</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">1.2M+</div>
            <div class="metric-label">Global Operators</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Highly fragmented supplier ecosystem</p>
          </div>
        </div>
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Sector Composition & Volume</div>
            <table class="data-table">
              <thead><tr><th>Category</th><th>Share</th><th>USD Total</th><th>Primary Tech Needs</th></tr></thead>
              <tbody>
                <tr><td>Day Tours & Sightseeing</td><td>38.0%</td><td>$83.6B</td><td>Fleet telematics, guide dispatch, audio guides</td></tr>
                <tr><td>Attractions & Museums</td><td>26.0%</td><td>$57.2B</td><td>Timed entry turnstiles, barcode ticketing, queues</td></tr>
                <tr><td>Adventure & Outdoor</td><td>18.0%</td><td>$39.6B</td><td>Digital waivers, equipment sizing, safety certs</td></tr>
                <tr><td>Water Sports & Marine</td><td>11.0%</td><td>$24.2B</td><td>Coast guard manifests, weather ops, vessel GPS</td></tr>
                <tr><td>Culinary & Cultural</td><td>7.0%</td><td>$15.4B</td><td>Dietary allergy tracking, chef scheduling</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Macro Operational Economics</div>
            <div class="flow-step"><div class="step-num">⚡</div><div><strong>High Fragmentation:</strong> Over 80% of operators generate &lt;$1M in annual revenue, relying on plug-and-play ResTech (FareHarbor, Bokun, Peek Pro).</div></div>
            <div class="flow-step"><div class="step-num">📱</div><div><strong>Last-Minute In-Destination Booking:</strong> 48% of all tours and activities are booked within 48 hours of departure, demanding instantaneous mobile checkout and real-time inventory locking.</div></div>
            <div class="flow-step"><div class="step-num">🌧️</div><div><strong>Weather Sensitivity:</strong> Outdoor activities suffer 15-25% weather-driven cancellation rates, requiring automated rescheduling and voucher credit engines.</div></div>
          </div>
        </div>
        """,
        "notes": "The tours and activities sector is the third largest segment in travel, but by far the most fragmented and digitally underserved."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Economic Friction: Direct vs OTA Intermediation",
        "subtitle": "Distribution channel analysis: $132.0B booked via OTAs (Viator, GetYourGuide, Klook) vs $88.0B direct",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Channel Distribution Mix</div>
            <table class="data-table">
              <thead><tr><th>Channel</th><th>GBV Share</th><th>Volume</th><th>Commission / Cost</th></tr></thead>
              <tbody>
                <tr><td><strong>Global OTAs</strong><br>(Viator / Tripadvisor, GetYourGuide, Klook)</td><td>60.0%</td><td>$132.0B</td><td>20.0% - 25.0% commission ($26.4B - $33.0B)</td></tr>
                <tr><td><strong>Direct Operator Web & Mobile</strong><br>(Direct-to-Consumer)</td><td>28.0%</td><td>$61.6B</td><td>2.9% + $0.30 payment processing + SEO/SEM</td></tr>
                <tr><td><strong>Concierge & Hotel Desks</strong><br>(In-Destination Affiliates)</td><td>7.0%</td><td>$15.4B</td><td>10.0% - 15.0% local partner commission</td></tr>
                <tr><td><strong>Walk-up / Field Kiosk</strong><br>(Cash / Terminal POS)</td><td>5.0%</td><td>$11.0B</td><td>2.5% merchant processing + kiosk hardware</td></tr>
              </tbody>
            </table>
            <div style="margin-top: 1rem;">
              <span class="pill pill-red">$31.68B Annual Distribution Friction</span>
              <span class="pill pill-green">$188.32B Net Retained Revenue</span>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">The OTA Dependency Trap</div>
            <p>While OTAs provide global customer acquisition, they charge steep 20-25% commissions and intentionally mask customer data (e.g., providing opaque emails like <code>12a3bc@guest.viator.com</code>), preventing operators from marketing directly to guests.</p>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Customer Data Re-Capture:</strong> Modern operators use mandatory digital waivers (Wherewolf/Smartwaiver) to capture real customer emails and phone numbers at check-in.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Direct Re-engagement:</strong> Automated post-tour photo delivery and SMS review campaigns drive direct re-booking for future travel.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Margin Recapture:</strong> Every 10% shift from OTAs to direct web bookings saves $13.2B in industry commission friction.</div></div>
          </div>
        </div>
        """,
        "notes": "Notice the 60% OTA share and 20-25% commission. The key architectural strategy for tour operators is using check-in waivers to de-anonymize OTA guests."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Cost & ROI Benchmark across 3 Variations",
        "subtitle": "Total Cost of Ownership (TCO) and 3-year commercial return comparison across architectural strategies",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-blue">Variation 1</span><br>With Salesforce</div>
            <div class="metric-hero" style="font-size: 1.8rem; margin: 0.5rem 0;">$5.5M - $9.5M</div>
            <div class="metric-label">Annual Software ACV</div>
            <div style="margin-top: 1rem; font-size: 0.85rem;">
              <p><strong>Implementation CapEx:</strong> $6.8M - $12.0M</p>
              <p><strong>Annual Run Cost:</strong> $2.2M - $3.8M / yr</p>
              <p><strong>3-Year ROI:</strong> <span style="color: var(--accent-green); font-weight: 700;">350%</span></p>
              <p><strong>Payback Horizon:</strong> 9 Months</p>
              <p><strong>Core Advantage:</strong> Zero-Copy Data Cloud guest de-anonymization, Agentforce autonomous weather rebooking, and MuleSoft OCTO connectors to OTAs.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-green">Variation 2</span><br>Without Salesforce (Open)</div>
            <div class="metric-hero" style="font-size: 1.8rem; margin: 0.5rem 0;">$4.5M - $7.8M</div>
            <div class="metric-label">Annual Software ACV</div>
            <div style="margin-top: 1rem; font-size: 0.85rem;">
              <p><strong>Implementation CapEx:</strong> $7.5M - $13.5M</p>
              <p><strong>Annual Run Cost:</strong> $3.1M - $5.0M / yr</p>
              <p><strong>3-Year ROI:</strong> <span style="color: var(--accent-blue); font-weight: 700;">270%</span></p>
              <p><strong>Payback Horizon:</strong> 13 Months</p>
              <p><strong>Core Advantage:</strong> Zero vendor lock-in, open-source lakehouse (Databricks/Snowflake), mobile push via Braze, and custom LLM destination agents.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-purple">Variation 3</span><br>Best Money Can Buy</div>
            <div class="metric-hero" style="font-size: 1.8rem; margin: 0.5rem 0;">$16.5M - $28M</div>
            <div class="metric-label">Annual Software ACV</div>
            <div style="margin-top: 1rem; font-size: 0.85rem;">
              <p><strong>Implementation CapEx:</strong> $22.0M - $38.0M</p>
              <p><strong>Annual Run Cost:</strong> $7.2M - $11.5M / yr</p>
              <p><strong>3-Year ROI:</strong> <span style="color: var(--accent-purple); font-weight: 700;">460%</span></p>
              <p><strong>Payback Horizon:</strong> 11 Months</p>
              <p><strong>Core Advantage:</strong> Palantir Foundry fleet & guide kinetic twin, Adobe Experience Platform sub-50ms personalization, and Samsara AI Fleet telematics.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Variation 1 has the fastest payback (9 months) due to rapid de-anonymization of OTA guests and automated weather disruption management."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Experiences Macro Drivers & Tech Imperatives",
        "subtitle": "Five structural forces transforming modern tour operations, distribution, and field execution",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Structural Industry Drivers</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Last-Minute Mobile Shift:</strong> 72% of millennial/Gen-Z travelers book experiences on mobile devices while already in-destination, demanding sub-second instant confirmation.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>The OCTO API Standard:</strong> The Open Connectivity for Tourism (OCTO) standardizes real-time availability and booking APIs across OTAs and ResTech platforms.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Digital Safety & Liability Waivers:</strong> Transition from physical paper clipboards to legally binding digital waivers (Smartwaiver, Wherewolf) completed on guests' phones.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Fleet Telematics & Guide Safety:</strong> IoT vehicle telematics (Samsara) and satellite personal beacons (Garmin inReach) protect guests in remote wilderness terrain.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Architectural Implications</div>
            <table class="data-table">
              <thead><tr><th>Driver</th><th>Legacy Approach</th><th>Modern Architecture</th></tr></thead>
              <tbody>
                <tr><td>OTA Distribution</td><td>Manual extranet inventory updates</td><td>Real-time bi-directional OCTO OpenAPI 3.0</td></tr>
                <tr><td>Guest Waivers</td><td>Paper clipboards signed at check-in</td><td>Mobile SMS waiver pre-arrival + OCR verification</td></tr>
                <tr><td>Weather Closures</td><td>Manual phone calls & frantic re-ticketing</td><td>Autonomous Agentforce weather rebooking</td></tr>
                <tr><td>Fleet Operations</td><td>Two-way radios & paper driver logs</td><td>Samsara AI GPS telematics + automated dispatch</td></tr>
                <tr><td>Customer Data</td><td>Anonymous OTA passenger names</td><td>Unified Traveler 360 de-anonymized via waivers</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "OCTO API and mobile digital waivers are the two pillars that dragged the tours and activities industry into the 21st century."
    },

    # PART 2: ASSUMED REQUIREMENTS & CONSTRAINTS (6-10)
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Tour & Activity Functional Requirements Matrix",
        "subtitle": "Operational capabilities required across booking, distribution, field operations, and guest safety",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Functional Domains</div>
            <table class="data-table">
              <thead><tr><th>Domain</th><th>Critical Capabilities</th><th>Priority</th></tr></thead>
              <tbody>
                <tr><td><strong>ResTech Booking Engine</strong></td><td>Real-time slot availability, resource-based capacity (guides/vehicles), dynamic pricing</td><td><span class="pill pill-red">P0 Critical</span></td></tr>
                <tr><td><strong>OTA Channel Manager</strong></td><td>Bi-directional sync with Viator, GetYourGuide, Klook via OCTO standard; rate parity</td><td><span class="pill pill-red">P0 Critical</span></td></tr>
                <tr><td><strong>Digital Waivers & Safety</strong></td><td>ESIGN/UETA compliant waiver capture, minor consent, medical disclosure, emergency contact</td><td><span class="pill pill-red">P0 Legal</span></td></tr>
                <tr><td><strong>Field Check-in & Manifest</strong></td><td>Mobile QR barcode scan, offline handheld check-in, real-time headcounts, no-show release</td><td><span class="pill pill-blue">P1 Operations</span></td></tr>
                <tr><td><strong>Fleet & Guide Dispatch</strong></td><td>Guide credential matching (WFR/languages), vehicle maintenance tracking, GPS route optimization</td><td><span class="pill pill-blue">P1 Operations</span></td></tr>
                <tr><td><strong>Post-Tour Merchandising</strong></td><td>Digital photo/video automated facial matching, direct review generation (Tripadvisor/Google)</td><td><span class="pill pill-amber">P2 Revenue</span></td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Operational Decoupling Requirements</div>
            <div class="flow-step"><div class="step-num">🌲</div><div><strong>Remote Field Autonomy:</strong> Guides leading tours in remote national parks, canyons, or open ocean must be able to verify manifests, check in guests, and record incidents with zero cellular coverage.</div></div>
            <div class="flow-step"><div class="step-num">🌐</div><div><strong>Global OTA Real-Time Lock:</strong> When the last 2 seats on a catamaran tour are booked via Viator, GetYourGuide must receive an immediate availability push to prevent double-booking.</div></div>
            <div class="flow-step"><div class="step-num">⚡</div><div><strong>Sub-Second Check-in Throughput:</strong> Attractions handling 5,000 visitors per hour require turnstile barcode scan latencies under 200 milliseconds.</div></div>
          </div>
        </div>
        """,
        "notes": "Notice how resource-based capacity works: a tour isn't just limited by seats on a bus; it's limited by guide-to-guest legal ratios and equipment availability."
    },
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Non-Functional & Operational SLA Requirements",
        "subtitle": "Performance, availability, latency, and disaster recovery thresholds for high-volume experience operations",
        "content": """
        <div class="grid-4" style="margin-bottom: 1rem;">
          <div class="glass-card">
            <div class="metric-hero">&lt;500ms</div>
            <div class="metric-label">OCTO API Latency</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">OTA availability & booking check SLA</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">99.99%</div>
            <div class="metric-label">Peak Season Uptime</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Zero downtime during summer/holidays</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">&lt;200ms</div>
            <div class="metric-label">Turnstile Scan Speed</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Attraction barcode/QR validation</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero">100%</div>
            <div class="metric-label">Offline Manifest SLA</div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Zero field lockouts without cellular</p>
          </div>
        </div>
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Scalability & Peak Season Elasticity</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>10x Seasonal Demand Spikes:</strong> Tour operators experience extreme seasonality (e.g., Alaska glacier tours operate exclusively May-September; European walking tours peak July-August). Infrastructure must auto-scale down 90% in winter.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Edge Caching with Cloudflare Workers:</strong> Static tour itineraries, images, and base pricing cached at 300+ global edge locations to absorb OTA scraping bots.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Distributed Inventory Locks:</strong> Redis-based distributed locks with 10-minute TTL to prevent inventory race conditions during high-volume flash sales.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Disaster Recovery & Redundancy</div>
            <table class="data-table">
              <thead><tr><th>Component</th><th>RTO</th><th>RPO</th><th>Strategy</th></tr></thead>
              <tbody>
                <tr><td>Booking Engine Core</td><td>&lt; 5 minutes</td><td>&lt; 1 second</td><td>Multi-region active-active database replication</td></tr>
                <tr><td>Field Check-in App</td><td>Instantaneous</td><td>0 seconds</td><td>Local SQLite database with opportunistic background sync</td></tr>
                <tr><td>Digital Waiver Vault</td><td>&lt; 1 hour</td><td>0 seconds</td><td>Immutable WORM cloud storage with multi-region backup</td></tr>
                <tr><td>Fleet GPS Telematics</td><td>&lt; 15 minutes</td><td>&lt; 10 seconds</td><td>Edge buffer on Samsara gateway uploading over cellular/Wi-Fi</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Because outdoor operations have 10x summer-to-winter swings, serverless and auto-scaling cloud architectures are vital to avoid burning cash in the off-season."
    },
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Field Constraints & Legacy Technical Debt",
        "subtitle": "Overcoming remote wilderness conditions, ResTech fragmentation, and legacy clipboards",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Remote Field Operational Constraints</div>
            <div class="flow-step"><div class="step-num">📡</div><div><strong>Zero Cellular Deadzones:</strong> Tours in national parks (Grand Canyon, Yellowstone) or coastal waters have zero LTE/5G. Mobile devices must operate in 100% offline standalone mode.</div></div>
            <div class="flow-step"><div class="step-num">🔋</div><div><strong>Battery & Environmental Durability:</strong> Guide handhelds must withstand 10-hour shifts in sub-zero alpine conditions or 45°C desert heat, with direct sunlight viewability (1,000+ nits).</div></div>
            <div class="flow-step"><div class="step-num">🔄</div><div><strong>Multi-Guide Manifest Conflicts:</strong> Two guides checking in guests simultaneously at different bus boarding doors in offline mode must reconcile without duplicating seats.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Legacy Technical Debt Hotspots</div>
            <table class="data-table">
              <thead><tr><th>Legacy Practice</th><th>Operational Failure Mode</th><th>Modern Architecture Solution</th></tr></thead>
              <tbody>
                <tr><td><strong>Paper Liability Waivers</strong></td><td>Illegible handwriting, lost paper files during lawsuits, massive check-in bottleneck.</td><td>Wherewolf / Smartwaiver mobile digital signing + cloud OCR extraction.</td></tr>
                <tr><td><strong>Manual OTA Extranets</strong></td><td>Staff manually entering Viator bookings into local booking software; double-bookings.</td><td>Bi-directional OCTO API automated channel management.</td></tr>
                <tr><td><strong>Two-Way VHF Radios</strong></td><td>Poor range, no automated dispatch, no record of vehicle location during emergencies.</td><td>Samsara AI Fleet GPS + Cellular Push-to-Talk (Zello).</td></tr>
                <tr><td><strong>Cash / Paper Vouchers</strong></td><td>Theft risk, slow accounting reconciliation, manual commission calculation.</td><td>Integrated Stripe Terminal / Square mobile card readers + tokenization.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Paper waivers are a massive legal liability. If a customer is injured and the paper waiver cannot be found in a physical filing cabinet, insurance won't cover it."
    },
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Regulatory, Safety & Compliance Framework",
        "subtitle": "Navigating commercial transport, public land permits, marine safety, and digital waiver legal enforceability",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Safety & Commercial Transportation Regulations</div>
            <div class="flow-step"><div class="step-num">🚌</div><div><strong>DOT & FMCSA Hours of Service (HOS):</strong> Tour bus and shuttle drivers must comply with Electronic Logging Device (ELD) mandates. Violations result in federal shutdowns.</div></div>
            <div class="flow-step"><div class="step-num">🏞️</div><div><strong>USFS & National Park Service (NPS) Permits:</strong> Commercial Use Authorizations (CUA) impose strict daily passenger quotas and guide-to-guest ratios (e.g., max 10 hikers per guide).</div></div>
            <div class="flow-step"><div class="step-num">⛵</div><div><strong>US Coast Guard (USCG) Passenger Vessel Safety:</strong> Commercial charter boats must maintain certified passenger manifests and drug testing compliance under Title 46 CFR.</div></div>
            <div class="flow-step"><div class="step-num">🧗</div><div><strong>OSHA & ACCT Standards:</strong> Zipline, climbing, and canopy tours require daily hardware torque inspections and logbooks.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Digital Legal & Privacy Compliance</div>
            <table class="data-table">
              <thead><tr><th>Regulation</th><th>Scope in Experiences</th><th>Architectural Requirement</th></tr></thead>
              <tbody>
                <tr><td><strong>ESIGN & UETA Acts</strong></td><td>Electronic signatures on liability waivers</td><td>Audit trail capturing IP address, timestamp, signature biometric stroke, and waiver text version.</td></tr>
                <tr><td><strong>PCI-DSS 4.0</strong></td><td>In-person and online tour bookings</td><td>P2PE encrypted card readers; zero PAN stored on mobile tablets or local servers.</td></tr>
                <tr><td><strong>COPPA & Minor Consent</strong></td><td>Children participating in youth tours</td><td>Parent/guardian verification workflows for participants under 18 years old.</td></tr>
                <tr><td><strong>EU GDPR / CCPA</strong></td><td>International tourists booking experiences</td><td>Consent capture for photo/video marketing; automated Right to be Forgotten.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Electronic signatures must comply with ESIGN and UETA. Capturing the IP address, timestamp, and exact waiver version signed is critical for legal enforceability."
    },
    {
        "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
        "title": "Tour Architectural Trade-offs & Decisions",
        "subtitle": "Strategic architectural compromises between SaaS ResTech, custom development, offline resilience, and OTA reliance",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header">All-in-One ResTech vs Headless</div>
            <p><strong>Trade-off:</strong> Turnkey all-in-one ResTech (FareHarbor/Bokun) vs composable headless booking engine.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-green">Choice: API-First Hybrid</span></p>
              <p>Leverage FareHarbor/Bokun for core inventory and OTA connectivity; build headless custom web/mobile front-ends for branded direct checkout.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Cloud-First vs Offline-First</div>
            <p><strong>Trade-off:</strong> Cloud-native real-time sync vs local SQLite offline-first mobile check-in.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-blue">Choice: Offline-First Edge</span></p>
              <p>Mobile guide apps must function 100% offline with local manifest storage, using CRDTs to merge check-in events when connectivity resumes.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">OTA Embrace vs Disintermediation</div>
            <p><strong>Trade-off:</strong> Maximizing OTA reach vs fighting for pure direct bookings.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-purple">Choice: Trojan Horse Capture</span></p>
              <p>Use OTAs as top-of-funnel customer acquisition; capture real traveler identity at check-in via waivers; convert to direct lifetime customers.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "The 'Trojan Horse' strategy is the smartest commercial play: let OTAs spend marketing dollars to acquire the customer, then capture their direct identity via the check-in waiver."
    },

    # PART 3: IT STANDARDS & GOVERNANCE (11-15)
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "Enterprise Architecture Framework: TOGAF & C4",
        "subtitle": "Structuring dual-realm experience architecture across Central Cloud Platforms and Field Mobile Terminals",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">C4 Model Architecture in Experiences</div>
            <div class="flow-step"><div class="step-num">C1</div><div><strong>System Context:</strong> Travelers, Guides, Dispatchers, and OTAs interacting with booking systems, field mobile apps, and fleet telematics.</div></div>
            <div class="flow-step"><div class="step-num">C2</div><div><strong>Containers:</strong> Enterprise Cloud (Salesforce / AWS / Snowflake), ResTech Core (Bokun / FareHarbor), Field Guide Apps (React Native / iOS), and Vehicle Gateways (Samsara).</div></div>
            <div class="flow-step"><div class="step-num">C3</div><div><strong>Components:</strong> OCTO Connector, Digital Waiver Vault, Manifest Reconciler, Dynamic Pricing Engine, Agentforce Weather Rebooker.</div></div>
            <div class="flow-step"><div class="step-num">C4</div><div><strong>Code:</strong> TypeScript microservices, OpenAPI schemas, SQLite local storage handlers, and Apex/Python AI agent tools.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">TOGAF Architecture Domains</div>
            <table class="data-table">
              <thead><tr><th>TOGAF Domain</th><th>Experience Sector Focus</th></tr></thead>
              <tbody>
                <tr><td><strong>Business Architecture</strong></td><td>End-to-end experience lifecycle: In-destination discovery, instant OTA booking, digital waiver, departure execution, post-tour photo merchandising.</td></tr>
                <tr><td><strong>Data Architecture</strong></td><td>Canonical Traveler 360, resource capacity models, immutable waiver legal vault, and GPS telematics.</td></tr>
                <tr><td><strong>Application Architecture</strong></td><td>Event-driven, API-first architecture connecting ResTech engines to OTAs, field apps, and CRM.</td></tr>
                <tr><td><strong>Technology Architecture</strong></td><td>Serverless hyperscaler cloud, cellular IoT gateways, ruggedized field tablets, and high-speed turnstile barcode readers.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Applying TOGAF and C4 gives tour operators a clear structural blueprint connecting shoreside cloud engines to ruggedized field tablets."
    },
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "API Standards & The OCTO Specification",
        "subtitle": "The Open Connectivity for Tourism (OCTO) standard and modern integration protocols",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">The OCTO OpenAPI 3.0 Standard</div>
            <p>OCTO is the open-source API standard developed by the tours and activities industry to replace proprietary, brittle point-to-point connections with universal endpoints:</p>
            <div class="flow-step"><div class="step-num">1</div><div><code>GET /products</code>: Returns tour catalog, options, inclusions, meeting points, and operational restrictions.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><code>POST /availability</code>: Queries real-time departure slots, remaining capacity, and dynamic pricing tiers.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><code>POST /bookings</code>: Creates a provisional booking hold, commits customer details, and returns confirmed barcode/QR.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><code>POST /bookings/{id}/cancel</code>: Triggers real-time cancellation, capacity release, and refund calculation.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Protocol Integration Topology</div>
            <table class="data-table">
              <thead><tr><th>Source System</th><th>Native Protocol</th><th>Target Architecture</th><th>Payload Standard</th></tr></thead>
              <tbody>
                <tr><td>Viator / GetYourGuide</td><td>OCTO / Proprietary REST</td><td>API Gateway / MuleSoft</td><td>JSON (OCTO v1.2)</td></tr>
                <tr><td>FareHarbor / Bokun</td><td>ResTech Webhooks</td><td>AWS EventBridge / Kafka</td><td>JSON Webhook Events</td></tr>
                <tr><td>Samsara Fleet GPS</td><td>MQTT / Cellular Telematics</td><td>IoT Core / Kafka</td><td>Protocol Buffers / JSON</td></tr>
                <tr><td>Smartwaiver / Wherewolf</td><td>REST API / Webhooks</td><td>Salesforce Data Cloud</td><td>JSON + Signed PDF Base64</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "OCTO has revolutionized the industry by allowing an operator to connect to 50+ OTAs through a single standard API schema."
    },
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "Event-Driven Architecture & Messaging Topology",
        "subtitle": "Real-time event streaming across booking channels, field operations, and customer notifications",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Experience Domain Events</div>
            <table class="data-table">
              <thead><tr><th>Event Name</th><th>Trigger Source</th><th>Downstream Subscribers</th></tr></thead>
              <tbody>
                <tr><td><code>BookingConfirmed</code></td><td>ResTech / OTA API</td><td>Capacity Ledger, Guide Dispatch, Waiver SMS Engine</td></tr>
                <tr><td><code>WaiverSigned</code></td><td>Smartwaiver / Wherewolf</td><td>Manifest Reconciler, Data Cloud Identity Linker</td></tr>
                <tr><td><code>GuestCheckedIn</code></td><td>Guide Mobile App</td><td>Headcount Monitor, Turnstile Gate, No-Show Releaser</td></tr>
                <tr><td><code>WeatherAlertIssued</code></td><td>WeatherOps / NOAA API</td><td>Agentforce Rebooking Agent, Operations Dispatch</td></tr>
                <tr><td><code>TourDeparted</code></td><td>Samsara Fleet Geofence</td><td>Status Tracker, Return ETA Predictor, Emergency Console</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Event Mesh Architecture</div>
            <div class="mermaid">
            flowchart TD
              OTA["OTAs (Viator/GYG)"] -->|OCTO| Gate["API Gateway"]
              Web["Direct Web Booking"] --> Gate
              Gate --> EB["Cloud Event Mesh<br>(Kafka / EventBridge)"]
              EB --> Res["ResTech Inventory Ledger"]
              EB --> Waiver["SMS Waiver Dispatch"]
              EB --> Guide["Guide Handheld Sync"]
              EB --> DC["Salesforce Data Cloud"]
              Weather["WeatherOps Feed"] -->|Storm Alert| EB
              EB --> Agent["Agentforce Weather Rebooker"]
            </div>
          </div>
        </div>
        """,
        "notes": "Event-driven architecture ensures that when a weather alert triggers or a booking arrives, all downstream systems react instantly."
    },
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "Field Cybersecurity & Zero-Trust Architecture",
        "subtitle": "Securing mobile field handhelds, protecting waiver PII, and enforcing tokenized payments",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Field Mobile Device Security (MDM)</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Mobile Device Management (MDM):</strong> Apple Business Manager / Microsoft Intune enforces remote wipe, biometric passcode, and app whitelisting on all guide iPads and rugged Android handhelds.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Local Storage Encryption:</strong> Field SQLite databases encrypted using SQLCipher (AES-256) with encryption keys held in the device secure enclave (Keychain/Keystore).</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Cellular APN Isolation:</strong> Field devices connect via private cellular APNs directly to cloud VPCs, bypassing public internet exposure.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Waiver PII & Payment Security</div>
            <table class="data-table">
              <thead><tr><th>Data Domain</th><th>Threat / Vulnerability</th><th>Zero-Trust Mitigation</th></tr></thead>
              <tbody>
                <tr><td>Waiver Medical Disclosures</td><td>Guide browsing sensitive health data</td><td>Role-based access: guides see only emergency flags (e.g., "Asthma"); full medical data restricted.</td></tr>
                <tr><td>Field Credit Card Payments</td><td>Card skimmers on mobile readers</td><td>PCI-P2PE certified readers (Stripe BBPOS / Square); PAN never touches mobile OS.</td></tr>
                <tr><td>Minor Participant Data</td><td>Unauthorized exposure of children's photos</td><td>Automated blurring of minor faces on public marketing feeds; private family-only photo galleries.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Guide tablets carry medical disclosures and minor data. Enforcing SQLCipher and role-based field views prevents catastrophic privacy breaches."
    },
    {
        "part": "PART 3: IT STANDARDS & GOVERNANCE",
        "title": "Experience Data Governance & Master Data Management",
        "subtitle": "Architecting the Unified Traveler 360 and managing local operator/guide master data",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Master Data Entities in Experiences</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Traveler Master Data:</strong> Reconciling disparate bookings across OTAs, direct web, and concierge desks into a single Golden Traveler Profile.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Product & Resource Catalog:</strong> Canonical definitions of tours, departure slots, pickup locations, vehicles, and certified guides across all booking channels.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Waiver Legal Vault:</strong> Immutable 7-year retention of digitally signed waivers, emergency contacts, and medical acknowledgments.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Data Quality & De-anonymization Rules</div>
            <table class="data-table">
              <thead><tr><th>Source</th><th>Raw Input</th><th>Cleansed Master Output</th></tr></thead>
              <tbody>
                <tr><td>Viator Booking</td><td><code>John D., 12a3@guest.viator.com</code></td><td>Anonymous booking record</td></tr>
                <tr><td>Check-in Waiver</td><td><code>John Doe, john.doe@gmail.com, +1-555-0192</code></td><td>Matched & De-anonymized Golden Record</td></tr>
                <tr><td>Hotel Pickup</td><td><code>"hyatt near beach"</code></td><td>Harmonized to <code>Hyatt Regency Maui (Stop #4)</code></td></tr>
                <tr><td>Medical Flag</td><td><code>"allergic to peanuts and bees"</code></td><td>Structured flags: <code>[DIETARY_PEANUT, MEDICAL_EPIPEN]</code></td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "De-anonymizing OTA guests through check-in waivers is the holy grail of tour operator MDM. It turns a one-time transaction into a direct customer relationship."
    },

    # PART 4: 13-LAYER ARCHITECTURE & 3 VARIATIONS (16-20)
    {
        "part": "PART 4: 13-LAYER ARCHITECTURE",
        "title": "13-Layer Master Architecture Blueprint",
        "subtitle": "The definitive enterprise technology taxonomy powering modern tour and experience operators",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">The 13 Enterprise Architecture Layers</div>
            <div style="font-size: 0.85rem; line-height: 1.6;">
              <p><strong>1. ResTech & Core Ops:</strong> Bokun, FareHarbor, Peek Pro, resource capacity</p>
              <p><strong>2. Contact Center:</strong> Service Cloud Voice / Zendesk Talk, SMS support</p>
              <p><strong>3. CRM & Partner Portals:</strong> Sales Cloud, Hotel Concierge B2B Extranets</p>
              <p><strong>4. Loyalty & Memberships:</strong> Annual passes, repeat discount engine</p>
              <p><strong>5. CDP & Identity:</strong> Salesforce Data Cloud / Segment / Adobe AEP</p>
              <p><strong>6. API & Channel Manager:</strong> OCTO OpenAPI 3.0, Rezdy Marketplace, MuleSoft</p>
              <p><strong>7. Cloud & Edge Infra:</strong> Serverless AWS/GCP + Offline SQLite Mobile Handhelds</p>
              <p><strong>8. Fleet Telematics & GPS:</strong> Samsara AI Telematics, Garmin inReach SOS</p>
              <p><strong>9. Safety & Digital Waivers:</strong> Smartwaiver, Wherewolf, ESIGN compliant vault</p>
              <p><strong>10. Digital App & Turnstiles:</strong> Guest mobile web, guide app, Axess/Skidata gates</p>
              <p><strong>11. Marketing Automation:</strong> Marketing Cloud / Braze, automated photo delivery</p>
              <p><strong>12. Finance & Merchant ERP:</strong> Stripe / Adyen, QuickBooks / SAP S/4HANA</p>
              <p><strong>13. AI & Automation:</strong> Agentforce weather rebooking, Palantir dispatch</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Architectural Cohesion & Handoffs</div>
            <div class="flow-step"><div class="step-num">⚡</div><div><strong>Real-Time Distribution:</strong> Layers 1, 6, and 10 maintain instant sub-second inventory sync across 50+ global OTAs to maximize yield and prevent overbooking.</div></div>
            <div class="flow-step"><div class="step-num">🌲</div><div><strong>Field Independence:</strong> Layers 7, 8, 9, and 10 ensure guides and shuttle drivers operate flawlessly in remote wilderness without cellular signal.</div></div>
            <div class="flow-step"><div class="step-num">🎯</div><div><strong>Revenue Recapture:</strong> Layers 3, 5, 11, and 13 de-anonymize OTA guests and convert them into high-margin direct lifetime travelers.</div></div>
          </div>
        </div>
        """,
        "notes": "Here is the complete 13-layer taxonomy for tours and experiences. Every layer is purpose-built to solve the unique challenges of experiential travel."
    },
    {
        "part": "PART 4: 13-LAYER ARCHITECTURE",
        "title": "Variation 1: The Salesforce-Centric Ecosystem",
        "subtitle": "Unified experiential travel architecture anchored on Salesforce Data Cloud, Agentforce, and MuleSoft",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Stack Specification</div>
            <table class="data-table">
              <thead><tr><th>Layer</th><th>Selected Platform</th><th>Deployment Mode</th></tr></thead>
              <tbody>
                <tr><td>CRM & Partner Portals</td><td>Salesforce Sales Cloud + Experience Cloud</td><td>Enterprise Cloud SaaS</td></tr>
                <tr><td>CDP & Guest 360</td><td>Salesforce Data Cloud</td><td>Hyperscale Zero-Copy Lakehouse</td></tr>
                <tr><td>Integration Fabric</td><td>MuleSoft Anypoint + OCTO Connectors</td><td>Cloud API Gateway + Edge Microservices</td></tr>
                <tr><td>AI Concierge & Rebooker</td><td>Salesforce Agentforce</td><td>Autonomous reasoning over weather/schedules</td></tr>
                <tr><td>Marketing Automation</td><td>Salesforce Marketing Cloud (SFMC)</td><td>Journey Builder, SMS & WhatsApp push</td></tr>
                <tr><td>ResTech & Booking Core</td><td>Bokun / FareHarbor + Smartwaiver</td><td>SaaS ResTech + Digital Waiver Vault</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic & Commercial Evaluation</div>
            <div class="flow-step"><div class="step-num">✓</div><div><strong>Instant Guest De-anonymization:</strong> Data Cloud ingests waiver data in real time, merging anonymous OTA bookings into rich Traveler 360 profiles.</div></div>
            <div class="flow-step"><div class="step-num">✓</div><div><strong>Autonomous Weather Rebooking:</strong> Agentforce monitors NOAA feeds and automatically messages affected guests with 1-click rebooking or credit options.</div></div>
            <div class="flow-step"><div class="step-num">⚠️</div><div><strong>Mobile Offline Extension:</strong> Requires a custom React Native / Swift wrapper with SQLite for offline guide field check-in.</div></div>
            <div style="margin-top: 1rem;">
              <span class="pill pill-blue">ACV: $5.5M - $9.5M / yr</span>
              <span class="pill pill-green">3-Year ROI: 350%</span>
            </div>
          </div>
        </div>
        """,
        "notes": "Variation 1 delivers unparalleled commercial agility: turning anonymous OTA passengers into direct marketing assets within minutes of signing a waiver."
    },
    {
        "part": "PART 4: 13-LAYER ARCHITECTURE",
        "title": "Variation 2: Without Salesforce (Open Modern)",
        "subtitle": "Decoupled, modern cloud architecture utilizing Snowflake, Braze, Zendesk, and Kafka",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Stack Specification</div>
            <table class="data-table">
              <thead><tr><th>Layer</th><th>Selected Platform</th><th>Deployment Mode</th></tr></thead>
              <tbody>
                <tr><td>Lakehouse / Storage</td><td>Snowflake / Databricks</td><td>Multi-cloud Lakehouse Architecture</td></tr>
                <tr><td>CDP & Streaming</td><td>Twilio Segment / mParticle</td><td>Real-time clickstream & event routing</td></tr>
                <tr><td>CRM & Contact Center</td><td>Zendesk Suite / Microsoft Dynamics 365</td><td>Omnichannel Support + SMS Ticketing</td></tr>
                <tr><td>Marketing Engine</td><td>Braze</td><td>Mobile-first real-time streaming campaigns</td></tr>
                <tr><td>Event Mesh</td><td>Confluent Apache Kafka / AWS EventBridge</td><td>Managed Cloud Event Mesh</td></tr>
                <tr><td>ResTech & Booking Core</td><td>Bokun / FareHarbor + Wherewolf</td><td>SaaS ResTech + Digital Waiver Vault</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic & Commercial Evaluation</div>
            <div class="flow-step"><div class="step-num">✓</div><div><strong>Zero Vendor Lock-in:</strong> Open standards allow independent replacement of any layer without enterprise platform penalties.</div></div>
            <div class="flow-step"><div class="step-num">✓</div><div><strong>Mobile Messaging Power:</strong> Braze excels at in-destination push notifications, geolocation-triggered messaging, and SMS delivery.</div></div>
            <div class="flow-step"><div class="step-num">⚠️</div><div><strong>Integration Overhead:</strong> Requires custom engineering to build and maintain data pipelines between ResTech, waivers, and the data lake.</div></div>
            <div style="margin-top: 1rem;">
              <span class="pill pill-green">ACV: $4.5M - $7.8M / yr</span>
              <span class="pill pill-blue">3-Year ROI: 270%</span>
            </div>
          </div>
        </div>
        """,
        "notes": "Variation 2 is the preferred architecture for engineering-driven experiential brands that want full control over their code and customer journey logic."
    },
    {
        "part": "PART 4: 13-LAYER ARCHITECTURE",
        "title": "Variation 3: The Best Platforms Money Can Buy",
        "subtitle": "Sovereign-grade global operator architecture: Palantir Foundry, Adobe Experience Cloud, and Samsara AI",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Stack Specification</div>
            <table class="data-table">
              <thead><tr><th>Layer</th><th>Selected Platform</th><th>Deployment Mode</th></tr></thead>
              <tbody>
                <tr><td>Kinetic Fleet & Guide Twin</td><td>Palantir Foundry & AIP</td><td>Sovereign multi-cloud + Edge AIP runtimes</td></tr>
                <tr><td>Fleet Telematics & Safety</td><td>Samsara AI Fleet Dashcams & GPS</td><td>Cellular IoT gateways + AI dashcams</td></tr>
                <tr><td>Digital Experience & CDP</td><td>Adobe Experience Cloud (AEP + AJO + AEM)</td><td>Sub-50ms streaming edge personalization</td></tr>
                <tr><td>Contact Center</td><td>Genesys Cloud CX + Google CCAI</td><td>AI-orchestrated global contact center</td></tr>
                <tr><td>Turnstiles & Access Control</td><td>Skidata / Axess Smart Gates</td><td>Hardware turnstiles with RFID / barcode</td></tr>
                <tr><td>ResTech & Booking Core</td><td>Custom Headless Engine on AWS + Smartwaiver</td><td>High-throughput bespoke microservices</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic & Commercial Evaluation</div>
            <div class="flow-step"><div class="step-num">★</div><div><strong>Kinetic Fleet Optimization:</strong> Palantir Foundry models guide certifications, vehicle maintenance, live GPS traffic, and weather to optimize daily dispatch for 500+ vehicles.</div></div>
            <div class="flow-step"><div class="step-num">★</div><div><strong>Carrier-Grade Turnstile Speed:</strong> Skidata/Axess gates process 12,000 visitors per hour with sub-100ms barcode validation at premier attractions.</div></div>
            <div style="margin-top: 1rem;">
              <span class="pill pill-purple">ACV: $16.5M - $28M / yr</span>
              <span class="pill pill-green">3-Year ROI: 460%</span>
            </div>
          </div>
        </div>
        """,
        "notes": "Variation 3 represents the pinnacle of experiential technology, utilized by massive global attraction operators, ski resorts, and national tour conglomerates."
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
              <tr><td>1. ResTech Core</td><td>Bokun / FareHarbor</td><td>Bokun / FareHarbor / Xola</td><td>Custom Headless Engine on AWS</td></tr>
              <tr><td>2. Contact Center</td><td>Service Cloud Voice + Amazon Connect</td><td>Zendesk Talk / Twilio Flex</td><td>Genesys Cloud CX + Google CCAI</td></tr>
              <tr><td>3. CRM / Partner</td><td>Salesforce Sales Cloud + Experience Cloud</td><td>Microsoft Dynamics 365 + Web Portal</td><td>Salesforce Unlimited + Custom Portal</td></tr>
              <tr><td>4. Loyalty</td><td>Salesforce Loyalty Management</td><td>Talon.One / SessionM</td><td>Kobie / Custom Sovereign Engine</td></tr>
              <tr><td>5. CDP / Data</td><td>Salesforce Data Cloud (Zero-Copy)</td><td>Snowflake + Twilio Segment</td><td>Adobe Experience Platform (AEP)</td></tr>
              <tr><td>6. Integration</td><td>MuleSoft Anypoint + OCTO Connectors</td><td>Kong Gateway + Apache Kafka</td><td>Confluent Kafka + Apigee + MuleSoft</td></tr>
              <tr><td>7. Infra / Edge</td><td>AWS Serverless + Offline Mobile SQLite</td><td>GCP / AWS + Offline React Native</td><td>AWS Dedicated + Rugged Field Edge</td></tr>
              <tr><td>8. Fleet Telematics</td><td>Samsara Telematics Connector</td><td>Geotab / Verizon Connect</td><td>Samsara AI Dashcams + Dual GPS</td></tr>
              <tr><td>9. Digital Waivers</td><td>Smartwaiver + MuleSoft Sync</td><td>Wherewolf + Webhook Sync</td><td>Smartwaiver Enterprise + Legal Vault</td></tr>
              <tr><td>10. Digital App</td><td>Salesforce Mobile SDK / React Native</td><td>Native Swift/Kotlin + Next.js</td><td>Adobe AEM + Native Apps + Skidata</td></tr>
              <tr><td>11. Marketing</td><td>Marketing Cloud (SFMC) + Einstein</td><td>Braze + Customer.io</td><td>Adobe Journey Optimizer (AJO)</td></tr>
              <tr><td>12. Finance / ERP</td><td>Stripe Terminal + QuickBooks / SAP</td><td>Stripe / Adyen + Dynamics 365</td><td>Adyen + SAP S/4HANA Dedicated</td></tr>
              <tr><td>13. AI & Automation</td><td>Salesforce Agentforce Weather Rebooker</td><td>Custom LLM on Databricks / Bedrock</td><td>Palantir AIP + OpenAI Enterprise Tier</td></tr>
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
        "subtitle": "Organizing experience platforms into Systems of Record, Intelligence, Engagement, and Action",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">The Four Spheres Taxonomy</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Systems of Record (SoR):</strong> Immutable source of truth for transactions and legal records. ResTech Booking Engine (Bokun/FareHarbor), Smartwaiver Legal Vault, SAP / QuickBooks General Ledger.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Systems of Intelligence (SoI):</strong> Data ingestion, identity resolution, machine learning. Salesforce Data Cloud, Snowflake, Databricks, and Palantir Foundry.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Systems of Engagement (SoE):</strong> Omnichannel customer and partner touchpoints. Service Cloud Voice, Marketing Cloud, Mobile Guest Web, Hotel Concierge Portal.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Systems of Action (SoA):</strong> Operational field execution. Guide Mobile Check-in Handhelds, Skidata/Axess Turnstiles, Samsara Fleet Dispatch, Stripe Terminal.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Architectural Interlock Dynamics</div>
            <div class="mermaid">
            flowchart TD
              SoI["Systems of Intelligence<br>(Data Cloud / Snowflake)"] -->|Audiences & AI Context| SoE["Systems of Engagement<br>(Marketing Cloud / Agentforce)"]
              SoE -->|Direct Bookings & Requests| SoR["Systems of Record<br>(ResTech / Waivers / ERP)"]
              SoR -->|Manifests & Capacity| SoA["Systems of Action<br>(Guide Handhelds / Turnstiles / Fleet)"]
              SoA -->|Check-in Events & Telematics| SoI
            </div>
          </div>
        </div>
        """,
        "notes": "Understanding how the four spheres interact prevents architectural overlap and ensures clean separation of concerns."
    },
    {
        "part": "PART 5: TOOL COMPLEMENTARITY",
        "title": "Core System Handoffs: OTA Booking to Manifest",
        "subtitle": "Sequence diagram from initial Viator/GYG booking through OCTO API to guide mobile manifest",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">OTA Booking to Field Manifest Sequence</div>
          <div class="mermaid">
          sequenceDiagram
            autonumber
            actor Traveler as Traveler (on Viator)
            participant OTA as Viator / GetYourGuide
            participant OCTO as OCTO API Gateway
            participant Res as ResTech (Bokun / FareHarbor)
            participant Mule as MuleSoft Integration
            participant SF as Salesforce Data Cloud
            participant SMS as Twilio / SFMC SMS
            participant Guide as Guide Mobile Handheld

            Traveler->>OTA: Book 2 Seats on Whale Watch Tour
            OTA->>OCTO: POST /bookings (OCTO Standard JSON)
            OCTO->>Res: Decrement Departure Capacity (Seats: 18 -> 16)
            Res-->>OCTO: Return Confirmed Booking ID & Barcode
            OCTO-->>OTA: Return Booking Confirmation to Traveler
            Res->>Mule: Publish BookingCreated Event
            Mule->>SF: Create Participant & Booking Record
            Mule->>Guide: Push Updated Manifest to Local SQLite
            SF->>SMS: Trigger Pre-Tour SMS with Smartwaiver Link
            SMS-->>Traveler: "Please sign your waiver before arrival"
          </div>
        </div>
        """,
        "notes": "Notice how the booking decrements capacity across all channels via OCTO and instantly pushes the updated manifest to the guide's tablet."
    },
    {
        "part": "PART 5: TOOL COMPLEMENTARITY",
        "title": "Digital Waiver & Guest Check-In Sequence",
        "subtitle": "Sequence diagram of pre-tour mobile waiver signing, QR turnstile check-in, and equipment allocation",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">Digital Waiver Signing and Field Check-in Flow</div>
          <div class="mermaid">
          sequenceDiagram
            autonumber
            actor Guest as Tour Participant
            participant Phone as Guest Mobile Phone
            participant Waiver as Smartwaiver / Wherewolf
            participant DC as Salesforce Data Cloud
            participant Guide as Guide Mobile App
            participant Gear as Equipment Inventory Service

            Guest->>Phone: Open Waiver Link from SMS
            Phone->>Waiver: Sign Liability Waiver & Enter Medical Info
            Waiver->>DC: Ingest Real Email, Phone, Emergency Contact
            DC->>DC: De-anonymize OTA Booking & Update Golden Record
            Waiver->>Guide: Update Manifest: "Waiver Verified (Green)"
            Guest->>Guide: Arrive at Departure Pier & Present QR Code
            Guide->>Guide: Scan QR Code with Mobile Camera
            Guide->>Gear: Request Equipment: Wetsuit Size L, Fins Size 10
            Gear-->>Guide: Confirm Gear Bin #14 Allocated
            Guide-->>Guest: Hand over Gear & Welcome Aboard
          </div>
        </div>
        """,
        "notes": "This sequence shows the magic moment: the traveler signs the waiver, the OTA booking is instantly de-anonymized, and the guide's tablet turns green."
    },
    {
        "part": "PART 5: TOOL COMPLEMENTARITY",
        "title": "Dynamic Weather Disruption & Autonomous Rebooking",
        "subtitle": "Sequence diagram of severe weather detection, automated cancellation, and Agentforce rebooking",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">Autonomous Weather Disruption and Rebooking Sequence</div>
          <div class="mermaid">
          sequenceDiagram
            autonumber
            participant Weather as WeatherOps / NOAA Feed
            participant Agent as Agentforce Rebooking Agent
            participant Res as ResTech Booking Core
            participant Comms as SFMC WhatsApp / SMS Engine
            actor Guest as Affected Traveler
            participant Mule as MuleSoft / Stripe

            Weather->>Agent: Storm Alert: 35-knot winds at 14:00 (Gale Warning)
            Agent->>Res: Identify 4 Affected Afternoon Catamaran Sailings (120 Guests)
            Agent->>Res: Flag Sailings as "Weather Cancelled" & Lock Inventory
            Agent->>Agent: Generate Alternative Options: Tomorrow 09:00 OR Full Refund
            Agent->>Comms: Dispatch Personalized WhatsApp Message with 1-Click Buttons
            Comms->>Guest: "Due to high winds, tour cancelled. Tap 1 to rebook tomorrow, Tap 2 for refund"
            Guest->>Comms: Tap "Rebook Tomorrow 09:00"
            Comms->>Agent: Ingest Guest Selection
            Agent->>Res: Book 2 Seats on Tomorrow 09:00 Departure
            Agent->>Mule: Re-issue Digital Tickets & Update Waiver Link
            Agent-->>Guest: "Confirmed! Your new tickets are ready."
          </div>
        </div>
        """,
        "notes": "Agentforce handles what used to take 4 staff members 3 hours of frantic phone calls in less than 90 seconds autonomously."
    },
    {
        "part": "PART 5: TOOL COMPLEMENTARITY",
        "title": "Tour Integration Friction Points & Mitigation",
        "subtitle": "Overcoming operational friction across OTA overbooking, waiver matching, and no-shows",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header">OTA Overbooking Collisions</div>
            <p><strong>Problem:</strong> Viator and GetYourGuide sell the final seats simultaneously during a high-traffic surge.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-green">Mitigation</span></p>
              <p>Distributed Redis Capacity Locks: 10-second atomic hold placed during checkout; capacity buffer of 2 "safety seats" held back from OTAs until 2 hours before departure.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Waiver Name Mismatch</div>
            <p><strong>Problem:</strong> Booking under "Bob Smith", but waiver signed under legal name "Robert J. Smith", failing automated match.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-blue">Mitigation</span></p>
              <p>Fuzzy Matching + Phone Hash: Jaro-Winkler string distance (>0.82) combined with exact match on mobile phone number or booking reference code in waiver URL.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Last-Minute No-Shows</div>
            <p><strong>Problem:</strong> 8-12% no-show rate leaves expensive tour seats empty while walk-up guests are turned away.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-purple">Mitigation</span></p>
              <p>Automated Standby Release: 15 minutes before departure, unchecked-in seats automatically released to standby queue via guide mobile app.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Safety buffers and automated standby release protect the operator's yield and prevent embarrassing overbooking situations at the pier."
    },

    # PART 6: DATA INGESTION, MODELING & LAKEHOUSE (26-30)
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Experience Data Ingestion Architecture",
        "subtitle": "Handling four distinct ingestion modalities: OTA webhooks, telematics, waivers, and turnstiles",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Four Ingestion Modalities</div>
            <table class="data-table">
              <thead><tr><th>Modality</th><th>Data Sources</th><th>Protocol / Engine</th><th>Frequency</th></tr></thead>
              <tbody>
                <tr><td><strong>OTA Webhooks</strong></td><td>Viator, GetYourGuide, Klook, Direct Web</td><td>HTTPS / OCTO OpenAPI 3.0</td><td>Sub-second real-time</td></tr>
                <tr><td><strong>Digital Waivers</strong></td><td>Smartwaiver, Wherewolf, Formstack</td><td>Webhook / REST API</td><td>Event-driven (on sign)</td></tr>
                <tr><td><strong>Fleet Telematics</strong></td><td>Samsara GPS, vehicle speed, engine diagnostics</td><td>Cellular MQTT / Kafka</td><td>1 - 5 seconds</td></tr>
                <tr><td><strong>Turnstiles & POS</strong></td><td>Skidata barcode scans, Stripe card taps</td><td>Edge WebSocket / TCP Sockets</td><td>&lt;100ms sub-second</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Cloud Ingestion Pipeline</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>API Gateway Tier:</strong> Cloudflare Workers / AWS API Gateway terminates incoming webhooks from 50+ OTAs, enforcing HMAC signature verification.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Stream Buffering:</strong> Events stream into Apache Kafka / AWS Kinesis to absorb sudden booking spikes without overloading downstream databases.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Lakehouse Landing:</strong> Raw JSON events land in Object Storage (S3 / GCS) formatted into Apache Iceberg / Delta Lake tables.</div></div>
          </div>
        </div>
        """,
        "notes": "HMAC signature verification at the gateway is critical to prevent fraudulent webhook injections from fake OTA endpoints."
    },
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Canonical Experience Data Model & Entities",
        "subtitle": "Standardized entity-relationship model covering participant, booking, departure slot, guide, and waiver",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Experience Entities</div>
            <table class="data-table">
              <thead><tr><th>Entity</th><th>Key Attributes</th><th>Relationships</th></tr></thead>
              <tbody>
                <tr><td><strong>Participant</strong></td><td>ParticipantID, FullName, Email, MobilePhone, DOB, DietaryFlags</td><td>1:M Bookings, 1:M Waivers</td></tr>
                <tr><td><strong>ExperienceBooking</strong></td><td>BookingID, PNR, ChannelID (Viator/Direct), TourProductID, SlotID</td><td>M:1 Participant, 1:M Tickets</td></tr>
                <tr><td><strong>DepartureSlot</strong></td><td>SlotID, TourProductID, StartTime, MaxCapacity, AvailableSeats</td><td>1:M Bookings, M:1 Guide</td></tr>
                <tr><td><strong>DigitalWaiver</strong></td><td>WaiverID, BookingID, ParticipantID, SignedPDF_URI, IPAddress</td><td>1:1 Participant per Tour</td></tr>
                <tr><td><strong>GuideResource</strong></td><td>GuideID, FullName, Certifications (WFR/CPR), Languages, ShiftState</td><td>1:M DepartureSlots</td></tr>
                <tr><td><strong>VehicleAsset</strong></td><td>VehicleID, PlateNo, Capacity, ELD_Status, FuelLevel, TelematicsID</td><td>1:M DepartureSlots</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Data Model Design Principles</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Slot-Scoped vs Lifetime-Scoped:</strong> Departure slots, manifests, and waivers are slot-scoped. Traveler profiles, lifetime booking history, and review sentiment are enterprise-scoped.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Resource Capacity Constraints:</strong> Departure capacity is calculated dynamically as <code>MIN(VehicleCapacity, GuideRatioCapacity, PermitQuota)</code>.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Immutable Legal Vault:</strong> Signed waiver PDFs and audit metadata are write-once-read-many (WORM) compliant and cannot be modified.</div></div>
          </div>
        </div>
        """,
        "notes": "Notice how capacity is constrained by the minimum of vehicle seats, legal guide ratios, and park permit quotas. You can't just sell seats if you don't have guides."
    },
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Identity Resolution & Unified Profile Engine",
        "subtitle": "De-anonymizing OTA travelers and unifying booking records across disparate travel channels",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">The De-Anonymization Engine</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Anonymous Booking Ingestion:</strong> Traveler books on Viator. ResTech receives <code>name="J. Smith"</code>, <code>email="v-9842@guest.viator.com"</code>. Identity status: <em>Anonymous</em>.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Pre-Tour Waiver Capture:</strong> Guest clicks SMS link and completes digital waiver on phone, providing real name "Johnathan Smith", personal email "jsmith@gmail.com", and phone number.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Deterministic Linkage:</strong> Identity engine matches the unique booking reference token embedded in the waiver URL, linking the real customer to the OTA booking.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Golden Record Creation:</strong> Golden Party ID created in Data Cloud; triggers automated welcome SMS with hotel pickup directions.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Identity Resolution Flowchart</div>
            <div class="mermaid">
            flowchart TD
              OTA["Viator / GYG Booking<br>(Opaque Guest Email)"] --> Matcher["Identity Resolution Engine<br>(Data Cloud / Segment)"]
              Waiver["Digital Waiver Submission<br>(Real Email & Mobile Phone)"] --> Matcher
              Web["Direct Web Booking<br>(Real Email & Phone)"] --> Matcher
              Matcher --> Token{"Waiver Token Match?"}
              Token -->|Yes| Link["Link Real Identity to OTA PNR"]
              Token -->|No| Fuzzy{"Phone / Name Fuzzy Match?"}
              Fuzzy -->|Yes| Link
              Fuzzy -->|No| New["Create New Participant Profile"]
              Link --> Golden["Golden Traveler 360 Profile"]
              Golden --> SFMC["Marketing Cloud / Braze Direct Campaigns"]
            </div>
          </div>
        </div>
        """,
        "notes": "This identity resolution architecture is the engine of direct booking growth: capturing 85%+ of anonymous OTA travelers' real contact info."
    },
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Medallion Lakehouse Architecture for Experiences",
        "subtitle": "Transforming raw field telematics, booking webhooks, and waivers into high-value data products",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-amber">Bronze Layer</span><br>Raw & Streaming Ingestion</div>
            <div style="font-size: 0.85rem; margin-top: 0.8rem;">
              <p><strong>Sources:</strong> Raw OCTO booking webhooks, Samsara GPS pings, Smartwaiver JSON, Stripe payment events.</p>
              <p><strong>Format:</strong> Raw JSON / Parquet stored in S3/GCS.</p>
              <p><strong>Retention:</strong> 7 years immutable audit trail.</p>
              <p><strong>Characteristics:</strong> Append-only, unvalidated raw payloads.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-blue">Silver Layer</span><br>Cleansed & Conformed</div>
            <div style="font-size: 0.85rem; margin-top: 0.8rem;">
              <p><strong>Transformations:</strong> Currency conversion, timezone normalization to local tour time, PII masking, deduplication.</p>
              <p><strong>Tables:</strong> ConformedBookings, ValidatedManifests, CleanedTelematics, VerifiedWaivers.</p>
              <p><strong>Engine:</strong> dbt / Databricks Delta Lake / Snowflake.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header"><span class="pill pill-purple">Gold Layer</span><br>Curated Data Products</div>
            <div style="font-size: 0.85rem; margin-top: 0.8rem;">
              <p><strong>Business Products:</strong></p>
              <p>• <strong>Traveler Lifetime Value (LTV):</strong> Multi-destination rebooking score.</p>
              <p>• <strong>Departure Yield Matrix:</strong> Revenue per seat mile.</p>
              <p>• <strong>Guide Performance Score:</strong> NPS vs incident rate.</p>
              <p>• <strong>Fleet Utilization Twin:</strong> Operating cost per passenger.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "The Medallion architecture turns disparate operational feeds into polished data products for commercial and operational leaders."
    },
    {
        "part": "PART 6: DATA & LAKEHOUSE",
        "title": "Data Governance, Lineage & Legal Archival",
        "subtitle": "Ensuring regulatory compliance, legal waiver enforceability, and privacy automation",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Legal Waiver Retention & Defensibility</div>
            <div class="flow-step"><div class="step-num">⚖️</div><div><strong>7-Year Statute of Limitations:</strong> Personal injury lawsuits can be filed years after an incident. Signed digital waivers and audit logs must be preserved in immutable WORM cloud storage (Amazon S3 Object Lock).</div></div>
            <div class="flow-step"><div class="step-num">📄</div><div><strong>Cryptographic Integrity:</strong> SHA-256 hash of signed waiver PDF stored in database. Any tampering with document content invalidates hash, proving authentic evidence in court.</div></div>
            <div class="flow-step"><div class="step-num">🔒</div><div><strong>GDPR Carve-out for Legal Defense:</strong> Right to be Forgotten requests automated in OneTrust, but waiver legal records retained under GDPR Article 17(3)(e) (defense of legal claims).</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Data Lineage & Compliance Matrix</div>
            <table class="data-table">
              <thead><tr><th>Data Asset</th><th>Lineage Tracking</th><th>Compliance Target</th></tr></thead>
              <tbody>
                <tr><td>Digital Liability Waiver</td><td>Smartwaiver -> S3 WORM Vault -> Salesforce</td><td>ESIGN / UETA / Tort Law Defense</td></tr>
                <tr><td>Driver Hours of Service</td><td>Samsara ELD -> DOT Webhook -> Fleet Core</td><td>FMCSA 49 CFR Part 395</td></tr>
                <tr><td>Customer Payment Token</td><td>Stripe Terminal -> Token Vault -> ERP GL</td><td>PCI-DSS 4.0 Level 1</td></tr>
                <tr><td>Guest Marketing Consent</td><td>Check-in Checkbox -> OneTrust -> SFMC / Braze</td><td>EU GDPR / CCPA / CAN-SPAM</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Remember GDPR Article 17(3)(e): a customer can demand you delete their marketing profile, but you legally retain their signed waiver for liability defense."
    },

    # PART 7: END-TO-END CUSTOMER JOURNEYS (31-36)
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 1: In-Destination Inspiration & Search",
        "subtitle": "The experience journey begins: mobile search, OTA meta-ranking, and dynamic local discovery",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Traveler Discovery & Search Behavior</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>In-Market Mobile Search:</strong> Tourist arrives in Honolulu, searches Google for "best snorkeling tour near Waikiki" on their iPhone.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Google Things to Do & OTA Ads:</strong> Google Things to Do module displays direct booking links alongside Viator and GetYourGuide listings with real-time pricing.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Dynamic Social Re-targeting:</strong> Instagram ad displays user-generated video of sea turtle snorkeling, deep-linking directly into mobile checkout.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Search Architecture & Ranking Factors</div>
            <div class="mermaid">
            flowchart TD
              Traveler["Mobile Traveler Search"] --> Google["Google Things to Do / OTAs"]
              Google --> Cache["CDN Edge Cache<br>(Cloudflare Workers)"]
              Cache --> Res["ResTech Inventory Engine<br>(Bokun / FareHarbor)"]
              Res --> RMS["Dynamic Pricing Engine"]
              RMS --> Cache
              Traveler --> Book["Mobile Checkout Page (<1.2s Load)"]
            </div>
            <div style="margin-top: 1rem; font-size: 0.85rem; color: var(--text-muted);">
              <p><strong>Speed is Conversion:</strong> Every 100ms decrease in mobile checkout page load time lifts in-destination booking conversion by 8.4%.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Google 'Things to Do' has been a massive disruption to traditional OTAs, allowing operators to place direct booking links directly on Google Search."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 2: Booking, Dynamic Add-ons & Sizing",
        "subtitle": "Frictionless checkout: instant slot confirmation, hotel pickup selection, and equipment sizing",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Checkout & Merchandising Flow</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Slot Selection & Seat Lock:</strong> Traveler selects tomorrow's 08:30 AM departure; 2 seats locked in Redis for 10 minutes.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Hotel Pickup Selector:</strong> Geocoded hotel dropdown matches traveler's hotel to designated shuttle pickup stop #3 with exact 07:45 AM pickup time.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Pre-Tour Sizing & Add-ons:</strong> Seamlessly captures wetsuit sizes (M, L), shoe sizes, and upsells "GoPro Rental + 64GB SD Card" for $45.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>1-Tap Apple Pay / Google Pay:</strong> Checkout completed in under 20 seconds with biometric authorization.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Ancillary Conversion & Yield Lift</div>
            <table class="data-table">
              <thead><tr><th>Add-on Product</th><th>Attach Rate</th><th>Price</th><th>Margin</th></tr></thead>
              <tbody>
                <tr><td>GoPro Camera Rental</td><td>18.5%</td><td>$45.00</td><td>88% gross margin</td></tr>
                <tr><td>Wetsuit / Gear Upgrade</td><td>34.0%</td><td>$15.00</td><td>92% gross margin</td></tr>
                <tr><td>Hotel Shuttle Pickup</td><td>42.0%</td><td>$20.00</td><td>65% gross margin</td></tr>
                <tr><td>Flexible Weather Insurance</td><td>29.0%</td><td>$12.00</td><td>85% gross margin</td></tr>
              </tbody>
            </table>
            <div style="margin-top: 1rem;">
              <span class="pill pill-green">+$38.50 Avg Ancillary Spend per Booking</span>
            </div>
          </div>
        </div>
        """,
        "notes": "Capturing wetsuit and shoe sizes during checkout eliminates 15 minutes of chaotic sizing arguments at the departure dock."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 3: Pre-Tour Preparation & Digital Waiver",
        "subtitle": "Automated readiness: SMS waiver links, medical disclosure, safety briefings, and packing lists",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Mobile Pre-Tour Preparation</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Automated SMS Dispatch:</strong> 24 hours prior to departure, automated SMS sends personalized waiver link and what-to-bring packing list.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Digital Waiver Completion:</strong> Traveler opens mobile-responsive waiver, signs with finger, adds minor children, and acknowledges safety rules.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Digital Boarding Pass:</strong> Boarding pass with dynamic QR code, shuttle pickup GPS map, and emergency contact phone saved to Apple / Google Wallet.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Real-Time Weather Reassurance:</strong> Automated push notification confirms: "Weather looks gorgeous for tomorrow's 08:30 AM sail! Waters are calm."</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Pre-Arrival Verification Architecture</div>
            <div class="mermaid">
            flowchart TD
              Booking["Booking Created"] --> SMS["Twilio / SFMC SMS Gateway"]
              SMS --> Link["Personalized Waiver URL"]
              Link --> Sign["Smartwaiver Mobile Signing"]
              Sign --> Vault["S3 WORM Legal Vault"]
              Sign --> DC["Data Cloud (De-anonymize)"]
              Sign --> Manifest["Guide Manifest Updated (Green)"]
              Manifest --> Wallet["Apple / Google Wallet Pass"]
            </div>
          </div>
        </div>
        """,
        "notes": "Achieving an 85%+ pre-arrival waiver completion rate cuts check-in queues from 45 minutes to under 5 minutes."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 4: Day-of-Tour Arrival & Guide Check-in",
        "subtitle": "The departure turnstile: GPS shuttle tracking, mobile QR ticket scan, and equipment dispatch",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Frictionless Arrival & Boarding</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Live Shuttle Tracking:</strong> Guests awaiting hotel pickup view live shuttle location and arrival countdown on their mobile phone (powered by Samsara GPS).</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Sub-Second QR Scan:</strong> Guide scans guest's Apple Wallet QR code using rugged iPad. System confirms booking, waiver verification, and wetsuit size in &lt;300ms.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Pre-Staged Equipment Hand-off:</strong> Gear bin #14 pre-packed with Large wetsuit and size 10 fins handed to guest immediately.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Headcount Reconciliation:</strong> Guide taps "Manifest Finalized"; headcounts sync to shoreside safety console prior to engine start.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Check-in Efficiency KPIs</div>
            <table class="data-table">
              <thead><tr><th>Metric</th><th>Paper Clipboards</th><th>Digital QR + Waivers</th><th>Improvement</th></tr></thead>
              <tbody>
                <tr><td>Check-in Time / Guest</td><td>3.5 minutes</td><td>18 seconds</td><td><span style="color: var(--accent-green); font-weight: 700;">91% Faster</span></td></tr>
                <tr><td>Departure Delays</td><td>22% of tours</td><td>1.8% of tours</td><td><span style="color: var(--accent-green); font-weight: 700;">-20 pts Delay</span></td></tr>
                <tr><td>Waiver Audit Compliance</td><td>82% (Lost forms)</td><td>100% (Cryptographic)</td><td><span style="color: var(--accent-green); font-weight: 700;">Zero Legal Risk</span></td></tr>
                <tr><td>Standby Seat Resale</td><td>12% captured</td><td>88% captured</td><td><span style="color: var(--accent-green); font-weight: 700;">+$4.2M Margin</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "18 seconds per guest vs 3.5 minutes. When you're boarding 100 passengers onto a boat, that is the difference between on-time departure and a 45-minute delay."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 5: In-Experience Delivery, Safety & Photos",
        "subtitle": "The tour experience: guide mobile companion, automated facial photo tagging, and emergency telemetry",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">In-Experience Operations & Delivery</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Guide Mobile Companion:</strong> Guide's rugged tablet displays participant dietary notes, emergency contacts, and tour timeline milestones in offline mode.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Automated Photo Capture:</strong> Professional tour photographer captures high-res photos during zipline or dive; uploaded to edge server with AI facial tagging.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Real-Time Fleet Geofencing:</strong> Samsara telematics tracks tour boat/van location; automatically alerts dispatch if vessel enters restricted marine sanctuary.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Emergency Satellite SOS:</strong> Garmin inReach / Iridium satellite link allows guide to trigger instant SOS with exact coordinates from remote wilderness.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">In-Experience Technology Stack</div>
            <table class="data-table">
              <thead><tr><th>Capability</th><th>Platform / Tech</th><th>Operational Role</th></tr></thead>
              <tbody>
                <tr><td>Guide Companion</td><td>Offline SQLite / React Native</td><td>Offline manifest, incident logging, timekeeping</td></tr>
                <tr><td>Photo Tagging</td><td>AWS Rekognition / Local AI Edge</td><td>Matches photos to participant faces automatically</td></tr>
                <tr><td>Vehicle Safety</td><td>Samsara AI Dashcams</td><td>Detects driver fatigue, harsh braking, speeding</td></tr>
                <tr><td>Wilderness Comms</td><td>Garmin inReach / Zello PTT</td><td>Satellite SOS messaging & cellular push-to-talk</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Automated facial recognition photo tagging turns what used to be an exhausting manual photo sorting task into an instant, high-margin upsell."
    },
    {
        "part": "PART 7: CUSTOMER JOURNEYS",
        "title": "Phase 6: Post-Tour Review Capture & Retention",
        "subtitle": "Closing the loop: instant photo package delivery, Tripadvisor review prompt, and future direct booking",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Post-Experience Re-engagement</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Instant Photo Gallery SMS:</strong> 30 minutes after tour completion, guest receives SMS: "Your snorkeling photos are ready! View your personalized gallery."</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>1-Click Photo Purchase:</strong> Guest purchases high-res digital photo package for $39 via Apple Pay; images delivered instantly to camera roll.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Review Acceleration Workflow:</strong> Positive photo buyers prompted: "Loved your guide Keanu? Leave a 5-star review on Tripadvisor!" Directly deep-linked to review page.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Cross-Sell Bounce-Back:</strong> "Book your next island tour direct and save 15% with promo code ALOHA15."</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Post-Tour Commercial Impact</div>
            <table class="data-table">
              <thead><tr><th>Metric</th><th>Industry Average</th><th>AI-Orchestrated</th><th>Commercial Lift</th></tr></thead>
              <tbody>
                <tr><td>Photo Package Sales</td><td>11.0% attach</td><td>32.5% attach</td><td><span style="color: var(--accent-green); font-weight: 700;">+195% Margin</span></td></tr>
                <tr><td>Tripadvisor Review Velocity</td><td>4.2 reviews / mo</td><td>28.5 reviews / mo</td><td><span style="color: var(--accent-green); font-weight: 700;">#1 Organic Rank</span></td></tr>
                <tr><td>Direct Re-booking Rate</td><td>3.5%</td><td>14.8%</td><td><span style="color: var(--accent-green); font-weight: 700;">+$8.2M Margin</span></td></tr>
                <tr><td>Guide Gratuity via Mobile</td><td>$4.50 / guest</td><td>$11.20 / guest</td><td><span style="color: var(--accent-green); font-weight: 700;">+148% Tips</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Sending the photo gallery within 30 minutes while the dopamine is still high results in a 3x higher purchase rate than sending it the next day."
    },

    # PART 8: PROCESS OPTIMIZATION & WORKFLOWS (37-41)
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "As-Is vs To-Be Operational Transformation",
        "subtitle": "Re-engineering legacy manual tour operations into an automated, digital-first operating model",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Legacy As-Is Operational State</div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-red);">1</div><div><strong>Clipboard Bottlenecks:</strong> 80 passengers waiting in line under the hot sun to sign physical paper waivers on clipboards with broken pens.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-red);">2</div><div><strong>Manual OTA Extranet Updates:</strong> Office staff spending 4 hours every morning manually typing Viator and GetYourGuide bookings into local booking software.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-red);">3</div><div><strong>Weather Chaos:</strong> Sudden squalls force staff to make 100 frantic phone calls to cancel tours, resulting in chargebacks and furious tourists.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Modern To-Be Digital Ecosystem</div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-green);">1</div><div><strong>Pre-Arrival Mobile Waivers:</strong> 85%+ waivers signed on personal phones before arriving; 18-second QR check-in at the dock.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-green);">2</div><div><strong>Bi-directional OCTO Sync:</strong> Zero manual data entry; real-time inventory locking across all OTAs and direct channels automatically.</div></div>
            <div class="flow-step"><div class="step-num" style="background: var(--accent-green);">3</div><div><strong>Autonomous Weather Rebooking:</strong> Agentforce identifies weather cancellations, rebooks 70% of guests to alternative slots, and issues instant refunds.</div></div>
          </div>
        </div>
        """,
        "notes": "The operational transformation frees staff from low-value data entry and phone answering, letting them focus on delivering unforgettable guest experiences."
    },
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "Automated Turnaround & Equipment Allocation",
        "subtitle": "The 45-minute turnaround: sanitizing, inspecting, and staging gear between morning and afternoon tours",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">Tour Turnaround Critical Path (45-Minute Window)</div>
          <div class="mermaid">
          gantt
            title 45-Minute Tour Turnaround Workflow (12:00 to 12:45)
            dateFormat mm
            axisFormat %M min

            section Disembarkation
            Morning Tour Docks & Debarks   :00, 10
            Equipment Offload & Sorting     :05, 15
            section Sanitization & Inspection
            Wetsuit & Snorkel Sanitization  :10, 25
            Zipline Harness Safety Torque   :15, 30
            Vessel Refueling & Waste Pump   :15, 35
            section Afternoon Staging
            Afternoon Gear Pre-Binning      :25, 40
            Afternoon Manifest Finalized    :30, 40
            section Boarding
            Afternoon Guest QR Check-in     :35, 45
            All-Aboard & Engine Departure   :43, 45
          </div>
        </div>
        """,
        "notes": "Tight turnarounds maximize asset utilization. Turning a catamaran or zipline course around in 45 minutes allows 2 full tours per day instead of 1."
    },
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "Dynamic Revenue & Departure Slot Yield",
        "subtitle": "Algorithmic pricing based on weather, booking window, historical demand, and competitor rates",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Dynamic Pricing Algorithms</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Prime-Time Slot Premiums:</strong> 09:00 AM and 01:00 PM departures priced at a 20% premium ($145 vs $119 baseline); early bird 06:30 AM discounted to drive baseline volume.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Weather-Surge Pricing:</strong> Perfect sunny weather forecast increases outdoor tour prices by 15%; overcast forecast triggers automated indoor museum promotions.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Last-Minute Scarcity Escalation:</strong> When remaining capacity on a departure falls below 4 seats, price escalates 25% automatically across all channels.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Dynamic Pricing Impact Benchmark</div>
            <table class="data-table">
              <thead><tr><th>Product</th><th>Static Pricing</th><th>Dynamic Yield Engine</th><th>Revenue Lift</th></tr></thead>
              <tbody>
                <tr><td>Catamaran Snorkel (Peak)</td><td>$125 flat</td><td>$110 - $165 dynamic</td><td><span style="color: var(--accent-green); font-weight: 700;">+21.4% Lift</span></td></tr>
                <tr><td>Zipline Canopy Tour</td><td>$149 flat</td><td>$129 - $189 dynamic</td><td><span style="color: var(--accent-green); font-weight: 700;">+18.2% Lift</span></td></tr>
                <tr><td>Sunset Cocktail Cruise</td><td>$89 flat</td><td>$79 - $125 dynamic</td><td><span style="color: var(--accent-green); font-weight: 700;">+26.8% Lift</span></td></tr>
                <tr><td>Guided E-Bike Tour</td><td>$95 flat</td><td>$85 - $115 dynamic</td><td><span style="color: var(--accent-green); font-weight: 700;">+14.5% Lift</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Dynamic pricing in tours has historically lagged behind airlines and hotels, but early adopters are seeing 15-25% immediate top-line revenue lift."
    },
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "Workforce & Certified Guide Scheduling",
        "subtitle": "Matching guide language skills, Wilderness First Responder (WFR) credentials, and seasonal shifts",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Guide Scheduling Complexity</div>
            <p>Tour guides are the heart of experiential travel. Managing a workforce of 150+ guides requires balancing legal certifications, language skills, vehicle driver licenses, and unpredictable weather shifts.</p>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Automated Credential Tracking:</strong> System tracks Wilderness First Responder (WFR), CPR, Coast Guard Captain's Licenses, and CDL endorsements. Expired credentials automatically lock guides from scheduling.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Language & Skill Matching:</strong> Spanish, German, or Japanese-speaking private tour requests automatically assigned to qualified guides.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Fair Shift & Tip Equity:</strong> Algorithms balance high-tipping prime weekend tours with lower-volume weekday shifts across the guide pool.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Workforce Systems Architecture</div>
            <table class="data-table">
              <thead><tr><th>Platform</th><th>Domain</th><th>Critical Capability</th></tr></thead>
              <tbody>
                <tr><td><strong>Deputy / When I Work</strong></td><td>Guide Scheduling</td><td>Mobile shift swapping, overtime tracking, geofenced clock-in</td></tr>
                <tr><td><strong>Salesforce Field Service</strong></td><td>Enterprise Dispatch</td><td>Complex guide & vehicle routing, customer ETA push</td></tr>
                <tr><td><strong>TipHaus / Branch</strong></td><td>Digital Tip Payouts</td><td>Instant end-of-day electronic tip distribution to guide debit cards</td></tr>
                <tr><td><strong>TalentLMS</strong></td><td>Guide Certification</td><td>Safety compliance modules, wildlife encounter training</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Instant electronic tip payout at the end of every shift has become a major recruiting and retention tool for tour guides."
    },
    {
        "part": "PART 8: PROCESS OPTIMIZATION",
        "title": "Safety, Incident Management & Emergency SOS",
        "subtitle": "Wilderness emergency response, incident logging, park ranger reporting, and insurance documentation",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Emergency Incident Protocol</div>
            <div class="flow-step"><div class="step-num">🚨</div><div><strong>Field Incident Logging:</strong> Guide logs participant slip/fall directly in mobile app (offline mode) with timestamped photos, GPS coordinates, and witness statements.</div></div>
            <div class="flow-step"><div class="step-num">📡</div><div><strong>Satellite SOS Escalation:</strong> In remote canyons with zero cellular coverage, guide triggers Garmin inReach SOS, notifying GEOS International Emergency Center and local Search & Rescue.</div></div>
            <div class="flow-step"><div class="step-num">📑</div><div><strong>Automated Regulatory Filing:</strong> Incident report automatically pre-populates NPS Form 10-58 (Visitor Injury) and OSHA 301 logs.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Incident Architecture & Insurance Defensibility</div>
            <div class="mermaid">
            flowchart TD
              Field["Field Incident Occurs"] --> App["Guide Mobile Incident Logger"]
              App --> Photo["Timestamped Injury Photos"]
              App --> GPS["Samsara / Device GPS Coordinates"]
              App --> Waiver["Link Signed Digital Waiver"]
              App --> Cloud["Upload to Legal Cloud Vault"]
              Cloud --> Ins["Automated Notice to Insurance Broker"]
              Cloud --> NPS["NPS / USCG Regulatory Report"]
            </div>
          </div>
        </div>
        """,
        "notes": "A properly documented digital incident report with timestamped GPS, photos, and the signed waiver can save millions in frivolous personal injury litigation."
    },

    # PART 9: AI & AGENTIC SYSTEMS (42-46)
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Experience Enterprise AI Architecture",
        "subtitle": "Hierarchical agentic fabric balancing cloud foundation models with offline field mobile agents",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Dual-Realm AI Architecture</div>
            <div class="flow-step"><div class="step-num">☁️</div><div><strong>Cloud Foundation Tier:</strong> Large frontier models (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro) running in cloud hyperscalers for complex dynamic pricing optimization, multi-day itinerary generation, and marketing copywriting.</div></div>
            <div class="flow-step"><div class="step-num">📱</div><div><strong>Offline Mobile AI Tier:</strong> On-device lightweight models (Apple Foundation Models / Mobile Llama 3) running on guide iPads for offline multilingual speech translation and safety guidelines.</div></div>
            <div class="flow-step"><div class="step-num">🛡️</div><div><strong>Safety Guardrails:</strong> Strict deterministic guardrails preventing AI from promising weather guarantees, granting unauthorized refunds, or altering legal waiver terms.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">AI Agentic Architecture Topology</div>
            <div class="mermaid">
            flowchart TD
              Traveler["Traveler (Web / WhatsApp / SMS)"] --> Gateway["API Gateway"]
              Gateway --> Agentforce["Agentforce Experience Fabric"]
              Agentforce --> Concierge["Booking Concierge Agent"]
              Agentforce --> Weather["Weather Rebooking Agent"]
              Agentforce --> Dispatch["Guide & Fleet Dispatch Agent"]
              Concierge --> Res["ResTech OCTO APIs"]
              Weather --> NOAA["NOAA Weather API"]
              Dispatch --> Samsara["Samsara Fleet API"]
              Agentforce --> Response["Action / Natural Language Response"]
            </div>
          </div>
        </div>
        """,
        "notes": "The combination of cloud foundation models for booking reasoning and on-device offline models for guide translation provides the best of both worlds."
    },
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Multi-Agent Systems & Role Specialization",
        "subtitle": "Autonomous AI agents collaborating across booking concierge, weather rebooking, and guide dispatch",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Specialized Experience AI Agents</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>In-Destination Concierge Agent:</strong> Recommends perfect tours based on traveler family composition, budget, physical fitness, and live weather conditions.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Autonomous Weather Rebooking Agent:</strong> Detects severe weather alerts; automatically cancels hazardous departures and rebooks 70%+ of guests to alternative slots.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Fleet & Guide Dispatch Agent:</strong> Optimizes shuttle bus pickup routes based on live traffic; assigns certified guides to match guest language needs.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Review & Photo Merchandising Agent:</strong> Analyzes tour photos, tags participants, generates personalized preview galleries, and crafts tailored review prompts.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Multi-Agent Collaboration Flow</div>
            <div class="mermaid">
            flowchart TD
              Supervisor["Agent Supervisor / Orchestrator"]
              Supervisor <--> Concierge["Concierge Agent"]
              Supervisor <--> Weather["Weather Rebooker"]
              Supervisor <--> Dispatch["Dispatch Agent"]
              Supervisor <--> Review["Review & Photo Agent"]
              Weather -->|Cancelled Departure| Dispatch
              Dispatch -->|Reroute Guides| ResTech["ResTech System of Record"]
              Weather -->|Rebook Guests| Review
            </div>
          </div>
        </div>
        """,
        "notes": "Agent collaboration is key: when the Weather Agent cancels a tour, it alerts the Dispatch Agent to stand down vehicles and re-assign guides."
    },
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Model Context Protocol & Tour Tooling",
        "subtitle": "Connecting agentic AI to ResTech, waivers, and telematics via standardized MCP tool servers",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">MCP Tool Catalog for Experiences</div>
            <table class="data-table">
              <thead><tr><th>MCP Tool Name</th><th>Target System</th><th>Parameters & Function</th></tr></thead>
              <tbody>
                <tr><td><code>check_slot_availability</code></td><td>ResTech (Bokun)</td><td>TourID, Date, PaxCount; returns available departure slots.</td></tr>
                <tr><td><code>rebook_tour_departure</code></td><td>ResTech / OCTO</td><td>BookingID, NewSlotID; transfers reservation and updates manifest.</td></tr>
                <tr><td><code>query_shuttle_eta</code></td><td>Samsara Telematics</td><td>HotelStopID, VehicleID; returns real-time ETA in minutes.</td></tr>
                <tr><td><code>verify_waiver_status</code></td><td>Smartwaiver</td><td>ParticipantEmail, BookingID; returns signed status & PDF link.</td></tr>
                <tr><td><code>issue_voucher_credit</code></td><td>Stripe / ResTech</td><td>BookingID, Amount; issues digital gift voucher or card refund.</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">MCP Tool Execution Example</div>
            <pre style="background: rgba(0,0,0,0.4); padding: 0.8rem; border-radius: 6px; font-size: 0.75rem; color: #a5d6a7;">
// Weather Rebooking Agent MCP Tool Execution
{
  "tool": "rebook_tour_departure",
  "arguments": {
    "booking_id": "BK-789210",
    "target_slot_id": "SLOT-2026-10-15-0900",
    "reason": "WEATHER_CANCELLATION_GALE_WARNING",
    "customer_confirmed": true,
    "notify_customer_channel": "WHATSAPP"
  }
}
// Response from Bokun ResTech Engine
{
  "status": "SUCCESS",
  "new_booking_id": "BK-789210-R1",
  "departure_time": "2026-10-15T09:00:00-10:00",
  "barcode_url": "https://tickets.example.com/qr/88219"
}
            </pre>
          </div>
        </div>
        """,
        "notes": "Model Context Protocol (MCP) gives AI agents clean, structured programmatic access to ResTech engines and telematics feeds."
    },
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Predictive ML & Tour Demand Forecasting",
        "subtitle": "Data-driven optimization of departure slot pricing, guide staffing, and no-show prediction",
        "content": """
        <div class="grid-3">
          <div class="glass-card">
            <div class="card-header">Predictive No-Show Modeling</div>
            <p><strong>Model:</strong> Gradient boosted trees trained on booking channel, lead time, hotel location, and weather forecast.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-green">Impact</span></p>
              <p>Predicts probability of no-shows with 88% accuracy; allows controlled 5% overbooking on low-risk departures, recovering $3.4M in empty seat revenue.</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Dynamic Guide Staffing</div>
            <p><strong>Model:</strong> Time-series forecasting (Prophet / ARIMA) predicting 14-day advance booking curves per tour category.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-blue">Impact</span></p>
              <p>Eliminates over-staffing on slow days and under-staffing on surge weekends, cutting seasonal labor waste by 16% ($2.8M savings).</p>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Dynamic Yield Pricing</div>
            <p><strong>Model:</strong> Reinforcement learning adjusting departure prices in real time based on remaining seat velocity and OTA demand.</p>
            <div style="margin-top: 0.8rem; font-size: 0.85rem;">
              <p><span class="pill pill-purple">Impact</span></p>
              <p>Lifts average ticket price by 18.5% on prime weekend departures, driving $6.8M in incremental gross margin.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Predictive ML turns tour operating from a guessing game into a precision science, optimizing both labor costs and ticket yield."
    },
    {
        "part": "PART 9: AI & AGENTIC SYSTEMS",
        "title": "Deflection, Resolution & Experience AI ROI",
        "subtitle": "Quantifying the commercial and operational impact of AI automation across tours and attractions",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">AI Operational Impact Metrics</div>
            <table class="data-table">
              <thead><tr><th>Operational Domain</th><th>Pre-AI Baseline</th><th>AI-Assisted State</th><th>Net Business Value</th></tr></thead>
              <tbody>
                <tr><td>Customer Inbound Deflection</td><td>12.0% (Basic FAQ)</td><td>74.5% (Agentforce / SMS)</td><td>$8.4M annual labor savings</td></tr>
                <tr><td>Weather Rebooking Recovery</td><td>28.0% recovered</td><td>72.5% recovered</td><td>$14.2M saved tour revenue</td></tr>
                <tr><td>Direct Booking Conversion</td><td>2.1% website avg</td><td>4.8% (AI Concierge)</td><td>$11.6M OTA commission saved</td></tr>
                <tr><td>Photo Package Attach Rate</td><td>11.0% attach</td><td>32.5% attach</td><td>$6.8M high-margin photo revenue</td></tr>
                <tr><td>Check-in Bottlenecks</td><td>25 min peak wait</td><td>3 min peak wait</td><td>+22 points in Guest NPS</td></tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">The $41.0M Annual Value Creation Engine</div>
            <div class="flow-step"><div class="step-num">$</div><div><strong>Direct Commission Savings:</strong> $11.6M saved by shifting OTA bookings to direct website bookings via de-anonymization.</div></div>
            <div class="flow-step"><div class="step-num">🌧️</div><div><strong>Weather Revenue Recovery:</strong> $14.2M in tour revenue saved via autonomous instant rebooking into alternative slots.</div></div>
            <div class="flow-step"><div class="step-num">⚙️</div><div><strong>Labor & Ancillary Lift:</strong> $15.2M in contact center labor savings and high-margin photo/video sales.</div></div>
            <div style="margin-top: 1rem;">
              <span class="pill pill-green">Total Annual Value: $41.0M across enterprise</span>
            </div>
          </div>
        </div>
        """,
        "notes": "The business case for AI in tours is bulletproof: saving $14M in weather cancellations alone pays for the entire technology investment."
    },

    # PART 10: MASTER INTEGRATION & ROADMAP (47-52)
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Master Enterprise Integration Topology",
        "subtitle": "End-to-end integration topology connecting OTAs, ResTech engines, cloud hubs, and field terminals",
        "content": """
        <div class="glass-card" style="margin-bottom: 1rem;">
          <div class="card-header">Master Experience Integration Topology</div>
          <div class="mermaid">
          flowchart LR
            subgraph OTAs["Global Distribution Channels"]
              VTR["Viator / Tripadvisor"]
              GYG["GetYourGuide"]
              KLK["Klook"]
              DIR["Direct Web / App"]
            end
            subgraph Gateway["API Gateway & Connectivity"]
              OCTO["OCTO API Gateway"]
              MULE["Enterprise MuleSoft Anypoint"]
              VTR & GYG & KLK & DIR --> OCTO
              OCTO --> MULE
            end
            subgraph Core["Enterprise Cloud Core"]
              RES["ResTech Core (Bokun/FareHarbor)"]
              DC["Salesforce Data Cloud / Snowflake"]
              CRM["Salesforce Core / Dynamics 365"]
              AI["Agentforce AI Engine"]
              MULE <--> RES & DC & CRM & AI
            end
            subgraph Field["Field Operations & Edge"]
              WAIV["Smartwaiver Legal Vault"]
              GUIDE["Guide Handhelds (Offline SQLite)"]
              FLEET["Samsara Fleet GPS & AI Dashcams"]
              GATE["Skidata / Axess Turnstiles"]
              Core <--> Field
            end
          </div>
        </div>
        """,
        "notes": "This master topology illustrates how all channels, core engines, and field systems integrate into a cohesive enterprise architecture."
    },
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "OCTO Protocol Translation & Channel Sync",
        "subtitle": "Detailed architecture of real-time inventory locking, rate parity, and OTA webhook ingestion",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Channel Sync Architecture Stages</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Inbound Booking Webhook:</strong> Viator pushes <code>BookingRequest</code> payload via OCTO v1.2 specification.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Atomic Capacity Hold:</strong> Distributed Redis lock verifies and reserves requested seats in &lt;50ms.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Downstream Channel Broadcast:</strong> Event mesh broadcasts remaining capacity updates to GetYourGuide and Klook via asynchronous OCTO push.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Field Handheld Delta Sync:</strong> Guide tablet manifests updated via background WebSocket connection.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Channel Latency & Consistency Benchmark</div>
            <table class="data-table">
              <thead><tr><th>Channel Operation</th><th>Legacy Polling</th><th>Modern OCTO Push</th><th>Improvement</th></tr></thead>
              <tbody>
                <tr><td>Availability Query</td><td>2,400ms</td><td>180ms</td><td><span style="color: var(--accent-green); font-weight: 700;">92% Faster</span></td></tr>
                <tr><td>Booking Commit</td><td>4,500ms</td><td>320ms</td><td><span style="color: var(--accent-green); font-weight: 700;">93% Faster</span></td></tr>
                <tr><td>Multi-OTA Sync Window</td><td>15 - 30 minutes</td><td>&lt; 1.5 seconds</td><td><span style="color: var(--accent-green); font-weight: 700;">Zero Overbooking</span></td></tr>
                <tr><td>Cancellation Capacity Return</td><td>Manual email / hours</td><td>Instantaneous</td><td><span style="color: var(--accent-green); font-weight: 700;">Instant Resale</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Moving from 15-minute polling to sub-second OCTO push eliminates overbooking across multiple OTAs forever."
    },
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Phased Implementation Roadmap (24 Months)",
        "subtitle": "Strategic four-phase execution timeline mitigating operational disruption across seasonal peaks",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Four Implementation Phases</div>
            <div class="flow-step"><div class="step-num">P1</div><div><strong>Months 1-6: ResTech Core & OCTO Integration:</strong> Consolidate fragmented booking engines into Bokun/FareHarbor, deploy OCTO API gateway to top 3 OTAs, and roll out digital waivers.</div></div>
            <div class="flow-step"><div class="step-num">P2</div><div><strong>Months 7-12: Data Fabric & Traveler 360:</strong> Stand up Salesforce Data Cloud / Snowflake, establish waiver de-anonymization pipeline, and launch direct customer marketing journeys.</div></div>
            <div class="flow-step"><div class="step-num">P3</div><div><strong>Months 13-18: Field Operations & Fleet Telematics:</strong> Deploy rugged guide tablets with offline check-in, install Samsara AI telematics across fleet, and integrate turnstiles.</div></div>
            <div class="flow-step"><div class="step-num">P4</div><div><strong>Months 19-24: Autonomous AI & Dynamic Yield:</strong> Deploy Agentforce autonomous weather rebooking, dynamic pricing yield engine, and automated photo merchandising.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Seasonal Implementation Alignment</div>
            <div class="mermaid">
            flowchart TD
              LowSeason1["Months 1-6: Winter Low Season (Core Setup)"] --> Pilot["Months 7-9: Spring Shoulder (Pilot 2 Locations)"]
              Pilot --> Peak1["Months 10-12: Summer Peak (Freeze Changes / Run)"]
              Peak1 --> LowSeason2["Months 13-18: Winter Low Season (Fleet & AI)"]
              LowSeason2 --> Peak2["Months 19-24: Full Global Deployment (Peak Ready)"]
            </div>
            <div style="margin-top: 1rem; font-size: 0.85rem; color: var(--text-muted);">
              <p><strong>Critical Risk Rule:</strong> Zero core software migrations during July/August summer peak. Major infrastructure transitions execute exclusively during winter shoulder months.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Never touch core booking systems during the July/August summer rush. Phase deployments strictly around winter low seasons."
    },
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Target Operating Model & Change Management",
        "subtitle": "Structuring organization, field guide enablement, and cross-functional operational squads",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Target Operating Model (BCG Framework)</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Experience Product Pods:</strong> Agile squads (Product Manager, Solutions Architect, Operations Lead, UX Designer) dedicated to specific customer moments (e.g., In-Market Booking, Field Departure, Post-Tour Photo).</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>Field Lead Ambassadors:</strong> Senior guides trained as digital champions to mentor seasonal staff on mobile tablet check-in and waiver troubleshooting.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Central Operations Command (COC):</strong> Centralized 24/7 dispatch center monitoring fleet GPS, weather radars, and turnstile throughput in real time.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Field Change Management Principles</div>
            <table class="data-table">
              <thead><tr><th>Stakeholder Group</th><th>Primary Resistance</th><th>Change Strategy</th></tr></thead>
              <tbody>
                <tr><td>Seasonal Tour Guides</td><td>Reluctance to carry tablets; fear of battery death in cold.</td><td>Ruggedized cases with hand straps, 10-hour battery life, high-contrast sunlight UI, automated tip boost.</td></tr>
                <tr><td>Reservations Staff</td><td>Fear of AI chatbots eliminating customer service jobs.</td><td>Reposition agents as "VIP Destination Specialists" handling high-ticket luxury custom itineraries.</td></tr>
                <tr><td>Shuttle Bus Drivers</td><td>Distrust of AI dashcams and GPS telematics.</td><td>Focus dashcams on driver exoneration during accidents; bonus incentives for safe driving scores.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """,
        "notes": "Guide adoption makes or breaks field technology. If the tablet is clunky or dies in the cold, guides will immediately pull out paper clipboards."
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
                <tr><td><strong>OTA Connectivity & De-anonymization</strong></td><td>4.8 / 5.0</td><td>4.1 / 5.0</td><td>4.7 / 5.0</td></tr>
                <tr><td><strong>Speed of Implementation (Time-to-Value)</strong></td><td>4.7 / 5.0</td><td>3.4 / 5.0</td><td>3.5 / 5.0</td></tr>
                <tr><td><strong>Field Offline Resilience</strong></td><td>4.0 / 5.0</td><td>4.6 / 5.0</td><td>4.9 / 5.0</td></tr>
                <tr><td><strong>Total Cost of Ownership (TCO)</strong></td><td>3.9 / 5.0</td><td>4.3 / 5.0</td><td>2.3 / 5.0</td></tr>
                <tr><td><strong>AI Automation & Weather Rebooking</strong></td><td>4.8 / 5.0</td><td>3.6 / 5.0</td><td>4.9 / 5.0</td></tr>
                <tr style="font-weight: 700; background: rgba(255,255,255,0.05);">
                  <td><strong>Blended Composite Score</strong></td>
                  <td><span style="color: var(--accent-blue);">4.44 / 5.00</span></td>
                  <td><span style="color: var(--accent-green);">4.00 / 5.00</span></td>
                  <td><span style="color: var(--accent-purple);">4.06 / 5.00</span></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Architectural Recommendation</div>
            <div class="flow-step"><div class="step-num">🏆</div><div><strong>Best Commercial Balance: Variation 1 (With Salesforce):</strong> Delivers the fastest payback (9 months) and highest commercial ROI by turning anonymous OTA bookings into direct lifetime customers via Data Cloud and Agentforce.</div></div>
            <div class="flow-step"><div class="step-num">🚀</div><div><strong>Ultra-Tier Scale: Variation 3:</strong> Recommended for massive national attractions, ski resorts, and mega-operators ($500M+ revenue) where Palantir fleet twins and Skidata turnstiles dominate.</div></div>
          </div>
        </div>
        """,
        "notes": "Variation 1 earns the highest composite score (4.44) due to its unbeatable ability to de-anonymize OTA guests and automate weather rebooking."
    },
    {
        "part": "PART 10: INTEGRATION & ROADMAP",
        "title": "Executive Conclusion & Experiences North Star",
        "subtitle": "The definitive architectural vision for the future of experiential travel, tours, and attractions",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Core Architectural Takeaways</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>De-anonymize or Perish:</strong> Operators who fail to capture real traveler identities via digital waivers will remain trapped paying 25% commissions to OTAs forever.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>OCTO is the Universal Standard:</strong> Standardize all channel distribution on OCTO OpenAPI 3.0 to eliminate custom point-to-point maintenance debt.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>Field Handhelds Must Be Offline-First:</strong> Never rely on cellular signal in the wild. Build local SQLite caching and background sync into every guide tool.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>Autonomous Weather Resilience is High ROI:</strong> Agentforce weather rebooking saves millions in lost cancellations while delighting stranded travelers.</div></div>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic North Star Architecture</div>
            <div style="text-align: center; padding: 1.5rem 0;">
              <div class="metric-hero" style="font-size: 2.2rem; color: var(--accent-green);">Connected • Autonomous • Experiential</div>
              <p style="margin-top: 1rem; color: var(--text-muted); font-size: 0.95rem;">A unified enterprise experiences ecosystem connecting global OTA distribution with rugged field excellence, creating unforgettable human adventures and sustainable enterprise value.</p>
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
    html_output_path = os.path.join(BASE_DIR, "tours", "presentation.html")
    md_output_path = os.path.join(BASE_DIR, "tours", "PRESENTATION_FRAMEWORK_COMPENDIUM.md")

    # Apply visual enhancements (interactive charts, Mermaid architectures, CLI suites)
    slides = vsc.apply_visual_enhancements("TOURS", slides)

    engine.render_reveal_html(meta, slides, html_output_path)
    engine.render_presentation_markdown(meta, slides, md_output_path)
    print("Tours presentation generation complete. Total slides:", len(slides))
