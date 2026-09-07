import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REVISI_DIR = os.path.dirname(BASE_DIR)

print(f"Applying perfect alignment for Dokumen 005 across codebase...")

# -----------------------------------------------------------------------------
# 1. UPDATE DOKUMEN 005
# -----------------------------------------------------------------------------
f005 = os.path.join(REVISI_DIR, "005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md")
with open(f005, "r", encoding="utf-8") as f:
    c005 = f.read()

# 1.1 Mermaid diagram
c005 = c005.replace(
    'S4 --> S5["Sem 5 (21 SKS): Deep Learning, IoT, Mobile, KPM, Peminatan 1"]\n        S5 --> S6["Sem 6 (19 SKS): Smart AI, Smart City 2 SKS, Platform Eng, Peminatan 2-3"]',
    'S4 --> S5["Sem 5 (21 SKS): Keamanan Lanjut, IoT, Mobile, KPM, Peminatan 1"]\n        S5 --> S6["Sem 6 (19 SKS): Deep Learning, Smart AI, Smart City 2 SKS, Platform Eng, Peminatan 2-3"]'
)

# 1.2 Tabel Sebaran 8 Semester (line 150-151)
c005 = c005.replace(
    "| **Sem 5** | Deep Learning & IoT | 7 MK | 21 SKS | Deep Learning, IoT, Mobile, KPM, Peminatan 1 |\n| **Sem 6** | AI Integrasi & Platform | 7 MK | 19 SKS | Smart AI, Smart City, Platform, Metopel |",
    "| **Sem 5** | Keamanan Lanjut & IoT | 7 MK | 21 SKS | Keamanan Lanjut, Data Mining, IoT, Mobile, KPM, Peminatan 1 |\n| **Sem 6** | Deep Learning & Platform | 7 MK | 19 SKS | Integrasi AI, Smart City, Deep Learning, Platform Eng, Metopen |"
)

# 1.3 Header Semester 5 & Semester 6
c005 = c005.replace(
    "### SEMESTER 5 (21 SKS) — Tahap Spesialisasi Deep Learning, IoT & Peminatan 1",
    "### SEMESTER 5 (21 SKS) — Tahap Spesialisasi Keamanan Lanjut, IoT & Peminatan 1"
)
c005 = c005.replace(
    "### SEMESTER 6 (19 SKS) — Tahap Spesialisasi MBKM & Platform Engineering",
    "### SEMESTER 6 (19 SKS) — Tahap Spesialisasi Deep Learning, Platform Engineering & MBKM"
)

# 1.4 Tabel 3.1
c005 = c005.replace(
    "| **Sem 5** | 7 MK | 21 SKS | 101 SKS | 14,4% | Tahap Spesialisasi Deep Learning & IoT |\n| **Sem 6** | 7 MK | 19 SKS | 120 SKS | 13,0% | Tahap Spesialisasi MBKM & Platform Eng |",
    "| **Sem 5** | 7 MK | 21 SKS | 101 SKS | 14,4% | Tahap Spesialisasi Keamanan Lanjut & IoT |\n| **Sem 6** | 7 MK | 19 SKS | 120 SKS | 13,0% | Tahap Spesialisasi Deep Learning & Platform Eng |"
)

with open(f005, "w", encoding="utf-8") as f:
    f.write(c005)
print("Updated 005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md")


# -----------------------------------------------------------------------------
# 2. UPDATE DOKUMEN 007 (STI-625: 2 SKS Teori, Prasyarat STI-521, 4x Asesmen Teori)
# -----------------------------------------------------------------------------
f007 = os.path.join(REVISI_DIR, "007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md")
with open(f007, "r", encoding="utf-8") as f:
    c007 = f.read()

# Tabel 39.A
c007 = c007.replace(
    "| **Bobot SKS / Tipe** | **3 SKS** / Tipe: **+P** (100m Teori + 170m Lab + 180m Mandiri) |\n| **Semester / Rumpun MK** | **Semester 6** / Sistem Informasi & Tata Kelola (Core STI) |\n| **Prasyarat Akademik** | `STI-101` Pengantar Sistem & TI |",
    "| **Bobot SKS / Tipe** | **2 SKS** / Tipe: **Teori** (100m Kuliah + 120m Mandiri) |\n| **Semester / Rumpun MK** | **Semester 6** / Sistem Informasi & Tata Kelola (Core STI) |\n| **Prasyarat Akademik** | `STI-521` Internet of Things (IoT) |"
)

# Tabel 39.C Asesmen UTS & Tugas 2 to Teori
c007 = c007.replace(
    "| **8** | **EVALUASI TENGAH SEMESTER (UTS)** | **Ujian Analisis Domain SPBE & Koding Pemetaan Spasial Web GIS** | **Ujian Tertulis & Lab (170m)** | **UTS: Evaluasi Proyek Awal 50% / Ujian Praktik (Bobot: 25%)** |",
    "| **8** | **EVALUASI TENGAH SEMESTER (UTS)** | **Ujian Analisis Domain SPBE & Arsitektur Layanan Smart City** | **Ujian Tertulis / Case Analysis (100m)** | **UTS: Ujian Tertulis Teori (Bobot: 30%)** |"
)
c007 = c007.replace(
    "| **12** | **Mampu menyusun skema interoperabilitas Satu Data Indonesia (C4)** | **Interoperabilitas Data Publik: Arsitektur API SPBE & Integrasi Antar-OPD** | **Case Method Class (270m)** | **Tugas 2: Milestone Proyek 2 / Blueprint SPBE (Bobot: 25%)** |",
    "| **12** | **Mampu menyusun skema interoperabilitas Satu Data Indonesia (C4)** | **Interoperabilitas Data Publik: Arsitektur API SPBE & Integrasi Antar-OPD** | **Case Method Class (270m)** | **Tugas 2: Milestone Blueprint SPBE (Bobot: 20%)** |"
)

with open(f007, "w", encoding="utf-8") as f:
    f.write(c007)
print("Updated 007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md")


# -----------------------------------------------------------------------------
# 3. UPDATE BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md
# -----------------------------------------------------------------------------
fbuku = os.path.join(REVISI_DIR, "BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md")
with open(fbuku, "r", encoding="utf-8") as f:
    cbuku = f.read()

# 3.1 Semester 6 table (lines 290-301)
cbuku = cbuku.replace(
    "### SEMESTER 6 (20 SKS)",
    "### SEMESTER 6 (19 SKS)"
)
cbuku = cbuku.replace(
    "| 40 | `STI-625` | Smart City & Pemerintahan Digital | 2 | +P | Core STI | `STI-521` |",
    "| 40 | `STI-625` | Smart City & Pemerintahan Digital | 2 | Teori | Core STI | `STI-521` |"
)
cbuku = cbuku.replace(
    "| **SUBTOTAL** | — | **Total SKS Semester 6 (7 MK)** | **20** | — | — | **Kumulatif: 121 SKS** |",
    "| **SUBTOTAL** | — | **Total SKS Semester 6 (7 MK)** | **19** | — | — | **Kumulatif: 120 SKS** |"
)
cbuku = cbuku.replace(
    "| **SUBTOTAL** | — | **Total SKS Semester 7 (7 MK)** | **20** | — | — | **Kumulatif: 141 SKS** |",
    "| **SUBTOTAL** | — | **Total SKS Semester 7 (7 MK)** | **20** | — | — | **Kumulatif: 140 SKS** |"
)

# 3.2 Tabel 3.1 Kalkulasi SKS (lines 324-334)
cbuku = cbuku.replace(
    "| Sem 5 | 7 MK | 21 SKS | 101 SKS | 14,3% | Tahap Spesialisasi Deep Learning & IoT |\n| Sem 6 | 7 MK | 20 SKS | 121 SKS | 13,6% | Tahap Spesialisasi MBKM & Platform Eng |\n| Sem 7 | 7 MK | 20 SKS | 141 SKS | 13,6% | Tahap Integrasi Capstone, PKL & Sempro |",
    "| Sem 5 | 7 MK | 21 SKS | 101 SKS | 14,4% | Tahap Spesialisasi Keamanan Lanjut & IoT |\n| Sem 6 | 7 MK | 19 SKS | 120 SKS | 13,0% | Tahap Spesialisasi Deep Learning & Platform Eng |\n| Sem 7 | 7 MK | 20 SKS | 140 SKS | 13,7% | Tahap Integrasi Capstone, PKL & Sempro |"
)

# 3.3 Line 390 list
cbuku = cbuku.replace(
    "• STI-625 Smart City (3)",
    "• STI-625 Smart City (2)"
)

# 3.4 Silabus STI-625 in BUKU
cbuku = cbuku.replace(
    "| **Kode & Nama Mata Kuliah** | **STI-625 — Smart City & Pemerintahan Digital** (*Smart City & Digital Governance*) |\n| **Bobot SKS / Tipe** | **3 SKS** / Tipe: **+P** (100m Teori + 170m Lab + 180m Mandiri) |\n| **Semester / Rumpun MK** | **Semester 6** / Sistem Informasi & Tata Kelola (Core STI) |\n| **Prasyarat Akademik** | `STI-101` Pengantar Sistem & TI |",
    "| **Kode & Nama Mata Kuliah** | **STI-625 — Smart City & Pemerintahan Digital** (*Smart City & Digital Governance*) |\n| **Bobot SKS / Tipe** | **2 SKS** / Tipe: **Teori** (100m Kuliah + 120m Mandiri) |\n| **Semester / Rumpun MK** | **Semester 6** / Sistem Informasi & Tata Kelola (Core STI) |\n| **Prasyarat Akademik** | `STI-521` Internet of Things (IoT) |"
)
cbuku = cbuku.replace(
    "| **8** | **EVALUASI TENGAH SEMESTER (UTS)** | **Ujian Analisis Domain SPBE & Koding Pemetaan Spasial Web GIS** | **Ujian Tertulis & Lab (170m)** | **UTS: Evaluasi Proyek Awal 50% / Ujian Praktik (Bobot: 25%)** |",
    "| **8** | **EVALUASI TENGAH SEMESTER (UTS)** | **Ujian Analisis Domain SPBE & Arsitektur Layanan Smart City** | **Ujian Tertulis / Case Analysis (100m)** | **UTS: Ujian Tertulis Teori (Bobot: 30%)** |"
)
cbuku = cbuku.replace(
    "| **12** | **Mampu menyusun skema interoperabilitas Satu Data Indonesia (C4)** | **Interoperabilitas Data Publik: Arsitektur API SPBE & Integrasi Antar-OPD** | **Case Method Class (270m)** | **Tugas 2: Milestone Proyek 2 / Blueprint SPBE (Bobot: 25%)** |",
    "| **12** | **Mampu menyusun skema interoperabilitas Satu Data Indonesia (C4)** | **Interoperabilitas Data Publik: Arsitektur API SPBE & Integrasi Antar-OPD** | **Case Method Class (270m)** | **Tugas 2: Milestone Blueprint SPBE (Bobot: 20%)** |"
)

with open(fbuku, "w", encoding="utf-8") as f:
    f.write(cbuku)
print("Updated BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md")


# -----------------------------------------------------------------------------
# 4. UPDATE DOKUMEN LAIN (006, 023)
# -----------------------------------------------------------------------------
f006 = os.path.join(REVISI_DIR, "006_DISTRIBUSI_DAN_PANDUAN_MK_PEMINATAN_MBKM.md")
if os.path.exists(f006):
    with open(f006, "r", encoding="utf-8") as f:
        c006 = f.read()
    c006 = c006.replace("• STI-625 Smart City (3)", "• STI-625 Smart City (2)")
    with open(f006, "w", encoding="utf-8") as f:
        f.write(c006)
    print("Updated 006_DISTRIBUSI_DAN_PANDUAN_MK_PEMINATAN_MBKM.md")

f023 = os.path.join(REVISI_DIR, "023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md")
if os.path.exists(f023):
    with open(f023, "r", encoding="utf-8") as f:
        c023 = f.read()
    c023 = c023.replace("`STI-625` Smart City (3)", "`STI-625` Smart City (2)")
    with open(f023, "w", encoding="utf-8") as f:
        f.write(c023)
    print("Updated 023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md")

print("\nPERFECT ALIGNMENT SELESAI!")
