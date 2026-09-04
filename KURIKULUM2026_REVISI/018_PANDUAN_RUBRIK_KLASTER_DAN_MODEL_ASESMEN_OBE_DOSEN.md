# 018 — PANDUAN MASTER RUBRIK KLASTER, INDIKATOR KINERJA & MODEL ASESMEN OBE DOSEN

## PROGRAM STUDI SISTEM DAN TEKNOLOGI INFORMASI (SISTEKIN)
### FAKULTAS SAINS DAN TEKNOLOGI INFORMASI (FSTI) — UNIVERSITAS WIDYAGAMA MALANG

---

## 1. PENDAHULUAN & LANDASAN ASESMEN OBE SISTEKIN 2026

Dokumen ini merupakan **panduan operasional asesmen resmi** bagi seluruh dosen pengampu mata kuliah di Program Studi Sistem dan Teknologi Informasi (SISTEKIN) FSTI UWG. Panduan ini dirancang khusus untuk memenuhi standar akreditasi **LAM INFOKOM / APTIKOM OBE v2.0** dan **Permendikbudristek No. 53 Tahun 2023**, dengan berpegang pada 5 prinsip utama:
1. **Akuntabel & Terukur:** Setiap komponen nilai berakar langsung dari Capaian Pembelajaran Mata Kuliah (CPMK) dan CPL prodi.
2. **Profesional & Terstandar:** Menghilangkan subjektivitas penilaian dengan rubrik analitik berbasis kriteria (*criterion-referenced*).
3. **Jujur & Otentik:** Dilengkapi protokol verifikasi keaslian karya (*live code walkthrough* & riwayat commit Git).
4. **Efisiensi Beban Dosen (*Lecturer-Friendly*):** Membatasi evaluasi formal hanya pada **4 Titik Asesmen Baku** yang memetakan secara langsung *1-to-1* ke 4 CPMK, sehingga meniadakan kerumitan konversi matriks nilai.
5. **Kepatuhan Mutlak IKU 7 ($\ge 50\%$):** Mengintegrasikan metode pembelajaran pemecahan kasus (*Case Method*) dan proyek tim (*Team-Based Project*) ke dalam skema UTS dan UAS.

---

## 2. ARSITEKTUR 4 TITIK ASESMEN BAKU (1-TO-1 CPMK MAPPING)

Seluruh 67 mata kuliah portofolio SISTEKIN 2026 wajib menerapkan skema evaluasi 4 titik berikut:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        ARSITEKTUR 4-TITIK ASESMEN BAKU SISTEKIN 2026 (1-to-1 OBE MAPPING)              │
├───────────────────┬──────────────┬──────────────────┬─────────────────┬────────────────────────────────┤
│ TITIK ASESMEN     │ WAKTU UJI    │ CPMK TARGET      │ LEVEL BLOOM     │ BENTUK BUKTI OTENTIK (EVIDENCE)│
├───────────────────┼──────────────┼──────────────────┼─────────────────┼────────────────────────────────┤
│ 1. TUGAS 1        │ Pekan 4      │ **CPMK-1**       │ C2 – C3         │ Kuis Analitik / Problem Solving│
│    (Bobot: 20%)   │              │ (Fondasi Dasar)  │ (Understand)    │ Mandiri (Studi Kasus Awal)     │
├───────────────────┼──────────────┼──────────────────┼─────────────────┼────────────────────────────────┤
│ 2. UTS            │ Pekan 8      │ **CPMK-2**       │ C3 – C4         │ Case-Method Exam / Evaluasi    │
│    (Bobot: 25-30%)│              │ (Aplikasi Kasus) │ (Apply/Analyze) │ Modul Praktikum Terjadwal      │
├───────────────────┼──────────────┼──────────────────┼─────────────────┼────────────────────────────────┤
│ 3. TUGAS 2        │ Pekan 12     │ **CPMK-3**       │ C4 – C5         │ Team-Based Project (Milestone) │
│    (Bobot: 20-25%)│              │ (Desain Solusi)  │ (Evaluate)      │ / Implementasi Sistem Mini     │
├───────────────────┼──────────────┼──────────────────┼─────────────────┼────────────────────────────────┤
│ 4. UAS            │ Pekan 16     │ **CPMK-4**       │ C5 – C6         │ Final Project Showcase / Demo  │
│    (Bobot: 30%)   │              │ (Sintesis Akhir) │ (Create/Synthes)│ Produk Portofolio / Ujian Akhir│
└───────────────────┴──────────────┴──────────────────┴─────────────────┴────────────────────────────────┘
```

> **Formula Nilai Akhir Mata Kuliah:**
> $$\text{Nilai Akhir MK} = (w_1 \times \text{CPMK}_1) + (w_2 \times \text{CPMK}_2) + (w_3 \times \text{CPMK}_3) + (w_4 \times \text{CPMK}_4) = 100\%$$
> *Dimana: $w_1 = 20\%$, $w_2 = 25-30\%$, $w_3 = 20-25\%$, $w_4 = 30\%$.*

---

## 3. RUBRIK MASTER 4 KLASTER MATA KULIAH

Dosen pengampu menentukan klaster mata kuliah yang diampu, lalu menerapkan rubrik evaluasi yang bersesuaian:

### KLASTER 1 (K-1): SAINS DASAR & TEORI FORMAL
*Daftar MK: `STI-102 Kalkulus`, `STI-103 Arsitektur & Org. STI`, `STI-204 Matematika Diskrit & Logika`, `STI-205 Aljabar Linear`, `STI-418 Dasar Keamanan Informasi`, `FST-408 Probabilitas & Statistika`, `FST-611 Metodologi Penelitian`.*

* **Bobot Asesmen:** Tugas 1 (20%) | UTS (30%) | Tugas 2 (20%) | UAS (30%)
* **Bentuk Asesmen:** Kuis Analitik, Ujian Tertulis Uraian, Paper Analisis Teorema, Ujian Akhir Komprehensif.

| Kriteria Penilaian | Sangat Baik (80–100) | Baik (68–79) | Cukup (56–67) | Kurang (< 56) |
|---|---|---|---|---|
| **1. Penguasaan Konsep & Formula (40%)** | Menguasai prinsip teoretis dan formula matematika 100% tepat tanpa kekeliruan. | Formula benar, terdapat kesalahan minor pada penulisan notasi/simbol. | Konsep dasar dipahami, namun salah memilih formula turunan. | Salah total dalam memahami definisi dan konsep dasar. |
| **2. Keruntutan Alur Logika (40%)** | Alur pembuktian/perhitungan sistematis, logis, dan runtut dari premis awal ke konklusi. | Alur sebagian besar runtut, terdapat lompatan langkah kecil yang tidak fatal. | Alur perhitungan melompat-lompat dan sulit diverifikasi logikanya. | Jawaban tidak runtut, tidak ada jalan pengerjaan, atau menebak. |
| **3. Akurasi Hasil Akhir (20%)** | Nilai/hasil akhir 100% presisi dengan satuan/format representasi yang tepat. | Hasil akhir terdapat kesalahan aritmatika minor (< 5%). | Hasil akhir salah karena galat perhitungan di tengah alur pengerjaan. | Hasil akhir salah total. |

---

### KLASTER 2 (K-2): REKAYASA PERANGKAT LUNAK & DATA
*Daftar MK: `FST-102 Algoritma`, `FST-203 Struktur Data`, `FST-207 Basis Data`, `STI-311 Web Front-End`, `STI-416 Web Back-End`, `STI-522 Mobile App`, `STI-415 DW & BI`, `STI-627 Platform Engineering`.*

* **Bobot Asesmen:** Tugas 1 (20%) | UTS (25%) | Tugas 2 (25%) | UAS (30%)
* **Bentuk Asesmen:** Coding Challenge/Schema Design, Lab Hands-on Exam, Team Mini-Project (Sprint 1), Final App Showcase & Repositori Git.

| Kriteria Penilaian | Sangat Baik (80–100) | Baik (68–79) | Cukup (56–67) | Kurang (< 56) |
|---|---|---|---|---|
| **1. Fungsionalitas & Bebas Bug (40%)** | Seluruh fitur berjalan 100% mulus, validasi input ketat, tidak ada *crash/runtime error*. | Seluruh fitur utama jalan, terdapat *glitch* minor pada validasi sekunder. | Fitur utama berjalan sebagian, terjadi *error* pada skenario tertentu. | Program tidak dapat di-*compile*, *crash* total, atau fitur utama gagal. |
| **2. Arsitektur & Clean Code (30%)** | Struktur kode modular (MVC/Clean Architecture), penamaan variabel intuitif, ber-standar industri. | Struktur kode rapi, sedikit redundansi kode (*code smell* minor). | Kode monolitik dalam 1 file panjang, sulit dibaca dan dirawat. | Kode berantakan (*spaghetti code*), tidak ada pemisahan layer logika. |
| **3. Basis Data & API Integrity (20%)** | Relasi tabel ternormalisasi (3NF), query efisien, respons status HTTP API presisi. | Relasi tabel benar, query berjalan baik namun belum terindeks optimal. | Terdapat anomali data/redundansi pada tabel, respons API tidak standar. | Basis data rusak (*broken relation*) atau query gagal eksekusi. |
| **4. Repositori & Versi Git (10%)** | Commit message deskriptif, ada branching rapi, dokumentasi `README.md` lengkap. | Menggunakan Git dengan riwayat commit memadai, dokumentasi standar. | Riwayat commit hanya 1x (*single bulk upload*), tanpa README. | Tidak mengumpulkan repositori Git atau repositori kosong. |

---

### KLASTER 3 (K-3): KECERDASAN ARTIFISIAL, CLOUD & CYBERSECURITY
*Daftar MK: `STI-307 AI`, `STI-413 Machine Learning`, `STI-414 NLP & IR`, `STI-519 Deep Learning`, `STI-521 IoT`, `STI-417 Cloud Computing`, `STI-624 Integrasi AI`, `STI-626 Keamanan Lanjut`, seluruh MK Pilihan `STA` dan `STB`.*

* **Bobot Asesmen:** Tugas 1 (20%) | UTS (25%) | Tugas 2 (25%) | UAS (30%)
* **Bentuk Asesmen:** Data Pipeline Prep & Environment, Model Training/Security Audit, Hyperparameter Tuning & Penetration Testing, End-to-End Smart Service Showcase.

| Kriteria Penilaian | Sangat Baik (80–100) | Baik (68–79) | Cukup (56–67) | Kurang (< 56) |
|---|---|---|---|---|
| **1. Metodologi Pipeline & Konfigurasi (35%)** | Alur pipeline (data prep, split, train/test, deploy) 100% valid dan bebas *data leakage*. | Pipeline berjalan baik, terdapat ketidaksempurnaan minor pada normalisasi. | Pipeline melompati tahapan penting (misal: evaluasi tanpa data uji terpisah). | Pipeline salah konsep atau konfigurasi server gagal total. |
| **2. Kinerja & Optimasi Metrik (35%)** | Model mencapai metrik optimal (F1/Accuracy tinggi), latensi server rendah, sistem tangguh. | Metrik performa memadai, model bekerja sesuai ekspektasi standar. | Model mengalami *overfitting/underfitting* parah atau server sering *down*. | Model tidak belajar sama sekali (*random guess*) atau sistem tidak aman. |
| **3. Analisis Hasil & Rekomendasi (20%)** | Mampu menginterpretasikan *confusion matrix*, kurva ROC, *log attack*, dan memberi solusi kritis. | Analisis tepat, mampu membaca grafik metrik dengan interpretasi benar. | Hanya menampilkan grafik tanpa penjelasan makna teknisnya. | Tidak mampu menjelaskan hasil output model atau log sistem. |
| **4. Reproducibility & Dokumentasi (10%)** | Notebook/script terstruktur, `requirements.txt` lengkap, instruksi replikasi mudah dijalankan. | Kode dapat dijalankan ulang dengan sedikit konfigurasi manual. | Kode sulit di-run ulang karena dependensi library tidak dicantumkan. | Kode tidak dapat dieksekusi sama sekali oleh dosen/penguji. |

---

### KLASTER 4 (K-4): SINTESIS, MANAJEMEN, STARTUP & CAPSTONE
*Daftar MK: `STI-306 APSI`, `STI-309 RPL`, `STI-523 Manpro TI`, `STI-625 Smart City`, `STI-728 Startup Digital`, `FST-610 Capstone Project`, `FST-612 PKL`, `FST-613 Pra-Skripsi`, `FST-714 Skripsi`.*

* **Bobot Asesmen:** Tugas 1 (20%) | UTS (30%) | Tugas 2 (20%) | UAS (30%)
* **Bentuk Asesmen:** Problem Discovery & SRS Document, Architecture Design & Interactive Prototype, MVP Testing & UAT, Final Product Pitching & Defense.

| Kriteria Penilaian | Sangat Baik (80–100) | Baik (68–79) | Cukup (56–67) | Kurang (< 56) |
|---|---|---|---|---|
| **1. Relevansi Masalah & Solusi Nyata (30%)** | Solusi menyelesaikan masalah riil mitra/industri secara inovatif dan berdampak tinggi. | Solusi menjawab kebutuhan masalah dengan pendekatan standar industri. | Solusi hanya bersifat simulasi teoritis tanpa konteks pengguna nyata. | Solusi tidak relevan dengan rumusan masalah yang diajukan. |
| **2. Kelengkapan Produk & Rekayasa (30%)** | MVP berfungsi penuh, arsitektur kokoh, teruji dengan UAT bernilai kepuasan tinggi. | Produk berfungsi pada alur utama, modul pendukung masih prototipe. | Produk hanya berupa mockup tampilan tanpa integrasi backend nyata. | Produk tidak selesai atau tidak dapat didemokan. |
| **3. Manajemen Proyek & Kerja Sama Tim (20%)** | Pembagian peran tim seimbang, sprint agile terpantau di Trello/Jira/Git, disiplin *timeline*. | Kolaborasi tim berjalan baik, seluruh anggota berkontribusi aktif. | Kontribusi didominasi 1-2 anggota (*free-rider problem* terdeteksi). | Tim tidak kompak, terjadi konflik internal yang menggagalkan proyek. |
| **4. Presentasi & Naskah Laporan (20%)** | Pitching memukau, demonstrasi lancar, naskah laporan rapi berstandar formal IEEE/UWG. | Presentasi jelas, laporan lengkap sesuai struktur pedoman penulisan. | Presentasi kaku, laporan memiliki banyak kesalahan tata bahasa/format. | Presentasi gagal mendemokan produk, laporan tidak lengkap. |

---

## 4. TEMPLATE LEMBAR ASESMEN CEPAT DOSEN (*SPEED GRADING SHEET*)

Dosen dapat langsung menyalin template berikut ke Excel atau Google Sheets kelas:

```
================================================================================================================
                    LEMBAR ASESMEN OBE CEPAT (SPEED GRADING) - SISTEKIN UWG
================================================================================================================
Mata Kuliah : [STI-413] Machine Learning (3 SKS)                   Semester / Kelas : 4 / A
Klaster     : K-3 (AI, Cloud & Cybersecurity)                     Dosen Pengampu   : [Nama Dosen]
----------------------------------------------------------------------------------------------------------------
No | NIM        | NAMA MAHASISWA   | TUGAS 1 (20%) | UTS (25%) | TUGAS 2 (25%) | UAS (30%) | AKHIR | GRADE |
   |            |                  | [CPMK-1: C3]  | [CPMK-2: C3] | [CPMK-3: C4] | [CPMK-4: C5] | (OBE) |       |
----------------------------------------------------------------------------------------------------------------
1  | 23010001   | Achmad Fauzi     | 85            | 80        | 88            | 90        | 86.0  | A     |
2  | 23010002   | Budi Santoso     | 75            | 70        | 78            | 82        | 76.6  | B+    |
3  | 23010003   | Citra Lestari    | 90            | 85        | 92            | 95        | 90.7  | A     |
4  | 23010004   | Dewi Anggraini   | 80            | 78        | 84            | 88        | 82.9  | A     |
----------------------------------------------------------------------------------------------------------------
RATA-RATA KETERCAPAIAN CPMK        | 82.5% (P1)    | 78.3% (P1)| 85.5% (KK1)   | 88.8% (KK1)| STATUS: TUNTAS│
================================================================================================================
```

---

## 5. PROTOKOL KEJUJURAN AKADEMIK & INTEGRITAS PENGGUNAAN AI

1. **Etika Penggunaan Generative AI (LLM / Copilot / ChatGPT):**
   * Penggunaan AI diperbolehkan sebagai sarana *brainstorming*, referensi sintaksis, dan *debugging*.
   * Mahasiswa **wajib** mencantumkan deklarasi pemanfaatan AI (*AI Transparency Declaration*) pada setiap penyerahan laporan tugas/proyek.
2. **Uji Kejujuran & Validasi Kode 3 Menit (*Code Walkthrough*):**
   * Dosen berhak memanggil mahasiswa secara acak untuk menjelaskan logika baris kode program yang dikumpulkan selama 3 menit.
   * Riwayat commit Git berkala (*Git History*) menjadi bukti sah pengerjaan mandiri oleh mahasiswa bersangkutan.

---

*Dokumen ini merupakan panduan resmi asesmen kurikuler bagi Program Studi SISTEKIN FSTI Universitas Widyagama Malang.*
