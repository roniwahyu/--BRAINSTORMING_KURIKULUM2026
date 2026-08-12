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

## Key Decisions (already made — DO NOT revisit unless asked)

| ID | Keputusan | Detail |
|---|---|---|
| **VMTS** | Arah prodi = **AI/Smart Systems + Technopreneurship** | Visi 2045: "sistem & teknologi informasi cerdas berbasis kecerdasan artifisial dan technopreneurship" |
| **5 Profil Lulusan** | Intelligent Information System Developer, UX & Digital Service Designer, Smart Technology Integrator, Technopreneur in Smart Information Services, Digital Governance & System Analyst | Disepakati rapat 09 Juni 2026 |
| **R1** | MK 0 SKS (Agama II, Kewirausahaan II) = **kebijakan universitas** | Dipertahankan, tidak diubah |
| **R2** | Rebalancing beban: semua sem ≤20 SKS | Sem 5-6-7 memuat peminatan |
| **R3** | Reposisi: RPL Sem6→Sem4, Metpen Sem7→Sem6, Statistika Sem4→Sem2 | Diterapkan |
| **R4** | 3 Peminatan berbasis BoK APTIKOM SI+TI | P1: Sistem Cerdas & Analitik Data, P2: Infrastruktur & Keamanan Digital, P3: Layanan Digital & Technopreneurship |
| **R5** | MBKM maks 20 SKS di Sem 6-7 | Slot konversi dari peminatan + PKL |
| **R6** | Capstone Design lintas-3-prodi (SISTEKIN + Bisnis Digital + Teknik Informatika) | Menggantikan Skripsi sbg default TA |
| **R7** | MK "pinggiran" jadi **pilihan peminatan** (tidak dihapus) | AR/VR, Game Design, Signal Processing, Semantic Web, Multimedia → pilihan P1/P2/P3 |
| **R8** | Tandai metode PjBL/Case + jenis MK (Teori/Praktik/Praktikum) | Sudah diterapkan di tabel struktur revisi |

---

## Important Correction (anti-hallucination)

**Dokumen internal `analisis_vmts_sistekin.md` dan `analisis_mk_sistekin.md` menyimpulkan VMTS & Kurikulum 2025 "TIDAK LAYAK (47.5%)" dan mendorong pembelokan ke Enterprise Architecture. Kesimpulan itu SALAH secara metodologis** karena:

- Mengukur VMTS dengan tolok ukur karangan sendiri ("STI wajib Enterprise Architecture")
- BUKU_OBE APTIKOM SI v2.0 **tidak mewajibkan** Enterprise Architecture — EA hanya BK16 (kompetensi **pendukung**)
- AI/Analytics/Smart Systems adalah BoK yang sah (BK13, BK18, area Intelligent Systems TI)

**Jangan gunakan** skor 47.5% / 57.1% / 100% dari dokumen-dokumen itu. Arah AI/Smart Systems **dipertahankan**.

---

## Sub-Agent Skills (5 hidden `.agent-skills.md`)

Tersedia 5 file definisi sub-agent di root workspace. Gunakan agent ini untuk mendelegasikan tugas secara paralel:

| # | File | Agent | Peran | Dipicu oleh Langkah |
|---|---|---|---|---|
| 1 | `.strategic-analyst-agent-skills.md` | **Strategic Analyst** | Environmental Scanning, SWOT, VMTS (Latar Belakang) | Langkah 0.1, 0.2 |
| 2 | `.obe-designer-agent-skills.md` | **OBE Designer** | Profil Lulusan, PEO, CPL (Bloom, ABCD) | Langkah 1, 2 |
| 3 | `.curriculum-architect-agent-skills.md` | **Curriculum Architect** | Matriks BoK, MK+SKS, Struktur 8 Semester, MBKM | Langkah 3, 4 |
| 4 | `.qa-evaluator-agent-skills.md` | **QA & Assessment Evaluator** | Rubrik, TA Non-Skripsi, PPEPP | Langkah 5 |
| 5 | `.document-reader-agent-skills.md` | **Document Reader** | Ekstraksi & analisis dokumen (PDF/MD/Excel/Word) | Semua langkah (support) |

### Alur Kolaborasi Sub-Agent

```
Document Reader ──→ Strategic Analyst ──→ OBE Designer ──→ Curriculum Architect ──→ QA Evaluator
 (ekstrak data)      (SWOT + VMTS)       (PEO + CPL)       (BoK + 8 sem + MBKM)      (rubrik + TA)
```

**Setiap agent** memiliki `System Role`, `Core Responsibilities`, `Operational Guidelines`, dan `Constraints` yang spesifik. Baca file `.agent-skills.md` terkait sebelum mendelegasikan tugas.

---

## Working Directory Structure

```
!!BRAINSTORMING_KURIKULUM2026/
├── AGENTS.md                                    ← FILE INI (handoff untuk agent)
├── .strategic-analyst-agent-skills.md           ← 🤖 Strategic Analyst
├── .obe-designer-agent-skills.md                ← 🤖 OBE Designer
├── .curriculum-architect-agent-skills.md        ← 🤖 Curriculum Architect
├── .qa-evaluator-agent-skills.md                ← 🤖 QA & Assessment Evaluator
├── .document-reader-agent-skills.md             ← 🤖 Document Reader
├── 001_...md – 005_...md                        ← 5 Dokumen analisis & revisi (output)
├── workspace-019fd6ce-.../AWAL/                 ← KURIKULUM2025 (kurikulum lama)
│   ├── 001_Summary_Pemetaan_...md               ← Brainstorming APTIKOM (draft AI)
│   ├── 002_Detail_Pemetaan_CPL_...md
│   ├── 003_Rekomendasi_Konsentrasi_...md
│   ├── 004_Kurikulum_Lengkap_STI_...md
│   ├── 005_Komprehensif_Kurikulum_...md
│   ├── 006_Master_Detail_...md
│   ├── analisis_mk_sistekin.md                  ← ⚠️ MENYESATKAN (lihat koreksi)
│   ├── analisis_vmts_sistekin.md                ← ⚠️ MENYESATKAN (lihat koreksi)
│   ├── 17_cpl_tidak_terlalu_banyak.md           ← OK (referensi)
│   ├── asesmen_obe_4_komponen.md                ← OK (referensi)
│   ├── obc_abc_cpl_cpmk.md                      ← OK (referensi ABCD)
│   ├── smart_information_system_...md           ← OK (referensi)
│   ├── Laporan Daftar Kurikulum Prodi Sistekin.pdf ← SIAKAD (sumber resmi)
│   ├── kurikulum_sistekin_text.txt              ← Ekstraksi teks SIAKAD
│   ├── vmts_full_text.txt                       ← Notulensi VMTS 09 Juni 2026
│   └── vmts_text.txt
├── workspace-019fd9ef-.../                      ← BUKU_OBE (3 panduan resmi)
│   ├── OBE_SISTEM_INFORMASI_2.0_APTIKOM_...txt  ← ACUAN UTAMA (SI v2.0, IS2020)
│   ├── 716903001-PANDUAN-KURIKULUM-OBE-...txt   ← Panduan TI 2023 (IT2017)
│   ├── 642302046-...-BUKU-KURIKULUM-SI-...txt   ← SI v1.0 (pelengkap)
│   └── uploads/                                 ← PDF asli
├── STRUKTUR_KURIKULUM2025_SISTEKIN_SAAT_INI.md  ← (1) Potret struktur saat ini
├── LAPORAN_GAP_ANALYSIS_KURIKULUM2025_SISTEKIN.md ← (2) Gap vs 12-bagian OBE
├── INSIGHT_KELEMAHAN_KURIKULUM2025_vs_BUKU_OBE.md ← (3) 10 kelemahan berbukti
├── REKOMENDASI_REVISI_STRUKTUR_KURIKULUM2025_SISTEKIN.md ← (4) 8 rekomendasi
└── STRUKTUR_REVISI_KURIKULUM_SISTEKIN_8_SEMESTER.md ← (5) Struktur final revisi
```

---

## Current State & Next Steps

**Sudah selesai:** Analisis struktur Kurikulum 2025 + Revisi struktur 8 semester (dokumen #1-#5)
**Sedang/selanjutnya:** Menunggu konfirmasi user untuk **Langkah 1: Profil Lulusan & PEO** → **Langkah 2: CPL formal**

**Yang belum dikerjakan (gap OBE):**
- CPL formal 4 kategori (S/KU/P/KK) + referensi IS2020/SKKNI
- PEO terukur 3-5 tahun
- Matriks CPL↔BK↔MK↔CPMK
- CPMK & Sub-CPMK per MK (action verb + Bloom)
- RPS + asesmen berjenjang + rubrik
- Bab MBKM formal + Bab Evaluasi & Tracer Study

---

## Anti-Halusinasi Rules

1. Jika dokumen referensi tidak cukup, **hentikan dan beri tahu** data apa yang kurang — jangan membuat asumsi.
2. Setiap klaim tentang "standar APTIKOM" harus bisa dirujuk ke halaman/kutipan BUKU_OBE.
3. Jangan gunakan skor kuantitatif (47.5%, 57.1%, 100%) dari dokumen `analisis_*` — tidak valid.
4. Arah prodi = **AI/Smart Systems** (VMTS resmi). Enterprise Architecture = **opsional** (BK16 pendukung).
5. **Jangan kerjakan semua langkah sekaligus.** Tunggu konfirmasi tiap langkah.

---

*File ini berfungsi sebagai "memory/soul" untuk semua agent yang bekerja di folder ini. Baca dan pahami sebelum memulai tugas baru.*