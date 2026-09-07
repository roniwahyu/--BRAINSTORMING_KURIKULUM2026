"""
Script swap definitif:
1. Tukar posisi dan silabus:
   - Deep Learning & Neural Networks: dari Sem 5 (lama STI-519) -> Sem 6 (baru STI-626)
   - Keamanan Informasi Lanjut: dari Sem 6 (lama STI-626) -> Sem 5 (baru STI-519)
2. Sesuaikan prasyarat:
   - STI-624 (Sem 6): prasyarat menjadi STI-413 & STI-416 (karena DL sekarang satu semester di Sem 6)
   - STA-04, STA-05, STA-06 (Sem 7): prasyarat DL merujuk STI-626
   - STB-05 (Sem 7): prasyarat Keamanan Lanjut merujuk STI-519
3. Sesuaikan dokumen 024 (matriks ekivalensi):
   - STI-634 asal K2025 memetakan ke STI-626 (Sem 6, E2)
   - Sem 5 K2026: memiliki STI-519 (Wajib Tempuh, defisit 3 SKS)
   - Sem 6 K2026: memiliki STI-626 (Diakui dari STI-634, defisit 0 SKS)
   - Neraca 3A.3: Sem 5 diakui 15 / defisit 3; Sem 6 diakui 13 / defisit 0; Total 114 diakui / 14 defisit
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REVISI_DIR = os.path.dirname(BASE_DIR)

print(f"Working directory: {REVISI_DIR}")

# -----------------------------------------------------------------------------
# 1. UPDATE DOKUMEN 005 (005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md)
# -----------------------------------------------------------------------------
f005 = os.path.join(REVISI_DIR, "005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md")
with open(f005, "r", encoding="utf-8") as f:
    c005 = f.read()

# 1.1 Tabel 1.3
c005 = c005.replace(
    "| 19 | `STI-519` | Deep Learning & Neural Networks | 3 | +P | Sem 5 | `STI-413` |",
    "| 19 | `STI-519` | Keamanan Informasi Lanjut | 3 | Teori | Sem 5 | `STI-418` |"
)
c005 = c005.replace(
    "| 24 | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | Sem 6 | `STI-519`, `STI-416` |",
    "| 24 | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | Sem 6 | `STI-413`, `STI-416` |"
)
c005 = c005.replace(
    "| 26 | `STI-626` | Keamanan Informasi Lanjut | 3 | Teori | Sem 6 | `STI-418` |",
    "| 26 | `STI-626` | Deep Learning & Neural Networks | 3 | +P | Sem 6 | `STI-413` |"
)

# 1.2 Ringkasan Sebaran
c005 = c005.replace(
    "| **Sem 5** | AI Lanjut, Data Mining & IoT | 7 MK | 21 SKS | Deep Learning, Data Mining, IoT, Mobile, KPM, Peminatan 1 |",
    "| **Sem 5** | Keamanan Lanjut, Data Mining & IoT | 7 MK | 21 SKS | Keamanan Lanjut, Data Mining, IoT, Mobile, KPM, Peminatan 1 |"
)
c005 = c005.replace(
    "| **Sem 6** | Platform Eng, Smart City & MBKM | 7 MK | 19 SKS | Integrasi AI, Smart City, Keamanan Lanjut, Platform Eng, Metopen |",
    "| **Sem 6** | Deep Learning, Smart City & Platform Eng | 7 MK | 19 SKS | Integrasi AI, Smart City, Deep Learning, Platform Eng, Metopen |"
)

# 1.3 Rincian Semester 5
c005 = c005.replace(
    "### SEMESTER 5 (21 SKS) — Tahap Spesialisasi AI Lanjut, IoT & Peminatan 1",
    "### SEMESTER 5 (21 SKS) — Tahap Spesialisasi Keamanan Lanjut, IoT & Peminatan 1"
)
c005 = c005.replace(
    "| 32 | `STI-519` | Deep Learning & Neural Networks | 3 | +P | Core STI | `STI-413` |",
    "| 32 | `STI-519` | Keamanan Informasi Lanjut | 3 | Teori | Core STI | `STI-418` |"
)

# 1.4 Rincian Semester 6
c005 = c005.replace(
    "### SEMESTER 6 (19 SKS) — Tahap Spesialisasi Platform Engineering & MBKM",
    "### SEMESTER 6 (19 SKS) — Tahap Spesialisasi Deep Learning, Platform Engineering & MBKM"
)
c005 = c005.replace(
    "| 39 | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | Core STI | `STI-519`, `STI-416` |",
    "| 39 | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | Core STI | `STI-413`, `STI-416` |"
)
c005 = c005.replace(
    "| 41 | `STI-626` | Keamanan Informasi Lanjut | 3 | Teori | Core STI | `STI-418` |",
    "| 41 | `STI-626` | Deep Learning & Neural Networks | 3 | +P | Core STI | `STI-413` |"
)

with open(f005, "w", encoding="utf-8") as f:
    f.write(c005)
print("Updated 005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md")


# -----------------------------------------------------------------------------
# 2. UPDATE DOKUMEN 007 & BUKU_KURIKULUM (SWAP SILABUS MK 32 & MK 40)
# -----------------------------------------------------------------------------
def swap_syllabus_sections(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Ekstrak Section 32 (Deep Learning)
    # Dari '### 32. STI-519 — Deep Learning & Neural Networks' sampai sebelum '### 33.'
    m32 = re.search(r"(### 32\. STI-519 — Deep Learning & Neural Networks.*?\n)(?=---\s*\n+### 33\.)", content, re.DOTALL)
    if not m32:
        print(f"ERROR: Section 32 not found in {filepath}")
        return
    sec32_old = m32.group(1)

    # Ekstrak Section 40 (Keamanan Informasi Lanjut)
    # Dari '### 40. STI-626 — Keamanan Informasi Lanjut' sampai sebelum '### 41.'
    m40 = re.search(r"(### 40\. STI-626 — Keamanan Informasi Lanjut.*?\n)(?=---\s*\n+### 41\.)", content, re.DOTALL)
    if not m40:
        print(f"ERROR: Section 40 not found in {filepath}")
        return
    sec40_old = m40.group(1)

    # Transformasi Section 40 (Keamanan Lanjut) menjadi Section 32 (Sem 5, STI-519)
    sec32_new = sec40_old
    sec32_new = sec32_new.replace("### 40. STI-626 — Keamanan Informasi Lanjut", "### 32. STI-519 — Keamanan Informasi Lanjut")
    sec32_new = sec32_new.replace("#### Tabel 40.A:", "#### Tabel 32.A:")
    sec32_new = sec32_new.replace("#### Tabel 40.B:", "#### Tabel 32.B:")
    sec32_new = sec32_new.replace("#### Tabel 40.C:", "#### Tabel 32.C:")
    sec32_new = sec32_new.replace("**STI-626 — Keamanan Informasi Lanjut**", "**STI-519 — Keamanan Informasi Lanjut**")
    sec32_new = sec32_new.replace("**Semester 6**", "**Semester 5**")

    # Transformasi Section 32 (Deep Learning) menjadi Section 40 (Sem 6, STI-626)
    sec40_new = sec32_old
    sec40_new = sec40_new.replace("### 32. STI-519 — Deep Learning & Neural Networks", "### 40. STI-626 — Deep Learning & Neural Networks")
    sec40_new = sec40_new.replace("#### Tabel 32.A:", "#### Tabel 40.A:")
    sec40_new = sec40_new.replace("#### Tabel 32.B:", "#### Tabel 40.B:")
    sec40_new = sec40_new.replace("#### Tabel 32.C:", "#### Tabel 40.C:")
    sec40_new = sec40_new.replace("**STI-519 — Deep Learning & Neural Networks**", "**STI-626 — Deep Learning & Neural Networks**")
    sec40_new = sec40_new.replace("**Semester 5**", "**Semester 6**")

    # Ganti di dokumen
    content = content.replace(sec32_old, sec32_new)
    content = content.replace(sec40_old, sec40_new)

    # Update prasyarat pada MK lain
    # STI-624
    content = content.replace(
        "| **Prasyarat Akademik** | `STI-519` Deep Learning & Neural Networks |",
        "| **Prasyarat Akademik** | `STI-413` Machine Learning & `STI-416` Web Back End Development |"
    )
    # STA-04
    content = content.replace(
        "| **Prasyarat Akademik** | `STI-519` Deep Learning & `STI-417` Komputasi Awan |",
        "| **Prasyarat Akademik** | `STI-626` Deep Learning & `STI-417` Komputasi Awan |"
    )
    # STA-05
    content = content.replace(
        "| **Prasyarat Akademik** | `STI-519` Deep Learning & Neural Networks |",
        "| **Prasyarat Akademik** | `STI-414` Pengantar NLP & IR & `STI-626` Deep Learning |"
    )
    # STA-06
    content = content.replace(
        "| **Prasyarat Akademik** | `STI-519` Deep Learning & `STI-521` IoT |",
        "| **Prasyarat Akademik** | `STI-626` Deep Learning & `STI-521` IoT |"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated and swapped syllabus in {os.path.basename(filepath)}")

swap_syllabus_sections(os.path.join(REVISI_DIR, "007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md"))

# Di BUKU_KURIKULUM juga perlu update tabel sebaran MK di Bab 5
fbuku = os.path.join(REVISI_DIR, "BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md")
with open(fbuku, "r", encoding="utf-8") as f:
    cbuku = f.read()

cbuku = cbuku.replace(
    "| 19 | `STI-519` | Deep Learning & Neural Networks | 3 | +P | Sem 5 | `STI-413` |",
    "| 19 | `STI-519` | Keamanan Informasi Lanjut | 3 | Teori | Sem 5 | `STI-418` |"
)
cbuku = cbuku.replace(
    "| 24 | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | Sem 6 | `STI-519`, `STI-416` |",
    "| 24 | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | Sem 6 | `STI-413`, `STI-416` |"
)
cbuku = cbuku.replace(
    "| 26 | `STI-626` | Keamanan Informasi Lanjut | 3 | Teori | Sem 6 | `STI-418` |",
    "| 26 | `STI-626` | Deep Learning & Neural Networks | 3 | +P | Sem 6 | `STI-413` |"
)
cbuku = cbuku.replace(
    "| 32 | `STI-519` | Deep Learning & Neural Networks | 3 | +P | Core STI | `STI-413` |",
    "| 32 | `STI-519` | Keamanan Informasi Lanjut | 3 | Teori | Core STI | `STI-418` |"
)
cbuku = cbuku.replace(
    "| 39 | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | Core STI | `STI-519`, `STI-416` |",
    "| 39 | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | Core STI | `STI-413`, `STI-416` |"
)
cbuku = cbuku.replace(
    "| 41 | `STI-626` | Keamanan Informasi Lanjut | 3 | Teori | Core STI | `STI-418` |",
    "| 41 | `STI-626` | Deep Learning & Neural Networks | 3 | +P | Core STI | `STI-413` |"
)
with open(fbuku, "w", encoding="utf-8") as f:
    f.write(cbuku)

swap_syllabus_sections(fbuku)


# -----------------------------------------------------------------------------
# 3. UPDATE DOKUMEN 004 (004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md)
# -----------------------------------------------------------------------------
f004 = os.path.join(REVISI_DIR, "004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md")
with open(f004, "r", encoding="utf-8") as f:
    c004 = f.read()

# Row 32 & 41 in Matriks CPL (Section 2.1)
c004 = c004.replace(
    "| 32 | `STI-519` | Deep Learning & Neural Net | 3 | | | | | | | | | **R** | **R** | | | | | PL-1 | PEO-1, PEO-3 | **R** |",
    "| 32 | `STI-519` | Keamanan Informasi Lanjut | 3 | | | | | | | **M** | | | | **M** | **M** | | | PL-2 | PEO-1 | **M** |"
)
c004 = c004.replace(
    "| 41 | `STI-626` | Keamanan Informasi Lanjut | 3 | | | | | | | **M** | | | | **M** | **M** | | | PL-2 | PEO-1 | **M** |",
    "| 41 | `STI-626` | Deep Learning & Neural Net | 3 | | | | | | | | | **R** | **R** | | | | | PL-1 | PEO-1, PEO-3 | **R** |"
)

# BoK mapping in Section 3
c004 = c004.replace(
    "| **BK-IS18** | *Machine Learning and Data Science* | `STI-413`, `STI-519`, `STA-04` | `STA-02`, `STA-06` | 5 MK | ✅ Sangat Kuat |",
    "| **BK-IS18** | *Machine Learning and Data Science* | `STI-413`, `STI-626`, `STA-04` | `STA-02`, `STA-06` | 5 MK | ✅ Sangat Kuat |"
)
c004 = c004.replace(
    "| **BK-IT02** | *Applied AI & Intelligent Technologies* | `STI-307`, `STI-413`, `STI-414`, `STI-519`, `STI-624` | `STA-03..06` | 9 MK | ✅ Sangat Kuat |",
    "| **BK-IT02** | *Applied AI & Intelligent Technologies* | `STI-307`, `STI-413`, `STI-414`, `STI-626`, `STI-624` | `STA-03..06` | 9 MK | ✅ Sangat Kuat |"
)
c004 = c004.replace(
    "| **BK-IS06** | *Information Security and Risk Management* | `STI-418`, `STI-626`, `STB-01`, `STB-03` | `FST-206` | 5 MK | ✅ Sangat Kuat |",
    "| **BK-IS06** | *Information Security and Risk Management* | `STI-418`, `STI-519`, `STB-01`, `STB-03` | `FST-206` | 5 MK | ✅ Sangat Kuat |"
)
c004 = c004.replace(
    "| **BK-IT06** | *Cybersecurity Principles & Defense* | `STI-418`, `STI-626`, `STB-01` | `STB-03` | 4 MK | ✅ Sangat Kuat |",
    "| **BK-IT06** | *Cybersecurity Principles & Defense* | `STI-418`, `STI-519`, `STB-01` | `STB-03` | 4 MK | ✅ Sangat Kuat |"
)

# IKU 7 Table (Section 4)
c004 = c004.replace(
    "| 32 | `STI-519` | Deep Learning & Neural Net | 3 | 20% | 50% | 30% | **70%** | ✅ Patuh IKU 7 |",
    "| 32 | `STI-519` | Keamanan Informasi Lanjut | 3 | 30% | 40% | 30% | **70%** | ✅ Patuh IKU 7 |"
)
c004 = c004.replace(
    "| 41 | `STI-626` | Keamanan Informasi Lanjut | 3 | 30% | 40% | 30% | **70%** | ✅ Patuh IKU 7 |",
    "| 41 | `STI-626` | Deep Learning & Neural Net | 3 | 20% | 50% | 30% | **70%** | ✅ Patuh IKU 7 |"
)

with open(f004, "w", encoding="utf-8") as f:
    f.write(c004)
print("Updated 004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md")


# -----------------------------------------------------------------------------
# 4. UPDATE DOKUMEN 011 (011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md)
# -----------------------------------------------------------------------------
f011 = os.path.join(REVISI_DIR, "011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md")
with open(f011, "r", encoding="utf-8") as f:
    c011 = f.read()

# Sheet 2
c011 = c011.replace(
    "| 40 | STI-519 | Deep Learning & Neural Networks (+P) | 5 | 3 |  |  |  |  |  |  |  |  | V | V |  |  |  |  | 2 |",
    "| 40 | STI-519 | Keamanan Informasi Lanjut | 5 | 3 |  |  |  |  |  |  | V |  |  |  | V | V |  |  | 3 |"
)
c011 = c011.replace(
    "| 47 | STI-626 | Keamanan Informasi Lanjut | 6 | 3 |  |  |  |  |  |  | V |  |  |  | V | V |  |  | 3 |",
    "| 47 | STI-626 | Deep Learning & Neural Networks (+P) | 6 | 3 |  |  |  |  |  |  |  |  | V | V |  |  |  |  | 2 |"
)

# Sheet 3
c011 = c011.replace(
    "STI-519 Deep Learning (3) / STI-520 Data Mining (3) / STI-521 IoT (3) / STI-522 Mobile App (3) / STI-523 Manpro TI (3) / MKU-507 KPM (3) / MK Pilihan 1 (3) / MKU-508 KWU II (0)",
    "STI-519 Keamanan Lanjut (3) / STI-520 Data Mining (3) / STI-521 IoT (3) / STI-522 Mobile App (3) / STI-523 Manpro TI (3) / MKU-507 KPM (3) / MK Pilihan 1 (3) / MKU-508 KWU II (0)"
)
c011 = c011.replace(
    "STI-624 Integrasi AI (3) / STI-625 Smart City (2) / STI-626 Keamanan Lanjut (3) / STI-627 Digital Platform Eng (3) / FST-611 Metopel (2) / MK Pilihan 2 (3) / MK Pilihan 3 (3)",
    "STI-624 Integrasi AI (3) / STI-625 Smart City (2) / STI-626 Deep Learning (3) / STI-627 Digital Platform Eng (3) / FST-611 Metopel (2) / MK Pilihan 2 (3) / MK Pilihan 3 (3)"
)

# Sheet 4
c011 = c011.replace(
    "| STI-519 | Deep Learning & Neural Networks | 3 | 5 |  |  |  |  |  |  |  |  | M | M |  |  |  |  | 2 |",
    "| STI-519 | Keamanan Informasi Lanjut | 3 | 5 |  |  |  |  |  |  | M |  |  |  | M | M |  |  | 3 |"
)
c011 = c011.replace(
    "| STI-626 | Keamanan Informasi Lanjut | 3 | 6 |  |  |  |  |  |  | M |  |  |  | M | M |  |  | 3 |",
    "| STI-626 | Deep Learning & Neural Networks | 3 | 6 |  |  |  |  |  |  |  |  | M | M |  |  |  |  | 2 |"
)

# Sheet 5
c011 = c011.replace(
    "| STI-626 | Keamanan Informasi Lanjut | PL-2 | CPMK1 | Menganalisis teknik serangan lanjutan",
    "| STI-519 | Keamanan Informasi Lanjut | PL-2 | CPMK1 | Menganalisis teknik serangan lanjutan"
)
c011 = c011.replace(
    "| STI-626 | Keamanan Informasi Lanjut | PL-2 | CPMK2 | Melakukan digital forensics analysis",
    "| STI-519 | Keamanan Informasi Lanjut | PL-2 | CPMK2 | Melakukan digital forensics analysis"
)
c011 = c011.replace(
    "| STI-626 | Keamanan Informasi Lanjut | PL-2 | CPMK3 | Menyusun kebijakan keamanan informasi",
    "| STI-519 | Keamanan Informasi Lanjut | PL-2 | CPMK3 | Menyusun kebijakan keamanan informasi"
)
c011 = c011.replace(
    "| STI-627: 100% OK | STI-626: 100% OK | | | |",
    "| STI-627: 100% OK | STI-519: 100% OK | | | |"
)

# Sheet 12
c011 = c011.replace(
    "## Sheet 12: Template Evaluasi OBE - STI-626 (Keamanan)",
    "## Sheet 12: Template Evaluasi OBE - STI-519 (Keamanan)"
)
c011 = c011.replace(
    "> TEMPLATE EVALUASI OBE - STI-626 Keamanan Informasi Lanjut",
    "> TEMPLATE EVALUASI OBE - STI-519 Keamanan Informasi Lanjut"
)

# Sheet 13 & 14
c011 = c011.replace(
    "| P3 | Infrastruktur TI & keamanan | 12 | STI-521 IoT, STI-625 Smart City, STI-626 Keamanan Lanjut, FST-714 Skripsi |",
    "| P3 | Infrastruktur TI & keamanan | 12 | STI-521 IoT, STI-625 Smart City, STI-519 Keamanan Lanjut, FST-714 Skripsi |"
)
c011 = c011.replace(
    "| KK1 | AI/ML integration ke SI bisnis | 11 | STI-519 Deep Learning, STI-624 Integrasi AI, FST-610 Capstone |",
    "| KK1 | AI/ML integration ke SI bisnis | 11 | STI-626 Deep Learning, STI-624 Integrasi AI, FST-610 Capstone |"
)
c011 = c011.replace(
    "| KK2 | Data engineering & ML pipeline | 7 | STI-519 Deep Learning, STI-520 Data Mining, STA-04 MLOps |",
    "| KK2 | Data engineering & ML pipeline | 7 | STI-626 Deep Learning, STI-520 Data Mining, STA-04 MLOps |"
)
c011 = c011.replace(
    "| KK4 | Audit, GRC & tata kelola TI | 7 | STI-626 Keamanan Lanjut, STB-04 COBIT, FST-612 PKL |",
    "| KK4 | Audit, GRC & tata kelola TI | 7 | STI-519 Keamanan Lanjut, STB-04 COBIT, FST-612 PKL |"
)

with open(f011, "w", encoding="utf-8") as f:
    f.write(c011)
print("Updated 011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md")


# -----------------------------------------------------------------------------
# 5. UPDATE DOKUMEN 012 (012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md)
# -----------------------------------------------------------------------------
f012 = os.path.join(REVISI_DIR, "012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md")
with open(f012, "r", encoding="utf-8") as f:
    c012 = f.read()

c012 = c012.replace(
    "[SEM 5]  ├── STI-519 Deep Learning & Neural Networks (+P) ─────┴── STI-413 Machine Learning (+P) [SEM 4]",
    "[SEM 6]  ├── STI-626 Deep Learning & Neural Networks (+P) ─────┴── STI-413 Machine Learning (+P) [SEM 4]"
)
c012 = c012.replace(
    "yang menjadi landasan wajib bagi `STI-519 Deep Learning` (Sem 5)",
    "yang menjadi landasan wajib bagi `STI-626 Deep Learning` (Sem 6)"
)
c012 = c012.replace(
    "         ├── STI-626 Keamanan Informasi Lanjut ────────────────┤     │",
    "         ├── STI-519 Keamanan Informasi Lanjut ────────────────┤     │"
)
c012 = c012.replace(
    "   * Sem 6: Ethical Hacking, OWASP Top 10, Kali Linux (`STB-03` & `STI-626`)",
    "   * Sem 5: Keamanan Lanjut (`STI-519`), Sem 6: Ethical Hacking (`STB-03`)"
)
c012 = c012.replace(
    "| **5** | `STI-519` | Deep Learning & Neural Networks | 3 | +P | `STI-413` Machine Learning | `STI-205` Aljabar Linear, `FST-408` Probstat | 🟢 **Sangat Kuat** |",
    "| **5** | `STI-519` | Keamanan Informasi Lanjut | 3 | Teori | `STI-418` Dasar Keamanan | `STI-312` Jarkom, `STB-01` NetSec | 🟢 **Sangat Kuat** |"
)
c012 = c012.replace(
    "| **6** | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | `STI-519` DL, `STI-416` Back End | `STI-414` NLP & IR, `STI-413` ML | 🟢 **Sangat Kuat** |",
    "| **6** | `STI-624` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | `STI-413` ML, `STI-416` Back End | `STI-414` NLP & IR, `STI-307` Cerdas | 🟢 **Sangat Kuat** |"
)
c012 = c012.replace(
    "| **6** | `STI-626` | Keamanan Informasi Lanjut | 3 | Teori | `STI-418` Dasar Keamanan | `STI-312` Jarkom, `STB-01` NetSec | 🟢 **Sangat Kuat** |",
    "| **6** | `STI-626` | Deep Learning & Neural Networks | 3 | +P | `STI-413` Machine Learning | `STI-205` Aljabar Linear, `FST-408` Probstat | 🟢 **Sangat Kuat** |"
)
c012 = c012.replace(
    "| **7** | `STA-04` | MLOps & AI Pipeline *(P1)* | 3 | +P | `STI-519` DL, `STI-417` Cloud |",
    "| **7** | `STA-04` | MLOps & AI Pipeline *(P1)* | 3 | +P | `STI-626` DL, `STI-417` Cloud |"
)
c012 = c012.replace(
    "| **7** | `STA-05` | Conversational AI & LLM *(P1)* | 3 | +P | `STI-414` NLP & IR, `STI-519` DL |",
    "| **7** | `STA-05` | Conversational AI & LLM *(P1)* | 3 | +P | `STI-414` NLP & IR, `STI-626` DL |"
)
c012 = c012.replace(
    "| **7** | `STA-06` | Smart Surveillance & Edge AI *(P1)*| 3 | +P | `STI-519` DL, `STI-521` IoT |",
    "| **7** | `STA-06` | Smart Surveillance & Edge AI *(P1)*| 3 | +P | `STI-626` DL, `STI-521` IoT |"
)
c012 = c012.replace(
    "| **7** | `STB-05` | Keamanan Cloud & Kripto *(P2)* | 3 | +P | `STI-417` Cloud, `STI-626` Security |",
    "| **7** | `STB-05` | Keamanan Cloud & Kripto *(P2)* | 3 | +P | `STI-417` Cloud, `STI-519` Security |"
)

with open(f012, "w", encoding="utf-8") as f:
    f.write(c012)
print("Updated 012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md")


# -----------------------------------------------------------------------------
# 6. UPDATE DOKUMEN 024 (024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md)
# -----------------------------------------------------------------------------
f024 = os.path.join(REVISI_DIR, "024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md")
with open(f024, "r", encoding="utf-8") as f:
    c024 = f.read()

# Bagian 3: Baris 43 STI-634
c024 = c024.replace(
    "| 43 | `STI-634` | Pengolahan Citra Digital dan Vision (+P) | 3 | `STI-519` | Deep Learning & Neural Networks (+P) | 3 |  5 | **E2** | K2026 mengintegrasikan computer vision ke dalam kerangka deep learning (CNN). Overlap ± 65% → wajib uji penyetaraan pada komponen arsitektur jaringan saraf & pelatihan model |",
    "| 43 | `STI-634` | Pengolahan Citra Digital dan Vision (+P) | 3 | `STI-626` | Deep Learning & Neural Networks (+P) | 3 |  6 | **E2** | K2026 mengintegrasikan computer vision ke dalam kerangka deep learning (CNN). Overlap ± 65% → wajib uji penyetaraan pada komponen arsitektur jaringan saraf & pelatihan model |"
)

# Bagian 3A: Tabel Semester 5 & Semester 6
sem5_old = """#### SEMESTER 5 — Diakui 18 SKS Paket + 3 SKS Elektif, Defisit 0 SKS Paket ✅

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-519` | Deep Learning & Neural Networks (+P) | 3 | E2 | `STI-634` | **Uji penyetaraan** (CNN & pelatihan model) |
| `STI-520` | Data Mining & Visualisasi Data (+P) | 3 | E3/G-2 | `STI-208` + `STI-740` | Rata-rata berbobot 2 MK lama |
| `STI-521` | Internet of Things (IoT) (+P) | 3 | E1 | `STI-526` | Alih nilai langsung |
| `STI-522` | Pemrograman Aplikasi Mobile (+P) | 3 | E1 | `STI-419` | Alih nilai langsung |
| `STI-523` | Manajemen Proyek TI | 3 | E2 | `STI-421` (2 SKS) | **Tugas penyetaraan** 1 SKS |
| `MKU-507` | Kuliah Pengabdian Kepada Masyarakat (KPM) | 3 | E1 | `MKU-507` | Alih nilai langsung |
| `MKU-508` | Kewirausahaan II | 0 | E1 | `MKU-508` | Alih nilai langsung |
| *Elektif* | **MK Peminatan 1** | 3 | — | Lihat Bagian 6.3 | Bergantung jalur peminatan |

#### SEMESTER 6 — Diakui 10 SKS Paket + 6 SKS Elektif, Defisit 3 SKS Paket

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-624` | Integrasi Layanan Cerdas Berbasis AI (+P) | 3 | E2 | `STI-741` | **Praktikum penyetaraan** (MK penciri prodi) |
| `STI-625` | Smart City & Pemerintahan Digital | 2 | E1 | `STI-637` (3 SKS) | Alih nilai; 1 SKS jadi kredit bebas |
| `STI-626` | Keamanan Informasi Lanjut | 3 | **B** | — | **WAJIB TEMPUH** — jenjang keamanan lanjut |
| `STI-627` | Digital Platform Engineering (+P) | 3 | E2 | `STI-739` | **Uji penyetaraan** (reorientasi platform) |
| `FST-611` | Metodologi Penelitian | 2 | E1 | `MFT-002` | Alih nilai langsung |
| *Elektif* | **MK Peminatan 2 & 3** | 6 | — | Lihat Bagian 6.3 | Bergantung jalur peminatan |"""

sem5_new = """#### SEMESTER 5 — Diakui 15 SKS Paket + 3 SKS Elektif, Defisit 3 SKS Paket

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-519` | Keamanan Informasi Lanjut | 3 | **B** | — | **WAJIB TEMPUH** — jenjang keamanan lanjut |
| `STI-520` | Data Mining & Visualisasi Data (+P) | 3 | E3/G-2 | `STI-208` + `STI-740` | Rata-rata berbobot 2 MK lama |
| `STI-521` | Internet of Things (IoT) (+P) | 3 | E1 | `STI-526` | Alih nilai langsung |
| `STI-522` | Pemrograman Aplikasi Mobile (+P) | 3 | E1 | `STI-419` | Alih nilai langsung |
| `STI-523` | Manajemen Proyek TI | 3 | E2 | `STI-421` (2 SKS) | **Tugas penyetaraan** 1 SKS |
| `MKU-507` | Kuliah Pengabdian Kepada Masyarakat (KPM) | 3 | E1 | `MKU-507` | Alih nilai langsung |
| `MKU-508` | Kewirausahaan II | 0 | E1 | `MKU-508` | Alih nilai langsung |
| *Elektif* | **MK Peminatan 1** | 3 | — | Lihat Bagian 6.3 | Bergantung jalur peminatan |

#### SEMESTER 6 — Diakui 13 SKS Paket + 6 SKS Elektif, Defisit 0 SKS Paket ✅

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-624` | Integrasi Layanan Cerdas Berbasis AI (+P) | 3 | E2 | `STI-741` | **Praktikum penyetaraan** (MK penciri prodi) |
| `STI-625` | Smart City & Pemerintahan Digital | 2 | E1 | `STI-637` (3 SKS) | Alih nilai; 1 SKS jadi kredit bebas |
| `STI-626` | Deep Learning & Neural Networks (+P) | 3 | E2 | `STI-634` | **Uji penyetaraan** (CNN & pelatihan model) |
| `STI-627` | Digital Platform Engineering (+P) | 3 | E2 | `STI-739` | **Uji penyetaraan** (reorientasi platform) |
| `FST-611` | Metodologi Penelitian | 2 | E1 | `MFT-002` | Alih nilai langsung |
| *Elektif* | **MK Peminatan 2 & 3** | 6 | — | Lihat Bagian 6.3 | Bergantung jalur peminatan |"""

c024 = c024.replace(sem5_old, sem5_new)

# Tabel 3A.3
t3a_old = """| Sem 5 | 18 (tanpa elektif) | 18 | 0 | — | **100%** |
| Sem 6 | 13 (tanpa elektif) | 10 | 3 | `STI-626` | 76,9% |"""
t3a_new = """| Sem 5 | 18 (tanpa elektif) | 15 | 3 | `STI-519` | 83,3% |
| Sem 6 | 13 (tanpa elektif) | 13 | 0 | — | **100%** |"""
c024 = c024.replace(t3a_old, t3a_new)

# Bagian 6.1 (Tabel 6.1 MK Wajib Baru)
c024 = c024.replace(
    "| 3 | `STI-626` | Keamanan Informasi Lanjut | 3 |  6 | Core STI | Penguatan jenjang keamanan bertingkat (dasar Sem 4 → lanjut Sem 6) untuk memenuhi CPL KK4 (audit, GRC & tata kelola TI) pada jalur wajib, tidak hanya elektif |",
    "| 3 | `STI-519` | Keamanan Informasi Lanjut | 3 |  5 | Core STI | Penguatan jenjang keamanan bertingkat (dasar Sem 4 → lanjut Sem 5) untuk memenuhi CPL KK4 (audit, GRC & tata kelola TI) pada jalur wajib, tidak hanya elektif |"
)

# Bagian 7.1 (Tabel 7.1)
c024 = c024.replace(
    "| MK Inti Core STI (28 MK) | 79 | **70** | 9 | `STI-103` (3), `STI-312` (3), `STI-626` (3) |",
    "| MK Inti Core STI (28 MK) | 79 | **70** | 9 | `STI-103` (3), `STI-312` (3), `STI-519` (3) |"
)
c024 = c024.replace(
    "`FST-610` (3) dan `STI-626` (3) atau ekuivalen",
    "`FST-610` (3) dan `STI-519` (3) atau ekuivalen"
)
c024 = c024.replace(
    "`STI-417`, `STI-519`, `STI-523`",
    "`STI-417`, `STI-626`, `STI-523`"
)

# Bagian 8: Tabel Entri SIAKAD
c024 = c024.replace(
    "| `STI-634` | 3 | `STI-519` | 3 | E2 | C | **Ya** |",
    "| `STI-634` | 3 | `STI-626` | 3 | E2 | C | **Ya** |"
)

with open(f024, "w", encoding="utf-8") as f:
    f.write(c024)
print("Updated 024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md")


# -----------------------------------------------------------------------------
# 7. UPDATE DOKUMEN LAINNYA
# -----------------------------------------------------------------------------
other_files = [
    "006_DISTRIBUSI_DAN_PANDUAN_MK_PEMINATAN_MBKM.md",
    "009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md",
    "013_REKOMENDASI_SOLUSI_DAN_MITIGASI_KELEMAHAN_KURIKULUM.md",
    "015_SIMULASI_AKSELERASI_KELULUSAN_7_SEMESTER.md",
    "016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md",
    "017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md",
    "018_PANDUAN_RUBRIK_KLASTER_DAN_MODEL_ASESMEN_OBE_DOSEN.md",
    "019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md",
    "023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md",
    "025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md",
    "026_ANALISIS_KRITIS_MK_DIHAPUS_DAN_REKOMENDASI_PENGGANTI.md",
    "028_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_CORE_STI.md",
    "deep_cross_audit.py"
]

for fname in other_files:
    fpath = os.path.join(REVISI_DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    orig = c

    # Ganti prasyarat
    c = c.replace("`STI-519` Deep Learning", "`STI-626` Deep Learning")
    c = c.replace("`STI-519` DL", "`STI-626` DL")
    c = c.replace("STI-519 Deep Learning", "STI-626 Deep Learning")
    c = c.replace("`STI-626` Keamanan Informasi Lanjut", "`STI-519` Keamanan Informasi Lanjut")
    c = c.replace("`STI-626` Security", "`STI-519` Security")
    c = c.replace("`STI-626` Keamanan Lanjut", "`STI-519` Keamanan Lanjut")
    c = c.replace("STI-626 Keamanan Lanjut", "STI-519 Keamanan Lanjut")

    # Khusus di 009D: (STI-413 / STI-519) -> (STI-413 / STI-626)
    c = c.replace("STI-413 / STI-519", "STI-413 / STI-626")

    # Khusus 025 prasyarat STA-10/11
    c = c.replace("`STI-519` (Deep Learning)", "`STI-626` (Deep Learning)")
    c = c.replace("`STI-626` (Keamanan Informasi Lanjut)", "`STI-519` (Keamanan Informasi Lanjut)")

    # Khusus 015 Simulasi Akselerasi
    c = c.replace("STI-519 | Deep Learning", "STI-519 | Keamanan Informasi Lanjut")
    c = c.replace("STI-626 | Keamanan Informasi Lanjut", "STI-626 | Deep Learning")

    if c != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated {fname}")

print("\nSELURUH FILE SELESAI DIPERBARUI!")
