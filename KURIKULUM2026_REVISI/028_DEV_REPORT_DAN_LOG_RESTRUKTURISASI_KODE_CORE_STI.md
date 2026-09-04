# 028 — DEV REPORT & DEV LOG: RESTRUKTURISASI KODE MK CORE STI KONTINU
## Laporan Rekayasa dan Log Perubahan Penomoran Berkesinambungan (STI-101 s.d. STI-728)
**Program Studi Sistem dan Teknologi Informasi (S1) — FSTI Universitas Widyagama Malang**

---

### RINGKASAN EKSEKUTIF (EXECUTIVE SUMMARY)

| Parameter | Keterangan |
|---|---|
| **Tanggal Eksekusi** | 04 September 2026 |
| **Status Pekerjaan** | **SELESAI (100% Tuntas, Teruji & Terverifikasi)** |
| **Lingkup Rekayasa** | Restrukturisasi sistemik kode 28 Mata Kuliah Inti Program Studi (Core STI) Kurikulum 2026 |
| **Skema Pengkodean** | Transisi dari *Reset per Semester* (`STI-101..103`, `STI-201..202`, dst.) ke *Continuous Running Number* lintas semester (`STI-101` s.d. `STI-728`) |
| **Total Berkas Diperbarui** | **23 Dokumen Markdown** (termasuk `AGENTS.md`) + **4 Skrip Otomasi Python** |
| **Volume Pergantian Teks** | **1.301 titik pergantian** tersubstitusi secara atomik (*single-pass word-boundary regex*) |
| **Artefak Luaran** | 1 Berkas Excel Master OBE (14 Tab), 1 Berkas Excel Ekivalensi Awam (8 Sheet), 1 Dokumen Word Lanskap Siap Cetak, 33 Halaman HTML Portal Interaktif |
| **Integritas Sistem** | **Zero Discrepancy** (Lulus uji sinkronisasi 35 dokumen & Lulus 11/11 audit ground truth SIAKAD) |

---

### 1. LATAR BELAKANG DAN MASALAH TEKNIS (PROBLEM STATEMENT)

Sebelum implementasi ini, 28 mata kuliah Inti Program Studi (Core STI) pada draf Kurikulum 2026 menggunakan skema penomoran berbasis reset di tiap semester:
* Sem 1: `STI-101`, `STI-102`, `STI-103`
* Sem 2: `STI-201`, `STI-202`
* Sem 3: `STI-301` s.d. `STI-307`
* Sem 4: `STI-401`, `STI-402`, `STI-403`, `STI-404`, `STI-405`, `STI-407`
* Sem 5: `STI-501`, `STI-503`, `STI-504`, `STI-505`, `STI-506`
* Sem 6: `STI-601` s.d. `STI-604`
* Sem 7: `STI-701`

**Temuan Masalah Arsitektural:**
1. **Inkonsistensi Nomenklatur:** Mata Kuliah Wajib Umum (MKWU) Kurikulum 2026 telah menggunakan skema *running number* kumulatif lintas semester (`MKU-101..103` $\rightarrow$ `MKU-204` $\rightarrow$ `MKU-405..406` $\rightarrow$ `MKU-507..508`). Demikian juga standar historis SIAKAD UWG pada Kurikulum 2025 (`STI-101..104` $\rightarrow$ `STI-205..209` $\rightarrow$ `STI-310..317` $\rightarrow$ dst.). Penggunaan skema reset pada Core STI menciptakan disparitas konvensi.
2. **Anomali Lompatan Nomor (Dead Codes):**
   * Di Semester 4, kode melompat dari `STI-405` langsung ke `STI-407` (nomor `STI-406` tidak ada / hilang).
   * Di Semester 5, kode melompat dari `STI-501` langsung ke `STI-503` (nomor `STI-502` tidak ada / hilang).
3. **Ketiadaan Informasi Urutan Kumulatif:** Pengguna dokumen tidak dapat langsung mengetahui nomor urut mata kuliah dalam portofolio inti prodi hanya dari melihat 3 digit kode MK.

---

### 2. FORMULA DAN STANDAR PENGKODEAN BARU

Sesuai arahan Tim Pengembang Kurikulum, formula penomoran distandarisasi secara ketat:
$$\mathbf{STI\text{-}[Semester][Nomor\ Urut\ Kumulatif\ 2\ Digit]}$$

* **Digit 1 (`Semester`):** Menunjukkan penempatan semester mata kuliah (1 s.d. 7).
* **Digit 2 & 3 (`Nomor Urut Kumulatif`):** Angka urut kontinu 2 digit (`01` s.d. `28`) yang berjalan berkesinambungan tanpa putus dari Semester 1 hingga Semester 7.

---

### 3. TABEL TRANSFORMASI KODE 28 MK CORE STI (BEFORE VS AFTER)

| Sem | No Urut | Kode Lama | Kode Baru Kontinu | Nama Mata Kuliah | SKS | Prasyarat Lama | Prasyarat Baru (Updated) |
|:---:|:---:|:---:|:---:|---|:---:|---|---|
| **1** | 01 | `STI-101` | **`STI-101`** | Pengantar Sistem dan Teknologi Informasi | 2 | — | — |
| **1** | 02 | `STI-102` | **`STI-102`** | Kalkulus | 3 | — | — |
| **1** | 03 | `STI-103` | **`STI-103`** | Arsitektur dan Organisasi Sistem Teknologi Informasi | 3 | — | — |
| **2** | 04 | `STI-201` | **`STI-204`** | Matematika Diskrit dan Logika | 3 | `STI-103` | `STI-103` |
| **2** | 05 | `STI-202` | **`STI-205`** | Aljabar Linear dan Matriks | 3 | `STI-102` | `STI-102` |
| **3** | 06 | `STI-301` | **`STI-306`** | Analisis dan Perancangan Sistem Informasi | 3 | `STI-101`, `FST-207` | `STI-101`, `FST-207` |
| **3** | 07 | `STI-302` | **`STI-307`** | Sistem Cerdas | 2 | `STI-201`, `FST-204` | **`STI-204`**, `FST-204` |
| **3** | 08 | `STI-303` | **`STI-308`** | UI/UX Design & Prototyping | 3 | `FST-101` | `FST-101` |
| **3** | 09 | `STI-304` | **`STI-309`** | Rekayasa Perangkat Lunak | 3 | `FST-203` | `FST-203` |
| **3** | 10 | `STI-305` | **`STI-310`** | Sistem Operasi | 3 | `STI-103` | `STI-103` |
| **3** | 11 | `STI-306` | **`STI-311`** | Web Front End Development | 3 | `FST-102` | `FST-102` |
| **3** | 12 | `STI-307` | **`STI-312`** | Jaringan Komputer | 3 | `STI-103` | `STI-103` |
| **4** | 13 | `STI-401` | **`STI-413`** | Machine Learning | 3 | `STI-202`, `STI-302` | **`STI-205`**, **`STI-307`** |
| **4** | 14 | `STI-403` | **`STI-414`** | Pengantar NLP & Information Retrieval | 2 | `STI-302` | **`STI-307`** |
| **4** | 15 | `STI-402` | **`STI-415`** | Data Warehouse & Business Intelligence | 3 | `FST-207` | `FST-207` |
| **4** | 16 | `STI-407` | **`STI-416`** | Web Back End Development | 3 | `FST-207`, `STI-306` | `FST-207`, **`STI-311`** |
| **4** | 17 | `STI-404` | **`STI-417`** | Komputasi Awan (Cloud Computing) | 3 | `STI-307`, `STI-305` | **`STI-312`**, **`STI-310`** |
| **4** | 18 | `STI-405` | **`STI-418`** | Dasar Keamanan Informasi | 2 | `STI-307` | **`STI-312`** |
| **5** | 19 | `STI-501` | **`STI-519`** | Deep Learning & Neural Networks | 3 | `STI-401` | **`STI-413`** |
| **5** | 20 | `STI-503` | **`STI-520`** | Data Mining & Visualisasi Data | 3 | `STI-401`, `STI-402` | **`STI-413`**, **`STI-415`** |
| **5** | 21 | `STI-504` | **`STI-521`** | Internet of Things (IoT) | 3 | `STI-307`, `STI-305` | **`STI-312`**, **`STI-310`** |
| **5** | 22 | `STI-505` | **`STI-522`** | Pemrograman Aplikasi Mobile | 3 | `STI-306`, `STI-407` | **`STI-311`**, **`STI-416`** |
| **5** | 23 | `STI-506` | **`STI-523`** | Manajemen Proyek TI | 3 | `STI-301`, `STI-304` | **`STI-306`**, **`STI-309`** |
| **6** | 24 | `STI-601` | **`STI-624`** | Integrasi Layanan Cerdas Berbasis AI | 3 | `STI-501`, `STI-407` | **`STI-519`**, **`STI-416`** |
| **6** | 25 | `STI-602` | **`STI-625`** | Smart City & Pemerintahan Digital | 2 | `STI-504` | **`STI-521`** |
| **6** | 26 | `STI-603` | **`STI-626`** | Keamanan Informasi Lanjut | 3 | `STI-405` | **`STI-418`** |
| **6** | 27 | `STI-604` | **`STI-627`** | Digital Platform Engineering | 3 | `STI-407` | **`STI-416`** |
| **7** | 28 | `STI-701` | **`STI-728`** | Inovasi Teknologi dan Startup Digital | 3 | `STI-604`, `MKU-204` | **`STI-627`**, `MKU-204` |

---

### 4. PENYESUAIAN POHON PRASYARAT PADA MATA KULIAH LAIN (CASCADING)

Perubahan kode Core STI secara otomatis memicu pemutakhiran syarat prasyarat pada:
1. **MK Wajib Fakultas (FSTI):**
   * `FST-610 Capstone Project FSTI` (Sem 7): Prasyarat `STI-506` dimutakhirkan ke **`STI-523`** *Manajemen Proyek TI*.
2. **MK Pilihan Peminatan (Elektif):**
   * `STA-01 Decision Support Systems` (Sem 5): Prasyarat `STI-402` dimutakhirkan ke **`STI-415`** *Data Warehouse & BI*.
   * `STB-01 Network Security & Digital Forensics` (Sem 5): Prasyarat `STI-307` dimutakhirkan ke **`STI-312`** *Jaringan Komputer*.
   * `STB-02 Cloud Architecture & DevOps` (Sem 6): Prasyarat `STI-404` dimutakhirkan ke **`STI-417`** *Komputasi Awan*.
   * `STC-01 UX Research & Design` (Sem 5): Prasyarat `STI-303` dimutakhirkan ke **`STI-308`** *UI/UX Design & Prototyping*.
   * `STC-02 Rekayasa & Otomasi Proses Bisnis` (Sem 6): Prasyarat `STI-301` dimutakhirkan ke **`STI-306`** *Analisis dan Perancangan SI*.
   * `STC-05 SaaS Architecture & Multi-Tenancy` (Sem 7): Prasyarat `STI-604` dimutakhirkan ke **`STI-627`** *Digital Platform Engineering*.

---

### 5. DEV LOG EKSEKUSI PER FILE (METRIK PERGANTIAN)

Eksekusi dijalankan via engine Python `_tools/execute_core_sti_migration.py` menggunakan mekanisme penggantian satu putaran (*single-pass regex*) dengan batas kata (`\b`) guna mencegah efek penggantian berulang (*cascading replacement bug*).

| No | Nama Berkas | Lokasi | Jumlah Titik Diganti | Status |
|:---:|---|---|:---:|:---:|
| 1 | `AGENTS.md` | Workspace Root | 7 | ✅ Selesai |
| 2 | `000_CHANGELOG_ALIGNMENT_FINAL.md` | `KURIKULUM2026_REVISI/` | 15 | ✅ Selesai |
| 3 | `004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md` | `KURIKULUM2026_REVISI/` | 122 | ✅ Selesai |
| 4 | `005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md` | `KURIKULUM2026_REVISI/` | 49 | ✅ Selesai |
| 5 | `006_DISTRIBUSI_DAN_PANDUAN_MK_PEMINATAN_MBKM.md` | `KURIKULUM2026_REVISI/` | 5 | ✅ Selesai |
| 6 | `007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md` | `KURIKULUM2026_REVISI/` | 84 | ✅ Selesai |
| 7 | `009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md` | `KURIKULUM2026_REVISI/` | 23 | ✅ Selesai |
| 8 | `009_PEDOMAN_CAPSTONE_PROJECT_DAN_TUGAS_AKHIR_NON_SKRIPSI.md` | `KURIKULUM2026_REVISI/` | 5 | ✅ Selesai |
| 9 | `011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md` | `KURIKULUM2026_REVISI/` | 135 | ✅ Selesai |
| 10 | `012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md` | `KURIKULUM2026_REVISI/` | 134 | ✅ Selesai |
| 11 | `013_REKOMENDASI_SOLUSI_DAN_MITIGASI_KELEMAHAN_KURIKULUM.md` | `KURIKULUM2026_REVISI/` | 19 | ✅ Selesai |
| 12 | `014_ANALISIS_KRITIS_PEMANGKASAN_SKS_TEORI_SEM4_SEM5.md` | `KURIKULUM2026_REVISI/` | 10 | ✅ Selesai |
| 13 | `015_SIMULASI_AKSELERASI_KELULUSAN_7_SEMESTER.md` | `KURIKULUM2026_REVISI/` | 48 | ✅ Selesai |
| 14 | `016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md` | `KURIKULUM2026_REVISI/` | 21 | ✅ Selesai |
| 15 | `017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md` | `KURIKULUM2026_REVISI/` | 49 | ✅ Selesai |
| 16 | `018_PANDUAN_RUBRIK_KLASTER_DAN_MODEL_ASESMEN_OBE_DOSEN.md` | `KURIKULUM2026_REVISI/` | 22 | ✅ Selesai |
| 17 | `019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md` | `KURIKULUM2026_REVISI/` | 76 | ✅ Selesai |
| 18 | `023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md` | `KURIKULUM2026_REVISI/` | 18 | ✅ Selesai |
| 19 | `024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md` | `KURIKULUM2026_REVISI/` | 129 | ✅ Selesai |
| 20 | `025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md` | `KURIKULUM2026_REVISI/` | 46 | ✅ Selesai |
| 21 | `026_ANALISIS_KRITIS_MK_DIHAPUS_DAN_REKOMENDASI_PENGGANTI.md` | `KURIKULUM2026_REVISI/` | 10 | ✅ Selesai |
| 22 | `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md` | `KURIKULUM2026_REVISI/` | 274 | ✅ Selesai |
| 23 | `_tools/export_024_awam.py` | `KURIKULUM2026_REVISI/_tools/` | 4 | ✅ Selesai |
| 24 | `_tools/verify_zero_discrepancy.py` | `KURIKULUM2026_REVISI/_tools/` | 3 | ✅ Selesai |
| 25 | `_tools/deep_cross_audit.py` | `KURIKULUM2026_REVISI/_tools/` | 25 | ✅ Selesai |
| 26 | `_tools/fix_012.py` | `KURIKULUM2026_REVISI/_tools/` | 15 | ✅ Selesai |
| **TOTAL** | — | — | **1.348** | **100% SUKSES** |

*(Catatan: Dokumen `027_RENCANA_RESTRUKTURISASI_KODE_MK_CORE_STI_KONTINU.md` dipertahankan secara sengaja agar riwayat tabel asal `STI-201` s.d. `STI-701` tetap terdokumentasi).*

---

### 6. LAPORAN HASIL PENGUJIAN & VALIDASI (QA / INTEGRITY AUDIT)

#### 6.1 Uji Konsistensi Dokumen (`verify_zero_discrepancy.py`)
* **Status:** **PASS / 100% SINKRON**
* **Hasil Terminal:**
  ```
  Auditing 35 markdown files in KURIKULUM2026_REVISI...
  [SUCCESS] 100% PERFECT ALIGNMENT: Semua file Markdown di KURIKULUM2026_REVISI telah 100% sinkron dan selaras!
  ```

#### 6.2 Uji Ground Truth Kurikulum 2025 (`verify_k2025_ground_truth.py`)
* **Status:** **LULUS 11/11 KELOMPOK UJI**
* **Validasi Target K2026:**
  - Kode target unik: 49 MK valid (0 kode tidak dikenal di Dok 005/007).
  - Neraca rekognisi arah balik: Paket wajib K2026 = 49 MK / 128 SKS (114 SKS diakui, 14 SKS defisit MK baru: `STI-103`, `FST-204`, `STI-312`, `STI-626`, `FST-610`).
  - Ketuntasan klaim ganda: `STI-414` (menang `STI-528`), `STI-728` (menang `STI-742`).

#### 6.3 Re-generasi Berkas Excel & Word Master
1. **`011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.xlsx`:** Berhasil diekspor ulang (14 tab berformat rapi dan autofit).
2. **`024_RINGKAS_EKIVALENSI_UNTUK_AWAM.xlsx`:** Berhasil diekspor ulang (8 sheet interaktif dengan header beku dan filter otomatis).
3. **`024_RINGKAS_EKIVALENSI_UNTUK_AWAM.docx`:** Berhasil diekspor ulang (9 tabel lanskap siap cetak dan edar).

#### 6.4 Re-generasi Portal HTML
* Seluruh 32 file Markdown dikonversi ulang ke HTML modern dengan styling interaktif, prism code highlighting, dan responsive tables.
* File `index.html` diperbarui sebagai portal navigasi tunggal seluruh dokumen kurikulum.

---

### 7. KESIMPULAN

Restrukturisasi kode mata kuliah Core STI Kurikulum 2026 menjadi sistem kontinu (`STI-101` s.d. `STI-728`) telah berhasil dituntaskan dengan standar mutu tertinggi (*Zero Redundancy, Zero Gap, Zero Discrepancy*). Seluruh dokumen kebijakan, silabus, instrumen evaluasi OBE, buku kurikulum final, dan berkas ekivalensi SIAKAD kini telah berada dalam kondisi seragam, konsisten, dan siap diimplementasikan.

---
*Dokumen ini merupakan catatan resmi rekayasa perangkat ajar Kurikulum OBE SISTEKIN 2026.*  
**Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang**
