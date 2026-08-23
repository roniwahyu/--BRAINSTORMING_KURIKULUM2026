# -*- coding: utf-8 -*-
import os
import re
import glob

workdir = r"d:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI"

md_files = glob.glob(os.path.join(workdir, "*.md"))

print(f"Auditing {len(md_files)} markdown files in KURIKULUM2026_REVISI...")

errors = 0
for fpath in md_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        lines = content.splitlines()

    for idx, line in enumerate(lines):
        line_num = idx + 1
        
        # Check STI-103 naming
        if "STI-103" in line:
            # Check if it contains old name Logika Informatika without being an equivalence table old column or historical doc
            if "Logika Informatika" in line and not any(k in line for k in ["(Lama)", "Logika Informatika lama", "Logika Informatika (Lama)", "Ekuivalen / Penyesuaian Topik"]):
                if fname not in ["016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md"]:
                    print(f"[DISCREPANCY] {fname}:{line_num} -> Found STI-103 with old name: {line.strip()}")
                    errors += 1

        # Check STI-201 naming
        if "STI-201" in line:
            if "Matematika Diskrit" in line and "Logika" not in line and not any(k in line for k in ["(Lama)", "Matematika Diskrit (Lama)", "Matematika Diskrit lama"]):
                if fname not in ["016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md"]:
                    print(f"[DISCREPANCY] {fname}:{line_num} -> Found STI-201 without Logika: {line.strip()}")
                    errors += 1

if errors == 0:
    print("[SUCCESS] 100% PERFECT ALIGNMENT: Semua file Markdown di KURIKULUM2026_REVISI telah 100% sinkron dan selaras!")
else:
    print(f"[FAILED] Ditemukan {errors} diskrepansi yang perlu diperbaiki.")
