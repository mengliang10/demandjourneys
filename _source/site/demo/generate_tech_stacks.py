#!/usr/bin/env python3
"""
Enterprise Tech Stack Data Definitions and Generator for Travel, Transportation & Hospitality Labs
Covers Airlines, Cruises, Hotels, and Tours across 3 variations:
1. With Salesforce
2. Without Salesforce (Best-of-Breed Modern Open/Enterprise)
3. The Best Platforms Money Can Buy (Ultra-Tier Sovereign / High-Roller Enterprise Pinnacle)
"""

import os
import json

BASE_DIR = "/run/media/ml/Storage/Labs"

def get_layer_definitions():
    return [
        {"id": "core_ops", "name": "1. Core Industry Operational Stack", "icon": "⚙️", "desc": "Mission-critical industry core: PSS, PMS, CRS, Booking Engines, DCS, Marine Ops, Fleet & Guide Dispatch"},
        {"id": "marketing", "name": "2. Marketing Automation & AdTech", "icon": "📣", "desc": "Omni-channel journey orchestration, email/SMS/push/WhatsApp, adtech syndication, attribution & personalization"},
        {"id": "crm_service", "name": "3. CRM & Omni-Channel Service Desk", "icon": "🎧", "desc": "Customer case management, agent desktop, contact center telephony/CTI, digital messaging & VIP host desk"},
        {"id": "loyalty", "name": "4. Loyalty Management & Gamification", "icon": "💎", "desc": "Frequent traveler points/miles ledger, tier management, coalition partner earn/burn, promotions & co-brand credit cards"},
        {"id": "cdp", "name": "5. Customer Data Platform (CDP) & Identity", "icon": "🧬", "desc": "Streaming event ingestion, deterministic/probabilistic identity graph, golden profile & consent governance"},
        {"id": "integration", "name": "6. API Gateway, Integration & Event Mesh", "icon": "🔌", "desc": "Universal API management, iPaaS, Kafka/event streaming, legacy protocol adaptation (EDIFACT/OXI/OTA XML/NDC)"},
        {"id": "cloud_data", "name": "7. Cloud Infrastructure & Lakehouse", "icon": "☁️", "desc": "Multi-cloud compute, serverless, relational DBs, analytical lakehouse (Snowflake/Databricks), real-time query engines"},
        {"id": "ai_ml", "name": "8. AI, Machine Learning & Agentic Systems", "icon": "🤖", "desc": "Generative AI, frontier LLMs, autonomous reasoning agents, predictive models (pricing/churn/delays), MCP servers"},
        {"id": "frontends", "name": "9. Website, Mobile Apps & Digital Front-Ends", "icon": "📱", "desc": "Brand responsive web booking engines, native iOS/Android apps, check-in kiosks, digital key/boarding pass wallets"},
        {"id": "cms_dxp", "name": "10. Headless CMS, DXP & Digital Asset Mgmt", "icon": "🎨", "desc": "Headless content repositories, multi-lingual localization, enterprise DAM, CDN edge delivery"},
        {"id": "finance_erp", "name": "11. Finance, Revenue Accounting, ERP & Billing", "icon": "💳", "desc": "ASC 606 / IFRS 15 revenue recognition, general ledger, payment gateways (Adyen/Stripe), global tax & fraud engines"},
        {"id": "hr_workforce", "name": "12. HR, Workforce Mgmt & Crew Scheduling", "icon": "👥", "desc": "Core HRIS, employee portals, union/aviation/maritime work-hour compliance, shift bidding, global payroll"},
        {"id": "governance", "name": "13. Enterprise Governance, Security & Privacy", "icon": "🛡️", "desc": "GDPR/PDPA/UU PDP privacy, PCI-DSS Level 1 tokenization, SOC2 Type II, IAM (Okta), Zero-Trust & HSM key mgmt"}
    ]

print("Layer definitions loaded.")
