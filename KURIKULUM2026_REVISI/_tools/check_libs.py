import sys
import os

pdf_candidates = ["pypdf", "pdfplumber", "fitz", "pypdf2"]
for mod in pdf_candidates:
    try:
        __import__(mod)
        print(f"{mod}: available")
    except ImportError:
        pass

try:
    import docx
    print("docx: available")
except ImportError:
    pass
