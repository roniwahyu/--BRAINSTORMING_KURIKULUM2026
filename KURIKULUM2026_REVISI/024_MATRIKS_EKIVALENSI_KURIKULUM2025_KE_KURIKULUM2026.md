# 024 — MATRIKS EKIVALENSI MATA KULIAH KURIKULUM 2025 → KURIKULUM 2026 (REVISI)
## Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang

**Dokumen Revisi Definitif Kurikulum 2026**
**Sumber Data Kurikulum Lama (GROUND TRUTH TUNGGAL):** `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` — Laporan resmi SIAKAD Universitas Widyagama Malang, Kurikulum 2025, **56 MK / 146 SKS**, 3 halaman, dicetak 05 Agustus 2026 oleh Syahroni Wahyu Iriananda, S.Kom., M.T. (`siakad.widyagama.ac.id/siakad/rep_kurikulumprodi`)
**Sumber Data Kurikulum Baru:** Dokumen 005 (Struktur 8 Semester), Dokumen 006 (Peminatan & MBKM), Dokumen 011 (Matriks CPL–MK 67 MK Portofolio)
**Standar Rujukan:** Permendikbudristek No. 53 Tahun 2023 (Pasal 24 tentang Pengakuan Hasil Belajar), Panduan KPT 2024 Ditjen Diktiristek, Panduan Kurikulum OBE APTIKOM v2.0.

> [!IMPORTANT]
> **Kaidah Ground Truth Kurikulum 2025.** Seluruh atribut mata kuliah Kurikulum 2025 pada dokumen ini — nomor urut, kode, nama, bobot SKS, nilai minimal, dan penempatan semester — **wajib bersumber langsung** dari PDF Laporan SIAKAD di atas. Tidak ada atribut K2025 yang boleh diturunkan dari dokumen antara, catatan rapat, ataupun ingatan penyusun. Setiap perubahan pada Bagian 3 dan Bagian 8 wajib divalidasi ulang dengan menjalankan:
>
> ```
> python _tools/verify_k2025_ground_truth.py
> ```
>
> Skrip tersebut membaca PDF SIAKAD secara langsung dan menggagalkan proses (exit code 1) bila ditemukan penyimpangan pada 8 butir uji: integritas ekstraksi PDF, header sebaran SKS per semester, kecocokan baris demi baris (nomor urut, nama, SKS), penempatan semester asal, Zero Orphan, neraca kategori E1–E5, validitas kode target K2026, serta presisi semester MK elektif peminatan.

---

## 1. RINGKASAN EKSEKUTIF

Kurikulum 2025 (K2025) memuat **56 Mata Kuliah / 146 SKS** yang seluruhnya berstatus wajib tanpa skema peminatan. Kurikulum 2026 Revisi (K2026) memuat **55 Mata Kuliah / 146 SKS paket ditempuh** dari **portofolio 67 MK / 182 SKS**, dengan 3 paket peminatan @ 18 SKS, jalur MBKM 20 SKS, dan 4 opsi Tugas Akhir non-skripsi.

### REKAPITULASI HASIL PEMETAAN EKIVALENSI

| Indikator Pemetaan | Jumlah MK | Jumlah SKS | Keterangan |
|---|:---:|:---:|---|
| MK K2025 ekuivalen penuh (E1) | 34 MK | 89 SKS | Konten identik / substantif sama, SKS baru ≤ SKS lama |
| MK K2025 ekuivalen bersyarat (E2) | 11 MK | 29 SKS | Overlap 60–85%, defisit SKS, atau penambahan praktikum → wajib uji penyetaraan |
| MK K2025 ekuivalen gabungan (E3) | 8 MK | 19 SKS | 4 klaster peleburan: 2 MK lama → 1 MK baru (menghasilkan 4 MK baru / 12 SKS) |
| MK K2025 ekuivalen pecah (E4) | 1 MK | 3 SKS | `STI-101` (3 SKS) dipecah menjadi `STI-101` (2) + `FST-101` (2) |
| MK K2025 tanpa padanan (E5) | 2 MK | 6 SKS | `STI-423` Game Design & Gamifikasi, `STI-638` Intelligent Signal Processing |
| **TOTAL MK KURIKULUM 2025** | **56 MK** | **146 SKS** | **Seluruh MK lama terpetakan (Zero Orphan)** |
| MK K2026 memiliki padanan K2025 | 49 MK | — | 73,1% dari 67 MK portofolio (rincian per semester: Bagian 3A) |
| MK K2026 **BARU** tanpa padanan | 18 MK | — | 5 MK wajib paket (14 SKS) + 13 MK elektif peminatan |
| **SKS diakui bagi lulusan penuh K2025** | — | **117–120 SKS** | Bergantung peminatan: P1/P2 = 120 SKS, P3 = 117 SKS |
| **Defisit yang wajib ditempuh** | — | **26–29 SKS** | 14 SKS MK wajib baru + 12–15 SKS elektif peminatan |

### STRUKTUR DOKUMEN INI (PETA NAVIGASI)

Matriks disusun dua arah agar dapat dipakai oleh dua pengguna berbeda:

| Kebutuhan Pengguna | Bagian yang Dibuka | Titik Tolak |
|---|---|---|
| Operator SIAKAD: "MK lama ini dikonversi ke mana?" | **Bagian 3** (matriks maju) dan **Bagian 8** (format entri basis data) | 56 MK Kurikulum 2025 |
| Dosen Penasihat Akademik: "MK baru ini bisa diakui dari MK lama apa? Apa yang wajib ditempuh mahasiswa saya?" | **Bagian 3A** (matriks rekognisi arah balik per semester) | 67 MK portofolio Kurikulum 2026 |
| Ketua Program Studi: "Berapa beban tambahan mahasiswa transisi?" | **Bagian 7** (simulasi pengakuan per skenario & tahap studi) | Paket 146 SKS Kurikulum 2026 |
| Tim Penjaminan Mutu: "Apakah pemetaan ini dapat dipertanggungjawabkan?" | **Bagian 9** (audit keterlacakan 17 butir) | PDF Laporan SIAKAD |

> [!IMPORTANT]
> **Tiga temuan kritis yang wajib ditindaklanjuti sebelum entri SIAKAD:**
> 1. **Kolisi kode MK:** kode `STI-102` dan `STI-103` dipakai untuk mata kuliah yang **berbeda** di K2025 dan K2026 (lihat Bagian 5). Tanpa pemisahan tahun kurikulum di basis data SIAKAD, konversi KHS akan salah petakan.
> 2. **Gap fondasi K2025:** K2025 **tidak memiliki** mata kuliah Jaringan Komputer maupun Arsitektur/Organisasi Komputer. Keduanya menjadi MK baru wajib (`STI-312`, `STI-103`) dan berstatus prasyarat bagi Cloud, IoT, dan Keamanan pada K2026.
> 3. **Perubahan prefiks fakultas:** MK berkode `MFT-xxx` pada K2025 bermigrasi ke prefiks `FST-xxx` pada K2026 (Bahasa Inggris, Metodologi Penelitian, PKL, Skripsi).

---

## 2. LEGENDA KATEGORI EKIVALENSI

| Kode | Kategori | Definisi Operasional | Konsekuensi Akademik |
|:---:|---|---|---|
| **E1** | Ekuivalen Penuh | Capaian pembelajaran substantif sama; SKS MK baru ≤ SKS MK lama | Nilai lama dialihkan langsung apa adanya |
| **E2** | Ekuivalen Bersyarat | Overlap konten 60–85%, atau SKS MK baru > SKS MK lama, atau MK lama tanpa praktikum sedangkan MK baru berpraktikum | Wajib **uji penyetaraan** (tugas mandiri terstruktur / portofolio / praktikum penyetaraan). Nilai maksimum yang dapat diakui adalah nilai lama |
| **E3** | Ekuivalen Gabungan | 2 MK lama dilebur menjadi 1 MK baru | Nilai baru = rata-rata berbobot SKS nilai MK lama; kelebihan SKS menjadi kredit bebas |
| **E4** | Ekuivalen Pecah | 1 MK lama menurunkan 2 MK baru | MK baru pertama diakui penuh; MK baru kedua diakui bersyarat |
| **E5** | Tanpa Padanan | Tidak ada MK K2026 dengan capaian pembelajaran setara | SKS diakui sebagai **kredit bebas** (tercatat pada transkrip, tidak mengurangi kewajiban paket 146 SKS) |
| **B** | MK Baru | MK K2026 tanpa asal-usul di K2025 | **Wajib ditempuh** oleh mahasiswa transisi |

---

## 3. MATRIKS EKIVALENSI UTAMA (ARAH K2025 → K2026)

> [!NOTE]
> **Kolom 1–4 (No, Kode K2025, Nama MK Kurikulum 2025, SKS) adalah kutipan verbatim PDF Laporan SIAKAD.** Nomor urut mengikuti penomoran 1–56 pada laporan asli; nama mata kuliah dan bobot SKS tidak dimodifikasi. Kolom 5 dan seterusnya merupakan hasil pemetaan tim kurikulum ke Kurikulum 2026.

### 3.0 REKAPITULASI GROUND TRUTH KURIKULUM 2025 (LAPORAN SIAKAD)

| Semester | Jumlah MK | Beban SKS | SKS Kumulatif | Status MK |
|:---:|:---:|:---:|:---:|:---:|
| Sem 1 | 7 MK | 18 SKS | 18 SKS | Seluruhnya Wajib |
| Sem 2 | 7 MK | 18 SKS | 36 SKS | Seluruhnya Wajib |
| Sem 3 | 8 MK | 20 SKS | 56 SKS | Seluruhnya Wajib |
| Sem 4 | 9 MK | 20 SKS | 76 SKS | Seluruhnya Wajib (termasuk `MKU-406` 0 SKS) |
| Sem 5 | 9 MK | 21 SKS | 97 SKS | Seluruhnya Wajib (termasuk `MKU-508` 0 SKS) |
| Sem 6 | 7 MK | 21 SKS | 118 SKS | Seluruhnya Wajib |
| Sem 7 | 7 MK | 20 SKS | 138 SKS | Seluruhnya Wajib |
| Sem 8 | 2 MK | 8 SKS | 146 SKS | Seluruhnya Wajib |
| **TOTAL** | **56 MK** | **146 SKS** | **146 SKS** | **Tanpa MK pilihan / peminatan** |

> Kurikulum 2025 **tidak mengenal mata kuliah pilihan**: kolom "Wajib/Pilihan" pada laporan SIAKAD bernilai `Wajib` untuk seluruh 56 MK, dan kolom "Paket?" bernilai `Tidak`. Nilai minimal kelulusan seluruh MK adalah **C**. Inilah dasar mengapa skema 3 peminatan pada K2026 sepenuhnya merupakan struktur baru.

### 3.1 EKIVALENSI MK SEMESTER 1 KURIKULUM 2025 (18 SKS)

| No | Kode K2025 | Nama MK Kurikulum 2025 | SKS | Kode K2026 | Nama MK Kurikulum 2026 (Revisi) | SKS | Smt | Kat | Catatan Penyetaraan |
|:---:|:---:|---|:---:|:---:|---|:---:|:---:|:---:|---|
| 1 | `MKU-101` | Agama I | 2 | `MKU-101` | Agama I | 2 | 1 | **E1** | Kode, nama, dan SKS identik |
| 2 | `MKU-102` | Pancasila | 2 | `MKU-102` | Pancasila | 2 | 1 | **E1** | Kode, nama, dan SKS identik |
| 3 | `MKU-103` | Bahasa Indonesia | 2 | `MKU-103` | Bahasa Indonesia | 2 | 1 | **E1** | Kode, nama, dan SKS identik |
| 4 | `STI-101` | Pengantar Sistem dan Teknologi Informasi | 3 | `STI-101` + `FST-101` | Pengantar Sistem & Teknologi Informasi (2) + Dasar Teknologi Digital (2) | 2+2 | 1 | **E4** | MK 3 SKS dipecah menjadi 2 MK @ 2 SKS. `STI-101` diakui penuh; `FST-101` diakui bersyarat (literasi digital & etika teknologi merupakan materi baru) |
| 5 | `STI-102` | Algoritma dan Pemrograman (+P) | 3 | `FST-102` | Algoritma dan Pemrograman (+P) | 3 | 1 | **E1** | Konten identik; **kode berubah** `STI-102` → `FST-102` (migrasi ke MK wajib fakultas). Perhatikan kolisi kode pada Bagian 5 |
| 6 | `STI-103` | Logika Informatika | 2 | `STI-204` | Matematika Diskrit dan Logika | 3 | 2 | **E3** | Dilebur bersama `STI-205` Matematika Diskrit — lihat klaster G-1 |
| 7 | `STI-104` | Kalkulus | 4 | `STI-102` | Kalkulus | 3 | 1 | **E1** | SKS diturunkan 4 → 3 (rasionalisasi Dok. 014). Selisih 1 SKS menjadi kredit bebas. **Kode berubah** `STI-104` → `STI-102` |

### 3.2 EKIVALENSI MK SEMESTER 2 KURIKULUM 2025 (18 SKS)

| No | Kode K2025 | Nama MK Kurikulum 2025 | SKS | Kode K2026 | Nama MK Kurikulum 2026 (Revisi) | SKS | Smt | Kat | Catatan Penyetaraan |
|:---:|:---:|---|:---:|:---:|---|:---:|:---:|:---:|---|
| 8 | `MFT-201` | Bahasa Inggris | 2 | `FST-205` | Basic English for IT | 2 | 2 | **E1** | Konten diperkuat konteks TI; **prefiks berubah** `MFT` → `FST` |
| 9 | `MKU-204` | Kewirausahaan I | 2 | `MKU-204` | Kewirausahaan I | 2 | 2 | **E1** | Kode, nama, dan SKS identik |
| 10 | `STI-205` | Matematika Diskrit | 2 | `STI-204` | Matematika Diskrit dan Logika | 3 | 2 | **E3** | Dilebur bersama `STI-103` Logika Informatika — lihat klaster G-1 |
| 11 | `STI-206` | Basis Data (+P) | 3 | `FST-207` | Sistem Basis Data (+P) | 3 | 2 | **E1** | Konten identik; **kode berubah** `STI-206` → `FST-207` |
| 12 | `STI-207` | Struktur Data | 3 | `FST-203` | Struktur Data dan Algoritma (+P) | 3 | 2 | **E2** | MK baru **berpraktikum** sedangkan MK lama teori murni → wajib praktikum penyetaraan (implementasi struktur data terprogram) |
| 13 | `STI-208` | Visualisasi Data dan Dashboard Interaktif (+P) | 2 | `STI-520` | Data Mining & Visualisasi Data (+P) | 3 | 5 | **E3** | Dilebur bersama `STI-740` Penambangan Data dan Visualisasi — lihat klaster G-2 |
| 14 | `STI-209` | Aljabar Linear | 4 | `STI-205` | Aljabar Linear dan Matriks | 3 | 2 | **E1** | SKS diturunkan 4 → 3 (rasionalisasi Dok. 014). Selisih 1 SKS menjadi kredit bebas |

### 3.3 EKIVALENSI MK SEMESTER 3 KURIKULUM 2025 (20 SKS)

| No | Kode K2025 | Nama MK Kurikulum 2025 | SKS | Kode K2026 | Nama MK Kurikulum 2026 (Revisi) | SKS | Smt | Kat | Catatan Penyetaraan |
|:---:|:---:|---|:---:|:---:|---|:---:|:---:|:---:|---|
| 15 | `STI-310` | Analisis dan Perancangan Sistem Informasi | 3 | `STI-306` | Analisis dan Perancangan Sistem Informasi | 3 | 3 | **E1** | Konten dan SKS identik; kode dinomorulang |
| 16 | `STI-311` | Sistem Operasi | 3 | `STI-310` | Sistem Operasi | 3 | 3 | **E1** | Konten dan SKS identik; kode dinomorulang |
| 17 | `STI-312` | Pemrograman Web (+P) | 3 | `STI-311` | Web Front End Development (+P) | 3 | 3 | **E2** | K2026 memisahkan front end dan back end. `STI-312` diakui sebagai `STI-311`; mahasiswa **tetap wajib** menempuh `STI-416` Web Back End Development (3 SKS) |
| 18 | `STI-313` | Keamanan Informasi Dasar | 2 | `STI-418` | Dasar Keamanan Informasi | 2 | 4 | **E1** | Nama dan SKS setara; posisi bergeser Sem 3 → Sem 4 |
| 19 | `STI-314` | Interaksi Manusia dan Komputer | 3 | `STI-308` | UI/UX Design & Prototyping (+P) | 3 | 3 | **E3** | Dilebur bersama `STI-635` Desain & Evaluasi Antarmuka Pengguna — lihat klaster G-3 |
| 20 | `STI-315` | Etika dan Hukum TI | 2 | `FST-206` | Etika Profesi & Hukum Digital | 2 | 2 | **E1** | Cakupan diperluas ke etika AI & pelindungan data pribadi; SKS setara |
| 21 | `STI-316` | Multimedia Interaktif | 2 | `STC-04` | Immersive Media & XR Development (+P) | 3 | 7 | **E3** | Dilebur bersama `STI-531` Augmented Reality dan Virtual Reality — lihat klaster G-4. Padanan berada pada **MK elektif Peminatan P3 (Sem 7)**, bukan MK wajib: diakui hanya bila mahasiswa memilih Peminatan P3, jika tidak dihitung sebagai kredit bebas |
| 22 | `STI-317` | Metode Komputasi dan Numerik | 2 | `STA-02` | Computational Methods & Numerics (+P) | 3 | 6 | **E2** | Padanan berada pada **MK elektif Peminatan P1 (Sem 6)**. Diakui hanya bila mahasiswa memilih Peminatan P1; jika tidak, dihitung sebagai kredit bebas. Defisit 1 SKS + komponen praktikum → uji penyetaraan |

### 3.4 EKIVALENSI MK SEMESTER 4 KURIKULUM 2025 (20 SKS)

| No | Kode K2025 | Nama MK Kurikulum 2025 | SKS | Kode K2026 | Nama MK Kurikulum 2026 (Revisi) | SKS | Smt | Kat | Catatan Penyetaraan |
|:---:|:---:|---|:---:|:---:|---|:---:|:---:|:---:|---|
| 23 | `MKU-405` | Kewarganegaraan | 2 | `MKU-405` | Kewarganegaraan | 2 | 4 | **E1** | Kode, nama, dan SKS identik |
| 24 | `MKU-406` | Agama II | 0 | `MKU-406` | Agama II | 0 | 4 | **E1** | MK 0 SKS kebijakan UWG; identik |
| 25 | `STI-418` | Sistem Cerdas | 2 | `STI-307` | Sistem Cerdas | 2 | 3 | **E1** | Nama dan SKS identik; posisi bergeser Sem 4 → Sem 3 |
| 26 | `STI-419` | Mobile Application Development (+P) | 3 | `STI-522` | Pemrograman Aplikasi Mobile (+P) | 3 | 5 | **E1** | Konten dan SKS setara; posisi bergeser Sem 4 → Sem 5 |
| 27 | `STI-420` | Semantic Web dan Ontologi | 2 | `STI-414` | Pengantar NLP & Information Retrieval (+P) | 2 | 4 | **E2** | Reorientasi materi: ontologi/RDF → NLP & temu kembali informasi. Overlap ± 60% (representasi pengetahuan & pengindeksan semantik) → wajib uji penyetaraan |
| 28 | `STI-421` | Manajemen Proyek TI | 2 | `STI-523` | Manajemen Proyek Teknologi Informasi | 3 | 5 | **E2** | SKS naik 2 → 3 (penambahan praktik alat manajemen proyek Agile) → wajib tugas penyetaraan 1 SKS |
| 29 | `STI-422` | E-Commerce dan Digital Business | 3 | `STI-728` | Inovasi Teknologi dan Startup Digital (+P) | 3 | 7 | **E2** | Reorientasi dari model bisnis e-commerce ke inovasi produk & startup (penegasan batas dengan Prodi Bisnis Digital). Overlap ± 65% → wajib uji penyetaraan |
| 30 | `STI-423` | Game Design dan Gamifikasi Sosial (+P) | 3 | — | *Tidak ada padanan* | — | — | **E5** | **Dihapus** dari K2026 (di luar positioning "Integrator AI"). Unsur gamifikasi terserap parsial pada `STC-01` UX Research & `STC-04` XR. Diakui sebagai kredit bebas 3 SKS |
| 31 | `STI-424` | Probabilitas dan Statistika | 3 | `FST-408` | Probabilitas dan Statistika | 3 | 4 | **E1** | Konten dan SKS identik; **kode berubah** `STI-424` → `FST-408` |

### 3.5 EKIVALENSI MK SEMESTER 5 KURIKULUM 2025 (21 SKS)

| No | Kode K2025 | Nama MK Kurikulum 2025 | SKS | Kode K2026 | Nama MK Kurikulum 2026 (Revisi) | SKS | Smt | Kat | Catatan Penyetaraan |
|:---:|:---:|---|:---:|:---:|---|:---:|:---:|:---:|---|
| 32 | `MKU-507` | Kuliah Pengabdian Kepada Masyarakat | 3 | `MKU-507` | Kuliah Pengabdian Kepada Masyarakat (KPM) | 3 | 5 | **E1** | Kode, nama, dan SKS identik |
| 33 | `MKU-508` | Kewirausahaan II | 0 | `MKU-508` | Kewirausahaan II | 0 | 5 | **E1** | MK 0 SKS kebijakan UWG; identik |
| 34 | `STI-525` | Pemrograman Lanjut dan API (+P) | 3 | `STI-416` | Web Back End Development (+P) | 3 | 4 | **E1** | Konten inti (REST API, layanan sisi server) setara; SKS identik; posisi bergeser Sem 5 → Sem 4 |
| 35 | `STI-526` | Internet of Things (+P) | 3 | `STI-521` | Internet of Things (IoT) (+P) | 3 | 5 | **E1** | Nama, SKS, dan semester identik |
| 36 | `STI-527` | Sistem Informasi Berbasis Cloud | 2 | `STI-417` | Komputasi Awan (Cloud Computing) | 3 | 4 | **E2** | SKS naik 2 → 3 dan orientasi bergeser dari pemanfaatan SI berbasis cloud ke arsitektur layanan cloud (IaaS/PaaS/SaaS) → wajib tugas penyetaraan |
| 37 | `STI-528` | Text Mining dan NLP | 2 | `STI-414` | Pengantar NLP & Information Retrieval (+P) | 2 | 4 | **E1** | Konten inti setara; **catatan:** apabila mahasiswa telah lulus `STI-528`, maka `STI-420` Semantic Web (baris 27) tidak lagi dapat diklaim untuk MK yang sama dan dialihkan menjadi kredit bebas |
| 38 | `STI-529` | Keamanan Jaringan dan Forensik Digital (+P) | 3 | `STB-01` | Network Security & Digital Forensics (+P) | 3 | 5 | **E1** | Padanan pada **MK elektif Peminatan P2 (Sem 5)**. Diakui penuh bila mahasiswa memilih Peminatan P2; jika tidak, dihitung sebagai kredit bebas |
| 39 | `STI-530` | Data Warehouse dan Business Intelligence (+P) | 3 | `STI-415` | Data Warehouse & Business Intelligence (+P) | 3 | 4 | **E1** | Nama dan SKS identik; posisi bergeser Sem 5 → Sem 4 |
| 40 | `STI-531` | Augmented Reality dan Virtual Reality (+P) | 2 | `STC-04` | Immersive Media & XR Development (+P) | 3 | 7 | **E3** | Dilebur bersama `STI-316` Multimedia Interaktif — lihat klaster G-4. Padanan berada pada MK elektif Peminatan P3 (Sem 7) |

### 3.6 EKIVALENSI MK SEMESTER 6 KURIKULUM 2025 (21 SKS)

| No | Kode K2025 | Nama MK Kurikulum 2025 | SKS | Kode K2026 | Nama MK Kurikulum 2026 (Revisi) | SKS | Smt | Kat | Catatan Penyetaraan |
|:---:|:---:|---|:---:|:---:|---|:---:|:---:|:---:|---|
| 41 | `STI-632` | Rekayasa Perangkat Lunak | 3 | `STI-309` | Rekayasa Perangkat Lunak | 3 | 3 | **E1** | Nama dan SKS identik; posisi bergeser Sem 6 → Sem 3 (penguatan fondasi rekayasa lebih dini) |
| 42 | `STI-633` | Sistem Pendukung Keputusan | 3 | `STA-01` | Decision Support Systems (+P) | 3 | 5 | **E1** | Padanan pada **MK elektif Peminatan P1 (Sem 5)**. Diakui penuh bila mahasiswa memilih Peminatan P1; jika tidak, dihitung sebagai kredit bebas |
| 43 | `STI-634` | Pengolahan Citra Digital dan Vision (+P) | 3 | `STI-519` | Deep Learning & Neural Networks (+P) | 3 | 5 | **E2** | K2026 mengintegrasikan computer vision ke dalam kerangka deep learning (CNN). Overlap ± 65% → wajib uji penyetaraan pada komponen arsitektur jaringan saraf & pelatihan model |
| 44 | `STI-635` | Desain dan Evaluasi Antarmuka Pengguna (UI/UX) (+P) | 3 | `STI-308` | UI/UX Design & Prototyping (+P) | 3 | 3 | **E3** | Dilebur bersama `STI-314` Interaksi Manusia dan Komputer — lihat klaster G-3 |
| 45 | `STI-636` | Machine Learning (+P) | 3 | `STI-413` | Machine Learning (+P) | 3 | 4 | **E1** | Nama dan SKS identik; posisi bergeser Sem 6 → Sem 4 |
| 46 | `STI-637` | Smart City dan Sistem Pemerintahan Digital | 3 | `STI-625` | Smart City & Pemerintahan Digital | 2 | 6 | **E1** | SKS diturunkan 3 → 2 (rasionalisasi Dok. 014). Selisih 1 SKS menjadi kredit bebas |
| 47 | `STI-638` | Intelligent Signal Processing | 3 | — | *Tidak ada padanan* | — | — | **E5** | **Dihapus** dari K2026 (bertumpang dengan ranah riset algoritma Prodi TI, Dok. 016). Unsur ekstraksi fitur sinyal terserap parsial pada `STI-519` Deep Learning & `STA-06` Smart Surveillance. Diakui sebagai kredit bebas 3 SKS |

### 3.7 EKIVALENSI MK SEMESTER 7 KURIKULUM 2025 (20 SKS)

| No | Kode K2025 | Nama MK Kurikulum 2025 | SKS | Kode K2026 | Nama MK Kurikulum 2026 (Revisi) | SKS | Smt | Kat | Catatan Penyetaraan |
|:---:|:---:|---|:---:|:---:|---|:---:|:---:|:---:|---|
| 48 | `MFT-002` | Metodologi Penelitian | 2 | `FST-611` | Metodologi Penelitian | 2 | 6 | **E1** | Nama dan SKS identik; **prefiks berubah** `MFT` → `FST`; posisi bergeser Sem 7 → Sem 6 |
| 49 | `MFT-003` | Praktik Kerja Lapangan | 3 | `FST-612` | Praktik Kerja Lapangan (PKL) | 3 | 7 | **E1** | Nama dan SKS identik; **prefiks berubah** `MFT` → `FST` |
| 50 | `STI-739` | Platform Literasi dan Edukasi Digital (+P) | 3 | `STI-627` | Digital Platform Engineering (+P) | 3 | 6 | **E2** | Reorientasi dari platform edukasi domain-spesifik ke rekayasa platform digital generik (arsitektur layanan, skalabilitas, DevOps dasar). Overlap ± 60% → wajib uji penyetaraan |
| 51 | `STI-740` | Penambangan Data dan Visualisasi (+P) | 3 | `STI-520` | Data Mining & Visualisasi Data (+P) | 3 | 5 | **E3** | Dilebur bersama `STI-208` Visualisasi Data dan Dashboard Interaktif — lihat klaster G-2 |
| 52 | `STI-741` | Integrasi Layanan Cerdas Berbasis AI | 3 | `STI-624` | Integrasi Layanan Cerdas Berbasis AI (+P) | 3 | 6 | **E2** | Nama dan SKS identik, namun MK baru **berpraktikum** (MK penciri prodi) → wajib praktikum penyetaraan (integrasi API model AI ke aplikasi nyata) |
| 53 | `STI-742` | Inovasi Teknologi dan Startup Digital | 3 | `STI-728` | Inovasi Teknologi dan Startup Digital (+P) | 3 | 7 | **E2** | Nama dan SKS identik, namun MK baru **berpraktikum** (validasi produk & pitching) → wajib praktikum penyetaraan. **Catatan:** apabila mahasiswa telah lulus `STI-742`, maka `STI-422` E-Commerce (baris 29) dialihkan menjadi kredit bebas |
| 54 | `STI-743` | Audit dan Tata Kelola Sistem Informasi | 3 | `STB-04` | IT Governance & Compliance (COBIT 2019) | 3 | 7 | **E1** | Padanan pada **MK elektif Peminatan P2 (Sem 7)**. Diakui penuh bila mahasiswa memilih Peminatan P2; jika tidak, dihitung sebagai kredit bebas |

### 3.8 EKIVALENSI MK SEMESTER 8 KURIKULUM 2025 (8 SKS)

| No | Kode K2025 | Nama MK Kurikulum 2025 | SKS | Kode K2026 | Nama MK Kurikulum 2026 (Revisi) | SKS | Smt | Kat | Catatan Penyetaraan |
|:---:|:---:|---|:---:|:---:|---|:---:|:---:|:---:|---|
| 55 | `MFT-004` | Skripsi | 6 | `FST-714` | Skripsi / Tugas Akhir | 6 | 8 | **E1** | SKS identik; **prefiks berubah** `MFT` → `FST`. K2026 menyediakan 4 opsi Tugas Akhir non-skripsi dengan bobot ekuivalen 6 SKS (Dok. 009) |
| 56 | `STI-844` | Pra Skripsi | 2 | `FST-613` | Pra-Skripsi / Seminar Proposal | 2 | 7 | **E1** | SKS identik; **kode berubah** `STI-844` → `FST-613`; posisi bergeser Sem 8 → Sem 7 |

### 3.9 VERIFIKASI KESEIMBANGAN MATRIKS EKIVALENSI

| Kategori | Jumlah MK K2025 | Total SKS K2025 | Status Verifikasi |
|:---:|:---:|:---:|---|
| E1 — Ekuivalen Penuh | 34 MK | 89 SKS | ✅ |
| E2 — Ekuivalen Bersyarat | 11 MK | 29 SKS | ✅ |
| E3 — Ekuivalen Gabungan | 8 MK | 19 SKS | ✅ |
| E4 — Ekuivalen Pecah | 1 MK | 3 SKS | ✅ |
| E5 — Tanpa Padanan | 2 MK | 6 SKS | ✅ |
| **TOTAL** | **56 MK** | **146 SKS** | ✅ **Cocok dengan Laporan SIAKAD K2025** |

---

## 3A. MATRIKS REKOGNISI ARAH BALIK (K2026 ← K2025) — PENYAMAAN VERSI PER SEMESTER

Bagian 3 memetakan **dari** Kurikulum 2025 (perspektif MK lama: "ke mana MK saya dikonversi?"). Bagian ini memetakan arah sebaliknya, **ke** Kurikulum 2026 (perspektif struktur baru: "MK ini bisa direkognisi dari MK lama yang mana?"), sehingga Dosen Penasihat Akademik dapat menyusun Kartu Rencana Studi mahasiswa transisi langsung per semester tanpa membaca ulang seluruh matriks.

### 3A.1 REKAPITULASI KELENGKAPAN REKOGNISI PORTOFOLIO 67 MK

| Status Rekognisi | Jumlah MK | Total SKS | Persentase Portofolio |
|---|:---:|:---:|:---:|
| MK K2026 dapat direkognisi dari K2025 | 49 MK | 129 SKS | 70,9% |
| MK K2026 **baru** — wajib ditempuh (tidak dapat direkognisi) | 18 MK | 53 SKS | 29,1% |
| **TOTAL PORTOFOLIO KURIKULUM 2026** | **67 MK** | **182 SKS** | **100,0%** |

Dari 49 MK yang dapat direkognisi, **43 MK** memiliki satu MK asal tunggal dan **6 MK** memiliki dua MK asal (4 klaster peleburan E3 ditambah 2 kasus klaim ganda).

### 3A.2 MATRIKS REKOGNISI PAKET WAJIB PER SEMESTER (49 MK / 128 SKS)

Kolom "Asal K2025" adalah MK yang **harus sudah lulus** (nilai ≥ C) agar MK K2026 dapat direkognisi.

#### SEMESTER 1 — Diakui 16 SKS, Defisit 3 SKS

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `MKU-101` | Agama I | 2 | E1 | `MKU-101` | Alih nilai langsung |
| `MKU-102` | Pancasila | 2 | E1 | `MKU-102` | Alih nilai langsung |
| `MKU-103` | Bahasa Indonesia | 2 | E1 | `MKU-103` | Alih nilai langsung |
| `STI-101` | Pengantar Sistem dan Teknologi Informasi | 2 | E4 | `STI-101` (3 SKS) | Alih nilai langsung (sisi pertama pemecahan) |
| `FST-101` | Dasar Teknologi Digital | 2 | E4 | `STI-101` (3 SKS) | **Uji penyetaraan** (sisi kedua pemecahan) |
| `FST-102` | Algoritma dan Pemrograman (+P) | 3 | E1 | `STI-102` | Alih nilai langsung — **awas kolisi kode** |
| `STI-102` | Kalkulus | 3 | E1 | `STI-104` (4 SKS) | Alih nilai; 1 SKS jadi kredit bebas |
| `STI-103` | Arsitektur dan Organisasi Sistem TI | 3 | **B** | — | **WAJIB TEMPUH** — gap fondasi K2025 |

#### SEMESTER 2 — Diakui 18 SKS, Defisit 2 SKS

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-204` | Matematika Diskrit dan Logika | 3 | E3/G-1 | `STI-103` + `STI-205` | Rata-rata berbobot 2 MK lama |
| `STI-205` | Aljabar Linear dan Matriks | 3 | E1 | `STI-209` (4 SKS) | Alih nilai; 1 SKS jadi kredit bebas |
| `FST-203` | Struktur Data dan Algoritma (+P) | 3 | E2 | `STI-207` | **Praktikum penyetaraan** |
| `FST-204` | Pengantar Kecerdasan Artifisial & Data | 2 | **B** | — | **WAJIB TEMPUH** — pintu masuk pipeline AI |
| `FST-205` | Basic English for IT | 2 | E1 | `MFT-201` | Alih nilai langsung |
| `FST-206` | Etika Profesi & Hukum Digital | 2 | E1 | `STI-315` | Alih nilai langsung |
| `FST-207` | Sistem Basis Data (+P) | 3 | E1 | `STI-206` | Alih nilai langsung |
| `MKU-204` | Kewirausahaan I | 2 | E1 | `MKU-204` | Alih nilai langsung |

#### SEMESTER 3 — Diakui 17 SKS, Defisit 3 SKS

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-306` | Analisis dan Perancangan Sistem Informasi | 3 | E1 | `STI-310` | Alih nilai langsung |
| `STI-307` | Sistem Cerdas | 2 | E1 | `STI-418` | Alih nilai langsung |
| `STI-308` | UI/UX Design & Prototyping (+P) | 3 | E3/G-3 | `STI-314` + `STI-635` | Rata-rata berbobot 2 MK lama |
| `STI-309` | Rekayasa Perangkat Lunak | 3 | E1 | `STI-632` | Alih nilai langsung |
| `STI-310` | Sistem Operasi | 3 | E1 | `STI-311` | Alih nilai langsung |
| `STI-311` | Web Front End Development (+P) | 3 | E2 | `STI-312` | **Uji penyetaraan** (pemisahan front/back end) |
| `STI-312` | Jaringan Komputer (+P) | 3 | **B** | — | **WAJIB TEMPUH** — prasyarat Cloud, IoT, Keamanan |

#### SEMESTER 4 — Diakui 21 SKS, Defisit 0 SKS ✅

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-413` | Machine Learning (+P) | 3 | E1 | `STI-636` | Alih nilai langsung |
| `STI-415` | Data Warehouse & Business Intelligence (+P) | 3 | E1 | `STI-530` | Alih nilai langsung |
| `STI-414` | Pengantar NLP & Information Retrieval (+P) | 2 | E1 | `STI-528` | Alih nilai; `STI-420` → kredit bebas |
| `STI-417` | Komputasi Awan (Cloud Computing) | 3 | E2 | `STI-527` (2 SKS) | **Tugas penyetaraan** 1 SKS |
| `STI-418` | Dasar Keamanan Informasi | 2 | E1 | `STI-313` | Alih nilai langsung |
| `STI-416` | Web Back End Development (+P) | 3 | E1 | `STI-525` | Alih nilai langsung |
| `FST-408` | Probabilitas dan Statistika | 3 | E1 | `STI-424` | Alih nilai langsung |
| `MKU-405` | Kewarganegaraan | 2 | E1 | `MKU-405` | Alih nilai langsung |
| `MKU-406` | Agama II | 0 | E1 | `MKU-406` | Alih nilai langsung |

#### SEMESTER 5 — Diakui 18 SKS Paket + 3 SKS Elektif, Defisit 0 SKS Paket ✅

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-519` | Deep Learning & Neural Networks (+P) | 3 | E2 | `STI-634` | **Uji penyetaraan** (CNN & pelatihan model) |
| `STI-520` | Data Mining & Visualisasi Data (+P) | 3 | E3/G-2 | `STI-208` + `STI-740` | Rata-rata berbobot 2 MK lama |
| `STI-521` | Internet of Things (IoT) (+P) | 3 | E1 | `STI-526` | Alih nilai langsung |
| `STI-522` | Pemrograman Aplikasi Mobile (+P) | 3 | E1 | `STI-419` | Alih nilai langsung |
| `STI-523` | Manajemen Proyek TI | 3 | E2 | `STI-421` (2 SKS) | **Tugas penyetaraan** 1 SKS |
| `MKU-507` | Kuliah Pengabdian Kepada Masyarakat (KPM) | 3 | E1 | `MKU-507` | Alih nilai langsung |
| `MKU-508` | Kewirausahaan II | 0 | E1 | `MKU-508` | Alih nilai langsung |
| *Elektif* | **MK Peminatan 1** | 3 | — | Lihat Bagian 6.3 | Bergantung jalur peminatan |

#### SEMESTER 6 — Diakui 10 SKS Paket + 6 SKS Elektif, Defisit 3 SKS Paket

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-624` | Integrasi Layanan Cerdas Berbasis AI (+P) | 3 | E2 | `STI-741` | **Praktikum penyetaraan** (MK penciri prodi) |
| `STI-625` | Smart City & Pemerintahan Digital | 2 | E1 | `STI-637` (3 SKS) | Alih nilai; 1 SKS jadi kredit bebas |
| `STI-626` | Keamanan Informasi Lanjut | 3 | **B** | — | **WAJIB TEMPUH** — jenjang keamanan lanjut |
| `STI-627` | Digital Platform Engineering (+P) | 3 | E2 | `STI-739` | **Uji penyetaraan** (reorientasi platform) |
| `FST-611` | Metodologi Penelitian | 2 | E1 | `MFT-002` | Alih nilai langsung |
| *Elektif* | **MK Peminatan 2 & 3** | 6 | — | Lihat Bagian 6.3 | Bergantung jalur peminatan |

#### SEMESTER 7 — Diakui 8 SKS Paket + 9 SKS Elektif, Defisit 3 SKS Paket

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `STI-728` | Inovasi Teknologi dan Startup Digital (+P) | 3 | E2 | `STI-742` | **Praktikum penyetaraan**; `STI-422` → kredit bebas |
| `FST-610` | Capstone Project FSTI (+P) | 3 | **B** | — | **WAJIB TEMPUH** — wahana asesmen 10 dari 14 CPL |
| `FST-612` | Praktik Kerja Lapangan (PKL) | 3 | E1 | `MFT-003` | Alih nilai langsung |
| `FST-613` | Pra-Skripsi / Seminar Proposal | 2 | E1 | `STI-844` | Alih nilai langsung |
| *Elektif* | **MK Peminatan 4, 5 & 6** | 9 | — | Lihat Bagian 6.3 | Bergantung jalur peminatan |

#### SEMESTER 8 — Diakui 6 SKS, Defisit 0 SKS ✅

| Kode K2026 | Nama Mata Kuliah | SKS | Kat | Asal K2025 | Tindakan Akademik |
|:---:|---|:---:|:---:|:---:|---|
| `FST-714` | Skripsi / Tugas Akhir | 6 | E1 | `MFT-004` | Alih nilai langsung; tersedia 4 opsi non-skripsi |

### 3A.3 NERACA REKOGNISI PAKET WAJIB PER SEMESTER

| Semester | SKS Paket K2026 | Diakui dari K2025 | Defisit | MK Wajib Baru | Persentase Diakui |
|:---:|:---:|:---:|:---:|---|:---:|
| Sem 1 | 19 | 16 | 3 | `STI-103` | 84,2% |
| Sem 2 | 20 | 18 | 2 | `FST-204` | 90,0% |
| Sem 3 | 20 | 17 | 3 | `STI-312` | 85,0% |
| Sem 4 | 21 | 21 | 0 | — | **100%** |
| Sem 5 | 18 (tanpa elektif) | 18 | 0 | — | **100%** |
| Sem 6 | 13 (tanpa elektif) | 10 | 3 | `STI-626` | 76,9% |
| Sem 7 | 11 (tanpa elektif) | 8 | 3 | `FST-610` | 72,7% |
| Sem 8 | 6 | 6 | 0 | — | **100%** |
| **TOTAL PAKET WAJIB** | **128** | **114** | **14** | **5 MK** | **89,1%** |

> [!IMPORTANT]
> **Semester 1 dan 3 adalah titik kritis penyisipan.** Dua dari tiga MK wajib baru (`STI-103` Arsitektur & Organisasi STI di Sem 1, dan `STI-312` Jaringan Komputer di Sem 3) merupakan **prasyarat berantai** bagi MK di semester berikutnya: `STI-103` menjadi prasyarat `STI-204`, `STI-310`, dan `STI-312`; sedangkan `STI-312` menjadi prasyarat `STI-417` Cloud, `STI-418` Keamanan, `STI-521` IoT, dan `STB-01` Network Security. Bagi mahasiswa transisi yang telah melewati Semester 3, kedua MK ini **wajib disisipkan paling lambat pada Semester 5** agar tidak memblokir MK lanjutan.

---

## 4. EMPAT KLASTER PELEBURAN MATA KULIAH (KATEGORI E3)

Peleburan dilakukan untuk menghapus redundansi materi yang teridentifikasi pada Audit Forensik Zero Redundancy (Dok. 017) dan Audit BoK APTIKOM (Dok. 016).

### 4.1 TABEL KLASTER PELEBURAN

| Klaster | MK Kurikulum 2025 yang Dilebur | SKS Lama | MK Kurikulum 2026 Hasil Peleburan | SKS Baru | Selisih | Rasional Peleburan |
|:---:|---|:---:|---|:---:|:---:|---|
| **G-1** | `STI-103` Logika Informatika (2) + `STI-205` Matematika Diskrit (2) | 4 | `STI-204` Matematika Diskrit dan Logika | 3 | −1 | Logika proposisi dan aljabar Boolean adalah subbagian kanonik Matematika Diskrit (BK-IS10). Pemisahan menimbulkan pengulangan materi ± 40% |
| **G-2** | `STI-208` Visualisasi Data & Dashboard Interaktif (2) + `STI-740` Penambangan Data dan Visualisasi (3) | 5 | `STI-520` Data Mining & Visualisasi Data | 3 | −2 | Visualisasi tanpa didahului penambangan data menyebabkan MK Sem 2 mengajarkan alat tanpa substansi analitik. Digabung pada Sem 5 setelah `STI-413` Machine Learning |
| **G-3** | `STI-314` Interaksi Manusia dan Komputer (3) + `STI-635` Desain & Evaluasi Antarmuka Pengguna UI/UX (3) | 6 | `STI-308` UI/UX Design & Prototyping | 3 | −3 | Dua MK mengampu BK yang sama (BK-IS13 / BK-IT09) dengan overlap ± 70%. Materi riset pengguna lanjutan dipindahkan ke elektif `STC-01` UX Research & Design |
| **G-4** | `STI-316` Multimedia Interaktif (2) + `STI-531` Augmented Reality dan Virtual Reality (2) | 4 | `STC-04` Immersive Media & XR Development | 3 | −1 | Multimedia interaktif merupakan prasyarat inheren pengembangan XR. Dipindahkan ke elektif Peminatan P3 karena bukan kompetensi inti "Integrator AI" |
| **TOTAL** | **8 MK Kurikulum 2025** | **19 SKS** | **4 MK Kurikulum 2026** | **12 SKS** | **−7 SKS** | Efisiensi 7 SKS direalokasi ke `STI-103` Arsitektur STI, `STI-312` Jaringan Komputer, dan `FST-204` Pengantar AI & Data |

### 4.2 ATURAN KONVERSI NILAI UNTUK KLASTER PELEBURAN

Nilai MK baru dihitung sebagai rata-rata berbobot SKS dari nilai kedua MK lama:

$$N_{\text{baru}} = \frac{(N_1 \times \text{SKS}_1) + (N_2 \times \text{SKS}_2)}{\text{SKS}_1 + \text{SKS}_2}$$

| Kondisi Kelulusan MK Lama | Perlakuan Konversi | Nilai Diakui |
|---|---|---|
| Kedua MK lama **lulus** (≥ C) | Konversi langsung dengan formula rata-rata berbobot | Hasil formula, dibulatkan ke huruf terdekat |
| Hanya **satu** MK lama lulus | Diakui **bersyarat (E2)** — wajib uji penyetaraan atas materi MK yang belum lulus | Maksimum nilai MK lama yang lulus |
| Kedua MK lama **belum lulus** | Tidak diakui | Wajib menempuh ulang MK baru secara penuh |
| Kelebihan SKS hasil peleburan (7 SKS) | Dicatat sebagai **kredit bebas** pada transkrip | Tidak mengurangi kewajiban paket 146 SKS |

---

## 5. PERINGATAN KOLISI KODE MATA KULIAH (WAJIB DITANGANI DI SIAKAD)

Terdapat **4 kode mata kuliah** yang dipakai untuk MK berbeda pada K2025 dan K2026. Tanpa pemisahan berbasis tahun kurikulum, konversi otomatis KHS akan salah petakan.

| Kode | Makna pada Kurikulum 2025 | SKS | Makna pada Kurikulum 2026 (Revisi) | SKS | Tingkat Risiko | Mitigasi Teknis |
|:---:|---|:---:|---|:---:|:---:|---|
| `STI-102` | Algoritma dan Pemrograman (+P) | 3 | **Kalkulus** | 3 | 🔴 **Tinggi** | Kunci pencarian SIAKAD **wajib** komposit `(tahun_kurikulum, kode_mk)`. Algoritma & Pemrograman K2025 dipetakan ke `FST-102`, bukan `STI-102` |
| `STI-103` | Logika Informatika | 2 | **Arsitektur dan Organisasi Sistem Teknologi Informasi** | 3 | 🔴 **Tinggi** | Logika Informatika K2025 dipetakan ke `STI-204` (klaster G-1). `STI-103` K2026 adalah **MK baru** yang wajib ditempuh |
| `STI-101` | Pengantar Sistem dan Teknologi Informasi | 3 | Pengantar Sistem & Teknologi Informasi | 2 | 🟡 **Sedang** | Nama sama, SKS berbeda (3 → 2). Pemetaan E4: `STI-101` (2) + `FST-101` (2) |
| `STI-418`/`STI-313` | Keamanan Informasi Dasar (`STI-313`) | 2 | Dasar Keamanan Informasi (`STI-418`) | 2 | 🟢 **Rendah** | Kode berbeda, tidak berkolisi. Dicatat sebagai perubahan penomoran murni |

> [!WARNING]
> **Prasyarat entri basis data SIAKAD:** Kurikulum 2026 **harus** diregistrasi sebagai entitas kurikulum terpisah (Kurikulum: 2026) dengan tabel pemetaan ekivalensi eksplisit. Penimpaan (overwrite) tabel MK Kurikulum 2025 akan merusak riwayat KHS seluruh angkatan aktif.

---

## 6. MATA KULIAH BARU KURIKULUM 2026 (TANPA PADANAN DI K2025)

### 6.1 MK WAJIB BARU — WAJIB DITEMPUH MAHASISWA TRANSISI (5 MK / 14 SKS)

| No | Kode K2026 | Nama Mata Kuliah | SKS | Smt | Kategori | Justifikasi Kemunculan |
|:---:|:---:|---|:---:|:---:|:---:|---|
| 1 | `STI-103` | Arsitektur dan Organisasi Sistem Teknologi Informasi | 3 | 1 | Core STI | **Gap fondasi kritis K2025.** K2025 tidak mengajarkan organisasi komputer, hierarki memori, maupun representasi data tingkat mesin (BK-IS03 / BK-IT05). Menjadi prasyarat `STI-310` Sistem Operasi dan `STI-312` Jaringan Komputer |
| 2 | `STI-312` | Jaringan Komputer (+P) | 3 | 3 | Core STI | **Gap fondasi kritis K2025.** K2025 melompat langsung ke `STI-529` Keamanan Jaringan tanpa MK jaringan komputer dasar. Prasyarat wajib bagi Cloud (`STI-417`), IoT (`STI-521`), dan Keamanan (`STI-418`) |
| 3 | `STI-626` | Keamanan Informasi Lanjut | 3 | 6 | Core STI | Penguatan jenjang keamanan bertingkat (dasar Sem 4 → lanjut Sem 6) untuk memenuhi CPL KK4 (audit, GRC & tata kelola TI) pada jalur wajib, tidak hanya elektif |
| 4 | `FST-204` | Pengantar Kecerdasan Artifisial & Data | 2 | 2 | FSTI | Pintu masuk pipeline AI 5 tahap (Dok. 016). K2025 baru menyentuh AI pada Sem 4 (`STI-418` Sistem Cerdas) tanpa MK pengantar konseptual |
| 5 | `FST-610` | Capstone Project FSTI (+P) | 3 | 7 | FSTI | **Wahana asesmen terintegrasi 10 dari 14 CPL** (Dok. 011 Sheet 5). K2025 tidak memiliki proyek integratif selain Skripsi |
| **TOTAL** | — | **MK Wajib Baru** | **14** | — | — | **Defisit minimum bagi seluruh mahasiswa transisi** |

### 6.2 MK ELEKTIF BARU PER PEMINATAN (13 MK / 39 SKS DITAWARKAN)

| Peminatan | MK Elektif Baru (Tanpa Padanan K2025) | Jml | MK Elektif dengan Padanan K2025 |
|---|---|:---:|---|
| **P1: Integrated Smart Systems** | `STA-03` Intelligent Agent Systems, `STA-04` MLOps and AI Pipeline, `STA-05` Conversational AI & Intelligent Assistant, `STA-06` Smart Surveillance & IoT Analytics | 4 | `STA-01` ← `STI-633` SPK; `STA-02` ← `STI-317` Metode Komputasi (E2) |
| **P2: Cloud Infrastructure & Cybersecurity** | `STB-02` Cloud Architecture & DevOps, `STB-03` Cybersecurity Risk Management, `STB-05` IT Service Management ITIL 4, `STB-06` Enterprise Architecture TOGAF | 4 | `STB-01` ← `STI-529` Keamanan Jaringan; `STB-04` ← `STI-743` Audit & Tata Kelola SI |
| **P3: Digital Platform Engineering** | `STC-01` UX Research & Design, `STC-02` Rekayasa & Otomasi Proses Bisnis, `STC-03` Rekayasa Aplikasi Industri Vertikal, `STC-05` SaaS Architecture & Multi-Tenancy, `STC-06` Digital Product Management & Agile | 5 | `STC-04` ← `STI-316` + `STI-531` (klaster G-4) |
| **TOTAL** | — | **13** | **5 MK elektif memiliki padanan** |

### 6.3 EKIVALENSI MK PEMINATAN MENURUT SEMESTER DEFINITIF (SEM 5–6–7)

Kolom **Smt** pada Bagian 3 kini merujuk semester definitif Dokumen 005 (pola tetap 1 MK di Sem 5, 2 MK di Sem 6, 3 MK di Sem 7 untuk setiap peminatan), bukan lagi rentang generik "Sem 5–7". Tabel berikut memetakan asal-usul K2025 dan prasyarat K2026 setiap MK elektif pada posisi semesternya.

| Smt | P1 — Integrated Smart Systems | Asal K2025 | P2 — Cloud Infra & Cybersecurity | Asal K2025 | P3 — Digital Platform Engineering | Asal K2025 |
|:---:|---|---|---|---|---|---|
| **5** | `STA-01` Decision Support Systems | `STI-633` SPK (**E1**) | `STB-01` Network Security & Digital Forensics | `STI-529` Keamanan Jaringan (**E1**) | `STC-01` UX Research & Design | — (**B**) |
| **6** | `STA-02` Computational Methods & Numerics | `STI-317` Metode Komputasi (**E2**) | `STB-02` Cloud Architecture & DevOps | — (**B**) | `STC-02` Rekayasa & Otomasi Proses Bisnis | — (**B**) |
| **6** | `STA-03` Intelligent Agent Systems | — (**B**) | `STB-03` Cybersecurity Risk Management | — (**B**) | `STC-03` Rekayasa Aplikasi Industri Vertikal | — (**B**) |
| **7** | `STA-04` MLOps and AI Pipeline | — (**B**) | `STB-04` IT Governance & Compliance COBIT 2019 | `STI-743` Audit & Tata Kelola SI (**E1**) | `STC-04` Immersive Media & XR Development | `STI-316` + `STI-531` (**E3**/G-4) |
| **7** | `STA-05` Conversational AI & Assistant | — (**B**) | `STB-05` IT Service Management ITIL 4 | — (**B**) | `STC-05` SaaS Architecture & Multi-Tenancy | — (**B**) |
| **7** | `STA-06` Smart Surveillance & IoT Analytics | — (**B**) | `STB-06` Enterprise Architecture TOGAF | — (**B**) | `STC-06` Digital Product Management & Agile | — (**B**) |
| **SKS diakui** | **6 SKS** (1 E1 + 1 E2) | — | **6 SKS** (2 E1) | — | **3 SKS** (1 E3) | — |
| **SKS defisit** | **12 SKS** (4 MK baru) | — | **12 SKS** (4 MK baru) | — | **15 SKS** (5 MK baru) | — |

> [!IMPORTANT]
> **Konsekuensi bagi mahasiswa transisi:** pengakuan MK elektif **bergantung pada peminatan yang dipilih**. MK K2025 yang berpadanan ke elektif di luar peminatan terpilih otomatis menjadi kredit bebas. Contoh: mahasiswa yang telah lulus `STI-633` SPK namun memilih Peminatan P2 tidak dapat mengklaim `STA-01`; 3 SKS tersebut dicatat sebagai kredit bebas.
>
> **Prasyarat elektif wajib dicek terpisah.** Empat MK elektif memiliki prasyarat pada MK wajib **baru** K2026 yang belum ditempuh mahasiswa transisi: `STB-01` membutuhkan `STI-312` Jaringan Komputer (MK baru), sedangkan `STA-04` membutuhkan `STI-624` yang berada pada semester yang sama sehingga perlu ditetapkan sebagai prasyarat lunak (concurrent) atau dihapus.

---

## 7. SIMULASI PENGAKUAN SKS BAGI MAHASISWA TRANSISI

### 7.1 SKENARIO A — MAHASISWA TELAH LULUS SELURUH 146 SKS KURIKULUM 2025

| Komponen Paket K2026 | SKS Paket | SKS Diakui | Defisit | Rincian MK Defisit |
|---|:---:|:---:|:---:|---|
| MKWU (8 MK) | 13 | **13** | 0 | — |
| MK Wajib FSTI (13 MK) | 36 | **31** | 5 | `FST-204` (2), `FST-610` (3) |
| MK Inti Core STI (28 MK) | 79 | **70** | 9 | `STI-103` (3), `STI-312` (3), `STI-626` (3) |
| MK Elektif Peminatan P1 (6 MK) | 18 | **6** | 12 | `STA-03`, `STA-04`, `STA-05`, `STA-06` |
| MK Elektif Peminatan P2 (6 MK) | 18 | **6** | 12 | `STB-02`, `STB-03`, `STB-05`, `STB-06` |
| MK Elektif Peminatan P3 (6 MK) | 18 | **3** | 15 | `STC-01`, `STC-02`, `STC-03`, `STC-05`, `STC-06` |
| **TOTAL (jalur P1 atau P2)** | **146** | **120** | **26** | Setara **1 semester penuh** |
| **TOTAL (jalur P3)** | **146** | **117** | **29** | Setara **1 semester penuh (21 SKS) + 8 SKS** |

> [!NOTE]
> **Rincian status pengakuan (jalur P1/P2):** Dari 114 SKS MK wajib yang diakui, **24 SKS berstatus bersyarat (E2)** dan mensyaratkan uji penyetaraan, yaitu `FST-203`, `STI-311`, `STI-417`, `STI-519`, `STI-523`, `STI-624`, `STI-627`, dan `STI-728`. Pada jalur P1 terdapat tambahan 3 SKS bersyarat (`STA-02`), sedangkan `FST-101` (2 SKS) bersyarat melalui skema E4.

### 7.1.1 NERACA SKS KURIKULUM 2025 SETELAH KONVERSI (146 SKS)

| Komponen Neraca | Jalur P1 | Jalur P2 | Jalur P3 | Uraian |
|---|:---:|:---:|:---:|---|
| SKS lama terpakai untuk konversi | 125 SKS | 126 SKS | 124 SKS | Total SKS MK K2025 yang berhasil diklaim ke MK K2026 |
| SKS lama menjadi **kredit bebas** | 21 SKS | 20 SKS | 22 SKS | MK K2025 tanpa klaim: E5 (6 SKS) + klaim ganda (5 SKS) + MK elektif di luar peminatan terpilih (9–11 SKS) |
| **TOTAL SKS KURIKULUM 2025** | **146** | **146** | **146** | Seluruh SKS lama terserap (Zero Orphan) |
| SKS K2026 diakui dari konversi | 120 SKS | 120 SKS | 117 SKS | Penyusutan 4–7 SKS akibat rasionalisasi SKS dan peleburan MK |
| SKS K2026 wajib ditempuh (defisit) | 26 SKS | 26 SKS | 29 SKS | Lihat tabel 7.1 |
| **TOTAL PAKET KURIKULUM 2026** | **146** | **146** | **146** | Ambang lulus minimum nasional 144 SKS terpenuhi |

### 7.2 SKENARIO B — MAHASISWA AKTIF PER TAHAP STUDI

| Tahap Studi saat Transisi | SKS K2025 Ditempuh | SKS Diakui K2026 | Defisit MK Wajib Baru | Rekomendasi Jalur |
|---|:---:|:---:|---|---|
| **Telah selesai Sem 1–2** | 36 SKS | ± 31 SKS | `STI-103` (3), `FST-204` (2), `STI-312` (3) | **Migrasi penuh ke K2026.** Sisipkan 3 MK baru secara bertahap pada Sem 3–4 (maksimum +3 SKS per semester) agar beban per semester tetap ≤ 22 SKS |
| **Telah selesai Sem 3–4** | 76 SKS | ± 66 SKS | `STI-103` (3), `STI-312` (3), `FST-204` (2), `FST-610` (3) | **Migrasi selektif.** `STI-103` dan `STI-312` wajib pada Sem 5 karena menjadi prasyarat Cloud, IoT, dan Keamanan; `FST-610` Capstone pada Sem 7 |
| **Telah selesai Sem 5–6** | 118 SKS | ± 106 SKS | `FST-610` (3) dan `STI-626` (3) atau ekuivalen | **Tetap pada K2025** dengan penyisipan `FST-610` Capstone Project FSTI sebagai pengganti 3 SKS MK pilihan. Migrasi penuh tidak efisien karena defisit melampaui 24 SKS |
| **Sedang menempuh Sem 7–8** | ≥ 138 SKS | ≥ 126 SKS | — | **Tetap pada K2025 hingga lulus.** Diberikan akses opsional pada 4 opsi Tugas Akhir non-skripsi (Dok. 009) sebagai ekuivalen `MFT-004` Skripsi 6 SKS |

> [!NOTE]
> Kolom "SKS Diakui K2026" pada Skenario B bersifat indikatif karena bergantung pada komposisi MK yang benar-benar lulus. Perhitungan definitif per mahasiswa dilakukan melalui Berita Acara Konversi individual berdasarkan tabel pada Bagian 8.

### 7.3 PRINSIP TATA KELOLA MASA TRANSISI

| No | Prinsip | Uraian Operasional |
|:---:|---|---|
| 1 | **Tanpa Kerugian Akademik** | Tidak ada mahasiswa yang mengalami penambahan masa studi akibat pemberlakuan K2026. Bila konversi menghasilkan defisit > 24 SKS bagi mahasiswa Sem ≥ 5, mahasiswa berhak menyelesaikan studi pada K2025 |
| 2 | **Ambang Kelulusan Tetap** | Syarat lulus tetap **minimum 144 SKS**; paket K2026 = 146 SKS (Permendikbudristek No. 53/2023) |
| 3 | **Nilai Minimum Konversi** | MK dapat dikonversi hanya bila nilai lama **≥ C** (sesuai kolom Nilai Minimal Laporan SIAKAD K2025) |
| 4 | **Perlakuan Kredit Bebas** | Kredit bebas hasil E5, klaim ganda, dan MK elektif di luar peminatan terpilih tercatat pada transkrip sebagai capaian tambahan, **tidak** dihitung sebagai pemenuhan paket 146 SKS, dan **tidak** menjadi dasar penolakan kelulusan |
| 5 | **Kewenangan Pengesahan** | Konversi disahkan oleh **Surat Keputusan Dekan FSTI** atas usulan Ketua Program Studi berdasarkan Berita Acara Rapat Tim Kurikulum |
| 6 | **Masa Berlaku Paralel** | K2025 dan K2026 berjalan paralel maksimum **4 tahun akademik** hingga angkatan terakhir K2025 lulus |
| 7 | **Mekanisme Uji Penyetaraan (E2)** | Bentuk: tugas mandiri terstruktur, portofolio bukti kerja, praktikum penyetaraan, atau ujian komprehensif. Diselenggarakan oleh dosen pengampu MK K2026, maksimum 2 kali kesempatan per MK |
| 8 | **Perekaman PDDikti** | Seluruh hasil konversi wajib direkam pada modul Pengakuan Hasil Belajar (RPL Internal) dan dilaporkan pada PDDikti sesuai Permendikbudristek No. 53/2023 Pasal 24 |

---

## 8. MATRIKS EKIVALENSI RINGKAS (FORMAT ENTRI SIAKAD)

Format satu baris per pasangan konversi, siap diimpor ke tabel `mk_ekivalensi` SIAKAD.

| Kode Lama | SKS Lama | Kode Baru | SKS Baru | Kat | Nilai Min | Uji Penyetaraan |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MKU-101` | 2 | `MKU-101` | 2 | E1 | C | Tidak |
| `MKU-102` | 2 | `MKU-102` | 2 | E1 | C | Tidak |
| `MKU-103` | 2 | `MKU-103` | 2 | E1 | C | Tidak |
| `MKU-204` | 2 | `MKU-204` | 2 | E1 | C | Tidak |
| `MKU-405` | 2 | `MKU-405` | 2 | E1 | C | Tidak |
| `MKU-406` | 0 | `MKU-406` | 0 | E1 | C | Tidak |
| `MKU-507` | 3 | `MKU-507` | 3 | E1 | C | Tidak |
| `MKU-508` | 0 | `MKU-508` | 0 | E1 | C | Tidak |
| `MFT-201` | 2 | `FST-205` | 2 | E1 | C | Tidak |
| `MFT-002` | 2 | `FST-611` | 2 | E1 | C | Tidak |
| `MFT-003` | 3 | `FST-612` | 3 | E1 | C | Tidak |
| `MFT-004` | 6 | `FST-714` | 6 | E1 | C | Tidak |
| `STI-101` | 3 | `STI-101` | 2 | E4 | C | Tidak |
| `STI-101` | 3 | `FST-101` | 2 | E4 | C | **Ya** |
| `STI-102` | 3 | `FST-102` | 3 | E1 | C | Tidak |
| `STI-103` | 2 | `STI-204` | 3 | E3/G-1 | C | Bersyarat |
| `STI-205` | 2 | `STI-204` | 3 | E3/G-1 | C | Bersyarat |
| `STI-104` | 4 | `STI-102` | 3 | E1 | C | Tidak |
| `STI-206` | 3 | `FST-207` | 3 | E1 | C | Tidak |
| `STI-207` | 3 | `FST-203` | 3 | E2 | C | **Ya** |
| `STI-208` | 2 | `STI-520` | 3 | E3/G-2 | C | Bersyarat |
| `STI-740` | 3 | `STI-520` | 3 | E3/G-2 | C | Bersyarat |
| `STI-209` | 4 | `STI-205` | 3 | E1 | C | Tidak |
| `STI-310` | 3 | `STI-306` | 3 | E1 | C | Tidak |
| `STI-311` | 3 | `STI-310` | 3 | E1 | C | Tidak |
| `STI-312` | 3 | `STI-311` | 3 | E2 | C | **Ya** |
| `STI-313` | 2 | `STI-418` | 2 | E1 | C | Tidak |
| `STI-314` | 3 | `STI-308` | 3 | E3/G-3 | C | Bersyarat |
| `STI-635` | 3 | `STI-308` | 3 | E3/G-3 | C | Bersyarat |
| `STI-315` | 2 | `FST-206` | 2 | E1 | C | Tidak |
| `STI-316` | 2 | `STC-04` | 3 | E3/G-4 | C | Bersyarat |
| `STI-531` | 2 | `STC-04` | 3 | E3/G-4 | C | Bersyarat |
| `STI-317` | 2 | `STA-02` | 3 | E2 | C | **Ya** |
| `STI-418` | 2 | `STI-307` | 2 | E1 | C | Tidak |
| `STI-419` | 3 | `STI-522` | 3 | E1 | C | Tidak |
| `STI-420` | 2 | `STI-414` | 2 | E2 | C | **Ya** |
| `STI-421` | 2 | `STI-523` | 3 | E2 | C | **Ya** |
| `STI-422` | 3 | `STI-728` | 3 | E2 | C | **Ya** |
| `STI-423` | 3 | — | — | E5 | — | Kredit Bebas |
| `STI-424` | 3 | `FST-408` | 3 | E1 | C | Tidak |
| `STI-525` | 3 | `STI-416` | 3 | E1 | C | Tidak |
| `STI-526` | 3 | `STI-521` | 3 | E1 | C | Tidak |
| `STI-527` | 2 | `STI-417` | 3 | E2 | C | **Ya** |
| `STI-528` | 2 | `STI-414` | 2 | E1 | C | Tidak |
| `STI-529` | 3 | `STB-01` | 3 | E1 | C | Tidak |
| `STI-530` | 3 | `STI-415` | 3 | E1 | C | Tidak |
| `STI-632` | 3 | `STI-309` | 3 | E1 | C | Tidak |
| `STI-633` | 3 | `STA-01` | 3 | E1 | C | Tidak |
| `STI-634` | 3 | `STI-519` | 3 | E2 | C | **Ya** |
| `STI-636` | 3 | `STI-413` | 3 | E1 | C | Tidak |
| `STI-637` | 3 | `STI-625` | 2 | E1 | C | Tidak |
| `STI-638` | 3 | — | — | E5 | — | Kredit Bebas |
| `STI-739` | 3 | `STI-627` | 3 | E2 | C | **Ya** |
| `STI-741` | 3 | `STI-624` | 3 | E2 | C | **Ya** |
| `STI-742` | 3 | `STI-728` | 3 | E2 | C | **Ya** |
| `STI-743` | 3 | `STB-04` | 3 | E1 | C | Tidak |
| `STI-844` | 2 | `FST-613` | 2 | E1 | C | Tidak |

> [!NOTE]
> **Aturan klaim ganda (double claim).** Dua pasangan konversi bermuara pada MK baru yang sama. Untuk setiap pasangan, hanya **satu** MK lama dapat diklaim; sisanya dialihkan menjadi kredit bebas. Urutan penentuan prioritas bersifat berjenjang:
>
> 1. **Kategori lebih kuat menang** — pasangan berkategori E1 mengalahkan E2.
> 2. **Bila kategori sama, kemiripan capaian pembelajaran yang lebih tinggi menang** (ditetapkan Tim Kurikulum).
>
> | MK Baru | Asal K2025 | Kategori | Klaim Diprioritaskan | Dialihkan ke Kredit Bebas | Dasar Penentuan |
> |:---:|---|:---:|:---:|:---:|---|
> | `STI-414` | `STI-528` Text Mining dan NLP | **E1** | ✅ `STI-528` | `STI-420` (2 SKS) | Jenjang 1: E1 mengalahkan E2 |
> | `STI-414` | `STI-420` Semantic Web dan Ontologi | E2 | — | — | — |
> | `STI-728` | `STI-742` Inovasi Teknologi dan Startup Digital | **E2** | ✅ `STI-742` | `STI-422` (3 SKS) | Jenjang 2: nama & capaian identik dengan MK baru, sedangkan `STI-422` hanya beririsan ± 65% |
> | `STI-728` | `STI-422` E-Commerce dan Digital Business | E2 | — | — | — |
>
> Konsekuensi: setiap mahasiswa kehilangan **5 SKS** dari 146 SKS lamanya akibat klaim ganda (2 SKS dari `STI-420` + 3 SKS dari `STI-422`), yang tercatat sebagai kredit bebas pada transkrip.

> [!WARNING]
> **Enam baris konversi bermuara ke MK elektif peminatan** (`STA-01`, `STA-02`, `STB-01`, `STB-04`, `STC-04`), sehingga **tidak dapat dikonversi otomatis** oleh SIAKAD. Baris-baris ini wajib diberi flag `butuh_peminatan = TRUE` dan hanya dieksekusi setelah mahasiswa menetapkan pilihan peminatan pada Semester 5.

| Kode Lama | SKS Lama | Kode Baru | SKS Baru | Smt Baru | Peminatan | Kat | Syarat Eksekusi |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| `STI-633` | 3 | `STA-01` | 3 | 5 | **P1** | E1 | Hanya bila mahasiswa memilih P1 |
| `STI-317` | 2 | `STA-02` | 3 | 6 | **P1** | E2 | Hanya bila memilih P1 + uji penyetaraan |
| `STI-529` | 3 | `STB-01` | 3 | 5 | **P2** | E1 | Hanya bila mahasiswa memilih P2 |
| `STI-743` | 3 | `STB-04` | 3 | 7 | **P2** | E1 | Hanya bila mahasiswa memilih P2 |
| `STI-316` | 2 | `STC-04` | 3 | 7 | **P3** | E3/G-4 | Hanya bila memilih P3 (klaster G-4) |
| `STI-531` | 2 | `STC-04` | 3 | 7 | **P3** | E3/G-4 | Hanya bila memilih P3 (klaster G-4) |

---

## 9. VERIFIKASI SILANG DOKUMEN (AUDIT KETERLACAKAN)

Verifikasi dijalankan secara terprogram oleh `_tools/verify_k2025_ground_truth.py`, yang membaca PDF Laporan SIAKAD K2025 **secara langsung** (bukan salinan atau ringkasan) dan membandingkannya dengan dokumen definitif K2026. Skrip mencakup 11 kelompok uji dan menghasilkan 17 butir verifikasi.

| # | Butir Verifikasi | Sumber Pembanding | Hasil |
|:---:|---|---|:---:|
| 1 | Jumlah MK K2025 = 56 MK | PDF Laporan SIAKAD, 3 halaman | ✅ **56 MK** |
| 2 | Total SKS K2025 = 146 SKS | PDF Laporan SIAKAD | ✅ **146 SKS** |
| 3 | Sebaran SKS per semester (18-18-20-20-21-21-20-8) | PDF Laporan SIAKAD | ✅ 8/8 semester cocok |
| 4 | Status seluruh MK = Wajib, Paket = Tidak, Nilai Min = C | PDF Laporan SIAKAD | ✅ Konsisten |
| 5 | Header seksi 3.1–3.8 sesuai sebaran PDF | Bagian 3 vs PDF | ✅ 8/8 header cocok |
| 6 | Nomor urut, nama MK, dan SKS tiap baris = PDF | Bagian 3 (56 baris) vs PDF | ✅ **0 ketidakcocokan** |
| 7 | Setiap baris berada di seksi semester asal yang benar | Bagian 3 vs kolom Semester PDF | ✅ **0 baris salah seksi** |
| 8 | Seluruh 56 MK K2025 terpetakan (Zero Orphan) | Bagian 8 vs PDF | ✅ **0 MK terlantar** |
| 9 | Tidak ada kode K2025 fiktif | Bagian 8 vs PDF | ✅ **0 kode fiktif** |
| 10 | SKS lama tiap baris konversi = PDF | Bagian 8 vs PDF | ✅ **0 ketidakcocokan** |
| 11 | Neraca kategori E1–E5 = 34/11/8/1/2 MK = 146 SKS | Bagian 8 vs Bagian 1 & 3.9 | ✅ Konsisten |
| 12 | Seluruh 49 kode target K2026 valid | Bagian 8 vs Dok 005 & 007 | ✅ **0 kode target fiktif** |
| 13 | Simulasi pengakuan SKS: P1 = P2 = 120, P3 = 117 | Rekalkulasi dari Bagian 8 | ✅ Cocok dengan Bagian 7.1 |
| 14 | Semester MK elektif = semester definitif Dok 005 | Bagian 3 & 6.3 vs Dok 005 §4 | ✅ **0 tidak presisi** |
| 15 | Neraca rekognisi arah balik = 114 diakui / 14 defisit SKS | Bagian 3A.3 vs Dok 005 & Bagian 8 | ✅ Cocok, 8/8 semester |
| 16 | Portofolio 67 MK: 49 dapat direkognisi, 18 baru | Bagian 3A.1 vs Dok 005 & 007 | ✅ **67 = 49 + 18** |
| 17 | Aturan klaim ganda tuntas (tidak ambigu) | Bagian 8 vs kaidah berjenjang | ✅ 2/2 kasus terselesaikan |

### 9.1 CATATAN KOLISI KODE PADA AUDIT OTOMATIS

Sebelas kode dipakai pada kedua kurikulum (`MKU-101`, `MKU-102`, `MKU-103`, `MKU-204`, `MKU-405`, `MKU-406`, `MKU-507`, `MKU-508`, `STI-101`, `STI-102`, `STI-103`). Audit otomatis karena itu **membatasi pemeriksaan atribut K2025 pada Bagian 3 dan Bagian 8 saja** — dua bagian yang secara definisi memuat sisi K2025 — dan tidak menandai kemunculan kode yang sama di bagian lain sebagai galat. Tiga kode di antaranya berisiko tinggi dan telah dirinci pada Bagian 5: `STI-102` (Algoritma & Pemrograman → Kalkulus), `STI-103` (Logika Informatika → Arsitektur & Organisasi STI), dan `STI-101` (SKS berubah 3 → 2).

### 9.2 SUMBER K2025 SEKUNDER YANG TELAH DIREKONSILIASI

| Berkas | Peran | Status Rekonsiliasi |
|---|---|:---:|
| `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` | **Ground truth tunggal** atribut MK (kode, nama, SKS, semester) | ✅ Rujukan primer |
| `KURIKULUM2025/obe_pdf_extract/Implementasi_Modul_OBE_SISTEKIN2025_TABLES.md` | Sumber CPL/CPMK & IRM K2025 | ✅ 56/56 kode cocok, 0 konflik SKS |
| `KURIKULUM2025/Implementasi_MODUL_OBE_SISTEKIN2025.pdf` | Dokumen modul OBE K2025 | ✅ Selaras (via ekstraksi di atas) |
| `KURIKULUM2025/Notulensi Rapat VMTS & Kurikulum ... .pdf` | Notulensi rapat | ⚠️ **Bukan** ground truth atribut MK |

### 9.3 KONSISTENSI DUA ARAH MATRIKS (BIDIRECTIONAL BALANCE)

Matriks ini menyediakan dua perspektif atas satu himpunan pemetaan yang sama. Keduanya wajib berjumlah sama:

| Perspektif | Bagian | Titik Tolak | Neraca |
|---|:---:|---|---|
| **Maju** (K2025 → K2026) | Bagian 3 & 8 | 56 MK / 146 SKS Kurikulum 2025 | Seluruh 56 MK terpetakan: 34 E1 + 11 E2 + 8 E3 + 1 E4 + 2 E5 |
| **Balik** (K2026 ← K2025) | Bagian 3A | 67 MK / 182 SKS portofolio Kurikulum 2026 | 49 MK dapat direkognisi + 18 MK baru wajib ditempuh |
| **Titik temu** | Bagian 7 | Paket 146 SKS Kurikulum 2026 | 120 SKS diakui (P1/P2) atau 117 SKS (P3); defisit 26 atau 29 SKS |

Ketiga baris di atas telah diverifikasi saling konsisten secara terprogram (butir 11, 13, 15, dan 16 pada tabel 9). Perbedaan angka antar perspektif bukan inkonsistensi, melainkan konsekuensi dari tiga mekanisme yang sudah terdokumentasi: rasionalisasi SKS (Kalkulus 4→3, Aljabar Linear 4→3, Smart City 3→2), peleburan empat klaster E3 (−7 SKS), dan aturan klaim ganda (−5 SKS).

---
*Disahkan sebagai Dokumen Resmi 024 — Kurikulum OBE Revisi SISTEKIN 2026.*
**Tim Pengembang Kurikulum FSTI Universitas Widyagama Malang**
