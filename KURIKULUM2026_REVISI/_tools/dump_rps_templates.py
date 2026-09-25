import fitz  # PyMuPDF
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"d:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI"

def dump_pdf_structure(filename):
    filepath = os.path.join(base_dir, filename)
    print("=" * 80)
    print(f"FILE: {filename}")
    print("=" * 80)
    if not os.path.exists(filepath):
        print("NOT FOUND!")
        return
    
    doc = fitz.open(filepath)
    print(f"Total Pages: {len(doc)}")
    for i, page in enumerate(doc):
        print(f"\n--- PAGE {i+1} ---")
        text = page.get_text("text")
        print(text.strip())

dump_pdf_structure("0001_Template_RPS_OBE.pdf")
dump_pdf_structure("Template_RPS_GEN_2026_20092026-SWI.pdf")
