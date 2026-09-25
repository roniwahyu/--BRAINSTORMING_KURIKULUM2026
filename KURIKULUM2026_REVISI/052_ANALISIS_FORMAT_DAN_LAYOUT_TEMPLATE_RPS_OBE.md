# 052 — ANALISIS FORMAT DAN LAYOUT TEMPLATE RENCANA PEMBELAJARAN SEMESTER (RPS) OBE FSTI UWG

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Status Dokumen:** Laporan Audit Desain, Geometri Layout, dan Kamus Tag Generator RPS OBE  
**Tanggal:** 25 September 2026  
**Penyusun:** Tim Pengembang Kurikulum SISTEKIN & Asesor Internal Mutu Akademik  

---

## 1. Eksekutif Ringkasan & Ruang Lingkup

Laporan ini menyajikan hasil forensik visual, struktural, dan arsitektural atas dokumen template resmi Rencana Pembelajaran Semester (RPS) berbasis *Outcome-Based Education* (OBE) di lingkungan Universitas Widyagama Malang, yang bersumber dari:
1. `0001_Template_RPS_OBE.pdf` (11 Halaman — Sampel Riil Terisi untuk MK Dasar Pemrograman Komputer `MSN-315`).
2. `Template_RPS_GEN_2026_20092026-SWI.pdf` (9 Halaman — Template Master Generator ber-tag placeholder).
3. `Template_RPS_GEN_2026_20092026-SWO.docx` (Template Master Microsoft Word ber-tag placeholder).
4. `0003_PROMPT - BUAT RPS OBE With AI.pdf` (Pedoman Prompt Konstruktif AI untuk Penyusunan RPS OBE).

Tujuan analisis ini adalah untuk membongkar secara presisi tata letak (*layout*), orientasi halaman (*page geometry*), hirarki tabel, skema pembobotan, instrumen evaluasi lampiran, serta memetakan seluruh *placeholder* variabel guna membangun mesin automasi generator RPS (*RPS Batch Generator*) untuk seluruh **67 mata kuliah portofolio Kurikulum SISTEKIN 2026**.

---

## 2. Geometri & Orientasi Halaman (*Hybrid Orientation Architecture*)

Dokumen RPS OBE UWG menggunakan pendekatan desain **Tata Letak Campuran (*Hybrid Orientation*)**, yaitu menggabungkan halaman bertipe *Landscape* untuk tabel matriks perkuliahan yang lebar, dan halaman *Portrait* untuk instrumen soal/rubrik evaluasi dan lembar tanda tangan pengesahan.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        DOKUMEN RPS LENGKAP                             │
├───────────────────────────────────┬────────────────────────────────────┤
│   BAGIAN 1: MATRIKS KURIKULER     │    BAGIAN 2: INSTRUMEN ASESMEN     │
│       (Halaman Landscape)         │        (Halaman Portrait)          │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Hal 1: Cover Judul RPS          │ • Hal 5: Lampiran Tugas 1 + Rubrik │
│ • Hal 2: Identitas, Otorisasi,    │ • Hal 6: Lampiran UTS + Rubrik     │
│          CPL, CPMK, Korelasi CPL- │ • Hal 7: Lampiran Tugas 2 + Rubrik │
│          CPMK, Deskripsi MK       │ • Hal 8: Lampiran UAS + Rubrik     │
│ • Hal 3-4: Bahan Kajian, Pustaka, │ • Hal 9: Lembar Validasi UPM,      │
│            Dosen, Prasyarat, &    │          Dosen, dan Pengesahan     │
│            Tabel 16 Pertemuan     │          Ketua Program Studi       │
│            (8 Kolom Baku)         │                                    │
└───────────────────────────────────┴────────────────────────────────────┘
```

### Parameter Ukuran Halaman:
* **Halaman Landscape (Hal 1 s.d. 4):**
  * Ukuran Standar: A4 Landscape (Lebar = `841.7 pt` / `297 mm`, Tinggi = `595.4 pt` / `210 mm`).
  * Margin: Kiri `25 mm`, Kanan `20 mm`, Atas `20 mm`, Bawah `20 mm`.
  * Rasio Grid: Memfasilitasi tabel rencana mingguan dengan 8 kolom tanpa pemotongan teks ekstrem.
* **Halaman Portrait (Hal 5 s.d. 9):**
  * Ukuran Standar: A4 Portrait (Lebar = `595.4 pt` / `210 mm`, Tinggi = `841.7 pt` / `297 mm`).
  * Margin: Kiri `25 mm`, Kanan `20 mm`, Atas `25 mm`, Bawah `25 mm`.
  * Rasio Grid: Format baku soal ujian, tabel kriteria rubrik bertingkat, dan blok otorisasi tanda tangan pejabat.

---

## 3. Anatomi Struktural & Bedah Komponen Dokumen

### Bagian I: Halaman Sampul Depan (Cover — Hal 1, Landscape)
* **Judul Utama:** `RENCANA PEMBELAJARAN SEMESTER (RPS)`
* **Penyusun:** Nama Dosen Pengampu (`{{namadosen}}`) dan Nomor Induk / NUPTK (`{{nuptk}}`).
* **Institusi:** `UNIVERSITAS WIDYA GAMA MALANG`
* **Periode Penetapan:** Bulan dan Tahun Akademik (misal: `AGUSTUS, 2026`).

---

### Bagian II: Identitas, Otorisasi, & Capaian Pembelajaran (Hal 2, Landscape)

#### 1. Header Dokumen Penjaminan Mutu
* **Kolom Kiri:** Logo Resmi Universitas Widyagama Malang.
* **Kolom Tengah:**
  * Institusi: `UNIVERSITAS WIDYA GAMA`
  * Fakultas: `FAKULTAS SAINS DAN TEKNOLOGI INFORMASI`
  * Program Studi: `PROGRAM STUDI S1 SISTEM DAN TEKNOLOGI INFORMASI`
* **Kolom Kanan:** Nomor Dokumen Sistem Penjaminan Mutu Internal (SPMI): `071030.{{kodeprodi}}` (Contoh riil: `071030.B4.5.2.RPS-xxx`).
* **Sub-Header:** `RENCANA PEMBELAJARAN SEMESTER`

#### 2. Tabel Identitas Mata Kuliah
Tabel terbagi menjadi 6 sel atribut fundamental:
1. `MATA KULIAH (MK)`: Nama Mata Kuliah resmi (`{{namamk}}`).
2. `KODE`: Kode Mata Kuliah baku Kurikulum 2026 (`{{kodemk}}`, misal `STI-101`, `FST-207`, dll.).
3. `Rumpun MK`: Rumpun keilmuan (`{{rumpunmk}}`, misal: Mata Kuliah Dasar Sains FSTI, Core STI, Peminatan Smart Systems).
4. `BOBOT (sks)`: Terbagi tegas antara Teori dan Praktikum (`T={{skst}} P={{sksp}}`).
5. `SEMESTER`: Semester pelaksanaan (`{{sms}}`, Gasal/Genap, Semester 1 s.d. 8).
6. `Tgl Penyusunan`: Tanggal penetapan formal RPS (`{{tglsusun}}`).

#### 3. Blok Otorisasi Dokumen (3 Kolom Sejajar)
* **Pengembang RPS:** `{{pengembangrps}}`
* **Koordinator RMK:** `{{koordinatormk}}`
* **Ketua Program Studi:** `{{ketuaprodi}}`

#### 4. Blok Capaian Pembelajaran (CP)
* **CPL-PRODI yang dibebankan pada MK:**
  * Daftar kode dan rumusan CPL (menggunakan looping `[nocpl]` dan `[cpl]`).
* **Capaian Pembelajaran Mata Kuliah (CPMK):**
  * Rumusan CPMK berorientasi mahasiswa dengan formula Taksonomi Bloom C2 s.d. C6 (looping `[nocpmk]` dan `[cpmk]`).
* **Sub-CPMK:**
  * Penjabaran kemampuan akhir tiap tahapan belajar mingguan (looping `[nosubcpmk]` dan `[subcpmk]`).
* **Matriks Korelasi CPL terhadap CPMK & Bobot Penilaian:**
  * Tabel silang yang memetakan relasi CPL vs CPMK lengkap dengan persentase bobot sumatif, jumlah minggu pembelajaran, dan bentuk asesmen (`[tabelkolerasi]`).

#### 5. Deskripsi Singkat MK & Bahan Kajian
* **Deskripsi Singkat MK (`{{deskripsimk}}`):** Uraian naratif 150–200 kata mengenai ruang lingkup, posisi strategis, keterkaitan dengan profil lulusan STI, dan modus perkuliahan (teori/praktik).
* **Bahan Kajian (`{{bahankajian}}`):** Pokok-pokok bahasan keilmuan yang dipetakan langsung ke Sub-CPMK.

#### 6. Pustaka, Dosen Pengampu & Matakuliah Prasyarat
* **Pustaka Utama (`[pustakautama]`):** Buku teks primer ber-ISBN edisi mutakhir (maksimal 5–10 tahun terakhir).
* **Pustaka Pendukung (`[pustakapendukung]`):** Artikel jurnal bereputasi, prosiding konferensi IEEE/ACM, atau dokumentasi resmi standar industri.
* **Dosen Pengampu (`{{dosenpengampu}}`):** Nama dosen/tim pengampu berserta gelar akademik lengkap.
* **Matakuliah Syarat (`{{mkprasyarat}}`):** Kode & nama mata kuliah prasyarat akademik (atau tanda `-` jika tidak ada).

---

### Bagian III: Matriks Tabel Rencana Pembelajaran 16 Minggu (Hal 3 s.d. 4, Landscape)

Tabel rencana pembelajaran adalah instrumen utama RPS, mengadopsi standar baku SN-DIKTI dengan **8 Kolom Operasional**:

| Kolom | Header Kolom | Deskripsi Isi Konten | Tag Generator |
|:---:|---|---|:---:|
| **(1)** | **Mg ke-** | Nomor minggu perkuliahan (1 s.d. 16) | `[mingguke]` |
| **(2)** | **Kemampuan akhir tiap tahapan belajar (Sub-CPMK)** | Rumusan Sub-CPMK terukur menggunakan Kata Kerja Operasional (KKO) Taksonomi Bloom Revisi + formula ABCD | `[kemampuan_subcpmk]` |
| **(3)** | **Penilaian: Indikator** | Indikator unjuk kerja spesifik mahasiswa (misal: *1.1 Ketepatan merancang model...*) | `[indikator]` |
| **(4)** | **Penilaian: Kriteria & Teknik** | Kriteria penilaian (Rubrik Analitik/Holistik/Skala) dan Teknik penilaian (Tes: Pilihan ganda, esai; Non-tes: Unjuk kerja praktikum, presentasi proyek, laporan studi kasus) | `[kriteriateknik]` |
| **(5)** | **Bentuk, Metode Pembelajaran & Penugasan Mahasiswa [Estimasi Waktu] — Luring (offline)** | Moda tatap muka (Kuliah, Diskusi Kelas, Praktikum Lab) dilengkapi durasi baku menit: `TM: ... menit`, `PT: ... menit`, `BM: ... menit` | `[luring]` |
| **(6)** | **Bentuk, Metode Pembelajaran & Penugasan Mahasiswa [Estimasi Waktu] — Daring (online)** | Moda pembelajaran mandiri/terbimbing via LMS (Edlink, Moodle, Google Classroom, asynchronous forum) | `[daring]` |
| **(7)** | **Materi Pembelajaran [Pustaka]** | Rincian pokok bahasan mingguan beserta tautan sitasi nomor pustaka & bab/halaman referensi (misal: `[1] Bab 3, hal 45-60`) | `[materi]` |
| **(8)** | **Bobot Penilaian (%)** | Persentase kontribusi asesmen minggu tersebut terhadap akumulasi total 100% nilai akhir mata kuliah | `[bobot_nilai]` |

#### Titik Evaluasi Khusus:
* **Minggu ke-8:** Baris penghentian materi untuk pelaksanaan **Evaluasi Tengah Semester / Ujian Tengah Semester (UTS)**.
* **Minggu ke-16:** Baris penutupan perkuliahan untuk pelaksanaan **Evaluasi Akhir Semester / Ujian Akhir Semester (UAS)**.
* **Total Bobot Penilaian:** Diberikan baris agregasi akhir `Total bobot penilaian: 100%`.
* **Catatan Kaki Waktu Pembelajaran:** Diberikan singkatan standar:
  * `TM`: Tatap Muka ($1\text{ SKS} = 50\text{ menit/pekan}$)
  * `PT`: Penugasan Terstruktur ($1\text{ SKS} = 60\text{ menit/pekan}$)
  * `BM`: Belajar Mandiri ($1\text{ SKS} = 60\text{ menit/pekan}$)
  * *Praktikum/Responsi:* ($1\text{ SKS} = 170\text{ menit/pekan}$)

---

### Bagian IV: Lampiran Instrumen Soal & Rubrik Asesmen (Hal 5 s.d. 8, Portrait)

Salah satu keunggulan rancangan template RPS FSTI UWG adalah integrasi langsung instrumen soal dan rubrik ke dalam lampiran RPS (tidak dipisah dalam berkas terpisah). Lampiran ini memfasilitasi **4 Titik Evaluasi Baku**:

```
┌────────────────────────────────────────────────────────────────────────┐
│              4 TITIK EVALUASI ASESMEN OBE (TOTAL = 100%)               │
├───────────────┬────────────┬─────────────────────────────┬─────────────┤
│ Titik Asesmen │ Jadwal     │ Komponen Lampiran           │ Bobot Baku  │
├───────────────┼────────────┼─────────────────────────────┼─────────────┤
│ **Tugas 1**   │ Pekan 4-5  │ • Naskah Soal Penugasan 1   │ 20%         │
│ (Hal 5)       │            │ • Rubrik Penilaian Tugas 1  │             │
├───────────────┼────────────┼─────────────────────────────┼─────────────┤
│ **UTS**       │ Pekan 8    │ • Naskah Soal Ujian Tengah  │ 25% – 30%   │
│ (Hal 6)       │            │ • Rubrik Penilaian UTS      │             │
├───────────────┼────────────┼─────────────────────────────┼─────────────┤
│ **Tugas 2**   │ Pekan 12   │ • Naskah Soal Penugasan 2   │ 20% – 25%   │
│ (Hal 7)       │            │ • Rubrik Penilaian Tugas 2  │             │
├───────────────┼────────────┼─────────────────────────────┼─────────────┤
│ **UAS**       │ Pekan 16   │ • Naskah Soal Ujian Akhir   │ 30%         │
│ (Hal 8)       │            │ • Rubrik Penilaian UAS      │             │
└───────────────┴────────────┴─────────────────────────────┴─────────────┘
```

Masing-masing halaman lampiran memuat 2 blok kotak tabel:
1. **Kotak Atas:** Naskah Soal Penugasan / Soal Ujian (Instruksi kasus, batasan teknis, format pengumpulan).
2. **Kotak Bawah:** Matriks Rubrik Penilaian (Dimensi kriteria, indikator kinerja, gradasi level nilai: Sangat Kurang, Kurang, Cukup, Baik, Sangat Baik beserta skor bobot).

---

### Bagian V: Lembar Validasi & Pengesahan Tripartit (Hal 9, Portrait)

Menjamin kepatuhan standar PPEPP (Perencanaan, Pelaksanaan, Evaluasi, Pengendalian, Peningkatan) dan SPMI Universitas:

1. **Memvalidasi (Kiri Atas):**
   * Pihak: **Unit Penjaminan Mutu (UPM)** Fakultas Sains dan Teknologi Informasi
   * Format: `Nama Pejabat UPM` & `NUPTK. xxxxxxxxxx`
2. **Pengampu Mata Kuliah (Kanan Atas):**
   * Tanggal: `Malang, [Tanggal Bulan Tahun]`
   * Pihak: `Dosen Pengampu,`
   * Format: `{{namadosen}}` & `NUPTK. {{nuptk}}`
3. **Mengesahkan (Tengah Bawah):**
   * Pihak: **Ketua Program Studi {{prodi}}**
   * Format: `Nama Pejabat Program Studi` & `NUPTK. xxxxxxxxxxxxxxxx`

---

## 4. Kamus Lengkap Tag & Variabel Generator Template

Berikut adalah tabel kamus data (*data dictionary*) seluruh variabel yang dipakai pada template `Template_RPS_GEN_2026_20092026-SWO.docx` dan `Template_RPS_GEN_2026_20092026-SWI.pdf`:

### A. Tag Entitas Nilai Tunggal (`{{...}}`)

| No | Placeholder Tag | Nama Atribut | Tipe Data | Contoh Nilai Isi Kurikulum 2026 |
|:---:|---|---|---|---|
| 1 | `{{namamk}}` | Nama Mata Kuliah | String | Pemrograman Berorientasi Objek |
| 2 | `{{kodemk}}` | Kode Mata Kuliah | String | `STI-205` |
| 3 | `{{rumpunmk}}` | Rumpun Keilmuan MK | String | Core Sistem dan Teknologi Informasi |
| 4 | `{{skst}}` | Bobot SKS Teori | Integer | `2` |
| 5 | `{{sksp}}` | Bobot SKS Praktikum | Integer | `1` |
| 6 | `{{sms}}` | Semester Pelaksanaan | Integer/String | `2` atau `Genap` |
| 7 | `{{tglsusun}}` | Tanggal Penetapan RPS | String | `20 Agustus 2026` |
| 8 | `{{pengembangrps}}` | Dosen Pengembang RPS | String | `Tim KBK Rekayasa Perangkat Lunak` |
| 9 | `{{koordinatormk}}` | Koordinator RMK | String | `Dr. Roni Wahyu, S.Kom., M.T.` |
| 10 | `{{ketuaprodi}}` | Ketua Program Studi | String | `Ketua Prodi SISTEKIN FSTI` |
| 11 | `{{kodeprodi}}` | Kode Dokumen Prodi | String | `B4.5.2.RPS-STI205` |
| 12 | `{{prodi}}` | Nama Resmi Prodi | String | `Sistem dan Teknologi Informasi` |
| 13 | `{{namadosen}}` | Nama Dosen Utama | String | `Dr. Roni Wahyu, S.Kom., M.T.` |
| 14 | `{{nuptk}}` | NUPTK / NIDN Dosen | String | `0712345678` |
| 15 | `{{deskripsimk}}` | Deskripsi Singkat MK | Long Text | Narasi ringkas ruang lingkup keilmuan MK |
| 16 | `{{bahankajian}}` | Daftar Bahan Kajian | Long Text | Daftar nomor & nama BoK APTIKOM |
| 17 | `{{dosenpengampu}}` | Daftar Tim Dosen | String | Daftar seluruh pengampu kelas paralel |
| 18 | `{{mkprasyarat}}` | MK Prasyarat | String | `STI-101 Dasar Pemrograman` |

### B. Tag Entitas Looping / Blok Multi-Baris (`[...]`)

| No | Placeholder Tag | Lokasi Tampil | Fungsi & Struktur Pengulangan |
|:---:|---|---|---|
| 1 | `[nocpl]` & `[cpl]` | Hal 2: CP Prodi | Menampilkan pasangan baris Kode CPL (misal: `S1`, `KU1`, `P1`, `KK1`) dan Rumusan Teks CPL. |
| 2 | `[nocpmk]` & `[cpmk]` | Hal 2: CPMK | Menampilkan pasangan baris Kode CPMK (misal: `CPMK-1`) dan Rumusan Kalimat Berbasis ABCD. |
| 3 | `[nosubcpmk]` & `[subcpmk]` | Hal 2: Sub-CPMK | Menampilkan baris rincian Sub-CPMK mingguan. |
| 4 | `[tabelkolerasi]` | Hal 2: Matriks CPL-CPMK | Menampilkan tabel matriks korelasi CPL terhadap CPMK beserta persentase bobot (%) asesmen. |
| 5 | `[pustakautama]` | Hal 3: Pustaka | Daftar nomor urut buku acuan utama. |
| 6 | `[pustakapendukung]` | Hal 3: Pustaka | Daftar nomor urut artikel jurnal, prosiding, & dokumentasi resmi. |
| 7 | `[mingguke]` | Hal 3-4: Kolom 1 | Nomor minggu pertemuan (1 s.d. 16). |
| 8 | `[kemampuan_subcpmk]` | Hal 3-4: Kolom 2 | Rumusan Sub-CPMK minggu terkait. |
| 9 | `[indikator]` | Hal 3-4: Kolom 3 | Indikator penilaian mingguan. |
| 10 | `[kriteriateknik]` | Hal 3-4: Kolom 4 | Kriteria dan teknik penilaian mingguan. |
| 11 | `[luring]` | Hal 3-4: Kolom 5 | Moda pembelajaran luring + rincian estimasi waktu TM, PT, BM. |
| 12 | `[daring]` | Hal 3-4: Kolom 6 | Moda pembelajaran daring (LMS / Edlink). |
| 13 | `[materi]` | Hal 3-4: Kolom 7 | Pokok materi kajian dan nomor bab pustaka acuan. |
| 14 | `[bobot_nilai]` | Hal 3-4: Kolom 8 | Nilai persentase bobot asesmen minggu terkait. |
| 15 | `[penugasan1]` | Hal 5: Lampiran 1 | Teks naskah soal Penugasan Terstruktur 1 (Pekan 4). |
| 16 | `[rubriktugas1]` | Hal 5: Lampiran 1 | Tabel matriks rubrik analitik penilaian Tugas 1. |
| 17 | `[soaluts]` | Hal 6: Lampiran 2 | Teks naskah soal Ujian Tengah Semester (Pekan 8). |
| 18 | `[rubrikuts]` | Hal 6: Lampiran 2 | Tabel matriks rubrik analitik penilaian UTS. |
| 19 | `[tugas2]` | Hal 7: Lampiran 3 | Teks naskah soal Penugasan Terstruktur 2 (Pekan 12). |
| 20 | `[rubriktugas2]` | Hal 7: Lampiran 3 | Tabel matriks rubrik analitik penilaian Tugas 2. |
| 21 | `[soaluas]` | Hal 8: Lampiran 4 | Teks naskah soal Ujian Akhir Semester (Pekan 16). |
| 22 | `[rubrikuas]` | Hal 8: Lampiran 4 | Tabel matriks rubrik analitik/holistik penilaian UAS. |

---

## 5. Keselarasan Konstruktif (*Constructive Alignment*) dengan Kurikulum SISTEKIN 2026

Berdasarkan hasil komparasi terhadap seluruh dokumen ekosistem Kurikulum 2026 yang telah tuntas disusun, struktur template RPS ini menunjukkan **keterikatan dan keselarasan 100% sempurna**:

```
KURIKULUM 2026 (SOURCE OF TRUTH)              TEMPLATE RPS FSTI UWG
───────────────────────────────────────       ──────────────────────────────────────
Dokumen 003 (14 CPL & Genealogi BoK)    ───►  Hal 2: CPL-PRODI yang dibebankan ke MK
Dokumen 005 (Struktur 8 Sem / 67 MK)    ───►  Hal 2: Identitas MK, SKS (T/P), & Prasyarat
Dokumen 007 (Silabus 3-Tabel 67 MK)     ───►  Hal 2-4: Deskripsi, CPMK ABCD, Sub-CPMK,
                                              serta Tabel 16 Minggu (8 Kolom Baku)
Dokumen 008 & 018 (Sistem Asesmen OBE   ───►  Hal 5-8: Soal & Rubrik Analitik 4 Titik:
& 4 Master Rubrik Analitik Dosen)             • Tugas 1 (20%)   • UTS (25-30%)
                                              • Tugas 2 (20-25%)• UAS (30%)
Dokumen 043 (Boundary Guardrails & BoK) ───►  Hal 3-4: Materi Pembelajaran [Pustaka]
```

1. **Konvergensi 4 Titik Evaluasi Asesmen:**
   * Template RPS UWG menuntut tepat 4 lampiran asesmen: Tugas 1, UTS, Tugas 2, dan UAS.
   * Format ini identik 1-to-1 dengan konsensus arsitektur asesmen di **Dokumen 008** dan **Dokumen 007**, di mana setiap MK dievaluasi secara baku pada Pekan 4 (Tugas 1 = 20%), Pekan 8 (UTS = 25-30%), Pekan 12 (Tugas 2 = 20-25%), dan Pekan 16 (UAS = 30%), memenuhi standar IKU 7 (bobot evaluasi berbasis partisipasi/proyek/kasus $\ge 50\%$).
2. **Kesiapan Data Konten Mikro 67 MK:**
   * Kita **TIDAK PERLU merumuskan ulang dari nol** konten untuk mengisi template ini, karena **seluruh 67 mata kuliah** (28 MK Core STI, 13 MK FSTI, 8 MKWU, dan 18 MK Peminatan STA/STB/STC) telah memiliki:
     * 4 Rumusan CPMK berformat baku ABCD lengkap dengan level Taksonomi Bloom (C2 s.d. C6).
     * Rincian Sub-CPMK Minggu 1 s.d. 16.
     * Alokasi SKS Luring (TM, PT, BM) dan Daring.
     * Pemetaan Bahan Kajian BoK APTIKOM IS2020 & IT2017.
     * Daftar Buku Teks Pustaka Utama berstandar internasional.
     * Matriks Boundary Guardrails (*In-Scope, Out-of-Scope, Handoff Anchor*) di Dokumen 037 & 043.

---

## 6. Rekomendasi Alur Kerja Automasi (*RPS Generator Pipeline*)

Untuk memproduksi berkas RPS `.docx` dan `.pdf` bagi seluruh 67 mata kuliah secara instan dan bebas human error, direkomendasikan implementasi sistem automasi berbasis Python dengan skema berikut:

```
┌─────────────────────────────────┐
│     DATA SOURCE KURIKULER      │
│  • Dokumen 005 (Metadata MK)    │
│  • Dokumen 007 (Silabus 3-Tabel)│
│  • Dokumen 043 (CPMK & BoK)     │
│  • Dokumen 018 (Rubrik Master)  │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│      ENGINE GENERATOR PYTHON    │
│  (Menggunakan library `docx`    │
│   menggantikan placeholder      │
│   {{tag}} dan tabel [tag])      │
└────────────────┬────────────────┘
                 │
                 ├──────────────────────────────┐
                 ▼                              ▼
┌─────────────────────────────────┐ ┌─────────────────────────────────┐
│     OUTPUT WORD (.DOCX)         │ │      OUTPUT CETAK (.PDF)        │
│  Siap diedit / disesuaikan      │ │  Konversi instan via LibreOffice│
│  oleh dosen pengampu            │ │  atau Word Interop (Siap Cetak) │
└─────────────────────────────────┘ └─────────────────────────────────┘
```

### Langkah Implementasi Teknis:
1. **Parser Ekstraktor:** Skrip Python membaca file Markdown sumber (`005`, `007`, `043`, `018`) dan mengekstrak struktur kamus JSON untuk tiap mata kuliah.
2. **Template Processor:** Membuka `Template_RPS_GEN_2026_20092026-SWO.docx`, melakukan penggantian teks inline untuk variabel `{{...}}`, dan menyisipkan baris tabel dinamis untuk blok `[...]`.
3. **Penyuntik Rubrik:** Menyisipkan naskah soal studi kasus/proyek dan rubrik analitik dari Dokumen 018 ke halaman lampiran (Hal 5 s.d. 8).
4. **Batch Exporter:** Menghasilkan 67 berkas `.docx` rapi yang terorganisir per semester di folder target.

---

## 7. Kesimpulan

Dokumen template RPS OBE FSTI Universitas Widyagama Malang memiliki struktur yang **sangat sistematis, baku, dan ketat secara pedagogis**. Desain *hybrid orientation* (Landscape untuk matriks pembelajaran mingguan dan Portrait untuk instrumen asesmen serta legalitas) memastikan keterbacaan yang optimal bagi mahasiswa, dosen, auditor SPMI, maupun asesor LAM INFOKOM.

Portofolio kurikulum SISTEKIN 2026 kita telah **100% siap secara konten struktural maupun mikro**, sehingga proses konversi menuju dokumen operasional RPS untuk ke-67 mata kuliah dapat dieksekusi secara mulus menggunakan mekanisme automasi generator.
