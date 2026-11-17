#!/usr/bin/env python3
"""
Hotels & Lodging Presentation Generator — 52 Slides
Generates:
1. /run/media/ml/Storage/Labs/hotels/presentation.html
2. /run/media/ml/Storage/Labs/hotels/PRESENTATION_FRAMEWORK_COMPENDIUM.md
"""

import os
import sys
import json

BASE_DIR = "/run/media/ml/Storage/Labs"
sys.path.append(BASE_DIR)
import generate_presentation_engine as engine
import visual_slide_components as vsc

meta = {
    "title": "Hospitality & Lodging Systems Architecture",
    "short_code": "HOTELS",
    "sector": "Hotels, Lodging & Integrated Resorts",
    "scale": "$600.0B Room GBV • 4.25B Room Nights • $141.18 ADR • $194.6B GOP"
}

slides = [
    # PART 1: MACROECONOMICS, SIZING & REVENUE MODELS (1-5)
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Hospitality Enterprise Architecture Masterclass",
        "subtitle": "Systems Architecture, Technology Stacks, and Operational Orchestration across 13 Enterprise Dimensions",
        "content": """
        <div class="grid-2" style="margin-top: 1rem;">
          <div class="glass-card">
            <div class="card-header">Executive Briefing Scope</div>
            <p>Comprehensive architectural blueprint analyzing the mission-critical systems governing modern hotels, resorts, and lodging groups ($600B global market, 4.25B room nights). Designed for Hospitality CIOs, Chief Commercial Officers, and Enterprise Architects.</p>
            <div style="margin-top: 1rem;">
              <span class="pill pill-blue">13 Enterprise Layers</span>
              <span class="pill pill-green">3 Stack Variations</span>
              <span class="pill pill-purple">52 Master Slides</span>
              <span class="pill pill-amber">End-to-End Guest Journeys</span>
            </div>
          </div>
          <div class="glass-card">
            <div class="card-header">Core Themes Covered</div>
            <div class="flow-step"><div class="step-num">1</div><div><strong>Requirements & Governance:</strong> Multi-brand franchise complexity, asset owner P&L scrutiny, and HTNG/OHIP standards.</div></div>
            <div class="flow-step"><div class="step-num">2</div><div><strong>13-Layer Master Architecture:</strong> PMS, CRS, Channel Managers, RMS, POS, CRM, Loyalty, CDP, Lakehouse, AI.</div></div>
            <div class="flow-step"><div class="step-num">3</div><div><strong>End-to-End Guest Journeys:</strong> Google Hotel Ads search, direct booking, pre-arrival upsell, Apple Wallet NFC keys, and night audit.</div></div>
            <div class="flow-step"><div class="step-num">4</div><div><strong>AI-Assisted Efficiency:</strong> Agentforce concierge, HotSOS housekeeping dispatch, and dynamic pricing models.</div></div>
          </div>
        </div>
        """,
        "notes": "Welcome executive stakeholders. This deck provides an unbroken technical and commercial chain of logic across all hotel technology layers."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Global Lodging Sizing & Revenue Architecture",
        "subtitle": "Macroeconomic baseline: $600.0B Gross Booking Value across 4.25 Billion annual room nights",
        "content": """
        <div class="grid-4" style="margin-bottom: 1rem;">
          <div class="glass-card">
            <div class="metric-hero">$600.0B</div>
            <div class="metric-sub">Global Room GBV</div>
            <p style="margin-top: 0.4rem; color: var(--text-muted);">4.25B room nights globally at a blended ADR of $141.18.</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero" style="color: #10b981;">$512.3B</div>
            <div class="metric-sub">Net Hotel Room Revenue</div>
            <p style="margin-top: 0.4rem; color: var(--text-muted);">85.4% retained by property owners after distribution friction.</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero" style="color: #ef4444;">$87.7B</div>
            <div class="metric-sub">Distribution Friction</div>
            <p style="margin-top: 0.4rem; color: var(--text-muted);">14.6% blended take rate across OTAs, GDS, Bedbanks, and TMCs.</p>
          </div>
          <div class="glass-card">
            <div class="metric-hero" style="color: #f59e0b;">$194.6B</div>
            <div class="metric-sub">Gross Operating Profit (GOP)</div>
            <p style="margin-top: 0.4rem; color: var(--text-muted);">32.4% of GBV / 38.0% margin on Net Revenue. Property EBITDA.</p>
          </div>
        </div>
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Property Supply Segmentation</div>
            <table class="data-table">
              <tr><th>Property Category</th><th>Share</th><th>Annual GBV</th><th>Core Systems</th></tr>
              <tr><td>Branded & Chain Hotels</td><td>45.0%</td><td>$270.0B</td><td>Oracle Opera, Sabre SynXis, MARSHA</td></tr>
              <tr><td>Independent & Boutique Hotels</td><td>42.0%</td><td>$250.0B</td><td>Cloudbeds, Mews, SiteMinder, Protel</td></tr>
              <tr><td>Resorts, Casinos & Luxury</td><td>8.0%</td><td>$50.0B</td><td>Agilysys, Opera Cloud, Bally CMS</td></tr>
              <tr><td>Serviced Apartments / Extended</td><td>5.0%</td><td>$30.0B</td><td>Opera PMS, RMS Cloud, SynXis</td></tr>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Strategic Takeaway</div>
            <p>Distribution friction ($87.7B) is the single largest controllable cost in hotel operations. Shifting just 5% of bookings from OTAs to direct Brand.com expands hotel net GOP by <strong>$15.2 Billion globally</strong>.</p>
          </div>
        </div>
        """,
        "notes": "Establish the macro scale. Hoteliers surrender $87.7B annually to intermediaries."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Distribution Friction & Unit Economics Breakdown",
        "subtitle": "Financial waterfall tracking every dollar on a $200 ADR room night to hotel net profit",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header">Hotel Room Unit Economics ($200.00 ADR Example)</div>
            <table class="data-table">
              <tr><th>Component</th><th>Amount ($)</th><th>% of GBV</th><th>Operational Cost Driver</th></tr>
              <tr><td><strong>Gross Booking Value (ADR)</strong></td><td><strong>$200.00</strong></td><td><strong>100.0%</strong></td><td>Guest Room Night Rate</td></tr>
              <tr><td>OTA Commission (Blended 18%)</td><td>-$23.40</td><td>-11.7%</td><td>Weighted by 65% intermediated share</td></tr>
              <tr><td>Bedbank Markup / Wholesale</td><td>-$4.40</td><td>-2.2%</td><td>Hotelbeds / WebBeds net margin</td></tr>
              <tr><td>GDS & Switch Fees</td><td>-$1.60</td><td>-0.8%</td><td>Sabre/Amadeus booking fees ($4.50/res)</td></tr>
              <tr><td>Credit Card Merchant Fee</td><td>-$5.00</td><td>-2.5%</td><td>Payment gateway & acquiring fees</td></tr>
              <tr><td>Tech Stack & SaaS Fees (PMS/CRS)</td><td>-$1.40</td><td>-0.7%</td><td>Per-room SaaS license charges</td></tr>
              <tr><td><strong>Net Hotel Room Revenue</strong></td><td><strong>$164.20</strong></td><td><strong>82.1%</strong></td><td><strong>Net Retained by Property</strong></td></tr>
              <tr><td>Rooms Department Labor</td><td>-$41.05</td><td>-20.5%</td><td>Housekeeping, front desk, uniforms</td></tr>
              <tr><td>Brand Franchise & Royalty (9%)</td><td>-$14.78</td><td>-7.4%</td><td>Marriott/Hilton/IHG brand fees</td></tr>
              <tr><td>Utilities & Property Maintenance</td><td>-$16.42</td><td>-8.2%</td><td>HVAC, electricity, water, repairs</td></tr>
              <tr><td>Local Property Marketing & Sales</td><td>-$11.50</td><td>-5.7%</td><td>Local ads, collateral, local PR</td></tr>
              <tr><td>G&A, Property Tax & Insurance</td><td>-$18.06</td><td>-9.0%</td><td>Real estate taxes, building insurance</td></tr>
              <tr><td><strong>Gross Operating Profit (GOP)</strong></td><td><strong>$62.39</strong></td><td><strong>31.2%</strong></td><td><strong>Property EBITDA per Room Night</strong></td></tr>
            </table>
          </div>
          <div class="glass-card">
            <div class="card-header">Key Architectural Insights</div>
            <p><strong>The $35.80 Friction Barrier:</strong> Total intermediary and payment friction consumes $35.80 per room night. This equals nearly 60% of total property EBITDA ($62.39).</p>
            <div style="margin-top: 0.8rem;">
              <div class="card-header" style="color: #10b981;">The Direct Booking Yield Uplift</div>
              <p>A direct booking through Brand.com pays $0 in OTA commission and $0 in GDS fees, retaining $188.60 net revenue and expanding GOP to <strong>$86.79 (+39.1% profit expansion)</strong>.</p>
            </div>
          </div>
        </div>
        """,
        "notes": "Walk through the unit economics. Direct bookings generate 39% higher EBITDA."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Channel Share Dynamics: Direct vs OTAs vs GDS",
        "subtitle": "The high-stakes battle between Direct Brand.com (35.0%), Mega-OTAs (27.5%), and Corporate GDS (17.5%)",
        "content": """
        <div class="grid-3" style="margin-bottom: 1rem;">
          <div class="glass-card" style="border-left: 3px solid #10b981;">
            <div class="card-header">Direct Channels (35.0% / $210B)</div>
            <p><strong>Brand.com, Loyalty App, Voice, Walk-in:</strong> Highest net margin (88%-92%). Captures first-party guest profile, driving on-property F&B and spa upsell ($45/stay).</p>
          </div>
          <div class="glass-card" style="border-left: 3px solid #f87171;">
            <div class="card-header">Mega-OTAs (27.5% / $165B)</div>
            <p><strong>Booking Holdings, Expedia Group, Trip.com:</strong> 15% to 22% commission take rates. Controls top-of-funnel leisure search. Frequently masks guest contact data.</p>
          </div>
          <div class="glass-card" style="border-left: 3px solid #8b5cf6;">
            <div class="card-header">Corporate GDS & TMCs (17.5% / $105B)</div>
            <p><strong>Sabre, Amadeus, Travelport, Amex GBT, Concur:</strong> Negotiated corporate rates, high ADR ($220+), weekday business demand, GDS segment fees ($4.50-$6.00).</p>
          </div>
        </div>
        <div class="glass-card">
          <div class="card-header">Channel Economics & Net Yield Comparison</div>
          <table class="data-table">
            <tr><th>Channel</th><th>Gross ADR</th><th>Channel Cost</th><th>Payment Fee</th><th>Net Yield to Hotel</th><th>First-Party Data Access</th></tr>
            <tr><td>Direct Brand.com (Web/App)</td><td>$200.00</td><td>$3.00 (Booking Engine)</td><td>$4.50 (2.25%)</td><td><strong>$192.50 (96.3%)</strong></td><td>100% Full Contact & Preferences</td></tr>
            <tr><td>Metasearch (Google Hotels)</td><td>$200.00</td><td>$16.00 (8.0% CPA)</td><td>$4.50 (2.25%)</td><td><strong>$179.50 (89.8%)</strong></td><td>100% Direct Guest Relationship</td></tr>
            <tr><td>Corporate GDS / TMC</td><td>$240.00</td><td>$12.00 (GDS+TMC fee)</td><td>$6.00 (2.5%)</td><td><strong>$222.00 (92.5%)</strong></td><td>Corporate traveler name & company</td></tr>
            <tr><td>Mega-OTA (Expedia/Booking)</td><td>$200.00</td><td>$36.00 (18.0% Comm)</td><td>$6.00 (VCC fee 3%)</td><td><strong>$158.00 (79.0%)</strong></td><td>Masked relay email, zero direct comms</td></tr>
            <tr><td>Bedbank (Hotelbeds)</td><td>$180.00</td><td>$39.60 (22.0% Margin)</td><td>$0.00 (Pre-paid)</td><td><strong>$140.40 (78.0%)</strong></td><td>Zero guest data until check-in</td></tr>
          </table>
        </div>
        """,
        "notes": "Highlight the contrast: Direct yields 96.3% while Bedbanks yield 78.0%."
    },
    {
        "part": "PART 1: MACROECONOMICS & REVENUE",
        "title": "Strategic Business Imperatives for Hoteliers",
        "subtitle": "The four existential operational battlegrounds governing hotel software investments",
        "content": """
        <div class="grid-2">
          <div class="glass-card">
            <div class="card-header" style="color: #3b82f6;">1. Direct Channel Recapture & Guest Lifetime Value</div>
            <p>Hotels must aggressively expand direct booking share past 40% while identifying anonymous OTA bookers. This requires real-time identity resolution in Data Cloud and dynamic pre-arrival engagement via WhatsApp to drive loyalty sign-ups.</p>
            <div style="margin-top: 0.5rem;"><span class="pill pill-blue">Identity Resolution</span><span class="pill pill-blue">Google Hotel Ads</span><span class="pill pill-blue">Loyalty Enrollment</span></div>
          </div>
          <div class="glass-card">
            <div class="card-header" style="color: #10b981;">2. Operational Labor Efficiency & Housekeeping Optimization</div>
            <p>Labor represents 53% of hotel operating expenses. With post-pandemic labor shortages, hotels must automate room assignment, housekeeping dispatch (HotSOS), and front-desk check-in (Apple Wallet NFC digital room keys).</p>
            <div style="margin-top: 0.5rem;"><span class="pill pill-green">HotSOS Dispatch</span><span class="pill pill-green">Apple Wallet Key</span><span class="pill pill-green">Automated Check-in</span></div>
          </div>
          <div class="glass-card">
            <div class="card-header" style="color: #8b5cf6;">3. Unified On-Property Monetization (Total RevPAR / GOPPAR)</div>
            <p>Maximizing room revenue alone is insufficient. Modern operators optimize <strong>Total RevPAR (TRevPAR)</strong> across dining, bars, spas, golf, and cabanas, using unified POS and guest folios to capture $50+ in non-room spend per occupied room.</p>
            <div style="margin-top: 0.5rem;"><span class="pill pill-purple">Simphony POS</span><span class="pill pill-purple">SevenRooms VIP</span><span class="pill pill-purple">TRevPAR Maximization</span></div>
          </div>
          <div class="glass-card">
            <div class="card-header" style="color: #f59e0b;">4. Asset Owner Reporting & Franchise Alignment</div>
            <p>Hotel management companies operate on behalf of real estate asset owners who scrutinize every central technology fee. Software architectures must prove direct RevPAR and GOPPAR uplift on monthly owner statements.</p>
            <div style="margin-top: 0.5rem;"><span class="pill pill-amber">Owner Reporting</span><span class="pill pill-amber">GOPPAR Tracking</span><span class="pill pill-amber">TCO Defense</span></div>
          </div>
        </div>
        """,
        "notes": "Summarize Part 1. These 4 imperatives set the foundation for the 13-layer architecture."
    }
]

# Generate slides 6 to 52 programmatically
# PART 2: REQUIREMENTS & CONSTRAINTS (6-10)
slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Enterprise Baseline Persona: Multi-Brand Hotel Group",
    "subtitle": "Assumed operating model: Global hotel operator managing 540 properties and 85,000 rooms across 56 countries",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Portfolio Scale & Brand Architecture</div>
        <table class="data-table">
          <tr><th>Brand Tier</th><th>Properties</th><th>Total Rooms</th><th>Core Systems</th></tr>
          <tr><td>Luxury Resorts (Anantara / St. Regis tier)</td><td>65 Properties</td><td>12,000 Rooms</td><td>Opera Cloud, SevenRooms, Simphony</td></tr>
          <tr><td>Upper-Upscale Lifestyle (Avani / W tier)</td><td>120 Properties</td><td>24,000 Rooms</td><td>Opera Cloud, SiteMinder, Assa Abloy</td></tr>
          <tr><td>Urban Business / Extended Stay (Fraser / NH tier)</td><td>250 Properties</td><td>38,000 Rooms</td><td>Opera 5.5, SynXis CRS, RMS Cloud</td></tr>
          <tr><td>Midscale & Regional</td><td>105 Properties</td><td>11,000 Rooms</td><td>Cloudbeds, Mews, D-EDGE</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">The Multi-Owner Governance Dilemma</div>
        <p><strong>Decentralized Capital Structure:</strong> Over 70% of properties are owned by third-party institutional real estate investors (REITs, sovereign wealth funds, family offices). Each owner scrutinizes central marketing and IT chargebacks.</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #3b82f6;">Architectural Constraint</div>
          <p>The enterprise stack cannot mandate a simultaneous $50M global PMS replacement. It must provide <strong>Zero-Copy Data Harmonization</strong> across legacy Opera 5.5 on-premise and modern Opera Cloud instances.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "Establish the persona: a global multi-brand operator with mixed ownership."
})

slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Functional Requirements Matrix (PMS, CRS, Guest)",
    "subtitle": "Decomposition of 90+ functional capabilities across 5 hospitality operational domains",
    "content": """
    <div class="grid-3">
      <div class="glass-card">
        <div class="card-header">1. CRS & Distribution</div>
        <p>• <strong>Availability, Rates & Inventory (ARI):</strong> Sub-second rate parity synchronization across 450+ OTA channels.</p>
        <p>• <strong>Dynamic Rate Fences:</strong> Closed user group (CUG) loyalty rates and corporate negotiated discounts.</p>
        <p>• <strong>Group & MICE Quoting:</strong> Automated group room block displacement analysis.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">2. On-Property Operations</div>
        <p>• <strong>Housekeeping Dispatch:</strong> Real-time room status updates (Dirty ➔ Clean ➔ Inspected) in PMS.</p>
        <p>• <strong>Mobile Keyless Entry:</strong> Apple Wallet NFC digital room keys issued automatically upon room readiness.</p>
        <p>• <strong>F&B Folio Posting:</strong> Instant dining bill posting from POS to guest room folio.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">3. Guest Experience & CRM</div>
        <p>• <strong>Pre-Arrival Concierge:</strong> Automated WhatsApp upsell for limousine transfers and cabanas.</p>
        <p>• <strong>Guest Profile Harmonization:</strong> Merging dining, spa, and room stay preferences into a single profile.</p>
        <p>• <strong>Express Checkout:</strong> Contactless folio review and credit card settlement on mobile app.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Cross-System Operational Handshake</div>
      <p>When Housekeeping marks Room 402 'Inspected' in HotSOS, Opera PMS updates inventory state, MuleSoft fires a CDC event to Data Cloud, and Agentforce instantly messages the waiting guest: <em>'Your room is ready! Tap to download your Apple Wallet key.'</em></p>
    </div>
    """,
    "notes": "Walk through the cross-system handshake: HotSOS ➔ Opera ➔ MuleSoft ➔ Data Cloud ➔ Agentforce."
})

slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Non-Functional Requirements (NFRs) & Operational SLAs",
    "subtitle": "Strict performance, throughput, resilience, and recovery benchmarks for global hospitality",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Throughput & Latency SLAs</div>
        <table class="data-table">
          <tr><th>System Interaction</th><th>Peak Throughput</th><th>Latency SLA</th><th>Business Impact</th></tr>
          <tr><td>CRS Room Search / ARI Query</td><td>80,000 requests/sec</td><td>< 200 ms</td><td>Prevents Google Hotel Ads and OTA shopping timeouts</td></tr>
          <tr><td>Direct Web Booking Checkout</td><td>1,500 bookings/sec</td><td>< 600 ms</td><td>Eliminates shopping cart abandonment during promotions</td></tr>
          <tr><td>Digital Key Unlock Door Scan</td><td>500 door taps/second</td><td>< 300 ms</td><td>Instant seamless entry; avoids guest frustration in hallways</td></tr>
          <tr><td>POS Dining Folio Posting</td><td>2,000 checks/minute</td><td>< 100 ms</td><td>Prevents walk-outs and billing disputes at check-out</td></tr>
          <tr><td>Night Audit Processing</td><td>540 hotels batch run</td><td>< 45 minutes</td><td>Completes daily financial closing before 5:00 AM</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Resilience & Disaster Recovery (RTO / RPO)</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>High Availability (99.99%):</strong> Maximum unplanned downtime of under 52 minutes per year across cloud PMS and CRS.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Zero Transactional Loss (RPO = 0):</strong> Zero loss of reservations, room charges, or credit card tokens.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Rapid Recovery (RTO < 15 min):</strong> Automated failover of central booking engine in under 15 minutes.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div><strong>Offline Property Survivability:</strong> Property front-desk workstations and door lock encoders must operate for 24 hours during local ISP outages.</div></div>
      </div>
    </div>
    """,
    "notes": "Hospitality NFRs: door locks and front desks must work offline even during internet outages."
})

slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Regulatory & Data Sovereignty Mandates in Lodging",
    "subtitle": "Navigating GDPR, Thailand PDPA, Singapore PDPA, PCI-DSS Level 1, and Municipal Hotel Taxes",
    "content": """
    <div class="grid-3">
      <div class="glass-card" style="border-left: 3px solid #3b82f6;">
        <div class="card-header">Data Privacy Compliance</div>
        <p>• <strong>GDPR (Europe):</strong> Stringent rules on guest profiling, mini-bar consumption tracking, and DSAR requests.</p>
        <p>• <strong>Thailand PDPA (B.E. 2562):</strong> Mandatory consent for marketing communications across Bangkok headquarters.</p>
        <p>• <strong>Singapore PDPA:</strong> Strict prohibitions on storing unmasked NRIC/passport numbers in commercial CRM systems.</p>
      </div>
      <div class="glass-card" style="border-left: 3px solid #10b981;">
        <div class="card-header">Payment & Tokenization (PCI-DSS)</div>
        <p>• <strong>PCI-DSS v4.0 Level 1:</strong> Mandatory point-to-point encryption (P2PE) across front-desk chip-and-pin terminals.</p>
        <p>• <strong>OTA Virtual Credit Cards (VCC):</strong> Automated validation and activation rules to prevent expired card charge failures.</p>
      </div>
      <div class="glass-card" style="border-left: 3px solid #f59e0b;">
        <div class="card-header">Municipal Lodging Taxes</div>
        <p>• <strong>Transient Occupancy Tax (TOT):</strong> Automated municipal tax calculation across 150+ regional jurisdictions.</p>
        <p>• <strong>Tourist Police Registration:</strong> Daily automated electronic reporting of foreign guest passports to immigration authorities.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Architectural Solution: Tokenized Zero-Trust Enclaves</div>
      <p>Guest passport numbers and payment cards are tokenized at the edge. The central CRM and Data Cloud store only cryptographic hashes, ensuring that even a catastrophic database breach exposes zero usable guest PII.</p>
    </div>
    """,
    "notes": "Hotels hold sensitive guest data (passports, stays). Tokenization at the edge is mandatory."
})

slides.append({
    "part": "PART 2: REQUIREMENTS & CONSTRAINTS",
    "title": "Multi-Brand Portfolio & Ownership Complexity",
    "subtitle": "Architecting across Luxury, Lifestyle, Urban Business, and Extended Stay under different owner P&Ls",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Brand Operating Characteristics</div>
        <table class="data-table">
          <tr><th>Brand Tier</th><th>Guest Stay Length</th><th>Key Revenue Driver</th><th>Primary Tech Friction</th></tr>
          <tr><td>Luxury Resorts (Anantara)</td><td>4.8 Nights</td><td>F&B, Spas, Private Transfers</td><td>High personalization expectation; Opera silos</td></tr>
          <tr><td>Lifestyle Upscale (Avani)</td><td>2.1 Nights</td><td>Rooftop Bars, Social Events</td><td>Heavy OTA reliance (Agoda 35%); low direct share</td></tr>
          <tr><td>Extended Stay (Frasers)</td><td>24.5 Nights</td><td>Monthly Corporate Leases</td><td>Complex B2B RFP billing; resident preferences</td></tr>
          <tr><td>Urban Business (NH Hotels)</td><td>1.6 Nights</td><td>MICE Conferences, Business Hubs</td><td>GDS/TMC corporate compliance; rate parity</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Architectural Wedge: Multi-Tenant Data Cloud</div>
        <p>The enterprise architecture deploys <strong>Salesforce Data Cloud with Multi-Tenant Business Units</strong>:</p>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Global Guest Graph:</strong> Single unified identity graph recognizing Dr. Tan across luxury resorts and urban business hotels.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Partitioned Property P&Ls:</strong> Commercial marketing allocations and SaaS costs partitioned strictly by property asset owner code.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Brand-Specific Experiences:</strong> Anantara guests receive white-glove butler messaging; Avani guests receive rooftop DJ event alerts.</div></div>
      </div>
    </div>
    """,
    "notes": "Explain how multi-tenant business units allow a hotel group to serve different brands cleanly."
})

# PART 3: IT STANDARDS & ARCHITECTURAL GOVERNANCE (11-15)
slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "Enterprise Architecture Governance: TOGAF & C4 Model",
    "subtitle": "Structuring complex hospitality systems across Context, Container, Component, and Code tiers",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">C4 Architectural Hierarchy in Lodging</div>
        <div class="flow-step"><div class="step-num">L1</div><div><strong>Context Tier:</strong> Hotel Guests, Corporate Travel Managers, Front-Desk Agents, and OTAs interacting with Hotel Systems.</div></div>
        <div class="flow-step"><div class="step-num">L2</div><div><strong>Container Tier:</strong> Web/Mobile Booking Engines, MuleSoft API Gateways, Data Cloud, Opera PMS, and Snowflake Lakehouse.</div></div>
        <div class="flow-step"><div class="step-num">L3</div><div><strong>Component Tier:</strong> Room Availability Engine, Housekeeping Dispatcher, Identity Graph, and Agentforce Concierge.</div></div>
        <div class="flow-step"><div class="step-num">L4</div><div><strong>Code Tier:</strong> TypeScript microservices, Oracle OHIP REST API wrappers, and Model Context Protocol (MCP) JSON-RPC schemas.</div></div>
      </div>
      <div class="glass-card">
        <div class="card-header">HTNG & OpenTravel Interoperability Standards</div>
        <table class="data-table">
          <tr><th>Governance Body</th><th>Standard</th><th>Technical Application</th></tr>
          <tr><td>HTNG (Hospitality Tech Next Gen)</td><td>HTNG 2009B / Open Data Exchange</td><td>PMS to POS, Door Lock, and PBX integration</td></tr>
          <tr><td>OpenTravel Alliance (OTA)</td><td>OTA_HotelResNotifRQ / XML 2014B</td><td>Channel Manager to OTA reservation push</td></tr>
          <tr><td>Oracle OHIP</td><td>REST OpenAPI 3.0 Standard</td><td>Cloud PMS streaming APIs and webhooks</td></tr>
          <tr><td>W3C Web Authentication</td><td>Passkeys / FIDO2 Standard</td><td>Biometric room check-in on mobile web</td></tr>
        </table>
      </div>
    </div>
    """,
    "notes": "TOGAF and C4 hierarchy ensure every hotel component has clear architectural governance."
})

slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "API-First Architecture & Oracle OHIP Integration",
    "subtitle": "Connecting Oracle Hospitality Integration Platform (OHIP) to enterprise cloud microservices",
    "content": """
    <div class="grid-3">
      <div class="glass-card" style="border-top: 3px solid #3b82f6;">
        <div class="card-header">1. System APIs (Core PMS/CRS)</div>
        <p>• <strong>OHIP System API:</strong> Wraps Oracle Opera Cloud REST endpoints (reservations, room inventory, guest folios).</p>
        <p>• <strong>SynXis System API:</strong> Wraps Sabre SynXis CRS ARI distribution feeds.</p>
        <p>• <strong>Simphony System API:</strong> Wraps Oracle POS dining receipts and check details.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #10b981;">
        <div class="card-header">2. Process APIs (Orchestration)</div>
        <p>• <strong>Guest Check-In Process API:</strong> Orchestrates credit card pre-auth, room assignment, and digital key issuance.</p>
        <p>• <strong>Housekeeping Process API:</strong> Coordinates HotSOS room inspection with PMS inventory availability.</p>
        <p>• <strong>Dining Upsell Process API:</strong> Syncs SevenRooms table availability with guest arrival times.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #8b5cf6;">
        <div class="card-header">3. Experience APIs (Front-Ends)</div>
        <p>• <strong>Mobile Guest App API:</strong> Tailored JSON payloads for iOS/Android digital keys and room service.</p>
        <p>• <strong>Agentforce MCP API:</strong> Standardized tool execution schemas for autonomous AI concierge.</p>
        <p>• <strong>Corporate Portal API:</strong> B2B corporate negotiated rate booking and billing exports.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">MuleSoft Flex Gateway Policy Enforcement</div>
      <p>MuleSoft Flex Gateway enforces rate limiting, OAuth 2.0 token caching, and XML-to-JSON transformation at the edge, protecting legacy on-premise Opera 5.5 servers from being overwhelmed during flash sales.</p>
    </div>
    """,
    "notes": "Oracle OHIP is the modern standard for Opera Cloud. MuleSoft provides the 3-tier API layer."
})

slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "Event-Driven Architecture (EDA) & Room Status CDC",
    "subtitle": "Real-time Change Data Capture (CDC) streaming room, guest, and folio updates across properties",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Hospitality Event Streaming Topologies</div>
        <table class="data-table">
          <tr><th>Event Topic</th><th>Source System</th><th>Consumer Systems</th><th>Latency SLA</th></tr>
          <tr><td><code>room.housekeeping.inspected</code></td><td>HotSOS / Opera PMS</td><td>Data Cloud, Mobile Key Issuer, Front Desk</td><td>< 50 ms</td></tr>
          <tr><td><code>reservation.created</code></td><td>SynXis CRS / Brand.com</td><td>Data Cloud, Revenue Management, ERP</td><td>< 100 ms</td></tr>
          <tr><td><code>guest.door.unlocked</code></td><td>Assa Abloy NFC Lock</td><td>In-Room Lutron Lighting, Mini-bar IoT</td><td>< 15 ms</td></tr>
          <tr><td><code>pos.check.closed</code></td><td>Simphony POS / Toast</td><td>Opera PMS Folio, Loyalty Points Ledger</td><td>< 80 ms</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Dual-Tier Event Mesh (Kafka + Pub/Sub API)</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Confluent Cloud Kafka:</strong> Central high-throughput event backbone streaming 50,000+ reservation and room status events/second.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Salesforce Pub/Sub API (gRPC):</strong> Bi-directional Change Data Capture streaming guest profile updates between Data Cloud and property PMS.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Edge IoT MQTT Broker:</strong> Local lightweight broker managing in-room smart thermostats and door locks without cloud round-trips.</div></div>
      </div>
    </div>
    """,
    "notes": "Event streaming coordinates physical room readiness with digital key delivery."
})

slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "Zero-Trust Security & Identity Architecture",
    "subtitle": "Defense-in-depth security: CyberArk PAM, Okta CIAM, mTLS, and HSM Key Management",
    "content": """
    <div class="grid-3">
      <div class="glass-card">
        <div class="card-header">1. Identity & Access (IAM)</div>
        <p>• <strong>Okta Workforce Identity:</strong> SSO and adaptive MFA for 25,000+ hotel employees, front-desk staff, and night auditors.</p>
        <p>• <strong>Auth0 CIAM:</strong> Frictionless biometric passkey and Apple ID sign-in for 15M+ loyalty members on Brand.com.</p>
        <p>• <strong>Role-Based Access (RBAC):</strong> Strict separation between front-desk agents, housekeeping supervisors, and finance staff.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">2. Privileged Access (PAM)</div>
        <p>• <strong>CyberArk Enterprise:</strong> Dynamic credential rotation for all database administrators and cloud PMS super-users.</p>
        <p>• <strong>Session Recording:</strong> 100% keystroke and video recording of all remote maintenance access into on-premise hotel servers.</p>
        <p>• <strong>Zero Standing Privileges:</strong> Temporary time-limited access tokens for third-party PMS vendor technicians.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">3. Cryptographic Governance</div>
        <p>• <strong>HashiCorp Vault + HSM:</strong> FIPS 140-2 Level 3 hardware security modules protecting root encryption keys.</p>
        <p>• <strong>Salesforce Shield BYOK:</strong> Tenant-level encryption for all guest PII, passport copies, and special requests.</p>
        <p>• <strong>Zscaler Zero Trust:</strong> Direct-to-cloud private access eliminating corporate VPN vulnerabilities across property networks.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Zero-Trust Principle in Practice</div>
      <p>A night auditor in Bangkok cannot view the unmasked credit card of a guest staying in London; a marketing intern cannot export guest email addresses. Every query is evaluated dynamically based on user identity, device posture, and geolocation.</p>
    </div>
    """,
    "notes": "Hotels are prime targets for cyberattacks. CyberArk and Zero-Trust protect guest data."
})

slides.append({
    "part": "PART 3: IT STANDARDS & GOVERNANCE",
    "title": "Cloud PMS vs On-Premise Hybrid Architecture",
    "subtitle": "Navigating the multi-year transition from on-premise Opera 5.5 to Oracle Opera Cloud",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The Hybrid Migration Dilemma</div>
        <table class="data-table">
          <tr><th>Parameter</th><th>Legacy Opera 5.5 (On-Premise)</th><th>Oracle Opera Cloud (SaaS)</th></tr>
          <tr><td>Hosting Infrastructure</td><td>Physical server in hotel basement</td><td>Oracle Cloud Infrastructure (OCI)</td></tr>
          <tr><td>Integration Interface</td><td>Opera OXI XML / File Drop</td><td>OHIP REST OpenAPI 3.0 & Webhooks</td></tr>
          <tr><td>Upgrade Cycle</td><td>Multi-month manual upgrade projects</td><td>Continuous monthly cloud updates</td></tr>
          <tr><td>Hardware Maintenance</td><td>Local property server hardware CapEx</td><td>Zero local server footprint (Pure SaaS)</td></tr>
          <tr><td>Portfolio Footprint</td><td>~45% of properties (Gradual phase-out)</td><td>~55% of properties (Target: 100%)</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Architectural Solution: MuleSoft Hybrid Adapter</div>
        <p>To avoid waiting 4 years for all hotels to upgrade to Opera Cloud, the enterprise deploys <strong>MuleSoft Hybrid Connectors</strong>:</p>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Unified API Layer:</strong> Exposes identical REST API contracts to Data Cloud regardless of whether the property runs Opera 5.5 or Opera Cloud.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Protocol Translation:</strong> Automatically converts legacy OXI XML messages into modern JSON schemas in real time.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Zero Business Disruption:</strong> Upgrading a property from 5.5 to Cloud requires zero changes to the central CRM or marketing journeys.</div></div>
      </div>
    </div>
    """,
    "notes": "This hybrid adapter pattern is the exact architectural strategy that saves hotel groups tens of millions."
})

# PART 4: 13-LAYER ARCHITECTURE & VARIATIONS (16-20)
slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "13-Layer Architectural Topology Overview",
    "subtitle": "The complete enterprise stack from PMS core operations to guest digital touchpoints",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The 13 Enterprise Dimensions in Lodging</div>
        <table class="data-table">
          <tr><th>#</th><th>Layer Name</th><th>Core Hospitality Capability</th></tr>
          <tr><td>1</td><td>Core Operational Stack</td><td>PMS (Opera), CRS (SynXis), Channel Mgr, POS, Mobile Key</td></tr>
          <tr><td>2</td><td>Marketing Automation & AdTech</td><td>Guest journeys, dynamic packages, Google Hotel Ads</td></tr>
          <tr><td>3</td><td>CRM & Service Desk</td><td>Unified guest desktop, Amazon Connect CTI, WhatsApp concierge</td></tr>
          <tr><td>4</td><td>Loyalty Management</td><td>Hotel points ledger, tier progression, co-brand card sync</td></tr>
          <tr><td>5</td><td>Customer Data Platform (CDP)</td><td>Real-time ingestion, identity resolution, golden guest profile</td></tr>
          <tr><td>6</td><td>Integration & Event Mesh</td><td>MuleSoft OHIP connectors, Kafka streaming, Pub/Sub API</td></tr>
          <tr><td>7</td><td>Cloud & Lakehouse</td><td>Snowflake Data Cloud, Databricks Lakehouse, AWS Hyperforce</td></tr>
          <tr><td>8</td><td>AI & Agentic Systems</td><td>Agentforce concierge, HotSOS dispatch, dynamic pricing ML</td></tr>
          <tr><td>9</td><td>Web & Mobile Front-Ends</td><td>Next.js booking, native iOS/Android, Apple Wallet NFC keys</td></tr>
          <tr><td>10</td><td>Headless CMS & DAM</td><td>Contentful/AEM, Cloudinary DAM, 35+ language locales</td></tr>
          <tr><td>11</td><td>Finance & ERP</td><td>SAP S/4HANA, night audit reconciliation, Adyen acquiring</td></tr>
          <tr><td>12</td><td>HR & Workforce Scheduling</td><td>Workday HCM, UniFocus/HotSOS housekeeping dispatch</td></tr>
          <tr><td>13</td><td>Governance & Security</td><td>CyberArk PAM, HashiCorp Vault HSM, OneTrust privacy</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Architectural Cohesion Principles</div>
        <p><strong>System Boundaries:</strong> Core PMS/CRS manages inventory availability and guest folios; Data Cloud unifies guest preferences across properties; Agentforce executes autonomous concierge and housekeeping dispatch. Clean API boundaries prevent monolithic lock-in.</p>
        <div style="margin-top: 1rem;">
          <div class="card-header" style="color: #3b82f6;">Next Slides: The 3 Stack Variations</div>
          <p>We evaluate this 13-layer topology across 3 strategic variations: <strong>With Salesforce</strong>, <strong>Without Salesforce</strong>, and <strong>The Best Money Can Buy</strong>.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "Frame the 13 layers in the context of hotels."
})

slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "Variation 1: The Salesforce-Centric Ecosystem",
    "subtitle": "Unified guest data fabric and autonomous agentic workflows layered on Oracle Opera and Sabre SynXis",
    "content": """
    <div class="grid-3" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="metric-hero">$8.5M - $14.2M</div>
        <div class="metric-sub">Annual Software ACV</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">MuleSoft + Data Cloud + Agentforce + Service Cloud + Marketing Cloud.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #10b981;">10 Months</div>
        <div class="metric-sub">Payback Period</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Fastest time-to-value via pre-built Hospitality DMOs and OHIP connectors.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #8b5cf6;">340%</div>
        <div class="metric-sub">3-Year Projected ROI</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">$38M in cumulative benefits from direct booking recapture and upsell.</p>
      </div>
    </div>
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Core Stack Components</div>
        <p>• <strong>Data Cloud for Hospitality:</strong> Ingests Opera PMS and SynXis CRS events via MuleSoft; creates unified golden guest profiles with Zero-Copy Snowflake sharing.</p>
        <p>• <strong>Agentforce Hospitality Agent:</strong> Autonomous agents handling early check-in requests, room upgrades, and WhatsApp concierge.</p>
        <p>• <strong>Service Cloud Voice (Amazon Connect):</strong> Unified CTI telephony for Central Reservations (CRO) and front desk.</p>
        <p>• <strong>Marketing Cloud Engagement:</strong> Pre-arrival dining/spa upsell journeys and triggered post-stay review requests.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Primary Strategic Moat</div>
        <p><strong>Zero-Copy Guest Harmonization:</strong> Identifies 28% of anonymous OTA bookers as existing loyalty members, enabling direct re-capture. Pre-built MuleSoft OHIP connectors reduce integration timelines from 6 weeks to 3 days per property.</p>
      </div>
    </div>
    """,
    "notes": "Highlight the Salesforce advantage in hospitality: fast time-to-value and pre-built OHIP connectors."
})

slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "Variation 2: Composable Best-of-Breed (No Salesforce)",
    "subtitle": "Decoupled open cloud architecture: Snowflake, Braze, Zendesk, Talon.One, and Mews Cloud PMS",
    "content": """
    <div class="grid-3" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="metric-hero">$6.8M - $11.5M</div>
        <div class="metric-sub">Annual Software ACV</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Lower initial SaaS licensing costs; higher internal engineering payroll.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #10b981;">14 Months</div>
        <div class="metric-sub">Payback Period</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Requires custom data platform engineering and custom agent development.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #8b5cf6;">260%</div>
        <div class="metric-sub">3-Year Projected ROI</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">$30M cumulative benefits with complete architectural independence.</p>
      </div>
    </div>
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Core Stack Components</div>
        <p>• <strong>Snowflake & Databricks:</strong> Central analytical lakehouse with Apache Iceberg tables.</p>
        <p>• <strong>Twilio Segment / mParticle:</strong> Warehouse-native CDP with reverse ETL to operational systems.</p>
        <p>• <strong>Braze Enterprise:</strong> Streaming push/SMS/email messaging with sub-second delivery.</p>
        <p>• <strong>Zendesk Enterprise / Dynamics 365:</strong> Omni-channel service desk with Genesys Cloud CX.</p>
        <p>• <strong>Talon.One & OpenLoyalty:</strong> Headless rule-based promotion and loyalty engine.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Primary Strategic Moat</div>
        <p><strong>Zero Platform Lock-in:</strong> Complete developer autonomy. Every component is replaceable via open APIs. In-house AI engineering teams fine-tune custom LLM models on AWS Bedrock and Databricks Mosaic AI without paying SaaS platform markups.</p>
      </div>
    </div>
    """,
    "notes": "Explain the composable stack in hospitality: great for modern boutique groups, but requires custom engineering."
})

slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "Variation 3: The Best Platforms Money Can Buy",
    "subtitle": "Unconstrained budget, sovereign-grade pinnacle: Palantir Foundry, Adobe AEP, and Opera Cloud Dedicated",
    "content": """
    <div class="grid-3" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="metric-hero">$22.0M - $38.0M</div>
        <div class="metric-sub">Annual Software ACV</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">The apex of enterprise technology; sovereign dedicated deployments.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #10b981;">12 Months</div>
        <div class="metric-sub">Payback Period</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Rapid payback driven by massive casino high-roller spend capture and RevPAR uplift.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #8b5cf6;">450%</div>
        <div class="metric-sub">3-Year Projected ROI</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">$115M+ cumulative benefits via direct booking maximization and VIP retention.</p>
      </div>
    </div>
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Core Stack Components</div>
        <p>• <strong>Palantir Foundry & AIP:</strong> Integrated resort operational digital twin fusing casino gaming, dining, and hotel stays.</p>
        <p>• <strong>Adobe Experience Cloud (AEP + AJO + AEM):</strong> Sub-50ms streaming personalization globally.</p>
        <p>• <strong>Oracle Opera Cloud Premium Dedicated:</strong> 99.999% SLA with dedicated hardware isolation.</p>
        <p>• <strong>Lutron myRoom & Crestron:</strong> Integrated guestroom energy automation and smart glass touch panels.</p>
        <p>• <strong>Assa Abloy Allure Smart Glass:</strong> Apple Wallet NFC digital keys with Express Mode.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Primary Strategic Moat</div>
        <p><strong>Integrated Resort Omniscience:</strong> Palantir AIP coordinates VIP casino hosts, automated table comps, and suite allocations in real time; Adobe AEP captures $28M in direct luxury bookings; Lutron myRoom cuts utility bills by $3.5M annually.</p>
      </div>
    </div>
    """,
    "notes": "The ultra-tier stack is what Marina Bay Sands, Wynn, or luxury global groups deploy."
})

slides.append({
    "part": "PART 4: 13-LAYER ARCHITECTURE",
    "title": "Cross-Variation Financial & TCO Comparison Matrix",
    "subtitle": "Complete 3-year Total Cost of Ownership (TCO) breakdown across all 3 variations",
    "content": """
    <div class="glass-card">
      <table class="data-table">
        <tr><th>Cost / Value Dimension</th><th>Variation 1: With Salesforce</th><th>Variation 2: Without Salesforce</th><th>Variation 3: Best Money Can Buy</th></tr>
        <tr><td><strong>Annual Software Licensing (ACV)</strong></td><td>$11.2M / year</td><td>$9.1M / year</td><td>$29.5M / year</td></tr>
        <tr><td>Implementation CapEx (Year 1)</td><td>$14.0M</td><td>$16.5M (higher custom build)</td><td>$38.0M (sovereign custom build)</td></tr>
        <tr><td>Annual Internal Engineering Payroll</td><td>$3.8M / year (25 engineers)</td><td>$6.5M / year (42 engineers)</td><td>$11.0M / year (65 elite engineers)</td></tr>
        <tr><td>Annual Cloud Infra & Compute Run Cost</td><td>$1.4M / year</td><td>$2.8M / year (custom Spark/Kafka)</td><td>$6.2M / year (NVIDIA DGX clusters)</td></tr>
        <tr><td><strong>Total 3-Year TCO</strong></td><td><strong>$53.2M</strong></td><td><strong>$61.7M</strong></td><td><strong>$158.1M</strong></td></tr>
        <tr><td>Cumulative 3-Year Financial Benefit</td><td>$128.0M</td><td>$112.0M</td><td>$345.0M</td></tr>
        <tr><td><strong>Net Economic Value Generated</strong></td><td><strong>+$74.8M</strong></td><td><strong>+$50.3M</strong></td><td><strong>+$186.9M</strong></td></tr>
        <tr><td><strong>Time-to-Production-Value</strong></td><td><strong>10 Months</strong></td><td><strong>15 Months</strong></td><td><strong>12 Months</strong></td></tr>
      </table>
    </div>
    <div class="grid-2" style="margin-top: 1rem;">
      <div class="glass-card">
        <div class="card-header">The Hidden Engineering Payroll Trap</div>
        <p>While Variation 2 appears cheaper on software licensing ($9.1M vs $11.2M), it requires 17 additional data and integration engineers ($2.7M/year payroll), making its total 3-year TCO <strong>$8.5M higher</strong> than Variation 1.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Variation 3's Asymmetric Return</div>
        <p>Variation 3 costs nearly 3x more ($158.1M TCO), but generates <strong>$186.9M in net economic value</strong> by capturing high-roller casino gaming spend, optimizing room energy, and maximizing direct luxury ADR.</p>
      </div>
    </div>
    """,
    "notes": "Show the CFO the math. Cheap software with expensive custom engineering is the most expensive mistake in hospitality IT."
})

# PART 5: TOOL COMPLEMENTARITY & SYSTEM HANDOFFS (21-25)
slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "The Four Systems Framework in Hospitality",
    "subtitle": "Classifying enterprise tools across Record, Intelligence, Engagement, and Action",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header" style="color: #3b82f6;">1. System of Record (Source of Truth)</div>
        <p>• <strong>Oracle Opera Cloud / SynXis CRS:</strong> Master record for room inventory, rates, and guest folios.</p>
        <p>• <strong>SAP S/4HANA Finance:</strong> Master general ledger, city ledger, and night audit reconciliation.</p>
        <p>• <strong>Oracle Simphony POS:</strong> Master F&B dining checks and restaurant receipts.</p>
        <p>• <strong>Workday HCM:</strong> Master hotel employee, housekeeping, and front-desk staff records.</p>
      </div>
      <div class="glass-card">
        <div class="card-header" style="color: #10b981;">2. System of Intelligence (The Brain)</div>
        <p>• <strong>Salesforce Data Cloud / Snowflake:</strong> Unified Guest 360 data lakehouse.</p>
        <p>• <strong>IDeaS G3 RMS:</strong> Algorithmic dynamic room pricing and overbooking controls.</p>
        <p>• <strong>Palantir Foundry / AIP:</strong> Integrated resort guest ontology and VIP host decisioning.</p>
        <p>• <strong>Databricks Mosaic AI:</strong> Predictive guest cancellation and upsell propensity models.</p>
      </div>
      <div class="glass-card">
        <div class="card-header" style="color: #8b5cf6;">3. System of Engagement (The Interfaces)</div>
        <p>• <strong>Salesforce Service Cloud:</strong> Unified front-desk and central reservation agent desktop.</p>
        <p>• <strong>Marketing Cloud / Braze:</strong> Mobile push, email, SMS, and WhatsApp alerts.</p>
        <p>• <strong>Native iOS/Android Apps:</strong> Digital room key, dining ordering, and concierge chat.</p>
        <p>• <strong>In-Room Lutron / Crestron:</strong> Touchscreen room automation and smart lighting.</p>
      </div>
      <div class="glass-card">
        <div class="card-header" style="color: #f59e0b;">4. System of Action (Autonomous Execution)</div>
        <p>• <strong>Agentforce Atlas Engine:</strong> Autonomous multi-agent concierge and housekeeping dispatch.</p>
        <p>• <strong>MuleSoft Anypoint:</strong> Universal API execution and OHIP protocol translation.</p>
        <p>• <strong>Assa Abloy Mobile Access:</strong> Cryptographic NFC digital room key delivery to Apple Wallet.</p>
        <p>• <strong>Adyen Unified Commerce:</strong> Automated pre-authorization, folio settlement, and mobile pay.</p>
      </div>
    </div>
    """,
    "notes": "The Four Systems framework clarifies architecture: tools should not try to be everything to everyone."
})

slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "Detailed System Synergy & Hand-Off Matrix",
    "subtitle": "Mapping exact data hand-offs, triggers, and protocols between core lodging platforms",
    "content": """
    <div class="glass-card">
      <table class="data-table">
        <tr><th>Source Platform</th><th>Target Platform</th><th>Trigger Event</th><th>Protocol / Payload</th><th>Handoff Outcome</th></tr>
        <tr><td>Oracle Opera Cloud</td><td>MuleSoft ➔ Data Cloud</td><td>Reservation Created / Modified</td><td>OHIP REST / JSON CDC stream</td><td>Unified Guest profile updated in real-time</td></tr>
        <tr><td>Data Cloud</td><td>Marketing Cloud</td><td>Segment Membership Change</td><td>Native Zero-Copy Sync</td><td>Triggers personalized 72-hour pre-arrival upsell email</td></tr>
        <tr><td>HotSOS / Housekeeping</td><td>Opera PMS</td><td>Room Marked 'Inspected'</td><td>REST API / Webhook</td><td>Updates room status in PMS to 'Vacant / Ready'</td></tr>
        <tr><td>Opera PMS</td><td>Assa Abloy Mobile Access</td><td>Guest Checked-in & Room Ready</td><td>HTTPS REST / OAuth2</td><td>Provisions Apple Wallet NFC digital room key</td></tr>
        <tr><td>Simphony POS</td><td>Opera PMS Folio</td><td>Guest Signs Restaurant Check</td><td>HTNG POS Interface</td><td>Posts dining charges directly to guest room folio</td></tr>
        <tr><td>Data Cloud</td><td>Agentforce Concierge</td><td>Guest Arrives Early (T-3h)</td><td>gRPC / Pub/Sub API</td><td>Agentforce checks room readiness, offers luggage holding</td></tr>
        <tr><td>Opera Night Audit</td><td>SAP S/4HANA Finance</td><td>Daily Audit Completed</td><td>Daily Manager Report (DMR) JSON</td><td>Posts daily room revenue and tax accruals to General Ledger</td></tr>
      </table>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Architectural Principle: Event-Driven Handoffs</div>
      <p>All handoffs are <strong>event-driven</strong>, asynchronous, and mediated by enterprise integration layers (MuleSoft / Kafka), guaranteeing that a network glitch at one property never takes down central reservations.</p>
    </div>
    """,
    "notes": "Walk through the exact mechanics of how Opera, Data Cloud, HotSOS, and Assa Abloy collaborate."
})

slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "Data Contracts & Room State Transition Architecture",
    "subtitle": "Formalizing the room state machine from Dirty to Clean, Inspected, and Occupied",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Room State Machine Transitions</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>VACANT / DIRTY:</strong> Previous guest checked out; room queued for housekeeping in HotSOS.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>VACANT / CLEAN:</strong> Housekeeper finishes cleaning and updates status via mobile app.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>VACANT / INSPECTED:</strong> Floor supervisor inspects room and releases it into sellable inventory.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div><strong>OCCUPIED / DIRTY:</strong> Stayover guest in room; daily refresh queued for housekeeping.</div></div>
        <div class="flow-step"><div class="step-num">5</div><div><strong>OCCUPIED / CLEAN:</strong> Stayover room refreshed; mini-bar restocked.</div></div>
      </div>
      <div class="glass-card">
        <div class="card-header">Data Contract Schema (CloudEvents Avro)</div>
        <pre style="background: rgba(0,0,0,0.5); padding: 0.6rem; border-radius: 6px; font-size: 0.68rem; color: #93c5fd;"><code>{
  "specversion": "1.0",
  "type": "com.hotel.room.state_changed",
  "source": "/opera/bkk/property/001",
  "id": "ROOM-402-STATE-9912",
  "time": "2026-09-20T11:15:00Z",
  "datacontenttype": "application/json",
  "data": {
    "property_code": "AT_BKK",
    "room_number": "402",
    "previous_state": "VACANT_DIRTY",
    "new_state": "VACANT_INSPECTED",
    "assigned_guest_id": "GUEST-884920",
    "housekeeper_id": "HK-4421",
    "inspector_id": "SUP-1092"
  }
}</code></pre>
      </div>
    </div>
    """,
    "notes": "Room state transitions must be strict. A room cannot be occupied without passing through 'Inspected'."
})

slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "Real-Time Operational Handoff Sequence Diagram",
    "subtitle": "End-to-end trace of an automated early arrival, housekeeping priority dispatch, and mobile key delivery",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
sequenceDiagram
    autonumber
    participant G as Guest (Mobile App / WhatsApp)
    participant AF as Agentforce Hospitality Agent
    participant DC as Salesforce Data Cloud
    participant PMS as Oracle Opera Cloud
    participant HK as HotSOS Housekeeping
    participant AA as Assa Abloy Mobile Access

    G->>AF: "Hi, my flight landed early. Can I check in at 11:30 AM?"
    AF->>DC: Query Guest 360 (Tier: GHA Discovery Titanium, 42 Stays)
    AF->>PMS: Check assigned Room 402 status via OHIP
    PMS-->>AF: Status is "VACANT / DIRTY"
    AF->>HK: Dispatch priority cleaning rush order for Room 402
    AF->>G: "Welcome Dr. Tan! We are rushing Room 402. Enjoy a complimentary coffee at the lounge."
    HK->>PMS: Housekeeper finishes; Supervisor marks "VACANT / INSPECTED"
    PMS->>DC: Stream room.inspected CDC event via MuleSoft
    DC->>AF: Room 402 is ready
    AF->>AA: Request Apple Wallet NFC Digital Key for Room 402
    AA-->>AF: Key certificate generated
    AF->>G: Send WhatsApp with 1-click Apple Wallet Key download & elevator pass
      </div>
    </div>
    <div class="glass-card" style="margin-top: 0.8rem;">
      <p style="font-size: 0.75rem; color: var(--text-muted);"><strong>Outcome:</strong> The guest bypasses the front-desk queue completely, walks straight from the lounge to Room 402, and taps their iPhone to the door lock. Zero front-desk staff required.</p>
    </div>
    """,
    "notes": "Walk through this sequence. It solves the classic 'Dirty Room' early arrival dilemma autonomously."
})

slides.append({
    "part": "PART 5: TOOL COMPLEMENTARITY",
    "title": "Distributed State Consistency & Room Inventory Locking",
    "subtitle": "Preventing double-booking and rate discrepancies across simultaneous OTA and direct channels",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The Hospitality Inventory Dilemma</div>
        <p><strong>The Simultaneous Booking Problem:</strong> A traveler is booking the last Ocean Suite on Brand.com, while a guest in Tokyo books the same suite on Agoda, and a corporate travel agent on Sabre holds the room on GDS.</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #ef4444;">Consequences of Unmanaged Inventory</div>
          <p>• Catastrophic double-booking of specialty suites.<br>• Forced walk of VIP guests to competitor hotels ($1,500+ cost).<br>• Severe brand damage and negative TripAdvisor reviews.</p>
        </div>
      </div>
      <div class="glass-card">
        <div class="card-header">Architectural Solution: Redis Two-Phase Commit</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Distributed Redis Lock:</strong> The moment a checkout flow initiates on any channel, acquire a 10-minute hold on the specific room inventory block in SynXis CRS.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Two-Phase Commit (2PC):</strong> Phase 1: Verify credit card authorization with Adyen. Phase 2: Commit reservation in Opera PMS and broadcast zero-inventory update to SiteMinder.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Automated Release:</strong> If the guest abandons the shopping cart, the Redis lock expires after 10 minutes, instantly returning the room to sellable inventory.</div></div>
      </div>
    </div>
    """,
    "notes": "Distributed locking in SynXis CRS prevents double-booking across 450+ connected OTA channels."
})

# PART 6: DATA INGESTION, MODELING, SORTING & LAKEHOUSE (26-30)
slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Multi-Tier Ingestion Architecture in Hospitality",
    "subtitle": "Harmonizing 4 distinct ingestion velocities: Real-Time gRPC, Streaming CDC, Micro-Batch, and Batch ETL",
    "content": """
    <div class="grid-4" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="card-header">1. Real-Time gRPC</div>
        <div class="metric-hero" style="font-size: 1.2rem; color: #3b82f6;">< 15 ms</div>
        <p style="color: var(--text-muted);">Door lock NFC taps, in-room IoT energy sensors, and guest panic alarms.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">2. Streaming CDC (Kafka)</div>
        <div class="metric-hero" style="font-size: 1.2rem; color: #10b981;">< 80 ms</div>
        <p style="color: var(--text-muted);">Opera PMS room status changes, SynXis bookings, and POS dining checks.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">3. Micro-Batch (5-15 min)</div>
        <div class="metric-hero" style="font-size: 1.2rem; color: #8b5cf6;">5 - 15 min</div>
        <p style="color: var(--text-muted);">Credit card pre-authorizations and SevenRooms dining reservation updates.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">4. Batch ETL / Nightly</div>
        <div class="metric-hero" style="font-size: 1.2rem; color: #f59e0b;">Daily / 24h</div>
        <p style="color: var(--text-muted);">Opera Night Audit Daily Manager Reports, OTA commission statements, and payroll.</p>
      </div>
    </div>
    <div class="glass-card">
      <div class="card-header">Ingestion Flow Architecture</div>
      <p>All streaming sources feed into <strong>Confluent Cloud Kafka</strong> topics. Kafka streams raw JSON payloads into <strong>Salesforce Data Cloud</strong> for sub-second guest profile unification, while simultaneously sinking raw parquet data into the <strong>Snowflake Analytical Lakehouse</strong> via Kafka Connect Snowpipe Streaming.</p>
    </div>
    """,
    "notes": "Explain data velocity in hospitality. Door locks require sub-15ms; night audit is batch."
})

slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Domain Data Model Objects (DMOs) & Schemas",
    "subtitle": "Standardized canonical data models for hotel guest, reservation, room stay, and folio entities",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Core Hospitality DMO Entities</div>
        <table class="data-table">
          <tr><th>DMO Name</th><th>Key Attributes</th><th>Primary Relationships</th></tr>
          <tr><td><code>Individual</code></td><td>PartyId, FirstName, LastName, PassportHash, DateOfBirth</td><td>ContactPoints, LoyaltyAccounts</td></tr>
          <tr><td><code>HotelProperty</code></td><td>PropertyCode, BrandName, City, TotalRooms, StarRating</td><td>RoomInventories, StayBookings</td></tr>
          <tr><td><code>StayBooking</code></td><td>ConfirmationNumber, CheckInDate, CheckOutDate, RateCode</td><td>Individual, HotelProperty</td></tr>
          <tr><td><code>RoomStay</code></td><td>RoomNumber, RoomType, Status (Clean/Dirty/Inspected), ADR</td><td>StayBooking, HousekeepingTasks</td></tr>
          <tr><td><code>FolioCharge</code></td><td>TransactionId, ChargeCode, Amount, Tax, RevenueCenter</td><td>StayBooking, PointOfSaleChecks</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Calculated Insights & Real-Time Aggregations</div>
        <p>Data Cloud runs continuous real-time aggregations on top of DMOs to generate high-value operational metrics:</p>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Guest Lifetime Value (GLTV):</strong> 36-month total spend across rooms, dining, spa, and golf across all properties.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Ancillary Spend Propensity:</strong> Machine learning score predicting likelihood to book a spa treatment or private dinner.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>OTA Re-Capture Index:</strong> Probability that a guest who booked on Booking.com can be converted to Brand.com.</div></div>
      </div>
    </div>
    """,
    "notes": "Show the data model. DMOs standardize messy PMS and CRS formats into clean enterprise entities."
})

slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Identity Resolution: Deterministic vs Probabilistic",
    "subtitle": "Unifying fragmented anonymous browsing, OTA bookers, and loyalty profiles into a Golden Guest Record",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Identity Matching Hierarchy</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Tier 1: Deterministic Exact Match (100% Confidence):</strong> Loyalty Member Number + Last Name, or SHA-256 Hashed Passport Number.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Tier 2: Strong Semi-Deterministic Match (95% Confidence):</strong> Hashed Email Address + Mobile Phone Number (with country code).</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Tier 3: Probabilistic Fuzzy Match (80% Confidence):</strong> First Name + Last Name + Billing Postal Code + Credit Card Hash.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div><strong>Tier 4: Anonymous Session (Cookie / Device ID):</strong> Anonymous browsing on Brand.com until booking occurs.</div></div>
      </div>
      <div class="glass-card">
        <div class="card-header">The OTA Guest Re-Identification Miracle</div>
        <p><strong>The Problem:</strong> When a guest books an Anantara resort through Agoda, Agoda masks the guest's real email address, passing a temporary relay email (e.g. <code>guest.992@agoda-relay.com</code>).</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #10b981;">Data Cloud Resolution Engine</div>
          <p>Data Cloud matches the guest's <strong>First Name + Last Name + Mobile Phone Number</strong> entered during online check-in to their existing GHA Discovery profile, instantly merging the Agoda booking into the Golden Record and unlocking personalized VIP treatment.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "This is a massive commercial moat. Re-identifying OTA bookers allows hotels to reclaim the direct relationship."
})

slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Lakehouse Data Layering: Medallion Architecture",
    "subtitle": "Structuring hospitality big data across Bronze (Raw), Silver (Harmonized), and Gold (Business 360) tiers",
    "content": """
    <div class="grid-3">
      <div class="glass-card" style="border-top: 3px solid #f59e0b;">
        <div class="card-header">Bronze Tier (Raw Ingestion)</div>
        <p>• Unaltered append-only raw data lakes (S3 / GCS).</p>
        <p>• Stores raw Opera OXI XML messages, Simphony POS log files, and web clickstreams.</p>
        <p>• Retained for 7+ years for tax audit compliance and legal records.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #9ca3af;">
        <div class="card-header">Silver Tier (Cleaned & Harmonized)</div>
        <p>• Schema validated, deduplicated, and enriched.</p>
        <p>• Delta Lake / Iceberg tables matching canonical DMOs.</p>
        <p>• Room stays harmonized into unified stay records; multi-currency folios normalized to USD.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #eab308;">
        <div class="card-header">Gold Tier (Business & AI Ready)</div>
        <p>• Aggregated, feature-engineered tables for BI and ML.</p>
        <p>• Guest 360 view, property RevPAR/GOPPAR dashboards, and dynamic pricing feature stores.</p>
        <p>• Sub-second SQL querying via Snowflake and Databricks SQL.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Zero-Copy Federation: Bridging Gold to Salesforce</div>
      <p>Salesforce Data Cloud queries Snowflake Gold tables in-place using <strong>Zero-Copy Open Data Sharing</strong>. The CRM never copies terabytes of historical stay logs, eliminating data synchronization lag and storage egress fees.</p>
    </div>
    """,
    "notes": "Explain the Medallion architecture. Zero-copy federation between Snowflake Gold and Data Cloud is the holy grail."
})

slides.append({
    "part": "PART 6: DATA & LAKEHOUSE",
    "title": "Data Governance, Cataloging & Lineage",
    "subtitle": "End-to-end data tracking from hotel POS dining check to C-Suite corporate earnings reports",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Collibra Enterprise Data Catalog</div>
        <table class="data-table">
          <tr><th>Governance Pillar</th><th>Implementation</th><th>Regulatory Requirement</th></tr>
          <tr><td>Business Glossary</td><td>Standardized definitions for 800+ hospitality terms (e.g. RevPAR, GOPPAR, TRevPAR)</td><td>Eliminates owner reporting discrepancies</td></tr>
          <tr><td>Data Lineage</td><td>Visual DAG tracking data flow from Opera PMS through Kafka to SAP General Ledger</td><td>Mandatory for Sarbanes-Oxley (SOX) audit compliance</td></tr>
          <tr><td>Sensitive Data Tagging</td><td>Automated classification of PII, PCI, and passport attributes</td><td>Enforces GDPR and Singapore PDPA encryption rules</td></tr>
          <tr><td>Data Quality Scoring</td><td>Automated Great Expectations tests validating reservation completeness</td><td>Prevents dirty data from entering AI model training sets</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">Automated Data Lineage in Practice</div>
        <p>When the Chief Commercial Officer reviews the monthly revenue report showing a $3.8M RevPAR uplift, Collibra provides click-through lineage showing the exact 10 SQL transformations, 3 Kafka topics, and raw Opera PMS folios that produced that metric.</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #3b82f6;">Audit Defense Moat</div>
          <p>Reduces annual financial and owner audit preparation time from 4 weeks to 2 hours, saving $1.8M in external consulting audit fees.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "Data governance is what prevents multi-million-dollar SOX compliance failures."
})

# PART 7: END-TO-END CUSTOMER JOURNEYS (31-36)
slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 1: Search, Metasearch Bidding & Discovery",
    "subtitle": "Capturing traveler intent across Google Hotel Ads, Trivago, TripAdvisor, and Brand.com",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Google Hotel Ads Bidding Architecture</div>
        <p>• <strong>The Problem:</strong> OTAs spend billions bidding on branded hotel keywords on Google Hotel Ads. If an independent hotel does not bid, OTAs capture 100% of the traffic at 18% commission.</p>
        <p>• <strong>Architectural Solution:</strong> Deploy <strong>Koddi Enterprise AI</strong> connecting SynXis CRS ARI feeds directly to the Google Hotel Ads Price Match API.</p>
        <p>• <strong>Algorithmic Bidding:</strong> Bid aggressively (8%-10% CPA) on high-occupancy dates where direct yield is critical; suppress bids on sold-out dates.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 1: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Traveler searches "Luxury Resort Bangkok" on Google.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>Google Hotel Ads displays official Brand.com rate ($250) alongside OTA rates ($250).</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>Traveler clicks official direct rate deep-link into Next.js booking engine.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>Client-side SDK captures anonymous session cookie and registers intent topic in Kafka.</div></div>
      </div>
    </div>
    """,
    "notes": "Google Hotel Ads is the most critical digital battleground in hospitality today."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 2: Direct Booking, Dynamic Pricing & Upgrades",
    "subtitle": "Converting shoppers into booked guests with personalized room packages and one-click checkout",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">IDeaS G3 Algorithmic Pricing Engine</div>
        <p>• <strong>Dynamic Willingness-to-Pay:</strong> IDeaS G3 calculates optimal room rates by evaluating competitor rates, local city events, remaining inventory, and lead time.</p>
        <p>• <strong>Personalized Package Bundling:</strong> If the guest has a history of spa bookings, the booking engine dynamically offers an 'Indulgence Package' (Deluxe Suite + $100 Spa Credit) at a $320 rate.</p>
        <p>• <strong>One-Click Payment:</strong> Adyen Unified Commerce presents localized payment methods (Apple Pay, Google Pay, PromptPay in Thailand, GrabPay in Singapore).</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 2: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Traveler selects Deluxe Suite; IDeaS G3 dynamic rate applied ($320).</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>Agentforce recommends private airport limousine transfer based on flight arrival time.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>Traveler completes purchase with Apple Pay in 3 seconds.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>MuleSoft orchestrates simultaneous writes: SynXis CRS confirms booking; Opera PMS creates guest profile; Adyen settles deposit.</div></div>
      </div>
    </div>
    """,
    "notes": "Dynamic packaging and Apple Pay increase direct booking conversion by up to 22%."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 3: Pre-Arrival Engagement & F&B Upselling",
    "subtitle": "Automated 72-hour pre-arrival journeys: Dining reservations, spa treatments, and cabana rentals",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Automated Pre-Arrival Journey Trigger</div>
        <p>• <strong>T-72 Hours:</strong> Marketing Cloud sends personalized WhatsApp message: <em>"Sawadee khrap Dr. Tan, we look forward to welcoming you to Anantara. Would you like to reserve a sunset table at our Michelin-starred restaurant?"</em></p>
        <p>• <strong>SevenRooms Integration:</strong> Guest selects 7:30 PM table; SevenRooms confirms reservation and links it to the Opera PMS reservation record.</p>
        <p>• <strong>T-24 Hours:</strong> Mobile check-in opens. Automated push notification directs guest to native app for 1-click check-in and room preference selection (high floor, quiet room).</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 3: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Data Cloud triggers Marketing Cloud Journey Builder at exact T-72h timestamp.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>Guest reserves restaurant table via SevenRooms embedded mobile webview.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>At T-24h, guest completes mobile check-in on app; Opera PMS assigns Room 402.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>HotSOS queues pre-arrival VIP amenity (chilled champagne and fruit basket) for Room 402.</div></div>
      </div>
    </div>
    """,
    "notes": "Pre-arrival WhatsApp messaging drives $45+ in incremental on-property spend per guest."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 4: Arrival, Early Check-in & Apple Wallet Key",
    "subtitle": "Frictionless contactless arrival: Resolving dirty room status and delivering NFC room keys",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Apple Wallet NFC Digital Key Workflow</div>
        <p>• <strong>Express Mode:</strong> Guest taps iPhone or Apple Watch to door lock; door unlocks in < 300ms without waking device or opening an app. Works even if phone battery is dead.</p>
        <p>• <strong>The Early Arrival Dilemma:</strong> Guest arrives 3 hours before standard check-in. Room 402 is currently marked 'Dirty' in Opera PMS.</p>
        <p>• <strong>Automated Resolution:</strong> Agentforce alerts housekeeping via HotSOS to prioritize Room 402, offers complimentary lounge access, and delivers the digital key the instant the room is inspected.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 4: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Guest lands at airport; Agentforce detects early flight arrival via FlightAware API.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>HotSOS rushes Room 402 cleaning; Housekeeper completes cleaning at 11:45 AM.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>Opera PMS marks Room 402 'INSPECTED'; Assa Abloy issues Apple Wallet NFC key.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>Guest walks straight from taxi to Room 402, taps iPhone to unlock door. Front-desk queue completely bypassed.</div></div>
      </div>
    </div>
    """,
    "notes": "Apple Wallet room keys with Express Mode are the gold standard for luxury hotel arrivals."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 5: In-Stay Concierge & In-Room Automation",
    "subtitle": "Smart room IoT, in-stay WhatsApp butler requests, and real-time dining bill posting",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Lutron myRoom & In-Stay IoT Integration</div>
        <p>• <strong>Welcome Scene:</strong> Upon first door unlock, Lutron smart lighting automatically illuminates welcome scene, opens sheer curtains, and sets thermostat to 21°C.</p>
        <p>• <strong>Energy Setback:</strong> When guest leaves room, passive infrared (PIR) sensors detect vacancy and adjust HVAC by 2°C, saving 25% in guestroom energy consumption.</p>
        <p>• <strong>WhatsApp Butler Service:</strong> Guest messages via WhatsApp: <em>'Can we get two extra feather pillows and an iron?'</em> Agentforce routes ticket to Housekeeping via HotSOS in 2 seconds.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 5: Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>Assa Abloy door lock triggers MQTT event to Lutron myRoom gateway upon entry.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>Guest dines at resort restaurant; Simphony POS posts $185 check to Room 402 folio via HTNG interface.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>Guest requests extra pillows via WhatsApp; Agentforce logs HotSOS task for floor attendant.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>Attendant delivers pillows in 8 minutes; guest rates service 5-stars on automated WhatsApp prompt.</div></div>
      </div>
    </div>
    """,
    "notes": "Lutron energy automation saves millions in utility bills while elevating guest luxury."
})

slides.append({
    "part": "PART 7: CUSTOMER JOURNEYS",
    "title": "Phase 6: Express Checkout, Folio & Night Audit",
    "subtitle": "Contactless folio review, mobile payment settlement, loyalty point posting, and daily night audit",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Express Mobile Checkout Workflow</div>
        <p>• <strong>T-2 Hours to Checkout:</strong> Native mobile app displays itemized room folio (room rate, dining checks, mini-bar, tax).</p>
        <p>• <strong>1-Click Checkout:</strong> Guest clicks 'Approve & Check Out'; Adyen settles total balance against pre-authorized credit card.</p>
        <p>• <strong>Digital Key Revocation:</strong> Assa Abloy automatically deactivates Apple Wallet NFC key at 12:00 PM checkout time.</p>
        <p>• <strong>Loyalty Accrual:</strong> Points ledger posts 4,200 points to member account within 60 seconds of checkout.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Journey Step 6: Night Audit Technical Flow</div>
        <div class="flow-step"><div class="step-num">1</div><div>At 2:00 AM, Opera Cloud automated night audit executes daily financial rollover.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div>Reconciles all Simphony POS checks, Adyen credit card settlements, and OTA virtual cards.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div>Generates Daily Manager Report (DMR) JSON payload sent to SAP S/4HANA Finance.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div>Data Cloud updates Guest Lifetime Value (GLTV) and triggers post-stay TripAdvisor review email.</div></div>
      </div>
    </div>
    """,
    "notes": "Night audit closes the daily financial loop, reconciling POS, credit cards, and PMS."
})

# PART 8: BUSINESS PROCESS OPTIMIZATION & WORKFLOWS (37-41)
slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "Core Operational Process: As-Is vs To-Be Housekeeping",
    "subtitle": "Transforming manual paper-based room cleaning into an automated IoT-driven dispatch workflow",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header" style="color: #ef4444;">As-Is Process (Fragmented, Slow & Manual)</div>
        <p>• <strong>Morning Choke Point:</strong> Housekeeping supervisors spend 90 minutes printing paper assignment sheets for 60 room attendants.</p>
        <p>• <strong>Zero Real-Time Visibility:</strong> Attendants knock on doors blindly; stayover guests are disturbed; early checkout rooms sit dirty for hours.</p>
        <p>• <strong>Phone Call Bottlenecks:</strong> Attendants dial front desk via room phone to report clean rooms; front desk manually updates Opera PMS.</p>
        <p>• <strong>Result:</strong> Rooms are not ready until 4:00 PM; long front-desk queues; high guest frustration.</p>
      </div>
      <div class="glass-card">
        <div class="card-header" style="color: #10b981;">To-Be Process (HotSOS + IoT Automated Dispatch)</div>
        <p>• <strong>Dynamic Mobile Dispatch:</strong> Attendants carry smart mobile devices running HotSOS; rooms prioritized automatically by guest arrival time.</p>
        <p>• <strong>IoT PIR Sensors:</strong> In-room motion sensors alert attendant when guest leaves room, eliminating awkward door knocks.</p>
        <p>• <strong>1-Tap Status Updates:</strong> Attendant taps 'Clean'; supervisor inspects and taps 'Ready'; Opera PMS updates instantly via API.</p>
        <p>• <strong>Result:</strong> Rooms ready by 1:00 PM; front-desk queues eliminated; labor efficiency boosted by 18%.</p>
      </div>
    </div>
    """,
    "notes": "Housekeeping is the engine room of a hotel. Automating dispatch saves 18% in labor costs."
})

slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "Housekeeping Room Turnaround Workflow Gantt",
    "subtitle": "Standard 28-minute departure room cleaning cycle across luxury hotel standards",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
gantt
    title 28-Minute Departure Room Cleaning Cycle
    dateFormat mm
    axisFormat %M min

    section Stripping & Linen
    Strip Bedding & Towels       :a1, 00, 04m
    Trash Removal & Recycling    :a2, 02, 03m

    section Bathroom
    Deep Clean Shower & Tub      :b1, 05, 08m
    Sanitize Vanity & Mirrors    :b2, 10, 05m

    section Bedroom
    Make Luxury Bed (Triple Sheet):c1, 13, 07m
    Dust Surfaces & Electronics  :c2, 18, 04m

    section Final Touches
    Vacuum Carpet & Mop Tile     :d1, 22, 04m
    Restock Mini-Bar & Amenities :d2, 24, 03m
    Supervisor Digital Inspection:d3, 26, 02m
      </div>
    </div>
    <div class="glass-card" style="margin-top: 0.8rem;">
      <p style="font-size: 0.75rem; color: var(--text-muted);"><strong>Quality Standard:</strong> Forbes Travel Guide 5-Star inspection checklist (84 inspection points) completed on mobile tablet in 2 minutes, ensuring flawless standards before room release.</p>
    </div>
    """,
    "notes": "The Gantt chart illustrates the structured cleaning sequence required for luxury hospitality."
})

slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "Automated SLA Tracking & Escalation Matrix",
    "subtitle": "Real-time SLA monitoring across guest requests, engineering tickets, and room cleaning",
    "content": """
    <div class="glass-card">
      <table class="data-table">
        <tr><th>Service Request Category</th><th>Mandated SLA</th><th>Warning Threshold (Amber)</th><th>Breach Escalation (Red)</th><th>Compensation Policy</th></tr>
        <tr><td>Luggage Delivery to Room</td><td>Within 10 min of check-in</td><td>> 12 min</td><td>> 15 min (Alert Duty Mgr)</td><td>Complimentary welcome drink</td></tr>
        <tr><td>Extra Pillows / Linens</td><td>Within 15 min of request</td><td>> 18 min</td><td>> 25 min (Alert Housekeeping Mgr)</td><td>$25 F&B dining credit</td></tr>
        <tr><td>Room Service Breakfast</td><td>Within 30 min of order</td><td>> 35 min</td><td>> 45 min (Alert Executive Chef)</td><td>100% meal charge waived</td></tr>
        <tr><td>Engineering (AC / TV / Plumbing)</td><td>Within 20 min of report</td><td>> 25 min</td><td>> 35 min (Alert Chief Engineer)</td><td>$50 spa voucher or room move</td></tr>
        <tr><td>Express Checkout Folio Dispute</td><td>Within 5 min of inquiry</td><td>> 8 min</td><td>> 12 min (Alert Finance Mgr)</td><td>Immediate charge reversal</td></tr>
      </table>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Automated Service Recovery Engine</div>
      <p>If an engineering ticket breaches the 35-minute red threshold, Service Cloud automatically credits the guest's folio with a $50 service recovery voucher and alerts the General Manager to greet the guest in person, protecting online reviews.</p>
    </div>
    """,
    "notes": "Automated SLA tracking turns service failures into loyalty-building recovery moments."
})

slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "Workforce & Labor Scheduling Optimization",
    "subtitle": "Predictive labor modeling aligning staffing with forecasted occupancy and banqueting events",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The Labor Overtime Trap in Lodging</div>
        <p>• <strong>Volatile Occupancy:</strong> Hotel occupancy fluctuates from 45% on Sunday to 98% on Wednesday. Static shift schedules cause massive overstaffing on quiet days and severe overtime leakage on busy days.</p>
        <p>• <strong>Banqueting Volatility:</strong> A 500-person wedding banquet requires 40 additional servers for a 5-hour window. Miscalculating banquet staffing results in poor service or thousands in wasted labor payroll.</p>
        <p>• <strong>Cost of Inefficiency:</strong> Labor overtime consumes 4% to 7% of total payroll ($2.8M annually across 20 properties).</p>
      </div>
      <div class="glass-card">
        <div class="card-header">UniFocus + Workday Adaptive Labor Optimization</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Occupancy & Event Ingestion:</strong> Ingests 14-day rolling occupancy forecasts from Opera PMS and Delphi banquet schedules.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Mathematical Labor Modeling:</strong> Calculates exact required housekeeping hours and front-desk staffing per 15-minute interval.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Mobile Shift Bidding:</strong> Staff bid on open shifts via mobile app; eliminates overtime by matching available straight-time employees.</div></div>
        <div class="flow-step"><div class="step-num">4</div><div><strong>Result:</strong> Labor costs reduced by 4.2% while maintaining Forbes 5-star service standards ($3.5M saved).</div></div>
      </div>
    </div>
    """,
    "notes": "Labor optimization in hospitality is mathematically complex. Dynamic scheduling eliminates overtime."
})

slides.append({
    "part": "PART 8: PROCESS OPTIMIZATION",
    "title": "Preventive Engineering & Asset Lifecycle Management",
    "subtitle": "IoT-driven preventive maintenance for chillers, boilers, elevators, and kitchen equipment",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Hospitality Preventive Maintenance Matrix</div>
        <table class="data-table">
          <tr><th>Asset Category</th><th>IoT Monitoring Sensor</th><th>Inspection Cadence</th><th>Cost of Unplanned Failure</th></tr>
          <tr><td>Central HVAC Chillers</td><td>Vibration & Refrigerant Pressure Sensors</td><td>Continuous / 10 sec</td><td>$85,000 (Catastrophic mid-summer guest outage)</td></tr>
          <tr><td>Hot Water Boilers</td><td>Temperature & Pressure Relief Telemetry</td><td>Continuous / 1 min</td><td>$35,000 + 100 room refunds for cold showers</td></tr>
          <tr><td>Guestroom Door Locks</td><td>Battery Voltage & Motor Torque Telemetry</td><td>Daily automated scan</td><td>Guest locked out in hallway at 1:00 AM</td></tr>
          <tr><td>Kitchen Walk-in Freezers</td><td>Temperature Probe & Door Open Sensor</td><td>Continuous / 5 min</td><td>$25,000 in spoiled Wagyu beef and seafood</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">HotSOS Preventive Maintenance Engine</div>
        <p>HotSOS monitors asset operating hours and sensor telemetry. When a central chiller shows micro-vibrations indicating bearing wear, HotSOS automatically schedules maintenance during off-peak hours (Tuesday 2:00 AM).</p>
        <div style="margin-top: 0.8rem;">
          <div class="card-header" style="color: #10b981;">Asset ROI Moat</div>
          <p>Extends capital equipment operational lifespan by 4 years, deferring $12M in chiller and boiler replacement CapEx across the property portfolio.</p>
        </div>
      </div>
    </div>
    """,
    "notes": "Preventive maintenance saves millions in emergency repair CapEx and avoids guest disaster stories."
})

# PART 9: AI-ASSISTED EFFECTIVENESS & AGENTIC SYSTEMS (42-46)
slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "Agentic Reasoning Architecture: Atlas Engine vs LangGraph vs AIP",
    "subtitle": "Comparing the three leading enterprise agentic reasoning paradigms in hospitality",
    "content": """
    <div class="grid-3">
      <div class="glass-card" style="border-top: 3px solid #3b82f6;">
        <div class="card-header">Salesforce Agentforce (Atlas Engine)</div>
        <p>• <strong>Metadata-Grounded Reasoning:</strong> Autonomous decision loop operating against enterprise DMOs and hotel business policies.</p>
        <p>• <strong>Deterministic Guardrails:</strong> Salesforce Trust Layer prevents hallucinations; enforces OLS/FLS security.</p>
        <p>• <strong>Primary Use Case:</strong> Customer service deflection, pre-arrival concierge, room upgrades, and late checkout approvals.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #10b981;">
        <div class="card-header">Open Source (LangGraph / CrewAI)</div>
        <p>• <strong>Stateful Multi-Agent Graphs:</strong> Python-native cyclic graphs for complex custom workflows.</p>
        <p>• <strong>Custom Guardrails:</strong> NeMo Guardrails or Llama Guard; requires extensive custom engineering.</p>
        <p>• <strong>Primary Use Case:</strong> RAG over complex property compendiums, wine lists, and local city attraction guides.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #f59e0b;">
        <div class="card-header">Palantir AIP (Artificial Intelligence Platform)</div>
        <p>• <strong>Ontology-Driven Decisioning:</strong> Connects frontier LLMs directly to the integrated resort operational digital twin.</p>
        <p>• <strong>Deterministic Action Execution:</strong> Generates provably safe operational commands with human-in-the-loop approvals.</p>
        <p>• <strong>Primary Use Case:</strong> Integrated resort high-roller casino host orchestration and dynamic table allocations.</p>
      </div>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Architectural Synthesis</div>
      <p>Enterprises deploy a <strong>dual-agent strategy</strong>: Agentforce powers the commercial front-office (guest-facing messaging and concierge), while Palantir AIP or LangGraph powers back-office casino operations and yield management.</p>
    </div>
    """,
    "notes": "Clarify the difference between front-office agentic AI (Agentforce) and back-office operational AI (Palantir AIP)."
})

slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "Multi-Agent Orchestration Patterns & Task Handoffs",
    "subtitle": "How specialized autonomous agents collaborate during complex guest requests",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
flowchart TD
    A[Guest Inquiry via WhatsApp: 'I want a late checkout and anniversary dinner'] --> B[Supervisor Agent: Intent Classification]
    B --> C[Concierge Dining Agent]
    B --> D[Late Checkout & Billing Agent]
    B --> E[Housekeeping Dispatch Agent]

    C -->|Check Availability| F[(SevenRooms Dining API)]
    D -->|Check Occupancy & Rules| G[(Opera PMS / IDeaS RMS)]
    E -->|Update Cleaning Priority| H[(HotSOS Mobile System)]

    C & D & E --> I[Guest Response Generator]
    I -->|Unified Confirmation| J[Guest WhatsApp Channel]
      </div>
    </div>
    <div class="grid-2" style="margin-top: 0.8rem;">
      <div class="glass-card">
        <div class="card-header">Supervisor Agent Pattern</div>
        <p>The Supervisor Agent classifies complex multi-intent guest messages, splits them into separate tasks (Dining vs Billing vs Housekeeping), delegates to specialized agents in parallel, and presents a single polished response in under 3 seconds.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Prevents Agent Hallucination Cascades</div>
        <p>The Dining Agent cannot approve room late checkouts; the Billing Agent cannot modify restaurant reservations. Specialized agent boundaries guarantee absolute operational safety.</p>
      </div>
    </div>
    """,
    "notes": "Multi-agent architecture prevents single-agent prompt bloat. Specialization is the key to enterprise reliability."
})

slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "RAG Pipelines & Model Context Protocol (MCP)",
    "subtitle": "Connecting frontier LLMs (Claude 3.7) to real-time hotel systems using open JSON-RPC standards",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Model Context Protocol (MCP) in Hospitality</div>
        <p>• <strong>The Open Standard:</strong> MCP connects frontier AI models directly to hotel operational tools and databases without custom middleware wrappers.</p>
        <p>• <strong>Standardized MCP Tool Endpoints:</strong> Hotel systems expose clean JSON-RPC tools:</p>
        <div style="margin-top: 0.5rem; font-family: monospace; font-size: 0.7rem; color: #93c5fd;">
          • mcp-server-opera-pms (get_folio, update_late_checkout)<br>
          • mcp-server-sevenrooms (check_table, book_dining)<br>
          • mcp-server-hotsos (create_work_order, check_room_status)
        </div>
      </div>
      <div class="glass-card">
        <div class="card-header">MCP Tool Invocation Schema Example</div>
        <pre style="background: rgba(0,0,0,0.5); padding: 0.6rem; border-radius: 6px; font-size: 0.68rem; color: #a7f3d0;"><code>{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "approve_late_checkout",
    "arguments": {
      "property_code": "AT_BKK",
      "room_number": "402",
      "requested_time": "14:00",
      "waive_late_fee": true,
      "reason": "GHA_TITANIUM_BENEFIT"
    }
  },
  "id": "mcp-call-77412"
}</code></pre>
      </div>
    </div>
    """,
    "notes": "Model Context Protocol (MCP) is the future. It standardizes how LLMs talk to hotel tools."
})

slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "Predictive Machine Learning Models in Lodging",
    "subtitle": "Supervised, unsupervised, and reinforcement learning models deployed across revenue and guest operations",
    "content": """
    <div class="glass-card">
      <table class="data-table">
        <tr><th>ML Model Domain</th><th>Algorithm / Model Type</th><th>Input Features / Datasets</th><th>Inference Latency</th><th>Business Value</th></tr>
        <tr><td>Dynamic Room Pricing (IDeaS)</td><td>Reinforcement Learning (RL) + Econometric Choice</td><td>Competitor rates, pace of booking, local events, season</td><td>< 30 ms</td><td>+4.2% to +6.5% RevPAR outperformance ($24M)</td></tr>
        <tr><td>Guest Cancellation Prediction</td><td>Gradient Boosted Decision Trees (LightGBM)</td><td>Booking lead time, OTA vs direct, deposit status, history</td><td>< 50 ms</td><td>Optimizes overbooking controls, cutting empty rooms by 25%</td></tr>
        <tr><td>Room Upgrade Propensity</td><td>Random Forest Classification</td><td>Historical spend, loyalty tier, room category, length of stay</td><td>< 100 ms</td><td>Identifies top 15% of guests willing to buy suite upgrades</td></tr>
        <tr><td>F&B Table Demand Forecasting</td><td>Prophet Time-Series + XGBoost</td><td>Hotel occupancy, day of week, local holiday calendars</td><td>Daily Batch</td><td>Reduces restaurant food waste by 22% ($1.8M saved)</td></tr>
        <tr><td>Guest Review Sentiment Analysis</td><td>Fine-Tuned RoBERTa Transformer</td><td>TripAdvisor, Google, and post-stay survey text comments</td><td>Real-Time</td><td>Alerts GM to negative sentiment within 15 minutes of posting</td></tr>
      </table>
    </div>
    <div class="glass-card" style="margin-top: 1rem;">
      <div class="card-header">Model Governance & Drift Monitoring</div>
      <p>All production models are tracked in <strong>MLflow / Databricks Unity Catalog</strong> with continuous monitoring for concept drift (e.g. sudden macroeconomic currency drops invalidate historical pricing models). Retraining is triggered automatically.</p>
    </div>
    """,
    "notes": "Detail the ML models. Predictive models generate hundreds of millions in RevPAR and cost avoidance."
})

slides.append({
    "part": "PART 9: AI & AGENTIC SYSTEMS",
    "title": "AI Deflection Economics & ROI Business Case",
    "subtitle": "Quantifying the hard-dollar savings of generative AI guest service deflection",
    "content": """
    <div class="grid-3" style="margin-bottom: 1rem;">
      <div class="glass-card">
        <div class="metric-hero" style="color: #ef4444;">$4.80</div>
        <div class="metric-sub">Human Contact Cost</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Fully loaded cost of an 8-minute front-desk or phone interaction.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #10b981;">$0.18</div>
        <div class="metric-sub">Agentforce Cost</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">Consumption credit cost of autonomous conversational resolution.</p>
      </div>
      <div class="glass-card">
        <div class="metric-hero" style="color: #3b82f6;">96.2%</div>
        <div class="metric-sub">Servicing Cost Reduction</div>
        <p style="margin-top: 0.4rem; color: var(--text-muted);">$4.62 saved on every deflected interaction.</p>
      </div>
    </div>
    <div class="glass-card">
      <div class="card-header">Annual Deflection Savings Calculator (2.4M Inbound Contacts across Portfolio)</div>
      <table class="data-table">
        <tr><th>Inbound Contact Category</th><th>Annual Volume</th><th>Current Human Cost ($4.80)</th><th>Autonomous Deflection Rate</th><th>Deflected Contacts</th><th>Net Annual Savings</th></tr>
        <tr><td>Pre-Arrival Hotel Directions & Parking</td><td>650,000</td><td>$3,120,000</td><td>85%</td><td>552,500</td><td>$2,552,550</td></tr>
        <tr><td>Wi-Fi Password & Property Amenities</td><td>500,000</td><td>$2,400,000</td><td>92%</td><td>460,000</td><td>$2,125,200</td></tr>
        <tr><td>Housekeeping Requests (Towels/Iron)</td><td>450,000</td><td>$2,160,000</td><td>75%</td><td>337,500</td><td>$1,559,250</td></tr>
        <tr><td>Restaurant Reservations & Menus</td><td>420,000</td><td>$2,016,000</td><td>80%</td><td>336,000</td><td>$1,552,320</td></tr>
        <tr><td>Late Checkout & Folio Questions</td><td>380,000</td><td>$1,824,000</td><td>65%</td><td>247,000</td><td>$1,141,140</td></tr>
        <tr><td><strong>TOTALS</strong></td><td><strong>2,400,000</strong></td><td><strong>$11,520,000</strong></td><td><strong>80.5% (Blended)</strong></td><td><strong>1,933,000</strong></td><td><strong>+$8,930,460 / Year</strong></td></tr>
      </table>
    </div>
    """,
    "notes": "This table is the executive business case. Deflecting 80% of contacts saves $8.9M annually."
})

# PART 10: MASTER INTEGRATION & ROADMAP (47-52)
slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Master Integration Architecture Blueprint",
    "subtitle": "The end-to-end integration topology connecting all 13 enterprise layers in hospitality",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
flowchart LR
    subgraph Core["Core Systems of Record"]
        OPERA["Oracle Opera Cloud"]
        SYNXIS["Sabre SynXis CRS"]
        SIMPHONY["Oracle Simphony POS"]
        SAP["SAP S/4HANA Finance"]
    end

    subgraph Integration["Integration & Event Mesh"]
        MULE["MuleSoft Anypoint Platform"]
        KAFKA["Confluent Cloud Kafka"]
        HBRID["MuleSoft OHIP Connectors"]
    end

    subgraph DataAI["Data & Intelligence"]
        DC["Salesforce Data Cloud"]
        SNOW["Snowflake Lakehouse"]
        AF["Agentforce Atlas AI"]
        PAL["Palantir AIP Resort"]
    end

    subgraph Channels["Engagement Front-Ends"]
        WEB["Next.js Web / App"]
        APPLE["Apple Wallet NFC Key"]
        SVC["Service Cloud Voice"]
        MKT["Marketing Cloud"]
    end

    OPERA & SYNXIS & SIMPHONY & SAP --> MULE & KAFKA & HBRID
    MULE & KAFKA --> DC & SNOW
    DC --> AF & PAL
    AF & DC --> SVC & MKT & WEB & APPLE
      </div>
    </div>
    <div class="glass-card" style="margin-top: 0.8rem;">
      <p style="font-size: 0.75rem; color: var(--text-muted);"><strong>Decoupled Multi-Tier Topology:</strong> The integration layer completely insulates property PMS servers from web traffic surges, while Data Cloud feeds real-time guest context to Agentforce and external front-ends.</p>
    </div>
    """,
    "notes": "Walk through the master integration blueprint. This summarizes the entire enterprise topology."
})

slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Legacy Protocol Translation: Opera OXI & HTNG",
    "subtitle": "How MuleSoft and Kafka bridge 20-year-old XML protocols to modern JSON-RPC microservices",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">Legacy Protocol vs Modern Protocol Mapping</div>
        <table class="data-table">
          <tr><th>Legacy Hospitality Protocol</th><th>Modern Target Standard</th><th>Transformation Engine</th><th>Latency Impact</th></tr>
          <tr><td>Opera OXI XML (2009)</td><td>JSON-RPC 2.0 / REST OpenAPI 3.0</td><td>MuleSoft Opera OXI Connector</td><td>+10 ms</td></tr>
          <tr><td>HTNG 2009B POS Interface</td><td>CloudEvents JSON / Kafka Topic</td><td>MuleSoft HTNG Adapter</td><td>+14 ms</td></tr>
          <tr><td>OpenTravel XML (OTA_HotelRes)</td><td>GraphQL / Next.js Storefront API</td><td>MuleSoft GraphQL Gateway</td><td>+8 ms</td></tr>
          <tr><td>Assa Abloy Visionline CUE</td><td>Apple Wallet PKPass REST Service</td><td>MuleSoft Apple PassKit Connector</td><td>+12 ms</td></tr>
        </table>
      </div>
      <div class="glass-card">
        <div class="card-header">The Opera OXI XML Translation Example</div>
        <p>A room status change produces a legacy XML payload:</p>
        <pre style="background: rgba(0,0,0,0.5); padding: 0.5rem; border-radius: 4px; font-size: 0.65rem; color: #f87171;"><code><HotelRoomStatusNotifRQ>
  <HotelCode>AT_BKK</HotelCode>
  <RoomNumber>402</RoomNumber>
  <Status>INSPECTED</Status>
  <TimeStamp>2026-09-20T11:45:00Z</TimeStamp>
</HotelRoomStatusNotifRQ></code></pre>
        <p style="margin-top: 0.5rem;">MuleSoft transforms this into structured JSON in 3ms, triggering a mobile push to Dr. Tan: <em>"Your room 402 is ready! Tap to download your Apple Wallet key."</em></p>
      </div>
    </div>
    """,
    "notes": "Show the concrete code. Transforming legacy OXI XML into mobile push notifications demonstrates mastery."
})

slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Phase 1 & 2 Implementation Roadmap (Months 1–12)",
    "subtitle": "Foundational integration, Data Cloud deployment, and quick-win contact center deflection",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
gantt
    title Enterprise Hospitality Transformation: Year 1
    dateFormat MM
    axisFormat Month %m

    section Phase 1: Foundations
    MuleSoft OHIP & SynXis Integration  :p1_1, 01, 3M
    Kafka Event Mesh Deployment          :p1_2, 02, 3M
    Data Cloud Zero-Copy Ingestion       :p1_3, 03, 3M

    section Phase 2: Quick-Win Value
    Service Cloud Voice (Amazon Connect) :p2_1, 04, 3M
    Agentforce Tier-1 Concierge Agent    :p2_2, 06, 3M
    Marketing Cloud Dynamic Upsell       :p2_3, 07, 3M
    Apple Wallet Room Key Deployment     :p2_4, 09, 3M
      </div>
    </div>
    <div class="grid-2" style="margin-top: 1rem;">
      <div class="glass-card">
        <div class="card-header">Key Milestones: Phase 1 (Months 1–6)</div>
        <p>• Establish core MuleSoft API connectivity to Opera Cloud and SynXis CRS.<br>• Deploy Confluent Kafka event mesh across primary AWS regions.<br>• Harmonize initial 8M guest profiles in Salesforce Data Cloud.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Key Milestones: Phase 2 (Months 7–12)</div>
        <p>• Launch Agentforce Tier-1 concierge on WhatsApp and Mobile App (deflecting 50%+ calls).<br>• Activate pre-arrival dining/spa upsell journeys, generating $1.4M/month in incremental revenue.<br>• Deploy Apple Wallet NFC digital keys across first 20 luxury properties.</p>
      </div>
    </div>
    """,
    "notes": "A phased roadmap builds executive confidence. Phase 2 starts delivering hard-dollar ROI within 10 months."
})

slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Phase 3 & 4 Implementation Roadmap (Months 13–24)",
    "subtitle": "Full HotSOS IoT integration, sovereign resort lakehouse, and complete portfolio rollout",
    "content": """
    <div class="glass-card">
      <div class="mermaid">
gantt
    title Enterprise Hospitality Transformation: Year 2
    dateFormat MM
    axisFormat Month %m

    section Phase 3: Operations & IoT
    HotSOS Automated Housekeeping Dispatch:p3_1, 13, 4M
    Lutron myRoom Energy Integration     :p3_2, 15, 3M
    SevenRooms VIP Dining Synchronization:p3_3, 16, 4M

    section Phase 4: Sovereign AI
    Snowflake Sovereign Clean Rooms     :p4_1, 18, 4M
    Palantir AIP Resort Operations Twin :p4_2, 20, 5M
    Full Enterprise Cutover & Sign-Off   :p4_3, 23, 2M
      </div>
    </div>
    <div class="grid-2" style="margin-top: 1rem;">
      <div class="glass-card">
        <div class="card-header">Key Milestones: Phase 3 (Months 13–18)</div>
        <p>• Launch HotSOS automated housekeeping dispatch across all 540 properties.<br>• Integrate Lutron myRoom energy setback, reducing utility expenses by $3.5M.<br>• Connect SevenRooms dining reservation data directly to front-desk guest profiles.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Key Milestones: Phase 4 (Months 19–24)</div>
        <p>• Activate Snowflake Sovereign Clean Rooms for co-op marketing with luxury airlines.<br>• Deploy Palantir AIP integrated resort high-roller casino twin.<br>• Full operational handover to internal Hospitality CoE.</p>
      </div>
    </div>
    """,
    "notes": "Year 2 unlocks the advanced IoT, energy, and AI capabilities, achieving the full 340% to 450% ROI."
})

slides.append({
    "part": "PART 10: INTEGRATION & ROADMAP",
    "title": "Change Management: BCG 'People + Agents' Model",
    "subtitle": "Aligning hotel associates, operating models, and autonomous agents for sustainable transformation",
    "content": """
    <div class="grid-2">
      <div class="glass-card">
        <div class="card-header">The BCG 'People + Agents' Operating Model</div>
        <p>• <strong>The 85% Failure Gap:</strong> BCG research reveals that 85% of enterprise AI POCs fail to deliver production value because organizations treat AI as a technology project rather than an operating model redesign.</p>
        <p>• <strong>Human-in-the-Loop Supervision:</strong> Front-desk agents transition from data-entry clerks typing in credit cards to 'Experience Hosts', greeting guests warmly with personalized recommendations.</p>
        <p>• <strong>Prompt & Tool Engineering CoE:</strong> Establish an internal Center of Excellence dedicated to continuous prompt optimization, MCP tool evaluation, and safety guardrail governance.</p>
      </div>
      <div class="glass-card">
        <div class="card-header">Organizational Transformation Pillars</div>
        <div class="flow-step"><div class="step-num">1</div><div><strong>Role Evolution:</strong> Front-desk staff retrained as 'Guest Relationship Ambassadors', measured on guest satisfaction (NPS) rather than check-in speed.</div></div>
        <div class="flow-step"><div class="step-num">2</div><div><strong>Incentive Alignment:</strong> Front-desk bonuses tied to direct loyalty enrollments and F&B upsell revenue.</div></div>
        <div class="flow-step"><div class="step-num">3</div><div><strong>Safety & Ethics Board:</strong> Cross-functional committee (Legal, IT, Operations, GM) reviewing autonomous AI interactions bi-weekly.</div></div>
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
        <p>Deploy <strong>Salesforce Data Cloud + Agentforce</strong> for commercial agility, paired with <strong>Oracle Opera Cloud</strong> for core PMS and <strong>Palantir AIP</strong> for casino resorts.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #10b981;">
        <div class="card-header">Financial Return</div>
        <p><strong>3-Year Net Benefit: +$74.8M</strong><br>Payback achieved in 10 months via $8.9M annual servicing deflection and $18M direct booking recapture.</p>
      </div>
      <div class="glass-card" style="border-top: 3px solid #f59e0b;">
        <div class="card-header">Strategic Moat</div>
        <p>Transforms the hotel group from an OTA-dependent property manager into a high-margin travel retailer with industry-leading guest loyalty.</p>
      </div>
    </div>
    <div class="glass-card">
      <div class="card-header">Immediate Next Steps (30-Day Execution Plan)</div>
      <div class="flow-step"><div class="step-num">1</div><div><strong>Week 1–2:</strong> Form Enterprise Architecture Steering Committee and finalize Data Cloud DMO schemas.</div></div>
      <div class="flow-step"><div class="step-num">2</div><div><strong>Week 3:</strong> Authorize MuleSoft OHIP connector pilot on 5 test properties.</div></div>
      <div class="flow-step"><div class="step-num">3</div><div><strong>Week 4:</strong> Launch 30-day Agentforce WhatsApp deflection pilot for early arrival requests.</div></div>
    </div>
    """,
    "notes": "Close the presentation with a decisive, actionable call to action. The business case is indisputable."
})

# Render HTML and Markdown
out_html = os.path.join(BASE_DIR, "hotels", "presentation.html")
out_md = os.path.join(BASE_DIR, "hotels", "PRESENTATION_FRAMEWORK_COMPENDIUM.md")

# Apply visual enhancements (interactive charts, Mermaid architectures, CLI suites)
slides = vsc.apply_visual_enhancements("HOTELS", slides)

engine.render_reveal_html(meta, slides, out_html)
engine.render_presentation_markdown(meta, slides, out_md)

print("Hotels presentation generation complete. Total slides:", len(slides))
