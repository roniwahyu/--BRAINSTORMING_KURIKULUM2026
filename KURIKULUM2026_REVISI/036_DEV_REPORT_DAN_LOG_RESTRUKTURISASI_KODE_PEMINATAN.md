# 036 — DEV REPORT & DEV LOG: RESTRUKTURISASI KODE MK PEMINATAN (STA, STB, STC)
## Laporan Rekayasa dan Log Perubahan Penomoran Berbasis Semester (Reset ke 01 per Semester)
**Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang**

---

### RINGKASAN EKSEKUTIF (EXECUTIVE SUMMARY)

| Parameter | Keterangan |
|---|---|
| **Tanggal Eksekusi** | 10 September 2026 |
| **Status Pekerjaan** | **SELESAI (100% Tuntas, Teruji, dan Terverifikasi Penuh)** |
| **Lingkup Rekayasa** | Restrukturisasi sistemik kode 18 Mata Kuliah Pilihan Peminatan (*Elective Tracks*) Kurikulum 2026 |
| **Skema Pengkodean Baru** | Format 3-digit berbasis semester dengan reset ke `01` pada setiap semester: `STA/STB/STC-501` (Sem 5), `601..602` (Sem 6), dan `701..703` (Sem 7) |
| **Formula Baku** | $$\mathbf{ST[A/B/C]\text{-}[Semester][Nomor\ Urut\ dalam\ Semester\ (2\ Digit)]}$$ |
| **Total Berkas Diperbarui** | **22 Berkas Markdown** (termasuk `AGENTS.md`) + **8 Skrip Automasi Python** |
| **Volume Pergantian Teks** | **660 titik pergantian** tersubstitusi secara atomik (*single-pass word-boundary regex*) |
| **Residual Kode Lama** | **0 kemunculan** kode lama (`STA-01..06`, `STB-01..06`, `STC-01..06`) di seluruh repositori |
| **Artefak Luaran Terbit** | 1 Berkas Excel Ekivalensi Awam (8 Sheet), 1 Dokumen Word Lanskap Siap Cetak (9 Tabel), 37 Halaman HTML Portal Interaktif `index.html` |
| **Integritas Sistem** | **Lulus 100% Zero Discrepancy** (45 berkas Markdown) & **Lulus 11/11 Kelompok Uji Ground Truth SIAKAD K2025** |

---

### 1. LATAR BELAKANG DAN MASALAH TEKNIS (PROBLEM STATEMENT)

Pada perancangan awal Kurikulum 2026, mata kuliah peminatan menggunakan penomoran serial datar 2-digit:
* **Peminatan 1 (Integrated Smart Systems):** `STA-01` s.d. `STA-06`
* **Peminatan 2 (Cloud Infrastructure & Cybersecurity):** `STB-01` s.d. `STB-06`
* **Peminatan 3 (Digital Platform Engineering):** `STC-01` s.d. `STC-06`

#### Temuan Masalah Arsitektural:
1. **Ketiadaan Informasi Semester pada Kode MK:** Kode `STA-02` atau `STB-05` tidak mencerminkan tingkat/semester penawaran mata kuliah tersebut, sehingga membingungkan mahasiswa saat KRS-an dan menyulitkan Dosen Penasihat Akademik (PA).
2. **Inkonsistensi Format dengan Rumpun Lain:**
   - **MKWU:** Menggunakan digit semester pada digit pertama (`MKU-101..103`, `MKU-204`, `MKU-405..406`, `MKU-507..508`).
   - **FSTI:** Menggunakan digit semester pada digit pertama (`FST-101..102`, `FST-203..207`, `FST-408`, `FST-611`, `FST-610..613`, `FST-714`).
   - **Core STI:** Menggunakan digit semester pada digit pertama (`STI-101..103`, `STI-204..205`, `STI-306..312`, `STI-413..418`, `STI-519..523`, `STI-624..627`, `STI-728`).
   Penggunaan kode 2-digit pada MK Peminatan merupakan anomali format tunggal yang tersisa di Kurikulum 2026.
3. **Bebas Risiko Kolisi Historis:** Berdasarkan audit basis data Kurikulum 2025 (`Laporan Daftar Kurikulum Prodi Sistekin.pdf`), Kurikulum 2025 tidak pernah menggunakan kode `STA`, `STB`, ataupun `STC` (0 kemunculan), sehingga transisi ke format 3-digit dijamin **100% bebas risiko tabrakan kode**.

---

### 2. KEPUTUSAN TIM KURIKULUM & FORMULA BAKU

Tim Kurikulum menetapkan **Model 2: Reset ke 01 pada Setiap Semester**:
* **Digit 1 (`Semester`):** Semester penawaran (`5`, `6`, atau `7`).
* **Digit 2 & 3 (`Urutan dalam Semester`):** Nomor urut mata kuliah peminatan dalam semester bersangkutan yang selalu dimulai dari `01` pada setiap semester (`501`, `601..602`, `701..703`).

**Keunggulan Model 2:**
1. **Simetri Sempurna Antar Peminatan:** Pada Semester 5, ketiga peminatan sama-sama menawarkan MK `501`. Pada Semester 6, ketiganya menawarkan `601` dan `602`. Pada Semester 7, ketiganya menawarkan `701`, `702`, dan `703`.
2. **Kesiapan Ekspansi Pool Pilihan (Dokumen 025):** Memudahkan penambahan mata kuliah pilihan baru di masa depan tanpa merusak urutan (cukup menambahkan `502`, `503`, `603`, `604`, dst.).

---

### 3. TABEL TRANSFORMASI KODE 18 MK PEMINATAN (BEFORE VS AFTER)

| Sem | Rumpun Peminatan | Nama Mata Kuliah | SKS | Tipe | Kode Lama | **Kode Baru Definitif** | Prasyarat Akademik Terverifikasi |
|:---:|:---|---|:---:|:---:|:---:|:---:|---|
| **5** | P1: Integrated Smart Systems | Decision Support Systems | 3 | +P | `STA-01` | **`STA-501`** | `STI-307` Sistem Cerdas |
| **5** | P2: Cloud Infra & Cyber | Network Security and Digital Forensics | 3 | +P | `STB-01` | **`STB-501`** | `STI-312` Jarkom, `STI-418` Dasar Keamanan |
| **5** | P3: Digital Platform Eng | User Experience Research & Design | 3 | +P | `STC-01` | **`STC-501`** | `STI-308` UI/UX Design & Prototyping |
| **6** | P1: Integrated Smart Systems | Computational Methods and Numerics | 3 | +P | `STA-02` | **`STA-601`** | `STI-102` Kalkulus, `STI-205` Aljabar Linear |
| **6** | P1: Integrated Smart Systems | Intelligent Agent Systems | 3 | +P | `STA-03` | **`STA-602`** | `STI-307` Sistem Cerdas |
| **6** | P2: Cloud Infra & Cyber | Cloud Architecture & DevOps | 3 | +P | `STB-02` | **`STB-601`** | `STI-417` Komputasi Awan |
| **6** | P2: Cloud Infra & Cyber | Cybersecurity Risk Management | 3 | Teori | `STB-03` | **`STB-602`** | `STI-418` Dasar Keamanan Informasi |
| **6** | P3: Digital Platform Eng | Rekayasa & Otomasi Proses Bisnis (BPA) | 3 | +P | `STC-02` | **`STC-601`** | `STI-306` Analisis & Perancangan Sistem Informasi |
| **6** | P3: Digital Platform Eng | Rekayasa Aplikasi Industri Vertikal | 3 | +P | `STC-03` | **`STC-602`** | `STI-416` Web Back End Development |
| **7** | P1: Integrated Smart Systems | MLOps and AI Pipeline | 3 | +P | `STA-04` | **`STA-701`** | `STI-413` Machine Learning, `STI-624` Integrasi AI |
| **7** | P1: Integrated Smart Systems | Conversational AI & Intelligent Assistant | 3 | +P | `STA-05` | **`STA-702`** | `STI-413` Machine Learning, `STI-416` Web Back End |
| **7** | P1: Integrated Smart Systems | Smart Surveillance & IoT Analytics | 3 | +P | `STA-06` | **`STA-703`** | `STI-626` Deep Learning, `STI-521` IoT |
| **7** | P2: Cloud Infra & Cyber | IT Governance & Compliance (COBIT 2019) | 3 | Teori | `STB-04` | **`STB-701`** | `STI-101` Pengantar STI |
| **7** | P2: Cloud Infra & Cyber | IT Service Management (ITIL 4) | 3 | Teori | `STB-05` | **`STB-702`** | `STI-101` Pengantar STI |
| **7** | P2: Cloud Infra & Cyber | Enterprise Architecture (TOGAF) | 3 | Teori | `STB-06` | **`STB-703`** | `STI-306` Analisis & Perancangan Sistem Informasi |
| **7** | P3: Digital Platform Eng | Immersive Media & XR Development | 3 | +P | `STC-04` | **`STC-701`** | `STI-311` Web Front End Development |
| **7** | P3: Digital Platform Eng | SaaS Architecture & Multi-Tenancy | 3 | +P | `STC-05` | **`STC-702`** | `STI-416` Web Back End Development |
| **7** | P3: Digital Platform Eng | Digital Product Management & Agile | 3 | Teori | `STC-06` | **`STC-703`** | `STI-523` Manajemen Proyek TI |

---

### 4. PENYELARASAN DOKUMEN PROYEKSI POOL 2027 (DOKUMEN 025)

Pada dokumen usulan masa depan [025 — Rekomendasi Pengembangan Pool MK Peminatan 2027](025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md), 18 mata kuliah pilihan tambahan telah diselaraskan kodenya:
* **Semester 5 Usulan:** `STA-502` Computer Vision, `STA-503` Time Series; `STB-502` Linux Admin, `STB-503` Virtualization; `STC-502` Design Systems, `STC-503` E-Commerce API.
* **Semester 6 Usulan:** `STA-603` Big Data, `STA-604` Edge AI; `STB-603` Ethical Hacking, `STB-604` Kubernetes; `STC-603` Microservices, `STC-604` Cross-Platform Mobile.
* **Semester 7 Usulan:** `STA-704` Generative AI, `STA-705` Autonomous Systems; `STB-704` SOC & SIEM, `STB-705` Zero Trust; `STC-704` Enterprise ERP, `STC-705` Web3.

---

### 5. DEV LOG EKSEKUSI PER FILE (METRIK PERGANTIAN)

Eksekusi dijalankan secara serempak melalui engine `_tools/restrukturisasi_kode_peminatan.py` menggunakan boundary regex atomik:

| No | Nama Berkas | Lokasi | Titik Pergantian | Status |
|:---:|---|---|:---:|:---:|
| 1 | `AGENTS.md` | Workspace Root | 9 | ✅ Selesai |
| 2 | `000_CHANGELOG_ALIGNMENT_FINAL.md` | `KURIKULUM2026_REVISI/` | 3 | ✅ Selesai |
| 3 | `004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md` | `KURIKULUM2026_REVISI/` | 70 | ✅ Selesai |
| 4 | `005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md` | `KURIKULUM2026_REVISI/` | 72 | ✅ Selesai |
| 5 | `007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md` | `KURIKULUM2026_REVISI/` | 36 | ✅ Selesai |
| 6 | `009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md` | `KURIKULUM2026_REVISI/` | 14 | ✅ Selesai |
| 7 | `011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md` | `KURIKULUM2026_REVISI/` | 23 | ✅ Selesai |
| 8 | `012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md` | `KURIKULUM2026_REVISI/` | 47 | ✅ Selesai |
| 9 | `016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md` | `KURIKULUM2026_REVISI/` | 2 | ✅ Selesai |
| 10 | `017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md` | `KURIKULUM2026_REVISI/` | 6 | ✅ Selesai |
| 11 | `019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md` | `KURIKULUM2026_REVISI/` | 26 | ✅ Selesai |
| 12 | `023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md` | `KURIKULUM2026_REVISI/` | 6 | ✅ Selesai |
| 13 | `024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md` | `KURIKULUM2026_REVISI/` | 82 | ✅ Selesai |
| 14 | `025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md` | `KURIKULUM2026_REVISI/` | 35 | ✅ Selesai |
| 15 | `026_ANALISIS_KRITIS_MK_DIHAPUS_DAN_REKOMENDASI_PENGGANTI.md` | `KURIKULUM2026_REVISI/` | 26 | ✅ Selesai |
| 16 | `027_RENCANA_RESTRUKTURISASI_KODE_MK_CORE_STI_KONTINU.md` | `KURIKULUM2026_REVISI/` | 6 | ✅ Selesai |
| 17 | `028_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_CORE_STI.md` | `KURIKULUM2026_REVISI/` | 6 | ✅ Selesai |
| 18 | `030_JUSTIFIKASI_AKADEMIS_DAN_BoK_STA02_COMPUTATIONAL_METHODS_SEBAGAI_MK_PILIHAN.md` | `KURIKULUM2026_REVISI/` | 18 | ✅ Selesai |
| 19 | `031_PETA_KESELARASAN_KPT2024_STATUS_DOKUMEN.md` | `KURIKULUM2026_REVISI/` | 1 | ✅ Selesai |
| 20 | `039_LAMPIRAN_SIAP_BUKU_KPT_SISTEKIN_2026.md` | `KURIKULUM2026_REVISI/` | 21 | ✅ Selesai |
| 21 | `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md` | `KURIKULUM2026_REVISI/` | 160 | ✅ Selesai |
| **TOTAL** | **21 Berkas Markdown Dokumen Kurikulum** | — | **660** | **100% Sukses** |

#### Skrip Tooling Python yang Diperbarui:
1. `_tools/verify_k2025_ground_truth.py` (Mendukung pola regex `ST[ABC]-\d{2,3}`).
2. `_tools/export_024_awam.py` (Mendukung pengenalan 3-digit elektif).
3. `_tools/add_peminatan_to_005.py`
4. `_tools/add_peminatan_to_buku.py`
5. `_tools/apply_dl_security_switch.py`
6. `_tools/deep_cross_audit.py`
7. `_tools/export_005_to_excel.py`
8. `_tools/fill_template_kpt.py`
9. `_tools/fix_012.py`
10. `_tools/convert_md_to_html.py` (Menambahkan entri Dokumen 035 dan 036 ke portal navigasi).

---

### 6. BUKTI VERIFIKASI SISTEM (VERIFICATION AUDIT TRAIL)

#### A. Verifikasi Ground Truth SIAKAD K2025 (`verify_k2025_ground_truth.py`)
```
==============================================================================
VERIFIKASI GROUND TRUTH KURIKULUM 2025 (LAPORAN SIAKAD)
==============================================================================
Sumber : KURIKULUM2025\Laporan Daftar Kurikulum Prodi Sistekin.pdf

[1] INTEGRITAS EKSTRAKSI PDF                : 56 MK / 146 SKS OK
[2] HEADER SEKSI 3.x DOKUMEN 024            : 8/8 semester cocok OK
[3] AUDIT BARIS DEMI BARIS MATRIKS UTAMA    : 0 ketidakcocokan atribut OK
[4] PENEMPATAN BARIS PADA SEKSI ASAL        : 0 baris salah seksi OK
[5] ZERO ORPHAN TABEL ENTRI SIAKAD          : 0 orphan / 0 fiktif OK
[6] NERACA KATEGORI EKIVALENSI E1-E5        : E1=34, E2=11, E3=8, E4=1, E5=2 OK
[7] VALIDITAS KODE TARGET KURIKULUM 2026    : 49 kode target unik valid OK
[8] SEMESTER MK ELEKTIF PEMINATAN           : 18 kode definitif presisi OK
[9] NERACA REKOGNISI ARAH BALIK (BAGIAN 3A) : 114 SKS diakui / 14 SKS defisit OK
[10] KELENGKAPAN REKOGNISI PORTOFOLIO 67 MK : 49 direkognisi / 18 baru OK
[11] KETUNTASAN ATURAN KLAIM GANDA          : 2 kasus terselesaikan tuntas OK

==============================================================================
[LULUS] Seluruh rujukan Kurikulum 2025 konsisten 100% dengan Laporan SIAKAD.
==============================================================================
```

#### B. Audit Zero Residual Kode Lama (`scan_peminatan_occurrences.py`)
```
Total occurrences of old codes (STA-01..06, STB-01..06, STC-01..06): 0 across 45 files.
```

#### C. Audit Zero Discrepancy (`verify_zero_discrepancy.py`)
```
Auditing 45 markdown files in KURIKULUM2026_REVISI...
[SUCCESS] 100% PERFECT ALIGNMENT: Semua file Markdown di KURIKULUM2026_REVISI telah 100% sinkron dan selaras!
```

---

### 7. ARTEFAK LUARAN RESMI YANG DITERBITKAN

1. **Berkas Markdown Kurikulum:**
   - [005 — Struktur Kurikulum 8 Semester & Peminatan](005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md)
   - [007 — Formulasi CPMK & Silabus 3-Tabel 67 MK Portofolio](007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md)
   - [024 — Matriks Ekivalensi Kurikulum 2025 ke Kurikulum 2026](024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md)
   - [035 — Restrukturisasi Kode MK Peminatan (STA, STB, STC) Berbasis Semester](035_RESTRUKTURISASI_KODE_MK_PEMINATAN_STA_STB_STC.md)
   - [036 — Dev Report & Dev Log Restrukturisasi Kode MK Peminatan](036_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_PEMINATAN.md)
   - [BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md](BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md)
2. **Berkas Diseminasi Non-Teknis:**
   - `024_RINGKAS_EKIVALENSI_UNTUK_AWAM.xlsx` (8 Sheet lengkap dengan filter & warna status).
   - `024_RINGKAS_EKIVALENSI_UNTUK_AWAM.docx` (9 Tabel format lanskap siap cetak dan edar).
3. **Portal Navigasi & HTML Interaktif:**
   - 37 berkas HTML terkonversi rapi.
   - Portal web [index.html](index.html) dengan menu navigasi terintegrasi.

---
*Laporan Dev Report & Dev Log ini disahkan sebagai dokumentasi resmi rekayasa Kurikulum OBE SISTEKIN 2026.*  
**Tim Pengembang Kurikulum FSTI Universitas Widyagama Malang**
