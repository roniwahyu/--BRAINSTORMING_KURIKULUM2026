# 017 — VERIFIKASI GROUND TRUTH KURIKULUM 2025 vs DOKUMEN 2026 (006–022)

**Tanggal:** 18 Agustus 2026  
**Status:** FINAL — Verifikasi Penuh Seluruh Dokumen Kurikulum 2026 (Dokumen 006 s.d. 022)  
**Ground Truth:** KURIKULUM 2025 (`Laporan Daftar Kurikulum Prodi Sistekin.pdf`, 56 MK, 146 SKS)  
**Tujuan:** Memastikan integritas data, konsistensi angka kredit SKS, pemetaan CPL, dan kepatuhan regulasi makro.

---

## 1. STATUS GROUND TRUTH KURIKULUM 2025

| Parameter | Data Kurikulum 2025 (SIAKAD UWG) |
|---|---|
| **Status Operasional** | File resmi terverifikasi manusia, dijalankan 2 semester awal |
| **Total Mata Kuliah** | 56 Mata Kuliah (Semua Wajib, 0 Peminatan) |
| **Total SKS** | 146 SKS |
| **Peminatan** | 0 Peminatan (Generalis) |
| **MK Praktikum (+P)** | 16 MK Praktikum |
| **Capaian Pembelajaran**| 10 CPL Umum (CPL01–CPL10) |
| **Profil Lulusan** | 6 Profil Lulusan (PL01–PL06) |

---

## 2. MATRIKS VERIFIKASI DOKUMEN 006 s.d. 022

| No | Dokumen | Parameter SKS / MK | Status CPL / BoK | Status Keselarasan & Ketetapan Kunci |
|:---:|---|:---:|:---:|:---:|
| **006** | `KEPUTUSAN_FINAL_ARAH_KURIKULUM` | 170 SKS / 61 MK | 14 CPL / 3 Peminatan | ✅ **100% SINKRON** (P1-P3 @ 6 MK / 18 SKS) |
| **007** | `BEDAH_STRUKTUR_KURIKULUM` | 170 SKS / 61 MK | 14 CPL / 47.1% +P | ✅ **100% SINKRON** (DW-BI Sem 4, Manpro Sem 5) |
| **008** | `LANGKAH1_PROFIL_LULUSAN_PEO` | 6 PL × 3 Jalur | PEO 3–5 Tahun | ✅ **100% SINKRON** (Indikator PEO Terukur) |
| **009** | `LANGKAH2_CPL_FORMAL` | 14 CPL SN-Dikti | S(1), KU(3), P(4), KK(6) | ✅ **100% SINKRON** (Tepat 14 CPL) |
| **009A**| `CPL_SIKAP` | CPL S1 | Etika & Moral | ✅ **100% SINKRON** |
| **009B**| `CPL_KETERAMPILAN_UMUM` | CPL KU1–KU3 | SN-Dikti Permendikbud 53 | ✅ **100% SINKRON** |
| **009C**| `CPL_PENGETAHUAN` | CPL P1–P4 | BoK IS2020 / IT2017 | ✅ **100% SINKRON** |
| **009D**| `CPL_KETERAMPILAN_KHUSUS` | CPL KK1–KK6 | @2 per Peminatan | ✅ **100% SINKRON** |
| **009E**| `RINGKASAN_CPL_LENGKAP` | 14 CPL | 19 BoK SI + 27 BoK TI | ✅ **100% SINKRON** |
| **010** | `KOMPILASI_CPL_KE_STRUKTUR` | 170 SKS / 61 MK | 14 CPL Coverage | ✅ **100% SINKRON** (DW-BI Sem 4, Manpro Sem 5) |
| **011** | `STRUKTUR_KURIKULUM_TABEL` | 170 SKS / 61 MK | 24 MK Praktikum (+P) | ✅ **MASTER TABEL FINAL TERKUNCI** |
| **012** | `MATRIKS_CPL_vs_MK` | 170 SKS / 61 MK | $\ge 3$ MK per CPL | ✅ **100% SINKRON** (Matriks Pemetaan Utuh) |
| **013** | `SEMESTER_GANJIL_PRAKTIKUM` | 19 S1, 20 S3, 21 S5, 21 S7 | Alokasi Lab Lengkap | ✅ **100% SINKRON** (Fasilitas Lab Terpetakan) |
| **014** | `ANALISIS_IOT_POSISI` | STI-504 (3 SKS, +P) | Penjamin CPL P3/KK3 | ✅ **100% SINKRON** (Wajib Core di Sem 5) |
| **015** | `PERBANDINGAN_2025_vs_2026` | 146 SKS vs 170 SKS | 10 CPL vs 14 CPL | ✅ **100% SINKRON** (Komparasi Makro) |
| **016** | `KETENTUAN_MBKM_DAN_PRASYARAT`| Maks 20 SKS MBKM | Prerequisite Chain | ✅ **100% SINKRON** (Milestone >76, >100, >120) |
| **017** | `VERIFIKASI_GROUND_TRUTH` | Dokumen ini | Bukti Audit Silang | ✅ **100% VERIFIED** |
| **018** | `AUDIT_TRAIL_PERBAIKAN` | Log §1.0 s.d. §7.13 | Riwayat Konsensus | ✅ **100% UP-TO-DATE** |
| **019** | `SURVEY_PEMETAAN_IMPROVEMENT`| P1, P2, P3 Level S1 | STC-02 BPA Terisi | ✅ **100% SINKRON** |
| **020** | `ANALISIS_KESELARASAN_OBE` | 144 SKS Lulus | Single Source of Truth | ✅ **100% PERFECT ALIGNMENT** ⭐ |
| **021** | `PEMETAAN_BoK_VS_MK` | 19 SI-BK / 27 TI-BK | 0 Gap / BK15 Terpenuhi | ✅ **100% APTIKOM COMPLIANT** |
| **022** | `AUDIT_KRITIS_BEBAN_BOK` | Stress-Testing Audit | Mitigasi Risiko RPS | ✅ **100% RESOLVED** ⭐ |

---

## 3. RINGKASAN DATA KUNCI TIDAK BOLEH BERUBAH (GROUND TRUTH 2026)

1. **Jumlah CPL:** Tepat **14 CPL** (S1, KU1-KU3, P1-P4, KK1-KK6).
2. **Beban SKS Kelulusan Mahasiswa:** **Tepat 144 SKS** (Portofolio kurikulum yang ditawarkan = 170 SKS / 61 Mata Kuliah).
3. **Peminatan Keahlian:** Tepat **3 Peminatan Seimbang** @ 6 MK (18 SKS):
   - **P1: Integrated Smart Systems** (STA-01 s.d. STA-06)
   - **P2: Cloud Infrastructure & Cybersecurity** (STB-01 s.d. STB-06)
   - **P3: Digital Platform Engineering** (STC-01 s.d. STC-06, memuat *STC-02 Rekayasa & Otomasi Proses Bisnis*)
4. **Distribusi Beban Semester 4 & 5:**
   - **Semester 4 (Genap - 19 SKS):** `STI-402 Data Warehouse & Business Intelligence` (+P, 3 SKS).
   - **Semester 5 (Ganjil - 21 SKS):** `STI-506 Manajemen Proyek TI` (Non-+P, 3 SKS) & `STI-504 Internet of Things` (+P, 3 SKS, Core Wajib).

---

*Dokumen ini merupakan verifikasi integritas data final untuk seluruh rangkaian Dokumen 006 s.d. 022 Kurikulum SISTEKIN 2026.*
