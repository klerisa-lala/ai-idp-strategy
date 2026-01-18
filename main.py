"""
Application entry point
"""

from idp.pipeline import run_pipeline

if __name__ == "__main__":
    output = run_pipeline("invoice_sample.pdf")
    print("Final Processing Result:")
    print(output)
