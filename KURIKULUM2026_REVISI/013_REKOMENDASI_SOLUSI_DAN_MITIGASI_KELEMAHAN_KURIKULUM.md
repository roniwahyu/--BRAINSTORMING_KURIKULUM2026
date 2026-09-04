# 013 — REKOMENDASI STRATEGIS & SOLUSI MITIGASI KELEMAHAN KURIKULUM
## Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang

**Dokumen Resmi Rencana Mitigasi Risiko & Pedoman Implementasi Operasional Kurikulum OBE 2026**  
**Standar Rujukan:** Standar Penjaminan Mutu Internal (SPMI), Siklus PPEPP LAM INFOKOM, IABEE Criteria, dan Permendikbudristek No. 53 Tahun 2023.

---

## 1. PENDAHULUAN & PRINSIP PENETAPAN SOLUSI

Kurikulum OBE SISTEKIN 2026 dirancang dengan standar kompetensi tinggi untuk menjawab tantangan revolusi industri kecerdasan artifisial. Namun, keunggulan akademis ini membawa konsekuensi beban operasional dan kognitif yang signifikan.

Rekomendasi solusi dalam dokumen ini dibangun atas **4 Prinsip Utama**:
1. **Zero SKS Disruption:** Tidak mengubah total 146 SKS paket ditempuh atau struktur 8 semester yang telah ditetapkan.
2. **Pedagogical Efficiency:** Mengurangi redundansi tugas mahasiswa melalui integrasi lintas mata kuliah (*Cross-Course Project Integration*).
3. **Institutional Feasibility:** Menyesuaikan implementasi dengan kapasitas riil laboratorium, anggaran fakultas, dan rasio dosen.
4. **Student-Centered Flexibility:** Memberikan proteksi kelulusan tepat waktu melalui fleksibilitas MBKM dan semester antara remedial.

---

## 2. ARSITEKTUR SOLUSI 6 TITIK KRITIS KURIKULUM

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│               MATRIKS SINTESIS: 6 KELEMAHAN KRITIS VS 6 SOLUSI MITIGASI OPERASIONAL             │
├────┬────────────────────────────────────┬───────────────────────────────────────────────────────┤
│ No │ Area Kelemahan Kritis              │ Solusi Strategis & Kebijakan Operasional              │
├────┼────────────────────────────────────┼───────────────────────────────────────────────────────┤
│ 1  │ Overload Praktikum Sem 4 & 5       │ Skema "Integrated Cross-Course Studio Assignment"     │
│ 2  │ SPOF Rantai Prasyarat Koding Serial│ Kebijakan Semester Antara & Soft Prerequisite Rule    │
│ 3  │ Bentrok MBKM 20 SKS Semester 7     │ Ekuivalensi Multi-Track MBKM & Hybrid/Async Learning │
│ 4  │ Hardware AI & Cloud Cost Bottleneck│ Ekosistem Hybrid Compute & Lightweight AI Paradigm    │
│ 5  │ Kuota Minimum Kelas Peminatan      │ Dynamic Dual-Track System & Praktisi Mengajar         │
│ 6  │ Hidden Load MK 0 SKS (Agama & KWU) │ Micro-Learning Modular & Portfolio-Based Clearance    │
└────┴────────────────────────────────────┴───────────────────────────────────────────────────────┘
```

---

## 3. BEDAH DETAIL 6 SOLUSI STRATEGIS OPERASIONAL

---

### 💡 SOLUSI 1: Mengatasi Overload Praktikum Semester 4 & 5 via *Integrated Cross-Course Studio*

#### A. Identifikasi Masalah:
* Semester 4 memiliki 4 MK praktikum (+P), dan Semester 5 memiliki 5 MK praktikum (+P) ditambah KPM (3 SKS).
* Jika masing-masing dosen menugaskan proyek akhir mandiri, mahasiswa akan menanggung 4–5 proyek terpisah dalam rentang waktu pekan 12–16 yang memicu *burnout* dan penurunan kualitas karya.

#### B. Solusi Operasional:
Menerapkan kebijakan **Proyek Terpadu Antar-Mata Kuliah (*Cross-Course Joint Project*)**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   SKEMA PROYEK TERPADU SEMESTER 4 (PENGURANGAN BEBAN 50%)                        │
├──────────────────────────────────────┬───────────────────────────────────────────────────────────┤
│ Pasangan MK Terintegrasi             │ Bentuk Artefak Proyek Bersama                             │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────┤
│ STI-416 (Web Back End Development)   │ 1 Sistem Back-End API (NodeJS/FastAPI) yang membaca data  │
│                   +                  │ analitik dari skema Data Warehouse (PostgreSQL/BigQuery)  │
│ STI-415 (Data Warehouse & BI)        │ dan menyajikan endpoint dashboard teragregasi.            │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────┤
│ STI-413 (Machine Learning)           │ 1 Pipeline Analitik AI di mana model klasifikasi/regresi │
│                   +                  │ diterapkan pada data teks yang telah diproses oleh modul  │
│ STI-414 (Pengantar NLP & IR)         │ preprocessing dan TF-IDF/Embedding.                       │
└──────────────────────────────────────┴───────────────────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   SKEMA PROYEK TERPADU SEMESTER 5 & SINERGI KPM                                  │
├──────────────────────────────────────┬───────────────────────────────────────────────────────────┤
│ Pasangan MK Terintegrasi             │ Bentuk Artefak Proyek Bersama                             │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────┤
│ STI-521 (Internet of Things)         │ 1 Aplikasi Mobile (Flutter/React Native) yang berfungsi   │
│                   +                  │ sebagai antarmuka pemantauan sensor IoT secara real-time  │
│ STI-522 (Pemrograman Mobile)         │ via protokol MQTT/WebSocket.                              │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────┤
│ STI-519 (Deep Learning)              │ 1 Proyek Data Science Terintegrasi: ekstraksi fitur &     │
│                   +                  │ klastering data, dilanjutkan klasifikasi citra/sinyal     │
│ STI-520 (Data Mining & Visualisasi)  │ menggunakan Convolutional Neural Networks (CNN).          │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────┤
│ MKU-507 (KPM 3 SKS) Tematik          │ Produk IoT atau Mobile dari perkuliahan langsung dibawa   │
│                                      │ dan diimplementasikan pada desa mitra/UMKM KPM binaan.    │
└──────────────────────────────────────┴───────────────────────────────────────────────────────────┘
```

* **Dampak Positif:** Jumlah proyek berkurang dari 9 proyek terpisah menjadi 4 proyek komprehensif berkualitas tinggi yang layak masuk portofolio GitHub mahasiswa.

---

### 💡 SOLUSI 2: Mengatasi *Single Point of Failure (SPOF)* Prasyarat Koding

#### A. Identifikasi Masalah:
Rantai linier `STI-101 Algoritma` $\rightarrow$ `STI-205 OOP` $\rightarrow$ `STI-311 Front-End` $\rightarrow$ `STI-416 Back-End` $\rightarrow$ `STI-627 Platform` berisiko menunda kelulusan mahasiswa 1–2 tahun jika gagal di semester awal.

#### B. Solusi Operasional:
1. **Penerapan Kebijakan Dual Prerequisite (Hard vs Soft Prerequisite):**
   * **Hard Prerequisite (Nilai $\ge C$):** Hanya berlaku untuk transisi dari `STI-101 Algoritma` ke `FST-203 Struktur Data` dan `FST-205 OOP`.
   * **Soft / Advisory Prerequisite (Pernah Menempuh, Nilai $\ge D$):** Untuk MK lanjutan tingkat menengah (misal dari `STI-311 Web Front` ke `STI-416 Web Back` atau `STI-413 ML` ke `STI-519 Deep Learning`), mahasiswa yang mendapat nilai D diizinkan mengambil MK lanjutan secara paralel (*concurrent enrollment*) sambil mengulang ujian perbaikan.
2. **Penyelenggaraan Semester Antara / Remedial Bootcamp Khusus (Juli–Agustus):**
   * Fakultas secara rutin membuka Semester Antara dengan masa intensif 8 pekan khusus untuk 4 mata kuliah gerbang (*gateway courses*): `Algoritma & Pemrograman`, `OOP`, `Struktur Data`, dan `Matematika Diskrit`.

---

### 💡 SOLUSI 3: Ekuivalensi Penuh MBKM 20 SKS di Semester 6 & 7

#### A. Identifikasi Masalah:
Mahasiswa yang magang industri di luar kota berisiko terhambat presensi fisik pada mata kuliah wajib program studi dan bimbingan tugas akhir.

#### B. Solusi Operasional:
Menyusun **Paket Ekuivalensi Matriks MBKM 20 SKS Baku**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   TABEL KONVERSI RESMI MAGANG INDUSTRI MBKM (20 SKS)                             │
├───────────────────────┬─────┬─────────────────────────────────┬──────────────────────────────────┤
│ Komponen MBKM         │ SKS │ Mata Kuliah Ekuivalen di Sem 7  │ Bukti Asesmen Industri           │
├───────────────────────┼:---:┼─────────────────────────────────┼──────────────────────────────────┤
│ Proyek Rekayasa Teknis│  9  │ 3 MK Pilihan Peminatan (STA/B/C)│ Logbook, Source Code & Demo      │
│ Kinerja Profesional   │  3  │ FST-612 Praktik Kerja Lapangan  │ Lembar Evaluasi Mentor Industri  │
│ Capstone Produk Nyata │  3  │ FST-610 Capstone Project FSTI   │ Laporan Teknis Sistem Terpasang  │
│ Inovasi Proses Bisnis │  3  │ STI-728 Inovasi & Startup Dig.  │ Kajian Value Proposition & MVP   │
│ Proposal Proyek Akhir │  2  │ FST-613 Pra-Skripsi / Sempro    │ Draft Proposal Skripsi Industri  │
├───────────────────────┼:---:┼─────────────────────────────────┴──────────────────────────────────┤
│ TOTAL KONVERSI        │ 20  │ 100% SKS Semester 7 Terkonversi Penuh Tanpa Kuliah di Kampus       │
└───────────────────────┴:---:┴────────────────────────────────────────────────────────────────────┘
```

* **Dukungan LMS Asinkron:** Mahasiswa yang mengambil MBKM di luar paket 20 SKS penuh difasilitasi perkuliahan daring asinkron (rekaman video, materi di LMS Moodle/Google Classroom, kuis daring) sehingga tidak ada kendala presensi tatap muka.

---

### 💡 SOLUSI 4: Mengatasi *Hardware GPU & Cloud Cost Bottleneck*

#### A. Identifikasi Masalah:
Mata kuliah Deep Learning, MLOps, Computer Vision, dan Cloud Native membutuhkan daya komputasi tinggi yang berpotensi membebani anggaran prodi dan mahasiswa.

#### B. Solusi Operasional:
Menerapkan pendekatan **Tiga Tingkat Ekosistem Komputasi (*Tiered Compute Ecosystem*)**:

```
                  ┌─────────────────────────────────────────────────┐
                  │ TIER 3: ENTERPRISE AI LAB                       │
                  │ Workstation GPU Lokal FSTI (1-2 Server Fisik)   │
                  │ Digunakan untuk: Capstone & Skripsi Akhir       │
                  └────────────────────────┬────────────────────────┘
                                           │
                  ┌────────────────────────┴────────────────────────┐
                  │ TIER 2: ACADEMIC CLOUD ALLIANCE (GRATIS)        │
                  │ • AWS Academy • Google Cloud for Education      │
                  │ • GitHub Student Developer Pack ($200 Credits)  │
                  │ • Oracle Cloud Free Tier (4 OCPU ARM + 24GB)    │
                  └────────────────────────┬────────────────────────┘
                                           │
                  ┌────────────────────────┴────────────────────────┐
                  │ TIER 1: FREE CLOUD COMPUTE & LIGHTWEIGHT AI     │
                  │ • Google Colab Free Tier (T4 GPU)               │
                  │ • Kaggle Kernels (30 jam GPU P100/minggu)       │
                  │ • Model Ringan: TinyYOLO, MobileNet, Ollama     │
                  └─────────────────────────────────────────────────┘
```

* **Lightweight Model Rule:** Pada praktikum reguler mingguan, mahasiswa dilatih menggunakan arsitektur efisien (*Quantized 4-bit, DistilBERT, MobileNetV3, SQLite/DuckDB*) yang dapat berjalan pada laptop atau PC laboratorium standar tanpa memakan kuota cloud berbayar.

---

### 💡 SOLUSI 5: Menjamin Kelayakan Kuota Kelas Peminatan (*Class Viability*)

#### A. Identifikasi Masalah:
Penawaran 18 MK elektif (3 peminatan @ 6 MK) berisiko menghasilkan kelas kecil (4–6 orang) yang tidak memenuhi kuota efisiensi perkuliahan universitas ($\ge 10-15$ mahasiswa).

#### B. Solusi Operasional:
1. **Dynamic Dual-Track System:**
   * Di Semester 4, prodi menyelenggarakan pemetaan minat (*Talent & Interest Assessment*).
   * Dari 3 Peminatan, prodi mengaktifkan **2 Peminatan Utama (Mayor)** yang paling banyak dipilih mahasiswa pada angkatan tersebut, sedangkan peminatan ketiga dibuka dalam skema kolaboratif antar-perguruan tinggi (Pertukaran Mahasiswa MBKM).
2. **Program Praktisi Mengajar (Kemenristekdikti):**
   * Untuk mengatasi keterbatasan dosen internal pada mata kuliah mutakhir (*MLOps, SRE, Chaos Engineering, WebXR*), prodi secara rutin mengajukan hibah *Praktisi Mengajar* untuk menghadirkan CTO, DevOps Engineer, dan Lead Data Scientist dari industri.

---

### 💡 SOLUSI 6: Mengoptimalkan MK Non-SKS (Agama II & Kewirausahaan II)

#### A. Identifikasi Masalah:
`MKU-406 Agama II` dan `MKU-508 Kewirausahaan II` berbobot 0 SKS namun memakan waktu perkuliahan 100 menit/minggu di semester yang sudah sangat padat (21 SKS).

#### B. Solusi Operasional:
1. **Model Pembelajaran Micro-Learning Asinkron Modular:**
   * Perkuliahan tatap muka di kelas dikurangi menjadi 4x pertemuan utama (awal, tengah, dan akhir semester).
   * Sisa pertemuan dipenuhi melalui modul video pembelajaran mandiri pendek (10–15 menit) dan kuis refleksi di LMS.
2. **Portfolio-Based Clearance untuk Kewirausahaan II:**
   * Mahasiswa tidak diuji teori tertulis, melainkan cukup mengunggah *Pitch Deck* atau *Business Model Canvas (BMC)* yang selaras dengan proposal yang mereka susun di `STI-523 Manajemen Proyek TI` atau `STI-728 Inovasi Startup`.

---

## 4. MATRIKS RENCANA AKSI IMPLEMENTASI & MONITORING (PPEPP)

| Tahapan PPEPP | Langkah Aksi Mitigasi | Penanggung Jawab | Target Waktu | Indikator Keberhasilan |
|---|---|---|---|---|
| **Penetapan (P)** | Pengesahan SK Panduan Proyek Terpadu (*Integrated Assignment*) & Aturan Semester Antara | Dekan FSTI & Kaprodi SISTEKIN | Bulan ke-1 | Terbitnya Buku Panduan Operasional |
| **Pelaksanaan (P)** | Implementasi joint assignment di Sem 4 & Sem 5; Pemanfaatan AWS Academy & Colab | Tim Dosen Rumpun MK | Semester Berjalan | Penurunan tingkat stres & peningkatan mutu karya |
| **Evaluasi (E)** | Audit beban mahasiswa & survei kepuasan perkuliahan tengah semester | Gugus Kendali Mutu (GKM) FSTI | Pekan ke-8 (UTS) | $\ge 85\%$ mahasiswa merasa beban tugas proporsional |
| **Pengendalian (P)**| Rapat koordinasi dosen jika terjadi bentrok tugas akhir / kelebihan beban lab | Kaprodi & Sekprodi | Pekan ke-10 | Sinkronisasi ulang jadwal presentasi proyek |
| **Peningkatan (P)** | Pengajuan hibah Praktisi Mengajar dan penambahan lisensi cloud pendidikan | Dekanat & Tim Kurikulum | Tiap Akhir TA | Peningkatan akreditasi LAM INFOKOM & IABEE |

---

## 5. KESIMPULAN

Melalui **6 Solusi Strategis Operasional** di atas:
1. Kurikulum OBE SISTEKIN 2026 tetap **100% mempertahankan keunggulan visinya** (*AI, Smart Systems & Technopreneurship*).
2. Beban kerja mahasiswa Semester 4 dan 5 **terpangkas hingga 40–50%** berkat efisiensi penugasan terpadu.
3. Mahasiswa memiliki **jalur pengaman akademik yang kokoh** (*academic safety net*) sehingga risiko keterlambatan studi akibat gagal pada mata kuliah koding dasar dapat ditekan hingga $0\%$.

---
*Disahkan sebagai Dokumen Resmi 013 — Rekomendasi Solusi & Rencana Mitigasi Kurikulum SISTEKIN 2026.*  
**Tim Pengembang Kurikulum Program Studi Sistem dan Teknologi Informasi — FSTI Universitas Widyagama Malang**
