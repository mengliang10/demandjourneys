#!/usr/bin/env python3
"""
Updates navigation links across Labs suite to link the new Tech Stack Explorers
and Cross-Industry Benchmark Compendiums.
"""

import os

BASE_DIR = "/run/media/ml/Storage/Labs"

# 1. Update root index.html
root_index_path = os.path.join(BASE_DIR, "index.html")
with open(root_index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add link to top nav
if "CROSS_INDUSTRY_ENTERPRISE_TECH_STACK_BENCHMARK.md" not in content:
    content = content.replace(
        '<a href="VISUALIZATION_AND_PRESENTATION_FRAMEWORKS_COMPENDIUM.md" class="nav-link">📚 Frameworks Compendium</a>',
        '<a href="CROSS_INDUSTRY_ENTERPRISE_TECH_STACK_BENCHMARK.md" class="nav-link">🔬 Enterprise Tech Stacks</a>\n        <a href="VISUALIZATION_AND_PRESENTATION_FRAMEWORKS_COMPENDIUM.md" class="nav-link">📚 Frameworks Compendium</a>'
    )

# Add Tech Stack Explorer button to Hotels card
if 'href="hotels/tech_stack.html"' not in content:
    content = content.replace(
        '<a href="hotels/index.html" class="btn-launch btn-hotels">Launch Full Hotels Dashboard ➔</a>',
        '<a href="hotels/index.html" class="btn-launch btn-hotels">Launch Full Hotels Dashboard ➔</a>\n          <a href="hotels/tech_stack.html" class="btn-launch" style="background: rgba(37, 99, 235, 0.2); border: 1px solid #3b82f6; color: #93c5fd; margin-bottom: 0.75rem;">⚙️ Hotels Enterprise Tech Stack (13 Layers) ➔</a>'
    )

# Add Tech Stack Explorer button to Cruises card
if 'href="cruises/tech_stack.html"' not in content:
    content = content.replace(
        '<a href="cruises/index.html" class="btn-launch btn-cruises">Launch Full Cruises Dashboard ➔</a>',
        '<a href="cruises/index.html" class="btn-launch btn-cruises">Launch Full Cruises Dashboard ➔</a>\n          <a href="cruises/tech_stack.html" class="btn-launch" style="background: rgba(8, 145, 178, 0.2); border: 1px solid #06b6d4; color: #67e8f9; margin-bottom: 0.75rem;">⚙️ Cruises Enterprise Tech Stack (13 Layers) ➔</a>'
    )

# Add Tech Stack Explorer button to Airlines card
if 'href="airlines/tech_stack.html"' not in content:
    content = content.replace(
        '<a href="airlines/index.html" class="btn-launch btn-airlines">Launch Full Airlines Dashboard ➔</a>',
        '<a href="airlines/index.html" class="btn-launch btn-airlines">Launch Full Airlines Dashboard ➔</a>\n          <a href="airlines/tech_stack.html" class="btn-launch" style="background: rgba(124, 58, 237, 0.2); border: 1px solid #8b5cf6; color: #c4b5fd; margin-bottom: 0.75rem;">⚙️ Airlines Enterprise Tech Stack (13 Layers) ➔</a>'
    )

# Add Tech Stack Explorer button to Tours card
if 'href="tours/tech_stack.html"' not in content:
    content = content.replace(
        '<a href="tours/index.html" class="btn-launch btn-tours">Launch Full Tours Dashboard ➔</a>',
        '<a href="tours/index.html" class="btn-launch btn-tours">Launch Full Tours Dashboard ➔</a>\n          <a href="tours/tech_stack.html" class="btn-launch" style="background: rgba(5, 150, 105, 0.2); border: 1px solid #10b981; color: #6ee7b7; margin-bottom: 0.75rem;">⚙️ Tours Enterprise Tech Stack (13 Layers) ➔</a>'
    )

with open(root_index_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Updated {root_index_path}")

# 2. Update sector index.html files
for sector in ["hotels", "airlines", "cruises", "tours"]:
    sector_index = os.path.join(BASE_DIR, sector, "index.html")
    if os.path.exists(sector_index):
        with open(sector_index, "r", encoding="utf-8") as f:
            sec_content = f.read()
        
        # Add badge button in header if not present
        if 'href="tech_stack.html"' not in sec_content:
            target_str = '<div style="display: flex; gap: 0.5rem;">'
            replacement = '<div style="display: flex; gap: 0.5rem; align-items: center;">\n        <a href="tech_stack.html" class="badge-tag badge-blue" style="text-decoration: none; font-weight: 700; border: 1px solid #3b82f6;">⚙️ Enterprise Tech Stack (13 Layers) ➔</a>'
            sec_content = sec_content.replace(target_str, replacement, 1)
            
            with open(sector_index, "w", encoding="utf-8") as f:
                f.write(sec_content)
            print(f"Updated {sector_index}")

print("Navigation links updated successfully.")
