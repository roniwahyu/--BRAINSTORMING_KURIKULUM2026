# 018 — AUDIT TRAIL: PERBAIKAN DOKUMEN KURIKULUM SISTEKIN

**Tanggal:** 10 Agustus 2026
**Status:** FINAL — Log Perbaikan untuk Penelusuran & Verifikasi Berjenjang
**Tujuan:** Ground truth untuk agentic AI + verifikasi manusia

---

## 1. KONTEKS AWAL

### 1.1 Sumber Data

| Sumber | Status | Isi |
|---|---|---|
| `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` | ✅ Terverifikasi manusia, sudah dijalankan 2 semester | 56 MK, 146 SKS, 8 semester |
| `KURIKULUM2025/Implementasi_MODUL_OBE_SISTEKIN2025.pdf` | ✅ Terverifikasi manusia | 10 CPL (CPL01-CPL10), 6 PL (PL01-PL06) |

### 1.2 Fakta Ground Truth

| Aspek | KURIKULUM2025 (Lama) | Keterangan |
|---|---|---|
| **Total MK** | 56 MK | Semua wajib, 0 pilihan |
| **Total SKS** | 146 SKS | |
| **CPL** | 10 CPL (CPL01-CPL10) | Di `Implementasi_MODUL_OBE_SISTEKIN2025.pdf` |
| **Profil Lulusan** | 6 PL (PL01-PL06) | Di `Implementasi_MODUL_OBE_SISTEKIN2025.pdf` |
| **Peminatan** | 0 | Tidak ada |
| **MK Praktikum** | 17 MK (+P) | |
| **Status** | Berjalan 2 semester | Sudah di SIAKAD |

---

## 2. TEMUAN AUDIT (Sebelum Perbaikan)

### 2.1 Error HIGH Priority yang Ditemukan

| # | Error | Dokumen Asal | Bukti | Dampak |
|---|---|---|---|---|
| **H1** | Klaim salah "CPL belum ada" | 001, 002, 007 | KURIKULUM2025 punya 10 CPL di `Implementasi_MODUL_OBE_SISTEKIN2025.pdf` | Salah paham terhadap kondisi aktual |
| **H2** | Angka fabricasi "rencana 17 CPL" | 001 line 54 | Tidak ada angka 17 di sumber manapun | Hallucination |
| **H3** | Klaim "15 CPL" tapi daftar cuma 14 | 009, 009E, 010 | S(1)+KU(3)+P(4)+KK(6) = 14, bukan 15 | Error matematika |
| **H4** | 005 vs 011 kontradiksi fundamental | 005, 011 | Beda SKS per semester, Capstone vs Skripsi | Dokumen tidak konsisten |
| **H5** | BoK IS2020 nama salah | 010 lines 101-121 | Nama BK tidak sesuai IS2020 asli | Hallucination |
| **H6** | "20 SKS Magang" klaim legal tanpa dasar | 016 | Tidak ada di Permendikbudristek 53/2023 | Overclaim |
| **H7** | Gaji fabricasi Rp 5-12 juta | 006 lines 150, 177, 205 | Tidak ada data pasar kerja | Hallucination |

### 2.2 Error MEDIUM Priority

| # | Error | Dokumen | Keterangan |
|---|---|---|---|
| M1 | Klaim "5 Profil Lulusan" padahal 6 | 001 | Salah hitung |
| M2 | P2 BoK "AI, ML" di peminatan salah | 006 | Copy-paste error |
| M3 | Bahasa Inggris/Kewarganegaraan pindah semester tanpa penjelasan | 001 | Silent change |
| M4 | MK "renamed" diklaim "MK Baru" | 015 | Salah label |

---

## 3. LOG PERBAIKAN

### 3.1 Perbaikan Dokumen 001

**File:** `001_LAPORAN_GAP_ANALYSIS_KURIKULUM2025_SISTEKIN.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 54 | "Jumlah CPL (rencana 17) wajar" | "Sudah ada 10 CPL (CPL01–CPL10). Terdokumentasi di `Implementasi_MODUL_OBE_SISTEKIN2025.pdf`" | Angka 17 fabricasi |
| 67 | "❌ Belum ada (hanya label ringkas)" | "⚠️ Sudah ada 10 CPL (CPL01–CPL10), belum dikategorikan S/KU/P/KK" | CPL sudah ada |
| 68 | "⚠️ Profil ada (5), tapi belum jadi PEO terukur" | "✅ Sudah ada 6 PL (PL01–PL06) di `Implementasi_MODUL_OBE_SISTEKIN2025.pdf`, perlu tambah keterukuran PEO" | Salah hitung (5→6) |
| 116 | "❌ — Rumuskan CPL 4 kategori" | "⚠️ Sudah ada 10 CPL (CPL01–CPL10). Reorganisasi ke 4 kategori S/KU/P/KK" | CPL sudah ada |

### 3.2 Perbaikan Dokumen 002

**File:** `002_INSIGHT_KELEMAHAN_KURIKULUM2025_vs_BUKU_OBE.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 40 | "yang ada hanyalah kolom 'Nilai Minimal C' dan label kasar; belum ada rumusan CPL resmi" | "Sudah ada 10 CPL (CPL01–CPL10) di `Implementasi_MODUL_OBE_SISTEKIN2025.pdf`, tetapi belum dikategorikan ke 4 kategori SN-Dikti" | CPL sudah ada |

### 3.3 Perbaikan Dokumen 005

**File:** `005_STRUKTUR_REVISI_KURIKULUM_SISTEKIN_8_SEMESTER.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 2 | "Versi: Final" | "Versi: DRAFT LAMA" | Dokumen sudah disepngkan |
| 3 | (tidak ada) | "⚠️ STATUS: Dokumen ini sudah DISEPINGKAN oleh 011_STRUKTUR_KURIKULUM_TABEL.md" | Kontradiksi dengan 011 |

### 3.4 Perbaikan Dokumen 006

**File:** `006_KEPUTUSAN_FINAL_ARAH_KURIKULUM_SISTEKIN.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 150 | "Target Gaji Entry: Rp 7-12 juta" | (dihapus) | Hallucination — tidak ada data |
| 177 | "Target Gaji Entry: Rp 6-10 juta" | (dihapus) | Hallucination — tidak ada data |
| 205 | "Target Gaji Entry: Rp 5-9 juta (plus equity untuk startup)" | (dihapus) | Hallucination — tidak ada data |

### 3.5 Perbaikan Dokumen 007

**File:** `007_BEDAH_STRUKTUR_KURIKULUM_SISTEKIN.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 175 | "CPL — Belum ada — ⚠️ Perlu Langkah 1-2" | "Sudah ada 10 CPL (CPL01–CPL10), belum dikategorikan S/KU/P/KK — ⚠️ Perlu reorganisasi" | CPL sudah ada |

### 3.6 Perbaikan Dokumen 009

**File:** `009_LANGKAH2_CPL_FORMAL.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 1 | "CPL FORMAL (15 CPL)" | "CPL FORMAL (14 CPL)" | Error matematika: S(1)+KU(3)+P(4)+KK(6)=14 |
| 4 | "15 CPL sesuai BUKU_OBE" | "14 CPL sesuai BUKU_OBE" | Konsisten |
| 6 | "→ 15 CPL (konsolidasi)" | "→ 14 CPL (konsolidasi)" | Konsisten |
| 7 | "vs CPL baru (15)" | "vs CPL baru (14)" | Konsisten |

### 3.7 Perbaikan Dokumen 009E

**File:** `009E_RINGKASAN_CPL_LENGKAP_PEMETAAN_BoK.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 3 | "CPL Lengkap 15 CPL" | "CPL Lengkap 14 CPL" | Error matematika |
| 6 | "15 CPL baru merupakan" | "14 CPL baru merupakan" | Konsisten |
| 10 | "RINGKASAN CPL — 15 CPL" | "RINGKASAN CPL — 14 CPL" | Konsisten |

### 3.8 Perbaikan Dokumen 010

**File:** `010_KOMPILASI_CPL_KE_STRUKTUR_KURIKULUM.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 4 | "Kompilasi CPL (15 CPL)" | "Kompilasi CPL (14 CPL)" | Error matematika |
| 7 | "15 CPL baru merupakan" | "14 CPL baru merupakan" | Konsisten |
| 97 | "15 CPL → PEMETAAN KE BOBody" | "14 CPL → PEMETAAN KE Body" | Fix typo + count |
| 101-121 | BoK names salah (History and Social Context, dll) | BoK names benar (Foundation of IS, Data/Information Management, dll) | Hallucination — nama BK tidak sesuai IS2020 |

### 3.9 Perbaikan Dokumen 011

**File:** `011_STRUKTUR_KURIKULUM_TABEL.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 5 | "009 (15 CPL)" | "009 (14 CPL)" | Error matematika |

### 3.10 Perbaikan Dokumen 012

**File:** `012_MATRIKS_CPL_vs_MK.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 1 | "MATRIKS TOTAL MK vs 15 CPL" | "MATRIKS TOTAL MK vs 14 CPL" | Error matematika |
| 5 | "009 (15 CPL)" | "009 (14 CPL)" | Konsisten |
| 6 | "15 CPL" | "14 CPL" | Konsisten |

### 3.11 Perbaikan Dokumen 015

**File:** `015_PERBANDINGAN_KURIKULUM_2025_vs_2026.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 21 | "15 CPL (S/KU/P/KK)" | "14 CPL (S/KU/P/KK)" | Error matematika |
| 226 | "15 CPL (S/KU/P/KK)" | "14 CPL (S/KU/P/KK)" | Konsisten |
| 243 | "CPL: 10 → 15" | "CPL: 10 → 14" | Konsisten |

### 3.12 Perbaikan Dokumen 016

**File:** `016_KETENTUAN_MPKM_20SKS_DAN_PRASYARAT.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 17 | "SKS Diakui: 20 SKS" | "SKS Diakui: 20 SKS (kebijakan lokal prodi — bukan ketetapan Permendikbudristek 53/2023)" | Overclaim — tidak ada dasar hukum |

### 3.13 Perbaikan Dokumen 017

**File:** `017_VERIFIKASI_GROUND_TRUTH_KURIKULUM2025.md`

| Line | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| 141 | "15 (S/KU/P/KK)" | "14 (S/KU/P/KK)" | Error matematika |
| 182 | (tidak ada) | "✅ Koreksi: CPL baru = 14 (bukan 15) — S(1)+KU(3)+P(4)+KK(6) = 14" | Penambahan verifikasi |

### 3.14 Perbaikan Kode MK FST/STI (10 Agustus 2026)

**Konteks:** User menginformasikan bahwa MK terbagi menjadi:
- **MKU**: Mata Kuliah Universitas
- **FST-**: Mata Kuliah Fakultas (11 MK) — fondasi keilmuan lintas prodi FSTI
- **STI-**: Mata Kuliah Wajib Prodi (31 MK) — karakteristik SISTEKIN
- **STA-/STB-/STC-**: MK Pilihan Peminatan (18 MK)

**Dokumen yang diupdate:**

| Dokumen | Perubahan |
|---|---|
| **004** | Tambah catatan kode MK + referensi ke 006/011/012/015 |
| **005** | Tambah tabel kode MK (MKU, FST-, STI-, STA/STB/STC) |
| **006** | Rewrite Section 6: Struktur MK — Kategori & Kode (MKU 6 MK, FST 11 MK, STI 31 MK, Pilihan 18 MK) |
| **007** | Update Ringkasan Total: ~57 MK, ~168 SKS, tambah tabel kode MK |
| **010** | Update Section 5.5: MKWU + MK Fakultas (FST) — 11 MK, 32 SKS |
| **011** | Update Kode Pengenalan, tabel semester, Matriks Prasyarat (terpisah FST & STI), Total SKS |
| **012** | Rewrite total: 66 MK, 168 SKS (Wajib) + 18 MK (Pilihan) — tabel MKU/FST/STI/STA/STB/STC |
| **015** | Update Kode MK, Ringkasan (57 MK, 168 SKS), Detail per Komponen (MKU/FST/STI) |
| **017** | Update catatan untuk 007, 011, 012 |

**Total perubahan:** 9 dokumen terdampak, ~50 baris diupdate

### 3.15 Perbaikan Nama MK (10 Agustus 2026)

**Konteks:** User merevisi nama MK untuk lebih sesuai dengan industri:
- `Pemrograman Web` → `Web Front End Development`
- `Interaksi Manusia dan Komputer (IMK)` → `UI/UX Design`
- `Pemrograman Lanjut dan API` → `Web Back End Development`
- `Penambangan Data dan Visualisasi` → `Data Mining & Visualization`

**Dokumen yang diupdate (Batch 1 — Core):**

| Dokumen | Perubahan |
|---|---|
| **011** | Update nama MK di tabel semester + matriks prasyarat |
| **012** | Update nama MK di matriks CPL vs MK |
| **013** | Update nama MK di tabel praktikum semester ganjil |
| **015** | Update nama MK di tabel perbandingan 2025 vs 2026 |

**Dokumen yang diupdate (Batch 2 — Semua file relevan):**

| Dokumen | Perubahan |
|---|---|
| **004** | Update "Pemrograman Web/Lanjut-API" → "Web Front End/Web Back End Development" |
| **005** | Update 4 MK: Web Front End, UI/UX Design, Web Back End, Data Mining & Visualization |
| **006** | Update "Pemrograman Web, Pemrograman Mobile, Pemrograman API" → nama baru |
| **007** | Update "Penambangan Data & Visualisasi" → "Data Mining & Visualization" |
| **009C** | Update "IMK" → "UI/UX Design" di tabel relevansi |
| **010** | Update 11 baris: semua nama MK lama → nama baru (termasuk di tabel CPL, Semester, KK) |
| **016** | Update 8 baris: prasyarat chain + tabel prasyarat lengkap |

**Total perubahan:** 11 dokumen terdampak, ~30 baris diupdate

### 3.16 Penambahan MK Jaringan Komputer (10 Agustus 2026)

**Konteks:** User memutuskan menambah MK Jaringan Komputer (STI-307) ke Semester 3 sebagai fondasi jaringan sebelum IoT, Cloud, dan Security. Sebelumnya tidak ada MK jaringan dasar di kurikulum.

**Justifikasi:**
- Mahasiswa belajar IoT (sensor, dashboard), Cloud (IaaS/PaaS/SaaS), dan Keamanan (network security) tanpa pemahaman fundamental jaringan
- Jaringan Komputer = prerequisite domain knowledge untuk 6+ MK downstream
- CPL: P3 (Infrastruktur TI), KK3 (Cloud & Security)

**Dokumen yang diupdate:**

| Dokumen | Perubahan |
|---|---|
| **011** | Tambah STI-307 Sem 3 (20 SKS→20 SKS, 7 MK), update Matriks Prasyarat (row 14), update prasyarat STI-404/405, update Total SKS 168→171, Total MK 57→58 |
| **012** | Tambah baris Jaringan Komputer di matriks CPL, update Subtotal STI 31→32 MK, 95→98 SKS, update Grand Total 66→67 MK, 196→199 SKS |
| **013** | Tambah STI-307 di Semester 3 Ganjil, update Total Sem 3 dari 17→20 SKS |
| **015** | Tambah Jaringan Komputer di tabel perbandingan Sem 3, update Total 168→171 SKS, Total MK 57→58 |
| **006** | Tambah Jaringan Komputer di MK Wajib Prodi (31→32 MK, 95→98 SKS) |
| **010** | Tambah di Smart Systems (5.2), CPL P3/KK3 mapping, semester distribution |
| **016** | Tambah di prasyarat chain + tabel prasyarat (tidak ada prasyarat), update statistik |

**Total perubahan:** 7 dokumen terdampak

---

## 4. VERIFIKASI AKHIR

### 4.1 Cek Seluruh Dokumen

| Dokumen | Status | Bukti |
|---|---|---|
| **001** | ✅ FIXED | "Sudah ada 10 CPL" muncul 3 kali |
| **002** | ✅ FIXED | "Sudah ada 10 CPL" muncul 1 kali |
| **004** | ✅ UPDATED | Tambah catatan kode MK + nama MK direvisi |
| **005** | ✅ UPDATED | "DRAFT LAMA — DISEPINGKAN" + kode MK + nama MK direvisi |
| **006** | ✅ UPDATED | "Target Gaji" = 0, Section 6 rewrite + nama MK direvisi + Jaringan Komputer ditambah |
| **007** | ✅ UPDATED | "Sudah ada 10 CPL" + total ~58 MK + nama MK direvisi |
| **008** | ✅ OK | Tidak perlu update (PL, bukan MK) |
| **009** | ✅ FIXED | "14 CPL" muncul 4 kali |
| **009C** | ✅ UPDATED | Nama MK direvisi (IMK → UI/UX Design) |
| **009E** | ✅ FIXED | "14 CPL" muncul 3 kali |
| **010** | ✅ UPDATED | "14 CPL" + Section 5.5 MKWU + FST + nama MK direvisi + Jaringan Komputer (P3, KK3) |
| **011** | ✅ UPDATED | Kode MK + nama MK direvisi + Jaringan Komputer Sem 3 (57→58 MK, 168→171 SKS) |
| **012** | ✅ UPDATED | Rewrite: 67 MK, 199 SKS + nama MK direvisi + Jaringan Komputer CPL P3/KK3 |
| **013** | ✅ UPDATED | Nama MK direvisi + Jaringan Komputer Sem 3 Ganjil (17→20 SKS) |
| **014** | ✅ OK | Dokumen IoT, tidak perlu update kode |
| **015** | ✅ UPDATED | Kode MK + nama MK direvisi, total 58 MK, 171 SKS + Jaringan Komputer |
| **016** | ✅ FIXED | "kebijakan lokal prodi" + Jaringan Komputer di prasyarat chain |
| **017** | ✅ UPDATED | Catatan untuk 007, 011, 012 |
| **018** | ✅ UPDATED | Log perbaikan MK FST/STI + Penambahan Jaringan Komputer (Section 3.16) |

### 4.2 Ringkasan Perubahan

| Kategori | Jumlah Fix | Dokumen Terdampak |
|---|---|---|
| CPL "belum ada" → "sudah ada 10" | 4 fix | 001, 002, 007 |
| CPL count 15 → 14 | 13 fix | 009, 009E, 010, 011, 012, 015, 017 |
| Angka fabricasi dihapus | 4 fix | 001 (17 CPL), 006 (3 gaji) |
| BoK nama salah → benar | 1 fix | 010 (19 BK) |
| Dokumen usang ditandai | 1 fix | 005 |
| Overclaim ditambah catatan | 1 fix | 016 |
| **Kode MK FST/STI update** | **9 dokumen** | 004, 005, 006, 007, 010, 011, 012, 015, 017 |
| **Nama MK direvisi** | **11 dokumen** | 004, 005, 006, 007, 009C, 010, 011, 012, 013, 015, 016 |
| **TOTAL** | **33 fix + 9 update + 11 revisi nama** | **17+ dokumen** |

---

## 5. PELAJARAN UNTUK AGENTIC AI

### 5.1 Pola Error yang Ditemukan

| Pola | Contoh | Pencegahan |
|---|---|---|
| **Hallucination angka** | "rencana 17 CPL" | Selalu verifikasi angka ke sumber |
| **Hallucination nama** | BoK IS2020 nama salah | Selalu kutip dari dokumen asli |
| **Klaim berlebihan** | "20 SKS Magang = legal" | Bedakan kebijakan lokal vs regulasi |
| **Error matematika** | 15 CPL padahal 14 | Selalu hitung ulang |
| **Dokumen usang** | 005 vs 011 | Tandai status dokumen |
| **Copy-paste error** | P2 BoK "AI, ML" | Verifikasi konteks |

### 5.2 Protokol Verifikasi

1. **Selalu cek ground truth** — Baca file asli (PDF) sebelum klaim
2. **Hitung ulang** — Jangan percaya angka tanpa verifikasi
3. **Kutip sumber** — Setiap klaim harus ada referensi
4. **Bedaakan lokal vs regulasi** — Kebijakan prodi bukan hukum nasional
5. **Tandai dokumen usang** — Gunakan status yang jelas

---

## 6. REFERENSI

| Dokumen | Fungsi |
|---|---|
| `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` | Ground truth: struktur kurikulum lama |
| `KURIKULUM2025/Implementasi_MODUL_OBE_SISTEKIN2025.pdf` | Ground truth: CPL + PL lama |
| `017_VERIFIKASI_GROUND_TRUTH_KURIKULUM2025.md` | Verifikasi dokumen vs ground truth |
| `018_AUDIT_TRAIL_PERBAIKAN_DOKUMEN.md` | Dokumen ini — log perbaikan |

---

## 7. LOG PEKERJAAN 10 AGUSTUS 2026

### 7.1 Ringkasan Pekerjaan Hari Ini

**Tanggal:** 10 Agustus 2026
**Durasi:** ~2 jam
**Fokus:** Implementasi Kode MK FST/STI + Update Seluruh Dokumen

### 7.2 Pekerjaan yang Dilakukan

#### A. Update Kode MK FST/STI (Fokus Utama)

User menginformasikan bahwa MK terbagi menjadi:
- **MKU**: Mata Kuliah Universitas (6 MK, 14 SKS)
- **FST-**: Mata Kuliah Fakultas (11 MK, 32 SKS) — fondasi keilmuan lintas prodi FSTI
- **STI-**: Mata Kuliah Wajib Prodi (31 MK, 95 SKS) — karakteristik SISTEKIN
- **STA-/STB-/STC-**: MK Pilihan Peminatan (18 MK, 55 SKS)

**MK FST (11 MK):**
1. Algoritma Pemrograman (FST-101, 3 SKS, +P)
2. Pengantar AI (& Prompt Engineering) (FST-102, 2 SKS) — **MK Baru**
3. Statistika & Probabilitas (FST-103, 3 SKS, +P)
4. Basis Data (FST-104, 3 SKS, +P)
5. Basic English (FST-105, 2 SKS) — **MK Baru**
6. Etika dan Hukum Digital (FST-106, 2 SKS)
7. English For IT Professionals (FST-107, 2 SKS) — **MK Baru**
8. Metodologi Penelitian (FST-108, 3 SKS) — Paralel
9. PKL (FST-109, 3 SKS) — **MK Baru**, Paralel
10. Pra-Skripsi (FST-110, 3 SKS) — Paralel
11. Skripsi (FST-111, 6 SKS) — Paralel

**MBKM:** Program (bukan MK), dapat diakui maks 20 SKS → dikonversikan ke MK semester

#### B. Update Dokumen

| Dokumen | Perubahan Utama |
|---|---|
| **004** | Tambah catatan kode MK + referensi |
| **005** | Tambah tabel kode MK |
| **006** | Rewrite Section 6: Struktur MK — Kategori & Kode |
| **007** | Update Ringkasan Total: ~57 MK, ~168 SKS |
| **010** | Update Section 5.5: MKWU + MK Fakultas (FST) |
| **011** | Update Kode Pengenalan, tabel semester, Matriks Prasyarat, Total SKS, tambah Distribusi Ganjil/Genap |
| **012** | Rewrite total: 66 MK, 168 SKS (Wajib) + 18 MK (Pilihan) |
| **015** | Update Kode MK, Ringkasan, Detail per Komponen |
| **017** | Update catatan untuk 007, 011, 012 |
| **018** | Log perbaikan (section 3.14) + log pekerjaan hari ini |

#### C. Tambah Distribusi Ganjil/Genap di 011

| Komponen | Ganjil (1,3,5,7) | Genap (2,4,6,8) | Total |
|---|---|---|---|
| **MK** | 30 | 26 | 56 (+ 4 Paralel) |
| **SKS** | 82 | 76 | 158 (+ 15 Paralel) |
| **MK +P** | 17 | 10 | 27 |

**MK Paralel (Bisa diambil Ganjil/Genap):**
- Metodologi Penelitian (FST-108, 3 SKS)
- PKL (FST-109, 3 SKS)
- Pra-Skripsi (FST-110, 3 SKS)
- Skripsi (FST-111, 6 SKS)

### 7.3 Total Perubahan Hari Ini

| Kategori | Jumlah |
|---|---|
| Dokumen diupdate | 10 dokumen |
| Baris diupdate | ~100 baris |
| MK FST ditambahkan | 11 MK (7 dari STI + 4 baru) |
| Total MK kurikulum baru | 57 MK |
| Total SKS kurikulum baru | 168 SKS |

### 7.4 Status Akhir Semua Dokumen

| Dokumen | Status | Keterangan |
|---|---|---|
| 001 | ✅ FIXED | CPL "sudah ada 10" |
| 002 | ✅ FIXED | CPL "sudah ada 10" |
| 003 | ✅ OK | Ground truth KURIKULUM2025 |
| 004 | ✅ UPDATED | Tambah kode MK |
| 005 | ✅ UPDATED | DRAFT LAMA + kode MK |
| 006 | ✅ UPDATED | Section 6 rewrite (MKU/FST/STI) |
| 007 | ✅ UPDATED | Total ~57 MK, ~168 SKS |
| 008 | ✅ OK | PL, bukan MK |
| 009 | ✅ FIXED | 14 CPL |
| 009E | ✅ FIXED | 14 CPL |
| 010 | ✅ UPDATED | Section 5.5 MKWU + FST |
| 011 | ✅ UPDATED | Kode MK, tabel, prasyarat, ganjil/genap |
| 012 | ✅ UPDATED | Rewrite: 66 MK, 168 SKS |
| 013 | ✅ OK | Dokumen praktikum |
| 014 | ✅ OK | Dokumen IoT |
| 015 | ✅ UPDATED | Kode MK, total 57 MK, 168 SKS |
| 016 | ✅ FIXED | "kebijakan lokal prodi" |
| 017 | ✅ UPDATED | Catatan untuk 007, 011, 012 |
| 018 | ✅ UPDATED | Log perbaikan + log pekerjaan |

### 7.5 Pelajaran Hari Ini

1. **Kode MK harus konsisten** — Perubahan kode (MKP→STI, MKL→STA/STB/STC, tambah FST) harus diupdate ke seluruh dokumen
2. **MK Fakultas vs MK Prodi** — MK FST (Fakultas) adalah fondasi keilmuan lintas prodi, berbeda dari MK STI (Prodi) yang spesifik SISTEKIN
3. **MK Paralel** — Metodologi Penelitian, PKL, Pra-Skripsi, Skripsi bisa diambil di Ganjil atau Genap
4. **MBKM = Program, bukan MK** — Dapat diakui maks 20 SKS → dikonversikan ke MK semester
5. **Total akhir:** 59 MK | 171 SKS | 14 CPL | 3 Peminatan | 14 MK FSTI (37 SKS)

---

### 7.6 Update Ketentuan Baru FSTI (13 Agustus 2026)

- **Ketentuan MK FSTI Disesuaikan (14 MK, 37 SKS):**
  - Dasar Teknologi Digital (FST-101, 2 SKS, Sem 1)
  - Algoritma pemrograman (+P) (FST-102, 3 SKS, Sem 1)
  - Struktur Data dan Strategi Algoritma (+P) (FST-203, 3 SKS, Sem 2)
  - Pengantar kecerdasan Artifisial & Data (FST-204, 3 SKS, Sem 2)
  - Basic English (FST-205, 2 SKS, Sem 2)
  - Etika dan Hukum Digital (FST-206, 2 SKS, Sem 2)
  - Basis Data (+P) (FST-207, 3 SKS, Sem 2)
  - Statistika & Probabilitas (+P) (FST-408, 3 SKS, Sem 4)
  - English For IT Professionals (FST-409, 2 SKS, Sem 4)
  - Capstone Project (+P) (FST-610, 3 SKS, Sem 6)
  - Metpen (FST-611, 2 SKS, Sem 6-7, >76 SKS)
  - PKL (FST-612, 3 SKS, Sem 6-7, >100 SKS)
  - Pra-Skripsi (FST-613, 2 SKS, Sem 6-7-8, >100 SKS)
  - Skripsi (FST-714, 6 SKS, Sem 7-8, >120 SKS)
- **Status Dokumen Terupdate:** `006`, `007`, `010`, `011`, `012`, `015`, `018`, `README.md`, `006.xlsx`, `011.xlsx` (Semua terharmonisasi ke **171 SKS / 14 MK FSTI**).

---

*Dokumen ini merupakan audit trail lengkap perbaikan dokumen kurikulum SISTEKIN untuk penelusuran dan verifikasi berjenjang.*

