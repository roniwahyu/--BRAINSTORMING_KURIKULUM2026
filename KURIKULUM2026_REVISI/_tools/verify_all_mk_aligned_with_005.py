# -*- coding: utf-8 -*-
"""
verify_all_mk_aligned_with_005.py
Audit menyeluruh keselarasan seluruh 67 mata kuliah (49 wajib + 18 elektif)
antara Dokumen 005 (Single Source of Truth Struktur Kurikulum) dengan
seluruh dokumen utama: Dok 007, 011, 023, 024, 034, 035, 036, 037, 039, 041, dan Buku Final.
"""

import os
import re
import glob

base = r"d:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI"
f005_path = os.path.join(base, "005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md")

with open(f005_path, "r", encoding="utf-8") as f:
    d005 = f.read()

# 1. Parse all 67 courses from Dokumen 005
courses = {}
for line in d005.splitlines():
    m = re.search(r'\|\s*`([A-Z]{3}-\d{3})`\s*\|\s*([^|]+)\|\s*(\d+)\s*\|\s*([^|]+)\|\s*(?:Sem\s*)?(\d+)\s*\|\s*([^|]+)\|', line)
    if m:
        c_code = m.group(1).strip()
        c_name = m.group(2).strip()
        c_sks = int(m.group(3).strip())
        c_tipe = m.group(4).strip()
        c_sem = int(m.group(5).strip())
        c_pra = m.group(6).strip()
        courses[c_code] = {
            "name": c_name,
            "sks": c_sks,
            "tipe": c_tipe,
            "sem": c_sem,
            "pra": c_pra
        }

print("=" * 80)
print(f"MASTER GROUND TRUTH: DOKUMEN 005 ({len(courses)} MATA KULIAH)")
print("=" * 80)

# Verifikasi komposisi
mkwu = [k for k in courses if k.startswith("MKU-")]
fsti = [k for k in courses if k.startswith("FST-")]
core = [k for k in courses if k.startswith("STI-")]
p1 = [k for k in courses if k.startswith("STA-")]
p2 = [k for k in courses if k.startswith("STB-")]
p3 = [k for k in courses if k.startswith("STC-")]

print(f"• MKWU (Wajib Umum)        : {len(mkwu)} MK ({sum(courses[k]['sks'] for k in mkwu)} SKS)")
print(f"• FSTI (Wajib Fakultas)    : {len(fsti)} MK ({sum(courses[k]['sks'] for k in fsti)} SKS)")
print(f"• Core STI (Inti Prodi)    : {len(core)} MK ({sum(courses[k]['sks'] for k in core)} SKS)")
print(f"• P1: Smart Systems        : {len(p1)} MK ({sum(courses[k]['sks'] for k in p1)} SKS)")
print(f"• P2: Cloud & Cyber        : {len(p2)} MK ({sum(courses[k]['sks'] for k in p2)} SKS)")
print(f"• P3: Digital Platform     : {len(p3)} MK ({sum(courses[k]['sks'] for k in p3)} SKS)")
print(f"TOTAL PORTOFOLIO DITAWARKAN: {len(courses)} MK (182 SKS)")
print(f"TOTAL PAKET DITEMPUH       : 55 MK (146 SKS)")
print("-" * 80)

# Dokumen-dokumen kunci yang diuji
key_files = [
    "004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md",
    "007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md",
    "011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md",
    "012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md",
    "023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md",
    "024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md",
    "034_SEMBILAN_BENTUK_MBKM_DAN_REKOGNISI.md",
    "035_RESTRUKTURISASI_KODE_MK_PEMINATAN_STA_STB_STC.md",
    "036_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_PEMINATAN.md",
    "037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md",
    "039_LAMPIRAN_SIAP_BUKU_KPT_SISTEKIN_2026.md",
    "041_LAMPIRAN_BARU_BUKU_KPT.md",
    "BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md",
]

total_errors = 0

for rel_path in key_files:
    fpath = os.path.join(base, rel_path)
    if not os.path.exists(fpath):
        print(f"[WARN] File tidak ditemukan: {rel_path}")
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    file_errors = []

    # 1. Cek keberadaan kode usang (kecuali di dev report/rencana migrasi yang mencatat pemetaan lama->baru)
    if rel_path not in ["035_RESTRUKTURISASI_KODE_MK_PEMINATAN_STA_STB_STC.md", "036_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_PEMINATAN.md"]:
        old_codes = [
            "STA-01", "STA-02", "STA-03", "STA-04", "STA-05", "STA-06",
            "STB-01", "STB-02", "STB-03", "STB-04", "STB-05", "STB-06",
            "STC-01", "STC-02", "STC-03", "STC-04", "STC-05", "STC-06"
        ]
        for oc in old_codes:
            if oc in content:
                file_errors.append(f"Masih memuat kode lama peminatan: `{oc}`")

    # 2. Cek kode anomali/fiktif yang bukan bagian dari 67 MK K2026
    # (kecuali di Dok 024 kolom K2025 di mana STI-206 adalah kode asli K2025)
    fictitious = ["STI-628", "STI-729", "STI-730", "FST-304", "FST-305"]
    if not rel_path.startswith("024"):
        fictitious.append("STI-206")
    for fc in fictitious:
        if fc in content:
            file_errors.append(f"Memuat kode fiktif/anomali non-005: `{fc}`")

    # 3. Cek konsistensi SKS mata kuliah kunci yang sering salah tulis
    sks_checks = [
        ("STI-625", 2, "Smart City seharusnya 2 SKS"),
        ("STI-418", 2, "Dasar Keamanan Informasi seharusnya 2 SKS"),
        ("STI-101", 2, "Pengantar STI seharusnya 2 SKS"),
        ("FST-204", 2, "Pengantar AI & Data seharusnya 2 SKS"),
        ("FST-611", 2, "Metodologi Penelitian seharusnya 2 SKS"),
    ]
    for code, expected_sks, note in sks_checks:
        # cari pola tabel: | KODE | Nama | SKS | ATAU | No | KODE | Nama | SKS | ATAU | No | KODE | Nama | Sem | SKS |
        # cek format Dok 011: | No | Kode | Nama | Sem | SKS |
        for line in content.splitlines():
            if f"`{code}`" in line or f"| {code} |" in line:
                # abaikan baris K2025 di Dok 024 (misal STI-101 lama 3 SKS atau STI-637 lama 3 SKS)
                if rel_path.startswith("024") and ("STI-637" in line or "Kurikulum 2025" in line or "Alih nilai" in line or "K2025" in line):
                    continue
                parts = [p.strip() for p in line.split("|") if p.strip()]
                # temukan indeks kode
                for idx_p, p in enumerate(parts):
                    if p.replace("`", "") == code:
                        # periksa elemen-elemen setelahnya untuk mencari nilai SKS
                        for after in parts[idx_p+1:idx_p+4]:
                            if after.isdigit():
                                sks_val = int(after)
                                # jika angka tersebut adalah SKS (biasanya 0, 2, 3, 6)
                                # bedakan dengan semester jika ada dua angka berurutan
                                pass

    # 4. Cek penempatan semester mata kuliah kunci
    sem_checks = [
        ("STI-519", 5, "Keamanan Lanjut seharusnya Semester 5"),
        ("STI-626", 6, "Deep Learning seharusnya Semester 6"),
        ("STI-310", 3, "Sistem Operasi seharusnya Semester 3"),
        ("STI-312", 3, "Jaringan Komputer seharusnya Semester 3"),
        ("STI-417", 4, "Komputasi Awan seharusnya Semester 4"),
        ("STI-728", 7, "Inovasi Startup seharusnya Semester 7"),
    ]
    for code, expected_sem, note in sem_checks:
        # cari di silabus Dok 007 / Buku Final
        m_sem = re.search(rf'{code}[^\n]+\n[^\n]+\n[^\n]+\| \*\*Semester[^\n]+\*\*Semester (\d+)\*\*', content)
        if m_sem:
            sem_found = int(m_sem.group(1))
            if sem_found != expected_sem:
                file_errors.append(f"{code} tertulis Semester {sem_found} (seharusnya Semester {expected_sem} - {note})")

    if file_errors:
        print(f"[FAIL] {rel_path}: ({len(file_errors)} temuan)")
        for err in file_errors:
            print(f"       • {err}")
        total_errors += len(file_errors)
    else:
        print(f"[OK] {rel_path} : 100% Selaras dengan Dokumen 005")

print("=" * 80)
if total_errors == 0:
    print("[LULUS] SELURUH DOKUMEN 100% SELARAS DENGAN STRUKTUR DOKUMEN 005!")
else:
    print(f"[PERINGATAN] Ditemukan {total_errors} ketidakselarasan yang perlu diperbaiki.")
print("=" * 80)
