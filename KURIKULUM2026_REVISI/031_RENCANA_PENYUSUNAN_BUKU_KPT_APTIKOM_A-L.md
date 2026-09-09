# 031 — RENCANA PENYUSUNAN BUKU KPT BERBASIS TEMPLATE APTIKOM 12 BAGIAN A–L
## Program Studi Sistem dan Teknologi Informasi (S1) — FSTI Universitas Widyagama Malang

**Tanggal:** 09 September 2026  
**Status:** 🔄 **IN PROGRESS** — Label A–L sudah ditambahkan ke Dok. 023; pengisian konten gap sedang berjalan  
**Referensi Template:** `020_TEMPLATE_BUKU_KURIKULUM_KPT_OBE_APTIKOM.md`  
**Target File:** `023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md` *(revisi in-place, bukan file baru)*

---

## 1. SITUASI SAAT INI

Dokumen `023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md` sudah memuat **Buku KPT 12 Bab (Bab I–XII)** yang komprehensif (~67 KB, 986 baris setelah revisi). Struktur ini mengikuti KPT 2024 dan telah dilengkapi **label A–L APTIKOM paralel** pada setiap heading bab (per 09 Sep 2026).

### 1.1 Keputusan Desain (Konsensus)

| Pertanyaan | Jawaban |
|---|---|
| File baru atau revisi 023? | **Revisi 023** (label A–L ditambahkan paralel) |
| Kedalaman Bagian I (RPS)? | **Hanya kerangka format** tanpa contoh MK |
| Data UPPS tersedia? | **Belum** — semua `[PERLU DATA UPPS]` |

---

## 2. PEMETAAN TEMPLATE A–L ↔ STRUKTUR KPT 2024

| Bagian APTIKOM | Bab KPT 2024 | Judul | Status | Sumber Konten |
|:---:|:---:|---|:---:|---|
| **A** | **I** | Identitas Program Studi | ⚠️ PERLU DATA UPPS | Dok. 001 + data resmi UPPS |
| **B** | **II** | Evaluasi Kurikulum dan Tracer Study | ⚠️ PERLU LENGKAP | Dok. 001, 010, 019 |
| **C** | **III** | Landasan Perancangan & Pengembangan Kurikulum | ✅ TERISI | Ditulis di naskah ini |
| **D** | **IV** | Visi, Misi, Tujuan, Strategi, dan University Value | ✅ TERISI | Dok. 001, 002 |
| **E** | **V** | Rumusan Standar Kompetensi Lulusan (SKL) | ✅ TERISI | Dok. 002, 003, 009A–009E |
| **F** | **VI** | Penetapan Bahan Kajian | ⚠️ PERLU LENGKAP | Dok. 003, 016 |
| **G** | **VII** | Pembentukan MK dan Penentuan Bobot SKS | ✅ TERISI | Dok. 004, 005 |
| **H** | **VIII** | Matriks, Peta Kurikulum, dan Masa Tempuh | ✅ TERISI | Dok. 004, 005, 011, 012, 015 |
| **I** | **IX** *(sebagian)* | Rencana Pembelajaran Semester (RPS) | ⚠️ PERLU LENGKAP | Dok. 007, 008, 018 |
| **J** | **IX** *(sebagian)* | Asesmen Pembelajaran | ⚠️ PERLU LENGKAP | Dok. 008, 018 |
| **K** | **X** | Rencana Implementasi Hak Belajar Maks. 3 Semester | ⚠️ PERLU LENGKAP | Dok. 006, 009 |
| **L** | **XI** | Manajemen dan Mekanisme Pelaksanaan Kurikulum | ✅ TERISI | Dok. 008, 010, 013 |
| *(suplemen)* | **XII** | Tata Cara Penerimaan Mahasiswa | ✅ BARU | Ditulis di naskah ini |

> **Keterangan.** Template APTIKOM (A–L) dan KPT 2024 (I–XII) adalah satu kerangka yang sama dengan nomenklatur berbeda. Pengecualian: **Butir XII KPT 2024** tidak memiliki padanan di template APTIKOM — wajib per Permendikbudristek 53/2023 Pasal 44 huruf h.

---

## 3. GAP ANALYSIS — KONTEN YANG MASIH PERLU DIISI

### 3.1 Gap yang Terblokir Data Institusi (Tidak Bisa Diisi Tanpa Konfirmasi UPPS)

| Gap | Bagian | Konten yang Dibutuhkan | Sumber |
|:---:|:---:|---|---|
| 1 | **A** | Nomor SK akreditasi, gelar lulusan, website, email, nomor SK izin prodi | UPPS |
| 2 | **B** | Kolom "Kinerja Mutu aktual" dan "Kesenjangan" Tabel B (6 tahap Provus) | Data riil prodi |
| 3 | **III.5.3** | Nomor SK: Statuta, Renstra, VMTS Univ., VMTS FSTI, SPMI, Pedoman Akademik | UPPS |
| 4 | **VIII.5** | Batas maksimal masa studi sesuai Pedoman Akademik UWG | UPPS |

### 3.2 Gap yang Bisa Diisi (Konten Akademis — Tidak Butuh Data UPPS)

| Gap | Bagian | Konten | Prioritas |
|:---:|:---:|---|:---:|
| 5 | **F** | Tabel deskripsi/cakupan materi 19 BK-IS (IS2020) + 14 BK-IT (IT2017) | 🔴 Tinggi |
| 6 | **I** | Kerangka format RPS 8 kolom + penjelasan analisis pembelajaran | 🔴 Tinggi |
| 7 | **J** | Rubrik Holistik + Rubrik Skala Persepsi (belum ada di Dok. 008/018) | 🟡 Sedang |
| 8 | **K** | 6 BKP MBKM yang belum dirancang (KKNT, Asistensi, Riset, Kemanusiaan, Pertukaran, Bela Negara) | 🔴 Tinggi |
| 9 | **K** | Rekognisi kredit dalam Transkrip Akademik & SKPI | 🔴 Tinggi |

---

## 4. RENCANA KONTEN DETAIL PER BAGIAN GAP

### Bagian F — Penetapan Bahan Kajian
Tambahkan setelah baris kosong `| BK-IS01 | ... | [perlu ditulis] |`:

```
Tabel F.1 — 19 BK IS2020 dengan Deskripsi Cakupan Materi
Kolom: Kode BK | Nomenklatur | Deskripsi & Cakupan | MK Pengampu Utama | Sumber

Tabel F.2 — 14 BK IT2017 dengan Deskripsi Cakupan Materi
Kolom: Kode BK | Nomenklatur | Deskripsi & Cakupan | MK Pengampu Utama | Sumber
```

### Bagian I — RPS (Kerangka Format Saja)

```
I.1  11 komponen wajib sampul RPS
I.2  Template tabel 8 kolom mingguan (kosong siap isi)
I.3  Perhitungan estimasi waktu: 1 SKS = 170 menit/minggu
I.4  4 struktur analisis pembelajaran (Hirarki, Prosedural, Cluster, Kombinasi)
I.5  Gap note: kolom (3) Indikator & (4) Kriteria belum ada di Dok. 007
```

### Bagian J — Asesmen (Rubrik Baru)

```
J.7  Rubrik Holistik — 4 level deskriptor (Sangat Baik / Baik / Cukup / Kurang)
J.8  Rubrik Skala Persepsi — Likert 5 poin untuk asesmen sikap & partisipasi
```

### Bagian K — MBKM (Konten Baru)

```
K.1  Tabel 9 BKP lengkap (rows 4-9 yang masih [perlu ditulis] di Tabel X.1)
K.2  Mekanisme rekognisi kredit formal (prosedur, tim penilai, instrumen)
K.3  Format pencantuman di Transkrip Akademik (kode MK + ket. MBKM)
K.4  Format pencantuman di SKPI (deskripsi kegiatan + CPL yang dicapai)
```

---

## 5. PROGRESS TRACKER

| Pekerjaan | Status | Tanggal |
|---|:---:|---|
| Label A–L paralel ditambahkan ke 13 heading bab | ✅ SELESAI | 09 Sep 2026 |
| Daftar Isi diperbarui (kolom Bagian APTIKOM + Bab KPT) | ✅ SELESAI | 09 Sep 2026 |
| Halaman judul diperbarui (struktur naskah ganda) | ✅ SELESAI | 09 Sep 2026 |
| Bagian J dipisah dari Bagian I (heading baru) | ✅ SELESAI | 09 Sep 2026 |
| Tabel deskripsi 19 BK-IS + 14 BK-IT (Bagian F) | ⬜ BELUM | — |
| Kerangka format RPS 8 kolom (Bagian I) | ⬜ BELUM | — |
| Rubrik Holistik & Skala Persepsi (Bagian J) | ⬜ BELUM | — |
| 6 BKP MBKM + rekognisi Transkrip/SKPI (Bagian K) | ⬜ BELUM | — |
| Verifikasi konsistensi angka final dengan Dok. 005 | ✅ SELESAI | 08 Sep 2026 |

---

## 6. DATA UPPS YANG PERLU DIKUMPULKAN (Checklist untuk Kaprodi)

Kirimkan permintaan terpadu ke UPPS untuk 10 butir berikut:

- [ ] 1. Peringkat Akreditasi — nomor dan tanggal SK LAM INFOKOM/BAN-PT yang berlaku
- [ ] 2. Gelar Lulusan — nomenklatur resmi sesuai SK izin pembukaan prodi
- [ ] 3. Nomor SK Izin Operasional prodi + tahun penyelenggaraan pertama
- [ ] 4. Website resmi program studi
- [ ] 5. Email resmi program studi
- [ ] 6. Nomor SK Statuta Universitas Widyagama Malang
- [ ] 7. Nomor SK Renstra Universitas (beserta periode berlaku)
- [ ] 8. Identitas dokumen VMTS Universitas dan FSTI (nomor SK penetapan)
- [ ] 9. Nomor SK SPMI Universitas + nomor SOP Pembelajaran
- [ ] 10. Batas maksimal masa studi + jalur seleksi PMB (untuk Bab XII)

---

## 7. PETA JALAN FINALISASI NASKAH

```
[Tahap 1] ✅ Resolusi inkonsistensi angka komposisi SKS    → SELESAI 08 Sep 2026
[Tahap 2] ✅ Label A–L paralel ditambahkan ke Dok. 023     → SELESAI 09 Sep 2026
[Tahap 3] ⬜ Isi gap F, I, J, K (konten akademis baru)    → IN PROGRESS
[Tahap 4] ⬜ Kumpulkan 10 data UPPS (checklist §6)        → Koordinasi Kaprodi
[Tahap 5] ⬜ Input data UPPS ke Bagian A, C, D, H, XII
[Tahap 6] ⬜ Resolusi issue Dok. 019 (P0–P1):
           - Tabrakan kode FST-204/FST-205
           - Sinkronisasi rantai prasyarat 19 MK (Dok. 007 → Dok. 005)
           - Satu versi master matriks CPL↔PL (tetapkan Dok. 003)
[Tahap 7] ⬜ Verifikasi final: python _tools/verify_zero_discrepancy.py
[Tahap 8] ⬜ Ekspor ke DOCX/PDF untuk pengajuan SK Rektor
```

---

## 8. REFERENSI SILANG DOKUMEN

| Dokumen | Peran dalam Buku KPT |
|---|---|
| `001_ANALISIS_VMTS...md` | Sumber Bagian D (VMTS Prodi) |
| `002_FORMULASI_3_PEO...md` | Sumber Bagian E (PEO & 4 PL) |
| `003_STANDAR_14_CPL...md` | Sumber Bagian E & F (14 CPL + BoK) |
| `004_MATRIKS_KETERLACAKAN...md` | Sumber Bagian G & H (matriks I-R-M) |
| `005_STRUKTUR_KURIKULUM...md` | **Ground truth:** 8 semester, 55 MK, 146 SKS |
| `006_DISTRIBUSI_MK_PEMINATAN...md` | Sumber Bagian K (MBKM konversi SKS) |
| `007_FORMULASI_CPMK...md` | Lampiran 2: silabus 67 MK |
| `008_SISTEM_ASESMEN_OBE...md` | Sumber Bagian J (formula CPL, rubrik analitik) |
| `009_PEDOMAN_CAPSTONE...md` | Sumber Bagian K (Capstone & TA non-skripsi) |
| `010_INSTRUMEN_TRACER_STUDY...md` | Lampiran 3; Sumber Bagian B & L |
| `012_ANALISIS_JALUR_PONDASI...md` | Sumber Bagian H (pohon prasyarat) |
| `015_SIMULASI_AKSELERASI...md` | Lampiran 8; Sumber Bagian H.5 masa tempuh |
| `016_ANALISIS_BOK_APTIKOM...md` | Sumber Bagian F (pipeline AI 5 tahap) |
| `017_AUDIT_FORENSIK_ZERO...md` | Sumber Bagian F (audit zero redundancy) |
| `018_PANDUAN_RUBRIK_KLASTER...md` | Sumber Bagian J (4 klaster rubrik analitik) |
| `020_TEMPLATE_BUKU_KPT_OBE_APTIKOM.md` | **Template acuan** 12 Bagian A–L |
| `023_BUKU_KPT_SISTEKIN...md` | **Target revisi** — naskah utama buku KPT |

---

*Dokumen ini adalah rencana kerja (implementation plan) penyusunan Buku KPT SISTEKIN 2026.*  
*Single source of truth konten kurikulum: Dok. 001–018 + konsensus `AGENTS.md`.*

**Tim Pengembang Kurikulum FSTI Universitas Widyagama Malang**
