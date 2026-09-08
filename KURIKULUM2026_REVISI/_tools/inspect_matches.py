import os
import re

base = r'd:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI'

files = [
    '013_REKOMENDASI_SOLUSI_DAN_MITIGASI_KELEMAHAN_KURIKULUM.md',
    '017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md',
    '023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md',
    '024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md'
]

for fn in files:
    with open(os.path.join(base, fn), encoding='utf-8') as f:
        lines = f.readlines()
    print(f"=== {fn} ===")
    for i, line in enumerate(lines):
        line_clean = line.encode('ascii', errors='replace').decode('ascii')
        if re.search(r'STI-519[^|\n]*Deep Learning', line, re.I):
            print(f"  Line {i+1} [STI-519 DL]: {line_clean.strip()}")
        if re.search(r'Deep Learning[^|\n]*\([^)]*Sem 5\)', line):
            print(f"  Line {i+1} [DL Sem 5]: {line_clean.strip()}")
        if re.search(r'STI-626[^|\n]*Keamanan Informasi Lanjut', line, re.I):
            print(f"  Line {i+1} [STI-626 Keamanan]: {line_clean.strip()}")
        if re.search(r'STI-625[^|\n]*(?:3\s*SKS|Smart City\s*\(\s*3\s*\))', line):
            print(f"  Line {i+1} [STI-625 3 SKS]: {line_clean.strip()}")
        if re.search(r'STI-624[^|\n]*STI-519', line):
            print(f"  Line {i+1} [STI-624 pra STI-519]: {line_clean.strip()}")
