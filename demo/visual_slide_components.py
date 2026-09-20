#!/usr/bin/env python3
"""
Visual Slide Components Generator for Travel & Hospitality Presentations
Generates rich, interactive, and densely packed visual assets:
- Chart.js interactive charts (TCO, Distribution Economics, Channel Share, Deflection)
- Plotly.js Sankey & Waterfall diagrams
- Mermaid.js C4 Architecture, Sequence, State Machine, Multi-Agent Swarms, Gantt charts
- Densely packed Open-Source CLI Tool architectures from OPEN_SOURCE_CLI_TOOLS_AND_APPLICATIONS_COMPENDIUM.md
- Cross-Industry Benchmarks from CROSS_INDUSTRY_ENTERPRISE_TECH_STACK_BENCHMARK.md
"""

def get_chart_js_script():
    """Returns Chart.js initialization script to handle Reveal.js slide transitions."""
    return """
    <script>
      function initPresentationCharts() {
        if (typeof Chart === 'undefined') return;
        Chart.defaults.color = '#94a3b8';
        Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.08)';
        Chart.defaults.font.family = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        if (window.Reveal) {
          Reveal.on('slidechanged', event => {
            const canvases = event.currentSlide.querySelectorAll('canvas');
            canvases.forEach(canvas => {
              if (canvas.initChart && !canvas.chartInstance) {
                canvas.chartInstance = canvas.initChart();
              } else if (canvas.chartInstance) {
                canvas.chartInstance.resize();
              }
            });
            if (window.mermaid) {
              mermaid.contentLoaded();
            }
          });
        }
      }
      document.addEventListener('DOMContentLoaded', initPresentationCharts);
    </script>
    """

def get_kpi_row(kpis):
    """Generates a top KPI metric ribbon."""
    boxes = []
    for val, lbl, delta, direction in kpis:
        dir_class = "up" if direction == "up" else "down"
        arrow = "▲" if direction == "up" else "▼"
        boxes.append(f"""
      <div class="kpi-box">
        <div class="kpi-value">{val}</div>
        <div class="kpi-label">{lbl}</div>
        <div class="kpi-delta {dir_class}">{arrow} {delta}</div>
      </div>""")
    return f"""<div class="kpi-row" style="flex: 0 0 auto; margin-bottom: 6px;">{''.join(boxes)}
</div>"""

def get_terminal_box(title, cmd, output, comment=None):
    """Generates a styled CLI terminal window from the Open-Source Compendium."""
    comment_html = f'<span class="comment"># {comment}</span><br>' if comment else ''
    return f"""
    <div class="terminal-box">
      <div class="terminal-header">
        <span class="terminal-dot red"></span>
        <span class="terminal-dot yellow"></span>
        <span class="terminal-dot green"></span>
        <span class="terminal-title">{title}</span>
      </div>
      <div class="terminal-body">
        {comment_html}<span class="prompt">$</span> <span class="cmd">{cmd}</span><br>
        <span class="output">{output}</span>
      </div>
    </div>"""

def get_bottom_banner(label, text, theme="blue"):
    """Generates a full-width strategic outcome bar that anchors the bottom of the slide."""
    return f"""
    <div class="bottom-banner {theme}" style="flex: 0 0 auto; margin-top: 6px;">
      <div><strong>{label}:</strong> {text}</div>
    </div>"""

def get_progress_bars(bars):
    """Generates gradient progress bars for percentages."""
    out = ['<div style="margin: 4px 0;">']
    for label, pct, color in bars:
        out.append(f"""
      <div style="display: flex; justify-content: space-between; font-size: 0.72rem; color: #94a3b8; margin-bottom: 2px;">
        <span>{label}</span><strong style="color: #f9fafb;">{pct}%</strong>
      </div>
      <div class="progress-bar"><div class="progress-fill {color}" style="width: {pct}%;">{pct}%</div></div>""")
    out.append('</div>')
    return '\n'.join(out)

def get_slide_2_chart(sector_code, metric_name, base_val, anc_val, frict_val, ebit_val):
    """Generates a visual revenue breakdown doughnut chart for Slide 2."""
    canvas_id = f"chart-rev-breakdown-{sector_code.lower()}"
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">Visual Revenue Breakdown & Margin Leakage</div>
        <div style="position: relative; flex: 1; min-height: 220px;">
          <canvas id="{canvas_id}"></canvas>
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">Macroeconomic Capital Allocation</div>
          <div style="margin-bottom: 0.6rem;">
            <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 2px;">
              <span>Base Product Revenue:</span>
              <strong style="color: #10b981;">${base_val}B</strong>
            </div>
            <div class="progress-bar"><div class="progress-fill green" style="width: 75%;">75%</div></div>
          </div>
          <div style="margin-bottom: 0.6rem;">
            <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 2px;">
              <span>High-Margin Ancillary Revenue:</span>
              <strong style="color: #8b5cf6;">${anc_val}B</strong>
            </div>
            <div class="progress-bar"><div class="progress-fill purple" style="width: 20%;">20%</div></div>
          </div>
          <div style="margin-bottom: 0.6rem;">
            <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 2px;">
              <span>Intermediary Distribution Friction:</span>
              <strong style="color: #ef4444;">${frict_val}B</strong>
            </div>
            <div class="progress-bar"><div class="progress-fill red" style="width: 15%;">15%</div></div>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 2px;">
              <span>Net Enterprise Operating Profit (EBIT):</span>
              <strong style="color: #38bdf8;">${ebit_val}B</strong>
            </div>
            <div class="progress-bar"><div class="progress-fill blue" style="width: 10%;">10%</div></div>
          </div>
        </div>
        <div style="padding: 6px 10px; background: rgba(56, 189, 248, 0.08); border-left: 3px solid #38bdf8; border-radius: 4px; font-size: 0.76rem;">
          <strong>Strategic Takeaway:</strong> Ancillary spend represents over 100% of net industry operating profit. Shifting 5% of intermediated volume to direct digital channels eliminates friction and doubles enterprise EBITDA.
        </div>
      </div>
    </div>
    <script>
      (function() {{
        const canvas = document.getElementById('{canvas_id}');
        if (!canvas) return;
        canvas.initChart = function() {{
          return new Chart(canvas, {{
            type: 'doughnut',
            data: {{
              labels: ['Base Revenue (${base_val}B)', 'Ancillary Revenue (${anc_val}B)', 'Distribution Friction (${frict_val}B)', 'Net Operating Profit (${ebit_val}B)'],
              datasets: [{{
                data: [{base_val}, {anc_val}, {frict_val}, {ebit_val}],
                backgroundColor: ['#10b981', '#8b5cf6', '#ef4444', '#38bdf8'],
                borderColor: '#0b0f19',
                borderWidth: 2,
                hoverOffset: 6
              }}]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{
                  position: 'bottom',
                  labels: {{ color: '#cbd5e1', font: {{ size: 10 }}, boxWidth: 12, padding: 6 }}
                }}
              }},
              cutout: '65%'
            }}
          }});
        }};
        document.addEventListener('DOMContentLoaded', () => {{
          if (canvas.offsetParent !== null) canvas.chartInstance = canvas.initChart();
        }});
      }})();
    </script>
    """

def get_slide_3_waterfall(sector_code, gross_fare, direct_share, ota_share, friction_amount, net_retained, ebit):
    """Generates an interactive visual waterfall/distribution friction graphic for Slide 3."""
    canvas_id = f"chart-waterfall-{sector_code.lower()}"
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">Passenger Journey Unit Economics & Margin Waterfall</div>
        <div style="position: relative; flex: 1; min-height: 220px;">
          <canvas id="{canvas_id}"></canvas>
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">Friction Analysis: The ${friction_amount} Toll Barrier</div>
          <p style="font-size: 0.82rem; margin-bottom: 0.6rem;">Every transaction carries an unavoidable toll to legacy GDS, OTAs, payment gateways, and reservation fees:</p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 0.6rem;">
            <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); padding: 8px; border-radius: 6px;">
              <div style="color: #f87171; font-weight: 700; font-size: 1.1rem;">-${friction_amount}</div>
              <div style="font-size: 0.7rem; color: #94a3b8;">Intermediary Toll / Booking</div>
            </div>
            <div style="background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3); padding: 8px; border-radius: 6px;">
              <div style="color: #38bdf8; font-weight: 700; font-size: 1.1rem;">+${ebit}</div>
              <div style="font-size: 0.7rem; color: #94a3b8;">Final Operating Profit (EBIT)</div>
            </div>
          </div>
          <p style="font-size: 0.8rem; color: #cbd5e1;">
            <strong>The 85% Leaked Profit Trap:</strong> Intermediary friction (${friction_amount}) consumes nearly <strong>85%</strong> of total net operating profit (${ebit}). Shifting bookings to Direct Brand.com captures immediate margin lift.
          </p>
        </div>
        <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 0.4rem;">
          <span class="pill pill-blue">Direct Share: {direct_share}%</span>
          <span class="pill pill-amber">OTA / GDS Share: {ota_share}%</span>
          <span class="pill pill-green">Net Retained: ${net_retained}</span>
        </div>
      </div>
    </div>
    <script>
      (function() {{
        const canvas = document.getElementById('{canvas_id}');
        if (!canvas) return;
        canvas.initChart = function() {{
          return new Chart(canvas, {{
            type: 'bar',
            data: {{
              labels: ['Gross Fare', 'Intermediary Friction', 'Net Revenue', 'OpEx', 'Operating EBIT'],
              datasets: [{{
                label: 'Unit Economics ($)',
                data: [{gross_fare}, -{friction_amount}, {net_retained}, -{round(float(net_retained) - float(ebit), 2)}, {ebit}],
                backgroundColor: ['#3b82f6', '#ef4444', '#10b981', '#f59e0b', '#06b6d4'],
                borderRadius: 4
              }}]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{ legend: {{ display: false }} }},
              scales: {{
                y: {{
                  grid: {{ color: 'rgba(255, 255, 255, 0.05)' }},
                  ticks: {{ color: '#94a3b8', font: {{ size: 9 }} }}
                }},
                x: {{
                  grid: {{ display: false }},
                  ticks: {{ color: '#cbd5e1', font: {{ size: 9 }} }}
                }}
              }}
            }}
          }});
        }};
        document.addEventListener('DOMContentLoaded', () => {{
          if (canvas.offsetParent !== null) canvas.chartInstance = canvas.initChart();
        }});
      }})();
    </script>
    """

def get_slide_4_channel_chart(sector_code, direct_pct, ndc_pct, gds_pct, ota_pct):
    """Generates an interactive Channel Share comparison chart for Slide 4."""
    canvas_id = f"chart-channel-share-{sector_code.lower()}"
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">Channel Distribution Share & Cost Dynamics</div>
        <div style="position: relative; flex: 1; min-height: 220px;">
          <canvas id="{canvas_id}"></canvas>
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">The Unit Cost Economics by Channel</div>
          <table class="data-table" style="margin-bottom: 0.6rem;">
            <tr><th>Channel</th><th>Share</th><th>Cost / Booking</th><th>Ancillary Attach</th></tr>
            <tr><td><strong style="color: #10b981;">Direct Digital</strong></td><td>{direct_pct}%</td><td>$0.20 - $0.45</td><td>34.0% (High)</td></tr>
            <tr><td><strong style="color: #8b5cf6;">Modern API / NDC</strong></td><td>{ndc_pct}%</td><td>$0.80 - $1.50</td><td>18.5% (Medium)</td></tr>
            <tr><td><strong style="color: #f59e0b;">Legacy GDS</strong></td><td>{gds_pct}%</td><td>$4.50 - $6.50</td><td>8.0% (Low)</td></tr>
            <tr><td><strong style="color: #ef4444;">OTA Resellers</strong></td><td>{ota_pct}%</td><td>18% - 25% GBV</td><td>4.2% (Very Low)</td></tr>
          </table>
          <p style="font-size: 0.8rem; color: #cbd5e1;">
            <strong>The Architectural Mandate:</strong> Direct digital booking delivers <strong>12x lower transaction costs</strong> and <strong>4.2x higher ancillary attachment</strong> than legacy GDS/OTA channels.
          </p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 6px; padding: 6px 10px; font-size: 0.76rem;">
          <strong style="color: #a7f3d0;">Value Realization Formula:</strong> Shifting 10% of bookings from OTAs to Direct captures an incremental $18M - $32M in pure EBITDA annually.
        </div>
      </div>
    </div>
    <script>
      (function() {{
        const canvas = document.getElementById('{canvas_id}');
        if (!canvas) return;
        canvas.initChart = function() {{
          return new Chart(canvas, {{
            type: 'bar',
            data: {{
              labels: ['Direct Digital', 'Modern API / NDC', 'Legacy GDS', 'OTAs & Resellers'],
              datasets: [
                {{
                  label: 'Channel Share (%)',
                  data: [{direct_pct}, {ndc_pct}, {gds_pct}, {ota_pct}],
                  backgroundColor: '#3b82f6',
                  borderRadius: 4
                }},
                {{
                  label: 'Ancillary Attach (%)',
                  data: [34.0, 18.5, 8.0, 4.2],
                  backgroundColor: '#10b981',
                  borderRadius: 4
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{
                  position: 'top',
                  labels: {{ color: '#cbd5e1', font: {{ size: 9 }}, boxWidth: 10 }}
                }}
              }},
              scales: {{
                y: {{
                  grid: {{ color: 'rgba(255, 255, 255, 0.05)' }},
                  ticks: {{ color: '#94a3b8', font: {{ size: 9 }} }}
                }},
                x: {{
                  grid: {{ display: false }},
                  ticks: {{ color: '#cbd5e1', font: {{ size: 9 }} }}
                }}
              }}
            }}
          }});
        }};
        document.addEventListener('DOMContentLoaded', () => {{
          if (canvas.offsetParent !== null) canvas.chartInstance = canvas.initChart();
        }});
      }})();
    </script>
    """

def get_slide_11_c4_mermaid(sector_title, core_sys):
    """Generates C4 Context and Container Model for Slide 11."""
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">C4 Architecture Model: Context & Container Topology</div>
        <div class="mermaid" style="flex: 1;">
graph TB
  subgraph C1 ["Context Tier (L1)"]
    U["Customer / Frontline Guest / Travel Advisor"]
    E["Enterprise Travel & Operations Ecosystem"]
  end
  subgraph C2 ["Container Tier (L2)"]
    W["Web & Native Mobile (Next.js / Swift)"]
    API["Universal API Gateway (MuleSoft / Envoy)"]
    EVENT["Event Streaming Backbone (Kafka / Flink)"]
    CORE["Core Reservation & Operations ({core_sys})"]
    DATA["Data Cloud & Lakehouse (Iceberg / Snowflake)"]
    AGENT["Agentic Reasoning Fabric (Atlas Engine)"]
  end
  U --> W
  W --> API
  API --> EVENT
  EVENT --> CORE
  EVENT --> DATA
  DATA --> AGENT
  AGENT --> API
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">C4 Architectural Governance Standards</div>
          <table class="data-table" style="margin-bottom: 0.6rem;">
            <tr><th>C4 Level</th><th>Scope</th><th>Target Audience</th><th>Governance Standard</th></tr>
            <tr><td><strong>Level 1: Context</strong></td><td>System Boundaries & Actors</td><td>Board & C-Suite</td><td>TOGAF Enterprise Metamodel</td></tr>
            <tr><td><strong>Level 2: Container</strong></td><td>Apps, Data Stores, Microservices</td><td>Enterprise Architects</td><td>Cloud-Native CNCF Reference</td></tr>
            <tr><td><strong>Level 3: Component</strong></td><td>Class Modules, APIs, Schedulers</td><td>Lead Engineers</td><td>OpenAPI 3.1 / AsyncAPI</td></tr>
            <tr><td><strong>Level 4: Code</strong></td><td>Entity Models, State Machines</td><td>Software Developers</td><td>Clean Architecture / TDD</td></tr>
          </table>
          <p style="font-size: 0.8rem; color: #cbd5e1;">
            <strong>Architectural Tenet:</strong> Clean separation between L1 Context (business actors) and L2 Containers (runtime topologies) guarantees that changes to the core PSS/PMS do not ripple into guest-facing digital channels.
          </p>
        </div>
        <div style="background: rgba(59, 130, 246, 0.08); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 6px; padding: 6px 10px; font-size: 0.76rem;">
          <strong style="color: #93c5fd;">Enterprise Mandate:</strong> All 13 enterprise layers must map directly into the C4 Container Catalog with automated CI/CD dependency graph tracking.
        </div>
      </div>
    </div>
    """

def get_slide_12_api_mermaid(core_sys):
    """Generates Universal API Management Mermaid diagram for Slide 12."""
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">API-First Architecture: 3-Tier Layered Hierarchy</div>
        <div class="mermaid" style="flex: 1;">
graph TB
  subgraph EXP ["1. EXPERIENCE APIS (CONSUMPTION)"]
    E1["Mobile App API<br/>BFF Pattern (GraphQL)"]
    E2["Web Booking API<br/>Next.js Server Actions"]
    E3["B2B / Partner API<br/>OpenAPI 3.1 Specs"]
  end
  subgraph PRC ["2. PROCESS APIS (ORCHESTRATION)"]
    P1["Dynamic Booking Flow<br/>Saga State Machine"]
    P2["Disruption Rebooking<br/>Agentforce MCP Tool"]
    P3["Loyalty Redemption<br/>Real-Time Ledger Check"]
  end
  subgraph SYS ["3. SYSTEM APIS (ENCAPSULATION)"]
    S1["{core_sys} Adapter<br/>EDIFACT / OXI Translator"]
    S2["Payment Gateway<br/>PCI-DSS Vault Tokenizer"]
    S3["Lakehouse Ingest API<br/>Kafka / Iceberg Connector"]
  end
  EXP --> PRC
  PRC --> SYS
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">Universal API Management Framework</div>
          <table class="data-table" style="margin-bottom: 0.6rem;">
            <tr><th>Tier</th><th>Latency SLA</th><th>Security Policy</th><th>Protocol Standard</th></tr>
            <tr><td><strong>Experience</strong></td><td>< 50ms Edge</td><td>OAuth2 / PKCE / JWT</td><td>GraphQL / HTTP/3</td></tr>
            <tr><td><strong>Process</strong></td><td>< 200ms P99</td><td>mTLS / SPIFFE</td><td>gRPC / REST JSON</td></tr>
            <tr><td><strong>System</strong></td><td>< 500ms Core</td><td>IPsec / PrivateLink</td><td>SOAP / REST / Binary</td></tr>
          </table>
          <p style="font-size: 0.8rem; color: #cbd5e1;">
            <strong>MuleSoft Anypoint Gateway:</strong> Enforces rate-limiting, WAF inspection, and tokenization at the edge. Legacy backend systems are shielded from traffic surges during flash sales.
          </p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 6px; padding: 6px 10px; font-size: 0.76rem;">
          <strong style="color: #a7f3d0;">Governance Benchmark:</strong> 100% of internal APIs documented in OpenAPI 3.1 with automated contract testing via Prism and Newman in CI/CD.
        </div>
      </div>
    </div>
    """

def get_slide_13_eda_mermaid():
    """Generates Event-Driven Architecture Mermaid diagram for Slide 13."""
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">Event-Driven Architecture & Real-Time Telemetry</div>
        <div class="mermaid" style="flex: 1;">
graph TB
  subgraph PROD ["EVENT PRODUCERS"]
    P1["Operational Telemetry<br/>ACARS / IoT / AIS"]
    P2["Guest App Clicks<br/>Snowplow Real-Time"]
    P3["Core Booking Events<br/>Inventory Changes"]
  end
  subgraph MESH ["EVENT MESH BACKBONE"]
    K1["Apache Kafka 3.6<br/>Partitioned Topic Clusters"]
    K2["kcat Debugging CLI<br/>Topic Validation & Ingestion"]
    K3["Apache Flink 1.18<br/>Stateful Stream Processing"]
  end
  subgraph CONS ["EVENT CONSUMERS"]
    C1["Salesforce Data Cloud<br/>Real-Time Ingestion API"]
    C2["Agentforce Atlas<br/>Disruption Event Triggers"]
    C3["ClickHouse OLAP<br/>Sub-Second Dashboards"]
  end
  PROD --> MESH
  MESH --> CONS
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">Event Streaming SLA & Telemetry Performance</div>
          <table class="data-table" style="margin-bottom: 0.6rem;">
            <tr><th>Metric</th><th>Target SLA</th><th>Production Benchmark</th></tr>
            <tr><td>End-to-End Latency</td><td>< 250ms</td><td>48ms P99 (Kafka -> Flink -> Data Cloud)</td></tr>
            <tr><td>Throughput Capacity</td><td>100,000 EPS</td><td>450,000 EPS Peak (Flash Sale / Storm)</td></tr>
            <tr><td>Data Retention</td><td>7 Days Hot / 90 Cold</td><td>Tiered Storage to S3 / Apache Iceberg</td></tr>
            <tr><td>Ordering Guarantee</td><td>Strict Per-Entity</td><td>Keyed on PNR / Guest UUID / Vessel ID</td></tr>
          </table>
          <p style="font-size: 0.8rem; color: #cbd5e1;">
            <strong>Dead-Letter Queue (DLQ) Governance:</strong> Malformed payloads are routed to isolated DLQ topics with automated schema validation alerts via Slack and PagerDuty.
          </p>
        </div>
        <div style="background: rgba(139, 92, 246, 0.08); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 6px; padding: 6px 10px; font-size: 0.76rem;">
          <strong style="color: #c084fc;">Tool Showcase (Compendium):</strong> Confluent Kafka + <code>kcat</code> CLI enable zero-downtime hot topic partition rebalancing across multi-region clusters.
        </div>
      </div>
    </div>
    """

def get_slide_16_architecture_mermaid(sector_title, core_sys):
    """Generates full 13-layer architectural topology Mermaid diagram for Slide 16."""
    return f"""
    <div class="glass-card" style="flex: 1 1 0; display: flex; flex-direction: column; min-height: 0;">
      <div class="card-header">13-Layer Master Enterprise Architecture Topology — {sector_title}</div>
      <div class="mermaid" style="flex: 1;">
graph TB
  subgraph L1_3 ["CHANNELS & TOUCHPOINTS"]
    L9["Layer 9: Web, Mobile, Kiosks, Crew Tablets (React / iOS Native)"]
    L2["Layer 2: Omnichannel Marketing & Personalization (Marketing Cloud / Braze)"]
    L3["Layer 3: Customer Service & Contact Center (Service Cloud / Genesys)"]
  end
  subgraph L4_6 ["INTELLIGENCE & ENGAGEMENT FABRIC"]
    L4["Layer 4: Loyalty & Rewards Management (Salesforce Loyalty / Custom)"]
    L8["Layer 8: Agentic AI & Reasoning Swarms (Agentforce / Palantir AIP)"]
    L5["Layer 5: Real-Time Customer Data Platform (Data Cloud / Segment)"]
  end
  subgraph L7_10 ["INTEGRATION & LAKEHOUSE BACKBONE"]
    L6["Layer 6: Universal API Gateway & Event Mesh (MuleSoft / Apache Kafka)"]
    L7["Layer 7: Enterprise Data Lakehouse (Snowflake / Databricks / Iceberg)"]
    L10["Layer 10: Headless CMS & Digital Asset Management (Contentful / AEM)"]
  end
  subgraph L11_13 ["CORE SYSTEMS OF RECORD & GOVERNANCE"]
    L1["Layer 1: Core Operations ({core_sys})"]
    L11["Layer 11: Finance, Revenue Accounting & ERP (SAP S/4HANA / NetSuite)"]
    L12["Layer 12: HR, Crew & Workforce Management (Workday / Kronos)"]
    L13["Layer 13: Zero-Trust Security, IAM & Governance (CyberArk / Okta)"]
  end
  L1_3 --> L4_6
  L4_6 --> L7_10
  L7_10 --> L11_13
      </div>
    </div>
    """

def get_slide_17_salesforce_mermaid(core_sys):
    """Generates Variation 1 (Salesforce-Centric) Mermaid architecture diagram for Slide 17."""
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">Variation 1: The Unified Salesforce Agentic Ecosystem</div>
        <div class="mermaid" style="flex: 1;">
graph TB
  subgraph TOUCH ["OMNICHANNEL TOUCHPOINTS"]
    PA["Guest Mobile App (SDK)"]
    CT["Frontline Staff Tablets"]
    WA["WhatsApp / Apple Messages"]
    CC["Service Cloud Voice"]
  end
  subgraph SF_AGENT ["SALESFORCE AGENTIC RUNTIME"]
    AF["Agentforce Atlas Engine<br/>Autonomous Reasoning"]
    ETL["Einstein Trust Layer<br/>Zero-Retention & Masking"]
    SC["Service Cloud Desktop<br/>Unified Customer 360"]
    MC["Marketing Cloud Growth<br/>Journey Optimization"]
  end
  subgraph SF_DATA ["UNIFIED DATA & INTEGRATION"]
    DC["Salesforce Data Cloud<br/>Real-Time CIM Graph"]
    MS["MuleSoft Anypoint Gateway<br/>System / Process / Exp APIs"]
  end
  subgraph EXT_LAKE ["ZERO-COPY DATA FEDERATION"]
    SNOW["Snowflake / Databricks<br/>Lakehouse (Apache Iceberg)"]
  end
  subgraph LEGACY ["CORE SYSTEMS OF RECORD"]
    CORE["{core_sys}<br/>Core Operational Engine"]
    ERP["SAP S/4HANA<br/>Finance & General Ledger"]
  end
  TOUCH --> SF_AGENT
  SF_AGENT --> SF_DATA
  SF_DATA <--> EXT_LAKE
  SF_DATA --> MS
  MS --> LEGACY
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">Architectural Hallmarks & Moat</div>
          <p style="font-size: 0.82rem; margin-bottom: 0.4rem;"><strong>Single Metadata Framework:</strong> Unifies CRM, Data Cloud DMOs, Agentforce topics, and Omni-Channel routing without custom glue code.</p>
          <p style="font-size: 0.82rem; margin-bottom: 0.4rem;"><strong>Zero-Copy Lakehouse Federation:</strong> Bidirectional query federation with Snowflake, Databricks, and Google BigQuery via Apache Iceberg, eliminating petabyte-scale data duplication.</p>
          <p style="font-size: 0.82rem; margin-bottom: 0.4rem;"><strong>Deterministic Enterprise Guardrails:</strong> Einstein Trust Layer enforces zero data retention with LLM providers, dynamic PII masking, and cryptographic audit trails.</p>
          <table class="data-table" style="margin-top: 0.4rem;">
            <tr><th>Metric</th><th>Benchmark Value</th><th>Business Impact</th></tr>
            <tr><td>Time-to-Value (TTV)</td><td>9 to 12 Months</td><td>Fastest enterprise ROI realization</td></tr>
            <tr><td>Engineering Headcount</td><td>32 FTE Engineers</td><td>35% smaller team than custom FOSS</td></tr>
            <tr><td>Servicing Deflection</td><td>74.4% Blended Rate</td><td>$13.7M annual operational savings</td></tr>
          </table>
        </div>
        <div style="background: rgba(59, 130, 246, 0.08); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 6px; padding: 6px 10px; font-size: 0.76rem;">
          <strong style="color: #93c5fd;">Strategic Verdict:</strong> Optimal choice for enterprises demanding rapid commercial agility, deep customer 360, and autonomous service resolution without massive custom software engineering overhead.
        </div>
      </div>
    </div>
    """

def get_slide_18_open_source_mermaid(core_sys):
    """Generates Variation 2 (Composable Open-Source CLI Stack) Mermaid architecture diagram for Slide 18."""
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">Variation 2: Composable Open-Source CLI Architecture (FOSS Stack)</div>
        <div class="mermaid" style="flex: 1;">
graph TB
  subgraph CLI_STREAM ["EVENT STREAMING & INGESTION (CLI TOOLS)"]
    KAFKA["Apache Kafka Cluster"]
    KCAT["kcat (kafkacat CLI)<br/>High-Speed Consumer/Producer"]
    SNOWPLOW["Snowplow CLI (snowplowctl)<br/>Behavioral Event Validation"]
    MELTANO["Meltano CLI<br/>Singer ELT Pipeline Runner"]
  end
  subgraph CLI_LAKE ["ANALYTICAL LAKEHOUSE & OLAP (CLI TOOLS)"]
    CLICK["ClickHouse CLI (clickhouse-client)<br/>Real-Time Sub-Second OLAP"]
    DUCK["DuckDB CLI (duckdb)<br/>Vectorized Columnar Analytics"]
    POLARS["Polars CLI<br/>Rust In-Memory DataFrames"]
    DBT["dbt CLI (dbt-core)<br/>SQL Transformation DAGs"]
  end
  subgraph CLI_AI ["LOCAL & DISTRIBUTED AI/ML (CLI TOOLS)"]
    VLLM["vLLM CLI<br/>PagedAttention LLM Serving"]
    OLLAMA["Ollama CLI / llama.cpp<br/>GGUF Local Model Inference"]
    MLFLOW["MLflow CLI<br/>Model Registry & Tracking"]
    RAY["Ray CLI (ray submit)<br/>Distributed GPU Clusters"]
  end
  subgraph CLI_MMM ["MARKETING MMM & FINOPS (CLI TOOLS)"]
    ROBYN["Meta Robyn (Rscript)<br/>Automated Ridge MMM"]
    MERIDIAN["Google Meridian (Python JAX)<br/>Bayesian Marketing Mix"]
    INFRACOST["Infracost CLI<br/>Terraform Shift-Left FinOps"]
    OPENBB["OpenBB Terminal CLI<br/>Financial Valuation & Analytics"]
  end
  CLI_STREAM --> CLI_LAKE
  CLI_LAKE --> CLI_AI
  CLI_LAKE --> CLI_MMM
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">Production CLI Command Suite & Execution Engine</div>
          <div style="background: #050811; border: 1px solid #1e293b; border-radius: 8px; padding: 8px; font-family: monospace; font-size: 0.66rem; color: #a7f3d0; line-height: 1.4; overflow-y: auto; max-height: 340px;">
            <div style="color: #60a5fa; font-weight: bold;"># 1. Real-Time Streaming & CLI Validation</div>
            <span style="color: #94a3b8;">$</span> kcat -b kafka:9092 -t guest.telemetry -C -o end<br>
            <span style="color: #94a3b8;">$</span> snowplowctl lint --schema iglu:com.travel/pnr/jsonschema/1-0-0<br>
            <span style="color: #94a3b8;">$</span> meltano run tap-postgres target-clickhouse<br>
            <br>
            <div style="color: #34d399; font-weight: bold;"># 2. Vectorized OLAP & In-Memory Analytics</div>
            <span style="color: #94a3b8;">$</span> duckdb -c "SELECT guest_id, sum(ancillary) FROM 's3://lake/*.parquet' GROUP BY 1"<br>
            <span style="color: #94a3b8;">$</span> clickhouse-client --query "SELECT count(*) FROM ops_events WHERE delay > 15"<br>
            <span style="color: #94a3b8;">$</span> dbt run --select tag:realtime_inventory --target prod<br>
            <br>
            <div style="color: #c084fc; font-weight: bold;"># 3. Local & Distributed Generative AI Serving</div>
            <span style="color: #94a3b8;">$</span> vllm serve mistralai/Mistral-7B --tensor-parallel-size 2 --gpu-memory-utilization 0.9<br>
            <span style="color: #94a3b8;">$</span> ollama run llama3:70b "Analyze disruption recovery options for affected guests"<br>
            <span style="color: #94a3b8;">$</span> mlflow models serve -m models:/YieldOptimizer/Production -p 8080<br>
            <br>
            <div style="color: #fbbf24; font-weight: bold;"># 4. Marketing Mix Modeling & Cloud FinOps</div>
            <span style="color: #94a3b8;">$</span> Rscript run_robyn.R --allocator_optim --spend_budget 5000000<br>
            <span style="color: #94a3b8;">$</span> python -m meridian --config=configs/mmm_travel.yaml<br>
            <span style="color: #94a3b8;">$</span> infracost breakdown --path ./infra/terraform<br>
            <span style="color: #94a3b8;">$</span> openbb equity/fa/dcf --ticker DAL
          </div>
        </div>
        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 6px; padding: 6px 10px; font-size: 0.76rem;">
          <strong style="color: #a7f3d0;">The FOSS Trade-Off:</strong> $0 software licensing fees and zero vendor lock-in, but requires <strong>+23 additional data/platform engineers ($3.4M/year payroll)</strong> and longer time-to-value (14-18 months).
        </div>
      </div>
    </div>
    """

def get_slide_19_best_money_mermaid(core_sys):
    """Generates Variation 3 (Best Money Can Buy) Mermaid architecture diagram for Slide 19."""
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">Variation 3: Ultra-Tier Sovereign Pinnacle Architecture ($194.5M TCO)</div>
        <div class="mermaid" style="flex: 1;">
graph TB
  subgraph SOV_TOUCH ["MISSION-CRITICAL TOUCHPOINTS"]
    BIO["Biometric Facial Gate (Nuance Voice <3s)"]
    GEN["Genesys Sovereign Cloud CX (CCAI)"]
    AEM["Adobe Experience Manager (Headless AEM)"]
  end
  subgraph PALANTIR ["OPERATIONAL BRAIN (PALANTIR)"]
    PAL["Palantir Foundry Core<br/>Dynamic Enterprise Ontology"]
    AIP["Palantir AIP<br/>500 Crisis Permutations / 30s"]
  end
  subgraph ADOBE_AEP ["STREAMING COMMERCE & EXPERIENCE"]
    AEP["Adobe Experience Platform (AEP)<br/>Sub-50ms Global Edge Profile"]
    AJO["Adobe Journey Optimizer (AJO)<br/>Real-Time Offer Decisioning"]
  end
  subgraph SOV_SEC ["MILITARY-GRADE DEFENSE & INFRA"]
    CYBER["CyberArk Vault + HashiCorp HSM<br/>FIPS 140-2 Level 3 Cryptography"]
    ZSCALER["Zscaler Private Access<br/>Micro-Segmented Zero-Trust"]
    DGX["NVIDIA DGX H100 SuperPOD<br/>Private Sovereign AI Training"]
  end
  SOV_TOUCH --> ADOBE_AEP
  ADOBE_AEP <--> PALANTIR
  PALANTIR --> SOV_SEC
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">Sovereign Mission-Critical Supremacy</div>
          <p style="font-size: 0.82rem; margin-bottom: 0.4rem;"><strong>Palantir Dynamic Enterprise Ontology:</strong> Binds all physical assets, staff legalities, and passenger reservations into a real-time digital twin, evaluating 500 disruption permutations in 30 seconds.</p>
          <p style="font-size: 0.82rem; margin-bottom: 0.4rem;"><strong>Adobe Experience Platform (AEP):</strong> Sub-50ms global edge profile calculation with Adobe Journey Optimizer for real-time 1-to-1 dynamic pricing and personalized upsell.</p>
          <p style="font-size: 0.82rem; margin-bottom: 0.4rem;"><strong>Defense-Grade Security & Sovereign AI:</strong> CyberArk Vault with FIPS 140-2 Level 3 HSM hardware encryption, Zscaler micro-segmentation, and on-premise NVIDIA DGX H100 GPU clusters.</p>
          <table class="data-table" style="margin-top: 0.4rem;">
            <tr><th>Dimension</th><th>Sovereign Tier Metric</th><th>Strategic Advantage</th></tr>
            <tr><td>Crisis Recovery Time</td><td>< 2 Minutes Autonomous</td><td>Zero human panic during mass grounding</td></tr>
            <tr><td>Sovereign Survivability</td><td>Air-Gapped Local Cluster</td><td>100% operational during global cloud outages</td></tr>
            <tr><td>3-Year Net Economic Value</td><td>+$230.5M Net Margin Lift</td><td>Justifies $194.5M TCO for mega-operators</td></tr>
          </table>
        </div>
        <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 6px; padding: 6px 10px; font-size: 0.76rem;">
          <strong style="color: #fbbf24;">The Elite Standard:</strong> Built for national flagships, mega-resorts, and cruise conglomerates where single-minute operational outages cost millions of dollars.
        </div>
      </div>
    </div>
    """

def get_slide_20_tco_chart(sector_code, tco_v1, tco_v2, tco_v3, benefit_v1, benefit_v2, benefit_v3, net_v1, net_v2, net_v3):
    """Generates an interactive Chart.js Grouped Bar Chart comparing TCO & Net Economic Value for Slide 20."""
    canvas_id = f"chart-tco-comparison-{sector_code.lower()}"
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">3-Year TCO vs Net Economic Value Generated</div>
        <div style="position: relative; flex: 1; min-height: 220px;">
          <canvas id="{canvas_id}"></canvas>
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">Executive TCO & ROI Scorecard</div>
          <table class="data-table" style="margin-bottom: 0.6rem;">
            <tr><th>Metric</th><th>V1: Salesforce</th><th>V2: Without SF</th><th>V3: Best Money</th></tr>
            <tr><td><strong>3-Year Total TCO</strong></td><td><strong>${tco_v1}M</strong></td><td>${tco_v2}M</td><td>${tco_v3}M</td></tr>
            <tr><td>Annual License ACV</td><td>$14.5M</td><td>$12.2M</td><td>$35.0M</td></tr>
            <tr><td>Engineering Payroll</td><td>$4.8M (32 eng)</td><td>$8.2M (55 eng)</td><td>$14.0M (85 eng)</td></tr>
            <tr><td>3-Year Gross Benefit</td><td>${benefit_v1}M</td><td>${benefit_v2}M</td><td>${benefit_v3}M</td></tr>
            <tr><td><strong style="color: #10b981;">Net Economic Value</strong></td><td><strong style="color: #10b981;">+${net_v1}M</strong></td><td>+${net_v2}M</td><td><strong style="color: #38bdf8;">+${net_v3}M</strong></td></tr>
            <tr><td>Payback Period</td><td><strong>9 Months</strong></td><td>16 Months</td><td>14 Months</td></tr>
          </table>
          <p style="font-size: 0.8rem; color: #cbd5e1;">
            <strong>The Engineering Payroll Trap:</strong> While Variation 2 appears cheaper on software licensing ($12.2M vs $14.5M), it requires 23 additional data engineers ($3.4M/year payroll), making its total 3-year TCO <strong>$8.8M higher</strong>.
          </p>
        </div>
        <div style="background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 6px; padding: 6px 10px; font-size: 0.76rem;">
          <strong style="color: #38bdf8;">C-Suite Recommendation:</strong> Variation 1 provides the optimal risk-adjusted IRR (78.4%) and fastest time-to-value (9 months) for enterprise scale.
        </div>
      </div>
    </div>
    <script>
      (function() {{
        const canvas = document.getElementById('{canvas_id}');
        if (!canvas) return;
        canvas.initChart = function() {{
          return new Chart(canvas, {{
            type: 'bar',
            data: {{
              labels: ['V1: Salesforce', 'V2: Without SF', 'V3: Best Money'],
              datasets: [
                {{
                  label: '3-Year TCO ($M)',
                  data: [{tco_v1}, {tco_v2}, {tco_v3}],
                  backgroundColor: '#ef4444',
                  borderRadius: 4
                }},
                {{
                  label: 'Gross Benefit ($M)',
                  data: [{benefit_v1}, {benefit_v2}, {benefit_v3}],
                  backgroundColor: '#3b82f6',
                  borderRadius: 4
                }},
                {{
                  label: 'Net Value ($M)',
                  data: [{net_v1}, {net_v2}, {net_v3}],
                  backgroundColor: '#10b981',
                  borderRadius: 4
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{
                  position: 'top',
                  labels: {{ color: '#cbd5e1', font: {{ size: 9 }}, boxWidth: 10 }}
                }}
              }},
              scales: {{
                y: {{
                  grid: {{ color: 'rgba(255, 255, 255, 0.05)' }},
                  ticks: {{ color: '#94a3b8', font: {{ size: 9 }} }}
                }},
                x: {{
                  grid: {{ display: false }},
                  ticks: {{ color: '#cbd5e1', font: {{ size: 9 }} }}
                }}
              }}
            }}
          }});
        }};
        document.addEventListener('DOMContentLoaded', () => {{
          if (canvas.offsetParent !== null) canvas.chartInstance = canvas.initChart();
        }});
      }})();
    </script>
    """

def get_slide_21_four_systems_matrix(sector_title):
    """Generates the Four Systems Framework interactive card grid for Slide 21."""
    return f"""
    <div class="grid-4" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="border-top-color: #3b82f6;">
        <div class="card-header" style="color: #60a5fa;">1. System of Record (SoR)</div>
        <div style="font-size: 0.78rem; line-height: 1.4;">
          <p><strong>Definition:</strong> The authoritative source of transactional truth for core assets and bookings.</p>
          <p><strong>Characteristics:</strong> High ACID consistency, relational integrity, audited ledgers.</p>
          <p><strong>Primary Technologies:</strong> Core PSS / PMS / CRS, SAP S/4HANA, Workday HCM.</p>
        </div>
        <div style="margin-top: auto; padding: 4px 8px; background: rgba(59,130,246,0.1); border-radius: 4px; font-size: 0.72rem; color: #93c5fd;">
          <strong>Governance:</strong> Strict schema contracts; zero unverified direct writes.
        </div>
      </div>
      <div class="glass-card" style="border-top-color: #10b981;">
        <div class="card-header" style="color: #34d399;">2. System of Intelligence (SoI)</div>
        <div style="font-size: 0.78rem; line-height: 1.4;">
          <p><strong>Definition:</strong> The real-time data harmonization, ML feature store, and identity graph.</p>
          <p><strong>Characteristics:</strong> Sub-second streaming, probabilistic resolution, Zero-Copy query.</p>
          <p><strong>Primary Technologies:</strong> Salesforce Data Cloud, Snowflake, ClickHouse, DuckDB.</p>
        </div>
        <div style="margin-top: auto; padding: 4px 8px; background: rgba(16,185,129,0.1); border-radius: 4px; font-size: 0.72rem; color: #a7f3d0;">
          <strong>Governance:</strong> Apache Iceberg tables; column-level masking; GDPR consent.
        </div>
      </div>
      <div class="glass-card" style="border-top-color: #8b5cf6;">
        <div class="card-header" style="color: #a78bfa;">3. System of Engagement (SoE)</div>
        <div style="font-size: 0.78rem; line-height: 1.4;">
          <p><strong>Definition:</strong> Omnichannel interaction runtime for customers and frontline employees.</p>
          <p><strong>Characteristics:</strong> Contextual personalization, session persistence, low-latency UI.</p>
          <p><strong>Primary Technologies:</strong> Service Cloud Voice, Agentforce, Marketing Cloud, WhatsApp.</p>
        </div>
        <div style="margin-top: auto; padding: 4px 8px; background: rgba(139,92,246,0.1); border-radius: 4px; font-size: 0.72rem; color: #ddd6fe;">
          <strong>Governance:</strong> Einstein Trust Layer; zero LLM training on enterprise data.
        </div>
      </div>
      <div class="glass-card" style="border-top-color: #f59e0b;">
        <div class="card-header" style="color: #fbbf24;">4. System of Decision (SoD)</div>
        <div style="font-size: 0.78rem; line-height: 1.4;">
          <p><strong>Definition:</strong> Real-time operational decisioning, algorithmic pricing, and disruption recovery.</p>
          <p><strong>Characteristics:</strong> Mathematical optimization, multi-agent swarms, simulation.</p>
          <p><strong>Primary Technologies:</strong> Atlas Engine, Palantir AIP, LangGraph, vLLM, CausalML.</p>
        </div>
        <div style="margin-top: auto; padding: 4px 8px; background: rgba(245,158,11,0.1); border-radius: 4px; font-size: 0.72rem; color: #fde68a;">
          <strong>Governance:</strong> Human-in-the-loop triggers; strict financial authority limits.
        </div>
      </div>
    </div>
    """

def get_slide_24_sequence_mermaid(core_sys, channel_name):
    """Generates Real-Time Operational Handoff Sequence Diagram for Slide 24."""
    return f"""
    <div class="glass-card" style="flex: 1 1 0; display: flex; flex-direction: column; min-height: 0;">
      <div class="card-header">Real-Time Operational Handoff Sequence: Booking to Check-in / Boarding</div>
      <div class="mermaid" style="flex: 1;">
sequenceDiagram
  autonumber
  actor Guest as Customer / Guest
  participant App as Mobile App / Web (React)
  participant API as MuleSoft API Gateway
  participant DC as Salesforce Data Cloud
  participant AF as Agentforce Atlas Engine
  participant Core as Core Ops ({core_sys})
  participant Lake as Snowflake / Lakehouse

  Guest->>App: 1. Selects itinerary & completes booking
  App->>API: 2. POST /v2/reservations (Payload + Payment Token)
  API->>Core: 3. Create reservation & lock inventory
  Core-->>API: 4. Confirmation (PNR / Folio #)
  API->>DC: 5. Stream booking event via Ingestion API
  DC->>Lake: 6. Zero-Copy Iceberg synchronization
  DC->>AF: 7. Trigger customer journey orchestrator
  AF->>Guest: 8. Personalized WhatsApp confirmation with Apple Wallet pass
  Note over Guest,Core: Day-of-Travel / Arrival Milestone
  Guest->>App: 9. Initiates digital check-in / biometric scan
  App->>API: 10. POST /v2/checkin (Biometric Token)
  API->>Core: 11. Update status to CHECKED_IN & assign seat/room
  Core-->>App: 12. Digital key / boarding barcode issued
  API->>DC: 13. Publish state transition event
      </div>
    </div>
    """

def get_slide_25_state_machine_mermaid():
    """Generates Distributed State Consistency State Machine for Slide 25."""
    return f"""
    <div class="glass-card" style="flex: 1 1 0; display: flex; flex-direction: column; min-height: 0;">
      <div class="card-header">Distributed State Consistency & Reservation Lifecycle State Machine</div>
      <div class="mermaid" style="flex: 1;">
stateDiagram-v2
  [*] --> INITIATED: Guest begins checkout
  INITIATED --> INVENTORY_HELD: Temporary seat/room lock (10m TTL)
  INVENTORY_HELD --> PAYMENT_PROCESSING: Payment gateway authorization
  PAYMENT_PROCESSING --> CONFIRMED: Payment captured & PNR ticketed
  PAYMENT_PROCESSING --> INVENTORY_RELEASED: Payment declined / timeout
  INVENTORY_RELEASED --> [*]
  CONFIRMED --> CHECKED_IN: Digital check-in / boarding pass issued
  CHECKED_IN --> COMPLETED: Flight departed / Stay checked-out
  CONFIRMED --> DISRUPTED: Delay / Cancellation / Storm event
  DISRUPTED --> AUTO_REBOOKED: Agentforce autonomous recovery
  AUTO_REBOOKED --> CHECKED_IN: Guest accepts automated re-routing
  DISRUPTED --> REFUNDED: Compensation / refund issued (EU261/DOT)
  REFUNDED --> [*]
  COMPLETED --> [*]
      </div>
    </div>
    """

def get_slide_36_disruption_mermaid():
    """Generates Disruption Recovery & Autonomous IROPS Mermaid diagram for Slide 36."""
    return f"""
    <div class="glass-card" style="flex: 1 1 0; display: flex; flex-direction: column; min-height: 0;">
      <div class="card-header">Autonomous Disruption Recovery (IROPS) Workflow Architecture</div>
      <div class="mermaid" style="flex: 1;">
flowchart TD
  D1["Weather Alert / Mechanical Delay Event"] --> D2["Kafka Operational Telemetry Ingest"]
  D2 --> D3["Data Cloud: Affected Customer Cohort Identification"]
  D3 --> D4["Agentforce Atlas Engine: Reasoning Loop"]
  D4 --> D5{"Evaluation: High-Tier VIP or Standard Guest?"}
  D5 -- VIP Guest --> D6["Autonomous Rebooking on Earliest Flight/Suite + Limo Voucher"]
  D5 -- Standard Guest --> D7["Parallel Autonomous Multi-Option Offer via WhatsApp"]
  D6 --> D8["Push Notification + Apple Wallet Pass Update"]
  D7 --> D8
  D8 --> D9{"Guest Response?"}
  D9 -- 1-Click Accept --> D10["Update Core PSS / PMS via MuleSoft API"]
  D9 -- Decline / Modify --> D11["Escalate with Full Context to Live Service Cloud Agent"]
  D10 --> D12["Issue Meal / Hotel Voucher Barcode Automatically"]
  D11 --> D12
      </div>
    </div>
    """

def get_slide_38_turnaround_gantt(turnaround_title):
    """Generates Turnaround Workflow Gantt diagram for Slide 38."""
    return f"""
    <div class="glass-card" style="flex: 1 1 0; display: flex; flex-direction: column; min-height: 0;">
      <div class="card-header">{turnaround_title}</div>
      <div class="mermaid" style="flex: 1;">
gantt
  title Turnaround Critical Path Workflow (Minutes 0 to 35)
  dateFormat X
  axisFormat %M min

  section Deboarding
  Aircraft Blocks In & Chocks Placed      :done, d1, 0, 2
  Jetbridge Connected & Doors Open        :done, d2, 2, 5
  Passenger Deboarding (180 Pax)          :active, d3, 3, 15

  section Ground Servicing
  Baggage Unloading (Fwd & Aft Cargo)    :b1, 4, 18
  Potable Water & Lavatory Service        :b2, 10, 20
  Cabin Cleaning & Security Check         :b3, 14, 25
  Galley Catering Restock                 :b4, 16, 26
  Fueling Operations (Hydrant Truck)      :crit, b5, 12, 28

  section Boarding & Departure
  Outbound Baggage Loading & Scan         :o1, 18, 30
  Biometric Gate Boarding Commences       :crit, o2, 20, 32
  Cargo Doors Closed & Trim Sheet Final   :o3, 30, 33
  Passenger Doors Closed & Jetbridge Ret  :o4, 32, 34
  Pushback Tug Connected & Departure      :crit, o5, 34, 35
      </div>
    </div>
    """

def get_slide_42_atlas_engine_mermaid():
    """Generates Atlas Engine Reasoning Architecture Mermaid diagram for Slide 42."""
    return f"""
    <div class="glass-card" style="flex: 1 1 0; display: flex; flex-direction: column; min-height: 0;">
      <div class="card-header">Agentic Reasoning Architecture: Atlas Engine vs LangGraph vs Palantir AIP</div>
      <div class="mermaid" style="flex: 1;">
flowchart LR
  subgraph INPUT ["GROUNDING & CONTEXT"]
    USR["User Prompt / Event Trigger"]
    CTX["Data Cloud Dynamic Profile (DMOs)"]
    KNOW["Enterprise Knowledge Base (Vector RAG)"]
  end
  subgraph ATLAS ["AGENTFORCE ATLAS REASONING ENGINE"]
    DEC["Goal Decomposition & Intent Classifier"]
    TOP["Topic & Guardrail Policy Enforcement"]
    LOOP["Autonomous ReAct Loop<br/>(Reason -> Act -> Observe)"]
    PLAN["Plan Refinement & Memory Cache"]
  end
  subgraph TOOLS ["EXECUTABLE ENTERPRISE TOOLS (MCP)"]
    T1["MuleSoft PSS/PMS Booking Tool"]
    T2["Payment Gateway Tokenizer"]
    T3["Digital Voucher Generator"]
    T4["Notification Dispatch (WhatsApp/SMS)"]
  end
  subgraph TRUST ["EINSTEIN TRUST LAYER"]
    SEC["PII Masking & Tokenization"]
    TOX["Toxicity & Hallucination Guardrail"]
    AUD["Cryptographic Audit Trail"]
  end
  INPUT --> ATLAS
  ATLAS --> TRUST
  TRUST --> TOOLS
  TOOLS --> ATLAS
      </div>
    </div>
    """

def get_slide_43_multi_agent_mermaid():
    """Generates Multi-Agent Swarm Orchestration Mermaid diagram for Slide 43."""
    return f"""
    <div class="glass-card" style="flex: 1 1 0; display: flex; flex-direction: column; min-height: 0;">
      <div class="card-header">Multi-Agent Swarm Orchestration: Supervisor-Specialist Architecture</div>
      <div class="mermaid" style="flex: 1;">
flowchart TD
  SUP["SUPERVISOR AGENT<br/>Orchestration & Task Delegation"]
  subgraph SWARM ["SPECIALIST AUTONOMOUS AGENTS"]
    A1["COMMERCIAL AGENT<br/>Dynamic Pricing & Ancillaries"]
    A2["DISRUPTION AGENT<br/>IROPS & Flight Re-Routing"]
    A3["LOYALTY AGENT<br/>Points Ledger & Tier Status"]
    A4["OPERATIONS AGENT<br/>Baggage Tracking & Crew Legality"]
  end
  subgraph ENV ["ENTERPRISE RUNTIME ENVIRONMENT"]
    MCP["Model Context Protocol (MCP) Server Hub"]
    CORE["Core Reservation Systems (Altéa/Opera/Seaware)"]
  end
  SUP -->|Delegates Intent| A1
  SUP -->|Delegates Delay| A2
  SUP -->|Delegates Miles| A3
  SUP -->|Delegates Luggage| A4
  A1 <--> MCP
  A2 <--> MCP
  A3 <--> MCP
  A4 <--> MCP
  MCP <--> CORE
      </div>
    </div>
    """

def get_slide_44_mcp_mermaid():
    """Generates Model Context Protocol (MCP) Mermaid diagram for Slide 44."""
    return f"""
    <div class="glass-card" style="flex: 1 1 0; display: flex; flex-direction: column; min-height: 0;">
      <div class="card-header">Model Context Protocol (MCP) & Enterprise RAG Pipeline</div>
      <div class="mermaid" style="flex: 1;">
graph TB
  subgraph CLIENT ["AI AGENT HOSTS (MCP CLIENTS)"]
    C1["Agentforce Atlas Engine"]
    C2["LangGraph Multi-Agent Swarm"]
    C3["Frontline Assistant (iOS Tablet)"]
  end
  subgraph MCP_HUB ["UNIVERSAL MCP PROTOCOL LAYER"]
    HUB["MCP Server Hub (JSON-RPC 2.0 / SSE Transport)"]
    REG["Tool Registry & Dynamic Capability Discovery"]
    AUTH["Enterprise Authorization & Token Forwarding"]
  end
  subgraph SOURCES ["DATA & SYSTEM EXPOSURES (MCP SERVERS)"]
    S1["MuleSoft System APIs Server<br/>Tools: get_pnr, rebook_flight, issue_voucher"]
    S2["Data Cloud Vector DB Server<br/>Tools: search_faqs, match_guest_profile"]
    S3["Lakehouse Analytical Server<br/>Tools: query_delay_history, get_route_margin"]
  end
  CLIENT <==>|JSON-RPC via SSE| MCP_HUB
  MCP_HUB <==> SOURCES
      </div>
    </div>
    """

def get_slide_46_deflection_chart(sector_code):
    """Generates AI Deflection Economics & ROI Chart for Slide 46."""
    canvas_id = f"chart-deflection-roi-{sector_code.lower()}"
    return f"""
    <div class="grid-2" style="flex: 1 1 0; min-height: 0;">
      <div class="glass-card" style="display: flex; flex-direction: column;">
        <div class="card-header">Contact Center AI Deflection Curve & Cost-Per-Contact</div>
        <div style="position: relative; flex: 1; min-height: 220px;">
          <canvas id="{canvas_id}"></canvas>
        </div>
      </div>
      <div class="glass-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div class="card-header">Deflection Economics & ROI Business Case</div>
          <table class="data-table" style="margin-bottom: 0.6rem;">
            <tr><th>Channel</th><th>Cost / Contact</th><th>Deflection Rate</th><th>Customer CSAT</th></tr>
            <tr><td><strong style="color: #ef4444;">Human Voice Telephony</strong></td><td>$5.50 - $8.20</td><td>0% (Baseline)</td><td>74.2%</td></tr>
            <tr><td><strong style="color: #f59e0b;">Legacy Rules Chatbot</strong></td><td>$1.80 - $2.40</td><td>24.0%</td><td>58.1% (Low)</td></tr>
            <tr><td><strong style="color: #10b981;">Agentforce Autonomous AI</strong></td><td>$0.28 - $0.45</td><td>74.4%</td><td>86.8% (High)</td></tr>
          </table>
          <p style="font-size: 0.8rem; color: #cbd5e1;">
            <strong>Annual Economic Impact:</strong> Handling 12M annual customer contacts via Agentforce reduces contact center operating costs from <strong>$66.0M to $19.4M</strong>, capturing <strong>$46.6M in direct OpEx savings annually</strong>.
          </p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 6px; padding: 6px 10px; font-size: 0.76rem;">
          <strong style="color: #a7f3d0;">Payback Metric:</strong> Agentforce implementation reaches full financial break-even within <strong>7.4 months</strong> of enterprise production deployment.
        </div>
      </div>
    </div>
    <script>
      (function() {{
        const canvas = document.getElementById('{canvas_id}');
        if (!canvas) return;
        canvas.initChart = function() {{
          return new Chart(canvas, {{
            type: 'line',
            data: {{
              labels: ['Month 1', 'Month 3', 'Month 6', 'Month 9', 'Month 12', 'Month 18', 'Month 24'],
              datasets: [
                {{
                  label: 'Autonomous Deflection Rate (%)',
                  data: [15.2, 34.0, 52.5, 68.0, 74.4, 78.2, 82.0],
                  borderColor: '#10b981',
                  backgroundColor: 'rgba(16, 185, 129, 0.1)',
                  fill: true,
                  tension: 0.35,
                  yAxisID: 'y'
                }},
                {{
                  label: 'Blended Cost Per Contact ($)',
                  data: [5.20, 3.80, 2.45, 1.40, 0.95, 0.72, 0.58],
                  borderColor: '#ef4444',
                  backgroundColor: 'transparent',
                  borderDash: [5, 5],
                  tension: 0.35,
                  yAxisID: 'y1'
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{
                  position: 'top',
                  labels: {{ color: '#cbd5e1', font: {{ size: 9 }}, boxWidth: 10 }}
                }}
              }},
              scales: {{
                y: {{
                  type: 'linear',
                  display: true,
                  position: 'left',
                  grid: {{ color: 'rgba(255, 255, 255, 0.05)' }},
                  ticks: {{ color: '#10b981', font: {{ size: 9 }} }}
                }},
                y1: {{
                  type: 'linear',
                  display: true,
                  position: 'right',
                  grid: {{ drawOnChartArea: false }},
                  ticks: {{ color: '#ef4444', font: {{ size: 9 }} }}
                }},
                x: {{
                  grid: {{ display: false }},
                  ticks: {{ color: '#cbd5e1', font: {{ size: 9 }} }}
                }}
              }}
            }}
          }});
        }};
        document.addEventListener('DOMContentLoaded', () => {{
          if (canvas.offsetParent !== null) canvas.chartInstance = canvas.initChart();
        }});
      }})();
    </script>
    """

def get_slide_47_integration_mermaid(core_sys):
    """Generates Master Integration Architecture Blueprint Mermaid diagram for Slide 47."""
    return f"""
    <div class="glass-card" style="flex: 1 1 0; display: flex; flex-direction: column; min-height: 0;">
      <div class="card-header">Master Integration Architecture Blueprint: Hybrid Enterprise Bus</div>
      <div class="mermaid" style="flex: 1;">
graph TB
  subgraph FRONT ["DIGITAL EXPERIENCE LAYER"]
    W["Web / Native Mobile App"]
    K["Airport / Hotel / Vessel Kiosks"]
    C["Frontline Staff Tablet App"]
  end
  subgraph IPASS ["ENTERPRISE INTEGRATION LAYER (MULESOFT)"]
    GW["MuleSoft API Gateway<br/>Edge Security & Tokenization"]
    E_API["Experience API Tier<br/>BFF GraphQL / REST"]
    P_API["Process API Tier<br/>Booking & Disruption Sagas"]
    S_API["System API Tier<br/>Protocol Translators"]
  end
  subgraph MESH ["EVENT STREAMING & FABRIC"]
    KAFKA["Apache Kafka Event Mesh<br/>Real-Time Telemetry & CDC"]
    DC["Salesforce Data Cloud<br/>Real-Time CIM Graph"]
  end
  subgraph BACKEND ["CORE SYSTEMS OF RECORD"]
    CORE["{core_sys}<br/>Core Operational Engine"]
    ERP["SAP S/4HANA<br/>Financial Ledger"]
    CRM["Service Cloud Voice<br/>Customer 360"]
  end
  FRONT --> GW
  GW --> E_API
  E_API --> P_API
  P_API --> S_API
  P_API <--> KAFKA
  KAFKA <--> DC
  S_API --> CORE
  S_API --> ERP
  DC --> CRM
      </div>
    </div>
    """

# ---------------------------------------------------------------------------
# Master Application Function: Preserves all rich domain text while adding
# top KPI ribbons, middle CLI terminal tools / visual assets, and bottom banners
# ---------------------------------------------------------------------------

def apply_visual_enhancements(sector_code, slides):
    sec = sector_code.upper()
    if sec == "AIRLINES":
        title = "Commercial Aviation"
        core = "Amadeus Altéa / Sabre PSS"
        data = {"gbv": 800, "pax": "4.6B", "unit": "$173.91", "anc": 160, "direct": 52.5, "friction": 5.8, "ebit": 55.6}
        core_cli = "openbb equity/load --symbol DAL,LUV,AAL --stats"
        sector_takeaway = "Commercial Aviation requires sub-second dynamic pricing and autonomous IROPS recovery across 4.6B annual passengers."
    elif sec == "HOTELS":
        title = "Hospitality & Lodging"
        core = "Oracle Opera Cloud / Infor PMS"
        data = {"gbv": 600, "pax": "4.25B", "unit": "$141.18", "anc": 87.7, "direct": 35.0, "friction": 14.6, "ebit": 194.6}
        core_cli = "openbb equity/load --symbol MAR,HLT,H --stats"
        sector_takeaway = "Hospitality architecture centers on bypassing OTA commissions (18-22%) via direct loyalty booking and mobile room keys."
    elif sec == "CRUISES":
        title = "Cruises & Maritime"
        core = "Oracle Fidelio Cruise / Seaware PMS"
        data = {"gbv": 48, "pax": "35M", "unit": "$1,371", "anc": 16.8, "direct": 30.0, "friction": 13.0, "ebit": 6.72}
        core_cli = "openbb equity/load --symbol CCL,RCL,NCLH --stats"
        sector_takeaway = "Maritime operations mandate air-gapped vessel survivability at sea with bidirectional Starlink satellite synchronization."
    elif sec == "TOURS":
        title = "Tours & Experiences"
        core = "Bokun / FareHarbor / Peek Pro"
        data = {"gbv": 220, "pax": "1.8B", "unit": "$122.22", "anc": 35.0, "direct": 40.0, "friction": 14.4, "ebit": 26.4}
        core_cli = "openbb equity/load --symbol TRIP,BKNG --stats"
        sector_takeaway = "Tours & Activities architecture unifies 1.2M fragmented operators via the open OCTO API and real-time guide dispatch."

    # Pre-defined CLI Tool showcases mapped to slide indexes from OPEN_SOURCE_CLI_TOOLS_AND_APPLICATIONS_COMPENDIUM.md
    cli_map = {
        0: ("OpenBB Financial Terminal", core_cli, f"{{ 'sector': '{sec}', 'global_gbv': '${data['gbv']}B', 'direct_share': '{data['direct']}%' }}", "Macroeconomic Benchmark Query"),
        4: ("Infracost Cloud FinOps", "infracost breakdown --path ./terraform/direct_channel", f"Total Monthly Cost: $48,200 (Diff: -$14,500 via Serverless Edge)", "Shift-Left Cloud Architecture Cost Optimization"),
        5: ("DuckDB Columnar Analytics", f"duckdb -c \"SELECT brand, count(*), sum(volume) FROM 's3://{sec.lower()}-lake/fleet/*.parquet' GROUP BY 1\"", "┌──────────┬──────────┬─────────────┐\n│ brand    │ count(*) │ sum(volume) │\n├──────────┼──────────┼─────────────┤\n│ Flagship │      210 │ 28,000,000  │\n│ Low-Cost │       90 │ 17,000,000  │\n└──────────┴──────────┴─────────────┘", "Dual-Brand Operational Scale Verification"),
        6: ("dbt Transformation DAG", "dbt run --select tag:commercial_pricing --target prod", "Completed 18 data models in 14.2s (100% tests passed)", "Algorithmic Dynamic Pricing & Catalog ETL"),
        7: ("kcat High-Speed Consumer", f"kcat -b kafka:9092 -t {sec.lower()}.telemetry.sla -C -c 100", f"{{ 'p99_latency_ms': 42, 'dcs_availability': '99.999%', 'rpo_seconds': 0 }}", "Real-Time Operational SLA Monitoring"),
        8: ("Trivy & Cosign Security", "trivy image --severity HIGH,CRITICAL sovereign-core:v3.2", "Total: 0 (HIGH: 0, CRITICAL: 0) — FIPS 140-2 Compliant", "Zero-Trust Image Vulnerability Scanning"),
        9: ("DuckDB Interline Analytics", f"duckdb -c \"SELECT partner, sum(settled_amount) FROM 's3://{sec.lower()}-lake/clearing/*.parquet' GROUP BY 1\"", "Alliance & Code-Share Clearing House Settlement", "Multi-Brand Clearing House Verification"),
        13: ("HashiCorp Vault Secret Engine", "vault read transit/keys/customer-pnr-token -format=json | jq .data.keys", f"{{ 'cipher': 'aes256-gcm96', 'rotation_period': '30d', 'fips_mode': true }}", "Customer Data Encryption Key Management"),
        14: ("Polars Rust DataFrame Engine", f"polars run-query --sql \"SELECT station_id, p99_latency FROM 'edge_health.parquet' WHERE p99_latency > 50\"", "Found 0 nodes exceeding SLA threshold", "Edge Node High-Availability Health Check"),
        21: ("kcat State Transition Producer", f"kcat -b cluster:9092 -t {sec.lower()}.reservation.state -P -K: -l pnr_state.json", "Published 45,000 state transitions without loss", "Real-Time Reservation State Handoff"),
        22: ("Snowplow Behavioral CLI", f"snowplowctl lint --schema iglu:com.{sec.lower()}/booking_event/jsonschema/2-0-0", "Schema validation PASSED — Zero breaking drift detected", "Data Contract & Schema Evolution Governance"),
        25: ("ClickHouse Real-Time OLAP", f"clickhouse-client --query \"SELECT formatReadableQuantity(count(*)) FROM {sec.lower()}_telemetry_stream\"", "450,000 events/sec ingested with sub-50ms latency", "Multi-Tier Ingestion Streaming Telemetry"),
        26: ("DuckDB DMO Schema Inspector", f"duckdb -c \"DESCRIBE SELECT * FROM 's3://{sec.lower()}-lake/gold/dmo_guest.parquet'\"", "42 fields, CIM-compliant, zero-copy Iceberg format", "Domain Data Model Object (DMO) Validation"),
        27: ("CausalML Uplift Modeling", "python -m causalml.inference --method xlearner --treatment loyalty_offer", "AUUC: 0.884 | Incremental Lift: +14.2% on VIP cohort", "Machine Learning Identity Match & Uplift"),
        28: ("dbt Medallion DAG Runner", "dbt test --models tag:gold_dmo --threads 8 && dbt docs generate", "All 84 data integrity constraints passed across Bronze/Silver/Gold", "Lakehouse Medallion Architecture Transformation"),
        29: ("Great Expectations Suite", f"great_expectations checkpoint run {sec.lower()}_gold_suite", "Validation Succeeded: 100% expectation compliance", "Data Governance & Column-Level Lineage"),
        30: ("Meta Robyn MMM CLI", "Rscript run_robyn.R --allocator_optim --spend_budget 48000000", "Pareto optimal allocation: +18.4% direct channel ROAS", "Marketing Mix Modeling Ad Spend Allocation"),
        31: ("Uber Orbit Time-Series CLI", "python -m orbit.models.dlt --data route_demand.csv --predict", "Predicted 94.2% seat load factor across peak holiday corridors", "Dynamic Ancillary & Capacity Forecasting"),
        32: ("PostHog Feature Flag CLI", "posthog feature-flags get --key dynamic-upsell-whatsapp-v3", "Status: ACTIVE (Rollout: 100% to authenticated mobile users)", "Conversational Commerce Upsell Rollout"),
        33: ("vLLM High-Throughput Serving", "vllm serve meta-llama/Llama-3-70b-instruct --tensor-parallel-size 2", "Serving at 142 tokens/sec per GPU with PagedAttention", "Biometric Gate & Kiosk Language Assistant"),
        34: ("llama.cpp Embedded Inference", f"llama-cli -m mistral-7b-q4.gguf -p \"Frontline {title} recognition summary\"", "Offline inference latency: 32ms on Apple Silicon iPad", "Connected Crew & Frontline Tablet Copilot"),
        36: ("LEAN Algorithmic Backtester", "lean backtest --strategy TurnaroundScheduleOptimization", "Turnaround delay reduced by 14.8 minutes per departure", "Process Turnaround Schedule Optimization"),
        38: ("kcat Operational SLA Monitor", f"kcat -L -b kafka:9092 | grep -E \"sla.breach.alert|lag\"", "Consumer lag: 0 across all mission-critical DCS partitions", "Operational Delay Triage & Escalation"),
        39: ("Ray Distributed Compute", "ray submit cluster.yaml optimize_crew_roster.py --fleet B787", "Resolved 450 crew legality conflicts in 8.4 seconds", "Operations & Crew Legality Recovery Optimization"),
        40: ("Falco Runtime Security CLI", "falco -r /etc/falco/rules.d/aviation_safety_audit.yaml", "0 anomalous syscalls detected on core DCS container cluster", "Safety Incident & Regulatory Audit Trail"),
        44: ("NVIDIA Triton Model Server", f"tritonserver --model-repository=/opt/models/{sec.lower()}_predictive", "Serving 12 deep learning models concurrently with dynamic batching", "Predictive Delay & Dynamic Pricing Inference"),
        47: ("usql Protocol Translation", f"usql pgsql://sovereign:5432/edifact_bridge -c \"SELECT count(*) FROM translated_pnr\"", "1,450,000 legacy records translated with zero syntax errors", "Legacy EDIFACT / Type B / OXI Protocol Bridge"),
        48: ("Infracost Phase 1 Diff", "infracost diff --path terraform/phase1_core --format json", "Monthly delta: +$24,500 (100% within allocated Capex budget)", "Phase 1 & 2 Implementation Cost Governance"),
        49: ("MLflow Model Registry", f"mlflow models serve -m \"models:/{title.split()[0]}Agent/Production\" -p 9001", "Production model URI verified with cryptographic SHA256", "Phase 3 & 4 Agentic AI Production Deployment"),
        50: ("OpenBB Workforce Analytics", "openbb economy indicators --country Global --report productivity", "Frontline staff productivity up 34.2% post-agentic deployment", "BCG 'People + Agents' Change Management"),
        51: ("DuckDB Executive Scorecard", "duckdb -c \"SELECT stack_variation, payback_months, net_economic_value FROM 'final_tco.parquet'\"", "Variation 1 (Salesforce): 9 Months Payback | +$76.8M Net Economic Value", "C-Suite Strategic Decision Scorecard")
    }

    # Iterate through all slides
    for i in range(len(slides)):
        # Calculate dynamic slide-specific KPIs
        kpis = [
            (f"${data['gbv']}B", "Global GBV", "12.4%", "up"),
            (f"{data['unit']}", "Unit Value", "5.2%", "up"),
            (f"{data['direct']}%", "Direct Channel", "3.1%", "up"),
            (f"{data['friction']}%", "Friction", "2.1%", "down"),
            (f"${data['ebit']}B", "Net EBIT", "8.4%", "up")
        ]
        kpi_ribbon = get_kpi_row(kpis)

        # Bottom strategic banner
        bottom_banner = get_bottom_banner("Strategic Takeaway", sector_takeaway, "blue")

        # Check if this slide has an existing visual component
        visual_html = None
        if i == 1:
            visual_html = get_slide_2_chart(sec, "Unit", data['gbv'] * 0.75, data['anc'], data['gbv'] * data['friction'] / 100, data['ebit'])
        elif i == 2:
            unit_val = float(str(data['unit']).replace('$', '').replace(',', ''))
            ebit_val = float(data['ebit'])
            visual_html = get_slide_3_waterfall(sec, unit_val, data['direct'], 100 - data['direct'], round(unit_val * data['friction'] / 100, 2), round(unit_val * 0.85, 2), ebit_val)
        elif i == 3:
            visual_html = get_slide_4_channel_chart(sec, data['direct'], 18.5, 15.0, round(100 - data['direct'] - 33.5, 1))
        elif i == 10:
            visual_html = get_slide_11_c4_mermaid(title, core)
        elif i == 11:
            visual_html = get_slide_12_api_mermaid(core)
        elif i == 12:
            visual_html = get_slide_13_eda_mermaid()
        elif i == 15:
            visual_html = get_slide_16_architecture_mermaid(title, core)
        elif i == 16:
            visual_html = get_slide_17_salesforce_mermaid(core)
        elif i == 17:
            visual_html = get_slide_18_open_source_mermaid(core)
        elif i == 18:
            visual_html = get_slide_19_best_money_mermaid(core)
        elif i == 19:
            visual_html = get_slide_20_tco_chart(sec, 68.4, 52.1, 194.5, 145.2, 112.5, 425.0, 76.8, 60.4, 230.5)
        elif i == 20:
            visual_html = get_slide_21_four_systems_matrix(title)
        elif i == 23:
            visual_html = get_slide_24_sequence_mermaid(core, "Direct Channel")
        elif i == 24:
            visual_html = get_slide_25_state_machine_mermaid()
        elif i == 35:
            visual_html = get_slide_36_disruption_mermaid()
        elif i == 37:
            visual_html = get_slide_38_turnaround_gantt(f"{title} Turnaround & Staging Critical Path Workflow")
        elif i == 41:
            visual_html = get_slide_42_atlas_engine_mermaid()
        elif i == 42:
            visual_html = get_slide_43_multi_agent_mermaid()
        elif i == 43:
            visual_html = get_slide_44_mcp_mermaid()
        elif i == 45:
            visual_html = get_slide_46_deflection_chart(sec)
        elif i == 46:
            visual_html = get_slide_47_integration_mermaid(core)

        if visual_html:
            # For slides with primary charts or mermaid diagrams: Top KPI + Diagram + Bottom Banner
            slides[i]["content"] = f"""
            {kpi_ribbon}
            {visual_html}
            {bottom_banner}
            """
        else:
            # For all other slides: Keep the rich original content, inject CLI tool box and wrap in 3-tier structure
            orig = slides[i].get("content", "").strip()
            cli_info = cli_map.get(i)
            terminal_html = ""
            if cli_info:
                t_title, t_cmd, t_out, t_comm = cli_info
                terminal_html = get_terminal_box(t_title, t_cmd, t_out, t_comm)

            # Assemble content: Top KPI + Original Content + Terminal Box + Bottom Banner
            slides[i]["content"] = f"""
            {kpi_ribbon}
            <div style="flex: 1 1 0; min-height: 0; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
              {orig}
              {terminal_html}
            </div>
            {bottom_banner}
            """

    return slides

if __name__ == "__main__":
    print("Visual Slide Components module ready.")
