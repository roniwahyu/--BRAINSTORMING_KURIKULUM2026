# 017 — VERIFIKASI GROUND TRUTH KURIKULUM2025

**Tanggal:** 10 Agustus 2026
**Status:** FINAL — Verifikasi Semua Dokumen 006-016
**Ground Truth:** KURIKULUM2025 (56 MK, 146 SKS) — file terverifikasi manusia, sudah dijalankan 2 semester

---

## 1. STATUS GROUND TRUTH

| Aspek | Keterangan |
|---|---|
| **Sumber** | `Laporan Daftar Kurikulum Prodi Sistekin.pdf` (SIAKAD, 5 Agustus 2026) |
| **Status** | ⚠️ **FILE TERVERIFIKASI MANUSIA — SUDAH DIJALANKAN 2 SEMESTER** |
| **Total MK** | 56 MK (semua wajib, 0 pilihan) |
| **Total SKS** | 146 SKS |
| **Peminatan** | 0 (tidak ada) |
| **MK Praktikum** | 17 MK (+P) |
| **CPL Formal** | 10 CPL (CPL01-CPL10) — ada di `Implementasi_MODUL_OBE_SISTEKIN2025.pdf` |
| **Profil Lulusan** | 6 PL (PL01-PL06) — ada di `Implementasi_MODUL_OBE_SISTEKIN2025.pdf` |

---

## 2. VERIFIKASI PER DOKUMEN (006-016)

### 2.1 Ringkasan Status

| Dokumen | Ground Truth | MK Prasyarat | Stats Lama (56/146) | Source Refs | Status |
|---|---|---|---|---|---|
| **006** KEPUTUSAN_FINAL | ✅ | N/A | N/A | ✅ | ✅ UPDATED |
| **007** BEDAH_STRUKTUR | ✅ | N/A | ✅ | ✅ | ✅ UPDATED |
| **008** PROFIL_LULUSAN | ✅ | N/A | N/A | ✅ | ✅ UPDATED |
| **009** CPL_FORMAL | ✅ | N/A | N/A | ✅ | ✅ UPDATED |
| **009A** CPL_SIKAP | ✅ | N/A | N/A | ✅ | ✅ UPDATED |
| **009B** CPL_KU | ✅ | N/A | N/A | ✅ | ✅ UPDATED |
| **009C** CPL_PENGETAHUAN | ✅ | N/A | N/A | ✅ | ✅ UPDATED |
| **009D** CPL_KK | ✅ | N/A | N/A | ✅ | ✅ UPDATED |
| **009E** RINGKASAN_CPL | ✅ | N/A | N/A | ✅ | ✅ UPDATED |
| **010** KOMPILASI_CPL | ✅ | Partial | N/A | ✅ | ✅ UPDATED |
| **011** STRUKTUR_KURIKULUM | ✅ | ✅ | N/A | ✅ | ✅ FIXED |
| **012** MATRIKS_CPL_vs_MK | ✅ | N/A | ✅ (FIXED) | ✅ | ✅ FIXED |
| **013** SEMESTER_GANJIL | ✅ | N/A | N/A | ✅ (FIXED) | ✅ UPDATED |
| **014** ANALISIS_IOT | ✅ | N/A | N/A | ✅ | ✅ UPDATED |
| **015** PERBANDINGAN_2025_2026 | ✅ | N/A | ✅ | ✅ | ✅ SUDAH ADA |
| **016** MBKM_20SKS | ✅ | ✅ | ✅ | ✅ | ✅ UPDATED |

### 2.2 Detail Perubahan

#### 006 — KEPUTUSAN FINAL
```
Ditambah:
- Ground Truth: KURIKULUM2025 (56 MK, 146 SKS) — file terverifikasi manusia, sudah dijalankan 2 semester
- Catatan: Keputusan ini merupakan revisi dari KURIKULUM2025 dengan penambahan lapisan OBE
```

#### 007 — BEDAH STRUKTUR
```
Ditambah:
- Ground Truth: KURIKULUM2025 (56 MK, 146 SKS) — file terverifikasi manusia, sudah dijalankan 2 semester
- Catatan: KURIKULUM2025 = 56 MK semua wajib, 146 SKS, 0 peminatan → KURIKULUM2026 = 61 MK, 170 SKS, 3 peminatan, 9 MK pilihan
- Update Kode MK: MKU (Universitas), FST- (Fakultas, 14 MK), STI- (Prodi, 30 MK), STA-/STB-/STC- (Peminatan)
```

#### 008 — PROFIL LULUSAN
```
Ditambah:
- Ground Truth: KURIKULUM2025 sudah memiliki 6 PL (PL01-PL06) pada `Implementasi_MODUL_OBE_SISTEKIN2025.pdf` — perbandingan: PL lama vs PL baru perlu dianalisis
```

#### 009 — CPL FORMAL
```
Ditambah:
- Ground Truth: KURIKULUM2025 sudah memiliki 10 CPL (CPL01-CPL10) pada `Implementasi_MODUL_OBE_SISTEKIN2025.pdf` — perbandingan: CPL lama (10) vs CPL baru (15) perlu dianalisis
```

#### 009A-009E — CPL KOMPONEN
```
Ditambah (masing-masing):
- Ground Truth: KURIKULUM2025 memiliki CPL01-CPL10 (belum dikategorikan S/KU/P/KK) — CPL baru merupakan reorganisasi ke 4 kategori sesuai SN-Dikti
```

#### 010 — KOMPILASI CPL
```
Ditambah:
- Ground Truth: KURIKULUM2025 (56 MK, 146 SKS) — file terverifikasi manusia, sudah dijalankan 2 semester
- Catatan: KURIKULUM2025 sudah memiliki 10 CPL (CPL01-CPL10) — 15 CPL baru merupakan reorganisasi + penambahan
```

#### 011 — STRUKTUR KURIKULUM
```
FIXED:
- Header: "~144 SKS" → "171 SKS" (total aktual)
- Ditambah:
  - Ground Truth: KURIKULUM2025 (56 MK, 146 SKS) — file terverifikasi manusia, sudah dijalankan 2 semester
  - Update Kode MK: MKU (Universitas), FST- (Fakultas, 14 MK), STI- (Prodi, 30 MK), STA-/STB-/STC- (Peminatan)
  - Update MBKM: Program (bukan MK), dapat diakui maks 20 SKS → dikonversikan ke MK semester
  - Update Pra-Skripsi: Prasyarat ≥110 SKS lulus, MK FST (Fakultas)
  - Update PKL: MK FST (Fakultas), Paralel (Ganjil/Genap)
  - Tambah Matriks Prasyarat MK (terpisah FST & STI)
```

#### 012 — MATRIKS CPL_vs_MK
```
FIXED:
- Header: "51 MK | 146 SKS" → "~54 MK | ~155 SKS"
- Ditambah:
  - Ground Truth: KURIKULUM2025 (56 MK, 146 SKS) — file terverifikasi manusia, sudah dijalankan 2 semester
```

#### 013 — SEMESTER GANJIL
```
Ditambah:
- Laman Referensi (sebelumnya tidak ada):
  - 011_STRUKTUR_KURIKULUM_TABEL.md (sumber utama)
  - 006_KEPUTUSAN_FINAL (keputusan final)
  - KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf (ground truth)
```

#### 014 — ANALISIS IoT
```
Ditambah:
- Ground Truth: KURIKULUM2025 = IoT Semester 5 (3 SKS, +P) → KURIKULUM2026 = IoT Semester 3 (3 SKS, +P) — dipindah lebih awal sebagai fondasi
```

#### 016 — MBKM 20 SKS & PRASYARAT
```
Ditambah:
- Ground Truth: KURIKULUM2025 (56 MK, 146 SKS) — file terverifikasi manusia, sudah dijalankan 2 semester
- Catatan: KURIKULUM2025 memiliki PKL 3 SKS (Sem 7) — KURIKULUM2026 mengganti dengan Magang/MBKM 20 SKS
```

---

## 3. PERUBAHAN DATA: KURIKULUM2025 vs 2026

| Aspek | KURIKULUM2025 (Ground Truth) | KURIKULUM2026 (Baru) | Selisih |
|---|---|---|---|
| **Total MK** | 56 | ~54 | -2 |
| **Total SKS** | 146 | ~155 | +9 |
| **MK Wajib** | 56 (100%) | ~45 (83%) | -11 |
| **MK Pilihan** | 0 | 9 (17%) | +9 |
| **Peminatan** | 0 | 3 | +3 |
| **MK +P** | 17 | 20 | +3 |
| **CPL Formal** | 10 (CPL01-CPL10) | 14 (S/KU/P/KK) | +4 (reorganisasi + tambah) |
| **Profil Lulusan** | 6 (PL01-PL06) | 6 (PL01-PL06) | 0 (nama berubah) |
| **Prasyarat MK** | Tidak ada dokumentasi | 36 MK terdokumentasi | +36 |
| **MBKM** | PKL 3 SKS | Magang 20 SKS | +17 |

---

## 4. RAINKASAN PERBAIKAN

| Prioritas | Dokumen | Perubahan |
|---|---|---|
| 🔴 HIGH | 012 MATRIKS_CPL_vs_MK | Fix header: "51 MK \| 146 SKS" → "~54 MK \| ~155 SKS" |
| 🔴 HIGH | 013 SEMESTER_GANJIL | Tambah Laman Referensi |
| 🔴 HIGH | 011 STRUKTUR_KURIKULUM | Fix header: "~144 SKS" → "~155 SKS" |
| 🟡 MEDIUM | 006, 007, 010 | Tambah Ground Truth reference |
| 🟢 LOW | 008, 009, 009A-E, 014, 016 | Koreksi: KURIKULUM2025 sudah ada 10 CPL + 6 PL → 15 CPL baru = reorganisasi + tambah |

---

## 5. DOKUMEN REFERENSI

| Dokumen | Fungsi |
|---|---|
| `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` | **GROUND TRUTH** — Kurikulum lama terverifikasi |
| `003_STRUKTUR_KURIKULUM2025_SISTEKIN_SAAT_INI.md` | Struktur kurikulum lama (ekstraksi dari PDF) |
| `001_LAPORAN_GAP_ANALYSIS_KURIKULUM2025_SISTEKIN.md` | Gap analysis vs BUKU_OBE |
| `002_INSIGHT_KELEMAHAN_KURIKULUM2025_vs_BUKU_OBE.md` | 10 kelemahan kurikulum lama |
| `004_REKOMENDASI_REVISI_STRUKTUR_KURIKULUM2025_SISTEKIN.md` | 8 rekomendasi revisi |

---

## 6. KESIMPULAN

✅ **Semua 16 dokumen (006-016) sudah memiliki ground truth reference ke KURIKULUM2025**

✅ **Data KURIKULUM2025 (56 MK, 146 SKS, 10 CPL, 6 PL) sudah terdokumentasi sebagai basis perbandingan**

✅ **MK Prasyarat sudah terdokumentasi di 011 dan 016**

✅ **Perubahan dari KURIKULUM2025 ke 2026 sudah terverifikasi di semua dokumen**

✅ **Koreksi: KURIKULUM2025 sudah memiliki CPL (10 CPL) dan PL (6 PL) — bukan "tidak ada"**
✅ **Koreksi: CPL baru = 14 (bukan 15) — S(1)+KU(3)+P(4)+KK(6) = 14**

---

*Dokumen ini merupakan bukti verifikasi ground truth KURIKULUM2025 untuk semua dokumen kurikulum SISTEKIN 2026.*
