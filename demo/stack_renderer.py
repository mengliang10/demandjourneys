#!/usr/bin/env python3
"""
Shared Stack Renderer for Travel & Hospitality Tech Stacks
Generates:
1. Interactive, responsive, dark-mode glassmorphism tech_stack.html
2. Dense, executive-grade ENTERPRISE_TECH_STACK_ARCHITECTURE_COMPENDIUM.md
"""

import os
import json

def render_markdown(data, output_path):
    md = []
    md.append(f"# {data['sector']} — Enterprise Tech Stack & Systems Architecture Compendium\n")
    md.append(f"> **Masterclass Compendium**: Comprehensive 13-layer enterprise technology and systems blueprint comparing **Variation 1 (With Salesforce)**, **Variation 2 (Without Salesforce / Best-of-Breed Modern Open)**, and **Variation 3 (The Best Platforms Money Can Buy / Ultra-Tier Sovereign Pinnacle)**.\n")
    
    md.append("## 1. Industry Scale & Economic Baseline\n")
    for k, v in data["market_context"].items():
        md.append(f"- **{k.replace('_', ' ').title()}**: {v}")
    md.append("\n---\n")

    md.append("## 2. Executive Summary: The Three Architectural Variations\n")
    for v in data["variations"]:
        md.append(f"### {v['name']}: {v['tagline']}")
        md.append(f"*{v['summary']}*\n")
        md.append(f"- **Annual Software Licensing (ACV)**: `{v['total_acv_usd']}`")
        md.append(f"- **Implementation CapEx**: `{v['implementation_capex_usd']}`")
        md.append(f"- **Annual Run Cost (Infra + Headcount)**: `{v['annual_run_cost_usd']}`")
        md.append(f"- **Projected 3-Year ROI**: `{v['projected_roi']}`")
        md.append(f"- **Primary Strategic Moat**: {v['primary_moat']}\n")

    md.append("---\n")
    md.append("## 3. 13-Layer Master Architectural Specifications\n")

    for layer in data["layers"]:
        md.append(f"### {layer['name']}")
        md.append(f"**Layer Scope & Capabilities**: {layer['desc']}\n")

        for var_key, var_title in [
            ("var_salesforce", "Variation 1: With Salesforce (Salesforce-Centric Enterprise Ecosystem)"),
            ("var_no_salesforce", "Variation 2: Without Salesforce (Best-of-Breed Modern Open/Enterprise)"),
            ("var_best_money_can_buy", "Variation 3: The Best Platforms Money Can Buy (Ultra-Tier Sovereign)")
        ]:
            stack = layer["variations"][var_key]
            md.append(f"#### {var_title}\n")
            md.append("**Core Platforms & Key Vendors**:")
            for p in stack["platforms"]:
                md.append(f"- **{p['name']}** (*Vendor*: `{p['vendor']}`): {p['role']}")
            
            md.append("\n**Financial Profile & Unit Economics**:")
            md.append(f"- **Annual Software Licensing (ACV)**: `{stack['licensing_acv']}`")
            md.append(f"- **Implementation CapEx**: `{stack['implementation_capex']}`")
            md.append(f"- **Annual Run Cost**: `{stack['annual_run_cost']}`\n")

            md.append("**Data Handled & Domain Schemas**:")
            md.append(f"{stack['data_handled']}\n")

            md.append("**Operational Purpose & Functional Role**:")
            md.append(f"{stack['purpose']}\n")

            md.append("**Business Value, ROI & Strategic Moat**:")
            md.append(f"{stack['business_value']}\n")

            md.append("**Integration Architecture, Protocols & Latency SLA**:")
            md.append(f"`{stack['integration_specs']}`\n")

        md.append("---\n")

    md.append("## 4. Comprehensive TCO & Financial Comparison Matrix\n")
    md.append("| Architectural Layer | Variation 1: With Salesforce | Variation 2: Without Salesforce | Variation 3: Best Money Can Buy |")
    md.append("| :--- | :--- | :--- | :--- |")
    for layer in data["layers"]:
        v1 = layer["variations"]["var_salesforce"]["licensing_acv"]
        v2 = layer["variations"]["var_no_salesforce"]["licensing_acv"]
        v3 = layer["variations"]["var_best_money_can_buy"]["licensing_acv"]
        md.append(f"| **{layer['name']}** | {v1} | {v2} | {v3} |")
    
    md.append("\n---\n")
    md.append("## 5. Architectural Synthesis & Decision Matrix\n")
    md.append("""
When deciding between these three enterprise variations, CIOs, CTOs, and Chief Commercial Officers evaluate four primary trade-offs:

1. **Time-to-Value vs. Custom Autonomy**:
   - *Variation 1 (With Salesforce)* provides the fastest time-to-value (9 to 12 months) via pre-built industry data model objects (DMOs), MuleSoft accelerators, and the native Agentforce Atlas reasoning engine.
   - *Variation 2 (Without Salesforce)* provides maximum autonomy and avoids platform lock-in, but requires an internal data platform engineering team to maintain custom Kafka streaming pipelines, identity resolution graphs, and LLM state machines.
   - *Variation 3 (Best Money Can Buy)* represents sovereign-grade operational superiority, delivering military-grade resilience, carrier-grade five-nines uptime, and sub-second multi-agent operational recovery.

2. **Integration Complexity & Technical Debt**:
   - Legacy industry protocols (e.g., EDIFACT in airlines, OXI in hotels, CUTE/CUSS at airports, NMEA/satellite at sea) require robust protocol translation.
   - MuleSoft (Var 1) encapsulates these protocols into reusable REST/JSON APIs; Confluent Kafka (Var 2) streams raw events for asynchronous consumption; Solace / Dedicated Confluent (Var 3) guarantees microsecond deterministic delivery under extreme network loads.

3. **Data Sovereignty & Privacy Mandates**:
   - All variations must strictly adhere to regional privacy regulations (GDPR in Europe, Singapore PDPA, Indonesia UU PDP, California CCPA, and PCI-DSS Level 1 for payment data).
   - Variation 1 utilizes Salesforce Shield and Hyperforce sovereign instances; Variation 2 utilizes HashiCorp Vault and Collibra; Variation 3 deploys CyberArk, HSM-backed encryption, and air-gapped sovereign cloud VPCs.
""")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"Successfully generated Markdown: {output_path}")


def render_html(data, js_data_var_name, js_file_relative_path, output_path):
    # Prepare HTML template with tokens
    raw_data_json = json.dumps(data)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['sector']} - Enterprise Tech Stack Architecture</title>
  
  <style>
    :root {{
      --bg-primary: #0b0f19;
      --bg-secondary: #111827;
      --bg-card: rgba(17, 24, 39, 0.75);
      --bg-card-hover: rgba(31, 41, 55, 0.9);
      --border-color: rgba(75, 85, 99, 0.35);
      --border-highlight: rgba(59, 130, 246, 0.5);
      --text-primary: #f9fafb;
      --text-secondary: #9ca3af;
      --text-muted: #6b7280;
      --accent-blue: #3b82f6;
      --accent-cyan: #06b6d4;
      --accent-purple: #8b5cf6;
      --accent-emerald: #10b981;
      --accent-orange: #f97316;
      --accent-amber: #f59e0b;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.5;
      min-height: 100vh;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(59, 130, 246, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(139, 92, 246, 0.08) 0%, transparent 40%);
      padding: 1.5rem 2rem 3rem;
    }}

    .container {{ max-width: 1400px; margin: 0 auto; }}
    
    .glass-panel {{
      background: var(--bg-card);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.5rem;
      transition: all 0.2s ease-in-out;
    }}
    .glass-panel:hover {{ border-color: var(--border-highlight); }}

    /* Top Nav */
    .top-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      padding: 0.85rem 1.25rem;
      margin-bottom: 2rem;
      border-radius: 10px;
      font-size: 0.88rem;
    }}
    .nav-links {{ display: flex; gap: 1.25rem; align-items: center; flex-wrap: wrap; }}
    .nav-link {{ color: var(--text-secondary); text-decoration: none; transition: color 0.2s; font-weight: 500; }}
    .nav-link:hover {{ color: #60a5fa; }}
    .nav-badge {{
      font-size: 0.72rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      background: rgba(59, 130, 246, 0.2);
      color: #93c5fd;
      border: 1px solid rgba(59, 130, 246, 0.35);
    }}

    /* Header */
    .header {{ text-align: center; margin-bottom: 2.5rem; }}
    .header h1 {{ font-size: 2.4rem; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 0.5rem; }}
    .header p {{ color: var(--text-secondary); font-size: 1.05rem; max-width: 900px; margin: 0 auto; }}

    /* Variation Selector Switcher */
    .variation-switch-container {{
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }}
    .var-btn {{
      background: rgba(17, 24, 39, 0.8);
      border: 2px solid var(--border-color);
      border-radius: 10px;
      padding: 1rem 1.5rem;
      cursor: pointer;
      color: var(--text-secondary);
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 0.35rem;
      width: 340px;
      text-align: left;
    }}
    .var-btn:hover {{
      border-color: rgba(255, 255, 255, 0.3);
      color: var(--text-primary);
      transform: translateY(-2px);
    }}
    .var-btn.active-salesforce {{
      border-color: #3b82f6;
      background: rgba(59, 130, 246, 0.15);
      color: #fff;
      box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
    }}
    .var-btn.active-no-salesforce {{
      border-color: #10b981;
      background: rgba(16, 185, 129, 0.15);
      color: #fff;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
    }}
    .var-btn.active-best-money {{
      border-color: #f59e0b;
      background: rgba(245, 158, 11, 0.15);
      color: #fff;
      box-shadow: 0 0 20px rgba(245, 158, 11, 0.3);
    }}
    .var-btn-title {{ font-weight: 700; font-size: 1rem; }}
    .var-btn-tagline {{ font-size: 0.78rem; opacity: 0.85; }}

    /* Variation Summary Card */
    .var-summary-card {{
      margin-bottom: 2rem;
      border-left: 4px solid var(--accent-blue);
      padding: 1.5rem;
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 2rem;
    }}
    @media (max-width: 900px) {{
      .var-summary-card {{ grid-template-columns: 1fr; }}
    }}
    .var-summary-metrics {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1rem;
      padding-left: 1.5rem;
      border-left: 1px solid var(--border-color);
    }}
    .metric-box {{
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }}
    .metric-label {{ font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; }}
    .metric-value {{ font-size: 1.15rem; font-weight: 700; color: #60a5fa; }}

    /* Filter Pills */
    .filter-bar {{
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
      align-items: center;
    }}
    .filter-pill {{
      background: rgba(31, 41, 55, 0.7);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      padding: 0.4rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .filter-pill:hover, .filter-pill.active {{
      background: #2563eb;
      color: #fff;
      border-color: #3b82f6;
    }}

    /* Layers Grid */
    .layers-container {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 3rem;
    }}
    .layer-card {{
      position: relative;
      overflow: hidden;
      transition: all 0.2s;
    }}
    .layer-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1.25rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border-color);
    }}
    .layer-title-box {{ display: flex; align-items: center; gap: 0.75rem; }}
    .layer-icon {{ font-size: 1.8rem; }}
    .layer-title {{ font-size: 1.25rem; font-weight: 700; }}
    .layer-desc {{ font-size: 0.82rem; color: var(--text-secondary); }}

    .layer-cost-badge {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(0, 0, 0, 0.4);
      padding: 0.4rem 0.8rem;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      font-size: 0.85rem;
    }}

    .layer-body {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }}
    @media (max-width: 900px) {{
      .layer-body {{ grid-template-columns: 1fr; }}
    }}

    .section-title {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      font-weight: 700;
      margin-bottom: 0.5rem;
    }}

    /* Platform Pills */
    .platforms-grid {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      margin-bottom: 1rem;
    }}
    .platform-item {{
      background: rgba(0, 0, 0, 0.3);
      padding: 0.6rem 0.85rem;
      border-radius: 6px;
      border-left: 3px solid #3b82f6;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
    }}
    .platform-name {{ font-weight: 600; color: #f9fafb; }}
    .platform-vendor {{ font-size: 0.75rem; color: var(--text-muted); }}
    .platform-role {{ font-size: 0.78rem; color: var(--text-secondary); }}

    /* Info Callouts */
    .info-box {{
      background: rgba(0, 0, 0, 0.25);
      padding: 0.85rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.75rem;
      font-size: 0.85rem;
      line-height: 1.5;
    }}
    .info-box p {{ color: var(--text-secondary); }}

    /* Side-by-side comparison table */
    .table-container {{ overflow-x: auto; margin-top: 1.5rem; }}
    table {{ width: 100%; border-collapse: separate; border-spacing: 0; font-size: 0.85rem; }}
    th {{
      background: rgba(31, 41, 55, 0.9);
      padding: 0.85rem 1rem;
      text-align: left;
      font-weight: 600;
      color: var(--text-secondary);
      border-bottom: 1px solid var(--border-color);
    }}
    td {{ padding: 0.85rem 1rem; border-bottom: 1px solid rgba(75, 85, 99, 0.2); vertical-align: top; }}
    tr:hover td {{ background: rgba(255, 255, 255, 0.02); }}

    .badge-var1 {{ color: #93c5fd; background: rgba(59, 130, 246, 0.15); padding: 0.2rem 0.5rem; border-radius: 4px; }}
    .badge-var2 {{ color: #a7f3d0; background: rgba(16, 185, 129, 0.15); padding: 0.2rem 0.5rem; border-radius: 4px; }}
    .badge-var3 {{ color: #fde68a; background: rgba(245, 158, 11, 0.15); padding: 0.2rem 0.5rem; border-radius: 4px; }}
  </style>
</head>
<body>

  <div class="container">
    
    <!-- Top Nav -->
    <div class="glass-panel top-nav">
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <span class="nav-badge">ENTERPRISE TECH STACK</span>
        <span style="font-weight: 600; color: #f9fafb;">{data['sector']}</span>
      </div>
      <div class="nav-links">
        <a href="index.html" class="nav-link">📊 Sector Distribution Lab</a>
        <a href="../index.html" class="nav-link">🏠 Masterclass Hub</a>
        <a href="ENTERPRISE_TECH_STACK_ARCHITECTURE_COMPENDIUM.md" class="nav-link" target="_blank">📄 Full Compendium MD</a>
        <a href="../hotels/tech_stack.html" class="nav-link">🏨 Hotels Stack</a>
        <a href="../airlines/tech_stack.html" class="nav-link">✈️ Airlines Stack</a>
        <a href="../cruises/tech_stack.html" class="nav-link">🚢 Cruises Stack</a>
        <a href="../tours/tech_stack.html" class="nav-link">🎒 Tours Stack</a>
      </div>
    </div>

    <!-- Header -->
    <header class="header">
      <span class="nav-badge" style="margin-bottom: 0.75rem; display: inline-block;">13-Layer Master Architecture</span>
      <h1>{data['sector']} Tech Stack & Systems Architecture</h1>
      <p>
        Exhaustive multi-layer architectural mapping across 13 enterprise dimensions: Core Operations, Marketing, CRM/Service, Loyalty, CDP, Integration, Cloud, AI/ML, Front-Ends, CMS/DXP, Finance, HR & Governance.
      </p>
    </header>

    <!-- Variation Switcher -->
    <div class="variation-switch-container">
      <button class="var-btn active-salesforce" id="btn-var-salesforce" onclick="setVariation('var_salesforce')">
        <span class="var-btn-title">Variation 1: With Salesforce</span>
        <span class="var-btn-tagline">Salesforce-Centric Enterprise Ecosystem</span>
      </button>
      <button class="var-btn" id="btn-var-no-salesforce" onclick="setVariation('var_no_salesforce')">
        <span class="var-btn-title">Variation 2: Without Salesforce</span>
        <span class="var-btn-tagline">Best-of-Breed Modern Open/Enterprise</span>
      </button>
      <button class="var-btn" id="btn-var-best-money" onclick="setVariation('var_best_money_can_buy')">
        <span class="var-btn-title">Variation 3: Best Money Can Buy</span>
        <span class="var-btn-tagline">Ultra-Tier Sovereign & High-Roller Pinnacle</span>
      </button>
    </div>

    <!-- Variation Summary Card -->
    <div class="glass-panel var-summary-card" id="var-summary-panel">
      <!-- Dynamic Content Populated by JS -->
    </div>

    <!-- Filter Pills -->
    <div class="filter-bar">
      <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; margin-right: 0.5rem;">FILTER LAYERS:</span>
      <button class="filter-pill active" onclick="filterLayers('all', this)">All 13 Layers</button>
      <button class="filter-pill" onclick="filterLayers('ops', this)">Core & Ops</button>
      <button class="filter-pill" onclick="filterLayers('commercial', this)">Commercial & CX</button>
      <button class="filter-pill" onclick="filterLayers('data_ai', this)">Data, Integration & AI</button>
      <button class="filter-pill" onclick="filterLayers('enterprise', this)">ERP, HR & Governance</button>
    </div>

    <!-- Layers Container -->
    <div class="layers-container" id="layers-container">
      <!-- Dynamic Layers Populated by JS -->
    </div>

    <!-- Side-by-Side Comparison Matrix -->
    <div class="glass-panel" style="margin-top: 3rem;">
      <h2 style="font-size: 1.35rem; font-weight: 700; margin-bottom: 0.5rem;">Side-by-Side Architectural & Financial Comparison</h2>
      <p style="color: var(--text-secondary); font-size: 0.85rem; margin-bottom: 1.5rem;">
        Complete cross-comparison of annual software licensing (ACV), key vendors, and data models across all 3 variations.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th style="width: 22%;">Layer & Dimension</th>
              <th style="width: 26%;">Variation 1: With Salesforce</th>
              <th style="width: 26%;">Variation 2: Without Salesforce</th>
              <th style="width: 26%;">Variation 3: Best Money Can Buy</th>
            </tr>
          </thead>
          <tbody id="comparison-table-body">
            <!-- Populated by JS -->
          </tbody>
        </table>
      </div>
    </div>

  </div>

  <script>
    const STACK_DATA = {raw_data_json};

    let currentVariation = 'var_salesforce';
    let currentCategory = 'all';

    function setVariation(varId) {{
      currentVariation = varId;
      
      document.getElementById('btn-var-salesforce').className = 'var-btn' + (varId === 'var_salesforce' ? ' active-salesforce' : '');
      document.getElementById('btn-var-no-salesforce').className = 'var-btn' + (varId === 'var_no_salesforce' ? ' active-no-salesforce' : '');
      document.getElementById('btn-var-best-money').className = 'var-btn' + (varId === 'var_best_money_can_buy' ? ' active-best-money' : '');

      renderSummary();
      renderLayers();
    }}

    function filterLayers(cat, btn) {{
      currentCategory = cat;
      document.querySelectorAll('.filter-pill').forEach(el => el.classList.remove('active'));
      btn.classList.add('active');
      renderLayers();
    }}

    function renderSummary() {{
      const varData = STACK_DATA.variations.find(v => v.id === currentVariation);
      const panel = document.getElementById('var-summary-panel');
      
      let borderAccent = '#3b82f6';
      if (currentVariation === 'var_no_salesforce') borderAccent = '#10b981';
      if (currentVariation === 'var_best_money_can_buy') borderAccent = '#f59e0b';
      panel.style.borderLeftColor = borderAccent;

      panel.innerHTML = `
        <div>
          <span class="nav-badge" style="margin-bottom: 0.5rem; display: inline-block;">${{varData.name}}</span>
          <h2 style="font-size: 1.35rem; font-weight: 700; margin-bottom: 0.5rem;">${{varData.tagline}}</h2>
          <p style="color: var(--text-secondary); font-size: 0.88rem; line-height: 1.5; margin-bottom: 1rem;">${{varData.summary}}</p>
          <div style="font-size: 0.8rem; color: #93c5fd;"><strong>Strategic Moat:</strong> ${{varData.primary_moat}}</div>
        </div>
        <div class="var-summary-metrics">
          <div class="metric-box">
            <span class="metric-label">Annual Software ACV</span>
            <span class="metric-value" style="color: ${{borderAccent}};">${{varData.total_acv_usd}}</span>
          </div>
          <div class="metric-box">
            <span class="metric-label">Implementation CapEx</span>
            <span class="metric-value">${{varData.implementation_capex_usd}}</span>
          </div>
          <div class="metric-box">
            <span class="metric-label">Annual Run Cost</span>
            <span class="metric-value">${{varData.annual_run_cost_usd}}</span>
          </div>
          <div class="metric-box">
            <span class="metric-label">Projected 3-Yr ROI</span>
            <span class="metric-value" style="color: #34d399;">${{varData.projected_roi}}</span>
          </div>
        </div>
      `;
    }}

    function renderLayers() {{
      const container = document.getElementById('layers-container');
      container.innerHTML = '';

      STACK_DATA.layers.forEach(layer => {{
        let match = false;
        if (currentCategory === 'all') match = true;
        if (currentCategory === 'ops' && ['core_ops'].includes(layer.layer_id)) match = true;
        if (currentCategory === 'commercial' && ['marketing', 'crm_service', 'loyalty', 'frontends', 'cms_dxp'].includes(layer.layer_id)) match = true;
        if (currentCategory === 'data_ai' && ['cdp', 'integration', 'cloud_data', 'ai_ml'].includes(layer.layer_id)) match = true;
        if (currentCategory === 'enterprise' && ['finance_erp', 'hr_workforce', 'governance'].includes(layer.layer_id)) match = true;

        if (!match) return;

        const stack = layer.variations[currentVariation];
        
        let borderAccent = '#3b82f6';
        if (currentVariation === 'var_no_salesforce') borderAccent = '#10b981';
        if (currentVariation === 'var_best_money_can_buy') borderAccent = '#f59e0b';

        let platformsHtml = stack.platforms.map(p => `
          <div class="platform-item" style="border-left-color: ${{borderAccent}};">
            <div>
              <div class="platform-name">${{p.name}}</div>
              <div class="platform-role">${{p.role}}</div>
            </div>
            <div class="platform-vendor">${{p.vendor}}</div>
          </div>
        `).join('');

        let card = document.createElement('div');
        card.className = 'glass-panel layer-card';
        card.innerHTML = `
          <div class="layer-header">
            <div class="layer-title-box">
              <span class="layer-icon">${{layer.icon}}</span>
              <div>
                <div class="layer-title">${{layer.name}}</div>
                <div class="layer-desc">${{layer.desc}}</div>
              </div>
            </div>
            <div class="layer-cost-badge">
              <span style="color: var(--text-muted); font-size: 0.75rem;">ACV:</span>
              <strong style="color: ${{borderAccent}};">${{stack.licensing_acv}}</strong>
            </div>
          </div>

          <div class="layer-body">
            <div>
              <div class="section-title">Core Platforms & Vendor Capabilities</div>
              <div class="platforms-grid">
                ${{platformsHtml}}
              </div>

              <div class="section-title" style="margin-top: 1rem;">Types of Data Handled</div>
              <div style="margin-bottom: 1rem;">
                <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.4;">${{stack.data_handled}}</p>
              </div>

              <div class="section-title">Cost & Economics</div>
              <div class="info-box">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.35rem;">
                  <span>Implementation CapEx:</span> <strong>${{stack.implementation_capex}}</strong>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span>Annual Run Cost:</span> <strong>${{stack.annual_run_cost}}</strong>
                </div>
              </div>
            </div>

            <div>
              <div class="section-title">Purpose & Operational Role</div>
              <div class="info-box">
                <p>${{stack.purpose}}</p>
              </div>

              <div class="section-title">Business Value, ROI & Strategic Moat</div>
              <div class="info-box" style="border-left: 3px solid #10b981;">
                <p>${{stack.business_value}}</p>
              </div>

              <div class="section-title">Integration Protocols & Latency SLA</div>
              <div class="info-box" style="border-left: 3px solid #8b5cf6;">
                <p style="font-family: monospace; font-size: 0.78rem;">${{stack.integration_specs}}</p>
              </div>
            </div>
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    function renderComparisonTable() {{
      const tbody = document.getElementById('comparison-table-body');
      tbody.innerHTML = '';

      STACK_DATA.layers.forEach(layer => {{
        const v1 = layer.variations['var_salesforce'];
        const v2 = layer.variations['var_no_salesforce'];
        const v3 = layer.variations['var_best_money_can_buy'];

        let row = document.createElement('tr');
        row.innerHTML = `
          <td>
            <strong>${{layer.icon}} ${{layer.name}}</strong>
            <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.2rem;">${{layer.desc}}</div>
          </td>
          <td>
            <div class="badge-var1" style="display: inline-block; margin-bottom: 0.35rem;">${{v1.licensing_acv}}</div>
            <div style="font-size: 0.8rem; color: #f9fafb; font-weight: 600;">${{v1.platforms.map(p => p.name).slice(0, 3).join(', ')}}</div>
            <div style="font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.3rem;">${{v1.purpose.substring(0, 100)}}...</div>
          </td>
          <td>
            <div class="badge-var2" style="display: inline-block; margin-bottom: 0.35rem;">${{v2.licensing_acv}}</div>
            <div style="font-size: 0.8rem; color: #f9fafb; font-weight: 600;">${{v2.platforms.map(p => p.name).slice(0, 3).join(', ')}}</div>
            <div style="font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.3rem;">${{v2.purpose.substring(0, 100)}}...</div>
          </td>
          <td>
            <div class="badge-var3" style="display: inline-block; margin-bottom: 0.35rem;">${{v3.licensing_acv}}</div>
            <div style="font-size: 0.8rem; color: #f9fafb; font-weight: 600;">${{v3.platforms.map(p => p.name).slice(0, 3).join(', ')}}</div>
            <div style="font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.3rem;">${{v3.purpose.substring(0, 100)}}...</div>
          </td>
        `;
        tbody.appendChild(row);
      }});
    }}

    setVariation('var_salesforce');
    renderComparisonTable();
  </script>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully generated HTML: {output_path}")
