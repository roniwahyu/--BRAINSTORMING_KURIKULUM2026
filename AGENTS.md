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
| **3 PEO & 4 Profil Lulusan (PL)** | 3 PEO & 4 PL Role-Based (Dokumen 002) | **PEO-1** (Professional Practice & Systems Integration), **PEO-2** (Digital Innovation & Technopreneurship), **PEO-3** (Advanced Study, Research & Lifelong Learning). **PL-1** (Intelligent IS Dev & AI Eng), **PL-2** (Cloud Infra, Cyber & Smart Sys), **PL-3** (UI/UX & Digital Platform Eng), **PL-4** (Digital Technopreneur & IT Product Innovator). |
| **14 CPL (SN-Dikti & APTIKOM)** | 14 CPL Terstandar (Dokumen 003) | Sikap (S1), Keterampilan Umum (KU1, KU2, KU3), Pengetahuan (P1, P2, P3, P4), Keterampilan Khusus (KK1-KK6: @2 per peminatan). Dilengkapi genealogi sumber IS2020 CPL-P01..P17 & CPL-K01..K17 serta IT2017 KK1..KK3. |
| **Pondasi Arsitektur & Logika** | **STI-103 & STI-201 Terpadu** | **`STI-103 Arsitektur dan Organisasi Sistem Teknologi Informasi`** (3 SKS, Sem 1, BK-IS03/BK-IT05) menggantikan Logika Informatika lama; **`STI-201 Matematika Diskrit dan Logika`** (3 SKS, Sem 2, BK-IS10) mengintegrasikan logika proposisi & aljabar boolean bebas redundansi. |
| **Beban SKS Kelulusan** | **Paket Ditempuh 146 SKS / 55 MK** (Penataan Final) | Memenuhi & melampaui syarat lulus minimal 144 SKS (Permendikbudristek No. 53/2023). Komposisi paket: 8 MKWU [13 SKS] + 13 MK FSTI [36 SKS] + 28 MK Core STI [79 SKS] + 6 MK Elektif [18 SKS]. Portofolio ditawarkan: **182 SKS / 67 MK** (18 MK elektif; ambil 6 MK / 18 SKS). |
| **Batas Semester 1 & 2** | **Maksimal 20 SKS** | Sem 1 (19 SKS) & Sem 2 (Tepat 20 SKS). Sem 4 (21 SKS, Dasar Keamanan Informasi 2 SKS). Sem 6 (19 SKS, Smart City & Pem. Digital 2 SKS). Kewarganegaraan (2 SKS) di Sem 4. Etika & Hukum Digital (2 SKS) & Kewirausahaan I (2 SKS) di Sem 2. |
| **3 Peminatan Seimbang** | Masing-masing **6 MK (18 SKS)** | **P1: Integrated Smart Systems** (6 MK: STA-01..06), **P2: Cloud Infrastructure & Cybersecurity** (6 MK: STB-01..06), **P3: Digital Platform Engineering** (6 MK: STC-01..06). Mahasiswa menempuh 1 paket peminatan penuh (6 MK: 1 di Sem 5, 2 di Sem 6, 3 di Sem 7). |
| **Skema Asesmen Terstruktur** | **4x Titik Evaluasi Baku (Total = 100%)** | **Tugas 1** di Pekan 4 (20%), **UTS** di Pekan 8 (25% Praktikum / 30% Teori), **Tugas 2** di Pekan 12 (20% Teori / 25% Praktikum), dan **UAS** di Pekan 16 (30%). Memetakan secara langsung 1-to-1 ke 4 CPMK dan memenuhi IKU 7 $\ge 50\%$. |
| **Fondasi Sistem & Infra** | Sistem Operasi di Sem 3 | Sistem Operasi (STI-305, 3 SKS) & Jaringan Komputer (STI-307, 3 SKS) di Semester 3 sebagai fondasi IoT (Sem 5), Cloud (Sem 4), dan Security (Sem 4, STI-405 2 SKS). |
| **Penataan Tingkat Akhir** | KPM & KWU II Sem 5, Platform & Smart City Sem 6, Capstone & Pra-Skripsi Sem 7, Skripsi Sem 8 | KPM (3 SKS) & Kewirausahaan II (0 SKS) di Sem 5; Platform Eng (3 SKS) & Smart City (2 SKS) di Sem 6; Capstone Project FSTI (3 SKS), PKL (3 SKS) & Pra-Skripsi (2 SKS) di Sem 7; Skripsi Murni / Opsi Non-Skripsi (6 SKS) di Sem 8. |
| **Fleksibilitas MBKM** | Hingga 20 SKS di Sem 6-7 | Dikonversikan ke paket MK Peminatan, Capstone, dan PKL. |

---

## Important Correction (anti-hallucination)

1. **Jumlah CPL:** Tepat **14 CPL** (S1, KU1-KU3, P1-P4, KK1-KK6). Jangan gunakan angka 10, 15, atau 17.
2. **Profil Lulusan & PEO:** Tepat **4 Profil Lulusan (PL-1 s.d. PL-4)** dan **3 PEO (PEO-1 s.d. PEO-3)**.
3. **Beban SKS:** Paket ditempuh mahasiswa adalah **146 SKS / 55 MK** (syarat lulus minimal nasional 144 SKS — Permendikbud 53/2023). Portofolio ditawarkan **182 SKS / 67 MK** (18 MK elektif ditawarkan, diambil 6 MK / 18 SKS).
4. **Skema Asesmen:** Tepat **4x Titik Asesmen Baku** per mata kuliah (Tugas 1 [20%], UTS [25-30%], Tugas 2 [20-25%], UAS [30%]).
5. **Folder `KURIKULUM2026_REVISI/`** adalah **single source of truth definitif** untuk penyusunan Naskah Buku Kurikulum KPT-OBE SISTEKIN 2026.
6. **Ground Truth Kurikulum 2025 (WAJIB):** Seluruh atribut MK Kurikulum 2025 — nomor urut, kode, nama, SKS, semester, nilai minimal — **HARUS** bersumber langsung dari `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` (Laporan resmi SIAKAD, dicetak 05 Agustus 2026). Ground truth: **56 MK / 146 SKS**, sebaran **18-18-20-20-21-21-20-8**, **seluruh MK berstatus Wajib** (K2025 tidak punya MK pilihan/peminatan), kolom Paket = `Tidak`, nilai minimal = `C`. Jangan pernah menurunkan data K2025 dari ingatan, dokumen antara, atau notulensi rapat. Validasi: `python _tools/verify_k2025_ground_truth.py`.
7. **Kolisi kode K2025 ↔ K2026:** 11 kode dipakai di kedua kurikulum. Tiga berisiko tinggi: `STI-102` (K2025 Algoritma & Pemrograman → K2026 **Kalkulus**), `STI-103` (K2025 Logika Informatika → K2026 **Arsitektur & Organisasi STI**), `STI-101` (SKS berubah 3 → 2). Selalu sebutkan tahun kurikulum saat merujuk ketiga kode ini.

---

## Active Working Directory Structure (`KURIKULUM2026_REVISI/`)

```
KURIKULUM2026_REVISI/
├── 001_ANALISIS_VMTS_DAN_POSITIONING_STRATEGIS_SISTEKIN.md (VMTS 2045, SWOT & Positioning)
├── 002_FORMULASI_3_PEO_DAN_4_PROFIL_LULUSAN_SISTEKIN.md (3 PEO & 4 PL Role-Based + Indikator)
├── 003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md (14 CPL, Genealogi Sumber, 19 BoK IS & 14 BoK IT)
├── 004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md (Matriks Tabel Makro OBE VMTS-PEO-PL-CPL-MK-IRM)
├── 005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md (Struktur 8 Semester 146 SKS / 55 MK)
├── 006_DISTRIBUSI_DAN_PANDUAN_MK_PEMINATAN_MBKM.md (3 Peminatan @ 18 SKS & Panduan Konversi MBKM)
├── 007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md ⭐ (Silabus 3-Tabel Lengkap 67 MK Portofolio, 4x Asesmen)
├── 008_SISTEM_ASESMEN_OBE_FORMULA_CPL_DAN_RUBRIK_MASTER.md (Formula CPL Attainment, 4x Asesmen, 4 Rubrik Master, CQI)
├── 009A_CPL_SIKAP_SISTEKIN.md (Detail CPL S1, Indikator Kinerja, 4 PL & SN-Dikti)
├── 009B_CPL_KETERAMPILAN_UMUM_SISTEKIN.md (Detail CPL KU1-3, Indikator Kinerja & SN-Dikti)
├── 009C_CPL_PENGETAHUAN_SISTEKIN.md (Detail CPL P1-4, Indikator Kinerja, IS2020 & IT2017)
├── 009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md (Detail CPL KK1-6, 19 BoK IS2020 & 14 BoK IT2017)
├── 009E_RINGKASAN_CPL_LENGKAP_PEMETAAN_BoK.md ⭐ (Matriks Kompilasi 14 CPL, BoK, PL, Peminatan, VMTS)
├── 009_PEDOMAN_CAPSTONE_PROJECT_DAN_TUGAS_AKHIR_NON_SKRIPSI.md (Pedoman Capstone FSTI & 4 Opsi TA Non-Skripsi)
├── 010_INSTRUMEN_TRACER_STUDY_DAN_EVALUASI_PEO_PPEPP.md (Instrumen Tracer Study & Evaluasi PEO Siklus PPEPP)
├── 011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md ⭐ (14 Sheet Matriks Terpadu, Exportable ke Excel/Word/PDF)
├── 011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.xlsx (Output Workbook 15 Tab Berformat Rapi)
├── 012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md (Analisis Jalur Pondasi & Diagram Tree Prasyarat)
├── 013_REKOMENDASI_SOLUSI_DAN_MITIGASI_KELEMAHAN_KURIKULUM.md (6 Strategi Solusi & Mitigasi Beban)
├── 014_ANALISIS_KRITIS_PEMANGKASAN_SKS_TEORI_SEM4_SEM5.md (Rasionalisasi SKS Teori & Batas Kewenangan MK FSTI)
├── 015_SIMULASI_AKSELERASI_KELULUSAN_7_SEMESTER.md (Panduan & Simulasi Studi Akselerasi 3.5 Tahun / 146 SKS)
├── 016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md (Audit BoK APTIKOM & 5-Stage Pipeline AI)
├── 017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md ⭐ (Audit Forensik Zero Redundancy & Zero Gap 5 Domain)
├── 018_PANDUAN_RUBRIK_KLASTER_DAN_MODEL_ASESMEN_OBE_DOSEN.md ⭐ (Panduan Master 4 Klaster Rubrik & Model Asesmen Dosen)
├── 024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md ⭐ (Ekivalensi 56 MK K2025 → K2026, 5 Kategori E1-E5, 4 Klaster Peleburan, Tabel Entri SIAKAD)
├── 024_RINGKAS_EKIVALENSI_UNTUK_AWAM.xlsx ⭐ (8 Sheet Berwarna untuk Pembaca Non-Teknis: legenda status, 2 arah konversi, neraca per semester)
├── 024_RINGKAS_EKIVALENSI_UNTUK_AWAM.docx ⭐ (9 Tabel Lanskap Siap Cetak & Edar untuk Rapat Prodi / Sosialisasi Mahasiswa)
├── BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md ⭐ (Naskah Utuh Lengkap Buku Kurikulum Bab 1-8 + Silabus)
├── GENERATE_EXCEL_011.bat (Trigger Batch Sekali Klik untuk Re-generate Excel)
├── GENERATE_HTML.bat (Trigger Batch Sekali Klik untuk Re-generate Seluruh File HTML & Portal)
├── START_LIVE_WATCHER.bat (Trigger Background Watcher untuk Auto-update Excel saat file .md disimpan)
├── index.html (Portal Navigasi Interaktif Seluruh Dokumen Kurikulum 2026)
└── _tools/
    ├── convert_md_to_html.py (Engine Konversi Markdown ke HTML Modern & Interaktif)
    ├── export_all_to_excel.py (Engine Konversi Multi-Sheet Python)
    ├── export_024_awam.py ⭐ (Eksporter Dokumen 024 ke XLSX 8-Sheet & DOCX 9-Tabel untuk Pembaca Non-Teknis)
    ├── verify_k2025_ground_truth.py ⭐ (Verifikator 11 Kelompok Uji / 17 Butir: Rujukan K2025 vs PDF Laporan SIAKAD)
    ├── verify_zero_discrepancy.py (Engine Verifikasi Sinkronisasi 24 File)
    └── watch_and_auto_export.py (Engine Live Watcher)
```

### Sumber Ground Truth Kurikulum 2025 (`KURIKULUM2025/`)

```
KURIKULUM2025/
├── Laporan Daftar Kurikulum Prodi Sistekin.pdf ⭐⭐ (GROUND TRUTH TUNGGAL — Laporan SIAKAD,
│      56 MK / 146 SKS, sebaran 18-18-20-20-21-21-20-8, seluruhnya Wajib, nilai min C)
├── Implementasi_MODUL_OBE_SISTEKIN2025.pdf (Modul OBE K2025 — sumber CPL/CPMK lama)
├── Implementasi_Modul_OBE_S1_SISTEKIN_UWG_2025.xlsx (Workbook OBE K2025)
├── Notulensi Rapat VMTS & Kurikulum Program Studi SIST 090626.pdf (Notulensi — BUKAN ground truth MK)
├── [IA - UPPS] ... INSTRUMEN PEMENUHAN SYARAT MINIMUM AKREDITASI ... .pdf (Instrumen akreditasi)
└── obe_pdf_extract/ (Hasil ekstraksi Modul OBE 2025: 56/56 kode cocok, 0 konflik SKS)
```

---

## Current State & Next Steps

**Status Saat Ini:** 
- **Fase Makro OBE:** VMTS ↔ 3 PEO ↔ 4 PL ↔ 14 CPL ↔ 19 BoK IS2020 & 14/27 BoK IT2017 ↔ Struktur 8 Semester (146 SKS paket ditempuh / 182 SKS portofolio ditawarkan) ↔ 3 Peminatan Seimbang (@ 18 SKS) telah **100% tuntas dan terverifikasi di Dokumen 001–006**.
- **Fase Mikro OBE & Silabus 3-Tabel:** Formulasi Identitas MK, CPMK berbasis ABCD & Taksonomi Bloom (C2–C6), serta Matriks 16 Pertemuan dengan Skema 4x Asesmen (Tugas 1 [20%], UTS [25-30%], Tugas 2 [20-25%], UAS [30%]) untuk **seluruh 67 MK portofolio** telah **100% tuntas di Dokumen 007 (361 KB)**.
- **Fase Asesmen, Tugas Akhir, & Penjaminan Mutu:** Sistem Asesmen OBE (IKU 7 $\ge 50\%$, Formula Ketercapaian CPL, 4 Rubrik Analitik Master), Pedoman Capstone & 4 Opsi TA Non-Skripsi, serta Instrumen Tracer Study PEO telah **100% tuntas di Dokumen 008, 009, dan 010**.
- **Fase Audit Kritis & Akselerasi:** Kunci konsensus `STI-103 Arsitektur & Organisasi Sistem TI` dan `STI-201 Matematika Diskrit dan Logika`, Solusi Mitigasi (013), Simulasi Fast-Track 7 Semester (015), Pipeline AI (016), dan Audit Forensik Zero Redundancy & Zero Gap (017) telah **100% tuntas dan terverifikasi di Dokumen 012–017**.
- **Fase Naskah Buku Kurikulum Final:** Naskah utuh komprehensif Bab 1 s.d. Bab 8 (`BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md`, 445 KB) telah selesai dan 100% selaras dengan seluruh dokumen pendukung.
- **Fase Ekivalensi & Transisi Kurikulum:** Matriks ekivalensi 56 MK Kurikulum 2025 ke Kurikulum 2026 telah **100% tuntas di Dokumen 024**, mencakup 5 kategori penyetaraan (E1 Penuh 34 MK, E2 Bersyarat 11 MK, E3 Gabungan 8 MK, E4 Pecah 1 MK, E5 Tanpa Padanan 2 MK), 4 klaster peleburan MK (G-1 s.d. G-4, efisiensi −7 SKS), peringatan kolisi kode `STI-102`/`STI-103`, 18 MK baru K2026 (5 MK wajib / 14 SKS + 13 MK elektif), simulasi pengakuan SKS per jalur peminatan (P1/P2 = 120 SKS diakui, P3 = 117 SKS), serta tabel siap impor `mk_ekivalensi` SIAKAD (57 baris konversi).
- **Fase Verifikasi Ground Truth K2025:** Dokumen 024 telah **diaudit terprogram terhadap PDF Laporan SIAKAD** (`_tools/verify_k2025_ground_truth.py`, 11 kelompok uji) dan **LULUS 17 butir verifikasi**: 56 MK / 146 SKS, sebaran 8 semester, nomor urut & nama & SKS tiap baris identik PDF (0 ketidakcocokan), 0 baris salah seksi semester, Zero Orphan, 0 kode fiktif, neraca E1–E5 = 146 SKS, 49 kode target K2026 valid, simulasi SKS 120/120/117 terkonfirmasi, semester MK elektif presisi, neraca rekognisi arah balik 114 diakui / 14 defisit SKS, portofolio 67 MK = 49 direkognisi + 18 baru, serta 2/2 kasus klaim ganda tuntas.
- **Fase Penyamaan Versi & Rekognisi Dua Arah:** Dokumen 024 kini memuat **Bagian 3A Matriks Rekognisi Arah Balik (K2026 ← K2025)** — 8 tabel per semester yang menyatakan untuk setiap MK Kurikulum 2026: SKS, kategori ekivalensi, MK asal K2025, dan tindakan akademik (alih nilai langsung / uji penyetaraan / wajib tempuh). Neraca paket wajib: **114 dari 128 SKS diakui (89,1%), defisit 14 SKS pada 5 MK baru**. Semester 4, 5, dan 8 terekognisi 100%; titik kritis penyisipan ada di Sem 1 (`STI-103`) dan Sem 3 (`STI-307`) karena keduanya prasyarat berantai. Ditambahkan pula peta navigasi dokumen per peran pengguna, aturan klaim ganda berjenjang 2 tingkat (menuntaskan ambiguitas `STI-422` vs `STI-742` yang keduanya E2), dan Bagian 9.3 konsistensi dua arah matriks.
- **Fase Diseminasi untuk Pembaca Non-Teknis:** Dokumen 024 diterbitkan ulang dalam format ramah-awam via `_tools/export_024_awam.py`, menerjemahkan kode kategori E1–E5/B menjadi kalimat tindakan lugas (Diakui penuh / Diakui bersyarat / Digabung / Dipecah / Tidak ada padanan / Kalah prioritas / Wajib ditempuh) dengan pewarnaan konsisten. Keluaran: **XLSX 8 sheet** (Baca Ini Dulu, 2 arah konversi, neraca per semester, MK wajib baru, MK peminatan, klaster peleburan, sumber data — berheader beku & berfilter) dan **DOCX 9 tabel lanskap** siap cetak untuk rapat prodi dan sosialisasi mahasiswa. Kedua berkas dibangkitkan langsung dari PDF SIAKAD + Dok 005/007/024, bukan disalin manual.

---

*File ini berfungsi sebagai "memory/soul" untuk semua agent yang bekerja di folder ini.*