const AIRLINES_TECH_STACK_DATA = {
  "sector": "Airlines & Commercial Aviation",
  "market_context": {
    "global_scale": "$800.0B Passenger GBV (4.6B Departures)",
    "passenger_volume": "4.6 Billion Annual Passengers",
    "blended_fare_ancillary": "$173.91 per passenger",
    "ancillary_share": "$160.0B (20.0% of total revenue)",
    "distribution_cost": "$46.4B (5.8% friction)",
    "net_passenger_revenue": "$753.6B (94.2% retained)"
  },
  "variations": [
    {
      "id": "var_salesforce",
      "name": "Variation 1: With Salesforce",
      "tagline": "The Salesforce-Centric Enterprise Aviation Ecosystem",
      "summary": "Deeply unified enterprise architecture leveraging Salesforce Data Cloud as the passenger data fabric, Agentforce for autonomous IROPS and servicing, Service Cloud Voice, Marketing Cloud, and MuleSoft Direct for Amadeus/SITA, layered on industry core PSS/DCS.",
      "total_acv_usd": "$12,450,000 - $18,800,000 / year",
      "implementation_capex_usd": "$14,000,000 - $22,000,000",
      "annual_run_cost_usd": "$4,500,000 - $7,200,000 / year",
      "projected_roi": "310% over 3 years with 11-month payback period",
      "primary_moat": "Zero-Copy Data Cloud harmonization, native Agentforce autonomous multi-agent reasoning, and MuleSoft pre-built connectors to Amadeus Alt\u00e9a and SITA."
    },
    {
      "id": "var_no_salesforce",
      "name": "Variation 2: Without Salesforce (Best-of-Breed Open/Enterprise)",
      "tagline": "Modern Best-of-Breed Composable Aviation Stack",
      "summary": "Decoupled, best-of-breed architecture utilizing Snowflake/Databricks, Twilio Segment/mParticle CDP, Braze for real-time streaming marketing, Microsoft Dynamics 365 / Zendesk for contact centers, Talon.One for dynamic loyalty, and Confluent Kafka event mesh.",
      "total_acv_usd": "$9,800,000 - $15,200,000 / year",
      "implementation_capex_usd": "$16,500,000 - $26,000,000",
      "annual_run_cost_usd": "$6,200,000 - $9,500,000 / year",
      "projected_roi": "245% over 3 years with 15-month payback period",
      "primary_moat": "Complete vendor independence, open-source flexibility, custom fine-tuned LLM agents on AWS Bedrock/Databricks, and zero vendor lock-in."
    },
    {
      "id": "var_best_money_can_buy",
      "name": "Variation 3: The Best Platforms Money Can Buy",
      "tagline": "Ultra-Tier Sovereign & High-Roller Enterprise Pinnacle",
      "summary": "Unconstrained budget, sovereign-grade aviation architecture combining Palantir Foundry / AIP for operational ontology and autonomous IROPS, Adobe Experience Cloud (AEP + AJO + AEM), Databricks Lakehouse with dedicated NVIDIA DGX clusters, Genesys Cloud CX with Google CCAI, and Private Cloud Amadeus Alt\u00e9a.",
      "total_acv_usd": "$28,500,000 - $45,000,000 / year",
      "implementation_capex_usd": "$35,000,000 - $60,000,000",
      "annual_run_cost_usd": "$12,000,000 - $18,500,000 / year",
      "projected_roi": "420% over 3 years with 14-month payback period via massive IROPS cost avoidance and premium yield maximization",
      "primary_moat": "Military-grade data ontology (Palantir), sub-second real-time streaming personalization (Adobe AEP), sovereign cloud isolation, and carrier-grade operational resilience."
    }
  ],
  "layers": [
    {
      "layer_id": "core_ops",
      "name": "1. Core Industry Operational Stack",
      "icon": "\u2699\ufe0f",
      "desc": "Passenger Service Systems (PSS), Departure Control Systems (DCS), Flight Operations, MRO & Crew Tracking",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Amadeus Alt\u00e9a PSS (or SabreSonic)",
              "vendor": "Amadeus IT Group / Sabre",
              "role": "Core Reservations, Inventory & Ticketing (e-Ticket/EMD)"
            },
            {
              "name": "Amadeus Alt\u00e9a DCS",
              "vendor": "Amadeus",
              "role": "Airport Departure Control, Weight & Balance, Passenger Check-in"
            },
            {
              "name": "SITA WorldTracer & BagJourney",
              "vendor": "SITA",
              "role": "Global Lost Luggage Tracing & Real-Time RFID Telemetry"
            },
            {
              "name": "Sabre Movement Manager / Lido Flight 4D",
              "vendor": "Sabre / Lufthansa Systems",
              "role": "Flight Dispatch, Operational Control & Weather Tracking"
            },
            {
              "name": "Swiss-AS AMOS",
              "vendor": "Swiss Aviation Software",
              "role": "Aircraft Maintenance, Repair & Overhaul (MRO) Technical Operations"
            },
            {
              "name": "Jeppesen Crew Tracking",
              "vendor": "Boeing Digital Solutions",
              "role": "Pilot & Cabin Crew Legality, Roster Bidding & Fatigue Management"
            }
          ],
          "licensing_acv": "$18,000,000 - $32,000,000 (Transactional fee per passenger boarded: ~$0.55 - $0.85)",
          "implementation_capex": "$15,000,000 - $30,000,000 (Multi-year PSS cutover)",
          "annual_run_cost": "$5,000,000 / year",
          "data_handled": "PNR records, 13-digit e-Ticket numbers, EMDs, IATA seat maps, weight & balance trim sheets, aircraft tail number telemetry, RFID bag tags, pilot duty logs, FAR Part 117 / EASA FTL flight time limitations.",
          "purpose": "Executes all mission-critical operational flight execution, inventory availability, seat allocation, passenger boarding, baggage sorting, and aircraft airworthiness certification.",
          "business_value": "The foundational revenue and operational spine of the airline. Without PSS/DCS, no aircraft departs, no ticket is issued, and no flight plan is filed.",
          "integration_specs": "MuleSoft Direct for Amadeus connects Alt\u00e9a PSS via authenticated Type X / EDIFACT and REST/JSON APIs directly into Salesforce Data Cloud. SITA BagMessage streamed via Kafka to Service Cloud."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Amadeus Alt\u00e9a / Navitaire New Skies",
              "vendor": "Amadeus IT Group",
              "role": "Cloud-native PSS for network legacy or ultra-low-cost carriers"
            },
            {
              "name": "SITA BagMessage & WorldTracer",
              "vendor": "SITA",
              "role": "Baggage tracking and interline reconciliation"
            },
            {
              "name": "PROS Dynamic Revenue Management",
              "vendor": "PROS Holdings",
              "role": "Real-time algorithmic seat availability and willingness-to-pay pricing"
            },
            {
              "name": "Swiss-AS AMOS",
              "vendor": "Swiss Aviation Software",
              "role": "MRO airworthiness and spare parts inventory"
            },
            {
              "name": "Jeppesen Crew Management (Boeing)",
              "vendor": "Boeing",
              "role": "Crew pairing, roster construction and day-of-ops recovery"
            }
          ],
          "licensing_acv": "$16,500,000 - $28,000,000 / year",
          "implementation_capex": "$14,000,000 - $25,000,000",
          "annual_run_cost": "$4,800,000 / year",
          "data_handled": "Real-time PNR, booking class yield curves, bag scan events, maintenance logbooks, crew duty hours.",
          "purpose": "Provides the complete core operational and revenue management capability with direct Kafka event streaming to open data pipelines.",
          "business_value": "PROS algorithmic pricing delivers 2.5% - 4.5% yield expansion; Navitaire provides lowest cost per passenger boarded for LCC models.",
          "integration_specs": "Open REST APIs, MQ Series message brokers, and Confluent Kafka event bridges streaming PSS events to Snowflake at 50ms latency."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Amadeus Alt\u00e9a Dedicated Private Cloud Tier-1",
              "vendor": "Amadeus IT Group",
              "role": "Dedicated high-availability instance with 99.999% SLA"
            },
            {
              "name": "Palantir Foundry Aviation Core",
              "vendor": "Palantir Technologies",
              "role": "Enterprise operational digital twin integrating fleet, crew, baggage, and passenger data"
            },
            {
              "name": "Boeing Jeppesen Total Engine Optimization",
              "vendor": "Boeing Digital Solutions",
              "role": "Predictive fuel burn optimization and dynamic flight re-routing"
            },
            {
              "name": "SITA e-Aircraft DataHub",
              "vendor": "SITA",
              "role": "Real-time ACARS aircraft telemetry and engine sensor streaming"
            },
            {
              "name": "Swiss-AS AMOS Enterprise Cloud",
              "vendor": "Swiss-AS",
              "role": "Predictive component failure MRO with automated spares logistics"
            }
          ],
          "licensing_acv": "$35,000,000 - $55,000,000 / year",
          "implementation_capex": "$40,000,000 - $75,000,000",
          "annual_run_cost": "$10,000,000 / year",
          "data_handled": "Full avionics bus telemetry (ARINC 429/629), real-time engine vibration and fuel flow, complete passenger journey graphs, microsecond PNR modifications, sovereign border agency APIS/iAPI feeds.",
          "purpose": "The ultimate sovereign-grade operational command platform, unifying real-time avionics, passenger logistics, and crew orchestration into an unbroken digital twin.",
          "business_value": "Saves $45M+ annually in fuel burn and ground turnaround delays; eliminates PSS outage risk with five-nines contractual uptime.",
          "integration_specs": "Dedicated 10Gbps AWS Direct Connect links, encrypted gRPC streams, Palantir Foundry Data Connectors, sub-10ms operational telemetry pipelines."
        }
      }
    },
    {
      "layer_id": "marketing",
      "name": "2. Marketing Automation & AdTech",
      "icon": "\ud83d\udce3",
      "desc": "Omni-channel journey orchestration, dynamic ancillary merchandising, triggered flight status, and adtech syndication",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Salesforce Marketing Cloud Engagement",
              "vendor": "Salesforce",
              "role": "Email, SMS, Mobile Push, and WhatsApp journey orchestration"
            },
            {
              "name": "Marketing Cloud Personalization (Interaction Studio)",
              "vendor": "Salesforce",
              "role": "Real-time web/app dynamic offer personalization and next-best-action"
            },
            {
              "name": "Salesforce Marketing Cloud Growth / Advanced",
              "vendor": "Salesforce",
              "role": "Agentic campaign generation via Einstein 1 Platform"
            },
            {
              "name": "Advertising Studio",
              "vendor": "Salesforce",
              "role": "First-party audience sync to Google Customer Match and Meta CAPI"
            }
          ],
          "licensing_acv": "$1,400,000 - $2,600,000 / year",
          "implementation_capex": "$1,200,000 - $2,200,000",
          "annual_run_cost": "$600,000 / year",
          "data_handled": "Subscriber profiles, email interaction telemetry, browsing abandonment (flight search, seat selection), WhatsApp interaction logs, hashed PII for ad match.",
          "purpose": "Drives pre-trip ancillary merchandising (extra bags, seat upgrades, lounge passes), operational flight alerts, and personalized re-engagement campaigns.",
          "business_value": "Generates $35M+ in incremental direct ancillary revenue; reduces paid media ad waste by 22% via real-time suppression of checked-in passengers.",
          "integration_specs": "Direct native Zero-Copy synchronization with Salesforce Data Cloud; Journey Builder triggered via Data Cloud Streaming Events."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Braze Enterprise Customer Engagement",
              "vendor": "Braze",
              "role": "Cross-channel streaming campaigns (Push, In-App, Email, SMS, WhatsApp)"
            },
            {
              "name": "Movable Ink",
              "vendor": "Movable Ink",
              "role": "Dynamic visual content rendering (live countdowns, weather, gate numbers in email)"
            },
            {
              "name": "Branch.io",
              "vendor": "Branch Metrics",
              "role": "Deep-linking from promotional campaigns directly into flight search in mobile app"
            },
            {
              "name": "AppsFlyer Enterprise",
              "vendor": "AppsFlyer",
              "role": "Mobile app attribution, marketing analytics and deep-funnel fraud prevention"
            }
          ],
          "licensing_acv": "$1,100,000 - $1,900,000 / year",
          "implementation_capex": "$900,000 - $1,500,000",
          "annual_run_cost": "$550,000 / year",
          "data_handled": "Real-time user event streams, device tokens, deep-link click logs, mobile app session metrics, dynamic image cache.",
          "purpose": "High-speed, developer-friendly mobile and web messaging platform with ultra-low latency trigger capabilities.",
          "business_value": "Braze achieves 98% delivery within 60 seconds of flight schedule changes; Movable Ink boosts email click-through rate by 38%.",
          "integration_specs": "REST APIs, Webhooks, Twilio Segment / Snowflake direct synchronization via Braze Currents Kafka streams."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Adobe Experience Platform (AEP)",
              "vendor": "Adobe",
              "role": "Central real-time marketing data fabric and governance"
            },
            {
              "name": "Adobe Journey Optimizer (AJO)",
              "vendor": "Adobe",
              "role": "Unified omni-channel orchestration across digital and physical touchpoints"
            },
            {
              "name": "Adobe Target Enterprise",
              "vendor": "Adobe",
              "role": "AI-driven algorithmic dynamic pricing and content optimization"
            },
            {
              "name": "Marketo Measure (Bizible)",
              "vendor": "Adobe",
              "role": "Multi-touch B2B and corporate travel contract attribution"
            },
            {
              "name": "LiveRamp Safe Haven Clean Room",
              "vendor": "LiveRamp",
              "role": "Sovereign data clean room for co-brand bank and travel partner monetization"
            }
          ],
          "licensing_acv": "$3,200,000 - $5,500,000 / year",
          "implementation_capex": "$3,500,000 - $6,000,000",
          "annual_run_cost": "$1,400,000 / year",
          "data_handled": "Edge-computed visitor profiles, complete cross-device identity graphs, sub-second behavioral events, privacy-preserving clean room tokens.",
          "purpose": "The premier digital marketing and customer journey suite globally, enabling sub-50ms dynamic personalization across web, mobile, airport lounges, and in-flight screens.",
          "business_value": "Maximizes direct booking share to > 55%; extracts $18M+ in joint marketing revenue from co-brand credit card partners via clean rooms.",
          "integration_specs": "Adobe Experience Platform Web SDK (AEP Web SDK), Adobe Edge Network, streaming ingestion via Kafka, and bidirectional sync to Snowflake."
        }
      }
    },
    {
      "layer_id": "crm_service",
      "name": "3. CRM & Omni-Channel Service Desk",
      "icon": "\ud83c\udfa7",
      "desc": "Case management, agent desktop, CTI voice integration, digital messaging, and VIP Medallion service",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Salesforce Service Cloud Enterprise",
              "vendor": "Salesforce",
              "role": "Unified agent desktop, omni-channel case routing, and SLA tracking"
            },
            {
              "name": "Service Cloud Voice (Amazon Connect)",
              "vendor": "Salesforce / AWS",
              "role": "Integrated cloud contact center telephony with real-time transcription"
            },
            {
              "name": "Salesforce Digital Engagement",
              "vendor": "Salesforce",
              "role": "WhatsApp, SMS, Apple Messages for Business, and Web Chat routing"
            },
            {
              "name": "Agentforce Service Agent",
              "vendor": "Salesforce",
              "role": "Autonomous conversational AI resolving flight queries and baggage issues"
            }
          ],
          "licensing_acv": "$2,200,000 - $3,800,000 / year",
          "implementation_capex": "$2,000,000 - $3,500,000",
          "annual_run_cost": "$900,000 / year",
          "data_handled": "Customer contact records, case notes, voice audio streams, call transcripts, sentiment scores, EU261 compensation claims, voucher issuance logs.",
          "purpose": "Empowers 3,000+ contact center agents and airport desk staff with a single 360-degree passenger view, while deflecting 40%+ of volume autonomously.",
          "business_value": "Reduces Average Handle Time (AHT) by 84 seconds; deflects $14M in Tier-1 customer servicing costs annually; elevates CSAT from 68 to 86.",
          "integration_specs": "Integrated with Amadeus Alt\u00e9a via MuleSoft; CTI integration via Amazon Connect WebRTC; Pub/Sub API for real-time event streaming."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Microsoft Dynamics 365 Customer Service",
              "vendor": "Microsoft",
              "role": "Enterprise case management and omni-channel agent desktop"
            },
            {
              "name": "Genesys Cloud CX",
              "vendor": "Genesys",
              "role": "Global cloud contact center, intelligent routing and workforce management"
            },
            {
              "name": "Ada CX AI / Forethought",
              "vendor": "Ada / Forethought",
              "role": "Conversational AI resolution engine for passenger self-service"
            },
            {
              "name": "Infobip WhatsApp Business API",
              "vendor": "Infobip",
              "role": "Global conversational messaging gateway"
            }
          ],
          "licensing_acv": "$1,800,000 - $3,200,000 / year",
          "implementation_capex": "$2,200,000 - $4,000,000",
          "annual_run_cost": "$950,000 / year",
          "data_handled": "Customer interaction histories, voice recordings, chatbot transcripts, queue metrics, agent scheduling adherence.",
          "purpose": "Robust, telecommunications-grade contact center platform with tight Microsoft 365 / Teams enterprise collaboration.",
          "business_value": "Genesys Cloud provides industry-leading 99.999% voice availability and advanced workforce management for multi-site BPO operations.",
          "integration_specs": "Genesys Cloud Open APIs, Microsoft Dataverse connectors, Webhook dispatch to Azure Event Grid."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Genesys Cloud CX Sovereign Dedicated",
              "vendor": "Genesys",
              "role": "Dedicated enterprise private cloud contact center with zero shared tenancy"
            },
            {
              "name": "Google Cloud Contact Center AI (CCAI)",
              "vendor": "Google Cloud",
              "role": "Real-time agent assist, predictive sentiment, and voice bot orchestration"
            },
            {
              "name": "Verint Workforce Engagement & Speech Analytics",
              "vendor": "Verint Systems",
              "role": "100% voice audio automated quality monitoring and compliance auditing"
            },
            {
              "name": "Nuance Gatekeeper Voice Biometrics",
              "vendor": "Microsoft / Nuance",
              "role": "Instant frictionless voice biometrics authentication in IVR (< 3 seconds)"
            },
            {
              "name": "Palantir AIP VIP Medallion Concierge Desk",
              "vendor": "Palantir Technologies",
              "role": "Dedicated high-net-worth passenger resolution desk with automated PNR override authority"
            }
          ],
          "licensing_acv": "$5,200,000 - $8,800,000 / year",
          "implementation_capex": "$5,500,000 - $9,500,000",
          "annual_run_cost": "$2,200,000 / year",
          "data_handled": "Acoustic voiceprints, biometric security hashes, 100% decrypted audio streams, real-time agent screen recordings, VIP travel itineraries, executive escalation paths.",
          "purpose": "The gold standard in airline contact center operations: zero fraud, instant voice biometric verification, and ultra-high-touch concierge service for elite passengers.",
          "business_value": "Eliminates call center account takeover fraud ($8M+ saved); VIP elite retention increased by 14%; contact center productivity boosted by 42%.",
          "integration_specs": "Dedicated SIP trunks, TLS 1.3 encrypted WebSockets, direct Google CCAI Dialogflow CX integration, Palantir AIP secure REST endpoints."
        }
      }
    },
    {
      "layer_id": "loyalty",
      "name": "4. Loyalty Management & Gamification",
      "icon": "\ud83d\udc8e",
      "desc": "Frequent Flyer Program (FFP) points/miles ledger, tier status, coalition earn/burn, and co-brand credit cards",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Salesforce Loyalty Management",
              "vendor": "Salesforce",
              "role": "Frequent Flyer points/miles ledger, tier qualification, and partner rewards"
            },
            {
              "name": "Salesforce Data Cloud for Loyalty",
              "vendor": "Salesforce",
              "role": "Real-time tier status calculation and dynamic voucher provisioning"
            },
            {
              "name": "Salesforce Experience Cloud Loyalty Portal",
              "vendor": "Salesforce",
              "role": "Member digital self-service, mileage balance, and claim missing miles"
            }
          ],
          "licensing_acv": "$1,100,000 - $1,900,000 / year",
          "implementation_capex": "$1,500,000 - $2,800,000",
          "annual_run_cost": "$500,000 / year",
          "data_handled": "Frequent flyer account IDs, tier status (Silver/Gold/Platinum), qualifying miles (EQMs), non-qualifying award miles, partner transaction accruals, reward redemptions.",
          "purpose": "Powers the airline's high-margin frequent flyer program, managing member lifecycle, gamified promotions, and non-air partner coalition earn/burn.",
          "business_value": "Frequent flyer programs generate 30% to 50% of airline enterprise market value; enables seamless launch of partner promotions in under 3 days.",
          "integration_specs": "MuleSoft connectors to Amadeus Alt\u00e9a Loyalty / PSS; real-time transactional REST APIs for co-brand bank files."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Talon.One Promotion & Loyalty Engine",
              "vendor": "Talon.One",
              "role": "Rule-based real-time promotion and loyalty reward engine"
            },
            {
              "name": "Antavo Enterprise Loyalty Cloud",
              "vendor": "Antavo",
              "role": "Gamified loyalty management, VIP tier progression, and reward wallet"
            },
            {
              "name": "OpenLoyalty Microservices",
              "vendor": "OpenLoyalty",
              "role": "Headless loyalty ledger microservices"
            }
          ],
          "licensing_acv": "$750,000 - $1,400,000 / year",
          "implementation_capex": "$1,200,000 - $2,200,000",
          "annual_run_cost": "$450,000 / year",
          "data_handled": "Member IDs, rule triggers, coupon codes, point transaction ledgers, gamification badges.",
          "purpose": "API-first, headless loyalty architecture giving product engineering teams complete control over front-end user experience.",
          "business_value": "Talon.One processes promotion validations in under 15ms at 50,000 requests/sec during Black Friday flash sales.",
          "integration_specs": "Headless REST APIs, GraphQL endpoints, Webhooks, Kafka event stream to Snowflake."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Antavo Enterprise Loyalty Cloud Sovereign",
              "vendor": "Antavo",
              "role": "Custom high-throughput ledger supporting 100,000 TPS"
            },
            {
              "name": "Pointshound / Rocketmiles API",
              "vendor": "Points.com / Plusgrade",
              "role": "Global ancillary hotel and car rental loyalty earn/burn marketplace"
            },
            {
              "name": "Visa Direct & Amex Global Gateway",
              "vendor": "Visa / American Express",
              "role": "Real-time card-linked offer redemption at merchant POS terminals"
            }
          ],
          "licensing_acv": "$2,800,000 - $4,600,000 / year",
          "implementation_capex": "$3,200,000 - $5,500,000",
          "annual_run_cost": "$1,100,000 / year",
          "data_handled": "Financial-grade miles ledger, real-time ISO 8583 card swipe feeds, merchant category codes (MCC), partner currency exchange rates.",
          "purpose": "Transforms the loyalty program into a standalone fintech powerhouse, driving billion-dollar co-brand card revenue and instant merchant accrual.",
          "business_value": "Co-brand credit card mileage sales yield over $600M annually with 85%+ gross profit margins; card-linked offers increase daily engagement by 220%.",
          "integration_specs": "PCI-DSS Level 1 certified private circuits, ISO 8583 financial transaction protocol, sub-50ms API response SLA."
        }
      }
    },
    {
      "layer_id": "cdp",
      "name": "5. Customer Data Platform (CDP) & Identity",
      "icon": "\ud83e\uddec",
      "desc": "Real-time passenger event ingestion, deterministic/probabilistic identity graph, and unified golden record",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Salesforce Data Cloud for Travel",
              "vendor": "Salesforce",
              "role": "Zero-Copy data harmonization, identity resolution, and real-time Calculated Insights"
            },
            {
              "name": "Data Cloud Zero-Copy Federation",
              "vendor": "Salesforce / Snowflake",
              "role": "Direct querying of external Snowflake/Databricks lakehouse without ETL duplication"
            }
          ],
          "licensing_acv": "$1,200,000 - $2,200,000 / year (Based on Data Cloud segment & profile credits)",
          "implementation_capex": "$1,000,000 - $1,800,000",
          "annual_run_cost": "$450,000 / year",
          "data_handled": "Unified Individual DMO, Contact Point Email/Phone, Alt\u00e9a PNR history, KrisFlyer/Frequent Flyer status, baggage scan logs, web browsing sessions.",
          "purpose": "The central real-time passenger brain: resolves fragmented traveler touchpoints into a single golden profile accessible by marketing, service, and airport staff.",
          "business_value": "Eliminates duplicate marketing sends; enables front-desk agents to recognize high-value corporate travelers regardless of booking channel.",
          "integration_specs": "Zero-Copy open data architecture with Snowflake and BigQuery; streaming ingestion via Kafka, MuleSoft, and Salesforce Pub/Sub API."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Twilio Segment Unify (or mParticle)",
              "vendor": "Twilio / mParticle",
              "role": "Real-time customer data platform, identity graph, and reverse ETL"
            },
            {
              "name": "RudderStack Enterprise",
              "vendor": "RudderStack",
              "role": "Warehouse-native event streaming and reverse ETL to operational systems"
            }
          ],
          "licensing_acv": "$900,000 - $1,600,000 / year",
          "implementation_capex": "$1,100,000 - $1,900,000",
          "annual_run_cost": "$500,000 / year",
          "data_handled": "Cross-platform event payloads (Track, Identify, Page), anonymous-to-known user mapping, identity graphs, consent state.",
          "purpose": "Developer-centric, warehouse-first CDP architecture that feeds clean, validated event streams directly into Snowflake.",
          "business_value": "Reduces data engineering overhead by 65%; provides instantaneous event forwarding to 200+ downstream SaaS destinations.",
          "integration_specs": "Client-side iOS/Android/JavaScript SDKs, server-side REST APIs, Kafka streaming connector, direct Snowflake load."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Adobe Real-Time Customer Data Platform (RT-CDP)",
              "vendor": "Adobe",
              "role": "B2C & B2B unified streaming profile with patented identity governance"
            },
            {
              "name": "Snowflake Healthcare & Travel Data Clean Room",
              "vendor": "Snowflake",
              "role": "Sovereign multi-party data collaboration with airports, hotels, and banks"
            },
            {
              "name": "Palantir Foundry Dynamic Passenger Ontology",
              "vendor": "Palantir Technologies",
              "role": "Deep kinetic graph linking passenger relationships, corporate hierarchies, and travel patterns"
            }
          ],
          "licensing_acv": "$3,800,000 - $6,500,000 / year",
          "implementation_capex": "$4,000,000 - $7,500,000",
          "annual_run_cost": "$1,600,000 / year",
          "data_handled": "100-billion-node enterprise identity graph, multi-generational household groupings, corporate spend consolidation, real-time geo-location breadcrumbs.",
          "purpose": "The most advanced identity and kinetic graph platform in existence, fusing digital clickstreams, physical airport movements, and enterprise corporate travel agreements.",
          "business_value": "Unlocks $40M+ in targeted corporate travel contract retention and multi-million-dollar airline partner joint ventures.",
          "integration_specs": "Streaming ingestion via Apache Pulsar / Kafka, sub-100ms edge profile activation, encrypted clean room queries via SQL."
        }
      }
    },
    {
      "layer_id": "integration",
      "name": "6. API Gateway, Integration & Event Mesh",
      "icon": "\ud83d\udd0c",
      "desc": "API gateway, enterprise iPaaS, Kafka event streaming, and legacy aviation protocol adapters (EDIFACT, Type B, IATA NDC)",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "MuleSoft Anypoint Platform",
              "vendor": "Salesforce / MuleSoft",
              "role": "Universal API Management, API Gateway, and Enterprise Service Bus (ESB)"
            },
            {
              "name": "MuleSoft Direct for Amadeus & SITA",
              "vendor": "Salesforce / MuleSoft",
              "role": "Pre-built connectors mapping Alt\u00e9a PSS and SITA BagMessage to Salesforce DMOs"
            },
            {
              "name": "Salesforce Pub/Sub API (gRPC)",
              "vendor": "Salesforce",
              "role": "High-throughput, bi-directional event bus streaming Change Data Capture (CDC)"
            }
          ],
          "licensing_acv": "$1,500,000 - $2,800,000 / year (Core-based licensing)",
          "implementation_capex": "$1,800,000 - $3,200,000",
          "annual_run_cost": "$700,000 / year",
          "data_handled": "XML/JSON payloads, EDIFACT PNR messages, Type B baggage teletype, REST/OData requests, gRPC binary protocol buffers.",
          "purpose": "Acts as the central nervous system connecting 50-year-old mainframe aviation protocols (EDIFACT) to modern cloud microservices.",
          "business_value": "Cuts API development time by 60% through pre-packaged API-led connectivity; guarantees zero message loss during peak system spikes.",
          "integration_specs": "REST, SOAP, EDIFACT, gRPC, Kafka connectors, RAML/OAS3 API specifications, OAuth2 token validation."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Confluent Cloud Enterprise (Kafka)",
              "vendor": "Confluent",
              "role": "Managed enterprise event streaming backbone across multi-cloud regions"
            },
            {
              "name": "Kong Konnect API Gateway",
              "vendor": "Kong Inc.",
              "role": "Cloud-native, ultra-low latency API gateway and service mesh"
            },
            {
              "name": "Workato Enterprise iPaaS",
              "vendor": "Workato",
              "role": "Low-code enterprise workflow automation and business application integration"
            }
          ],
          "licensing_acv": "$1,200,000 - $2,200,000 / year",
          "implementation_capex": "$1,400,000 - $2,500,000",
          "annual_run_cost": "$650,000 / year",
          "data_handled": "Streaming event topics (flight_status, pnr_updated, bag_scanned), API gateway tokens, JSON microservices payloads.",
          "purpose": "High-performance, event-driven decoupled architecture optimized for Kubernetes, microservices, and continuous deployment.",
          "business_value": "Kong provides sub-millisecond API proxy latency; Confluent guarantees fault-tolerant streaming of 100,000+ flight events/sec.",
          "integration_specs": "Apache Kafka wire protocol, gRPC, REST, GraphQL, Kong Ingress Controller on Kubernetes."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Confluent Cloud Dedicated Tier-1 Clusters",
              "vendor": "Confluent",
              "role": "Dedicated multi-region event mesh with 99.999% SLA and infinite retention"
            },
            {
              "name": "Solace PubSub+ Event Broker",
              "vendor": "Solace",
              "role": "Hardware-accelerated ultra-low-latency event mesh for mission-critical flight ops"
            },
            {
              "name": "Kong Enterprise Gateway Sovereign",
              "vendor": "Kong Inc.",
              "role": "FIPS 140-2 compliant API security gateway with mTLS enforcement"
            },
            {
              "name": "AWS PrivateLink & Cloud Interconnect",
              "vendor": "Amazon Web Services",
              "role": "Direct encrypted VPC peering bypassing the public internet entirely"
            }
          ],
          "licensing_acv": "$3,500,000 - $5,800,000 / year",
          "implementation_capex": "$3,800,000 - $6,500,000",
          "annual_run_cost": "$1,500,000 / year",
          "data_handled": "Mission-critical ACARS telemetry, high-frequency flight positioning, sovereign passenger clearance, hardware-encrypted banking transactions.",
          "purpose": "Carrier-grade, military-spec integration mesh ensuring zero dropped packets and microsecond routing under extreme disaster scenarios.",
          "business_value": "Prevents catastrophic system-wide groundings caused by middleware crashes; meets highest defense and aviation regulatory mandates.",
          "integration_specs": "Hardware-accelerated SMF, AMQP, MQTT, Kafka, gRPC, dedicated 100Gbps dark fiber connections."
        }
      }
    },
    {
      "layer_id": "cloud_data",
      "name": "7. Cloud Infrastructure & Lakehouse",
      "icon": "\u2601\ufe0f",
      "desc": "Cloud compute, relational databases, data lakehouse, real-time analytics, and disaster recovery",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Salesforce Hyperforce on AWS",
              "vendor": "Salesforce / AWS",
              "role": "Sovereign regional cloud hosting for CRM, Data Cloud, and Agentforce"
            },
            {
              "name": "Snowflake Data Cloud",
              "vendor": "Snowflake",
              "role": "Enterprise analytical data warehouse with Zero-Copy Data Cloud sharing"
            },
            {
              "name": "Amazon Web Services (AWS) Core",
              "vendor": "AWS",
              "role": "EKS Kubernetes compute, Amazon S3 data lake, and Amazon RDS PostgreSQL"
            }
          ],
          "licensing_acv": "$2,500,000 - $4,200,000 / year",
          "implementation_capex": "$1,800,000 - $3,000,000",
          "annual_run_cost": "$1,100,000 / year",
          "data_handled": "Historical flight bookings (10+ years), financial ledgers, clickstream data lakes, customer identity tables, machine learning feature stores.",
          "purpose": "Provides elastic compute and infinite storage for historical analytics, regulatory reporting, and predictive AI model training.",
          "business_value": "Snowflake Zero-Copy eliminates 80% of data duplication costs and enables instant querying of 50TB datasets without data egress fees.",
          "integration_specs": "Apache Iceberg table formats, AWS PrivateLink, Snowflake Secure Data Sharing, JDBC/ODBC."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Google Cloud Platform (GCP) Core",
              "vendor": "Google Cloud",
              "role": "Google Kubernetes Engine (GKE), Cloud Spanner, and Cloud Storage"
            },
            {
              "name": "Databricks Lakehouse Platform",
              "vendor": "Databricks",
              "role": "Unified Apache Spark lakehouse for data engineering, BI, and ML"
            },
            {
              "name": "Snowflake Analytical Cloud",
              "vendor": "Snowflake",
              "role": "Enterprise data warehousing and data clean rooms"
            }
          ],
          "licensing_acv": "$2,800,000 - $4,800,000 / year",
          "implementation_capex": "$2,200,000 - $3,800,000",
          "annual_run_cost": "$1,300,000 / year",
          "data_handled": "Delta Lake parquet tables, streaming Spark logs, operational Spanner databases, real-time feature tables.",
          "purpose": "High-performance open lakehouse architecture optimized for heavy data science, predictive pricing, and complex data engineering.",
          "business_value": "Cloud Spanner provides 99.999% SLA with external consistency; Databricks Spark clusters process billions of search queries daily.",
          "integration_specs": "Delta Lake, Apache Iceberg, Apache Parquet, Cloud Spanner gRPC, Databricks Unity Catalog."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Multi-Cloud Sovereign Hybrid (AWS GovCloud / AWS Secret Region + GCP Sovereign)",
              "vendor": "AWS / Google Cloud",
              "role": "Sovereign isolated compute clusters with air-gapped security capability"
            },
            {
              "name": "Databricks Lakehouse on NVIDIA DGX Clusters",
              "vendor": "Databricks / NVIDIA",
              "role": "Dedicated enterprise AI compute for continuous foundation model pre-training"
            },
            {
              "name": "Snowflake Sovereign Clean Rooms",
              "vendor": "Snowflake",
              "role": "Isolated zero-trust clean rooms for interline and alliance data exchange"
            }
          ],
          "licensing_acv": "$7,500,000 - $12,500,000 / year",
          "implementation_capex": "$8,000,000 - $15,000,000",
          "annual_run_cost": "$3,500,000 / year",
          "data_handled": "Airspace defense telemetry, sovereign biometric passenger registries, encrypted inter-airline settlement ledgers, petabyte-scale sensor dumps.",
          "purpose": "The world's most resilient, un-hackable cloud infrastructure, built to survive nation-state cyberattacks and total regional power grid failures.",
          "business_value": "100% compliance with sovereign data residency laws across EU, US, and APAC; zero downtime guarantee for critical flight infrastructure.",
          "integration_specs": "Hardware Security Modules (HSM), Quantum-safe encryption, BGP Anycast, dedicated trans-oceanic fiber links."
        }
      }
    },
    {
      "layer_id": "ai_ml",
      "name": "8. AI, Machine Learning & Agentic Systems",
      "icon": "\ud83e\udd16",
      "desc": "Frontier LLMs, autonomous agentic reasoning (Agentforce / LangGraph / Palantir AIP), and predictive aviation ML models",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Salesforce Agentforce & Atlas Reasoning Engine",
              "vendor": "Salesforce",
              "role": "Autonomous agent orchestration for IROPS rebooking, baggage claims, and ancillaries"
            },
            {
              "name": "Claude 3.5 Sonnet / Claude 3.7 via Model Context Protocol (MCP)",
              "vendor": "Anthropic / Salesforce",
              "role": "Frontier multi-modal reasoning connected to enterprise tools via MCP"
            },
            {
              "name": "Einstein 1 Predictive AI Platform",
              "vendor": "Salesforce",
              "role": "Turnaround delay prediction, passenger churn scoring, and upgrade propensity modeling"
            }
          ],
          "licensing_acv": "$1,500,000 - $3,000,000 / year (Consumption credits + platform fees)",
          "implementation_capex": "$1,200,000 - $2,500,000",
          "annual_run_cost": "$600,000 / year",
          "data_handled": "Natural language passenger prompts, tool invocation schemas (JSON-RPC MCP), flight delay probability scores, upgrade bid amounts.",
          "purpose": "Empowers autonomous multi-agent reasoning directly inside the CRM and contact center, autonomously executing complex rebooking during IROPS.",
          "business_value": "Deflects 45% of peak storm disruption contacts; automates $12M in instant re-accommodation vouchers without human agent queues.",
          "integration_specs": "Model Context Protocol (MCP) servers, JSON-RPC 2.0, Salesforce Trust Layer, Zero-Copy data grounding."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Databricks Mosaic AI & MLflow",
              "vendor": "Databricks",
              "role": "End-to-end LLM fine-tuning, RAG evaluation, and model governance"
            },
            {
              "name": "AWS Bedrock (Anthropic Claude 3.5 & Amazon Titan)",
              "vendor": "Amazon Web Services",
              "role": "Serverless foundation model APIs with VPC private endpoints"
            },
            {
              "name": "LangGraph & CrewAI Frameworks",
              "vendor": "Open Source / CrewAI",
              "role": "Multi-agent autonomous state machines for flight operations workflows"
            },
            {
              "name": "Pinecone Enterprise Vector Database",
              "vendor": "Pinecone",
              "role": "Sub-50ms vector search for airline fare rules and contract of carriage RAG"
            }
          ],
          "licensing_acv": "$1,100,000 - $2,200,000 / year",
          "implementation_capex": "$1,600,000 - $3,000,000",
          "annual_run_cost": "$850,000 / year",
          "data_handled": "Vector embeddings (1536-dim), agent execution traces, fare rule PDFs, historical IROPS mitigation transcripts.",
          "purpose": "Complete developer autonomy to build, test, and deploy customized agentic workflows with custom guardrails.",
          "business_value": "Enables proprietary domain-specific fine-tuning on airline operational manuals; zero vendor platform markup.",
          "integration_specs": "Python, FastAPI, Docker, Kubernetes, LangChain/LangGraph, OpenAI-compatible REST endpoints."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Palantir AIP (Artificial Intelligence Platform)",
              "vendor": "Palantir Technologies",
              "role": "Ontology-grounded autonomous agentic operational command for IROPS and fleet recovery"
            },
            {
              "name": "Anthropic Claude 3.7 Sonnet Enterprise Dedicated",
              "vendor": "Anthropic",
              "role": "Dedicated throughput provisioned LLM capacity with zero rate-limiting"
            },
            {
              "name": "NVIDIA NeMo Guardrails & Inference Microservices (NIM)",
              "vendor": "NVIDIA",
              "role": "Hardware-accelerated LLM inference and deterministic safety guardrails"
            },
            {
              "name": "Custom Aviation SLMs (Mistral Large On-Premise)",
              "vendor": "Mistral AI / In-House",
              "role": "Locally hosted sovereign 70B parameter models fine-tuned on 20 years of flight logs"
            }
          ],
          "licensing_acv": "$6,500,000 - $11,000,000 / year",
          "implementation_capex": "$7,000,000 - $14,000,000",
          "annual_run_cost": "$2,800,000 / year",
          "data_handled": "Full enterprise operational ontology, air traffic control transcripts, real-time radar vectors, legal compensation liability matrices.",
          "purpose": "The apex of enterprise artificial intelligence: Palantir AIP autonomously simulates 500 IROPS recovery scenarios in 30 seconds, selecting the path that minimizes passenger disruption, crew duty timeouts, and financial compensation.",
          "business_value": "Saves $65M+ annually during severe weather crises; cuts disruption recovery time from 36 hours to under 4 hours.",
          "integration_specs": "Palantir Foundry Action API, NVIDIA TensorRT-LLM, encrypted gRPC, air-gapped on-premise inference cluster."
        }
      }
    },
    {
      "layer_id": "frontends",
      "name": "9. Website, Mobile Apps & Digital Front-Ends",
      "icon": "\ud83d\udcf1",
      "desc": "Responsive web booking engine, native iOS/Android mobile apps, airport self-service kiosks, and digital wallets",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Custom React / Next.js Web Booking Engine",
              "vendor": "In-House / Vercel",
              "role": "High-conversion direct digital flight search, seat selection, and payment checkout"
            },
            {
              "name": "Native iOS (Swift) & Android (Kotlin) Mobile Apps",
              "vendor": "In-House",
              "role": "Mobile boarding pass wallet, live trip tracker, and push notifications"
            },
            {
              "name": "Salesforce Experience Cloud Portals",
              "vendor": "Salesforce",
              "role": "Frequent Flyer self-service portal, corporate booking portal, and travel agent extranet"
            },
            {
              "name": "SITA Smart Path Kiosk Software",
              "vendor": "SITA",
              "role": "Airport self-service check-in, bag-drop kiosks, and biometric gate boarding"
            }
          ],
          "licensing_acv": "$1,200,000 - $2,100,000 / year",
          "implementation_capex": "$3,000,000 - $5,500,000",
          "annual_run_cost": "$1,400,000 / year",
          "data_handled": "Session state, payment form tokens, biometric face templates (at kiosk), Apple Wallet pass tokens, GPS location breadcrumbs.",
          "purpose": "Delivers a seamless, branded digital experience from initial flight search to mobile boarding pass and airport lounge access.",
          "business_value": "Drives direct channel share to > 52%; reduces airport check-in desk staffing costs by $18M annually through 85%+ self-service adoption.",
          "integration_specs": "GraphQL / REST APIs to PSS and Salesforce Data Cloud; Apple Wallet .pkpass web service; SITA CUTE/CUSS kiosk standards."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Next.js Enterprise Web Platform on Vercel",
              "vendor": "Vercel",
              "role": "Edge-rendered web booking engine with sub-100ms page load times"
            },
            {
              "name": "Native iOS & Android Mobile Apps",
              "vendor": "In-House",
              "role": "Mobile app with offline boarding pass cache and Live Activities"
            },
            {
              "name": "Auth0 by Okta CIAM",
              "vendor": "Okta",
              "role": "Customer Identity and Access Management with passkeys and social login"
            },
            {
              "name": "Embross / Materna Kiosk Platform",
              "vendor": "Embross / Materna",
              "role": "Self-service bag drop and CUSS check-in kiosks"
            }
          ],
          "licensing_acv": "$950,000 - $1,700,000 / year",
          "implementation_capex": "$3,200,000 - $5,800,000",
          "annual_run_cost": "$1,500,000 / year",
          "data_handled": "Web vitals, authentication tokens, CUSS XML baggage tags, device push tokens.",
          "purpose": "Modern composable front-end architecture with edge rendering and instantaneous global CDN caching.",
          "business_value": "Every 100ms reduction in web booking engine latency increases booking conversion by 1.2%, generating $9M+ in incremental revenue.",
          "integration_specs": "Vercel Edge Functions, GraphQL Federation, Okta OIDC/OAuth2, IATA CUSS 1.5 standard."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Ultra-High-Availability Bespoke Native iOS & Android Apps",
              "vendor": "In-House / Apple & Google Elite Partnerships",
              "role": "100% Swift & Kotlin native codebases with Apple Vision Pro spatial cabin tour"
            },
            {
              "name": "SITA Smart Path Biometric Facial Recognition Ecosystem",
              "vendor": "SITA",
              "role": "100% walk-through biometric terminal experience (curb-to-gate without showing passport or boarding pass)"
            },
            {
              "name": "Vercel Enterprise Edge Network + Cloudflare Workers",
              "vendor": "Vercel / Cloudflare",
              "role": "Global multi-cloud edge compute with zero single point of failure"
            },
            {
              "name": "Bespoke Airport VIP Lounge Kiosks & In-Seat Ordering",
              "vendor": "Custom In-House",
              "role": "Touchscreen luxury suite tablets integrated with luxury catering"
            }
          ],
          "licensing_acv": "$3,800,000 - $6,200,000 / year",
          "implementation_capex": "$8,000,000 - $15,000,000",
          "annual_run_cost": "$3,200,000 / year",
          "data_handled": "Encrypted biometric face templates (NIST compliant), Apple Secure Enclave credentials, Live Activity push streams, spatial 3D interaction telemetry.",
          "purpose": "The ultimate luxury passenger interface: walk straight from the limousine onto the plane without touching a single paper document or waiting in any line.",
          "business_value": "Reduces total passenger airport dwell time by 45 minutes; wins world's best airline digital experience awards, driving 12% premium cabin pricing power.",
          "integration_specs": "Biometric matching engines (ICAO 9303 compliant), Apple PassKit, WebSockets, ultra-low-latency edge caching."
        }
      }
    },
    {
      "layer_id": "cms_dxp",
      "name": "10. Headless CMS, DXP & Digital Asset Mgmt",
      "icon": "\ud83c\udfa8",
      "desc": "Headless content management, 40+ language localization, enterprise digital asset management (DAM), and edge delivery",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Contentful Enterprise Headless CMS",
              "vendor": "Contentful",
              "role": "Structured content repository powering web, mobile, in-flight screens, and kiosks"
            },
            {
              "name": "Cloudinary Enterprise DAM",
              "vendor": "Cloudinary",
              "role": "AI-powered automated image and video optimization across all device breakpoints"
            },
            {
              "name": "Salesforce Experience Cloud CMS",
              "vendor": "Salesforce",
              "role": "Integrated portal content management for loyalty members and B2B travel agents"
            }
          ],
          "licensing_acv": "$450,000 - $850,000 / year",
          "implementation_capex": "$500,000 - $950,000",
          "annual_run_cost": "$250,000 / year",
          "data_handled": "Destination travel guides, fleet seat maps, promotional banners, multi-lingual translations (42 locales), 4K cabin video assets.",
          "purpose": "Centrally stores and serves all marketing and operational copy, enabling marketing teams to publish campaigns without engineering deployments.",
          "business_value": "Cuts time-to-market for global fare sales from 2 weeks to 4 hours; reduces mobile app image payload by 62% for faster loading.",
          "integration_specs": "GraphQL Content API, Webhooks to Vercel/Next.js, Cloudinary dynamic image transformation URLs."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "Strapi Enterprise (or Sanity.io)",
              "vendor": "Strapi / Sanity",
              "role": "Composable headless CMS with real-time collaborative editing"
            },
            {
              "name": "Bynder Enterprise DAM",
              "vendor": "Bynder",
              "role": "Enterprise brand asset management, digital rights management (DRM), and creative workflow"
            },
            {
              "name": "Lokalise Enterprise",
              "vendor": "Lokalise",
              "role": "Automated translation management system integrated with GitHub and Figma"
            }
          ],
          "licensing_acv": "$380,000 - $720,000 / year",
          "implementation_capex": "$450,000 - $850,000",
          "annual_run_cost": "$220,000 / year",
          "data_handled": "JSON content schemas, localized translation strings, photographer rights metadata, high-res RAW brand assets.",
          "purpose": "Agile, modern content stack tailored for continuous localization and rapid multi-platform publishing.",
          "business_value": "Eliminates translation overhead; saves $600K annually in agency localization fees.",
          "integration_specs": "REST & GraphQL APIs, GitHub Actions automated sync, Bynder Brand Connect integrations."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Adobe Experience Manager (AEM Sites & AEM Assets Enterprise)",
              "vendor": "Adobe",
              "role": "The enterprise standard for global multi-site, multi-language digital experience management"
            },
            {
              "name": "Adobe Dynamic Media with Scene7",
              "vendor": "Adobe",
              "role": "Real-time 3D cabin rendering and automated smart-cropping for millions of asset variants"
            },
            {
              "name": "Akamai EdgeWorkers & Ion CDN",
              "vendor": "Akamai Technologies",
              "role": "Global Tier-1 CDN delivering content from 4,000+ edge locations worldwide"
            }
          ],
          "licensing_acv": "$1,800,000 - $3,200,000 / year",
          "implementation_capex": "$2,200,000 - $4,200,000",
          "annual_run_cost": "$900,000 / year",
          "data_handled": "Enterprise master asset library (500TB+), global taxonomy trees, digital rights licensing contracts, real-time edge cache tags.",
          "purpose": "The ultimate enterprise content powerhouse: powers hundreds of localized brand domains with automated governance, workflow approvals, and edge caching.",
          "business_value": "Guarantees 100% brand consistency globally; withstands massive traffic surges during global crisis announcements without cache misses.",
          "integration_specs": "Adobe Cloud Manager, Dispatcher configurations, Adobe Experience Platform connectors, Akamai Edge API."
        }
      }
    },
    {
      "layer_id": "finance_erp",
      "name": "11. Finance, Revenue Accounting, ERP & Billing",
      "icon": "\ud83d\udcb3",
      "desc": "ASC 606 / IFRS 15 passenger revenue accounting, general ledger, payment gateways (Adyen/Stripe), and global tax",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "SAP S/4HANA Finance",
              "vendor": "SAP",
              "role": "Enterprise General Ledger, Accounts Payable, Accounts Receivable, and Asset Accounting"
            },
            {
              "name": "Amadeus Passenger Revenue Accounting (PRA)",
              "vendor": "Amadeus",
              "role": "Automated ticket flied coupon settlement, interline proration, and IATA BSP reconciliation"
            },
            {
              "name": "Adyen Enterprise Unified Commerce",
              "vendor": "Adyen",
              "role": "Global payment gateway, credit card acquiring, and alternative payment methods (APMs)"
            },
            {
              "name": "Salesforce Billing & Net Zero Cloud",
              "vendor": "Salesforce",
              "role": "Corporate contract recurring invoicing and corporate carbon offset accounting"
            }
          ],
          "licensing_acv": "$2,800,000 - $4,800,000 / year",
          "implementation_capex": "$4,500,000 - $8,500,000",
          "annual_run_cost": "$1,200,000 / year",
          "data_handled": "Flown coupons, unearned passenger revenue liability (UPR), credit card chargebacks, VAT/GST tax rates across 180 countries, carbon emission records.",
          "purpose": "Recognizes passenger revenue strictly upon flight completion (ASC 606), reconciles global bank clearinghouses (IATA BSP/ARC), and processes billions in transactions.",
          "business_value": "Prevents revenue leakage on interline flight legs; Adyen smart-routing reduces payment processing interchange fees by 35 bps ($28M saved).",
          "integration_specs": "SAP IDoc / RFC interfaces via MuleSoft, Adyen Webhooks, IATA HOT (Hand-Off Tape) files."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "SAP S/4HANA Public Cloud / Oracle NetSuite",
              "vendor": "SAP / Oracle",
              "role": "Cloud ERP for financial management and consolidation"
            },
            {
              "name": "Accelya FLX Revenue Accounting",
              "vendor": "Accelya",
              "role": "Specialized aviation passenger and cargo revenue accounting platform"
            },
            {
              "name": "Stripe Enterprise Payments",
              "vendor": "Stripe",
              "role": "Global payment infrastructure with Stripe Radar fraud detection"
            },
            {
              "name": "Avalara AvaTax for Aviation",
              "vendor": "Avalara",
              "role": "Automated aviation passenger fuel and departure tax calculation"
            }
          ],
          "licensing_acv": "$2,400,000 - $4,200,000 / year",
          "implementation_capex": "$4,000,000 - $7,500,000",
          "annual_run_cost": "$1,100,000 / year",
          "data_handled": "Ledger journals, payment authorizations, 3D Secure 2.0 payloads, jurisdictional tax tables.",
          "purpose": "Modern, API-accessible financial and tax automation stack minimizing custom code for payment integrations.",
          "business_value": "Stripe Radar reduces credit card fraud by 45%; Avalara eliminates risk of severe foreign government aviation tax penalties.",
          "integration_specs": "Stripe REST APIs, Accelya standard data interfaces, Snowflake accounting export."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "SAP S/4HANA Enterprise Private Cloud (with Central Finance)",
              "vendor": "SAP",
              "role": "Tier-1 global financial backbone unifying multiple airline subsidiaries"
            },
            {
              "name": "Accelya Enterprise Passenger Revenue Accounting",
              "vendor": "Accelya",
              "role": "Automated real-time coupon proration and complex multi-carrier alliance settlement"
            },
            {
              "name": "Kyriba Enterprise Treasury Management",
              "vendor": "Kyriba",
              "role": "Global multi-currency liquidity forecasting, fuel hedging, and foreign exchange risk management"
            },
            {
              "name": "Adyen Enterprise Global Omnichannel Gateway",
              "vendor": "Adyen",
              "role": "Direct scheme acquiring (Visa/Mastercard/Amex/JCB/UnionPay) across 150+ local currencies"
            }
          ],
          "licensing_acv": "$6,200,000 - $10,500,000 / year",
          "implementation_capex": "$10,000,000 - $20,000,000",
          "annual_run_cost": "$2,500,000 / year",
          "data_handled": "Multi-currency bank accounts ($5B+ cash balances), jet fuel derivatives contracts, interline clearinghouse balances, sovereign tax audit vaults.",
          "purpose": "The ultimate corporate treasury and financial engine: protects against currency volatility, automates complex alliance revenue splits, and optimizes multi-billion-dollar cash flows.",
          "business_value": "Kyriba fuel hedging saves tens of millions during oil price spikes; direct acquiring saves $50M+ in international FX and processor markups.",
          "integration_specs": "SWIFT messaging network, SAP OData APIs, direct banking host-to-host links (EBICS/AS2)."
        }
      }
    },
    {
      "layer_id": "hr_workforce",
      "name": "12. HR, Workforce Mgmt & Crew Scheduling",
      "icon": "\ud83d\udc65",
      "desc": "Core HRIS, employee portals, pilot & cabin crew legality compliance, shift bidding, and global payroll",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Workday Human Capital Management (HCM)",
              "vendor": "Workday",
              "role": "Core HRIS, talent management, benefits, and global payroll"
            },
            {
              "name": "Salesforce Agentforce for HR Service",
              "vendor": "Salesforce",
              "role": "Autonomous internal employee service agent resolving HR inquiries in Slack"
            },
            {
              "name": "Jeppesen Crew Tracking & Rostering",
              "vendor": "Boeing Digital Solutions",
              "role": "Pilot and flight attendant legal roster optimization and fatigue mitigation"
            }
          ],
          "licensing_acv": "$1,600,000 - $2,800,000 / year",
          "implementation_capex": "$2,200,000 - $4,000,000",
          "annual_run_cost": "$750,000 / year",
          "data_handled": "Employee records, pilot flight certifications, medical exam dates, union contract rules (ALPA/AFA), crew hotel accommodations.",
          "purpose": "Ensures every flight is crewed with certified, rested personnel compliant with strict aviation laws while providing seamless employee self-service.",
          "business_value": "Eliminates illegal crew assignment groundings ($2M+ per incident); cuts HR administrative ticketing volume by 55% via Slack.",
          "integration_specs": "Workday RaaS (Reports-as-a-Service), MuleSoft Workday Connector, Jeppesen crew file exports."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "SAP SuccessFactors Employee Central",
              "vendor": "SAP",
              "role": "Global cloud HR and talent management system"
            },
            {
              "name": "UKG Pro (Ultimate Kronos Group)",
              "vendor": "UKG",
              "role": "Ground crew workforce management, time and attendance, and shift scheduling"
            },
            {
              "name": "AIMS Crew Management System",
              "vendor": "AIMS Airline Software",
              "role": "Complete crew planning, day-of-operations tracking, and mobile crew portal"
            }
          ],
          "licensing_acv": "$1,400,000 - $2,500,000 / year",
          "implementation_capex": "$2,000,000 - $3,800,000",
          "annual_run_cost": "$700,000 / year",
          "data_handled": "Ground handler shift schedules, biometric clock-in scans, pilot passport expiration alerts, union grievance tracking.",
          "purpose": "Specialized aviation workforce and crew management stack trusted by over 150 commercial carriers worldwide.",
          "business_value": "AIMS reduces crew overnight hotel and deadhead repositioning costs by 18%, saving $14M annually.",
          "integration_specs": "AIMS REST APIs, SAP SuccessFactors OData APIs, Kronos Workforce Central database links."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "Workday HCM & Workday Adaptive Planning Enterprise",
              "vendor": "Workday",
              "role": "Global human capital management, predictive headcount planning, and executive succession"
            },
            {
              "name": "Boeing Jeppesen Total Crew Optimization (Concert)",
              "vendor": "Boeing Digital Solutions",
              "role": "AI-driven mathematical crew pairing and preferential bidding system"
            },
            {
              "name": "UKG InTouch DX Biometric Timeclocks",
              "vendor": "UKG",
              "role": "Enterprise facial recognition clock-in for 20,000+ airport ground staff and mechanics"
            },
            {
              "name": "CyberArk Mobile Crew Identity Protection",
              "vendor": "CyberArk",
              "role": "Zero-trust privileged identity access for pilots accessing electronic flight bags (EFBs)"
            }
          ],
          "licensing_acv": "$4,200,000 - $7,000,000 / year",
          "implementation_capex": "$5,000,000 - $9,500,000",
          "annual_run_cost": "$1,800,000 / year",
          "data_handled": "Pilot electronic flight bag (EFB) crypto certificates, biometric clock-in hashes, predictive pilot retirement models, FAA audit vaults.",
          "purpose": "The ultimate workforce optimization and aviation crew safety architecture: solves NP-hard crew pairing problems across 10,000 daily flights.",
          "business_value": "Maximizes crew satisfaction through preferential bidding, reducing pilot attrition in a competitive global market; saves $32M in pairing efficiency.",
          "integration_specs": "High-performance mathematical solver clusters, Workday Enterprise Bus, CyberArk Identity APIs."
        }
      }
    },
    {
      "layer_id": "governance",
      "name": "13. Enterprise Governance, Security & Privacy",
      "icon": "\ud83d\udee1\ufe0f",
      "desc": "GDPR/PDPA/UU PDP privacy, PCI-DSS Level 1 tokenization, SOC2 Type II, IAM (Okta), Zero-Trust & HSM key management",
      "variations": {
        "var_salesforce": {
          "platforms": [
            {
              "name": "Salesforce Shield",
              "vendor": "Salesforce",
              "role": "Platform Encryption, Event Monitoring, and Field Audit Trail for CRM and Data Cloud"
            },
            {
              "name": "OneTrust Privacy & Consent Automation",
              "vendor": "OneTrust",
              "role": "Global consent management, cookie preferences, and DSAR automated fulfillment"
            },
            {
              "name": "Okta Workforce Identity Cloud",
              "vendor": "Okta",
              "role": "Single Sign-On (SSO), Adaptive Multi-Factor Authentication (MFA), and lifecycle provisioning"
            }
          ],
          "licensing_acv": "$900,000 - $1,700,000 / year",
          "implementation_capex": "$800,000 - $1,500,000",
          "annual_run_cost": "$400,000 / year",
          "data_handled": "Encrypted PII (passports, date of birth), audit logs of every agent record view, customer consent records, employee SSO credentials.",
          "purpose": "Guarantees regulatory compliance with global aviation privacy mandates (GDPR, California CCPA, Singapore PDPA) and protects customer trust.",
          "business_value": "Prevents catastrophic GDPR fines (up to 4% of global turnover); enables instant auditing of customer data access for regulatory inquiries.",
          "integration_specs": "Salesforce Shield BYOK (Bring Your Own Key), Okta SCIM / SAML 2.0, OneTrust REST APIs."
        },
        "var_no_salesforce": {
          "platforms": [
            {
              "name": "HashiCorp Vault Enterprise",
              "vendor": "HashiCorp / IBM",
              "role": "Central secrets management, encryption-as-a-service, and dynamic database credentials"
            },
            {
              "name": "Collibra Data Intelligence Platform",
              "vendor": "Collibra",
              "role": "Enterprise data governance, data catalog, and data lineage mapping"
            },
            {
              "name": "Cloudflare Magic Transit & WAF",
              "vendor": "Cloudflare",
              "role": "DDoS mitigation, web application firewall, and API security protection"
            }
          ],
          "licensing_acv": "$1,100,000 - $1,900,000 / year",
          "implementation_capex": "$1,000,000 - $1,800,000",
          "annual_run_cost": "$480,000 / year",
          "data_handled": "API secret keys, database passwords, TLS certificates, data catalog metadata, blocked malicious DDoS traffic.",
          "purpose": "Developer-centric, zero-trust security infrastructure protecting microservices and cloud databases from unauthorized access.",
          "business_value": "Cloudflare mitigates multi-terabit DDoS attacks during geopolitical tensions; HashiCorp Vault eliminates hardcoded credentials across 500+ repositories.",
          "integration_specs": "Vault Kubernetes injector, Cloudflare Terraform provider, Collibra metadata harvesters."
        },
        "var_best_money_can_buy": {
          "platforms": [
            {
              "name": "CyberArk Privileged Access Security Sovereign",
              "vendor": "CyberArk",
              "role": "Military-grade credential vaulting and session recording for infrastructure administrators"
            },
            {
              "name": "HashiCorp Vault with Hardware Security Modules (HSM)",
              "vendor": "HashiCorp / Thales",
              "role": "FIPS 140-2 Level 3 hardware-backed cryptographic key generation and storage"
            },
            {
              "name": "Zscaler Zero Trust Exchange (ZPA & ZIA)",
              "vendor": "Zscaler",
              "role": "Direct-to-cloud zero-trust network access eliminating corporate VPN vulnerabilities"
            },
            {
              "name": "Palantir Foundry Security & Access Controls",
              "vendor": "Palantir Technologies",
              "role": "Granular cell-level and row-level mandatory access control (MAC) based on security clearance"
            },
            {
              "name": "BigID Data Discovery & DSPM",
              "vendor": "BigID",
              "role": "AI-driven discovery of dark, unstructured sensitive passenger data across multi-cloud lakes"
            }
          ],
          "licensing_acv": "$3,800,000 - $6,500,000 / year",
          "implementation_capex": "$4,200,000 - $7,500,000",
          "annual_run_cost": "$1,600,000 / year",
          "data_handled": "Root cryptographic keys, privileged admin session keystrokes, dark PII discovery graphs, zero-trust microsegmentation rules.",
          "purpose": "The absolute pinnacle of sovereign enterprise security: trusted by intelligence agencies and defense ministries to prevent nation-state cyber breaches.",
          "business_value": "Eliminates lateral network movement during ransomware attacks; guarantees zero breach of passenger biometric and payment data.",
          "integration_specs": "PKCS#11 HSM interfaces, Zscaler Client Connector, CyberArk PAM REST APIs, BigID automated scan connectors."
        }
      }
    }
  ]
};
