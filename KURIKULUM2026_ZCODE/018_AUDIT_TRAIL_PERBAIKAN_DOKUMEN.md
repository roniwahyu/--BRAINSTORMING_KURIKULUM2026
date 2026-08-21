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
5. **Total akhir:** 61 MK | 170 SKS | 14 CPL | 3 Peminatan | 14 MK FSTI (36 SKS)

---

### 7.6 Update Ketentuan Baru FSTI (13 Agustus 2026)

- **Ketentuan MKWU Disesuaikan (8 MK, 14 SKS):**
  - Agama I (MKU-101, 2 SKS, Sem 1)
  - Pancasila (MKU-102, 2 SKS, Sem 1)
  - Bahasa Indonesia (MKU-103, 2 SKS, Sem 1)
  - Agama II (MKU-201A, **0 SKS**, Sem 2 — Kebijakan UWG)
  - Kewarganegaraan (MKU-201, 2 SKS, Sem 2)
  - Kewirausahaan I (MKU-202, 2 SKS, Sem 2)
  - Kewirausahaan II (MKU-402, **0 SKS**, Sem 4 — Kebijakan UWG)
  - KKN (MKU-203, 3 SKS, Libur Antar Sem)
- **Status Dokumen Terupdate:** `006`, `007`, `010`, `011`, `012`, `015`, `018`, `README.md`, `006.xlsx`, `011.xlsx` (Semua terharmonisasi ke **170 SKS / 14 MK FSTI / 8 MKWU**).

---

### 7.7 Update 4 Ketentuan Spesifik MK & Pertukaran Semester (13 Agustus 2026)

1. **Pengantar Kecerdasan Artifisial & Data (`FST-204`):**
   - Diubah dari 3 SKS → **2 SKS**.
   - Berstatus **Mata Kuliah Teori (Non-+P)**.
2. **Probabilitas dan Statistika (`FST-408`):**
   - 3 SKS.
   - Berstatus **Mata Kuliah Teori (Non-+P)**.
3. **Capstone Project (`FST-610`):**
   - 3 SKS, **MK Paralel (Semester 6, 7, 8)**.
4. **UI/UX Design & Prototyping (`STI-303`):**
   - Nomenklatur disempurnakan menjadi **UI/UX Design & Prototyping** (3 SKS).
   - Berstatus **Mata Kuliah Praktikum (+P: ✅)** (Figma design system, interactive prototyping & usability testing).
5. **Pertukaran Posisi Web Back End & APSI:**
   - **Web Back End Development (`STI-407`, 3 SKS, +P)** dipindahkan ke **Semester 4** (setelah *Web Front End Development* di Sem 3 & *Basis Data* di Sem 2).
   - **Analisis dan Perancangan Sistem Informasi (`STI-301`, 3 SKS)** dipindahkan ke **Semester 3** (selevel dengan *RPL* & *UI/UX Design & Prototyping*).
6. **Agama II (0 SKS) Dipindahkan ke Semester 4:**
   - `Agama II` (`MKU-401A`, 0 SKS) dipindahkan dari Semester 2 ke **Semester 4** bersamaan dengan `Kewirausahaan II` (0 SKS). (Beban SKS Sem 2 & Sem 4 tetap 22 SKS).
7. **Seminars / Pra-Skripsi (`FST-613`, 2 SKS) Menjadi Paket Tugas Akhir Paralel:**
   - `Seminars` dipindahkan dari Semester 5 menjadi **MK Paralel (Semester 6, 7, 8)** tempat mahasiswa menyusun dan mendesiminasikan Proposal Skripsi sebelum/bersamaan dengan pengambilan *Skripsi*.
8. **Sistem Cerdas (`STI-302`, 2 SKS, Sem 3) Ditetapkan Teori (Non-+P):**
   - Berstatus **Mata Kuliah Teori / Non-Praktikum** sebagai fondasi konsep AI (expert systems, fuzzy logic, rule-based systems).
9. **Keamanan Informasi Dasar (`STI-305`, 3 SKS) Dipindahkan ke Semester 3:**
   - Dipindahkan dari Semester 4 ke **Semester 3** (selevel dengan *Jaringan Komputer* & *RPL*).
10. **IoT (`STI-504`, 3 SKS, +P) & Pemrograman Mobile (`STI-505`, 3 SKS, +P) Dipindahkan ke Semester 5:**
    - **Internet of Things (IoT)** dipindahkan dari Semester 3 ke **Semester 5** (setelah mahasiswa menempuh *Jaringan Komputer* di Sem 3).
    - **Pemrograman Aplikasi Mobile** dipindahkan dari Semester 4 ke **Semester 5** (setelah *Web Front End* di Sem 3 & *Web Back End* di Sem 4).
    - **Beban Semester 5:** 21 SKS (7 MK: Deep Learning, DW-BI, Data Mining, IoT, Mobile, 2 MK Pilihan Peminatan).
### 7.9 Penyeimbangan 3 Peminatan, Batas 20 SKS Sem 2 (Kewarganegaraan ke Sem 4) & Penambahan Sistem Operasi (17 Agustus 2026)

1. **Penyesuaian Semester 2 Menjadi Tepat 20 SKS:**
   - Memindahkan `MKU-401 Kewarganegaraan` (2 SKS) dari Semester 2 ke **Semester 4 (Genap)** agar patuh Permendikbudristek No. 53/2023 Pasal 18 (batas maksimal 20 SKS di 2 semester pertama).
   - Mempertahankan `FST-206 Etika dan Hukum Digital` (2 SKS) di **Semester 2** agar mahasiswa mendapatkan pemahaman regulasi privasi data (UU PDP/GDPR) bersamaan dengan *Basis Data* dan *AI*.
2. **Penambahan Kembali MK Sistem Operasi:**
   - Memasukkan kembali `STI-305 Sistem Operasi` (3 SKS) ke **Semester 3 (Ganjil)** sebagai fondasi BoK IT2017/IS2020 infrastruktur sebelum Cloud dan Keamanan.
3. **Reposisi Conversational AI & Smart Surveillance:**
   - Menggeser `Conversational AI` (3 SKS, +P) dan `Smart Surveillance` (3 SKS, +P) dari MK Wajib menjadi **MK Pilihan Peminatan P1 (Integrated Smart Systems)**.
4. **Penyeimbangan 3 Peminatan (@ 6 MK / 18 SKS):**
   - Menetapkan portofolio peminatan yang seimbang secara proporsional: P1 (6 MK / 18 SKS), P2 (6 MK / 18 SKS), dan P3 (6 MK / 18 SKS). Mahasiswa mengambil 9 MK pilihan (27 SKS) di Semester 5 s.d. 7.
5. **Kewirausahaan I Tetap 2 SKS:**
   - Mempertahankan `MKU-202 Kewirausahaan I` (2 SKS) di Semester 2 untuk penguatan pilar VMTS 2045.

### 7.10 Penegasan Batasan Keilmuan & Fokus Silabus MK EdTech dan FinTech pada Peminatan P3 (17 Agustus 2026)

1. **Klarifikasi Batasan (*Distinctive Boundary*) vs Bisnis Digital:**
   - Mata kuliah `STC-02 EdTech Platform Development` (3 SKS, +P) dan `STC-03 FinTech Platform Development` (3 SKS, +P) pada Peminatan P3 (*Digital Platform Engineering*) ditegaskan berfokus pada **rekayasa arsitektur sistem dan integrasi API (*Platform Engineering*)**, bukan pada model bisnis atau pemasaran digital (ranah Bisnis Digital).
2. **Fokus Silabus & Keterlacakan BoK/CPL:**
   - **EdTech:** Arsitektur LMS, standar SCORM/LTI/xAPI, gamification logic engine, adaptive quiz algorithms, dan Learning Analytics API.
   - **FinTech:** Integrasi Payment Gateway (Midtrans/Xendit/Stripe), transaction double-entry ledger & idempotency, PCI-DSS security compliance, dan decentralized smart contract ledger.
   - **CPL & BoK:** Memenuhi CPL KK5 (Platform Skalabel) dan KK6 (Inovasi Startup) serta BoK IS2020 (BK07, BK09, BK17) dan BoK IT2017 (*Platform Technologies*).
3. **Harmonisasi Prasyarat:**
   - Ditetapkan prasyarat berjenjang: `STI-306 Web Front End` (Sem 3), `STI-407 Web Back End` (Sem 4), dan `FST-207 Basis Data` (Sem 2).

---

### 7.11 [DECISION FINAL — RESOLVED] Keputusan Restrukturisasi Peminatan P3: Penetapan STC-02 "Rekayasa & Otomasi Proses Bisnis" & Konsolidasi STC-03 (17 Agustus 2026)

> ✅ **Status: FINAL & TERKUNCI (Disetujui User).**  
> Keputusan ini menyelesaikan gap kritis `SI-BK15` dan menuntaskan redundansi pemrograman di Peminatan P3.

#### Ringkasan Keputusan:
1. **Penetapan MK Baru `STC-02 Rekayasa & Otomasi Proses Bisnis` (3 SKS, +P, Semester 5/6/7):**
   - **Nama Bahasa Inggris:** *Business Process Engineering & Automation*
   - **Level Kualifikasi:** Jenjang Sarjana (S1) Akademik-Rekayasa (KKNI Level 6), bukan vokasi/D4.
   - **Fokus Keilmuan:** Pemodelan formal proses bisnis (BPMN 2.0 / Petri Nets), *process mining*, optimasi metrik *throughput*, dan rekayasa orkestrasi alur kerja terdistribusi (*workflow orchestration engine* & integrasi API enterprise).
   - **Dampak Akreditasi:** **Menutup Gap Kritis `SI-BK15` (Business Process Management)** sehingga kurikulum SISTEKIN kini **100% memenuhi 19/19 Bahan Kajian IS2020 APTIKOM**.
2. **Konsolidasi EdTech & FinTech menjadi `STC-03 Rekayasa Aplikasi Industri Vertikal` (3 SKS, +P):**
   - Menghilangkan duplikasi arsitektur CRUD/API berulang antara EdTech dan FinTech.
   - Tetap mengajarkan domain studi kasus riil (*payment gateway, learning management, digital ledger*) dalam 1 MK yang padat dan fokus.
3. **Portofolio Peminatan P3 Menjadi Tepat 6 MK (18 SKS):**
   - `STC-01`: User Experience Research & Design (3 SKS, +P)
   - `STC-02`: Rekayasa & Otomasi Proses Bisnis (3 SKS, +P) ⭐
   - `STC-03`: Rekayasa Aplikasi Industri Vertikal (3 SKS, +P)
   - `STC-04`: Immersive Media & XR Development (3 SKS, +P)
   - `STC-05`: SaaS Architecture & Multi-Tenancy (3 SKS, +P)
   - `STC-06`: Digital Product Management & Agile Practices (3 SKS)

### 7.12 Penerbitan Dokumen 022: Audit Kritis Beban BoK, Tumpang Tindih Terselubung & Mitigasi Pedagogis (18 Agustus 2026)

1. **Konteks & Tujuan:**
   - Melakukan *stress-testing audit* menyeluruh pasca-penyelarasan makro kurikulum SISTEKIN 2026.
   - Hasil audit didokumentasikan resmi di **`022_AUDIT_KRITIS_BEBAN_BOK_DAN_KELEMAHAN_KURIKULUM2026.md`**.
2. **Empat Temuan & Rekomendasi Utama:**
   - **BoK Over-Saturation:** Mitigasi 15 SKS Matematika (`SI-BK11`) dengan pendekatan *Computational Mathematics* menggunakan Python/NumPy.
   - **Subtle Overlaps:** Menetapkan garis batas tegas antara *DW-BI* (Infrastruktur Data) vs *Data Mining* (Pola & Clustering) di Semester 5, serta *Integrasi AI* (Serving API) vs *Platform Eng* (Enterprise Plumbing).
   - **Semester 5 Overload Trap:** Mengidentifikasi risiko 5 MK Wajib Praktikum (+P) serempak; merekomendasikan *Integrated Project Assignment* (IoT + Mobile) dan relaksasi format praktikum di DW-BI/Data Mining.
   - **Operational Feasibility:** Pedoman pemanfaatan GPU cloud akademis dan kit IoT mandiri mahasiswa.
3. **Dokumen Terdampak & Terbuat:**
### 7.13 Pertukaran Posisi Semester: Data Warehouse & BI (Sem 4) ↔ Manajemen Proyek TI (Sem 5) (18 Agustus 2026)

1. **Konteks Masalah:**
   - Evaluasi pedagogis Dokumen [022] menemukan bahwa Semester 5 mengalami beban berlebih (*Semester 5 Overload Trap*) dengan 5 MK Praktikum Lab Wajib sekaligus. Selain itu, *DW-BI* dan *Data Mining* berada di semester yang sama sehingga materi ETL/Dashboard tumpang tindih.
2. **Keputusan Perubahan Disetujui:**
   - **`STI-402 Data Warehouse & Business Intelligence` (3 SKS, +P):** Dipindahkan dari Semester 5 ke **Semester 4 (Genap)**. Mahasiswa mempelajari gudang data segera setelah *Basis Data (Sem 2)* dan bersinergi dengan *Machine Learning (Sem 4)*.
   - **`STI-506 Manajemen Proyek Teknologi Informasi` (3 SKS, Non-+P):** Dipindahkan dari Semester 4 ke **Semester 5 (Ganjil)**. Mahasiswa mempelajari metodologi Agile/Scrum tepat 1 semester sebelum mengeksekusi *Capstone Project (FST-610)* di Semester 6.
3. **Dampak Positif:**
   - **Semester 4:** Beban 19 SKS menjadi sangat seimbang dengan 3 MK Lab (+P) + 4 MK Teori + MKWU.
   - **Semester 5:** Beban 21 SKS terselamatkan dari kejenuhan lab (menjadi 4 MK Lab + 1 MK Teori-Manajerial + 2 MK Pilihan).
   - **Alur Belajar Data:** Menjadi berjenjang sempurna: $\text{Basis Data (Sem 2)} \rightarrow \text{Data Warehouse (Sem 4)} \rightarrow \text{Data Mining (Sem 5)}$.
### 7.14 Penerbitan Dokumen 023: Formulasi 4 Matriks OBE Tingkat Lanjut (18 Agustus 2026)

1. **Konteks & Kebutuhan Standar Akreditasi:**
   - Melengkapi seluruh matriks kurikulum berbasis OBE sesuai standar instrumen Akreditasi LAM INFOKOM (Kriteria 9) dan standar internasional IABEE/ABET.
2. **Empat Matriks Baru yang Diformulasikan:**
   - **Matriks 1:** Matriks CPL $\leftrightarrow$ Mata Kuliah Berbasis Level Penguasaan (*Mastery Levels: Introduce / Reinforce / Master — I-R-M* & Taksonomi Bloom C2–C6).
   - **Matriks 2:** Matriks 2-Dimensi Formal Pemenuhan 19 Bahan Kajian IS2020 (`SI-BK01`–`SI-BK19`) dan 27 Bahan Kajian IT2017 (`TI-BK01`–`TI-BK27`) terhadap 61 Mata Kuliah.
   - **Matriks 3:** Matriks Keterlacakan Komprehensif (*End-to-End Traceability*: VMTS 2045 $\rightarrow$ 3 PEO $\rightarrow$ 6 PL $\rightarrow$ 14 CPL $\rightarrow$ 3 Peminatan $\rightarrow$ Target Karier).
   - **Matriks 4:** Matriks Rencana Asesmen Langsung CPL (*CPL Direct Assessment & Benchmark Mapping Matrix*) untuk sistem penjaminan mutu PPEPP.
### 7.15 Penerbitan Dokumen 024, 025, 026, dan 027: Formulasi Lengkap PL, CPL, CPMK & Sub-CPMK Seluruh 61 MK (18 Agustus 2026)

1. **Konteks & Standar Konstruksi:**
   - Menyusun capaian pembelajaran mikro (*Micro-Level Learning Outcomes*) untuk seluruh 61 Mata Kuliah portofolio SISTEKIN 2026.
   - Menggunakan formula **ABCD** (*Audience, Behavior, Condition, Degree*) dan kata kerja operasional **Taksonomi Bloom (C2–C6, P2–P5, A2–A5)**.
2. **Pembagian Dokumen Terbit:**
   - **`024_FORMULASI_CPMK_SUB_CPMK_SEMESTER_1_DAN_2.md`:** 16 MK Fondasi (FSTI, STI & MKWU — Algoritma, Kalkulus, Diskrit, Basis Data, Aljabar, AI Dasar, Etika Digital).
   - **`025_FORMULASI_CPMK_SUB_CPMK_SEMESTER_3_DAN_4.md`:** 17 MK Inti (APSI, Sistem Cerdas, UI/UX, RPL, OS, Jarkom, Web FE, ML, DW-BI, Web BE, Cloud, Keamanan Dasar, Probstat, English IT, KWN).
   - **`026_FORMULASI_CPMK_SUB_CPMK_SEMESTER_5_DAN_6.md`:** 10 MK Wajib Lanjut & Integrasi (Deep Learning, Data Mining, IoT, Mobile Dev, Manpro TI, Integrasi AI, Smart City, Keamanan Lanjut, Capstone FSTI, Metpen).
### 7.16 Penerbitan Dokumen 028: Contoh Rencana Pembelajaran Semester (RPS) Terstandar OBE (18 Agustus 2026)

1. **Konteks & Tujuan:**
   - Menyediakan dokumen contoh operasional RPS *ready-to-implement* yang mematuhi standar LAM INFOKOM, IABEE, dan Kepmendikbud No. 53/2023.
### 7.17 Penerbitan Dokumen 029: Panduan Sistem Asesmen, Evaluasi & Penjaminan Mutu Berbasis OBE (18 Agustus 2026)

1. **Konteks & Kepatuhan Standar Akreditasi:**
   - Menyusun kerangka kerja operasional asesmen berbasis luaran (*Outcome-Based Assessment*) yang mematuhi standar LAM INFOKOM (Kriteria 9), IABEE, dan IKU 7 (Case Method & PjBL $\ge 50\%$).
2. **Komponen Inti Panduan Asesmen:**
   - **Arsitektur Asesmen:** Direct Assessment (85%) & Indirect Assessment (15%).
   - **Formula Matematis CPL Attainment:** Algoritma perhitungan ketercapaian Sub-CPMK $\rightarrow$ CPMK $\rightarrow$ CPL per mata kuliah $\rightarrow$ Akumulasi CPL seluruh masa studi.
   - **Standar Ambang Batas (*Threshold*):** Target kelulusan CPL $\ge 70.0$ (Grade B) dengan capaian minimal kohort $\ge 75\%$.
   - **4 Rubrik Analitik Master:** Rubrik PjBL Proyek Terpadu, Rubrik Case Method, Rubrik Sidang Skripsi (`FST-714`), dan Rubrik Capstone Project (`FST-610`).
   - **Siklus PPEPP / CQI:** Manajemen perbaikan mutu berkelanjutan berbasis evaluasi semesteran.
   - **Portofolio Lulusan:** Profil Radar Chart Ketercapaian CPL sebagai lampiran resmi SKPI.
3. **Dokumen Terbit:**
   - `029_PANDUAN_SISTEM_ASESMEN_DAN_EVALUASI_OBE_SISTEKIN.md`.

---

### 7.18 Rekonsiliasi Matematis Total SKS & Penataan Struktur Semester Tingkat Akhir (19 Agustus 2026)

1. **Audit & Rekonsiliasi Matematis Total SKS (Dokumen 030):**
   - Mengoreksi seluruh ketidakcocokan agregat lama:
     - **MKWU:** 8 MK (13 SKS, karena Agama II & KWU II berbobot 0 SKS).
     - **FSTI:** 14 MK (38 SKS, dengan FST-204 berbobot 2 SKS).
     - **STI Wajib Inti:** 27 MK (77 SKS, setelah pengalihan Struktur Data, Basis Data, dan Statistika ke FSTI).
     - **MK Pilihan Peminatan Ditempuh:** 6 MK (18 SKS — tepat 1 paket peminatan penuh @ 6 MK / 18 SKS).
     - **Paket Ditempuh Mahasiswa:** **55 MK / 146 SKS** (Memenuhi syarat kelulusan minimal 144 SKS Permendikbudristek No. 53/2023).
     - **Portofolio Ditawarkan:** **67 MK / 182 SKS** (49 MK Wajib 130 SKS + 18 MK Pilihan P1-P3 54 SKS).
2. **Keputusan Penataan Struktur Semester Tingkat Akhir (Dokumen 031):**
   - **`MKU-203 KPM (KKN Digital)` (3 SKS):** Dipindahkan dari Semester 8 ke **Semester 5** agar pengabdian masyarakat tuntas lebih awal dan tidak mengganggu penyusunan Tugas Akhir.
   - **`STI-604 Digital Platform Engineering` (3 SKS, +P):** Dipindahkan dari Semester 7 ke **Semester 6** sehingga dikuasai sebelum eksekusi Capstone & Startup di Semester 7.
   - **`FST-610 Capstone Project FSTI` (3 SKS, +P):** Dipindahkan dari Semester 6 ke **Semester 7** sebagai puncak proyek rekayasa kolaboratif bersamaan dengan PKL & Startup Digital.
   - **`FST-613 Pra-Skripsi / Seminars` (2 SKS):** Dipindahkan dari Semester 8 ke **Semester 7** agar mahasiswa menyelesaikan proposal penelitian dan lulus Sempro di Semester 7.
   - **`FST-714 Skripsi / Tugas Akhir` (6 SKS, +P):** Ditempatkan di **Semester 8** sebagai *Single Track* murni (6 SKS) sehingga fokus kelulusan tepat waktu ($\le 4$ tahun) optimal.
### 7.19 Penerbitan Dokumen 032: Distribusi Final 55 Mata Kuliah 8 Semester SISTEKIN (20 Agustus 2026)

1. **Konteks & Tujuan:**
   - Menyediakan dokumen definitif tabel 8 semester (*clean, locked, zero-conflict*) yang siap dicantumkan langsung sebagai Lampiran Keputusan Resmi SK Rektor tentang Kurikulum SISTEKIN 2026.
2. **Karakteristik & Rincian Dokumen 032:**
   - **Tabel 8 Semester:** Memuat rincian 55 mata kuliah paket ditempuh (146 SKS) dengan kode mata kuliah, bobot SKS, tipe (+P/Teori/Praktik/Proyek/Seminar/Mandiri), kategori (MKWU/FSTI/Core STI/Elektif), pemetaan CPL utama, dan prasyarat akademik.
   - **Tabel Portofolio Peminatan:** Memuat rincian 18 MK elektif yang ditawarkan di SIAKAD (54 SKS) untuk 3 peminatan seimbang (P1, P2, P3).
   - **Rekapitulasi Komponen:** MKWU (13 SKS / 8 MK), FSTI (38 SKS / 14 MK), Core STI (77 SKS / 27 MK), dan Peminatan Ditempuh (18 SKS / 6 MK).
   - **Klausul Kepatuhan Regulasi:** Kepatuhan batas beban $\le 20\text{ SKS}$ pada Semester 1 (19 SKS) dan Semester 2 (20 SKS) serta pelampauan ambang batas nasional kelulusan $\ge 144\text{ SKS}$ (Permendikbudristek No. 53 Tahun 2023).
### 7.22 Penerbitan Dokumen 034: Analisis Restrukturisasi 4 Profil Lulusan & 3 PEO (20 Agustus 2026)

1. **Konteks & Tujuan:**
   - Menyusun analisis strategis restrukturisasi Profil Lulusan dari model 6 PL lama menjadi **4 Profil Lulusan Utama (PL-1 s.d. PL-4)** dan merumuskan **3 Butir PEO Berbasis Peran Karier (*Role-Based*)** sesuai rekomendasi Buku Panduan Kurikulum OBE APTIKOM SI v2.0 & TI 2023, standar IABEE, dan instrumen akreditasi LAM INFOKOM Kriteria 1 & 9.
2. **Karakteristik Dokumen 034:**
   - **4 Profil Lulusan (PL):** PL-1 (*Intelligent IS & Data/AI Engineer*), PL-2 (*Cloud, Cyber & Smart Systems Integrator*), PL-3 (*UI/UX Designer & Platform Engineer*), dan PL-4 (*Digital Technopreneur & IT Product Innovator*).
   - **3 Butir PEO Role-Based:** PEO-1 (*Jalur Profesional / Praktisi Industri*), PEO-2 (*Jalur Technopreneur & Startup*), PEO-3 (*Jalur Peneliti / Akademisi / Lifelong Learner*).
   - **Matriks Keterlacakan:** Pemetaan eksplisit VMTS 2045 $\leftrightarrow$ 3 PEO $\leftrightarrow$ 4 PL $\leftrightarrow$ 14 CPL.
   - **Roadmap Penajaman:** Panduan teknis bagi sesi/sub-agent berikutnya untuk memperbarui Dokumen 008, 033, dan menyusun kuesioner *tracer study* Buku Kurikulum.
3. **Dokumen Terbit:**
   - `034_ANALISIS_RESTRUKTURISASI_4_PROFIL_LULUSAN_DAN_3_PEO.md`.

---

*Dokumen ini merupakan audit trail lengkap perbaikan dokumen kurikulum SISTEKIN untuk penelusuran dan verifikasi berjenjang.*






