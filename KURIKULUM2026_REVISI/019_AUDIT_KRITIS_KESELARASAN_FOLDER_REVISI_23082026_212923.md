# 019 — AUDIT KRITIS KESELARASAN FOLDER `KURIKULUM2026_REVISI/`
## Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang

**Jenis Dokumen:** Laporan Audit Forensik Keselarasan Lintas-Dokumen (Cross-Document Alignment Audit)
**Tanggal Audit:** 23 Agustus 2026, 21:29:23 WIB
**Cakupan:** 26 file Markdown dalam folder `KURIKULUM2026_REVISI/`
**Standar Rujukan Pemeriksaan:** Permendikbudristek No. 53 Tahun 2023, Panduan Kurikulum OBE APTIKOM SI v2.0 (IS2020), Panduan Kurikulum OBE TI 2023 (CC2020/IT2017), Standar LAM INFOKOM & IABEE
**Status Dokumen:** Laporan Temuan — **belum ada perbaikan yang diterapkan**

---

## RINGKASAN EKSEKUTIF

Folder `KURIKULUM2026_REVISI/` **belum selaras**. Audit ini menemukan 3 temuan prioritas nol (P0), 5 temuan prioritas satu (P1), dan 9 temuan prioritas dua (P2).

**Temuan tentang alat verifikasi:** Skrip `_tools/verify_zero_discrepancy.py` melaporkan `[SUCCESS] 100% PERFECT ALIGNMENT`, namun pembacaan kode pada `_tools/verify_zero_discrepancy.py:22-35` menunjukkan skrip tersebut **hanya memeriksa dua pola string**, yaitu (a) apakah `STI-103` masih bernama "Logika Informatika" dan (b) apakah `STI-204` menyebut kata "Logika". Skrip ini **tidak memverifikasi** jumlah SKS, jumlah MK, komposisi rumpun, jumlah CPL, rantai prasyarat, maupun struktur bab. Klaim "zero discrepancy" dan "100% tuntas dan terverifikasi" pada `AGENTS.md` karena itu **tidak memiliki dasar verifikasi yang memadai**.

**Temuan tentang dokumen sumber:** Dokumen `005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md` **terverifikasi bersih**. Hasil hitung ulang 55 baris mata kuliah menghasilkan tepat 146 SKS, dengan subtotal dan kumulatif per semester yang seluruhnya benar secara aritmetika. Persoalan justru berada pada dokumen turunan (`004`, `007`, dan `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md`) yang **mengalami regresi** dari dokumen 005 yang sudah benar.

### Tabel Rekapitulasi Status Audit

| No | Aspek yang Diaudit | Status | Prioritas |
|:---:|---|:---:|:---:|
| 1 | Tabrakan kode MK aktif `FST-204` & `FST-205` | ❌ Bermasalah | **P0** |
| 2 | Kelengkapan Bab I–VIII Buku Kurikulum Final | ❌ Bab I, III, V tidak ada | **P0** |
| 3 | Akurasi angka komposisi rumpun & sebaran SKS di Buku Final | ❌ 3 kelompok angka salah | **P0** |
| 4 | Pemetaan 1-to-1 empat asesmen ke empat CPMK | ❌ Gagal pada 31 dari 65 MK | **P1** |
| 5 | Sinkronisasi rantai prasyarat 007 vs 005 | ❌ Menyimpang pada 19 MK | **P1** |
| 6 | Reproduktibilitas rekapitulasi SKS pembina CPL (004 §5) | ❌ 12 dari 14 baris tak cocok | **P1** |
| 7 | Keseragaman rumusan tekstual 14 CPL antar file | ❌ 4 CPL berbeda substantif | **P1** |
| 8 | Ketunggalan matriks CPL↔PL dan PEO↔CPL | ❌ 3 versi & 2 versi | **P1** |
| 9 | Kepatuhan pola I→R→M per CPL | ❌ KK4 tanpa I dan R | **P1** |
| 10 | Konsistensi SKS `STI-625` Smart City | ❌ 3 SKS vs 2 SKS | **P2** |
| 11 | Kelengkapan silabus 67 MK portofolio | ❌ Hanya 65 MK | **P2** |
| 12 | Validitas sintaks tabel Markdown untuk ekspor | ❌ 4 separator rusak | **P2** |
| 13 | Akurasi sel rekapitulasi dokumen 011 | ❌ 34 sel salah | **P2** |
| 14 | Konsistensi angka proporsi praktikum | ❌ 3 versi berbeda | **P2** |
| 15 | Keseragaman jumlah kolom tabel matriks 004 | ❌ 1 baris 22 kolom | **P2** |
| 16 | Akurasi rekapitulasi IKU 7 di Buku Final | ❌ 2 angka salah | **P2** |
| 17 | Kemutakhiran indeks dokumen `009_LANGKAH2` | ❌ Berhenti di Dok. 011 | **P2** |
| 18 | Kebersihan artefak sementara di folder | ❌ 1 file sisa | **P2** |
| 19 | Ketiadaan kode MK usang (`STI-104`, `STI-205`, dll.) | ✅ Bersih | — |
| 20 | Jumlah 14 CPL, 3 PEO, 4 PL | ✅ Bersih | — |
| 21 | Jumlah BoK (19 IS2020 / 14 IT2017) | ✅ Bersih | — |
| 22 | Konsistensi Target Bloom 14 CPL | ✅ Bersih | — |
| 23 | Bobot skema 4x asesmen (total 100%) | ✅ Bersih 65/65 MK | — |
| 24 | Kelengkapan matriks 16 pertemuan | ✅ Bersih 65/65 MK | — |
| 25 | Ketiadaan CPL orphan dan MK orphan | ✅ Bersih | — |
| 26 | Aritmetika dokumen 005 (146 SKS / 55 MK) | ✅ Bersih | — |

---

## 0. METODOLOGI DAN BASIS BUKTI AUDIT

Audit dilakukan dengan kombinasi tiga teknik agar temuan dapat direproduksi oleh pihak lain:

| Teknik | Penerapan | Cakupan |
|---|---|---|
| **Rekalkulasi aritmetika** | Parsing baris tabel Markdown lalu menjumlahkan ulang kolom SKS, bukan membaca label subtotal | 005, 004, 011, Buku Final |
| **Diff lintas-dokumen** | Membandingkan nilai atribut yang sama (nama MK, SKS, semester, prasyarat, rumusan CPL) antar file | 001–018 + Buku Final |
| **Validasi sintaksis** | Memeriksa jumlah kolom header vs separator vs baris data pada tabel yang diekspor ke Excel/HTML/DOCX | 004, 011 |

**Prinsip pembuktian:** setiap temuan disertai nomor baris file agar dapat diperiksa langsung. Angka "seharusnya" selalu berasal dari hasil hitung ulang terhadap baris data, bukan dari label rekapitulasi — karena justru label rekapitulasi yang banyak ditemukan salah.

**Batas audit (dinyatakan eksplisit):** audit ini memeriksa **konsistensi numerik, kelengkapan struktural, dan keterlacakan referensi silang**. Audit ini **tidak menilai** ketepatan pedagogis rumusan CPMK, kelayakan level Bloom yang dipilih, maupun kesesuaian substansi materi 16 pertemuan terhadap standar industri.

---

# BAGIAN I — TEMUAN PRIORITAS NOL (P0)

Temuan P0 adalah temuan yang **memblokir kelayakan naskah** untuk diajukan ke LAM INFOKOM, karena merusak keterlacakan OBE secara struktural atau menampilkan angka yang saling bertentangan dalam satu dokumen resmi.

---

## P0-1. TABRAKAN KODE MATA KULIAH AKTIF: `FST-204` DAN `FST-205`

### Deskripsi Temuan

Dua kode mata kuliah aktif digunakan untuk **dua mata kuliah yang berbeda secara substansi** pada dokumen yang berbeda. Ini bukan kasus kode usang (yang dicari lewat pola `STI-104`, `STI-205`, dsb.), melainkan **tabrakan identitas pada kode yang masih aktif** — kelas kesalahan yang lebih berbahaya justru karena lolos dari pencarian kode usang.

### Tabel Bukti Tabrakan Identitas

| Kode | Identitas menurut `005` + Buku Final (dokumen struktur) | Identitas menurut `004` + `007` (dokumen matriks & silabus) |
|:---:|---|---|
| **`FST-204`** | **Pengantar Kecerdasan Artifisial & Data** (2 SKS, Teori, Sem 2) | **Organisasi dan Arsitektur Komputer** (*Computer Org & Arch*) |
| **`FST-205`** | **Basic English for IT** (2 SKS, Teori, Sem 2) | **Pemrograman Lanjut** (*Advanced Object-Oriented Programming*) |

### Lokasi Bukti per File

| File | Baris | Kutipan Verbatim |
|---|:---:|---|
| `005_STRUKTUR...md` | 102 | `\| 12 \| `FST-204` \| Pengantar Kecerdasan Artifisial & Data \| 2 \| Teori \| FSTI \| `FST-101` \|` |
| `005_STRUKTUR...md` | 103 | `\| 13 \| `FST-205` \| Basic English for IT \| 2 \| Teori \| FSTI \| — \|` |
| `007_FORMULASI...md` | 531 | `### 12. FST-204 — Organisasi dan Arsitektur Komputer (Computer Org & Arch)` |
| `007_FORMULASI...md` | 573 | `### 13. FST-205 — Pemrograman Lanjut (Advanced Object-Oriented Programming)` |
| `004_MATRIKS...md` | 72 | `\| 12 \| `FST-204` \| Organisasi & Arsitektur Kom \| 2 \| ... \| PL-2 \| PEO-1 \| **I** \|` |
| `004_MATRIKS...md` | 73 | `\| 13 \| `FST-205` \| Pemrograman Lanjut (OOP) \| 2 \| ... \| PL-1, PL-3 \| PEO-1 \| **I** \|` |
| `BUKU...FINAL.md` | 244–245 | Tabel struktur Sem 2 memakai nama versi `005` |
| `BUKU...FINAL.md` | 854–855, 946–947, 1153–1154 | Tabel ekuivalensi, matriks I-R-M, dan tabel IKU 7 memakai nama versi `004`/`007` |

### Inkonsistensi Internal di Dalam Dokumen 007

Dokumen `007` **bertentangan dengan dirinya sendiri**. Satu kode dipakai dengan dua makna berbeda dalam satu file:

| Baris 007 | Konteks | `FST-204` dimaknai sebagai |
|:---:|---|---|
| 531 | Judul blok silabus MK ke-12 | Organisasi dan Arsitektur Komputer |
| 794 | Prasyarat `STI-307` Sistem Cerdas | **Pengantar AI & Data** |
| 922 | Prasyarat `STI-310` Sistem Operasi | **Organisasi & Arsitektur Komputer** |

Pola yang sama terjadi pada Buku Final: baris 2011 (prasyarat `STI-307`) memakai "Pengantar Kecerdasan Artifisial & Data", sementara baris 2139 (prasyarat `STI-310`) memakai "Organisasi & Arsitektur Komputer".

### Analisis Konsekuensi

Konsekuensi tabrakan ini berlapis dan seluruhnya berdampak akreditasi:

1. **Dua mata kuliah kehilangan silabus.** `Basic English for IT` dan `Pengantar Kecerdasan Artifisial & Data` ada di struktur 8 semester tetapi **tidak memiliki silabus 3-tabel** di dokumen 007 maupun di Lampiran 2 Buku Final.
2. **Dua mata kuliah kehilangan slot semester.** Sebaliknya, `Organisasi dan Arsitektur Komputer` dan `Pemrograman Lanjut (OOP)` memiliki silabus lengkap 16 pertemuan tetapi **tidak ada dalam struktur 8 semester**. Semester 2 pada dokumen 005 sudah terisi penuh 8 MK / 20 SKS (batas maksimal Pasal 18 Permendikbudristek No. 53/2023), sehingga kedua MK ini secara faktual tidak dapat ditempatkan tanpa menggeser MK lain.
3. **Potensi pelanggaran Zero Redundancy.** Mata kuliah `Organisasi dan Arsitektur Komputer` beririsan substansial dengan konsensus final **`STI-103 Arsitektur dan Organisasi Sistem Teknologi Informasi`** (3 SKS, Sem 1). Ini persis jenis redundansi yang seharusnya sudah ditutup oleh Dokumen 017 (Audit Forensik Zero Redundancy) — artinya audit 017 melewatkannya.
4. **Pemetaan CPL menjadi ambigu.** Dokumen 004 memetakan `FST-204 → P3` dan `FST-205 → P4` (benar untuk Organisasi Komputer dan OOP), sedangkan dokumen 011 memetakan `FST-204 → KK1` dan `FST-205 → KU2` (benar untuk Pengantar AI dan Basic English). **Kedua pemetaan benar untuk mata kuliahnya masing-masing** — masalahnya adalah dua mata kuliah berbeda menyandang kode yang sama.
5. **Rantai prasyarat menjadi tidak dapat divalidasi.** `STI-310 Sistem Operasi` mensyaratkan "FST-204 Organisasi & Arsitektur Komputer", yaitu mata kuliah yang menurut tabel struktur resmi tidak ada.

### Status Penyelesaian

Temuan ini **memerlukan keputusan Tim Pengembang Kurikulum**, bukan koreksi teknis oleh agent. Dua pertanyaan yang harus dijawab:

1. Mata kuliah mana yang benar mengisi Semester 2: pasangan (Pengantar KA & Data + Basic English for IT) atau pasangan (Organisasi & Arsitektur Komputer + Pemrograman Lanjut OOP)?
2. Bila keempatnya diperlukan, kode mana untuk masing-masing, dan MK mana yang digeser keluar dari Semester 2 agar batas 20 SKS tetap terpenuhi?

Sebelum keputusan ini diamb, **koreksi pada dokumen 004, 005, 007, dan Buku Final tidak dapat dilakukan secara konsisten**, karena keempat dokumen harus dikoreksi ke arah yang sama.

---

## P0-2. BUKU KURIKULUM FINAL KEHILANGAN BAB I, BAB III, DAN BAB V

### Deskripsi Temuan

`AGENTS.md` menyatakan bahwa "Naskah utuh komprehensif Bab 1 s.d. Bab 8 (`BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md`, 445 KB) telah selesai dan 100% selaras". Pemeriksaan heading level-1 pada file tersebut (4.044 baris) menunjukkan klaim ini **tidak sesuai isi file**.

### Tabel Bukti Heading Bab yang Ada

| Baris | Heading Bab yang Ditemukan | Status |
|:---:|---|:---:|
| — | *(Bab I — tidak ada)* | ❌ **Hilang** |
| 21 | `# BAB II: VISI, MISI, TUJUAN, DAN POSITIONING STRATEGIS` | ✅ Ada |
| — | *(Bab III — tidak ada)* | ❌ **Hilang** |
| 161 | `# BAB IV: CAPAIAN PEMBELAJARAN LULUSAN (CPL) DAN BODY OF KNOWLEDGE (BoK)` | ✅ Ada |
| — | *(Bab V — tidak ada)* | ❌ **Hilang** |
| 408 | `# BAB VI: PROGRAM MBKM, CAPSTONE PROJECT, DAN TUGAS AKHIR NON-SKRIPSI` | ✅ Ada |
| 492 | `# BAB VII: SISTEM ASESMEN OBE, FORMULA CPL, DAN PENJAMINAN MUTU PPEPP` | ✅ Ada |
| 813 | `# BAB VIII: TATA KELOLA, SUMBER DAYA LABORATORIUM, DAN ATURAN PERALIHAN` | ✅ Ada |

Pola penomoran yang melompat (II → IV → VI) mengindikasikan bab-bab tersebut **direncanakan ada** namun hilang pada proses penggabungan naskah, bukan sengaja tidak dibuat.

### Materi Bab yang Hilang Tersisip di Bab Lain

Konten sebagian besar tersedia, tetapi **berada di bab yang salah**:

| Bab yang Hilang | Materi Semestinya | Lokasi Aktual Materi Tersebut |
|:---:|---|---|
| **Bab I** | Pendahuluan, Landasan Hukum, Latar Belakang | Tidak ditemukan di manapun |
| **Bab III** | 3 PEO & 4 Profil Lulusan | Tersisip di dalam **Bab II** (baris 52 dst.) dan terduplikasi di **Bab VII** (baris 635) |
| **Bab V** | Struktur Kurikulum 8 Semester & Peminatan | Tersisip di dalam **Bab IV** (baris 205–365) |

### Bab II Tidak Memuat Rumusan VMTS — Padahal Itu Judulnya

Bab II berjudul "VISI, MISI, TUJUAN, DAN POSITIONING STRATEGIS", namun penomoran bagiannya melompat: tidak ada `## 1.`, langsung ke `## 2. FORMULASI DEFINITIF 4 PROFIL LULUSAN` (baris 52).

Verifikasi tegas melalui pencarian frasa kanonik:

| Frasa yang Dicari | Sumber Frasa | Hasil di Buku Final |
|---|---|:---:|
| "unggul dalam pengembangan sistem dan teknologi informasi cerdas" | Visi 2045 (`001:56`) | **0 hasil** |
| "bermartabat" | Visi 2045 | **0 hasil** |
| "Kekuatan (Strengths)" | Analisis SWOT (`001` §3) | **0 hasil** |

**Kesimpulan:** Bab tentang Visi–Misi–Tujuan **tidak memuat pernyataan Visi 2045 maupun analisis SWOT**. Yang tersisa dari dokumen 001 hanyalah tabel rekonsiliasi profil lulusan (baris 33–50). Padahal pernyataan Visi 2045 adalah **ground truth paling fundamental** dalam `AGENTS.md`, dan Kriteria 1 LAM INFOKOM secara eksplisit menuntut VMTS terdokumentasi.

### Bab IV Tidak Memuat Rumusan 14 CPL — Padahal Itu Judulnya

Bab IV berjudul "CAPAIAN PEMBELAJARAN LULUSAN (CPL) DAN BODY OF KNOWLEDGE (BoK)", namun:

| Elemen yang Semestinya Ada | Sumber | Hasil Pencarian di Buku Final |
|---|---|:---:|
| Rumusan tekstual 14 CPL | `003`, `009A`–`009D` | **0 hasil** untuk frasa kanonik "Menguasai konsep dasar sains, matematika terapan" |
| Rumusan CPL Sikap S1 | `009A:12` | **0 hasil** untuk "Bertakwa kepada Tuhan" |
| Rumusan CPL KK1 | `009D` | **0 hasil** untuk "Mampu menganalisis, merancang, dan mengembangkan sistem informasi cerdas" |
| Genealogi sumber IS2020 | `003` | **0 hasil** untuk "CPL-P01" |
| Matriks silang CPL | `003` | **0 hasil** untuk "MATRIKS SILANG CPL" |
| Indikator Kinerja CPL (*Performance Indicator*) | `009A`–`009D` | Hanya 2 kemunculan "Indikator Kinerja", keduanya dalam konteks "Indikator Kinerja Utama (IKU)" |

Yang tersedia di Bab IV hanyalah **kode CPL dan deskripsi ringkas satu baris** pada tabel rekapitulasi (baris 1057–1070). Sebaliknya, Bab IV justru memuat seluruh struktur 8 semester (baris 205–365) yang seharusnya menjadi Bab V.

Ini temuan berdampak akreditasi tertinggi pada Buku Final: **buku kurikulum yang tidak memuat rumusan CPL secara tekstual tidak dapat dinilai oleh asesor**, karena CPL adalah objek utama penilaian OBE.

### Pola Sistematis: Bagian `## 1.` Hilang pada Enam Dokumen Sisipan

Kehilangan bagian pertama terjadi berulang, mengindikasikan cacat pada proses generasi/penggabungan otomatis:

| Dokumen Sisipan | Bagian `## 1.` di File Sumber | Status di Buku Final |
|---|---|:---:|
| `001` (menjadi Bab II) | § 1. VISI, MISI, TUJUAN (VMTS) | ❌ Hilang |
| `003` (menjadi Bab IV) | § 1. LANDASAN DAN PRINSIP PERUMUSAN CPL | ❌ Hilang |
| `005` (tersisip di Bab IV) | § 1. REKAPITULASI DAN DISTRIBUSI BEBAN STUDI | ⚠️ Judul hilang, tabel terbawa |
| `009` (menjadi Bab VI) | § 1. Capstone Project | ❌ Hilang, mulai dari § 2 |
| `008` (menjadi Bab VII) | § 1. | ❌ Hilang, mulai dari § 2 |
| `010` (tersisip di Bab VII) | § 1. | ❌ Hilang, mulai dari § 2 |
| `004` (menjadi Lampiran 1) | § 1. MATRIKS KESELARASAN | ✅ Ada |
| `007` (menjadi Lampiran 2) | § 1. PANDUAN 3 TABEL | ✅ Ada |

### Dokumen 010 Tersisip Tanpa Pembatas Bab dan Menabrak Bab VII

Pada baris 610–632, Bab VII (isi dokumen `008`) berakhir dengan `## 5. INTEGRASI CAPAIAN CPL KE DALAM SKPI`. Kemudian **tanpa pembatas bab apa pun**, penomoran bagian me-*reset* ke `## 2. FORMULASI 3 PEO & KEPEMIMPINAN` pada baris 633 — yang merupakan awal dokumen `010`.

Akibatnya Bab VII memuat **dua rangkaian `## 2.`–`## 5.`** dengan topik yang berbeda. Pembaca akan melihat urutan janggal: "§5 Integrasi SKPI" langsung diikuti "§2 Formulasi PEO". Secara logis, materi PEO/Tracer Study ini adalah milik Bab III yang hilang.

### Heading Duplikat

| Heading | Jumlah Kemunculan | Baris |
|---|:---:|---|
| `3 PROGRAM EDUCATIONAL OBJECTIVES (PEO) SISTEKIN` | **2x** | 91 dan 635 |
| `Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains...` | **6x** | 24, 164, 373, 411, 495, 876 |

Tabel PEO lengkap dimuat dua kali dengan format berbeda (di Bab II dan di sisipan dokumen 010). Enam sub-judul boilerplate identik akan menghasilkan enam entri duplikat bila daftar isi digenerasi otomatis.

### Konten Visual yang Hilang

Pencarian penanda placeholder (`TBD`, `TODO`, `XXX`, `[isi]`, `PLACEHOLDER`, `TBA`, `LOREM`) menghasilkan **0 hasil** — tidak ada placeholder eksplisit. ✅

Namun ditemukan **5 heading visualisasi yang sama sekali kosong** (diikuti langsung heading lain tanpa konten):

| Baris | Heading Kosong |
|:---:|---|
| 31 | `### PETA PIKIRAN (MINDMAP) VMTS 2045 & POSITIONING PRODI` |
| 172 | `### VISUALISASI SILSILAH GENEALOGI 14 CPL & BOK APTIKOM` |
| 380 | `### VISUALISASI 3 PEMINATAN & JALUR MBKM 20 SKS` |
| 418 | `### VISUALISASI ALUR CAPSTONE & 4 OPSI TA NON-SKRIPSI` |
| 503 | `### VISUALISASI ALUR HINGGA ASESMEN OBE & SIKLUS PPEPP` |

Sebagai pembanding, dua heading visualisasi lain (baris 883 dan 1229) **berisi diagram Mermaid utuh** — membuktikan bahwa kelima diagram di atas benar-benar hilang, bukan sengaja dikosongkan.

Ditemukan pula dua lubang konten:
- **Baris 180–185:** enam baris kosong berurutan tepat sebelum `### REKAPITULASI KOMPOSISI KURIKULUM 2026`. Pada dokumen `005` lokasi ini berisi diagram Mermaid struktur & alur prasyarat.
- **Baris 611–615:** lima baris kosong di dalam `## 5. INTEGRASI CPL KE SKPI`. Konten yang hilang adalah **ASCII-art Radar Chart CPL**, yang masih utuh di `008_...md` baris 123 dst. Akibatnya Bab VII menjanjikan "Portofolio Capaian OBE (Radar Chart CPL)" lalu tidak menampilkannya.

### Tidak Ada Daftar Isi

Pencarian "Daftar Isi" / "DAFTAR ISI" menghasilkan **0 hasil**. Untuk naskah buku kurikulum yang akan diserahkan ke LAM INFOKOM, absennya daftar isi — bersama halaman pengesahan, kata pengantar, serta daftar tabel dan gambar — merupakan kekurangan formal.

Konsekuensi tambahan: bila daftar isi digenerasi dari heading yang ada sekarang, hasilnya menampilkan urutan bab yang janggal (II → IV → VI → VII → VIII) beserta enam baris boilerplate identik dan dua entri "3 PROGRAM EDUCATIONAL OBJECTIVES".

---

## P0-3. ANGKA KOMPOSISI DAN SEBARAN SKS DI BUKU FINAL SALAH (REGRESI DARI DOKUMEN 005)

### Deskripsi Temuan

Buku Kurikulum Final memuat tiga kelompok angka yang bertentangan dengan hasil hitung ulang tabel di dalam buku itu sendiri, **dan** bertentangan dengan dokumen sumber `005` yang sudah benar. Ini adalah **regresi**: dokumen turunan lebih buruk daripada sumbernya.

### P0-3a. Komposisi Rumpun Mata Kuliah Salah di Dua Tabel

| Lokasi | Tertulis di Buku Final | Seharusnya (hasil hitung ulang) | Selisih |
|---|---|---|:---:|
| `BUKU:191` | Mata Kuliah Wajib Fakultas (FSTI) — **14 MK / 38 SKS / 25,9%** | **13 MK / 36 SKS / 24,7%** | −1 MK, −2 SKS |
| `BUKU:192` | Mata Kuliah Inti Program Studi (Core STI) — **27 MK / 77 SKS / 53,1%** | **28 MK / 79 SKS / 54,1%** | +1 MK, +2 SKS |
| `BUKU:1270` | Mata Kuliah Dasar Fakultas (FSTI) — **14 MK / 38 SKS** | **13 MK / 36 SKS** | −1 MK, −2 SKS |
| `BUKU:1271` | Mata Kuliah Inti Program Studi (STI) — **27 MK / 77 SKS** | **28 MK / 79 SKS** | +1 MK, +2 SKS |

**Verifikasi hitung ulang.** Parsing kolom Kategori pada 55 baris MK di tabel struktur 8 semester dokumen `005` menghasilkan:

| Kategori | Jumlah MK | Total SKS |
|---|:---:|:---:|
| MKWU | 8 MK | 13 SKS |
| FSTI | **13 MK** | **36 SKS** |
| Core STI | **28 MK** | **79 SKS** |
| Peminatan (Elektif) | 6 MK | 18 SKS |
| **TOTAL** | **55 MK** | **146 SKS** |

Hasil ini **identik** dengan `005:46-50`, membuktikan dokumen 005 benar dan Buku Final yang salah.

**Mengapa kesalahan ini lolos selama ini.** Kesalahan bersifat "berimbang" — satu MK dan 2 SKS dipindahkan dari Core STI ke FSTI:

```
Klaim Buku Final : 14 MK + 27 MK = 41 MK ; 38 SKS + 77 SKS = 115 SKS
Nilai sebenarnya : 13 MK + 28 MK = 41 MK ; 36 SKS + 79 SKS = 115 SKS
```

Karena subtotal gabungan dan total keseluruhan (55 MK / 146 SKS) tetap benar, kesalahan ini **tidak terdeteksi oleh pemeriksaan total** — dan tidak terdeteksi oleh `verify_zero_discrepancy.py` yang bahkan tidak memeriksa SKS sama sekali.

### P0-3b. Sebaran SKS Semester 6 dan Kumulatif Semester 6–7 Salah

**Rekalkulasi lengkap 8 semester** (dihitung dari baris MK di dalam Buku Final, bukan dari label subtotalnya):

| Semester | Jml MK Dihitung | SKS Dihitung | Kumulatif Dihitung | Klaim di Buku Final | Verdict |
|:---:|:---:|:---:|:---:|---|:---:|
| Sem 1 | 8 | 19 | 19 | 8 MK / 19 SKS / 19 SKS | ✅ |
| Sem 2 | 8 | 20 | 39 | 8 MK / 20 SKS / 39 SKS | ✅ |
| Sem 3 | 7 | 20 | 59 | 7 MK / 20 SKS / 59 SKS | ✅ |
| Sem 4 | 8 (+1 MK 0 SKS) | 21 | 80 | 8 MK+1 / 21 SKS / 80 SKS | ✅ |
| Sem 5 | 7 (+1 MK 0 SKS) | 21 | 101 | 7 MK+1 / 21 SKS / 101 SKS | ✅ |
| **Sem 6** | 7 | **19** | **120** | 7 MK / **20 SKS** / **121 SKS** | ❌ |
| **Sem 7** | 7 | 20 | **140** | 7 MK / 20 SKS / **141 SKS** | ❌ |
| Sem 8 | 1 | 6 | **146** | 1 MK / 6 SKS / 146 SKS | ⚠️ |
| **TOTAL** | **55** | **146** | **146** | 55 MK / 146 SKS | ✅ |

**Rincian baris Semester 6 di Buku Final** (baris 293–299): `3 + 2 + 3 + 3 + 2 + 3 + 3 = 19 SKS`, bukan 20.

**Anomali aritmetika yang paling jelas terlihat asesor:** Buku Final menyatakan kumulatif Semester 7 = 141 SKS (`BUKU:312`) dan SKS Semester 8 = 6, namun kemudian menyatakan kumulatif Semester 8 = 146 SKS (`BUKU:318`). Padahal `141 + 6 = 147`. **Tabel tersebut tidak konsisten dengan dirinya sendiri.**

### Tabel Baris yang Perlu Dikoreksi

| Baris | Tertulis | Seharusnya |
|:---:|---|---|
| `BUKU:216` | `\| Sem 6 \| AI Integrasi & Plat. \| 7 MK \| 20 SKS \|` | `19 SKS` |
| `BUKU:290` | `### SEMESTER 6 (20 SKS)` | `### SEMESTER 6 (19 SKS)` |
| `BUKU:300` | `**Total SKS Semester 6 (7 MK)** \| **20** \| ... \| **Kumulatif: 121 SKS**` | `**19**` ... `**Kumulatif: 120 SKS**` |
| `BUKU:312` | `**Total SKS Semester 7 (7 MK)** \| **20** \| ... \| **Kumulatif: 141 SKS**` | SKS 20 benar; `**Kumulatif: 140 SKS**` |
| `BUKU:331` | `\| Sem 6 \| 7 MK \| 20 SKS \| 121 SKS \| 13,6% \|` | `19 SKS \| 120 SKS \| 13,0%` |
| `BUKU:332` | `\| Sem 7 \| 7 MK \| 20 SKS \| 141 SKS \| 13,6% \|` | `20 SKS \| 140 SKS \| 13,7%` |

**Pembanding sumber.** `005:72` (`\| Sem 6 \| ... \| 7 MK \| 19 SKS \|`), `005:156` (`### SEMESTER 6 (19 SKS)`), `005:166` (`Kumulatif: 120 SKS`), dan `005:180` (`Kumulatif: 140 SKS`) **seluruhnya sudah benar**. Ini mengonfirmasi bahwa temuan ini adalah regresi murni pada proses pembuatan Buku Final.

### P0-3c. Akar Penyebab: `STI-625` Smart City Tercatat 3 SKS

Sumber kesalahan Semester 6 dapat ditelusuri ke inkonsistensi SKS `STI-625`:

| File | Baris | Tertulis | Seharusnya |
|---|:---:|---|---|
| `007_FORMULASI...md` | 1689 | `\| **Bobot SKS / Tipe** \| **3 SKS** / Tipe: **+P** (100m Teori + 170m Lab + 180m Mandiri) \|` | **2 SKS / Teori** |
| `BUKU...FINAL.md` | 2906 | `\| **Bobot SKS / Tipe** \| **3 SKS** / Tipe: **+P** ... \|` | **2 SKS / Teori** |
| `BUKU...FINAL.md` | 294 | `\| 40 \| STI-625 \| Smart City & Pemerintahan Digital \| 2 \| **+P** \|` | SKS 2 benar; tipe **Teori** |
| `006_DISTRIBUSI...md` | 19 | `• STI-625 Smart City (3)` | `(2)` |
| `005_STRUKTUR...md` | 160 | `\| 40 \| `STI-625` \| Smart City & Pemerintahan Digital \| 2 \| Teori \|` | ✅ **Benar** |

Ground truth `AGENTS.md` menegaskan: *"Sem 6 (19 SKS, Smart City & Pem. Digital 2 SKS)"*. Dokumen `005` mematuhinya; `006`, `007`, dan Buku Final tidak.

**Dampak kuantitatif pada dokumen 007:** total SKS 65 blok silabus di `007` = **183 SKS**, sedangkan portofolio seharusnya **182 SKS**. Kelebihan +1 SKS bersumber tunggal dari `STI-625`. Semester 6 di `007` terhitung 32 SKS untuk 11 MK, seharusnya 31 SKS.

---

# BAGIAN II — TEMUAN PRIORITAS SATU (P1)

Temuan P1 adalah temuan yang **merusak keterlacakan OBE** (*constructive alignment*) dan hampir pasti dipersoalkan asesor, tetapi tidak menghalangi naskah untuk dibaca.

---

## P1-1. SKEMA "4 ASESMEN MEMETAKAN 1-TO-1 KE 4 CPMK" GAGAL PADA 31 DARI 65 MATA KULIAH

### Deskripsi Temuan

`AGENTS.md` menetapkan konsensus final: *"Memetakan secara langsung 1-to-1 ke 4 CPMK dan memenuhi IKU 7 ≥ 50%"*. Buku Final baris 523–527 juga memetakan empat titik asesmen ke CPMK-1 sampai CPMK-4 secara satu-satu.

Namun hanya **34 dari 65 MK** yang benar-benar memiliki 4 CPMK. Pada **31 MK (47,7%)**, pemetaan 1-to-1 secara aritmetis **mustahil terpenuhi**.

### Tabel Distribusi Jumlah CPMK per Mata Kuliah

| Jumlah CPMK | Jumlah MK | Persentase | Status Pemetaan 1-to-1 |
|:---:|:---:|:---:|:---:|
| 4 CPMK | 34 MK | 52,3% | ✅ Terpenuhi |
| 3 CPMK | 28 MK | 43,1% | ❌ Mustahil |
| 2 CPMK | 3 MK | 4,6% | ❌ Mustahil |
| **Total** | **65 MK** | **100%** | **31 MK gagal** |

### Daftar Mata Kuliah dengan 2 CPMK (3 MK)

| Kode | Nama Mata Kuliah | Baris di 007 | Baris di Buku Final |
|:---:|---|:---:|:---:|
| `MKU-101` | Agama I | 278 | 1495 |
| `MKU-102` | Pancasila | 319 | 1536 |
| `MKU-405` | Kewarganegaraan | 1342 | 2559 |

### Daftar Mata Kuliah dengan 3 CPMK (28 MK)

| No | Kode | Baris di 007 | No | Kode | Baris di 007 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `FST-101` | 65 | 15 | `STA-01` | 2066 |
| 2 | `STI-101` | 150 | 16 | `STA-04` | 2194 |
| 3 | `MKU-103` | 360 | 17 | `STB-01` | 2322 |
| 4 | `FST-204` | 531 | 18 | `STB-02` | 2364 |
| 5 | `FST-206` | 616 | 19 | `STB-03` | 2406 |
| 6 | `MKU-204` | 701 | 20 | `STB-04` | 2448 |
| 7 | `STI-307` | 786 | 21 | `STB-05` | 2490 |
| 8 | `STI-310` | 914 | 22 | `STB-06` | 2532 |
| 9 | `STI-418` | 1214 | 23 | `STC-01` | 2574 |
| 10 | `MKU-507` | 1598 | 24 | `STC-02` | 2616 |
| 11 | `STI-626` | 1726 | 25 | `STC-03` | 2658 |
| 12 | `FST-611` | 1811 | 26 | `STC-04` | 2700 |
| 13 | `FST-612` | 1939 | 27 | `STC-05` | 2742 |
| 14 | `FST-613` | 1981 | 28 | `STC-06` | 2784 |

### Pola Temuan yang Perlu Diperhatikan

**Seluruh 6 MK peminatan P2 (`STB-01` s.d. `STB-06`) dan seluruh 6 MK peminatan P3 (`STC-01` s.d. `STC-06`) hanya memiliki 3 CPMK**, sementara peminatan P1 (`STA`) memiliki 4 CPMK pada 4 dari 6 MK-nya.

Ini menciptakan **ketidaksetaraan kedalaman asesmen antar peminatan**, padahal `AGENTS.md` menegaskan ketiga peminatan harus "seimbang" (masing-masing 6 MK / 18 SKS). Kesetaraan SKS terpenuhi, tetapi kesetaraan granularitas CPMK tidak.

### Catatan Penting: Bobot Asesmennya Sendiri Bersih Sempurna

Perlu ditegaskan bahwa masalahnya **bukan** pada bobot asesmen:

| Aspek Asesmen | Hasil Audit |
|---|:---:|
| MK dengan tepat 4 titik asesmen berbobot | **65/65** ✅ |
| MK dengan total bobot tepat 100% | **65/65** ✅ |
| Pola MK Teori `20/30/20/30` | 28 MK ✅ |
| Pola MK non-Teori `20/25/25/30` | 37 MK ✅ |

Pola sepenuhnya sesuai ground truth (Tugas 1 20%, UTS 25–30%, Tugas 2 20–25%, UAS 30%) tanpa satu pun pengecualian. Tipe non-Teori yang memakai pola praktikum adalah `+P` (32 MK), `Praktik` (`MKU-507`), `Proyek` (`FST-610`), `Magang` (`FST-612`), `Seminar` (`FST-613`), dan `Mandiri` (`FST-714`).

Jadi persoalannya murni di **sisi jumlah CPMK**, bukan di sisi bobot.

### Temuan Turunan: Keterlacakan Asesmen→CPMK Bersifat Implisit

Pemeriksaan tambahan menunjukkan:

| Elemen | Jumlah Baris Diperiksa | Baris yang Mencantumkan Kode CPMK |
|---|:---:|:---:|
| Baris asesmen berbobot | 264 | **0** |
| Baris matriks 16 pertemuan | 1.040 | **0** |

Kolom asesmen **tidak pernah menyebut kode CPMK secara eksplisit**, demikian pula baris Sub-CPMK pada matriks pertemuan. Keterkaitan asesmen ke CPMK hanya dapat disimpulkan dari urutan pekan (Pekan 4 → CPMK-1, Pekan 8 → CPMK-2, dst.), tidak tertulis. Bagi asesor LAM INFOKOM yang menuntut bukti *constructive alignment*, keterlacakan implisit ini sulit dipertahankan.

### Opsi Penyelesaian

Dua jalur yang tersedia, keduanya memerlukan keputusan Tim Pengembang Kurikulum:

| Opsi | Tindakan | Volume Kerja | Konsekuensi |
|:---:|---|:---:|---|
| **A** | Tambahkan CPMK ke-4 pada 31 MK, dan CPMK ke-3 + ke-4 pada 3 MK MKWU | 31 MK | Pemetaan 1-to-1 utuh; konsisten dengan `AGENTS.md` |
| **B** | Longgarkan narasi menjadi "Tugas 2 dan UAS dapat memetakan ke CPMK yang sama" | 3 dokumen (007, 008, Buku) | Lebih cepat; tetapi melemahkan klaim 1-to-1 dan perlu revisi `AGENTS.md` |

**Rekomendasi:** Opsi A untuk 12 MK peminatan STB/STC (agar setara dengan STA), dan Opsi B untuk 3 MK MKWU (karena MKWU 2 SKS wajar hanya punya 2–3 CPMK).

---

## P1-2. RANTAI PRASYARAT DOKUMEN 007 MENYIMPANG DARI DOKUMEN 005 PADA 19 MATA KULIAH

### Deskripsi Temuan

Dokumen `005` adalah *single source of truth* untuk struktur dan prasyarat. Namun `007` (silabus) memuat prasyarat yang berbeda pada 19 dari 65 MK. Dokumen `012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md` yang seharusnya memvalidasi hal ini tampaknya tidak menangkap penyimpangan tersebut.

### P1-2a. Pelanggaran Urutan Semester — Prasyarat Tidak Mungkin Terpenuhi

Ini temuan paling serius pada kelompok prasyarat:

| Baris 007 | Mata Kuliah | Prasyarat di 007 | Masalah |
|:---:|---|---|---|
| **1050** | `STI-413` Machine Learning (**Sem 4**) | `FST-207`, **`FST-408`** | **`FST-408` Probabilitas & Statistika juga di Semester 4.** Prasyarat sesemester secara akademik tidak dapat dipenuhi — mahasiswa tidak mungkin sudah lulus MK yang baru ditempuh bersamaan. |

Prasyarat yang benar menurut `005:128` adalah `STI-205` Aljabar Linear (Sem 2) dan `STI-307` Sistem Cerdas (Sem 3) — keduanya mendahului Semester 4 dan secara substansi lebih tepat sebagai fondasi Machine Learning.

### P1-2b. Prasyarat Hilang atau Berkurang (9 MK) — Risiko Akademik

Mahasiswa dapat mengambil mata kuliah tanpa fondasi yang diperlukan:

| Baris 007 | Mata Kuliah | Prasyarat di 007 | Seharusnya (005) | Yang Hilang |
|:---:|---|---|---|---|
| 666 | `FST-207` Sistem Basis Data | **Tidak Ada** | `FST-102` | Algoritma & Pemrograman |
| 836 | `STI-308` UI/UX Design | **Tidak Ada** | `FST-101` | Dasar Teknologi Digital |
| 751 | `STI-306` APSI | `STI-101` | `STI-101`, `FST-207` | Sistem Basis Data |
| 1136 | `STI-416` Web Back End | `STI-311` | `FST-207`, `STI-311` | Sistem Basis Data |
| 1434 | `STI-520` Data Mining | `STI-415` | `STI-413`, `STI-415` | Machine Learning |
| 1563 | `STI-523` Manajemen Proyek TI | `STI-306` | `STI-306`, `STI-309` | Rekayasa Perangkat Lunak |
| 1648 | `STI-624` Integrasi Layanan Cerdas AI | `STI-519` | `STI-519`, `STI-416` | Web Back End |
| 1861 | `STI-728` Startup Digital | `MKU-204` | `STI-627`, `MKU-204` | Digital Platform Engineering |
| 1904 | `FST-610` Capstone Project FSTI | hanya ambang SKS | `STI-523`, ≥100 SKS | Manajemen Proyek TI |

Yang paling berisiko: `FST-207 Sistem Basis Data` tanpa prasyarat `FST-102 Algoritma dan Pemrograman`, dan `STI-416 Web Back End` tanpa prasyarat basis data — keduanya membuat mahasiswa dapat masuk MK teknis tanpa kemampuan pemrograman dasar.

### P1-2c. Prasyarat Berbeda Total (7 MK)

Bukan sekadar berkurang, tetapi merujuk mata kuliah yang sama sekali lain:

| Baris 007 | Mata Kuliah | Prasyarat di 007 | Seharusnya (005) |
|:---:|---|---|---|
| 879 | `STI-309` Rekayasa Perangkat Lunak | `FST-205` | **`FST-203`** Struktur Data |
| 922 | `STI-310` Sistem Operasi | `FST-204` | **`STI-103`** Arsitektur & Organisasi Sistem TI |
| 1007 | `STI-312` Jaringan Komputer | `FST-101` | **`STI-103`** Arsitektur & Organisasi Sistem TI |
| 1050 | `STI-413` Machine Learning | `FST-207`, `FST-408` | **`STI-205`, `STI-307`** |
| 1520 | `STI-522` Pemrograman Mobile | `FST-203`, `STI-311` | **`STI-311`, `STI-416`** |
| 1691 | `STI-625` Smart City | `STI-101` | **`STI-521`** Internet of Things |
| 581 | `FST-205` | `FST-102` | Tanpa prasyarat (konsekuensi P0-1) |

Penyimpangan pada `STI-310` dan `STI-312` sangat perlu diperhatikan: keduanya seharusnya berfondasi pada `STI-103`, yang merupakan **konsensus final** dalam `AGENTS.md` (*"Jaringan komputer memerlukan pemahaman datapath, bus biner, dan arsitektur hardware Sem 1"*). Penyimpangan ini justru meruntuhkan rasionalisasi keberadaan `STI-103`.

Perlu dicatat pula bahwa `STI-625 Smart City` mengalami **dua kesalahan sekaligus** — SKS salah (P0-3c) dan prasyarat salah.

### P1-2d. Ambang SKS Tidak Sinkron (6 MK) — Semua Lebih Ketat dari 005

| Mata Kuliah | Baris 007 | Ambang di 007 | Ambang di 005 | Selisih |
|---|:---:|:---:|:---:|:---:|
| `MKU-507` KPM | 1606 | ≥ 90 SKS | ≥ 80 SKS | +10 SKS |
| `FST-611` Metodologi Penelitian | 1819 | ≥ 100 SKS | ≥ 76 SKS | **+24 SKS** |
| `FST-610` Capstone Project | 1904 | ≥ 110 SKS | ≥ 100 SKS + `STI-523` | +10 SKS |
| `FST-612` PKL | 1947 | ≥ 100 SKS | ≥ 100 SKS | ✅ Sesuai |
| `FST-613` Pra-Skripsi | 1989 | hanya lulus `FST-611` | `FST-611` + ≥ 100 SKS | Ambang hilang |
| `FST-714` Skripsi | 2031 | hanya lulus `FST-613` | `FST-613` + ≥ 120 SKS | Ambang hilang |

**Analisis `FST-611`:** ambang ≥100 SKS di `007` masih *dapat* dipenuhi karena kumulatif akhir Semester 5 adalah 101 SKS. Namun margin-nya hanya 1 SKS — artinya **mahasiswa yang mengulang satu mata kuliah 2 SKS di semester manapun akan terhalang mengambil Metodologi Penelitian di Semester 6**, yang kemudian menunda Pra-Skripsi dan Skripsi secara berantai. Ambang ≥76 SKS pada `005` jauh lebih aman dan itulah yang menjadi konsensus.

**Analisis `FST-613` dan `FST-714`:** hilangnya ambang SKS justru melonggarkan syarat, memungkinkan mahasiswa mendaftar Skripsi hanya dengan lulus Pra-Skripsi tanpa memenuhi 120 SKS. Ini bertentangan dengan praktik penjaminan mutu.

### Dampak Terhadap Dokumen 015 (Simulasi Akselerasi 7 Semester)

Dokumen `015_SIMULASI_AKSELERASI_KELULUSAN_7_SEMESTER.md` menyusun simulasi kelulusan 3,5 tahun berdasarkan rantai prasyarat. Karena rantai prasyarat di `007` berbeda dari `005` pada 19 MK, **simulasi akselerasi tersebut perlu divalidasi ulang** setelah rantai prasyarat disatukan. Audit ini tidak memeriksa dokumen 015 secara mendalam.

---

## P1-3. REKAPITULASI SKS PEMBINA CPL DI DOKUMEN 004 §5 TIDAK DAPAT DIREPRODUKSI

### Deskripsi Temuan

Dokumen `004` §5 (baris 183–198) menyajikan tabel "Jumlah MK Pembina" dan "Total SKS Pembina Langsung" untuk masing-masing 14 CPL. **12 dari 14 baris tidak dapat direkonstruksi** dari matriks §3.1–3.4 pada dokumen yang sama.

### Tabel Perbandingan Klaim §5 vs Hitung Ulang Matriks §3

| CPL | Klaim §5 (MK) | Klaim §5 (SKS) | Hitung Ulang §3 (MK) | Hitung Ulang §3 (SKS) | Selisih SKS |
|:---:|---|:---:|:---:|:---:|:---:|
| S1 | 7 MK + Capstone + TA | **21** | 9 MK | **23** | +2 |
| KU1 | 10 MK + Capstone + TA | **29** | 10 MK | **30** | +1 |
| KU2 | 6 MK + Capstone + TA | 18 | 6 MK | 18 | ✅ **0** |
| KU3 | 4 MK + Capstone + TA | **14** | 5 MK | **17** | +3 |
| P1 | 7 MK | **20** | 6 MK | **21** | +1 |
| P2 | 12 MK | **34** | 11 MK | **32** | −2 |
| P3 | 10 MK | **28** | 10 MK | **30** | +2 |
| P4 | 11 MK | 32 | 10 MK | 32 | ✅ **0** |
| KK1 | 5 MK Inti + 6 MK P1 | **33** | 8 MK | **25** | **−8** |
| KK2 | 4 MK + 2 MK P1 | **18** | 6 MK | **21** | +3 |
| KK3 | 7 MK + 3 MK P2 | **30** | 10 MK | **31** | +1 |
| KK4 | 3 MK + 5 MK P2 | **24** | 4 MK | **15** | **−9** |
| KK5 | 7 MK + 5 MK P3 | **36** | 9 MK | **30** | **−6** |
| KK6 | 4 MK + 2 MK P3 | **21** | 7 MK | **20** | −1 |

### Analisis Mengapa Angka Ini Tidak Dapat Dipertahankan

Sebagian selisih **dapat** dijelaskan karena §5 memasukkan MK elektif sementara §3 tidak merincinya per-CPL. Namun penjelasan tersebut **tidak konsisten dengan arah selisihnya**:

- Jika §5 memasukkan elektif, maka angka §5 seharusnya **selalu lebih besar** dari §3.
- Kenyataannya: KK1 (33 vs 25, lebih besar) tetapi KK4 (24 vs 15, lebih besar) berdampingan dengan S1 (21 vs 23, lebih kecil) dan KU3 (14 vs 17, lebih kecil).
- Arah selisih yang tidak konsisten membuktikan **tidak ada satu pun formula perhitungan yang dapat menghasilkan seluruh 14 angka tersebut**.

Konsekuensinya, `004` §8 baris 335 mengklaim *"Seluruh 14 CPL terlayani secara adil dan proporsional dengan alokasi SKS yang solid"* — sebuah klaim yang **tidak didukung oleh tabel di atasnya**. Asesor yang melakukan verifikasi silang akan menemukan bahwa dasar klaim tersebut tidak dapat direproduksi.

### Temuan Terkait: Deskripsi Ringkas KU3 di `004:188` Salah Domain

| Sumber | Rumusan / Deskripsi KU3 |
|---|---|
| **`004:188`** (SALAH) | "**Tanggung jawab etis, kepatuhan regulasi siber & hukum digital**" — 4 MK Wajib + Capstone + TA / 14 SKS |
| `003:63` = `009B:16` = `009E:17` = `011:58` (BENAR, keempatnya sepakat) | "Mampu **mengambil keputusan** yang tepat berdasarkan **analisis data dan informasi**, bertanggung jawab atas pencapaian hasil kerja kelompok, melakukan **evaluasi diri**, serta mengelola **pembelajaran mandiri sepanjang hayat**." |

Deskripsi pada `004:188` menggambarkan konten **CPL S1 (Sikap) atau P3 (Pengetahuan Infrastruktur & Etika)**, sama sekali bukan KU3. Karena `004` adalah dokumen matriks keterlacakan utama yang dibaca asesor lebih dulu, kesalahan substantif di sini berdampak langsung pada kredibilitas seluruh matriks.

### Temuan Terkait: Cakupan CPL Bersih, Namun `KK4` Rawan

Sisi positifnya, **tidak ada CPL orphan**. Hasil parsing 55 baris MK pada Tabel 3.1–3.4 (total terhitung **tepat 146 SKS** ✅):

| CPL | Jml MK Pembina | CPL Orphan? | Catatan |
|:---:|:---:|:---:|---|
| S1 | 9 | Tidak | — |
| KU1 | 10 | Tidak | — |
| KU2 | 6 | Tidak | — |
| KU3 | 5 | Tidak | — |
| P1 | 6 | Tidak | — |
| P2 | 11 | Tidak | — |
| P3 | 10 | Tidak | — |
| P4 | 10 | Tidak | — |
| KK1 | 8 | Tidak | — |
| KK2 | 6 | Tidak | — |
| KK3 | 10 | Tidak | — |
| **KK4** | **4** | Tidak | ⚠️ **Paling tipis** |
| KK5 | 9 | Tidak | — |
| KK6 | 7 | Tidak | — |

**Risiko pada KK4 (Tata Kelola & Audit TI):** hanya dibina 4 MK di jalur wajib — `STI-626`, `FST-610`, `FST-612`, `FST-714`. Penopang riilnya berada pada 5 MK elektif `STB` (`004:159-164`), tetapi **elektif tidak wajib bagi mahasiswa peminatan P1 atau P3**.

Artinya, mahasiswa jalur P1 (Integrated Smart Systems) atau P3 (Digital Platform Engineering) mencapai KK4 **hanya melalui Keamanan Informasi Lanjut ditambah Capstone/PKL/Skripsi**. Ini titik lemah yang hampir pasti ditanyakan asesor: *"Bagaimana Prodi menjamin CPL KK4 tercapai oleh seluruh lulusan, bukan hanya lulusan peminatan P2?"*

### Temuan Format Terkait

| Lokasi | Temuan | Dampak |
|---|---|---|
| `004:76` (`MKU-204` Kewirausahaan I) | Baris memiliki **22 kolom**, sedangkan header dan 54 baris lainnya **21 kolom** (ada satu pipe berlebih) | Menggeser seluruh sel satu kolom ke kanan saat dikonversi ke Excel/Word |
| `004` §3 baris 50–53 | Legenda hanya mendefinisikan `I`/`R`/`M`; **simbol `*` tidak didefinisikan** | 6 baris `STA/B/C` (baris 113, 120, 121, 133, 134, 135) memakai `*` yang bermakna "bergantung paket peminatan" — tanpa legenda, asesor akan membacanya sebagai sel kosong |

---

## P1-4. RUMUSAN TEKSTUAL CPL BERBEDA SUBSTANTIF ANTAR FILE

### Deskripsi Temuan

Rumusan CPL adalah **objek penilaian utama** asesor LAM INFOKOM. Rumusan yang berbeda antar dokumen resmi membuat asesor tidak dapat menentukan mana yang berlaku. Audit menemukan 4 kelompok penyimpangan substantif.

### P1-4a. `KK3` Kehilangan Komponen IoT — Temuan Paling Berdampak

| Sumber | Rumusan KK3 |
|---|---|
| `003` = `009D` (identik verbatim) | "…infrastruktur cloud (Cloud/DevOps), **sistem sensor cerdas (IoT)**, dan ketahanan siber" |
| **`011:65`** | "…cloud, keamanan siber, DevOps (CI/CD, containerization, IaC)" — **komponen IoT hilang** |

Yang membuat temuan ini serius: pada baris yang sama, `011` **tetap menuliskan** kolom Fokus sebagai *"Cloud, **IoT** & infrastruktur terintegrasi"*. Jadi dokumen tersebut menyebut IoT di kolom fokus tetapi menghilangkannya dari rumusan CPL.

Dampak berantai: IoT adalah **penciri PL-2 (Cloud Infra, Cyber & Smart Sys)** dan dipetakan ke `BK-IT14`. Karena `011` adalah dokumen yang diekspor ke Excel dan Word untuk lampiran akreditasi, versi tanpa IoT inilah yang berpotensi terbaca asesor.

### P1-4b. `P4` Bergeser Domain dari Rekayasa Perangkat Lunak ke Pengelolaan Data

| Sumber | Rumusan P4 |
|---|---|
| `003:71` = `009C:17` (identik verbatim) | "**Menguasai prinsip rekayasa perangkat lunak modern** (web, mobile, **distributed**), manajemen basis data relasional/NoSQL…" |
| **`011:62`** | "**Memahami konsep pengelolaan data**, basis data, analitik data…" |

Ini bukan peringkasan, melainkan **perubahan domain CPL**. Rekayasa perangkat lunak modern (web, mobile, distributed) hilang sepenuhnya, digantikan fokus pada data. Padahal `P4` adalah CPL yang menopang `PL-3 (UI/UX & Digital Platform Eng)` dan seluruh jalur Web/Mobile pada struktur kurikulum.

### P1-4c. Verba `P1`–`P4` di Dokumen 011 Turun Level Bloom

Dokumen `011` Sheet 3 secara sistematis menurunkan level verba dibanding `003`/`009C`:

| CPL | `003` & `009C` (identik) | `011` Sheet 3 | Perubahan |
|:---:|---|---|---|
| P1 | "**Menguasai** konsep dasar sains…" (`003:68` / `009C:14`) | "**Mempunyai pengetahuan** dasar sains…" (`011:59`) | C4 → C2 |
| P2 | "**Menguasai konsep teoretis** sistem informasi, analisis & perancangan sistem, **arsitektur enterprise**…" (`003:69`) | "**Memahami konsep dasar** sistem informasi…" (`011:60`) — **klausa arsitektur enterprise hilang** | C4 → C2 + kehilangan komponen |
| P3 | "**Menguasai** prinsip dan konsep infrastruktur TI…" (`003:70`) | "**Memahami** konsep infrastruktur TI… **etika digital**…" (`011:61`) — menambah "etika digital" yang tidak ada di `003` | C4 → C2 + penambahan |
| P4 | Lihat P1-4b | Lihat P1-4b | C4 → C2 + pergeseran domain |

**Mengapa ini dipersoalkan asesor:** kolom "Target Bloom" pada **semua** file (termasuk `011` itu sendiri) secara konsisten menyatakan `P1 = C3` dan `P2`–`P4` = `C4`. Verba "memahami" dan "mempunyai pengetahuan" berada pada level **C2 (Understand)**, sehingga **verba rumusan bertentangan dengan level Bloom yang diklaim** dalam dokumen yang sama.

### P1-4d. `KK1` dan `KK6` Kehilangan Komponen di Dokumen 011

| CPL | `003` = `009D` (identik verbatim) | `011` Sheet 3 |
|:---:|---|---|
| KK1 | "…(AI/ML, **NLP, Computer Vision, Smart Sys, DSS**)" | "…berbasis **AI/ML**" (`011:63`) — **4 teknologi penciri hilang** |
| KK6 | "**merancang, memvalidasi model bisnis (Lean Startup/MVP)**, mengelola proyek agile, serta **mendirikan usaha rintisan**" | "merancang dan mengelola **proyek startup**… (lean startup, MVP, **scaling**…)" (`011:68`) |

Kehilangan pada `KK1` melemahkan penciri **peminatan P1 (flagship)**: NLP, Computer Vision, Smart Systems, dan DSS adalah tepat empat domain yang membedakan SISTEKIN dari Prodi TI menurut *distinctive positioning* dalam `AGENTS.md`.

### P1-4e. `KU2` Memiliki Dua Cakupan Pemangku Kepentingan yang Berbeda

| Sumber | Rumusan KU2 (bagian akhir) |
|---|---|
| `003:62` | "…serta memelihara dan mengembangkan jaringan kerja **kolaboratif dengan pemangku kepentingan industri**." |
| `009B:15` | "…serta memelihara dan mengembangkan jaringan kerja **profesional lintas disiplin**." |
| `011:57` | "Mampu **mengkomunikasikan gagasan, analisis, dan solusi teknis**… jaringan kerja **profesional**" |

"Pemangku kepentingan industri" mempersempit cakupan ke DUDI, sedangkan "lintas disiplin" adalah kompetensi kolaborasi yang lebih luas. Selain itu `003`/`009B` menyebut objek komunikasi sebagai **"rancangan arsitektur"** sementara `011` menyebut **"analisis"**.

Karena `KU2` diturunkan dari SN-Dikti KU4 dan KU6, rumusan yang paling dapat dipertahankan secara regulasi adalah **versi `009B`**.

### P1-4f. `S1` — Dokumen 003 Menjadi Outlier

| Sumber | Rumusan S1 |
|---|---|
| **`003:56`** (outlier) | "…menginternalisasi nilai, norma, **etika digital dan hukum profesi**, menjunjung tinggi kejujuran dan **integritas**, **mampu** bekerja sama…" |
| `009A:12` = `011:55` (identik) | "…menginternalisasi nilai, norma, **dan etika digital**, menjunjung tinggi kejujuran dan **profesionalisme**, bekerja sama…" |

Versi `003` memuat elemen tambahan ("hukum profesi", "integritas") yang tidak ada pada dua file lain. **Dua dari tiga file sepakat**, sehingga `003` adalah outlier — meskipun `003` justru berstatus master dokumen CPL. Arah koreksi perlu ditetapkan eksplisit oleh Tim Pengembang.

### Aspek Rumusan CPL yang Terverifikasi Bersih

| Perbandingan | Hasil |
|---|:---:|
| `003` ↔ `009C` untuk `P1`–`P4` | ✅ **Identik verbatim** |
| `003` ↔ `009D` untuk `KK1`–`KK6` | ✅ **Identik verbatim** |
| Target Bloom 14 CPL di 6 file (`003`, `009A`–`009E`, `009_LANGKAH2`) | ✅ **Konsisten 100%** (S1=A3; KU1=C4; KU2/KU3=C5; P1=C3; P2–P4=C4; KK1–KK3/KK5/KK6=C6; KK4=C5) |
| `003` ↔ `009B` untuk `KU1` | ⚠️ Kosmetik saja ("permasalahan **komputasi**" vs "permasalahan **computing**") |
| `009E` sebagai ringkasan | ✅ Sah — sudah menandai diri sebagai "Ringkasan Rumusan", bukan rumusan normatif |

---

## P1-5. MATRIKS `CPL↔PL` MEMILIKI TIGA VERSI DAN `PEO↔CPL` MEMILIKI DUA VERSI

### P1-5a. Tiga Versi Matriks CPL ↔ Profil Lulusan

Yang paling problematis: **dokumen `011` bertentangan dengan dirinya sendiri** — Sheet 3 dan Sheet 4 memberikan pemetaan berbeda untuk CPL yang sama.

| CPL | `011` Sheet 3 (kolom "PL Terkait") | `011` Sheet 4 (matriks ✓) | `003` §6 = `009E` §4 |
|:---:|---|---|---|
| KU1 | PL-1, PL-2 | PL-1, PL-2, PL-3, PL-4 | Seluruh PL |
| KU2 | PL-3, PL-4 | Seluruh PL | Seluruh PL |
| KU3 | PL-3, PL-4 | Seluruh PL | Seluruh PL |
| P1 | PL-1, PL-2 | Seluruh PL | PL-1, PL-2 |
| P4 | PL-1, PL-3 | PL-1, PL-3, PL-4 | PL-1, PL-3, PL-4 |

Penyimpangan tambahan pada `011` Sheet 4 terhadap `003` §6:

| Penyimpangan | Detail | Baris Pembanding di 003/009E |
|---|---|---|
| `KK5` hilang dari PL-1 dan PL-4 | Sheet 4 tidak memetakannya | `003:163`, `003:165` / `009E:82`, `009E:84` |
| `KK6` hilang dari PL-3 | Sheet 4 tidak memetakannya | `003:166` / `009E:85` |
| `P1` ditambahkan ke PL-3 dan PL-4 | Tidak ada di `003` | — |
| **PL-4 kehilangan 4 CPL** | `P2`, `P3`, `KK1`, `KK5` | `003` §6 |

**Yang bersih:** `003` §6 dan `009E` §4 **identik 4/4 baris** ✅. Jadi kedua outlier adalah `011` Sheet 3 dan `011` Sheet 4, dan versi `003`/`009E` yang harus dipertahankan.

### P1-5b. Dua Versi Matriks PEO ↔ CPL

| PEO | Hanya ada di `003` §7 | Hanya ada di `004` §2 |
|:---:|---|---|
| PEO-1 | `KU2` | `KK6` |
| PEO-2 | `P3`, `KK1` | — |
| PEO-3 | `KU3`, `KK5`, `KK6` | — |

`003` memetakan PEO-3 ke **seluruh 14 CPL**, sedangkan `004` hanya ke **11 CPL**. Untuk instrumen IABEE Kriteria 2 dan LAM INFOKOM, matriks PEO↔CPL harus **tunggal dan tidak ambigu**.

### P1-5c. Pola I→R→M Tidak Terpenuhi untuk `KK4` (dan Empat CPL Lain Tanpa Tahap I)

Hitung ulang matriks I/R/M pada `011` Sheet 7 (46 baris MK) terhadap baris rekapitulasi `011:248-250`:

| CPL | Jumlah `I` Aktual | Jumlah `R` Aktual | Jumlah `M` Aktual | Kepatuhan Pola I→R→M |
|:---:|:---:|:---:|:---:|:---:|
| **KK4** | **0** | **0** | 4 | ❌ **Langsung ke M** |
| KU3 | **0** | 1 | 5 | ❌ Tanpa tahap I |
| KK2 | **0** | 2 | — | ❌ Tanpa tahap I |
| KK3 | **0** | 4 | 5 | ❌ Tanpa tahap I |
| KK5 | **0** | 4 | 5 | ❌ Tanpa tahap I |

Temuan `KK4` adalah yang paling sulit dipertahankan: **tidak ada satu pun mata kuliah yang mengintroduksi (`I`) maupun menguatkan (`R`) KK4** pada Sheet 7 — CPL tersebut langsung muncul pada tahap Mastery. Ini bertentangan langsung dengan legenda `011:198` dan dengan visualisasi pada `004:19-23` yang keduanya mengklaim penerapan pola bertahap I→R→M.

Temuan ini bertaut dengan risiko `KK4` pada P1-3 (hanya 4 MK pembina wajib, penopang riil di elektif `STB` yang tidak wajib). Secara bersama-sama, keduanya menunjukkan **`KK4` adalah CPL terlemah dalam kurikulum ini** dan merupakan titik yang paling rentan dipersoalkan asesor.

---

# BAGIAN III — TEMUAN PRIORITAS DUA (P2)

Temuan P2 adalah temuan kebersihan teknis: angka rekapitulasi yang salah, sintaks yang berisiko menggagalkan ekspor, dan kelengkapan artefak. Tidak menghalangi substansi, tetapi menurunkan kredibilitas dokumen bila ditemukan asesor.

---

## P2-1. SILABUS HANYA MEMUAT 65 MATA KULIAH, BUKAN 67

### Bukti

| File | Klaim Judul | Jumlah Blok Silabus Aktual |
|---|---|:---:|
| `007_FORMULASI...md` | "67 MATA KULIAH" (baris 1, rekap baris 58) | **65** (bernomor 1–65, tanpa gap/duplikat) |
| `BUKU...FINAL.md` Lampiran 2 | "67 MATA KULIAH" (baris 1216, 1218, 1279) | **65** (nomor 66 dan 67 tidak ada) |

### Mata Kuliah yang Tidak Memiliki Silabus

| Kode | Nama Mata Kuliah | SKS | Semester | Lokasi di Struktur |
|:---:|---|:---:|:---:|---|
| `MKU-406` | Agama II | 0 | 4 | `005:136`, `BUKU:274` |
| `MKU-508` | Kewirausahaan II | 0 | 5 | `005:151`, `BUKU:287` |

Keduanya adalah MK 0 SKS kebijakan UWG. Pencarian string kedua kode di `007` menghasilkan **0 kemunculan** — bukan sekadar silabusnya kosong, tetapi kodenya tidak disebut sama sekali.

### Verifikasi Definisi "67 MK"

Untuk memastikan angka 67 memang benar sebagai ground truth:

```
MK non-elektif berkode di struktur (termasuk MKU-406 & MKU-508) = 49 MK
MK elektif ditawarkan (STA-01..06, STB-01..06, STC-01..06)      = 18 MK
                                                          Total = 67 MK ✅

Silabus aktual: 47 MK non-elektif + 18 MK elektif               = 65 MK
Selisih                                                          =  2 MK
```

Angka 67 pada `AGENTS.md` **terkonfirmasi benar**; yang kurang adalah dua silabus.

### Opsi Penyelesaian

| Opsi | Tindakan |
|:---:|---|
| A | Tambahkan silabus `MKU-406` dan `MKU-508` (meski 0 SKS, keduanya tetap MK wajib lulus) |
| B | Ubah seluruh klaim menjadi "65 MK bersilabus + 2 MK 0 SKS tanpa silabus" dengan catatan kaki penjelas |

**Rekomendasi:** Opsi A. Mata kuliah 0 SKS yang menjadi syarat kelulusan tetap memerlukan CPMK dan rubrik asesmen agar dapat dinyatakan lulus/tidak lulus secara akuntabel.

### Catatan Terkait: Lampiran 1 Buku Final Memuat 53 Baris untuk Klaim 55 MK

| Lokasi | Klaim | Aktual | Penjelasan |
|---|---|:---:|---|
| `BUKU:873`, `:875`, `:922` | "55 MATA KULIAH" | 53 baris MK | `MKU-406` dan `MKU-508` (0 SKS) tidak dimasukkan |
| `BUKU:931-1011` (Tabel 3.1–3.4) | — | 53 baris, total **146 SKS** ✅ | Nomor urut 1–53 lengkap tanpa lompatan |
| `BUKU:1142-1198` (Tabel IKU 7) | — | 53 baris, total **146 SKS** ✅ | — |

Secara SKS keduanya benar (0 SKS tidak menambah total). Bukan kesalahan aritmetika, tetapi memerlukan catatan kaki agar asesor tidak menghitung selisih 2 MK.

---

## P2-2. EMPAT SEPARATOR TABEL MARKDOWN RUSAK DI DOKUMEN 011

### Bukti

Dokumen `011` diekspor ke Excel (`GENERATE_EXCEL_011.bat`), HTML (`GENERATE_HTML.bat`), dan DOCX (`GENERATE_DOCX.bat`). Empat tabel memiliki baris separator dengan **pipe ganda** yang melanggar spesifikasi tabel Markdown:

| Baris | Sheet | Kolom Header | Kolom Separator | Kolom Baris Data | Baris Anomali |
|:---:|---|:---:|:---:|:---:|:---:|
| **289** | Sheet 9 (`STI-624`) | 12 | **24** | **13** | 11 dari 12 |
| **311** | Sheet 10 (`STI-413`) | 13 | **26** | **14** | 11 dari 12 |
| **333** | Sheet 11 (`STI-308`) | 12 | **24** | **13** | 11 dari 12 |
| **355** | Sheet 12 (`STI-626`) | 12 | **24** | **13** | 11 dari 12 |

Kutipan verbatim `011:289`:

```
|---||---||---||---||---||---||---||---||---||---||---||---||
```

Seharusnya (12 kolom):

```
|---|---|---|---|---|---|---|---|---|---|---|---|
```

Selain itu, baris 300–301, 322–323, 344–345, dan 366–367 (baris "Ringkasan Kelas" dan "% Mahasiswa ≥ 75") juga memakai `||` sebagai penanda *merge cell* — bukan sintaks Markdown yang valid.

### Analisis Risiko

Konverter Python kustom pada `_tools/export_all_to_excel.py` tampaknya toleran terhadap pipe ganda (file `.xlsx` yang dihasilkan menampilkan 12/13 kolom dengan benar). Namun:

- **Renderer HTML standar dan Pandoc** dapat menolak tabel tersebut atau membuang kolom terakhir.
- Konversi DOCX melalui `_tools/convert_md_to_docx.py` berisiko sama.
- Bila naskah dibaca di editor Markdown pihak ketiga (GitHub, VS Code preview, Typora), tabel akan tampil rusak.

Perbaikan bersifat mekanis dan aman: ganti keempat baris separator dengan jumlah kolom yang tepat sama dengan header.

### Catatan: Tabel Kosong di Sheet 9–12 Bukan Cacat

Sheet 9–12 masing-masing memiliki 10 dari 13 baris kosong (hanya kolom No terisi: 1, 2, 3, 4, 5, 10, 15, 20, 25, 30). Ini **disengaja dan wajar** — `011:31` (Sheet 1) dan `011:420` (Sheet 14) secara eksplisit menyatakan sheet ini adalah **template yang menunggu data SIAKAD**. Tidak ada tabel yang kosong tanpa penjelasan. ✅

---

## P2-3. SEL REKAPITULASI DOKUMEN 011 SALAH PADA 34 SEL

### P2-3a. Sebelas dari Empat Belas Angka "Jumlah MK Pendukung" Salah

Angka yang sama direplikasi di **tiga tempat** dalam satu file (`011:174` sebagai total Sheet 5, Sheet 13 baris 378–391, dan Sheet 14 baris 400–413), lalu diekspor ke Excel:

| CPL | Tertulis | Hitung Ulang dari 67 Baris Sheet 5 | Selisih |
|:---:|:---:|:---:|:---:|
| S1 | 9 | 9 | ✅ |
| KU1 | 12 | **11** | −1 |
| KU2 | 11 | **9** | −2 |
| KU3 | 6 | **5** | −1 |
| P1 | 9 | **7** | −2 |
| P2 | 15 | **12** | −3 |
| P3 | 12 | **13** | +1 |
| P4 | 12 | **10** | −2 |
| KK1 | 11 | **13** | +2 |
| KK2 | 7 | **8** | +1 |
| KK3 | 12 | **14** | +2 |
| KK4 | 7 | **8** | +1 |
| KK5 | 14 | 14 | ✅ |
| KK6 | 8 | 8 | ✅ |

### P2-3b. Sembilan Belas Sel Rekap I/R/M Salah di `011:248-250`

| Baris Rekap | Jumlah Sel Salah | Detail Selisih (tertulis → aktual) |
|---|:---:|---|
| Jumlah `I` (baris 248) | **1** | P3: `0` → **1** (`STI-103` pada `011:209` memberi I pada P3) |
| Jumlah `R` (baris 249) | **9** | KU2 (2→1), P2 (7→6), **P3 (7→4)**, P4 (7→5), KK2 (3→2), KK3 (5→4), **KK4 (1→0)**, **KK5 (6→4)**, KK6 (2→1) |
| Jumlah `M` (baris 250) | **9** | S1 (3→4), KU1 (4→5), **KU2 (4→6)**, KU3 (4→5), P3 (3→4), **KK3 (3→5)**, KK4 (3→4), KK5 (4→5), KK6 (3→4) |

Yang paling penting di antara ini: **`KK4` "Jumlah R" tertulis 1 padahal aktual 0** — inilah yang mengungkap temuan P1-5c (KK4 tanpa tahap I dan R). Angka `1` yang salah itu selama ini **menutupi** cacat pola I→R→M.

### P2-3c. Keempat Angka "Jumlah CPL per PL" Salah di `011:91`

| Lokasi | Tertulis | Hitung Ulang dari 14 Baris di Atasnya |
|---|---|---|
| `011:91` | `\| Jumlah CPL per PL \| \| \| 10 \| 9 \| 9 \| 8 \|` | PL-1 = **9**, PL-2 = **8**, PL-3 = **8**, PL-4 = **7** |

Klaim turunan pada `011:23` menyatakan *"Seluruh PL ditopang min. 8 CPL"* — setelah dikoreksi menjadi **min. 7 CPL**. Klaim substantif "min. 3 CPL per PL terpenuhi" tetap valid, sehingga dampak substantifnya rendah; namun keempat angkanya salah dan direplikasi.

### P2-3d. Anomali Penanda dan Hitungan di `011:121`

| Temuan | Detail |
|---|---|
| Penanda salah | `FST-612` (PKL) memakai `M` pada kolom KK4 dan KK5, padahal legenda `011:97` menyatakan `V = CPL dibebankan dan diases pada MK tersebut`. **Semua 65 baris lain memakai `V`.** Ini sisa penyuntingan dari Sheet 7 (yang memang berlegenda I/R/M). |
| Hitungan salah | Baris yang sama menuliskan `Jml CPL = 7` padahal aktual **6**. Satu-satunya baris di Sheet 5 dengan Jml CPL salah. |

### P2-3e. Pemetaan CPL Berbeda antara `004` dan `011` Sheet 5 pada 14 Mata Kuliah

Dari 49 MK yang ada di kedua dokumen, 14 MK memiliki pemetaan CPL berbeda:

| Mata Kuliah | Pemetaan di `004` | Pemetaan di `011` Sheet 5 | Sifat Selisih |
|:---:|---|---|---|
| **`FST-204`** | `P3` | `KK1` | **Bertentangan total** (konsekuensi P0-1) |
| **`FST-205`** | `P4` | `KU2` | **Bertentangan total** (konsekuensi P0-1) |
| **`FST-612`** PKL | 10 CPL (S1, KU1–3, KK1–6) | 6 CPL (S1, KU1–3, KK4, KK5) | `011` kehilangan KK1, KK2, KK3, KK6 |
| `STI-416` | P4, **KK5** | P4, **KU1** | Tukar KK5 ↔ KU1 |
| `FST-206` | S1, **KU3** | S1, **KU2** | Tukar KU3 ↔ KU2 |
| `MKU-507` KPM | S1, **KU3** | S1, **KU2** | Tukar KU3 ↔ KU2 |
| `FST-101` | KU1, P2 | P2 | `011` kehilangan KU1 |
| `FST-203` | P4 | P4, KU1 | `011` menambah KU1 |
| `FST-408` | P1 | P1, P4 | `011` menambah P4 |
| `FST-611` | KU1, KU2 | KU1, KU2, KU3 | `011` menambah KU3 |
| `FST-613` | KU1, KU2 | KU1, KU2, KU3 | `011` menambah KU3 |
| `STI-306` | KU1, P2 | KU1, P2, KK5 | `011` menambah KK5 |
| `STI-309` | KK5, P4 | KK5, KK6, P4 | `011` menambah KK6 |
| `STI-413` | KK1, P2 | KK1, **KK2**, P2 | `011` menambah KK2 |

**Yang bersih:** Sheet 5 ↔ Sheet 7 dalam `011` **konsisten 100%** untuk 46 MK bersama ✅.

**Catatan cakupan Sheet 7:** Sheet 7 hanya memuat 46 MK, tidak mencakup `MKU-405`, `MKU-406`, `MKU-508`, dan seluruh 18 MK elektif `STA`/`STB`/`STC`. Karena itu rekapitulasi I/R/M pada Sheet 7 **tidak merepresentasikan portofolio 67 MK** — perlu catatan eksplisit pada dokumen agar tidak disalahbaca.

---

## P2-4. ANGKA PROPORSI PRAKTIKUM MEMILIKI TIGA VERSI DAN TIDAK SATU PUN AKURAT

| Sumber | Klaim | Status |
|---|---|:---:|
| `005:57` | "20 Mata Kuliah (**63 SKS** / 43,2%)" | ❌ SKS salah |
| `BUKU:201` | "**21 Mata Kuliah** (**66 SKS** / 44,9%)" | ❌ Keduanya salah |
| **Hitung ulang dari tabel `005`** | **20 MK / 59 SKS** (tipe `+P`, `Praktik`, `Proyek`, `Magang`) | ✅ Terverifikasi |

**Rincian hitung ulang.** Parsing kolom Tipe pada 55 baris MK dokumen `005`:

| Tipe | Jumlah MK | Total SKS |
|---|:---:|:---:|
| `+P` (Teori + Praktikum) | 17 MK | 50 SKS |
| `Praktik` (`MKU-507` KPM) | 1 MK | 3 SKS |
| `Proyek` (`FST-610` Capstone) | 1 MK | 3 SKS |
| `Magang` (`FST-612` PKL) | 1 MK | 3 SKS |
| **Total berpraktikum** | **20 MK** | **59 SKS** |
| Persentase terhadap 146 SKS | — | **40,4%** |

Angka MK (20) pada `005` benar; angka SKS-nya (63) yang salah. Buku Final salah pada keduanya. Perlu dicatat bahwa perhitungan ini **belum memasukkan 6 MK elektif** (yang mayoritas bertipe `+P`) karena tabel struktur menandainya sebagai `Elektif`, bukan `+P`. Bila 6 MK elektif dimasukkan, hasilnya menjadi 26 MK / 77 SKS / 52,7% — tetapi angka ini pun tidak cocok dengan klaim manapun.

**Rekomendasi:** tetapkan satu definisi eksplisit ("MK dengan komponen praktikum terjadwal, termasuk/tidak termasuk elektif dan MK lapangan") lalu hitung ulang dan sinkronkan ke `005`, Buku Final, dan `011`.

---

## P2-5. REKAPITULASI IKU 7 DI BUKU FINAL SALAH HITUNG

### Bukti

Kutipan `BUKU:1200-1201`:

```
> * **Persentase MK Memenuhi IKU 7 (CM + PjBL ≥ 50%):** **89.1%** (49 dari 55 MK paket).
> * **Rata-rata Bobot Pembelajaran Kolaboratif Kurikulum:** **67.8%**
```

### Hitung Ulang dari 53 Baris Tabel IKU 7

| Metrik | Tertulis | Hitung Ulang | Selisih |
|---|:---:|:---:|:---:|
| MK memenuhi CM+PjBL ≥ 50% | **49 MK** | **48 MK** | −1 |
| Persentase | **89,1%** | **87,3%** (48/55) | −1,8 pp |
| Rata-rata bobot kolaboratif | **67,8%** | **63,7%** | −4,1 pp |

### Lima Mata Kuliah di Bawah 50% (Wajar dan Sudah Diberi Keterangan)

| Kode | Mata Kuliah | Bobot CM+PjBL | Baris |
|:---:|---|:---:|:---:|
| `STI-102` | Kalkulus | 20% | 1145 |
| `STI-103` | Arsitektur & Organisasi Sistem TI | 20% | 1146 |
| `STI-204` | Matematika Diskrit dan Logika | 20% | 1150 |
| `STI-205` | Aljabar Linear dan Matriks | 20% | 1151 |
| `FST-408` | Probabilitas dan Statistika | 30% | 1170 |

Perhitungan: `53 − 5 = 48 MK`, bukan 49. Kelimanya adalah MK matematika/sains dasar, sehingga bobot rendah dapat dipertahankan secara pedagogis.

**Yang bersih:** seluruh komponen persentase per baris (CM + PjBL + DA) berjumlah tepat 100%, dan kolom total CM+PjBL dihitung benar pada setiap baris ✅. Kesalahan hanya pada baris rekapitulasi.

---

## P2-6. TEMUAN KEBERSIHAN LAINNYA

### P2-6a. Ketidakseragaman Kolom Tabel di `004:76`

| Lokasi | Temuan | Dampak |
|---|---|---|
| `004:76` (`MKU-204` Kewirausahaan I) | **22 kolom**, sedangkan header dan 54 baris lain **21 kolom** | Menggeser seluruh sel satu kolom ke kanan saat diekspor ke Excel/Word |

### P2-6b. Empat Sel Pemetaan BoK Berbeda antara `003` dan `009D`/`009E`

| Kode BoK | Nama BoK | `003` | `009D`/`009E` | Selisih |
|:---:|---|---|---|---|
| `BK-IS04` | *Enterprise Architecture* | P2, KK5 (`003:117`) | P2, **KK4**, KK5 (`009E:38`) | +KK4 |
| `BK-IS09` | *Business Process Management* | P2, KK4 (`003:122`) | P2, KK4, **KK5** (`009E:43`) | +KK5 |
| `BK-IS11` | *Programming Fundamentals & OOP* | P1, P4, KK1 (`003:124`) | P1, P4, KK1, **KK5** (`009E:45`) | +KK5 |
| `BK-IT09` | *Data Analytics & Info Visualization* | P4, KK2 (`003:150`) | **KK1**, KK2 (`009D:91`) | P4→KK1 |

**Arah koreksi:** versi `009D`/`009E` lebih dapat dipertahankan secara logis — *Enterprise Architecture* memang menopang KK4 (Tata Kelola), sedangkan *BPM* dan *OOP* memang menopang KK5 (Platform Engineering). Jadi **`003` sebagai master perlu disinkronkan ke `009D`/`009E`**, bukan sebaliknya.

Dampak akreditasi rendah karena tidak mengubah jumlah atau cakupan BoK, tetapi asesor yang membandingkan dua tabel akan menemukannya.

### P2-6c. Indeks Dokumen di `009_LANGKAH2_CPL_FORMAL.md` §7 Sudah Kedaluwarsa

| Aspek | Status |
|---|---|
| Substansi 14 CPL, Target Bloom, jumlah BoK, 55 MK/146 SKS, 67 MK/182 SKS | ✅ **Konsisten** dengan `003`/`009A`–`009E` |
| §1 (Ringkasan 14 CPL) | ⚠️ Duplikat fungsi `009E` §1 |
| §3 (Matriks CPL↔Peminatan) | ⚠️ **Identik verbatim** dengan `009E` §5 (14/14 baris) |
| **§7 (Panduan Navigasi, baris 117–129)** | ❌ **Kedaluwarsa** — indeks berhenti di Dokumen 011; tidak memuat 012–018 maupun Buku Final |

**Penilaian eksplisit:** file ini **konsisten secara substansi, bukan artefak usang yang bertentangan**, tetapi **redundan secara struktural**. Satu-satunya bagian yang benar-benar *stale* adalah §7.

**Inkonsistensi minor internal:** §3 baris 56–59 menamai profil dengan label ad-hoc yang tidak ada dalam daftar resmi 4 PL — `PL-1 (Data Scientist & MLOps Specialist)`, `PL-2 (Cloud Systems Integrator & IoT Architect)`, `PL-2 (IT Auditor & Cybersecurity GRC Specialist)`, `PL-3 (UI/UX Designer & Full-Stack Platform Engineer)`. Label ini adalah **peran karier**, bukan nomenklatur PL. Bila dibaca asesor sebagai nomenklatur, akan tampak seolah ada lebih dari 4 PL.

**Rekomendasi:** pertahankan sebagai "Dokumen Pengantar Langkah 2", tetapi (a) perbarui §7 agar memuat 012–018 dan Buku Final, atau hapus §7 dan rujuk ke `index.html`; (b) ganti label ad-hoc §3 dengan nomenklatur PL resmi.

### P2-6d. Ambiguitas Notasi `P1`/`P2`/`P3` Dipakai Ganda

| Makna | Contoh Penggunaan |
|---|---|
| CPL Pengetahuan | `P1`, `P2`, `P3`, `P4` (dari 14 CPL) |
| Kode Peminatan | `P1: Integrated Smart Systems`, `P2: Cloud Infrastructure & Cybersecurity`, `P3: Digital Platform Engineering` |

Penggunaan ganda ini **konsisten di semua file** (jadi bukan inkonsistensi), tetapi berpotensi disalahbaca asesor pada `009A` §5, `009B` §5, `009C` §5, dan `009E` §5 — di mana kedua makna muncul berdekatan.

**Rekomendasi kosmetik:** gunakan `PM-1`/`PM-2`/`PM-3` untuk kode peminatan.

### P2-6e. Enam Baris CPMK Memakai Level Bloom Majemuk atau Ranah Afektif

| Baris di 007 | Level Tertulis | Penilaian |
|:---:|:---:|---|
| 294 | `A3` | ✅ Wajar (MKWU, ranah afektif) |
| 295 | `A3, C3` | ⚠️ Majemuk |
| 336 | `C3, A3` | ⚠️ Majemuk |
| **1061** | **`C5, C6`** | ❌ **`STI-413` CPMK-4 menggabungkan dua level kognitif** — menyulitkan penentuan level asesmen tunggal |
| 1359 | `C3, A3` | ⚠️ Majemuk |
| 1955 | `A3, C3` | ⚠️ Majemuk |

Pemakaian ranah afektif `A3` pada MKWU dapat dipertahankan. Yang perlu dikoreksi adalah baris 1061 (`C5, C6`) karena menggabungkan dua level kognitif dalam satu CPMK.

### P2-6f. Nomenklatur Kosmetik dan Duplikasi Nama Inggris

| Jenis | Detail | Volume |
|---|---|:---:|
| Perbedaan kosmetik `007` vs `005` | `&` vs `and`, tanda kurung, urutan akronim: `MKU-507`, `STA-02/05/06`, `STB-01/04/05/06`, `STC-01` | 9 MK |
| Nama Inggris ditulis dua kali di heading | Contoh `007:2448`: `### 57. STB-04 — IT Governance & Compliance (COBIT 2019) (IT Governance & Compliance (COBIT 2019))` | 10 MK peminatan |
| Perlu dicermati | `STC-06`: `007` "Digital Product Management **& Agile Practices**" vs `005` "Digital Product Management" (narasi `005` memang menyebut Agile, jadi ini pemendekan di `005`) | 1 MK |

### P2-6g. Artefak Sementara di Folder

| File | Ukuran | Timestamp | Keterangan |
|---|:---:|---|---|
| `_tmp_audit.py` | 553 byte | 23 Agustus 2026, 20:02 | Skrip sementara sisa pekerjaan sebelumnya (memproses dokumen 004). Aman dibersihkan. |

---

# BAGIAN IV — ASPEK YANG TERVERIFIKASI BERSIH

Bagian ini dinyatakan eksplisit agar audit ini berimbang dan agar Tim Pengembang tidak mengerjakan ulang hal yang sudah benar.

## 4.1 Ketiadaan Kode Mata Kuliah Usang — Bersih Total

Pencarian pola `STI-104`, `STI-205`, `FST-208`, `STI-203`, `STI-204`, `STI-208`, dan string "Logika Informatika" pada seluruh 26 file Markdown:

| File | Hasil |
|---|:---:|
| `001`, `002`, `003`, `004`, `009A`–`009E`, `009_LANGKAH2`, `011` | **0 kemunculan** ✅ |
| `007` (2.824 baris, dipindai penuh dengan pola `(FST\|STI\|MKU\|STA\|STB\|STC)-\d+`) | **0 kode di luar daftar ground truth** ✅ |

Kemunculan kode lama hanya pada 3 file, dan **seluruhnya kontekstual-historis yang sah**:

| File | Baris | Konteks | Penilaian |
|---|:---:|---|:---:|
| `017_AUDIT_FORENSIK...md` | 69, 139–145 | Tabel **log koreksi** yang mendokumentasikan penggantian `STI-104`/`STI-205`/`FST-208` | ✅ Wajib menyebut kode lama |
| `016_ANALISIS_BoK...md` | 66, 151 | Rasionalisasi peleburan "STI-103 Logika Informatika" ke `STI-204` | ✅ Sah |
| `BUKU...FINAL.md` | 850 | **Tabel ekuivalensi kurikulum lama→baru** Bab VIII | ✅ Wajib menyebut nama MK lama |

Kutipan `BUKU:850`:

```
| `STI-103` | Logika Informatika (Lama) | 3 | `STI-103` | Arsitektur & Organisasi Sistem TI | 3 | Ekuivalen / Penyesuaian Topik |
```

**Catatan:** ketujuh temuan yang dilaporkan `_tools/deep_cross_audit.py` seluruhnya adalah *false positive* dari kategori ini — skrip tersebut menandai tabel log koreksi di `017` sebagai pelanggaran, padahal tabel log memang harus menyebut kode lama.

## 4.2 Konsensus `STI-103` dan `STI-204` — Terpasang Konsisten

| Konsensus | Verifikasi |
|---|---|
| `STI-103` = "Arsitektur dan Organisasi Sistem Teknologi Informasi", 3 SKS, Sem 1 | ✅ `004:65`, `005:88`, `011:127`, `BUKU:232`, `BUKU:1452`, `BUKU:1458` |
| `STI-204` = "Matematika Diskrit dan Logika", 3 SKS, Sem 2 | ✅ `004:69`, `005:99`, `011:128`, `BUKU:241`, `BUKU:1619`, `BUKU:1625` |

## 4.3 Jumlah 14 CPL, 3 PEO, dan 4 PL — Bersih Total

| Aspek | Hasil |
|---|:---:|
| Kode CPL yang dipakai | Tepat `S1`, `KU1`–`KU3`, `P1`–`P4`, `KK1`–`KK6` = **14 CPL** ✅ |
| Kode CPL asing (`KK7`, `P5`, `KU4`-sebagai-CPL, `S2`-sebagai-CPL) | **0 kemunculan** ✅ |
| Penyebutan "10 CPL", "15 CPL", "17 CPL" | **0 kemunculan** ✅ |
| Kode PEO | Konsisten `PEO-1`–`PEO-3` di `002`, `003`, `004` ✅ |
| Kode PL | Konsisten `PL-1`–`PL-4`; tidak ada PL-5/PL-6 sebagai PL aktif ✅ |

Dua hal yang tampak seperti anomali tetapi terverifikasi sah:

| Temuan | Lokasi | Penjelasan |
|---|---|---|
| `PL-01`..`PL-06` | `002:15-26` | Tabel peleburan **profil lama**, eksplisit berlabel "Profil Lama (6 PL)" ✅ |
| `S2`..`S10`, `KU4`..`KU9`, `CPL-P01`..`P17`, `CPL-K01`..`K17`, `S01`..`S08`, `KU01`..`KU08` | `003`, `009A:66-75`, `009B:27-32`, `009C` | Kode **sumber** SN-Dikti dan APTIKOM/IS2020, bukan CPL prodi ✅ |

## 4.4 Jumlah BoK — Konsisten 100%

| Aspek | Hasil |
|---|:---:|
| `BK-IS01`–`BK-IS19` | **19 unik**, lengkap di `003`, `004`, `009D`, `009E` ✅ |
| `BK-IT01`–`BK-IT14` | **14 unik**, lengkap di `003`, `004`, `009D`, `009E` ✅ |
| Klaim tekstual "19 BoK IS2020 & 14 BoK IT2017" | Konsisten di `009E:6`, `009_LANGKAH2:38/73/85`, `011:27/419`, `004:206` ✅ |
| Angka menyimpang ("18 BoK", "20 BoK", "27 BoK" sebagai jumlah dipetakan) | **0 kemunculan** ✅ |

`003:24` menuliskan "IT2017 (14/27 Bahan Kajian)" — ini **benar**, artinya 14 dari 27 total BoK IT2017 yang dipetakan.

## 4.5 Skema Asesmen 4 Titik — Bersih Sempurna

| Aspek | Hasil |
|---|:---:|
| MK dengan tepat 4 titik asesmen | **65/65** ✅ |
| MK dengan total bobot tepat 100% | **65/65** ✅ |
| Pola MK Teori `20/30/20/30` | 28 MK ✅ |
| Pola MK non-Teori `20/25/25/30` | 37 MK ✅ |
| Bobot asesmen Sheet 8 `011` (6 MK penciri) | 6/6 tepat 100% ✅ |
| Konsistensi skema di Sheet 9–12 `011` | ✅ |

## 4.6 Matriks 16 Pertemuan — Bersih Sempurna

| Aspek | Hasil |
|---|:---:|
| MK dengan tepat 16 baris pertemuan bernomor 1–16 | **65/65** ✅ |
| Total baris pertemuan | 1.040 baris, tanpa duplikat/gap/baris terpotong ✅ |
| Kelengkapan 7 atribut Tabel A (Identitas) | **65/65** ✅ (Kode & Nama, Bobot SKS/Tipe, Semester/Rumpun, Prasyarat, CPL Dibebankan, Profil Lulusan, Target PEO) |

## 4.7 Aritmetika Dokumen 005 — Bersih Sempurna

Hasil rekalkulasi mandiri (parsing 55 baris MK, bukan membaca label subtotal):

| Aspek | Hasil Hitung Ulang | Klaim di 005 | Verdict |
|---|:---:|:---:|:---:|
| Total SKS | 146 | 146 | ✅ |
| Total MK | 55 | 55 | ✅ |
| Subtotal per semester | 19/20/20/21/21/19/20/6 | Sama | ✅ |
| Kumulatif per semester | 19/39/59/80/101/120/140/146 | Sama | ✅ |
| MKWU | 8 MK / 13 SKS | 8 MK / 13 SKS | ✅ |
| FSTI | 13 MK / 36 SKS | 13 MK / 36 SKS | ✅ |
| Core STI | 28 MK / 79 SKS | 28 MK / 79 SKS | ✅ |
| Elektif Peminatan | 6 MK / 18 SKS | 6 MK / 18 SKS | ✅ |
| Batas Sem 1 & 2 ≤ 20 SKS (Pasal 18 Permendikbudristek 53/2023) | Sem 1 = 19, Sem 2 = 20 | Sama | ✅ Patuh |
| Beban ≥ 144 SKS syarat lulus nasional | 146 SKS | 146 SKS | ✅ Patuh |

Satu-satunya cacat pada `005` adalah angka proporsi praktikum di baris 57 (lihat P2-4).

## 4.8 Ketiadaan CPL Orphan dan MK Orphan

| Aspek | Hasil |
|---|:---:|
| CPL orphan di `004` | **0** — setiap dari 14 CPL punya ≥ 4 MK pembina ✅ |
| CPL orphan di `011` | **0** — setiap CPL punya ≥ 5 MK pendukung ✅ |
| MK orphan di `011` Sheet 5 | **0 dari 67 MK** ✅ |
| MK tanpa pemetaan di `004` | 6 baris `STA/B/C` memakai notasi `*` (bukan sel kosong) — sah, tetapi legendanya belum didefinisikan (lihat P1-3) |

## 4.9 Kesamaan Rumusan yang Terverifikasi Identik Verbatim

| Perbandingan | Cakupan | Hasil |
|---|---|:---:|
| `003` ↔ `009C` | `P1`–`P4` | ✅ Identik verbatim |
| `003` ↔ `009D` | `KK1`–`KK6` | ✅ Identik verbatim |
| `003` §6 ↔ `009E` §4 | Matriks CPL↔PL | ✅ Identik 4/4 baris |
| `009_LANGKAH2` §3 ↔ `009E` §5 | Matriks CPL↔Peminatan | ✅ Identik 14/14 baris |
| `011` Sheet 5 ↔ Sheet 7 | Pemetaan CPL 46 MK bersama | ✅ Konsisten 100% |
| Target Bloom 14 CPL | 6 file (`003`, `009A`–`009E`, `009_LANGKAH2`) | ✅ Konsisten 100% |

## 4.10 Rekapitulasi Portofolio dan Sebaran di Dokumen 011 — Bersih

| Aspek | Hasil |
|---|:---:|
| Total MK Sheet 5 | **67** ✅ |
| Total SKS Sheet 5 | **182** ✅ |
| Subtotal MKWU / FSTI / Core STI | 8/13, 13/36, 28/79 — semuanya tepat ✅ |
| Subtotal elektif P1 / P2 / P3 | Masing-masing 6 MK / 18 SKS ✅ |
| Sheet 6: subtotal SKS per semester | 19/20/20/21/21/19/20/6 = **146** ✅ |
| Sheet 3: jumlah baris CPL | 14 baris, tanpa duplikat/kekurangan ✅ |
| Jumlah sheet | 14 heading `## Sheet N`, sesuai klaim `011:7`; file `.xlsx` berisi 15 tab (14 + Cover) ✅ |

## 4.11 VMTS 2045 di Dokumen Sumber

| Aspek | Hasil |
|---|:---:|
| Rumusan Visi 2045 di `001:56` | ✅ Sesuai ground truth `AGENTS.md` **verbatim** |
| Keselarasan VMTS → CPL | ✅ Terdokumentasi di `009E` §6 |
| Rumusan Visi di Buku Final | ❌ **Tidak ada** (lihat P0-2) |

## 4.12 Sebaran Semester MK Elektif

| Aspek | Hasil |
|---|:---:|
| 18 MK elektif berada di semester yang benar (`-01`→Sem 5, `-02`/`-03`→Sem 6, `-04`/`-05`/`-06`→Sem 7) | **18/18** ✅ |
| Setiap MK elektif = 3 SKS | **18/18** ✅ |
| Semester per MK di `007` (65 blok) | **64/65 benar**; hanya `STI-625` yang salah SKS (semesternya benar) ✅ |

---

# BAGIAN V — TEMUAN TENTANG ALAT VERIFIKASI

Bagian ini penting karena menjelaskan **mengapa** temuan-temuan di atas dapat lolos selama ini.

## 5.1 `verify_zero_discrepancy.py` Hanya Memeriksa Dua Pola String

Skrip `_tools/verify_zero_discrepancy.py` (41 baris) melaporkan:

```
Auditing 26 markdown files in KURIKULUM2026_REVISI...
[SUCCESS] 100% PERFECT ALIGNMENT: Semua file Markdown di KURIKULUM2026_REVISI telah 100% sinkron dan selaras!
```

Namun pembacaan kode pada baris 22–35 menunjukkan skrip ini **hanya menjalankan dua pemeriksaan**:

| Pemeriksaan | Baris | Logika |
|:---:|:---:|---|
| 1 | 23–28 | Apakah baris yang memuat `STI-103` juga memuat "Logika Informatika" tanpa penanda "(Lama)" |
| 2 | 31–35 | Apakah baris yang memuat `STI-204` menyebut "Matematika Diskrit" tanpa kata "Logika" |

### Yang Tidak Diperiksa oleh Skrip Ini

| Aspek | Diperiksa? | Temuan yang Lolos |
|---|:---:|---|
| Jumlah dan total SKS | ❌ | P0-3a, P0-3b, P0-3c |
| Jumlah MK per kategori | ❌ | P0-3a |
| Subtotal & kumulatif per semester | ❌ | P0-3b |
| Kelengkapan struktur bab | ❌ | P0-2 |
| Tabrakan kode MK aktif | ❌ | P0-1 |
| Rantai prasyarat | ❌ | P1-2 |
| Jumlah CPMK per MK | ❌ | P1-1 |
| Keseragaman rumusan CPL | ❌ | P1-4 |
| Ketunggalan matriks CPL↔PL / PEO↔CPL | ❌ | P1-5 |
| Reproduktibilitas angka rekapitulasi | ❌ | P1-3, P2-3, P2-5 |
| Validitas sintaks tabel Markdown | ❌ | P2-2 |
| Kelengkapan jumlah silabus | ❌ | P2-1 |

**Kesimpulan:** klaim "100% PERFECT ALIGNMENT" pada output skrip, dan klaim "100% tuntas dan terverifikasi" pada `AGENTS.md`, **tidak memiliki dasar verifikasi yang memadai**. Skrip tersebut memvalidasi dua nomenklatur mata kuliah, bukan keselarasan kurikulum.

## 5.2 `deep_cross_audit.py` Menghasilkan Tujuh False Positive

Skrip `_tools/deep_cross_audit.py` melaporkan 7 temuan, seluruhnya pada `017_AUDIT_FORENSIK...md` baris 139–145. Namun baris-baris tersebut adalah **tabel log koreksi** yang secara fungsional **harus** menyebut kode lama (`STI-104`, `STI-205`, `FST-208`) untuk mendokumentasikan penggantiannya.

Skrip ini sudah memiliki mekanisme pengecualian (`if fname not in [...]` pada baris 110) tetapi hanya mengecualikan `016_ANALISIS_BoK...md`, tidak `017`. Perbaikan: tambahkan `017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md` ke daftar pengecualian, atau lebih baik, kecualikan baris yang berada dalam konteks tabel ekuivalensi/log koreksi.

## 5.3 Rekomendasi Penguatan Alat Verifikasi

Sebelum melakukan koreksi substansi, **prioritaskan penulisan ulang skrip verifikasi**, agar regresi seperti P0-3 tidak lolos lagi. Cakupan minimum yang perlu diverifikasi otomatis:

| No | Pemeriksaan | Metode |
|:---:|---|---|
| 1 | Total SKS = 146 dan total MK = 55 | Parse tabel struktur, jumlahkan kolom SKS, bandingkan dengan label |
| 2 | Subtotal & kumulatif tiap semester | Rekalkulasi berantai, bandingkan dengan label subtotal |
| 3 | Komposisi rumpun (MKWU/FSTI/Core/Elektif) | Group-by kolom Kategori |
| 4 | Konsistensi SKS tiap kode MK lintas file | Bangun kamus `kode → SKS` per file, diff antar file |
| 5 | Konsistensi nama tiap kode MK lintas file | Bangun kamus `kode → nama` per file, diff antar file (akan menangkap P0-1) |
| 6 | Rantai prasyarat valid (semester prasyarat < semester MK) | Topological check terhadap kamus semester |
| 7 | Jumlah CPMK per MK = 4 | Hitung baris CPMK per blok |
| 8 | Total bobot asesmen = 100% dan jumlah titik = 4 | Parse kolom persentase |
| 9 | Jumlah baris pertemuan = 16 | Hitung baris matriks per blok |
| 10 | Jumlah kolom header = separator = tiap baris data | Validasi struktural tiap tabel |
| 11 | Kelengkapan heading Bab I–VIII | Cek keberadaan pola `# BAB {I..VIII}` |
| 12 | Jumlah blok silabus = 67 | Hitung heading `### N. KODE — Nama` |
| 13 | Rumusan tiap CPL identik lintas file | Normalisasi whitespace, diff string |
| 14 | Setiap CPL memiliki minimal satu `I`, satu `R`, satu `M` | Rekalkulasi matriks I/R/M |

---

# BAGIAN VI — RENCANA TINDAK LANJUT

## 6.1 Urutan Pengerjaan yang Direkomendasikan

Urutan ini dirancang agar tidak terjadi kerja ganda — keputusan yang berdampak luas diselesaikan lebih dulu.

| Tahap | Tindakan | Alasan Urutan | Pemilik Keputusan |
|:---:|---|---|---|
| **0** | Perkuat `verify_zero_discrepancy.py` sesuai §5.3 | Agar setiap koreksi berikutnya dapat diverifikasi otomatis dan regresi tidak lolos lagi | Agent (teknis) |
| **1** | **Putuskan identitas `FST-204` & `FST-205`** (P0-1) | Menentukan arah koreksi di `004`, `005`, `007`, dan Buku Final sekaligus. Tanpa ini, keempat dokumen tidak dapat dikoreksi konsisten | **Tim Pengembang Kurikulum** |
| **2** | Putuskan penyelesaian jumlah CPMK (P1-1) | Menentukan volume kerja pada 31 MK di `007` dan Lampiran 2 Buku Final | **Tim Pengembang Kurikulum** |
| **3** | Koreksi angka P0-3 di Buku Final (komposisi rumpun, Sem 6, kumulatif Sem 6–7, `STI-625`) | Murni aritmetika, angka benar sudah tersedia di `005` | Agent (teknis) |
| **4** | Satukan rantai prasyarat `007` → `005` (P1-2) | Setelah Tahap 1 selesai, karena `FST-204`/`FST-205` muncul sebagai prasyarat | Agent + validasi Tim |
| **5** | Rekonstruksi Bab I, III, V Buku Final (P0-2) | Materi tersedia di `001`, `003`, `009A`–`009E`; pekerjaan penggabungan | Agent (teknis) |
| **6** | Satukan rumusan 14 CPL (P1-4) dan matriks CPL↔PL / PEO↔CPL (P1-5) | Perlu keputusan versi mana yang berlaku | **Tim Pengembang** + Agent |
| **7** | Perbaiki angka rekapitulasi `004` §5 (P1-3) dan `011` (P2-3, P2-5) | Setelah pemetaan CPL final, agar tidak dihitung dua kali | Agent (teknis) |
| **8** | Selesaikan penguatan `KK4` (P1-3, P1-5c) | Memerlukan keputusan kurikuler: MK wajib mana yang menopang KK4 bagi mahasiswa P1/P3 | **Tim Pengembang Kurikulum** |
| **9** | Kebersihan teknis: separator `011`, kolom `004:76`, silabus `MKU-406`/`MKU-508`, proporsi praktikum, indeks `009_LANGKAH2`, hapus `_tmp_audit.py` | Independen, dapat dikerjakan paralel | Agent (teknis) |
| **10** | Regenerasi seluruh HTML/XLSX/DOCX + jalankan skrip verifikasi baru | Finalisasi | Agent (teknis) |

## 6.2 Keputusan yang Memerlukan Tim Pengembang Kurikulum

Empat keputusan berikut **tidak dapat diambil oleh agent** karena menyangkut substansi kurikulum, bukan konsistensi teknis:

| No | Keputusan | Pertanyaan Konkret |
|:---:|---|---|
| **1** | Identitas `FST-204` & `FST-205` | Mata kuliah mana yang benar mengisi Semester 2: (Pengantar KA & Data + Basic English for IT) atau (Organisasi & Arsitektur Komputer + Pemrograman Lanjut OOP)? Bila keempatnya diperlukan, MK mana yang digeser agar Semester 2 tetap ≤ 20 SKS? |
| **2** | Jumlah CPMK | Tambahkan CPMK ke-4 pada 31 MK (terutama 12 MK peminatan STB/STC), atau longgarkan narasi pemetaan 1-to-1? |
| **3** | Penguatan `KK4` | Bagaimana menjamin CPL KK4 (Tata Kelola & Audit TI) tercapai oleh mahasiswa peminatan P1 dan P3, yang tidak menempuh elektif STB? |
| **4** | Versi rumusan CPL yang berlaku | Untuk `S1` (versi `003` vs `009A`/`011`), `KU2` (versi `003` vs `009B`), `KK3` (dengan atau tanpa IoT), dan `P4` (domain RPL vs domain data) |

## 6.3 Estimasi Volume Koreksi Teknis

| Kategori | Jumlah Titik Koreksi | File Terdampak |
|---|:---:|---|
| Angka SKS & komposisi (P0-3) | 10 baris | `BUKU`, `006`, `007` |
| Struktur bab (P0-2) | 3 bab + 5 diagram + 6 bagian `## 1.` + 1 daftar isi | `BUKU` |
| Rantai prasyarat (P1-2) | 19 MK | `007` |
| Jumlah CPMK (P1-1) | 31 MK | `007`, `BUKU` |
| Rumusan CPL (P1-4) | 6 CPL | `003`, `011` |
| Matriks pemetaan (P1-5, P2-3e) | 5 CPL + 14 MK | `011`, `004` |
| Angka rekapitulasi (P1-3, P2-3, P2-5) | 12 + 34 + 2 = 48 sel | `004`, `011`, `BUKU` |
| Sintaks & kebersihan (P2-2, P2-6) | 4 separator + 1 baris kolom + 2 silabus + 1 indeks + 1 file | `011`, `004`, `007`, `009_LANGKAH2` |

---

# BAGIAN VII — PENUTUP

## 7.1 Ringkasan Penilaian

Folder `KURIKULUM2026_REVISI/` memiliki **fondasi substansi yang kuat** namun **lapisan konsistensi yang belum tuntas**.

Yang sudah kokoh: seluruh kerangka makro OBE (VMTS → 3 PEO → 4 PL → 14 CPL → 33 BoK) memiliki jumlah dan cakupan yang benar tanpa satu pun kode asing; dokumen `005` sebagai sumber struktur terverifikasi bersih secara aritmetika; skema 4 titik asesmen dan matriks 16 pertemuan bersih sempurna pada 65 dari 65 mata kuliah; tidak ada kode mata kuliah usang; tidak ada CPL orphan maupun MK orphan.

Yang belum tuntas terpusat pada tiga hal. Pertama, **tabrakan identitas `FST-204`/`FST-205`** yang membuat dua mata kuliah kehilangan silabus dan dua mata kuliah lain kehilangan slot semester. Kedua, **Buku Kurikulum Final belum layak diajukan** karena kehilangan Bab I, III, dan V, tidak memuat rumusan Visi 2045 maupun rumusan tekstual 14 CPL, dan memuat angka komposisi serta sebaran SKS yang salah. Ketiga, **angka rekapitulasi di berbagai dokumen tidak dapat direproduksi** dari data yang mendasarinya, sehingga klaim seperti "alokasi SKS yang solid" tidak terdukung.

Akar persoalan bersifat prosedural: alat verifikasi yang tersedia hanya memeriksa dua pola string, sehingga regresi numerik dan struktural pada dokumen turunan tidak pernah terdeteksi. Karena itu penguatan alat verifikasi diletakkan sebagai Tahap 0 dalam rencana tindak lanjut.

## 7.2 Pernyataan Batas Audit

Audit ini memeriksa konsistensi numerik, kelengkapan struktural, dan keterlacakan referensi silang. Hal-hal berikut **tidak diaudit** dan tidak boleh dianggap tervalidasi oleh laporan ini:

| Aspek | Status |
|---|---|
| Ketepatan pedagogis rumusan CPMK dan Sub-CPMK | Tidak diaudit |
| Kelayakan level Bloom yang dipilih per CPMK | Tidak diaudit (kecuali 6 baris level majemuk pada P2-6e) |
| Kesesuaian substansi materi 16 pertemuan terhadap standar industri | Tidak diaudit |
| Ketepatan pemetaan BoK terhadap dokumen asli IS2020 dan IT2017 | Tidak diaudit (hanya konsistensi internal antar file) |
| Validitas simulasi akselerasi 7 semester (`015`) | Tidak diaudit — perlu validasi ulang setelah rantai prasyarat disatukan |
| Kelayakan sumber daya laboratorium dan SDM dosen (Bab VIII) | Tidak diaudit |
| Kesesuaian dokumen `013`, `014`, `018` | Tidak diaudit secara mendalam |
| Isi file `.xlsx`, `.docx`, dan `.html` hasil ekspor | Tidak diaudit — audit dilakukan pada file `.md` sumber |

## 7.3 Status Perubahan File

**Tidak ada file yang diubah oleh audit ini.** Laporan ini bersifat diagnostik. Seluruh temuan disertai nomor baris agar dapat diverifikasi ulang secara independen sebelum koreksi diterapkan.

---

## LAMPIRAN — INDEKS TEMUAN BERDASARKAN FILE

| File | Temuan Terkait | Jumlah |
|---|---|:---:|
| `003_STANDAR_14_CPL...md` | P1-4e (KU2), P1-4f (S1 outlier), P1-5b (PEO↔CPL), P2-6b (4 sel BoK) | 4 |
| `004_MATRIKS_KETERLACAKAN...md` | P0-1 (FST-204/205), P1-3 (rekap §5 + KU3 salah domain + legenda `*` + kolom `:76`), P2-3e | 3 |
| `005_STRUKTUR_KURIKULUM...md` | P2-4 (proporsi praktikum) | 1 |
| `006_DISTRIBUSI...MBKM.md` | P0-3c (`STI-625` 3 SKS) | 1 |
| `007_FORMULASI_CPMK...md` | P0-1, P0-3c, P1-1 (31 MK), P1-2 (19 MK), P2-1 (65 vs 67), P2-6e, P2-6f | 7 |
| `009_LANGKAH2_CPL_FORMAL.md` | P2-6c (indeks stale + label PL ad-hoc) | 1 |
| `011_IMPLEMENTASI_OBE...md` | P1-4a–d (rumusan CPL), P1-5a (Sheet 3 vs 4), P1-5c (I→R→M), P2-2 (separator), P2-3 (34 sel) | 5 |
| `BUKU_KURIKULUM...FINAL.md` | P0-1, P0-2 (bab hilang), P0-3 (angka salah), P2-1, P2-5 (IKU 7) | 5 |
| `_tools/verify_zero_discrepancy.py` | §5.1 (cakupan tidak memadai) | 1 |
| `_tools/deep_cross_audit.py` | §5.2 (7 false positive) | 1 |
| `_tmp_audit.py` | P2-6g (artefak sementara) | 1 |

---

*Dokumen 019 — Laporan Audit Kritis Keselarasan Folder `KURIKULUM2026_REVISI/`*
*Disusun 23 Agustus 2026, 21:29:23 WIB*
*Status: Laporan Temuan Diagnostik — belum ada perbaikan yang diterapkan*
**Tim Pengembang Kurikulum FSTI Universitas Widyagama Malang**
