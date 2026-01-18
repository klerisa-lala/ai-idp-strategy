"""
End-to-end IDP pipeline with Human-in-the-Loop logic
"""

from idp.ingestion import ingest_document
from idp.ocr_engine import extract_text
from idp.classifier import classify
from idp.validator import needs_human_review
from human_in_loop.reviewer import human_review

def run_pipeline(file_name: str) -> dict:
    document = ingest_document(file_name)
    text = extract_text(document)
    result = classify(text)

    if needs_human_review(result):
        print("Low confidence detected → Routed to human reviewer")
        result = human_review(result)
    else:
        print("High confidence → Automatically processed")

    return result
