"""
Simulates document ingestion from an input source
"""

def ingest_document(file_name: str) -> dict:
    return {
        "file_name": file_name,
        "content": "Sample invoice text content"
    }
