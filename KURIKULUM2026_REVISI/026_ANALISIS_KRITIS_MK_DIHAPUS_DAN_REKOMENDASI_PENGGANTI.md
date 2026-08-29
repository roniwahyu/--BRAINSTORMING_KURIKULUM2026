# 026 — ANALISIS KRITIS HASIL DOKUMEN 024: VERIFIKASI KLAIM PENYERAPAN MATA KULIAH YANG DIHAPUS
## Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang

**Dokumen Revisi Definitif Kurikulum 2026**
**Objek Analisis:** Dokumen 024 (Matriks Ekivalensi K2025 → K2026), khusus kategori **E5 — Tanpa Padanan**
**Sumber Verifikasi:** `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` (ground truth K2025), Dokumen 007 (Silabus 67 MK Portofolio), Dokumen 003/009C/009D (14 CPL), Dokumen 016 & 017 (Audit BoK & Zero Redundancy), `KURIKULUM2025/obe_pdf_extract/Implementasi_Modul_OBE_SISTEKIN2025_TABLES.md` (Matriks CPL–MK K2025)
**Metode:** Pemindaian kata kunci terprogram atas 65 blok silabus MK pada Dokumen 007, dibandingkan dengan pernyataan naratif Dokumen 024.
**Tanggal Analisis:** 29 Agustus 2026

---

## 1. RUANG LINGKUP DAN BATAS ANALISIS

Analisis ini **hanya** menguji 2 mata kuliah Kurikulum 2025 berkategori **E5 (Tanpa Padanan)**, yaitu mata kuliah yang dihapus tanpa MK pengganti pada Kurikulum 2026:

| Kode K2025 | Nama Mata Kuliah | SKS | Smt | Perlakuan Dok 024 |
|:---:|---|:---:|:---:|---|
| `STI-423` | Game Design dan Gamifikasi Sosial (+P) | 3 | 4 | Dihapus, diakui sebagai kredit bebas 3 SKS |
| `STI-638` | Intelligent Signal Processing | 3 | 6 | Dihapus, diakui sebagai kredit bebas 3 SKS |

**Yang TIDAK dicakup analisis ini:** kategori E1 (34 MK), E2 (11 MK), E3 (8 MK), dan E4 (1 MK). Keempat kategori tersebut telah diverifikasi terpisah oleh `_tools/verify_k2025_ground_truth.py` pada aspek atribut MK, neraca SKS, dan Zero Orphan — bukan pada aspek kebenaran substansi materi.

---

## 2. TEMUAN

### 2.1 TEMUAN 1 — KLAIM PENYERAPAN GAMIFIKASI TIDAK TERBUKTI

**Pernyataan Dokumen 024** (Bagian 3.4, baris 30):

> "**Dihapus** dari K2026 (di luar positioning "Integrator AI"). Unsur gamifikasi terserap parsial pada `STC-01` UX Research & `STC-04` XR. Diakui sebagai kredit bebas 3 SKS"

**Pengujian:** pemindaian 11 kata kunci (`gamifikas`, `gamification`, `game`, `permainan`, `poin`, `leaderboard`, `badge`, `reward`, `level`, `player`, `pemain`) pada blok silabus lengkap `STC-01` dan `STC-04` di Dokumen 007.

**Hasil:**

| MK yang Diklaim Menyerap | Kemunculan Kata Kunci Gamifikasi | Status Klaim |
|:---:|---|:---:|
| `STC-01` User Experience Research & Design | **Nol.** Kata `level` muncul 4× pada konteks "Level Bloom" (2×) dan "WCAG 2.1 Level AAA" (2×) | ❌ **Tidak terbukti** |
| `STC-04` Immersive Media & XR Development | **Nol.** Kata `level` muncul 3× pada konteks "Level Bloom" (2×) dan "Level of Detail (LOD)" (1×) | ❌ **Tidak terbukti** |

**Pemindaian menyeluruh 67 MK portofolio** menunjukkan satu-satunya jangkar gamifikasi berada pada MK yang **tidak disebut** Dokumen 024:

| MK Sebenarnya | Lokasi | Kutipan Pokok Bahasan |
|:---:|:---:|---|
| `STC-03` Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech) | Pekan 9 | "Domain EdTech: Arsitektur LMS Modern, Kursus Daring, **Gamifikasi Pembelajaran**" |

Cakupannya adalah **satu sub-pokok bahasan dalam satu pekan**, bukan penyerapan setara MK 3 SKS.

---

### 2.2 TEMUAN 2 — KLAIM PENYERAPAN PENGOLAHAN SINYAL SEBAGIAN TIDAK TERBUKTI

**Pernyataan Dokumen 024** (Bagian 3.6, baris 47):

> "**Dihapus** dari K2026 (bertumpang dengan ranah riset algoritma Prodi TI, Dok. 016). Unsur ekstraksi fitur sinyal terserap parsial pada `STI-501` Deep Learning & `STA-06` Smart Surveillance. Diakui sebagai kredit bebas 3 SKS"

**Pengujian:** pemindaian 14 kata kunci (`sinyal`, `signal`, `fourier`, `fft`, `wavelet`, `filter digital`, `spektral`, `spektrum`, `frekuensi`, `audio`, `ekstraksi fitur`, `feature extraction`, `time series`, `deret waktu`).

**Hasil:**

| MK yang Diklaim Menyerap | Temuan | Status Klaim |
|:---:|---|:---:|
| `STI-501` Deep Learning & Neural Networks | `Feature Extraction` 1× (Pekan 7: *"Transfer Learning: Feature Extraction vs Fine-Tuning Model Vision"*), `Time Series` 1× (Pekan 12: *"Gated Architectures: LSTM Cells, GRU Cells untuk Time Series"*) | ⚠️ **Sebagian** — konteks vision & deret waktu, bukan pengolahan sinyal |
| `STA-06` Smart Surveillance and IoT Analytics | **Nol** dari 14 kata kunci. Seluruh 16 pekan murni *computer vision*: YOLOv8, ByteTrack, RetinaFace, TensorRT, Edge AI | ❌ **Tidak terbukti** |

**Pemindaian menyeluruh 67 MK portofolio** untuk `pengolahan sinyal`, `signal processing`, `fourier`, `wavelet`, `spektral`, dan `frekuensi sinyal`: **tidak ditemukan sama sekali**.

---

### 2.3 TEMUAN 3 — RUJUKAN JUSTIFIKASI PENGHAPUSAN TIDAK DAPAT DIVERIFIKASI

Dokumen 024 mendasarkan penghapusan `STI-638` pada *"bertumpang dengan ranah riset algoritma Prodi TI, **Dok. 016**"*.

**Pengujian:** pencarian `STI-423`, `STI-638`, `gamifikas`, dan `signal` pada Dokumen 016 (Audit BoK APTIKOM & Pipeline AI) dan Dokumen 017 (Audit Forensik Zero Redundancy & Zero Gap).

**Hasil:** **nol kemunculan pada kedua dokumen.** Kedua mata kuliah ini tidak pernah dibahas dalam audit mana pun, sehingga sitasi "Dok. 016" pada baris 47 tidak memiliki dasar yang dapat dilacak.

---

## 3. VERIFIKASI SISI CAPAIAN PEMBELAJARAN — PENGHAPUSAN DAPAT DIPERTANGGUNGJAWABKAN

Berbeda dari klaim penyerapan, **keputusan menghapus kedua MK itu sendiri konsisten** dengan penyempitan cakupan CPL.

### 3.1 PERBANDINGAN RUMUSAN CPL

| Kurikulum | Rumusan CPL Terkait | Menyebut Gamifikasi / Sinyal? |
|---|---|:---:|
| **K2025** `CPL04` | "Mampu merancang dan mengevaluasi antarmuka, pengalaman pengguna, **gamifikasi**, dan **multimedia interaktif** ..." | ✅ Eksplisit |
| **K2026** 14 CPL (S1, KU1–3, P1–4, KK1–6) | Pemindaian `gamifikas`, `sinyal`, `signal`, `multimedia` pada Dok 003, 009C, dan 009D | ❌ **Tidak disebut sama sekali** |

Penghapusan kedua MK **selaras** dengan hilangnya kedua ranah tersebut dari rumusan 14 CPL Kurikulum 2026. Ini keputusan lingkup (*scoping*) yang sah, bukan kesenjangan capaian pembelajaran.

### 3.2 KEDUA MK BUKAN PENGAMPU TUNGGAL DI K2025

Berdasarkan Matriks CPL–MK Kurikulum 2025 (Modul OBE 2025):

| MK Dihapus | CPL yang Diampu di K2025 | Jumlah MK K2025 Lain yang Juga Mengampu CPL Sama |
|:---:|:---:|:---:|
| `STI-423` | `CPL04`, `CPL08` | **17 MK** |
| `STI-638` | `CPL03`, `CPL05`, `CPL09` | **31 MK** |

Tidak ada CPL Kurikulum 2025 yang menjadi yatim akibat penghapusan ini.

---

## 4. RINGKASAN STATUS KLAIM

| # | Klaim Dokumen 024 | Status | Dampak |
|:---:|---|:---:|---|
| 1 | Gamifikasi terserap pada `STC-01` | ❌ Tidak terbukti | Salah alamat rujukan |
| 2 | Gamifikasi terserap pada `STC-04` | ❌ Tidak terbukti | Salah alamat rujukan |
| 3 | Ekstraksi fitur sinyal terserap pada `STI-501` | ⚠️ Sebagian, konteks berbeda | Perlu penajaman redaksi |
| 4 | Ekstraksi fitur sinyal terserap pada `STA-06` | ❌ Tidak terbukti | Salah alamat rujukan |
| 5 | Penghapusan `STI-638` berdasar Dok. 016 | ❌ Tidak dapat diverifikasi | Sitasi tanpa dasar |
| 6 | Penghapusan konsisten dengan cakupan 14 CPL | ✅ Terbukti | — |
| 7 | Tidak ada CPL K2025 yang yatim | ✅ Terbukti | — |

**Pokok masalah bukan kesenjangan capaian pembelajaran, melainkan klaim penyerapan yang salah alamat.** Risiko praktisnya: mahasiswa atau Dosen Penasihat Akademik yang menanyakan "materi Game Design saya diserap ke mana?" akan diarahkan ke `STC-01` atau `STC-04` yang tidak memuatnya.

---

## 5. REKOMENDASI PERBAIKAN — SELURUH MK TARGET TERSEDIA DI KURIKULUM2026_REVISI

### 5.1 UNTUK `STI-423` GAME DESIGN DAN GAMIFIKASI SOSIAL

| Opsi | Tindakan | MK Target | Konsekuensi |
|:---:|---|---|---|
| **A** *(minimal, tanpa ubah silabus)* | Ganti rujukan penyerapan dari `STC-01`/`STC-04` menjadi `STC-03` | `STC-03` Rekayasa Aplikasi Industri Vertikal (3 SKS, **Sem 6**, Peminatan **P3**) | Akurat secara faktual, tetapi cakupan hanya 1 pekan pada domain EdTech. Perlu dinyatakan jujur sebagai "singgungan", bukan "penyerapan" |
| **B** *(substantif, mengubah silabus)* | Tambahkan pokok bahasan desain perilaku & gamifikasi pada `STC-01` | `STC-01` User Experience Research & Design (3 SKS, **Sem 5**, Peminatan **P3**) | CPL `P4` (Arsitektur Informasi & Aksesibilitas) dan `KK5` (Riset UX) paling dekat dengan desain perilaku pengguna; silabus sudah memuat `onboarding`. Menuntut revisi Dokumen 007 dan persetujuan Tim Kurikulum |

### 5.2 UNTUK `STI-638` INTELLIGENT SIGNAL PROCESSING

| Opsi | Tindakan | MK Target | Konsekuensi |
|:---:|---|---|---|
| **A** *(minimal, tanpa ubah silabus)* | Ganti rujukan `STA-06` menjadi `STI-504`; pertahankan `STI-501` khusus untuk komponen deret waktu | `STI-504` Internet of Things (3 SKS, **Sem 5**, **paket wajib**) — memuat sensor, telemetri, MQTT | Prapemrosesan dan penapisan data sensor adalah tempat yang wajar. Rujukan `STI-501` dipersempit redaksinya menjadi "deret waktu (LSTM/GRU)", bukan "ekstraksi fitur sinyal" |
| **B** *(substantif, mengubah silabus)* | Tambahkan pokok bahasan prapemrosesan sinyal sensor pada `STI-504` | `STI-504` Internet of Things | Menuntut revisi Dokumen 007 |

### 5.3 UNTUK TEMUAN 3 (SITASI TANPA DASAR)

Hapus sitasi "Dok. 016" pada baris 47 Dokumen 024, **atau** tambahkan pembahasan `STI-423` dan `STI-638` ke Dokumen 016/017 agar sitasi menjadi sah. Pilihan pertama lebih ringkas; pilihan kedua lebih kuat untuk kepentingan asesmen LAM INFOKOM.

### 5.4 CATATAN LINGKUP YANG PERLU KEPUTUSAN PRODI

Apabila prodi menghendaki **pengolahan sinyal benar-benar tercakup** (bukan hanya dinyatakan terserap), perlu dicatat bahwa **tidak ada satu pun dari 67 MK portofolio yang saat ini memuatnya**. Hal ini tidak dapat diselesaikan dengan menyunting catatan ekivalensi dan merupakan keputusan lingkup kurikulum yang berada pada kewenangan Rapat Tim Kurikulum.

---

## 6. STATUS TINDAK LANJUT

| No | Butir | Status |
|:---:|---|:---:|
| 1 | Analisis dan verifikasi terprogram | ✅ Selesai |
| 2 | Perbaikan catatan baris 30 Dokumen 024 (`STI-423`) | ⏸️ Menunggu keputusan Opsi A atau B |
| 3 | Perbaikan catatan baris 47 Dokumen 024 (`STI-638`) | ⏸️ Menunggu keputusan Opsi A atau B |
| 4 | Penanganan sitasi "Dok. 016" tanpa dasar | ⏸️ Menunggu keputusan |
| 5 | Keputusan lingkup pengolahan sinyal | ⏸️ Kewenangan Rapat Tim Kurikulum |

> [!NOTE]
> Dokumen 024 **belum diubah**. Analisis ini disimpan sebagai temuan untuk dibahas terlebih dahulu, sesuai kaidah bahwa perubahan atas konsensus kurikulum memerlukan persetujuan Tim Pengembang.

---
*Disahkan sebagai Dokumen Resmi 026 — Kurikulum OBE Revisi SISTEKIN 2026.*
**Tim Pengembang Kurikulum FSTI Universitas Widyagama Malang**
