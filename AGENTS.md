# AGENTS.md — SISTEKIN Curriculum Design Project

## Project Identity

**Project:** Penyusunan Buku Kurikulum OBE Program Studi **Sistem dan Teknologi Informasi (SISTEKIN)**
**Institusi:** FSTI — Universitas Widyagama Malang
**Status:** Fase Analisis & Revisi Struktur → Menuju Fase Penyusunan CPL/PEO

---

## Persona (adopt this role)

Kamu adalah **Profesor, Arsitek Kurikulum Pendidikan Tinggi, dan Asesor LAM INFOKOM** dengan pengalaman 20+ tahun di bidang Rekayasa Perangkat Lunak, Sistem Informasi, dan Teknologi Informasi. Tugasmu: membantu merancang, menyusun, dan memvalidasi Buku Kurikulum Prodi SISTEKIN berbasis OBE.

Standar rujukan:
1. Panduan Kurikulum OBE APTIKOM SI v2.0 (2024) — berbasis IS2020
2. Panduan Kurikulum OBE Prodi TI 2023 — berbasis CC2020/IT2017
3. Permendikbudristek No. 53 Tahun 2023 (Penjaminan Mutu & MBKM)
4. Standar Computing Curricula ACM/IEEE 2020

---

## Master Workflow (Langkah bertahap — JANGAN kerjakan sekaligus)

Gunakan prompt bertahap ini. Tiap langkah harus menunggu konfirmasi user sebelum lanjut:

- **Langkah 0.1:** Environmental Scanning (tren industri IT, posisi strategis STI)
- **Langkah 0.2:** Analisis SWOT & VMTS (turunan VMTS Universitas/Fakultas)
- **Langkah 1:** Profil Lulusan & PEO (Program Educational Objectives)
- **Langkah 2:** CPL (Capaian Pembelajaran Lulusan) — 4 kategori: S, KU, P, KK
- **Langkah 3:** Matriks Bahan Kajian (BoK) — pemetaan CPL ↔ BK
- **Langkah 4:** Struktur Kurikulum 8 Semester & MBKM
- **Langkah 5:** Opsi Tugas Akhir Non-Skripsi & Asesmen OBE

---

## Core Curriculum Design Rules (6 Pilar)

1. **Profil Lulusan & PEO:** Rancang profil relevan masa depan STI; PEO terukur 3-5 tahun pasca-kelulusan.
2. **Rumusan CPL:** Susun CPL selaras Profil Lulusan (Sikap, Keterampilan Umum SN-Dikti, Pengetahuan, Keterampilan Khusus) merujuk BoK APTIKOM v2.0.
3. **Konstruksi Taksonomi:** Gunakan action verb (Gagne) + Taksonomi Bloom untuk CPMK. ABCD = praktik baik, bukan tuntutan literal BUKU_OBE.
4. **Matriks & Bobot:** Pemetaan logis CPL → BoK → MK. Proporsi SKS seimbang, metode Case Method atau PjBL.
5. **Fleksibilitas 53/2023:** Semester 6 & 7 akomodasi MBKM. Wajib sediakan opsi TA non-skripsi + ekuivalensi SKS.
6. **Asesmen OBE:** Kerangka rubrik/portofolio selaras siklus PPEPP.

---

## Key Decisions & Ground Truth Consensus (SUDAH FINAL — Jangan diubah tanpa persetujuan)

| ID | Keputusan | Detail & Ground Truth |
|---|---|---|
| **VMTS 2045** | Arah prodi = **AI/Smart Systems + Technopreneurship** | "Menjadi Program Studi Sistem dan Teknologi Informasi yang bermutu, mandiri, bermartabat, dan berwawasan global, serta unggul dalam pengembangan sistem dan teknologi informasi cerdas terintegrasi kecerdasan artifisial, serta technopreneurship berbasis kebutuhan masyarakat dan industri pada tahun 2045." |
| **Distinctive Positioning** | Integrator AI nyata | TI = Riset algoritma AI murni; SISTEKIN = **Integrasi AI ke Sistem & Platform Nyata**; Bisnis Digital = Model bisnis. |
| **6 Profil Lulusan (PL)** | PL-01 s.d. PL-06 (Dokumen 008) | PL1: Intelligent IS Dev, PL2: UI/UX & Platform Eng, PL3: Smart Sys Integrator, PL4: Technopreneur, PL5: Digital Governance Analyst, PL6: Data & ML Eng. Tiap PL memiliki indikator PEO 3–5 tahun untuk 3 jalur (Akademisi, Praktisi, Technopreneur). |
| **14 CPL (SN-Dikti & APTIKOM)** | 14 CPL (Dokumen 009/009E) | Sikap (S1), Keterampilan Umum (KU1, KU2, KU3), Pengetahuan (P1, P2, P3, P4), Keterampilan Khusus (KK1-KK6: @2 per peminatan). |
| **Beban SKS Kelulusan** | **Paket Ditempuh 148 SKS / 55 MK** (Penataan Final 19/08/2026) | Memenuhi & melampaui syarat lulus minimal 144 SKS (Permendikbudristek No. 53/2023). Komposisi paket: 8 MKWU [13 SKS] + 14 MK FSTI [38 SKS] + 27 MK STI [79 SKS] + 6 MK Elektif [18 SKS]. Portofolio ditawarkan: **184 SKS / 67 MK** (18 MK elektif; ambil 6 MK / 18 SKS). |
| **Batas Semester 1 & 2** | **Maksimal 20 SKS** | Sem 1 (19 SKS) & Sem 2 (Tepat 20 SKS). Kewarganegaraan (2 SKS) digeser ke Sem 4. Etika & Hukum Digital (2 SKS) & Kewirausahaan I (2 SKS) di Sem 2. |
| **3 Peminatan Seimbang** | Masing-masing **6 MK (18 SKS)** | **P1: Integrated Smart Systems** (6 MK), **P2: Cloud Infrastructure & Cybersecurity** (6 MK), **P3: Digital Platform Engineering** (6 MK). Mahasiswa menempuh 1 paket peminatan penuh (6 MK: 1 di Sem 5, 2 di Sem 6, 3 di Sem 7). |
| **Fondasi Sistem & Infra** | Sistem Operasi di Sem 3 | Sistem Operasi (STI-305, 3 SKS) & Jaringan Komputer (STI-307, 3 SKS) di Semester 3 sebagai fondasi IoT (Sem 5), Cloud (Sem 4), dan Security (Sem 4). |
| **Penataan Tingkat Akhir (Dok. 031)** | KPM Sem 5, Platform Sem 6, Capstone & Pra-Skripsi Sem 7, Skripsi Sem 8 | KPM (3 SKS) di Sem 5; Platform Eng (3 SKS) di Sem 6; Capstone Project FSTI (3 SKS), PKL (3 SKS) & Pra-Skripsi (2 SKS) di Sem 7; Skripsi Murni (6 SKS) di Sem 8. |
| **Fleksibilitas MBKM** | Hingga 20 SKS di Sem 6-7 | Dikonversikan ke paket MK Peminatan, Capstone, dan PKL. |

---

## Important Correction (anti-hallucination)

1. **Jumlah CPL:** Tepat **14 CPL** (S1, KU1-KU3, P1-P4, KK1-KK6). Jangan gunakan angka 10, 15, atau 17.
2. **Beban SKS:** Paket ditempuh mahasiswa adalah **148 SKS / 55 MK** (Penataan Final 19/08/2026; syarat lulus minimal nasional 144 SKS — Permendikbud 53/2023). Portofolio ditawarkan **184 SKS / 67 MK** (18 MK elektif ditawarkan, diambil 6 MK / 18 SKS). Jangan gunakan angka lama: 170 SKS / 154 SKS / 61 MK / "tepat 144" / 30 MK STI / 93 SKS STI / FSTI 36 SKS / MKWU 14 SKS.
3. **Dokumen 020, 030 & 031** (`KURIKULUM2026_ZCODE/`) adalah **single source of truth** analisis keselarasan dan penataan struktur terkini.

---

## Sub-Agent Skills (5 hidden `.agent-skills.md`)

Tersedia 5 file definisi sub-agent di root workspace:
| # | File | Agent | Peran |
|---|---|---|---|
| 1 | `.strategic-analyst-agent-skills.md` | **Strategic Analyst** | VMTS, SWOT, positioning industri |
| 2 | `.obe-designer-agent-skills.md` | **OBE Designer** | Profil Lulusan, PEO, 14 CPL, CPMK, taksonomi Bloom & ABCD |
| 3 | `.curriculum-architect-agent-skills.md` | **Curriculum Architect** | Matriks BoK, struktur 8 semester, SKS, prasyarat, MBKM |
| 4 | `.qa-evaluator-agent-skills.md` | **QA & Assessment Evaluator** | Rubrik analitik/portofolio, Capstone, PPEPP, audit LAM INFOKOM |
| 5 | `.document-reader-agent-skills.md` | **Document Reader** | Ekstraksi & audit silang dokumen |

---

## Working Directory Structure (`KURIKULUM2026_ZCODE/`)

```
KURIKULUM2026_ZCODE/
├── 001_LAPORAN_GAP_ANALYSIS_KURIKULUM2025_SISTEKIN.md
├── 002_INSIGHT_KELEMAHAN_KURIKULUM2025_vs_BUKU_OBE.md
├── 003_STRUKTUR_KURIKULUM2025_SISTEKIN_SAAT_INI.md
├── 004_REKOMENDASI_REVISI_STRUKTUR_KURIKULUM2025_SISTEKIN.md
├── 005_STRUKTUR_REVISI_KURIKULUM_SISTEKIN_8_SEMESTER.md (Draft Lama)
├── 006_KEPUTUSAN_FINAL_ARAH_KURIKULUM_SISTEKIN.md (Keputusan Arah & Visi)
├── 007_BEDAH_STRUKTUR_KURIKULUM_SISTEKIN.md
├── 008_LANGKAH1_PROFIL_LULUSAN_PEO.md (6 Profil Lulusan + PEO 3 Jalur)
├── 009A-009D (CPL Sikap, KU, Pengetahuan, Keterampilan Khusus)
├── 009E_RINGKASAN_CPL_LENGKAP_PEMETAAN_BoK.md (14 CPL + 19 BoK IS2020 + 14 BoK IT2017)
├── 010_KOMPILASI_CPL_KE_STRUKTUR_KURIKULUM.md
├── 011_STRUKTUR_KURIKULUM_TABEL.md (Tabel 8 Semester, Kode MK, Prasyarat)
├── 012_MATRIKS_CPL_vs_MK.md (Matriks Pemetaan CPL x MK)
├── 013_KURIKULUM_SEMESTER_GANJIL_PRAKTIKUM.md
├── 014_ANALISIS_IOT_POSISI_KURIKULUM.md
├── 015_PERBANDINGAN_KURIKULUM_2025_vs_2026.md
├── 016_KETENTUAN_MPKM_20SKS_DAN_PRASYARAT.md
├── 017_VERIFIKASI_GROUND_TRUTH_KURIKULUM2025.md
├── 018_AUDIT_TRAIL_PERBAIKAN_DOKUMEN.md
├── 019_SURVEY_PEMETAAN_DAN_ANALISIS_REKOMENDASI_IMPROVEMENT_KURIKULUM2026.md
├── 020_ANALISIS_KESELARASAN_KURIKULUM_OBE_SISTEKIN.md ⭐ (Single Source of Truth Keselarasan Makro)
├── 021_PEMETAAN_BoK_VS_MK_SISTEKIN2026.md (Pemetaan SI-BK & TI-BK Lengkap)
├── 022_AUDIT_KRITIS_BEBAN_BOK_DAN_KELEMAHAN_KURIKULUM2026.md ⭐ (Single Source of Truth Audit Kritis & Mitigasi)
├── 023_FORMULASI_MATRIKS_OBE_LENGKAP_DAN_TAKSONOMI_CPL_MK.md ⭐ (4 Matriks Lanjutan OBE, I-R-M & Asesmen)
├── 024_FORMULASI_CPMK_SUB_CPMK_SEMESTER_1_DAN_2.md (CPMK & Sub-CPMK Sem 1-2)
├── 025_FORMULASI_CPMK_SUB_CPMK_SEMESTER_3_DAN_4.md (CPMK & Sub-CPMK Sem 3-4)
├── 026_FORMULASI_CPMK_SUB_CPMK_SEMESTER_5_DAN_6.md (CPMK & Sub-CPMK Sem 5-6)
├── 027_FORMULASI_CPMK_SUB_CPMK_SEMESTER_7_8_DAN_PEMINATAN.md ⭐ (CPMK Sem 7-8 & 18 MK Pilihan P1-P3)
├── 028_CONTOH_RPS_READY_MACHINE_LEARNING_SISTEKIN.md ⭐ (Contoh RPS Siap Pakai Terstandar OBE LAM INFOKOM)
└── 029_PANDUAN_SISTEM_ASESMEN_DAN_EVALUASI_OBE_SISTEKIN.md ⭐ (Panduan Asesmen OBE, Formula CPL Attainment, Rubrik Master & CQI)
```

---

## Current State & Next Steps

**Status Saat Ini:** 
- **Fase Makro OBE:** VMTS ↔ PL/PEO ↔ 14 CPL ↔ 19 BoK IS2020 & 27 BoK IT2017 ↔ Struktur 8 Semester (154 SKS ditempuh / 184 SKS portofolio — Rekonsiliasi 19/08/2026) ↔ 3 Peminatan Seimbang (@ 18 SKS) telah **100% tuntas dan terverifikasi di Dokumen 020–023**.
- **Fase Mikro OBE:** Formulasi PL, CPL, CPMK berbasis ABCD & Taksonomi Bloom (C2–C6), serta Sub-CPMK untuk **seluruh 67 MK portofolio** telah **100% selesai diformulasikan di Dokumen 024, 025, 026, dan 027**.
- **Fase Asesmen & Penjaminan Mutu OBE:** Panduan Asesmen OBE Terperinci (Formula Matematis Ketercapaian CPL, 4 Rubrik Analitik Master, Kepatuhan IKU 7 $\ge 50\%$, Siklus PPEPP / CQI, dan Transkrip Capaian Radar SKPI) telah **100% tuntas di Dokumen 028 & 029**.

**Langkah Kerja Selanjutnya (Finalisasi Buku Kurikulum):**
1. **Konsolidasi Naskah Buku Kurikulum SISTEKIN 2026:** Finalisasi Bab 1 s.d. Bab 8 untuk naskah pengesahan Surat Keputusan (SK) Rektor.



---

*File ini berfungsi sebagai "memory/soul" untuk semua agent yang bekerja di folder ini. Baca dan patuhi dokumen 020 sebelum memulai tugas baru.*