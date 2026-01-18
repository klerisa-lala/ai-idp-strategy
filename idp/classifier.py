"""
Simulates document classification and data extraction
"""

import random

def classify(text: str) -> dict:
    return {
        "document_type": "Invoice",
        "confidence": round(random.uniform(0.7, 0.95), 2),
        "fields": {
            "invoice_number": "INV-001",
            "amount": "450 EUR"
        }
    }
