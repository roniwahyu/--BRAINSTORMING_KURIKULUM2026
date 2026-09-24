# 049 — LAPORAN RESMI EVALUASI DAN REVISI KURIKULUM: PENETAPAN STA-601 REKAYASA BIG DATA DAN KOMPUTASI TERDISTRIBUSI
## Rekayasa Kurikuler, Audit Standar APTIKOM, Resolusi Curricular Orphan, dan Harmonisasi Sistemik Kurikulum SISTEKIN 2026

---

### Informasi Dokumen
* **Nomor Dokumen:** 049/DEV-REP/KUR-SISTEKIN/2026
* **Status:** Laporan Resmi Evaluasi, Dev Report & Notulen Rekayasa Kurikulum OBE
* **Penyusun:** Tim Pengembang Kurikulum KPT-OBE Program Studi Sistem dan Teknologi Informasi (SISTEKIN)
* **Institusi:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang
* **Objek Evaluasi:** Mata Kuliah `STA-601` (Semester 6, Peminatan 1: Integrated Smart Systems)
* **Dokumen Rujukan Terkait:**
  - Dokumen 003 & 009D (Standar 14 CPL & Indikator Kinerja KK2)
  - Dokumen 004 (Matriks Keterlacakan OBE VMTS-PEO-PL-CPL-MK)
  - Dokumen 005 (Struktur Kurikulum 8 Semester & 3 Jalur Peminatan)
  - Dokumen 007 & Buku Kurikulum Final (Silabus Portofolio 67 MK & Skema 4x Asesmen)
  - Dokumen 024 (Matriks Ekivalensi K2025 → K2026)
  - Dokumen 025 (Rekomendasi Pool Peminatan & Cross-Track 2027)
  - Dokumen 030 (Arsip Justifikasi Awal Metode Komputasi Numerik)
  - Dokumen 043 (Matriks CPL, CPMK, BoK, dan Boundary Guardrails)
  - Dokumen 047 (Kajian Akademis Metode Numerik vs. Riset Operasi vs. Big Data)
  - Dokumen 048 (Surat Keputusan Definitif Penggantian STA-601)

---

## RINGKASAN EKSEKUTIF (EXECUTIVE SUMMARY)

Laporan resmi ini mendokumentasikan proses evaluasi kritis, audit standar kurikulum, penemuan kesenjangan kurikuler (*curricular orphan*), serta eksekusi revisi sistemik multi-dokumen terkait restrukturisasi mata kuliah **`STA-601`** pada Kurikulum OBE Program Studi Sistem dan Teknologi Informasi (SISTEKIN) 2026 FSTI UWG.

Rangkaian kerja ini menghasilkan 4 keputusan strategis kurikulum:
1. **Penggantian Definitif Mata Kuliah:** Menghapus mata kuliah *Computational Methods and Numerics* dan menetapkan **`STA-601 Rekayasa Big Data dan Komputasi Terdistribusi` (*Big Data Engineering & Distributed Systems*)** berbobot **3 SKS (+Praktikum)** pada Semester 6 Peminatan 1 (*Integrated Smart Systems*).
2. **Penyembuhan Anomali Kurikuler (*Curricular Orphan Gap*):** Memberikan "rumah definitif" bagi materi *Apache Spark, PySpark, Data Lakehouse, dan Apache Kafka* yang sebelumnya dijanjikan pada indikator CPL `KK2` (Dokumen 009D) namun sempat dilarang (*Out-of-Scope*) pada `STI-520 Data Mining` (Dokumen 043).
3. **Reposisi Riset Operasi ke Pool Elektif Cross-Track 2027:** Menolak opsi memaksakan Riset Operasi ke Core (karena beban Core sudah optimal 128 SKS) dan mengalokasikannya ke pool pilihan lintas minat (`STA-603` di Dokumen 025) untuk mendukung pemodelan rantai pasok digital dan *Technopreneurship* (`PL-4`).
4. **Harmonisasi Multi-Dokumen dan Ekivalensi Transisi:** Menyelaraskan seluruh dokumen terdampak (Dokumen 004, 005, 007, 024, 025, 030, 043, 047, 048, Buku Final, dan portal HTML) dengan menjaga kestabilan neraca kelulusan **146 SKS / 55 MK** dan portofolio **182 SKS / 67 MK**.

---

## 1. LATAR BELAKANG & TRIGGER EVALUASI KURIKULER

Evaluasi ini dipicu oleh diskusi akademik dan peninjauan mutu kurikulum terkait relevansi materi matematika dan optimasi komputasi:
* **Pertanyaan Awal:** Apakah mata kuliah *Metode Komputasi dan Numerik* yang diwarisi dari Kurikulum 2025 (`STI-317`) masih relevan dipertahankan di Kurikulum 2026, atau sebaiknya diganti menjadi *Riset Operasi* (*Operations Research*)?
* **Dilema Status Core vs. Elektif:** Pada Kurikulum 2025, Metode Numerik berstatus Wajib di Semester 3 karena struktur kurikulum saat itu kaku (*lock-step* 56 MK wajib tanpa pilihan). Pada Kurikulum 2026, mata kuliah tersebut sempat digeser menjadi elektif `STA-601` di Peminatan 1. Namun, hal ini menimbulkan pertanyaan: mengapa mahasiswa jalur Cloud/Cyber (`P2`) dan Platform/UX (`P3`) tidak menempuhnya, dan apakah salah satunya perlu diwajibkan di Core?
* **Pertimbangan "The Missing Piece":** Jika ditinjau dari profil lulusan **PL-1 (Intelligent IS Developer & Data/AI Engineer)**, apakah Riset Operasi adalah pengganti terbaik, ataukah ada kompetensi industri yang jauh lebih mendesak dan saat ini belum memiliki wadah di kurikulum?

---

## 2. AUDIT FORENSIK STANDAR APTIKOM & REGULASI NASIONAL

Tim Arsitektur Kurikulum melakukan audit forensik terhadap naskah standar kurikulum asosiasi:

| Parameter Evaluasi | Standar APTIKOM SI v2.0 (IS2020) | Standar APTIKOM TI 2023 (IT2017/CC2020) |
|---|---|---|
| **Metode Numerik di Core** | ❌ **Bukan Core Wajib.** Bahan kajian matematika (`BK11: Mathematics & Statistics`) diarahkan untuk pemodelan proses, basis data, dan analitik bisnis. | ❌ **Nol Kemunculan (0 kali).** Kata "numerik" tidak muncul di 78 halaman. Matematika wajib TI hanya 4: Kalkulus, Matdis, Aljabar Linear, dan Probstat. |
| **Riset Operasi di Core** | ❌ **Bukan Core Wajib Nasional.** Berstatus elektif pendukung (*Decision Science*). | ❌ **Bukan Core Wajib.** |
| **Akar Keilmuan** | Metode numerik klasik (Runge-Kutta, Simpson) adalah domain *Computer Science / Teknik Informatika* atau Teknik Mesin/Fisika. | Riset Operasi berakar dari Teknik Industri dan Sistem Informasi (optimasi keputusan kuantitatif). |

> **Temuan Kunci Regulasi:**  
> Baik APTIKOM SI maupun TI **TIDAK MEWAJIBKAN** Metode Numerik maupun Riset Operasi pada level Core. Menghapus Metode Numerik dari Core K2026 adalah keputusan yang 100% sah dan melegakan mahasiswa dari beban kognitif yang tidak relevan.

---

## 3. PENEMUAN ANOMALI KURIKULER: "CURRICULAR ORPHAN GAP"

Melalui pemindaian terprogram atas Dokumen 043 (*Boundary Guardrails*) dan Dokumen 009D (*CPL Keterampilan Khusus*), Tim Kurikulum menemukan inkonsistensi internal:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ANOMALI CURRICULAR ORPHAN YANG DITEMUKAN                        │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│   DOKUMEN 009D (Indikator CPL KK2.1)      │      DOKUMEN 043 (Baris 1213 - STI-520)    │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ Secara eksplisit menjanjikan bukti fisik: │ Secara tegas memberlakukan larangan:       │
│ "Pipeline Data dengan Pandas/PySpark      │ "❌ OUT-OF-SCOPE: Dilarang arsitektur      │
│  (STI-415 / STI-520)"                     │  cluster Big Data Hadoop/Spark, deployment │
│                                           │  pipeline data streaming."                 │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

**Analisis Realitas di Lapangan Kurikulum:**
1. `STI-415 Data Warehouse & BI` (Sem 4): Menggunakan PostgreSQL dan ETL konvensional (Pentaho/Airflow). Tidak mengajarkan cluster terdistribusi Spark.
2. `STI-520 Data Mining & Visualisasi` (Sem 5): Berfokus pada Scikit-Learn dan Pandas lokal, serta secara resmi **dilarang mengajarkan Hadoop/Spark**.
3. `STI-625 Digital Platform Engineering` (Sem 6): Menggunakan Kafka untuk *asynchronous microservices*, bukan untuk *Big Data Analytics Processing*.
4. `STA-701 MLOps & AI Pipeline` (Sem 7): Berfokus pada siklus hidup model AI (*MLflow/Kubeflow*).

> **Kesimpulan Anomali:**  
> Materi **Big Data Engineering, PySpark, Data Lakehouse, dan Komputasi Terdistribusi** adalah materi yang **dijanjikan di CPL KK2 tetapi dilarang di STI-520 dan tidak memiliki rumah di mata kuliah mana pun**. Sementara itu, Riset Operasi mencatatkan **0 kemunculan** di Dokumen 043.

---

## 4. ANALISIS KOMPARATIF MULTIDIMENSI

### 4.1 Tripartit: Metode Numerik vs. Riset Operasi vs. Big Data Engineering
* **Metode Numerik:** Lemah dan terisolasi. Algoritma aproksimasi diferensial sudah di-abstraksi oleh *deep learning frameworks* (PyTorch/TensorFlow).
* **Riset Operasi:** Sangat baik untuk logistik dan optimasi bisnis, namun tidak menyelesaikan kesenjangan hilangnya materi Big Data/PySpark pada CPL `KK2`.
* **Big Data Engineering:** Menutup kesenjangan kurikuler, merealisasikan janji CPL `KK2`, dan menjadi fondasi utama bagi insinyur AI modern.

### 4.2 Analisis Struktural: Mengapa Wajib Dipisahkan sebagai MK Mandiri?
Uji kelayakan membuktikan bahwa materi Big Data **tidak boleh diintegrasikan** ke dalam MK Core eksisting:
* Jika dimasukkan ke `STI-415` (Sem 4): Memicu *cognitive overload* parah karena mahasiswa baru belajar basis data dasar.
* Jika dimasukkan ke `STI-520` (Sem 5): Melanggar prinsip OBE karena `STI-520` adalah Core Wajib yang juga ditempuh mahasiswa jalur UI/UX dan Cloud/Cyber.
* **Solusi Terbaik:** Dipisahkan sebagai **MK Mandiri `STA-601` (3 SKS +P) di Semester 6** untuk mahasiswa peminatan P1.

### 4.3 Analisis Orientasi: Big Data Analysis vs. Big Data Engineering
* **Ranah Analisis Data Sudah Padat:** Kurikulum SISTEKIN sudah memiliki **6 mata kuliah analitik data** di Core (`FST-408`, `STI-413`, `STI-414`, `STI-415`, `STI-520`, `STI-624`). Menambah "Big Data Analysis" hanya akan memicu redundansi materi.
* **Ranah Rekayasa Data Masih Kosong:** Kemampuan membangun data pipeline terdistribusi skala industri sebelumnya bernilai **0 SKS**.
* **DNA SISTEKIN:** Sebagai sarjana Sistem dan Teknologi Informasi, keunggulan lulusan bertumpu pada **rekayasa infrastruktur dan keandalan sistem (*engineering*)**, bukan sekadar analisis statistik. Di industri, kebutuhan tenaga kerja menunjukkan rasio **1 Data Scientist : 2-3 Data Engineers**.

---

## 5. KEPUTUSAN STRATEGIS & ATRIBUT MATA KULIAH BARU

Berdasarkan seluruh hasil analisis, disahkan atribut baku untuk mata kuliah pengganti:

```
========================================================================================
KODE MATA KULIAH  : STA-601
NAMA MATA KULIAH  : Rekayasa Big Data dan Komputasi Terdistribusi
NAMA INTERNASIONAL: Big Data Engineering & Distributed Systems
BOBOT / STATUS    : 3 SKS (+Praktikum: 100m Teori + 170m Lab + 180m Mandiri) / Elektif P1
SEMESTER          : Semester 6 (Paket Elektif P1 ke-2)
PRASYARAT         : FST-207 Basis Data (+P) dan STI-415 Data Warehouse & BI (+P)
BAHAN KAJIAN      : BK-IS02 Data & Information Management (Sekunder: BK-IS18 Machine Learning)
CPL DIBINA        : P2 (Arsitektur Data Terdistribusi) & KK2 (Pipeline ETL/Streaming Skala Masif)
PROFIL LULUSAN    : PL-1 (Intelligent IS Developer & Data/AI Engineer)
TARGET PEO        : PEO-1 (Professional Practice & Systems Integration), PEO-3 (Lifelong Learning)
KOMPOSISI MATERI  : 70% Big Data Engineering + 30% Analytical Integration (Spark SQL/MLlib)
STACK TEKNOLOGI   : Apache Spark, PySpark, Apache Kafka, Delta Lake, MinIO/S3, Spark MLlib
========================================================================================
```

---

## 6. LOG REVISI & HARMONISASI MULTI-DOKUMEN (*IMPACT ANALYSIS*)

Pembaruan kurikuler ini telah diterapkan secara konsisten pada seluruh dokumen ekosistem kurikulum SISTEKIN 2026:

| No | Berkas Kurikulum | Bagian yang Diperbarui | Dampak & Keterangan |
|:--:|---|---|---|
| 1 | `004_MATRIKS_KETERLACAKAN_OBE.md` | Tabel 4.1 Baris 2 & Matriks BoK | Nama MK disesuaikan, CPL diperbarui (`P2, KK2`), `BK-IS02` bertambah menjadi 6 MK, `BK-IS10` menjadi 4 MK. |
| 2 | `005_STRUKTUR_KURIKULUM.md` | Tabel Sem 6 & Tabel Portofolio Peminatan | Nama `STA-601` diperbarui, prasyarat diselaraskan ke `FST-207` dan `STI-415`. SKS tetap 3 SKS (+P). |
| 3 | `007_FORMULASI_CPMK_DAN_RPS.md` | Bagian 49 (`STA-601`) | Silabus 3-tabel dirancang ulang: 4 CPMK ABCD (C3–C6), 16 pertemuan, dan skema 4x asesmen terstruktur (Tugas 1 [20%], UTS [25%], Tugas 2 [25%], UAS [30%]). |
| 4 | `043_MATRIKS_GUARDRAILS.md` | Guardrails `STI-520` & `STA-601` | *Handoff Anchor* `STI-520` kini mengalirkan data masif ke `STA-601`. Formulasi In-Scope/Out-of-Scope `STA-601` diselaraskan ke Spark/Kafka/Lakehouse. |
| 5 | `024_MATRIKS_EKIVALENSI.md` | Baris `STI-317` K2025 | `STI-317` (Metode Komputasi lama) diubah dari E2 menjadi **E5 (Tanpa Padanan, diakui kredit bebas 2 SKS)** karena materi numerik tidak relevan dengan Big Data Engineering. Neraca K2025 tetap 56 MK / 146 SKS. |
| 6 | `025_REKOMENDASI_ELEKTIF_2027.md` | Pool Elektif Cross-Track | Menambahkan **`STA-603 Riset Operasi dan Optimasi Sistem`** sebagai mata kuliah usulan pilihan bebas 2027. |
| 7 | `030_JUSTIFIKASI_STA601.md` | Header & Status Dokumen | Dokumen 030 diberi label **SUPERSEDED / DIARSIPKAN**, digantikan oleh Dokumen 047, 048, dan 049. |
| 8 | `BUKU_KURIKULUM_FINAL.md` | Bab IV, Bab V, & Bab VIII (§49) | Naskah utuh Buku Kurikulum diperbarui secara menyeluruh mencerminkan nama baru `STA-601`. |
| 9 | `047_ANALISIS_KURIKULER.md` | Naskah Kajian Lengkap | Menyimpan kajian analitis komparatif menyeluruh (Bagian 1 s.d. 7). |
| 10 | `048_KEPUTUSAN_PENGGANTIAN.md` | Surat Keputusan Definitif | Lembar legal keputusan tim pengembang kurikulum. |
| 11 | Portal Navigasi & HTML | `convert_md_to_html.py` & `index.html` | Seluruh 56 file HTML telah diregenerasi dan diselaraskan secara otomatis. |

---

## 7. JAMINAN MUTU, INTEGRITAS DATA & REKOMENDASI IMPLEMENTASI

### 7.1 Kepatuhan Neraca Kurikulum (Zero Discrepancy)
* **Paket Ditempuh Mahasiswa:** Tetap tepat **146 SKS / 55 MK** (memenuhi Permendikbudristek No. 53/2023).
* **Portofolio Mata Kuliah Ditawarkan:** Tetap tepat **182 SKS / 67 MK** (18 MK pilihan peminatan ditawarkan, diambil 6 MK / 18 SKS).
* **Sebaran Semester Mahasiswa Peminatan P1:**
  - Sem 1 (19), Sem 2 (20), Sem 3 (20), Sem 4 (21), Sem 5 (19), Sem 6 (19), Sem 7 (20), Sem 8 (8) = **146 SKS**.

### 7.2 Rekomendasi Kesiapan Laboratorium Komputasi
Untuk mendukung keterlaksanaan praktikum `STA-601 Rekayasa Big Data dan Komputasi Terdistribusi`, laboratorium komputasi FSTI UWG direkomendasikan menyiapkan:
1. **Lingkungan Container Terisolasi:** Penggunaan **Docker Desktop / Docker Compose** pada PC laboratorium untuk menjalankan cluster multi-node lokal (1 container Spark Master + 2 container Spark Worker + 1 container Zookeeper/Kafka + 1 container MinIO).
2. **Spesifikasi Minimum PC Lab:** RAM minimum 16 GB, prosesor multi-core (Intel Core i5 Gen 11 / AMD Ryzen 5 ke atas), dan SSD NVMe minimum 512 GB.
3. **Alternatif Cloud Edukasi:** Pemanfaatan kuota *Google Cloud Platform (GCP) for Education* atau *AWS Academy / Databricks Community Edition* untuk praktikum pengolahan data masif tanpa membebani infrastruktur lokal.

---

*Laporan Resmi ini disahkan dan ditandatangani secara digital oleh Tim Pengembang Kurikulum KPT-OBE SISTEKIN 2026.*  
**Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang**
