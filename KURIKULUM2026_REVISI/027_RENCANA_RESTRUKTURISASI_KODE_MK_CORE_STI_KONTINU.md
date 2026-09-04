# 027 — RENCANA AKSI RESTRUKTURISASI KODE MK CORE STI KONTINU
## Standarisasi Penomoran Berkesinambungan (STI-101 s.d. STI-728) Kurikulum 2026
**Program Studi Sistem dan Teknologi Informasi (S1) — FSTI Universitas Widyagama Malang**

---

### 1. LATAR BELAKANG DAN RASIONALITAS

Pada penyusunan draf Kurikulum 2026 sebelumnya, kode mata kuliah Inti Program Studi (Core STI) menggunakan skema *reset per semester* (`STI-101..103`, `STI-201..202`, `STI-301..307`, `STI-401..407`, `STI-501..506`, `STI-601..604`, `STI-701`). Skema tersebut memiliki dua kelemahan utama:
1. **Inkonsistensi Sistemik:** Mata Kuliah Wajib Umum (MKWU) di Kurikulum 2026 telah menggunakan skema nomor berkesinambungan lintas semester (`MKU-101..103` $\rightarrow$ `MKU-204` $\rightarrow$ `MKU-405..406` $\rightarrow$ `MKU-507..508`), demikian pula konvensi SIAKAD resmi UWG pada Kurikulum 2025 (`STI-101..104` $\rightarrow$ `STI-205..209` $\rightarrow$ dst.).
2. **Anomali Lompatan Nomor:** Pada draf lama terdapat nomor yang terlewat, yaitu hilangnya nomor 406 di Semester 4 (melompat dari `STI-405` ke `STI-407`) serta hilangnya nomor 502 di Semester 5 (melompat dari `STI-501` ke `STI-503`).

Sesuai arahan Tim Kurikulum, seluruh 28 Mata Kuliah Core STI distandarisasi menggunakan formula:
$$\mathbf{STI\text{-}[Semester][Nomor\ Urut\ Kumulatif\ 2\ Digit]}$$
di mana digit semester (1 s.d. 7) dipadukan dengan nomor urut kumulatif (01 s.d. 28) yang berlanjut tanpa putus antar semester.

---

### 2. TABEL DEFINITIF MAPPING KODE MK CORE STI (28 MK)

| Sem | No Urut | Kode Lama | Kode Baru Kontinu | Nama Mata Kuliah | SKS | Prasyarat Lama | Prasyarat Baru |
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

### 3. PENYESUAIAN PRASYARAT PADA MK LAIN (FSTI & PEMINATAN)

Mata kuliah non-Core STI yang memiliki prasyarat ke mata kuliah Core STI wajib dimutakhirkan:
1. **`FST-408` Probabilitas dan Statistika (Sem 4):** Prasyarat tetap `STI-102`.
2. **`FST-610` Capstone Project FSTI (Sem 7):** Prasyarat `STI-506` $\rightarrow$ diperbarui menjadi **`STI-523`**.
3. **`STA-01` Decision Support Systems (Sem 5):** Prasyarat `STI-402` $\rightarrow$ diperbarui menjadi **`STI-415`**.
4. **`STB-01` Network Security & Digital Forensics (Sem 5):** Prasyarat `STI-307` $\rightarrow$ diperbarui menjadi **`STI-312`**.
5. **`STB-02` Cloud Architecture & DevOps (Sem 6):** Prasyarat `STI-404` $\rightarrow$ diperbarui menjadi **`STI-417`**.
6. **`STC-01` UX Research & Design (Sem 5):** Prasyarat `STI-303` $\rightarrow$ diperbarui menjadi **`STI-308`**.
7. **`STC-02` Rekayasa & Otomasi Proses Bisnis (Sem 6):** Prasyarat `STI-301` $\rightarrow$ diperbarui menjadi **`STI-306`**.
8. **`STC-05` SaaS Architecture & Multi-Tenancy (Sem 7):** Prasyarat `STI-604` $\rightarrow$ diperbarui menjadi **`STI-627`**.

---

### 4. ANALISIS DAMPAK PADA DOKUMEN 024 (MATRIKS EKIVALENSI)

Penataan kode ini berdampak langsung pada pemetaan ekivalensi Kurikulum 2025 $\rightarrow$ Kurikulum 2026:
- Semua baris target K2026 yang sebelumnya merujuk ke kode lama (`STI-201` s.d. `STI-701`) diselaraskan ke kode baru (`STI-204` s.d. `STI-728`).
- Kolisi kode K2025 vs K2026 ditinjau ulang:
  - `STI-205` di K2025 adalah *Matematika Diskrit*, di K2026 menjadi *Aljabar Linear dan Matriks*.
  - `STI-310` di K2025 adalah *APSI*, di K2026 menjadi *Sistem Operasi*.
  - `STI-311` di K2025 adalah *Sistem Operasi*, di K2026 menjadi *Web Front End Development*.
  - `STI-418` di K2025 adalah *Sistem Cerdas*, di K2026 menjadi *Dasar Keamanan Informasi*.
  Tabel catatan kolisi kode di Dokumen 024 diperbarui untuk memberi panduan definitif bagi BAAK / Admin SIAKAD.

---

### 5. RENCANA EKSEKUSI DAN VERIFIKASI (ZERO DISCREPANCY)

Eksekusi refactoring dilakukan menggunakan skrip automasi teruji dengan tahapan:
1. **Fase 1 — Batch Replacement Dokumen Markdown:**
   Memperbarui 20 file markdown utama (`003`, `004`, `005`, `006`, `007`, `008`, `009D`, `009`, `011`, `012`, `013`, `014`, `015`, `016`, `017`, `018`, `024`, `025`, `026`, `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md`).
2. **Fase 2 — Pemutakhiran Skrip Python & Tooling:**
   Memperbarui kamus kode pada `_tools/verify_zero_discrepancy.py`, `_tools/export_011_tables_to_excel.py`, `_tools/export_024_awam.py`, `_tools/export_all_to_excel.py`.
3. **Fase 3 — Re-generasi Artifact Output:**
   - Jalankan ekspor Excel `011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.xlsx`.
   - Jalankan ekspor Excel & Word `024_RINGKAS_EKIVALENSI_UNTUK_AWAM.xlsx` dan `.docx`.
   - Jalankan konverter HTML seluruh dokumen markdown (`_tools/convert_md_to_html.py`).
4. **Fase 4 — Audit & Verifikasi Penuh:**
   - Jalankan `python _tools/verify_zero_discrepancy.py` untuk memastikan 100% konsistensi antar 24 file.
   - Jalankan `python _tools/verify_k2025_ground_truth.py` untuk memastikan kepatuhan ground truth K2025 tetap terjaga.
