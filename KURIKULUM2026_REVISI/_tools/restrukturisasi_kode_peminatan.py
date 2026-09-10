# -*- coding: utf-8 -*-
"""
Skrip Restrukturisasi Kode Mata Kuliah Peminatan (STA, STB, STC)
Kurikulum OBE SISTEKIN 2026

Mengubah kodifikasi 18 MK peminatan dari format 2-digit:
  STA-01..06, STB-01..06, STC-01..06
menjadi format 3-digit berbasis semester dengan reset ke 01 per semester:
  Sem 5: STA-501, STB-501, STC-501
  Sem 6: STA-601..602, STB-601..602, STC-601..602
  Sem 7: STA-701..703, STB-701..703, STC-701..703
Serta usulan 2027 (Dok 025):
  Sem 5: 502, 503
  Sem 6: 603, 604
  Sem 7: 704, 705
"""
import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

MAPPING_EXACT = {
    # Peminatan 1 (STA)
    "STA-01": "STA-501",
    "STA-02": "STA-601",
    "STA-03": "STA-602",
    "STA-04": "STA-701",
    "STA-05": "STA-702",
    "STA-06": "STA-703",
    # Peminatan 2 (STB)
    "STB-01": "STB-501",
    "STB-02": "STB-601",
    "STB-03": "STB-602",
    "STB-04": "STB-701",
    "STB-05": "STB-702",
    "STB-06": "STB-703",
    # Peminatan 3 (STC)
    "STC-01": "STC-501",
    "STC-02": "STC-601",
    "STC-03": "STC-602",
    "STC-04": "STC-701",
    "STC-05": "STC-702",
    "STC-06": "STC-703",
    # Usulan Dokumen 025 (2027)
    "STA-07": "STA-502",
    "STA-08": "STA-503",
    "STA-09": "STA-603",
    "STA-10": "STA-604",
    "STA-11": "STA-704",
    "STA-12": "STA-705",
    "STB-07": "STB-502",
    "STB-08": "STB-503",
    "STB-09": "STB-603",
    "STB-10": "STB-604",
    "STB-11": "STB-704",
    "STB-12": "STB-705",
    "STC-07": "STC-502",
    "STC-08": "STC-503",
    "STC-09": "STC-603",
    "STC-10": "STC-604",
    "STC-11": "STC-704",
    "STC-12": "STC-705",
}

MAPPING_RANGES = [
    (r"\bSTA-01\.\.06\b", "STA-501..703"),
    (r"\bSTB-01\.\.06\b", "STB-501..703"),
    (r"\bSTC-01\.\.06\b", "STC-501..703"),
    (r"\bSTA-01\.\.STA-06\b", "STA-501..STA-703"),
    (r"\bSTB-01\.\.STB-06\b", "STB-501..STB-703"),
    (r"\bSTC-01\.\.STC-06\b", "STC-501..STC-703"),
    (r"\bSTA-03\.\.06\b", "STA-602, STA-701..703"),
    (r"\bSTC-03\.\.05\b", "STC-602, STC-701..702"),
    (r"\bSTA-07\.\.12\b", "STA-502..705"),
    (r"\bSTB-07\.\.12\b", "STB-502..705"),
    (r"\bSTC-07\.\.12\b", "STC-502..705"),
]

def proses_file(filepath):
    if not os.path.isfile(filepath):
        return 0
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    new_content = content

    # 1. Ganti range patterns terlebih dahulu
    for pat, rep in MAPPING_RANGES:
        new_content = re.sub(pat, rep, new_content)

    # 2. Ganti exact patterns dengan word boundary
    for old_code, new_code in MAPPING_EXACT.items():
        pat = r"\b" + re.escape(old_code) + r"\b"
        new_content = re.sub(pat, new_code, new_content)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return 1
    return 0

def main():
    print("=" * 70)
    print("RESTRUKTURISASI KODE MK PEMINATAN (STA, STB, STC)")
    print("=" * 70)

    # File target
    md_files = glob.glob(os.path.join(BASE_DIR, "*.md"))
    agents_md = os.path.join(ROOT_DIR, "AGENTS.md")
    all_files = md_files + ([agents_md] if os.path.isfile(agents_md) else [])

    count_modified = 0
    for f in all_files:
        if proses_file(f):
            count_modified += 1
            print(f"[MODIFIED] {os.path.basename(f)}")

    print(f"\nTotal file Markdown diperbarui: {count_modified} dari {len(all_files)} file.")

    # Perbarui skrip-skrip pengujian & tooling di _tools/
    tool_files = glob.glob(os.path.join(BASE_DIR, "_tools", "*.py"))
    for tf in tool_files:
        if os.path.basename(tf) == "restrukturisasi_kode_peminatan.py":
            continue
        if proses_file(tf):
            print(f"[TOOL MODIFIED] {os.path.basename(tf)}")

if __name__ == "__main__":
    main()
