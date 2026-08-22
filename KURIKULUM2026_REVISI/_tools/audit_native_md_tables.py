"""
=============================================================================
AUDITOR TABLE MARKDOWN MURNI — KURIKULUM OBE SISTEKIN 2026
=============================================================================
Script ini memeriksa semua blok kode (```) di seluruh file .md untuk memastikan
tidak ada tabel yang 'tersembunyi' di dalam code block teks.
=============================================================================
"""

import os
import glob
import re

DIR = r'd:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI'

def audit_code_blocks():
    files = sorted(glob.glob(os.path.join(DIR, '*.md')))
    print(f"Memeriksa {len(files)} file markdown...")
    
    suspicious_blocks = []
    
    for f in files:
        fname = os.path.basename(f)
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
            
        # Cari semua blok ```
        blocks = re.findall(r'```([a-zA-Z0-9_-]*)\n([\s\S]*?)```', content)
        for lang, body in blocks:
            lang = lang.strip().lower()
            if lang in ['mermaid', 'python', 'json', 'yaml', 'bash', 'bat', 'cmd', 'diff', 'html', 'css', 'sql']:
                continue
                
            # Cek jika isi blok memuat pola tabel
            lines = body.strip().split('\n')
            if len(lines) > 2 and any('|' in l for l in lines) and any('-' in l for l in lines):
                suspicious_blocks.append((fname, lang, body[:100]))
            elif any(c in body for c in ['┌', '├', '└', '┼', '+---', '|---']):
                suspicious_blocks.append((fname, lang, body[:100]))
                
    if not suspicious_blocks:
        print("\n[VERIFIKASI SUKSES] 100% Seluruh dokumen Markdown menggunakan Native Markdown Tables!")
        print("Tidak ada tabel yang tersembunyi di dalam blok kode (```).")
    else:
        print(f"\n[PERINGATAN] Ditemukan {len(suspicious_blocks)} blok yang berpotensi berupa tabel dalam code block:")
        for fname, lang, preview in suspicious_blocks:
            print(f"  - File: {fname} (Lang: '{lang}')\n    Preview: {preview.strip()}...\n")

if __name__ == '__main__':
    audit_code_blocks()
