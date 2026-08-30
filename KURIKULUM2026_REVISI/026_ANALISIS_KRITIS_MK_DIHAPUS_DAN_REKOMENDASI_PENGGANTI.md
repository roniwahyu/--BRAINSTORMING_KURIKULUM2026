# 026 — ANALISIS KRITIS HASIL DOKUMEN 024: VERIFIKASI KLAIM PENYERAPAN MATA KULIAH YANG DIHAPUS
## Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang

**Dokumen Revisi Definitif Kurikulum 2026**
**Objek Analisis:** Dokumen 024 (Matriks Ekivalensi K2025 → K2026), khusus kategori **E5 — Tanpa Padanan**
**Sumber Verifikasi:** `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` (ground truth K2025), Dokumen 007 (Silabus 67 MK Portofolio), Dokumen 003/009C/009D (14 CPL), Dokumen 016 & 017 (Audit BoK & Zero Redundancy), `KURIKULUM2025/obe_pdf_extract/Implementasi_Modul_OBE_SISTEKIN2025_TABLES.md` (Matriks CPL–MK K2025)
**Metode:** Pemindaian kata kunci terprogram atas 65 blok silabus MK pada Dokumen 007, uji ambang overlap terhadap definisi operasional E2, dan rekalkulasi neraca SKS; dibandingkan dengan pernyataan naratif Dokumen 024.
**Tanggal Analisis:** 29 Agustus 2026

---

## 0. JAWABAN RINGKAS

**Tidak ada mata kuliah Kurikulum 2026 yang layak menjadi ekivalen bagi `STI-423` maupun `STI-638`.** Lima kandidat diuji terhadap ambang E2 (overlap konten 60–85% menurut Bagian 2 Dokumen 024); overlap tertinggi hanya **6,2%**. Karena itu status **E5 (Tanpa Padanan) dipertahankan** dan kedua MK tetap diakui sebagai kredit bebas 3 SKS.

Yang perlu diperbaiki adalah **catatan penyerapannya**, yang saat ini menunjuk mata kuliah yang tidak memuat materi tersebut. Rumusan pengganti tersedia pada Bagian 6.1 dan tidak mengubah satu pun angka konsensus.

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

## 5. UJI KELAYAKAN EKIVALENSI: APAKAH KEDUA MK DAPAT DINAIKKAN DARI E5 KE E2?

Sebelum merekomendasikan MK pengganti, kelayakannya diuji terhadap **definisi operasional E2 pada Bagian 2 Dokumen 024**: *"Overlap konten 60–85%"*. Overlap diukur sebagai proporsi pekan pada Matriks 16 Pertemuan MK K2026 yang memuat materi topik terkait.

### 5.1 HASIL UJI AMBANG OVERLAP

| Topik MK Dihapus | Kandidat MK K2026 | Pekan Termuat | Overlap | Status Ambang E2 (60–85%) |
|---|:---:|:---:|:---:|:---:|
| Gamifikasi (`STI-423`) | `STC-03` Rekayasa Aplikasi Industri Vertikal | 1 dari 16 (Pekan 9) | **6,2%** | ❌ Gagal |
| Gamifikasi (`STI-423`) | `STC-01` UX Research & Design | 0 dari 16 | **0,0%** | ❌ Gagal |
| Pengolahan sinyal (`STI-638`) | `STA-06` Smart Surveillance & IoT Analytics | 0 dari 16 | **0,0%** | ❌ Gagal |
| Pengolahan sinyal (`STI-638`) | `STI-501` Deep Learning & Neural Networks | 0 dari 16 | **0,0%** | ❌ Gagal |
| Pengolahan sinyal (`STI-638`) | `STI-504` Internet of Things | 0 dari 16 | **0,0%** | ❌ Gagal |

**Kesimpulan uji:** tidak ada satu pun kandidat yang memenuhi ambang E2. Overlap tertinggi hanya 6,2%, jauh di bawah batas bawah 60%.

### 5.2 SIMULASI DAMPAK BILA E5 DIPAKSA MENJADI E2

Untuk menunjukkan konsekuensinya secara terukur, dilakukan rekalkulasi seandainya `STI-423` → `STC-03` dan `STI-638` → `STA-06` dinaikkan menjadi E2:

| Indikator Konsensus | Kondisi Sekarang (E5) | Bila Dipaksa E2 | Perubahan |
|---|:---:|:---:|:---:|
| Neraca kategori E2 | 11 MK / 29 SKS | 13 MK / 35 SKS | +2 MK |
| Neraca kategori E5 | 2 MK / 6 SKS | **0 MK / 0 SKS** | −2 MK |
| SKS diakui jalur P1 | 120 SKS | 123 SKS | +3 |
| SKS diakui jalur P2 | 120 SKS | 120 SKS | 0 |
| SKS diakui jalur P3 | 117 SKS | 120 SKS | +3 |
| Defisit jalur P1 / P2 / P3 | 26 / 26 / 29 SKS | 23 / 26 / 26 SKS | berubah |

> [!WARNING]
> **Menaikkan status ke E2 akan mengubah angka konsensus yang sudah final** pada `AGENTS.md` dan Dokumen 024 (neraca E1–E5, serta simulasi "P1/P2 = 120 SKS, P3 = 117 SKS"), sementara dasar substantifnya tidak terpenuhi (overlap 0–6,2%). Selain itu, pengakuan menjadi tidak setara antar jalur: jalur P2 tidak memperoleh tambahan apa pun karena kedua MK pengganti berada di peminatan P1 dan P3.

---

## 6. REKOMENDASI

### 6.1 REKOMENDASI UTAMA — PERTAHANKAN STATUS E5, PERBAIKI CATATAN PENYERAPAN

Berdasarkan uji ambang pada Bagian 5, **status E5 untuk kedua mata kuliah dipertahankan**. Yang diperbaiki adalah catatan penyerapan yang salah alamat, bukan kategorinya.

| MK Dihapus | Catatan Sekarang (keliru) | Usulan Catatan Perbaikan |
|:---:|---|---|
| `STI-423` Game Design dan Gamifikasi Sosial | "Unsur gamifikasi terserap parsial pada `STC-01` UX Research & `STC-04` XR" | "**Dihapus** dari K2026 (di luar positioning "Integrator AI"; ranah *game development* menjadi kewenangan Prodi TI). Materi gamifikasi **tidak diserap sebagai penyetaraan**; hanya disinggung sebagai satu pokok bahasan pada `STC-03` Pekan 9 (Gamifikasi Pembelajaran domain EdTech), sehingga **tidak memenuhi ambang E2**. Diakui sebagai kredit bebas 3 SKS. Mahasiswa yang berminat melanjutkan tema ini dapat mengambilnya sebagai topik Tugas Akhir Opsi 2 (Proyek Inovasi Produk Industri) atau Opsi 3 (Tech Startup Mandiri)." |
| `STI-638` Intelligent Signal Processing | "bertumpang dengan ranah riset algoritma Prodi TI, Dok. 016. Unsur ekstraksi fitur sinyal terserap parsial pada `STI-501` Deep Learning & `STA-06` Smart Surveillance" | "**Dihapus** dari K2026 (pengolahan sinyal digital merupakan ranah riset algoritma, bukan integrasi sistem). Materi pengolahan sinyal **tidak tercakup** pada MK K2026 mana pun; `STI-501` hanya memuat pemodelan deret waktu melalui LSTM/GRU dan `Feature Extraction` dalam konteks *transfer learning vision*, sehingga **tidak memenuhi ambang E2**. Diakui sebagai kredit bebas 3 SKS. Analitik data sensor tingkat aplikatif tersedia pada `STI-504` IoT dan `STA-06` Smart Surveillance & IoT Analytics, namun bukan sebagai penyetaraan." |

Rumusan ini memenuhi tiga syarat sekaligus: jujur secara faktual, tidak mengubah angka konsensus mana pun, dan tetap memberi arah bagi mahasiswa yang menanyakan kelanjutan tema tersebut.

### 6.2 REKOMENDASI KEDUA — HAPUS SITASI YANG TIDAK DAPAT DILACAK

Hapus frasa "Dok. 016" pada catatan `STI-638`, karena kedua MK ini tidak pernah dibahas di Dokumen 016 maupun 017 (Temuan 3). Alternatifnya, tambahkan pembahasan keduanya ke Dokumen 017 sebagai butir *scoping decision* — pilihan ini lebih kuat untuk kepentingan asesmen LAM INFOKOM karena penghapusan MK akan ditanyakan asesor.

### 6.3 OPSI LANJUTAN BILA PRODI MENGHENDAKI MATERI TETAP TERCAKUP

Kedua opsi berikut **bukan** ekivalensi, melainkan perluasan cakupan kurikulum. Keduanya menuntut revisi Dokumen 007 dan persetujuan Rapat Tim Kurikulum.

| Topik | MK Penampung Paling Layak | Dasar Kelayakan | Konsekuensi |
|---|---|---|---|
| Gamifikasi & desain perilaku | `STC-01` UX Research & Design (3 SKS, Sem 5, P3) | CPL `P4` (Arsitektur Informasi & Aksesibilitas) dan `KK5` (Riset UX) adalah CPL terdekat dengan desain perilaku pengguna; silabus telah memuat `Micro-Interactions Design` (Pekan 12) dan `onboarding` (Pekan 13) yang bertetangga secara konseptual | Menambah pokok bahasan pada Pekan 12 atau 13; tidak menambah SKS |
| Prapemrosesan sinyal sensor | `STI-504` Internet of Things (3 SKS, Sem 5, paket wajib) | Satu-satunya MK yang memuat sensor, telemetri, dan MQTT sekaligus, dan berstatus **paket wajib** sehingga menjangkau seluruh mahasiswa tanpa bergantung peminatan | Menambah pokok bahasan penapisan & normalisasi data sensor; tidak menambah SKS |

> [!NOTE]
> Bila opsi 6.3 dijalankan, status kedua MK lama **tetap E5**. Perluasan cakupan tidak otomatis menciptakan hak penyetaraan, karena penyetaraan menuntut kesetaraan capaian pembelajaran, bukan sekadar kehadiran topik.

---

## 7. STATUS TINDAK LANJUT

| No | Butir | Status |
|:---:|---|:---:|
| 1 | Analisis dan verifikasi terprogram | ✅ Selesai |
| 2 | Uji ambang E2 atas 5 kandidat MK pengganti | ✅ Selesai — seluruhnya gagal ambang |
| 3 | Perbaikan catatan `STI-423` pada Bagian 3.4 Dokumen 024 | ⏸️ Menunggu persetujuan (rumusan siap, Bagian 6.1) |
| 4 | Perbaikan catatan `STI-638` pada Bagian 3.6 Dokumen 024 | ⏸️ Menunggu persetujuan (rumusan siap, Bagian 6.1) |
| 5 | Penghapusan sitasi "Dok. 016" yang tidak dapat dilacak | ⏸️ Menunggu persetujuan |
| 6 | Perluasan cakupan gamifikasi pada `STC-01` | ⏸️ Kewenangan Rapat Tim Kurikulum |
| 7 | Perluasan cakupan sinyal sensor pada `STI-504` | ⏸️ Kewenangan Rapat Tim Kurikulum |

> [!IMPORTANT]
> **Dokumen 024 belum diubah.** Angka konsensus tetap: E1 34 MK / E2 11 MK / E3 8 MK / E4 1 MK / **E5 2 MK**, dengan simulasi pengakuan P1 = P2 = 120 SKS dan P3 = 117 SKS. Rekomendasi Bagian 6.1 dan 6.2 bersifat perbaikan redaksi dan **tidak mengubah satu pun angka tersebut**.

---
*Disahkan sebagai Dokumen Resmi 026 — Kurikulum OBE Revisi SISTEKIN 2026.*
**Tim Pengembang Kurikulum FSTI Universitas Widyagama Malang**
