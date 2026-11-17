#!/usr/bin/env python3
"""
Master Reveal.js Presentation & Frameworks Generator for Travel & Hospitality Labs
Generates 50+ dense, presentation-grade Reveal.js slides for:
1. Airlines (/run/media/ml/Storage/Labs/airlines/presentation.html)
2. Hotels (/run/media/ml/Storage/Labs/hotels/presentation.html)
3. Cruises (/run/media/ml/Storage/Labs/cruises/presentation.html)
4. Tours (/run/media/ml/Storage/Labs/tours/presentation.html)

Includes companion Markdown compendiums for each.
"""

import os
import json

BASE_DIR = "/run/media/ml/Storage/Labs"

print("Initializing Presentation Generator...")
