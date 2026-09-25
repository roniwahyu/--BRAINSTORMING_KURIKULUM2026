import fitz  # PyMuPDF
import os

base_dir = r"d:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI"

files_to_check = [
    "0001_Template_RPS_OBE.pdf",
    "Template_RPS_GEN_2026_20092026-SWI.pdf",
    "0003_PROMPT - BUAT RPS OBE With AI.pdf"
]

for filename in files_to_check:
    filepath = os.path.join(base_dir, filename)
    print("=" * 80)
    print(f"FILE: {filename}")
    print("=" * 80)
    if not os.path.exists(filepath):
        print("FILE NOT FOUND!")
        continue
    
    doc = fitz.open(filepath)
    print(f"Total Pages: {len(doc)}")
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        text = page.get_text("text")
        print(f"--- PAGE {page_idx + 1} ---")
        lines = text.split("\n")
        print("\n".join(lines[:40]))  # print first 40 lines
        if len(lines) > 40:
            print(f"... [{len(lines) - 40} more lines omitted] ...")
        print("\n")
