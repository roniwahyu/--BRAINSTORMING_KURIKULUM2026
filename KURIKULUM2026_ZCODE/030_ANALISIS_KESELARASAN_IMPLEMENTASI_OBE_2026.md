# 030 — ANALISIS KESELARASAN & REKONSILIASI DOKUMEN KURIKULUM OBE SISTEKIN 2026

**Tanggal:** 19 Agustus 2026 (Rekonsiliasi Matematis Final — Updated)  
**Peran:** Arsitek Kurikulum & Asesor LAM INFOKOM / IABEE  
**Sumber Rujukan (cross-checked & reconciled):** Dokumen `006` s.d. `031` `KURIKULUM2026_ZCODE`, `Implementasi_Modul_OBE_SISTEKIN2026_TABLES.md`, dan `Implementasi_Modul_OBE_SISTEKIN2026.xlsx`  
**Status:** Laporan Audit Keselarasan & Berita Acara Rekonsiliasi Numerik Resmi  
**Prinsip Audit:** *Artifact-Based Verification*, *Zero Hallucination*, *Mathematical Rigor*, *Constructive Alignment*.

---

## 1. RINGKASAN REKONSILIASI NUMERIK RESMI

Setelah dilakukan audit matematis menyeluruh terhadap daftar baris mata kuliah di seluruh tabel semester Dokumen `011_STRUKTUR_KURIKULUM_TABEL.md`, `012_MATRIKS_CPL_vs_MK.md`, `020_ANALISIS_KESELARASAN_KURIKULUM_OBE_SISTEKIN.md`, dan `031_PENYESUAIAN_STRUKTUR_SEMESTER_5_7_8_DAN_TA.md`, seluruh ketidakcocokan hitungan lama telah **terekonsiliasi dan disinkronkan 100%**.

### Tabel Rekonsiliasi Komponen Kurikulum 2026 (Angka Terkunci & Bersih)

| Komponen Kurikulum | Jumlah MK Ditawarkan | SKS Ditawarkan | Jumlah MK Wajib Ditempuh | SKS Wajib Ditempuh | Keterangan & Status Validasi |
|---|:---:|:---:|:---:|:---:|---|
| **Mata Kuliah Umum Universitas (MKWU)** | **8 MK** | **13 SKS** | **8 MK** | **13 SKS** | 6 MK ber-SKS (13 SKS: Agama I 2, Pancasila 2, B.Indo 2, KWU I 2, KWN 2, KPM 3 di Sem 5) + 2 MK @ 0 SKS kebijakan UWG (Agama II & KWU II). |
| **Mata Kuliah Bersama Fakultas (FSTI)** | **14 MK** | **38 SKS** | **14 MK** | **38 SKS** | Fondasi saintek & keahlian lintas prodi (incl. FST-204 Pengantar AI @ 2 SKS, Metpen 2 SKS di Sem 6, Capstone 3 SKS di Sem 7, PKL 3 SKS di Sem 7, Pra-Skripsi 2 SKS di Sem 7, Skripsi 6 SKS di Sem 8). |
| **Mata Kuliah Wajib Inti Prodi (STI)** | **27 MK** | **79 SKS** | **27 MK** | **79 SKS** | Inti keilmuan SISTEKIN (Sem 1: 8 SKS, Sem 2: 6 SKS, Sem 3: 20 SKS, Sem 4: 15 SKS, Sem 5: 15 SKS, Sem 6: 12 SKS incl. Platform Eng, Sem 7: 3 SKS Startup). |
| **Mata Kuliah Pilihan Peminatan (STA/B/C)** | **18 MK** | **54 SKS** | **6 MK** | **18 SKS** | 3 Peminatan Seimbang (@ 6 MK / 18 SKS); Mahasiswa mengambil tepat 1 paket peminatan penuh (6 MK: 1 di Sem 5, 2 di Sem 6, 3 di Sem 7). |
| **SUBTOTAL WAJIB DITEMPUH** | **49 MK** | **130 SKS** | **49 MK** | **130 SKS** | **Fondasi & Inti Wajib Kurikulum** |
| **GRAND TOTAL PAKET 8 SEMESTER** | **55 MK** | **148 SKS** | **55 MK** | **148 SKS** | **Beban Paket Terjadwal (Syarat Lulus Minimal = 144 SKS Permendikbud 53/2023)** |
| **GRAND TOTAL PORTOFOLIO DITAWARKAN** | **67 MK** | **184 SKS** | — | — | **Total Seluruh Opsi Portofolio MK yang Ditawarkan Prodi** |

---

## 2. HASIL AUDIT PENATAAN STRUKTUR AKHIR & RESOLUSINYA

| # | Temuan Masalah Lama | Akar Penyebab (*Root Cause*) | Tindakan Koreksi & Resolusi Final | Status |
|:---:|---|---|---|:---:|
| 1 | **Klaim STI Wajib "30 MK / 93 SKS" vs Realita** | Pada draf awal Dokumen 006, 3 MK (Struktur Data, Basis Data, Statistika) masih berkode STI. Saat dialihkan ke FSTI (`FST-203`, `FST-207`, `FST-408`), jumlah MK STI berkurang dari 30 MK menjadi **27 MK (79 SKS)**, namun teks narasi ringkasan lama tidak diperbarui. | Dokumen 011, 012, 020, dan 031 telah diperbarui resmi: **STI Wajib Inti = 27 MK (79 SKS)**. | ✅ Tuntas |
| 2 | **Klaim FSTI "36 / 37 SKS" vs Penjumlahan Baris** | Header Dokumen 011 sempat menulis 37 SKS dan summary menulis 36 SKS, sedangkan penjumlahan 14 MK riil adalah $2+3+3+2+2+2+3+3+2+3+2+3+2+6 = \mathbf{38\text{ SKS}}$. | Seluruh dokumen (011, 012, 020, 030, 031) diseragamkan: **FSTI = 14 MK (38 SKS)** dengan `FST-204` = 2 SKS. | ✅ Tuntas |
| 3 | **Klaim MKWU "14 SKS" vs Penjumlahan Baris** | Penjumlahan 8 MKWU riil adalah $2+2+2+2+2+0+0+3 = \mathbf{13\text{ SKS}}$ (karena Agama II & KWU II berbobot 0 SKS). Ringkasan lama salah menjumlahkan menjadi 14 SKS. | Seluruh dokumen diseragamkan: **MKWU = 8 MK (13 SKS)**. | ✅ Tuntas |
| 4 | **Anomali Footer Semester 4 (Klaim 19 SKS vs Riil 22 SKS)** | Pergeseran `MKU-401 Kewarganegaraan` (2 SKS) dan `STI-402 DW-BI` (3 SKS) ke Semester 4 menambah beban riil menjadi 22 SKS, namun footer tabel Dokumen 011 tertinggal di angka 19 SKS. | Footer Semester 4 di Dokumen 011 dan 020 diperbarui menjadi **22 SKS** (8 MK ber-SKS + 2 MK @ 0 SKS). | ✅ Tuntas |
| 5 | **Penataan Runtun Riset & Capstone (Dok. 031)** | Perlunya sekuens riset yang kokoh agar mahasiswa lulus tepat waktu $\le 4$ tahun. | **Metpen (Sem 6) $\rightarrow$ Pra-Skripsi (Sem 7) $\rightarrow$ Skripsi Murni (Sem 8, 6 SKS)**; KPM digeser ke Sem 5; Capstone FSTI di Sem 7; Digital Platform Eng di Sem 6. | ✅ Tuntas |

---

## 3. DISTRIBUSI BEBAN 8 SEMESTER TERVALIDASI (148 SKS TERJADWAL)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   DISTRIBUSI BEBAN PER SEMESTER KURIKULUM SISTEKIN 2026                │
├────────────┬────────────────────────────┬─────────────────────────────┬────────────────┤
│ Semester   │ MK Wajib (MKWU + FST + STI)│ MK Pilihan Peminatan        │ Total SKS      │
├────────────┼────────────────────────────┼─────────────────────────────┼────────────────┤
│ Semester 1 │ 8 MK Wajib (19 SKS)        │ —                           │ 19 SKS (≤20) ✅│
│ Semester 2 │ 8 MK Wajib (20 SKS)        │ —                           │ 20 SKS (≤20) ✅│
│ Semester 3 │ 7 MK Wajib (20 SKS)        │ —                           │ 20 SKS         │
│ Semester 4 │ 8 MK + 2 MK @ 0 SKS (22 SKS)│ —                          │ 22 SKS         │
│ Semester 5 │ 6 MK Wajib (18 SKS - KPM)  │ 1 MK Pilihan (3 SKS)        │ 21 SKS         │
│ Semester 6 │ 5 MK Wajib (14 SKS - Platf)│ 2 MK Pilihan / MBKM (6 SKS) │ 20 SKS         │
│ Semester 7 │ 4 MK Wajib (11 SKS - Capst)│ 3 MK Pilihan / MBKM (9 SKS) │ 20 SKS         │
│ Semester 8 │ 1 MK Wajib (6 SKS - Skrips)│ —                           │ 6 SKS (Murni)  │
├────────────┼────────────────────────────┼─────────────────────────────┼────────────────┤
│ TOTAL      │ 49 MK Wajib (130 SKS)      │ 6 MK Pilihan (18 SKS)       │ 148 SKS Paket  │
└────────────┴────────────────────────────┴─────────────────────────────┴────────────────┘
* Beban kelulusan mahasiswa: 148 SKS (Memenuhi & melampaui syarat minimal 144 SKS Permendikbudristek No. 53/2023).
```

---

## 4. KESIMPULAN

Seluruh berkas perancangan kurikulum (`011`, `012`, `020`, `030`, `031`, dan modul implementasi Markdown/Excel) kini telah berada dalam status **100% SINKRON, TEREKONSILIASI SECARA MATEMATIS, DAN SIAP DIJADIKAN LAMPIRAN BUKU KURIKULUM & SK REKTOR**.
