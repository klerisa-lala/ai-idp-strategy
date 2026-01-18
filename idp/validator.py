"""
Determines whether human validation is required
"""

from config.settings import CONFIDENCE_THRESHOLD

def needs_human_review(result: dict) -> bool:
    return result["confidence"] < CONFIDENCE_THRESHOLD
