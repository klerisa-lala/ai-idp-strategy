"""
Represents the re-skilled human role validating AI outputs
"""

def human_review(result: dict) -> dict:
    result["reviewed_by_human"] = True
    result["confidence"] = 1.0
    return result
