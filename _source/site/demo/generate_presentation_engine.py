#!/usr/bin/env python3
"""
Presentation Engine for Travel & Hospitality Labs
Renders 50+ slide Reveal.js presentations and Markdown compendiums.
"""

import os
import json

def render_reveal_html(industry_meta, slides, output_path):
    """
    Renders an interactive Reveal.js HTML file with dark glassmorphic styling,
    Mermaid.js diagramming support, slide counter, and quick navigation jump.
    """
    slides_html = []
    
    for idx, slide in enumerate(slides, 1):
        slide_id = f"slide-{idx}"
        part_tag = slide.get("part", "OVERVIEW")
        title = slide.get("title", f"Slide {idx}")
        subtitle = slide.get("subtitle", "")
        content = slide.get("content", "")
        notes = slide.get("notes", "")

        slide_html = f"""
      <!-- Slide {idx}: {title} -->
      <section id="{slide_id}" data-transition="slide" style="text-align: left;">
        <div class="slide-header">
          <div class="slide-meta">
            <span class="badge-part">{part_tag}</span>
            <span class="badge-num">SLIDE {idx} / {len(slides)}</span>
          </div>
          <h2 class="slide-title">{title}</h2>
          {f'<div class="slide-subtitle">{subtitle}</div>' if subtitle else ''}
        </div>
        <div class="slide-body">
          {content}
        </div>
        {f'<aside class="notes">{notes}</aside>' if notes else ''}
      </section>"""
        slides_html.append(slide_html)

    all_slides_markup = "\n".join(slides_html)

    # Jump dropdown options
    jump_options = "\n".join([
        f'<option value="#/slide-{i+1}">{i+1}. {s.get("title", "")[:45]}</option>'
        for i, s in enumerate(slides)
    ])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{industry_meta['title']} — Executive Architecture Presentation</title>
  
  <!-- Reveal.js CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/theme/black.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/plugin/highlight/monokai.min.css">

  <!-- Custom Presentation Styles -->
  <style>
    :root {{
      --bg-color: #0b0f19;
      --card-bg: rgba(17, 24, 39, 0.85);
      --card-border: rgba(75, 85, 99, 0.4);
      --accent-blue: #3b82f6;
      --accent-cyan: #06b6d4;
      --accent-purple: #8b5cf6;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --text-main: #f9fafb;
      --text-muted: #94a3b8;
    }}

    .reveal {{
      background: radial-gradient(circle at 50% 18%, #141d31 0%, #0c101b 65%, #06080d 100%);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}

    .reveal .slides {{
      text-align: left;
    }}

    /* Full-Height Slide Section Architecture */
    .reveal .slides section {{
      width: 100% !important;
      height: 100% !important;
      top: 0 !important;
      left: 0 !important;
      padding: 22px 36px 26px 36px !important;
      box-sizing: border-box !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: flex-start !important;
      text-align: left !important;
    }}

    /* Slide Header */
    .slide-header {{
      flex-shrink: 0;
      margin-bottom: 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 6px;
    }}
    .slide-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}
    .badge-part {{
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(37, 99, 235, 0.15));
      color: #93c5fd;
      border: 1px solid rgba(59, 130, 246, 0.4);
      padding: 3px 10px;
      border-radius: 6px;
      box-shadow: 0 0 12px rgba(59, 130, 246, 0.15);
    }}
    .badge-num {{
      font-size: 0.75rem;
      color: #94a3b8;
      font-family: 'JetBrains Mono', 'Fira Code', monospace;
      font-weight: 600;
    }}
    .slide-title {{
      font-size: 1.6rem !important;
      font-weight: 800 !important;
      line-height: 1.15 !important;
      margin: 0 !important;
      text-transform: none !important;
      letter-spacing: -0.025em !important;
      background: linear-gradient(135deg, #ffffff 40%, #93c5fd 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .slide-subtitle {{
      font-size: 1.02rem;
      color: #94a3b8;
      margin-top: 4px;
      line-height: 1.35;
      font-weight: 400;
    }}

    /* Slide Body & Dynamic Vertical Stretch */
    .slide-body {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      min-height: 0;
      font-size: 0.9rem;
      line-height: 1.55;
      color: #cbd5e1;
    }}

    /* Grids */
    .grid-2, .grid-3, .grid-4, .grid-1-2, .grid-2-1 {{
      display: grid;
      gap: 16px;
      width: 100%;
    }}
    .grid-2 {{ grid-template-columns: 1fr 1fr; }}
    .grid-3 {{ grid-template-columns: 1fr 1fr 1fr; }}
    .grid-4 {{ grid-template-columns: repeat(4, 1fr); }}
    .grid-1-2 {{ grid-template-columns: 1fr 2fr; }}
    .grid-2-1 {{ grid-template-columns: 2fr 1fr; }}

    .slide-body > .grid-2,
    .slide-body > .grid-3,
    .slide-body > .grid-1-2,
    .slide-body > .grid-2-1 {{
      flex: 1 1 0;
      min-height: 0;
    }}

    .slide-body > .grid-4 {{
      flex: 0 0 auto;
    }}

    .slide-body > :only-child {{
      flex: 1 1 0;
      height: 100%;
    }}

    /* Glass Cards */
    .glass-card {{
      background: linear-gradient(145deg, rgba(20, 27, 45, 0.85) 0%, rgba(11, 16, 28, 0.95) 100%);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-top: 1px solid rgba(59, 130, 246, 0.35);
      border-radius: 12px;
      padding: 14px 18px;
      box-shadow: 0 12px 30px -8px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(14px);
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 8px;
      box-sizing: border-box;
      overflow: auto;
      height: 100%;
      transition: border-color 0.25s ease, box-shadow 0.25s ease;
    }}
    .glass-card:hover {{
      border-color: rgba(59, 130, 246, 0.5);
      box-shadow: 0 16px 36px -8px rgba(59, 130, 246, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.15);
    }}

    /* Bottom Strategic Outcome Banner */
    .bottom-banner {{
      flex: 0 0 auto;
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-left: 4px solid #38bdf8;
      border-radius: 8px;
      padding: 8px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      font-size: 0.78rem;
      line-height: 1.35;
      color: #e2e8f0;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
    }}
    .bottom-banner strong {{
      color: #38bdf8;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      font-size: 0.72rem;
      margin-right: 6px;
    }}
    .bottom-banner.green {{ border-left-color: #10b981; }}
    .bottom-banner.green strong {{ color: #34d399; }}
    .bottom-banner.purple {{ border-left-color: #8b5cf6; }}
    .bottom-banner.purple strong {{ color: #a78bfa; }}
    .bottom-banner.amber {{ border-left-color: #f59e0b; }}
    .bottom-banner.amber strong {{ color: #fbbf24; }}

    /* Terminal / CLI Mockup Window */
    .terminal-box {{
      background: #0d1117;
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      overflow: hidden;
      font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', Consolas, monospace;
      font-size: 0.74rem;
      line-height: 1.45;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
      margin: 4px 0;
    }}
    .terminal-header {{
      background: #161b22;
      padding: 5px 10px;
      display: flex;
      align-items: center;
      gap: 6px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .terminal-dot {{
      width: 9px;
      height: 9px;
      border-radius: 50%;
      display: inline-block;
    }}
    .terminal-dot.red {{ background: #ff5f56; }}
    .terminal-dot.yellow {{ background: #ffbd2e; }}
    .terminal-dot.green {{ background: #27c93f; }}
    .terminal-title {{
      font-size: 0.65rem;
      color: #8b949e;
      margin-left: 6px;
      font-weight: 600;
      letter-spacing: 0.03em;
    }}
    .terminal-body {{
      padding: 8px 12px;
      color: #c9d1d9;
      background: #0d1117;
      white-space: pre-wrap;
      word-break: break-word;
    }}
    .terminal-body .prompt {{
      color: #58a6ff;
      font-weight: 700;
      user-select: none;
    }}
    .terminal-body .cmd {{
      color: #7ee787;
      font-weight: 600;
    }}
    .terminal-body .comment {{
      color: #8b949e;
      font-style: italic;
    }}
    .terminal-body .output {{
      color: #e6edf3;
    }}

    .card-header {{
      font-size: 0.92rem;
      font-weight: 700;
      color: #38bdf8;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
      padding-bottom: 6px;
      flex-shrink: 0;
    }}

    /* Metrics & Numbers */
    .metric-hero {{
      font-size: 2.6rem;
      font-weight: 800;
      color: #38bdf8;
      line-height: 1.05;
      letter-spacing: -0.02em;
      margin-bottom: 4px;
    }}
    .metric-sub {{
      font-size: 0.78rem;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }}

    /* Data Tables */
    .data-table {{
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 0.82rem;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .data-table th {{
      background: rgba(30, 41, 59, 0.95);
      color: #38bdf8;
      padding: 8px 12px;
      text-align: left;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.74rem;
      letter-spacing: 0.04em;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .data-table td {{
      padding: 7px 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      color: #cbd5e1;
      line-height: 1.4;
    }}
    .data-table tr:last-child td {{
      border-bottom: none;
    }}
    .data-table tr:nth-child(even) td {{
      background: rgba(255, 255, 255, 0.02);
    }}
    .data-table tr:hover td {{
      background: rgba(59, 130, 246, 0.08);
    }}

    /* Badges & Pills */
    .pill {{
      display: inline-flex;
      align-items: center;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.74rem;
      font-weight: 600;
      margin-right: 6px;
      margin-bottom: 6px;
      letter-spacing: 0.02em;
      transition: transform 0.15s ease;
    }}
    .pill:hover {{
      transform: translateY(-1px);
    }}
    .pill-blue {{ background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); }}
    .pill-green {{ background: rgba(16, 185, 129, 0.2); color: #a7f3d0; border: 1px solid rgba(16, 185, 129, 0.4); }}
    .pill-purple {{ background: rgba(139, 92, 246, 0.2); color: #ddd6fe; border: 1px solid rgba(139, 92, 246, 0.4); }}
    .pill-amber {{ background: rgba(245, 158, 11, 0.2); color: #fde68a; border: 1px solid rgba(245, 158, 11, 0.4); }}
    .pill-red {{ background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); }}

    /* Flow Callout */
    .flow-step {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 10px;
      font-size: 0.86rem;
      line-height: 1.45;
    }}
    .step-num {{
      background: linear-gradient(135deg, #3b82f6, #1d4ed8);
      color: #fff;
      font-size: 0.72rem;
      font-weight: 700;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
      box-shadow: 0 0 10px rgba(59, 130, 246, 0.4);
    }}

    /* Mermaid Diagrams in Reveal */
    .mermaid {{
      font-size: 0.82rem !important;
      background: rgba(11, 16, 28, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 10px;
      border-radius: 10px;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
      box-sizing: border-box;
      overflow: auto;
    }}
    .mermaid svg {{
      max-width: 100% !important;
      max-height: 100% !important;
      height: auto !important;
    }}

    /* ─── VISUAL DENSITY UTILITIES ─── */

    /* Gradient Progress Bars */
    .progress-bar {{
      height: 18px;
      background: rgba(255,255,255,0.06);
      border-radius: 9px;
      overflow: hidden;
      margin: 4px 0;
      position: relative;
    }}
    .progress-fill {{
      height: 100%;
      border-radius: 9px;
      transition: width 0.8s ease;
      display: flex;
      align-items: center;
      padding-left: 8px;
      font-size: 0.65rem;
      font-weight: 700;
      color: #fff;
    }}
    .progress-fill.blue {{ background: linear-gradient(90deg, #3b82f6, #60a5fa); }}
    .progress-fill.green {{ background: linear-gradient(90deg, #10b981, #34d399); }}
    .progress-fill.purple {{ background: linear-gradient(90deg, #8b5cf6, #a78bfa); }}
    .progress-fill.amber {{ background: linear-gradient(90deg, #f59e0b, #fbbf24); }}
    .progress-fill.red {{ background: linear-gradient(90deg, #ef4444, #f87171); }}
    .progress-fill.cyan {{ background: linear-gradient(90deg, #06b6d4, #22d3ee); }}

    /* KPI Stat Widgets */
    .kpi-row {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .kpi-box {{
      flex: 1;
      min-width: 110px;
      background: linear-gradient(145deg, rgba(30,41,59,0.9), rgba(15,23,42,0.95));
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 10px;
      padding: 10px 14px;
      text-align: center;
    }}
    .kpi-value {{
      font-size: 1.8rem;
      font-weight: 800;
      color: #38bdf8;
      line-height: 1.1;
    }}
    .kpi-label {{
      font-size: 0.62rem;
      font-weight: 600;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-top: 3px;
    }}
    .kpi-delta {{
      font-size: 0.6rem;
      font-weight: 700;
      margin-top: 2px;
    }}
    .kpi-delta.up {{ color: #34d399; }}
    .kpi-delta.down {{ color: #f87171; }}

    /* Heat Map Table Enhancement */
    .heat-cell {{
      padding: 5px 8px !important;
      text-align: center !important;
      font-weight: 600 !important;
    }}
    .heat-high {{ background: rgba(16, 185, 129, 0.25) !important; color: #a7f3d0 !important; }}
    .heat-med {{ background: rgba(245, 158, 11, 0.2) !important; color: #fde68a !important; }}
    .heat-low {{ background: rgba(239, 68, 68, 0.2) !important; color: #fca5a5 !important; }}

    /* Status Indicators */
    .status-dot {{
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      margin-right: 6px;
    }}
    .status-dot.green {{ background: #34d399; box-shadow: 0 0 6px rgba(52,211,153,0.5); }}
    .status-dot.amber {{ background: #fbbf24; box-shadow: 0 0 6px rgba(251,191,36,0.5); }}
    .status-dot.red {{ background: #f87171; box-shadow: 0 0 6px rgba(248,113,113,0.5); }}
    .status-dot.blue {{ background: #60a5fa; box-shadow: 0 0 6px rgba(96,165,250,0.5); }}

    /* Icon-Stat Compact Cards */
    .stat-icon-card {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      background: rgba(30,41,59,0.6);
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.06);
      margin-bottom: 6px;
    }}
    .stat-icon {{
      font-size: 1.4rem;
      flex-shrink: 0;
    }}
    .stat-detail {{
      flex: 1;
    }}
    .stat-detail .val {{
      font-size: 1.1rem;
      font-weight: 800;
      color: #f9fafb;
      line-height: 1.1;
    }}
    .stat-detail .lbl {{
      font-size: 0.62rem;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    /* Comparison Grid */
    .compare-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 8px;
    }}
    .compare-col {{
      background: rgba(30,41,59,0.6);
      border: 1px solid rgba(255,255,255,0.06);
      border-radius: 10px;
      padding: 10px;
    }}
    .compare-col.highlight {{
      border-color: rgba(59,130,246,0.5);
      box-shadow: 0 0 20px rgba(59,130,246,0.1);
    }}
    .compare-header {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #38bdf8;
      margin-bottom: 8px;
      padding-bottom: 4px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }}

    /* Timeline / Roadmap Nodes */
    .timeline {{
      display: flex;
      gap: 0;
      align-items: flex-start;
    }}
    .timeline-node {{
      flex: 1;
      text-align: center;
      position: relative;
      padding: 0 8px;
    }}
    .timeline-node::before {{
      content: '';
      position: absolute;
      top: 16px;
      left: 0;
      right: 0;
      height: 3px;
      background: rgba(59,130,246,0.3);
    }}
    .timeline-node:first-child::before {{
      left: 50%;
    }}
    .timeline-node:last-child::before {{
      right: 50%;
    }}
    .timeline-dot {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: linear-gradient(135deg, #3b82f6, #1d4ed8);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.7rem;
      font-weight: 700;
      color: #fff;
      margin: 0 auto 6px;
      position: relative;
      z-index: 1;
    }}
    .timeline-label {{
      font-size: 0.65rem;
      font-weight: 600;
      color: #94a3b8;
      line-height: 1.3;
    }}

    /* Micro Chart Container */
    .chart-container {{
      position: relative;
      min-height: 180px;
      flex: 1;
    }}

    /* Gradient Accent Borders for variation */
    .accent-green {{ border-top-color: rgba(16, 185, 129, 0.5) !important; }}
    .accent-purple {{ border-top-color: rgba(139, 92, 246, 0.5) !important; }}
    .accent-amber {{ border-top-color: rgba(245, 158, 11, 0.5) !important; }}
    .accent-red {{ border-top-color: rgba(239, 68, 68, 0.5) !important; }}
    .accent-cyan {{ border-top-color: rgba(6, 182, 212, 0.5) !important; }}

    /* Custom Floating HUD Controls */
    .custom-controls {{
      position: fixed;
      bottom: 14px;
      left: 18px;
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(14px);
      padding: 6px 14px;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
      font-size: 0.78rem;
    }}
    .custom-controls select {{
      background: #1e293b;
      color: #f8fafc;
      border: 1px solid #475569;
      border-radius: 6px;
      padding: 4px 8px;
      font-size: 0.75rem;
      max-width: 280px;
      outline: none;
    }}
    .custom-controls a {{
      color: #38bdf8;
      text-decoration: none;
      font-weight: 600;
      transition: color 0.15s ease;
    }}
    .custom-controls a:hover {{
      color: #7dd3fc;
      text-decoration: underline;
    }}

    /* Progress bar */
    .reveal .progress {{
      height: 4px;
      background: rgba(255, 255, 255, 0.1);
    }}
    .reveal .progress span {{
      background: linear-gradient(90deg, #38bdf8, #3b82f6);
    }}

    /* Mermaid in Reveal fix: ensure visibility for rendering */
    /* Mermaid in Reveal fix: ensure visibility for rendering */
    .mermaid svg {{
      max-width: 100% !important;
      max-height: 100% !important;
    }}
  </style>

  <!-- Chart.js and Plotly MUST load in head so they are available for inline scripts -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js"></script>
  <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
</head>
<body>

  <div class="reveal">
    <div class="slides">
      {all_slides_markup}
    </div>
  </div>

  <!-- Quick Slide Navigator & Navigation Bar -->
  <div class="custom-controls">
    <span style="color: #60a5fa; font-weight: 700;">{industry_meta['short_code']} LABS</span>
    <select id="slide-jump" onchange="Reveal.slide(parseInt(this.value.replace('#/slide-', '')) - 1)">
      {jump_options}
    </select>
    <span>|</span>
    <a href="index.html">📊 Lab Hub</a>
    <span>|</span>
    <a href="tech_stack.html">⚙️ Tech Stack</a>
    <span>|</span>
    <a href="PRESENTATION_FRAMEWORK_COMPENDIUM.md" target="_blank">📄 Compendium MD</a>
  </div>

  <!-- Reveal.js and Plugins -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/plugin/notes/notes.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/plugin/markdown/markdown.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/plugin/highlight/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>

  <script>
    // Chart.js dark defaults (loaded in head, so always available)
    if (typeof Chart !== 'undefined') {{
      Chart.defaults.color = '#94a3b8';
      Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.08)';
      Chart.defaults.font.family = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
    }}

    // Mermaid: initialize but do NOT auto-render (we render per-slide)
    mermaid.initialize({{
      startOnLoad: false,
      theme: 'dark',
      themeVariables: {{
        primaryColor: '#1e3a8a',
        primaryBorderColor: '#3b82f6',
        primaryTextColor: '#f9fafb',
        lineColor: '#475569',
        secondaryColor: '#4c1d95',
        tertiaryColor: '#064e3b',
        fontFamily: '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif',
        fontSize: '13px'
      }},
      flowchart: {{ htmlLabels: true, curve: 'basis', useMaxWidth: true }},
      sequence: {{ useMaxWidth: true }},
      gantt: {{ useMaxWidth: true }}
    }});

    // Track which slides have been rendered
    const renderedSlides = new Set();

    async function renderSlide(slide) {{
      const slideId = slide.id || 'unknown';
      if (renderedSlides.has(slideId)) return;
      renderedSlides.add(slideId);

      // Render mermaid diagrams in this slide
      const mermaidDivs = slide.querySelectorAll('.mermaid:not([data-processed])');
      for (const div of mermaidDivs) {{
        try {{
          const id = 'mermaid-' + Math.random().toString(36).substr(2, 9);
          const graphDef = div.textContent.trim();
          div.textContent = '';
          const {{ svg }} = await mermaid.render(id, graphDef);
          div.innerHTML = svg;
          div.setAttribute('data-processed', 'true');
        }} catch (e) {{
          console.warn('Mermaid render error on', slideId, e);
          div.setAttribute('data-processed', 'true');
        }}
      }}

      // Resize any Chart.js canvases
      const canvases = slide.querySelectorAll('canvas');
      canvases.forEach(c => {{
        if (c.chartInstance) c.chartInstance.resize();
      }});
    }}

    Reveal.initialize({{
      hash: true,
      slideNumber: 'c/t',
      overview: true,
      center: false,
      transition: 'slide',
      backgroundTransition: 'fade',
      width: 1600,
      height: 900,
      margin: 0.04,
      minScale: 0.2,
      maxScale: 2.0,
      plugins: [ RevealHighlight, RevealNotes ]
    }}).then(() => {{
      // Render the first visible slide
      const currentSlide = Reveal.getCurrentSlide();
      if (currentSlide) renderSlide(currentSlide);

      // Render on every slide change
      Reveal.on('slidechanged', event => {{
        const select = document.getElementById('slide-jump');
        if (select) select.value = '#/slide-' + (event.indexh + 1);
        renderSlide(event.currentSlide);
      }});
    }});
  </script>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Reveal.js Presentation ({len(slides)} slides) at: {output_path}")


def render_presentation_markdown(industry_meta, slides, output_path):
    """
    Renders a companion markdown file with all 50+ slides documented in detail.
    """
    md = []
    md.append(f"# {industry_meta['title']} — Master Presentation Framework & Slides Compendium")
    md.append(f"\n> **Executive Reference**: Complete transcript and architectural documentation for the **50+ Slide Reveal.js Presentation** covering requirements, IT standards, systems architecture, customer journeys, workflows, AI orchestration, and integration topology.\n")
    md.append(f"- **Sector**: {industry_meta['sector']}")
    md.append(f"- **Scale Baseline**: {industry_meta['scale']}")
    md.append(f"- **Slide Count**: {len(slides)} Dense Slides")
    md.append(f"- **Interactive Presentation**: [`presentation.html`](presentation.html)\n")
    md.append("---\n")

    current_part = None
    for idx, slide in enumerate(slides, 1):
        part = slide.get("part", "GENERAL")
        if part != current_part:
            current_part = part
            md.append(f"\n## {current_part}\n")

        md.append(f"### Slide {idx}: {slide['title']}")
        if slide.get("subtitle"):
            md.append(f"*{slide['subtitle']}*\n")
        
        # Clean HTML tags for markdown text presentation
        clean_content = slide.get("content", "")
        import re
        # Preserve Mermaid diagrams as Markdown code fences
        clean_content = re.sub(r'<div class="mermaid">\s*(.*?)\s*</div>', r'\n```mermaid\n\1\n```\n', clean_content, flags=re.DOTALL)
        # Strip script and canvas tags
        clean_content = re.sub(r'<script.*?</script>', '', clean_content, flags=re.DOTALL)
        clean_content = re.sub(r'<canvas.*?</canvas>', '', clean_content, flags=re.DOTALL)
        # Remove simple HTML tags for cleaner reading in MD
        text_content = re.sub(r'<div[^>]*>', '', clean_content)
        text_content = re.sub(r'</div>', '', text_content)
        text_content = re.sub(r'<span[^>]*>', '', text_content)
        text_content = re.sub(r'</span>', '', text_content)
        text_content = re.sub(r'<h[1-6][^>]*>', '#### ', text_content)
        text_content = re.sub(r'</h[1-6]>', '\n', text_content)
        text_content = re.sub(r'<p[^>]*>', '', text_content)
        text_content = re.sub(r'</p>', '\n', text_content)
        text_content = re.sub(r'<br\s*/?>', '\n', text_content)
        text_content = re.sub(r'<strong>', '**', text_content)
        text_content = re.sub(r'</strong>', '**', text_content)
        text_content = re.sub(r'<em>', '*', text_content)
        text_content = re.sub(r'</em>', '*', text_content)
        
        md.append(text_content.strip())
        if slide.get("notes"):
            md.append(f"\n> **Presenter Notes**: {slide['notes']}\n")
        md.append("\n---\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"Generated Presentation Markdown ({len(slides)} slides) at: {output_path}")
