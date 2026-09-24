# 047 — ANALISIS KURIKULER: EVALUASI METODE NUMERIK VS. RISET OPERASI VS. REKAYASA BIG DATA PADA MATA KULIAH ELEKTIF STA-601
## Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang

---

### Informasi Dokumen
* **Nomor Dokumen:** 047/KUR-SISTEKIN/2026
* **Status:** Kajian Akademis & Rekomendasi Tim Arsitektur Kurikulum OBE
* **Objek Telaah:** Mata Kuliah Elektif Peminatan 1 (Sem 6, 3 SKS +P) — `STA-601`
* **Dokumen Terkait:** 
  - Dokumen 003 & 009D (Standar 14 CPL & Indikator Kinerja KK2)
  - Dokumen 005 (Struktur Kurikulum 8 Semester)
  - Dokumen 024 (Matriks Ekivalensi K2025 → K2026)
  - Dokumen 025 (Pool Pengembangan Elektif & Cross-Track 2027)
  - Dokumen 030 (Justifikasi Akademis STA-601)
  - Dokumen 043 (Matriks CPL, CPMK, BoK, dan Boundary Guardrails)
* **Standar Rujukan:**
  1. Panduan Kurikulum OBE Program Studi S1 Sistem Informasi APTIKOM Versi 2.0 (2024) — Berbasis IS2020
  2. Panduan Kurikulum OBE Program Studi S1 Teknologi Informasi APTIKOM (2023) — Berbasis IT2017/CC2020
  3. Standar Penjaminan Mutu & Akreditasi LAM INFOKOM

---

## 1. LATAR BELAKANG & RUMUSAN MASALAH

Pada peninjauan kurikulum Program Studi Sistem dan Teknologi Informasi (SISTEKIN) FSTI UWG, muncul pertanyaan kritis akademik terkait mata kuliah matematika komputasi dan pemodelan optimasi:

> 1. *"Bagaimana mandat Panduan OBE APTIKOM untuk rumpun Sistem Informasi dan Teknologi Informasi terkait Metode Numerik? Apakah masih relevan atau lebih baik diganti menjadi Riset Operasi?"*  
> 2. *"Mengingat `STA-601` berstatus Mata Kuliah Pilihan Peminatan 1 (Smart Systems) dan BUKAN Core (Wajib Seluruh Mahasiswa), apakah di ranah Core kita memerlukan salah satunya?"*  
> 3. *"Jika dipertimbangkan sebagai MK Elektif Peminatan 1, apakah Riset Operasi adalah pilihan terbaik, ataukah ada kompetensi industri krusial yang saat ini justru 'terlewatkan' (the missing piece) dalam arsitektur kurikulum kita?"*

Dokumen ini menyajikan hasil audit forensik menyeluruh terhadap regulasi APTIKOM, struktur SKS Core vs. Elektif, pemindaian teks pada Dokumen 043 (*Boundary Guardrails*), dan pembuktian ketercapaian CPL pada Dokumen 009D.

---

## 2. AUDIT MANDAT STANDAR APTIKOM PADA RANAH CORE (WAJIB)

### 2.1 Tinjauan Panduan APTIKOM SI v2.0 (IS2020)
* **Bahan Kajian Matematika:** Termaktub dalam `BK11: Mathematics and Statistics` (atau `BK-IS10: Applied Mathematics and Logic`). Deskripsi resmi: *"Membangun dasar pengetahuan matematika dan statistik yang diperlukan untuk analisis data, pemodelan sistem informasi, dan pengambilan keputusan organisasi."*
* **Mata Kuliah Wajib Diturunkan:** *Computational Thinking*, *Matematika Diskrit*, serta *Statistika & Probabilitas*.
* **Status Metode Numerik:** **TIDAK PERNAH MENJADI MATA KULIAH WAJIB INTI (CORE).** Kurikulum SI berorientasi pada pemodelan enterprise, basis data, rekayasa platform, dan tata kelola TI, bukan komputasi persamaan diferensial fisik.
* **Status Riset Operasi:** Bukan mata kuliah wajib inti nasional, melainkan tergolong **Mata Kuliah Pendukung / Pilihan** dalam ranah *Decision Science*, *Quantitative Methods*, atau *Business Analytics*.

### 2.2 Tinjauan Panduan APTIKOM TI 2023 (IT2017/CC2020)
* **Daftar 15 Mata Kuliah Wajib Inti Penciri Utama TI (Halaman 43, 45, 48):**  
  Rumpun TI hanya mewajibkan 4 pilar matematika dasar:
  1. *Matematika Diskrit & Logika*
  2. *Kalkulus*
  3. *Aljabar Linear Terapan & Matriks*
  4. *Probabilitas & Statistika*
* **Status Metode Numerik:** Kata *"numerik"* muncul **0 KALI (NOL KEMUNCULAN)** di seluruh 78 halaman naskah panduan resmi TI 2023. Metode Numerik klasik (Runge-Kutta, Simpson, Bisection) secara historis adalah ciri khas Program Studi **Teknik Informatika / Ilmu Komputer (Computer Science)**, bukan Teknologi Informasi.
* **Status Riset Operasi:** **TIDAK ADA** di daftar 15 MK Wajib Penciri TI.

### 2.3 Mengapa Kurikulum 2025 Memiliki Metode Numerik di Core Wajib?
Pada Kurikulum 2025, terdapat mata kuliah `STI-317 Metode Komputasi dan Numerik` (2 SKS, Semester 3, Wajib). Hal ini terjadi karena:
1. **Struktur K2025 yang Kaku (*Lock-step*):** Seluruh 56 MK (146 SKS) berstatus Wajib tanpa peminatan (kolom pilihan = 0 SKS).
2. **Warisan Prodi Informatika:** Mata kuliah dari kurikulum lama Teknik Informatika diserap tanpa filter relevansi profil lulusan STI.
3. **Beban yang Salah Sasaran:** Mahasiswa yang berminat pada UI/UX, Cloud, atau Keamanan Siber dipaksa menghitung galat floating-point dan aproksimasi kalkulator yang tidak pernah mereka pakai di dunia kerja.

> **Kesimpulan Tingkat Core:**  
> Keputusan Kurikulum 2026 untuk **MENGELUARKAN Metode Numerik dari CORE Wajib adalah 100% BENAR dan SAH secara standar APTIKOM**. Di tingkat Core, SISTEKIN **TIDAK PERLU** mewajibkan Metode Numerik maupun Riset Operasi. Materi logika optimasi esensial sudah diserap oleh `STI-204` (Teori Graf), `STI-205` (Aljabar Linear), `STI-310` (Penjadwalan OS), `STI-312` (Antrean Jaringan), dan `STI-413` (Machine Learning).

---

## 3. AUDIT FORENSIK DOKUMEN 043 & 009D: PENEMUAN "CURRICULAR ORPHAN"

Ketika kita menganalisis posisi mata kuliah elektif `STA-601` (Semester 6, Peminatan 1: Integrated Smart Systems), dilakukan pemindaian kata kunci terprogram terhadap seluruh dokumen silabus dan demarkasi materi (`043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md`). Hasilnya mengungkap **fakta kurikuler yang sangat mengejutkan**:

### 3.1 Bukti Larangan pada Dokumen 043 (Baris 1213)
Pada mata kuliah `STI-520 Data Mining & Visualisasi Data` (Semester 5), tertulis pagar pembatas resmi:
```markdown
#### STI-520 — Data Mining & Visualisasi Data
* 🟢 IN-SCOPE (Wajib Diajarkan): Eksplorasi Data Lanjut (EDA), Association Rule Mining (Apriori, FP-Growth), 
  Advanced Clustering (DBSCAN), Anomaly Detection, Prinsip Visualisasi Informasi Kognitif, Storytelling with Data.
* ❌ OUT-OF-SCOPE (Dilarang Diajarkan): ❌ Dilarang arsitektur cluster Big Data Hadoop/Spark, 
  training neural networks computer vision, deployment pipeline data streaming.
* 🔄 HANDOFF ANCHOR: Menguasai penemuan wawasan data; menyerahkan sistem pendukung keputusan eksekutif ke STA-501.
```
> **Temuan Kritis 1:**  
> Dosen pengampu `STI-520` **dilarang keras** mengajarkan *Arsitektur Cluster Big Data Hadoop/Spark* dan *Deployment Pipeline Data Streaming*. Tujuannya agar materi terfokus pada analitik lokal Python/Pandas. Namun, materi cluster & streaming tersebut **belum dialihkan ke mata kuliah mana pun!**

### 3.2 Bukti Janji CPL pada Dokumen 009D (Baris 122)
Pada Dokumen `009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md`, Capaian Pembelajaran Lulusan **`KK2` (Rekayasa Data, ETL, MLOps & BI)** menetapkan:
```markdown
| No | Indikator Kinerja KK2 | Bukti Portofolio / Asesmen |
|:--:|---|---|
| 1  | Mampu membangun pipeline akuisisi, praproses, dan transformasi data (ETL/ELT). | Pipeline Data dengan Pandas/PySpark (STI-415 / STI-520). |
```
> **Temuan Kritis 2:**  
> Dokumen CPL menjanjikan bukti portofolio mahasiswa berupa **`Pipeline Data dengan PySpark`**. Namun kenyataannya:
> - `STI-415` (Data Warehouse) hanya mengajarkan ETL relasional konvensional (Airflow/Pentaho).
> - `STI-520` (Data Mining) **melarang** Hadoop/Spark.
> - `STI-625` (Digital Platform) memakai Kafka untuk arsitektur *microservices*, bukan pemrosesan analitik Big Data.
> - `STA-701` (MLOps) fokus pada deployment model AI (*MLflow/Kubeflow*).

### 3.3 Temuan Status Riset Operasi pada Dokumen 043
* Hasil pemindaian kata kunci `Riset Operasi` dan `Operations Research` pada Dokumen 043 menghasilkan **0 KEMUNCULAN (NOL)**.
* Artinya, materi Riset Operasi saat ini memang belum pernah dirancang dalam silabus maupun sistem asesmen SISTEKIN 2026.

---

## 4. MATRIKS KOMPARASI TRIPARTIT KANDIDAT MATA KULIAH ELEKTIF STA-601

Berdasarkan temuan di atas, terdapat 3 alternatif arah pengembangan mata kuliah elektif `STA-601` di Semester 6 (Peminatan 1: Integrated Smart Systems):

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                     KOMPARASI 3 KANDIDAT MATA KULIAH ELEKTIF STA-601 (SEM 6, 3 SKS +P)           │
├──────────────────────┬─────────────────────────────┬───────────────────────────┬─────────────────┤
│ Parameter Evaluasi   │ Opsi 1: Status Quo          │ Opsi 2: Riset Operasi &   │ Opsi 3: Rekayasa│
│                      │ Computational Methods & Num │ Optimasi Sistem           │ Big Data & Dist.│
├──────────────────────┼─────────────────────────────┼───────────────────────────┼─────────────────┤
│ Nomenklatur          │ Computational Methods and   │ Riset Operasi dan         │ Rekayasa Big    │
│                      │ Numerics (+P)               │ Optimasi Sistem (+P)      │ Data dan Komp.  │
│                      │                             │                           │ Terdistribusi+P │
├──────────────────────┼─────────────────────────────┼───────────────────────────┼─────────────────┤
│ Fokus Keilmuan       │ Analisis galat komputasi,   │ Pemodelan keputusan,      │ Infrastruktur   │
│                      │ aproksimasi fungsi kontinu, │ alokasi sumber daya,      │ data skala besar│
│                      │ persamaan diferensial.      │ minimasi biaya operasional│ pipeline stream.│
├──────────────────────┼─────────────────────────────┼───────────────────────────┼─────────────────┤
│ Relevansi terhadap   │ Rendah — Model AI modern    │ Sedang s.d. Tinggi —      │ SANGAT TINGGI — │
│ Profil PL-1 (Data &  │ sudah menggunakan pustaka   │ Bagus untuk Prescriptive  │ 80% kerja nyata │
│ AI Engineer)         │ otomatis (frameworks).      │ Analytics & Logistik.     │ Data/AI Engineer│
│                      │                             │                           │ di industri.    │
├──────────────────────┼─────────────────────────────┼───────────────────────────┼─────────────────┤
│ Menyelesaikan Gap    │ ❌ Tidak menyelesaikan      │ ❌ Tidak menyelesaikan    │ ✅ MENYELESAIKAN│
│ Kurikuler (Orphan)?  │ larangan di STI-520         │ larangan di STI-520       │ GAP BoK & CPL   │
│                      │ maupun janji CPL KK2.       │ maupun janji CPL KK2.     │ SECARA PARIPURNA│
├──────────────────────┼─────────────────────────────┼───────────────────────────┼─────────────────┤
│ Pustaka Lab / Stack  │ Python, NumPy, SciPy.       │ Google OR-Tools, PuLP,    │ Apache Spark,   │
│ Teknologi Praktikum  │                             │ SciPy Optimize, NetworkX. │ PySpark, Kafka, │
│                      │                             │                           │ Delta Lake/S3.  │
├──────────────────────┼─────────────────────────────┼───────────────────────────┼─────────────────┤
│ Keterhubungan Alur   │ Terisolasi (terputus dari   │ Berpasangan dengan DSS    │ Jembatan emas:  │
│ Semester (Pipeline)  │ alur praktis AI industri).  │ STA-501 (MCDM vs LP/VRP). │ STI-520 (Mining)│
│                      │                             │                           │ ➔ STA-601 (Data)│
│                      │                             │                           │ ➔ STA-701 (MLOps│
└──────────────────────┴─────────────────────────────┴───────────────────────────┴─────────────────┘
```

---

## 5. ANALISIS STRUKTURAL: DIPISAHKAN SEBAGAI MK MANDIRI ATAU DIINTEGRASIKAN KE MK LAIN?

Sebuah pertimbangan krusial dalam desain kurikulum OBE adalah efisiensi kurikulum:  
> *"Apakah materi Rekayasa Big Data dan Komputasi Terdistribusi perlu dipisahkan menjadi mata kuliah mandiri (3 SKS di STA-601), ataukah sebaiknya diintegrasikan (ditumpangkan) ke dalam mata kuliah data yang sudah ada?"*

Berikut adalah hasil uji kelayakan komparatif terhadap kedua skenario:

### 5.1 Uji Skenario A: Jika Diintegrasikan ke MK Lain Eksisting
Jika materi Big Data dipaksakan masuk ke mata kuliah eksisting, terdapat 3 kandidat MK penampung:

| Kandidat MK Penampung | Kondisi Silabus Saat Ini (Dokumen 043) | Dampak & Risiko Akademis Jika Diintegrasikan |
|---|---|---|
| **`STI-415` Data Warehouse & Business Intelligence** (Sem 4, Core) | Fokus pada *Kimball Dimensional Modeling* (Star/Snowflake Schema), ETL relasional (Pentaho/Airflow), dan Dashboard PowerBI/Metabase. | ⚠️ **Cognitive Overload Parah di Semester 4.**<br/>Mahasiswa baru menuntaskan Basis Data dasar (`FST-207`) di Semester 2. Memaksa mahasiswa Semester 4 mengelola cluster terdistribusi Hadoop/Spark dan streaming Kafka akan menghancurkan pemahaman fondasi *dimensional modeling* dan BI bisnis karena waktu habis untuk *troubleshooting setup* cluster. |
| **`STI-520` Data Mining & Visualisasi Data** (Sem 5, Core) | Fokus pada *Exploratory Data Analysis (EDA)*, aturan asosiasi (Apriori/FP-Growth), klastering (DBSCAN), deteksi anomali, dan visual storytelling. | ⚠️ **Salah Sasaran Profil & Pelanggaran Prinsip OBE.**<br/>`STI-520` adalah mata kuliah **Core Wajib bagi seluruh mahasiswa** (termasuk jalur UI/UX dan Cloud/Cyber). Memaksa calon desainer UI/UX mengonfigurasi cluster worker Apache Spark terdistribusi sangat melanggar relevansi profil. Selain itu, silabus 16 pertemuan algoritma penambangan data sudah sangat padat. |
| **`STA-701` MLOps and AI Pipeline** (Sem 7, P1) | Fokus pada *Experiment Tracking (MLflow)*, *Containerization*, *Model Registry*, dan *Monitoring Model Drift*. | ⚠️ **Salah Tahapan Siklus (*Wrong Lifecycle Stage*).**<br/>MLOps adalah rekayasa siklus hidup **model AI di tahap produksi** (setelah data siap). Jika mahasiswa baru mempelajari cara mengolah Big Data terdistribusi di Semester 7 bersamaan dengan MLOps, mereka tidak memiliki landasan data yang matang untuk dilatih menjadi model AI skala besar. |

> **Kesimpulan Uji Integrasi:**  
> Mengintegrasikan Big Data ke dalam mata kuliah eksisting akan memicu **"obesitas kurikulum"**, merusak fokus kompetensi dasar MK induk, dan salah sasaran profil di level Core.

### 5.2 Uji Skenario B: Jika Dipisahkan Menjadi MK Mandiri (`STA-601`, 3 SKS +P di Sem 6)
Pemisahan menjadi mata kuliah mandiri di Semester 6 memiliki keunggulan arsitektural yang mutlak:

1. **Bobot Materi Memang Layak 1 MK Penuh (3 SKS +Praktikum):**  
   Materi arsitektur komputasi terdistribusi (HDFS, S3), pemrograman PySpark (DataFrame API, Catalyst Optimizer), *Data Lakehouse* (Delta Lake), dan *stream processing* (Kafka) membutuhkan waktu praktikum lab intensif (170 menit lab per pekan) yang tidak mungkin dirangkum hanya dalam 2–3 pertemuan kuliah lain.
2. **Penerapan Prinsip *Targeted Learning* (Peminatan P1):**  
   Hanya mahasiswa yang memilih peminatan **Integrated Smart Systems & Data/AI Engineer (PL-1)** yang menempuh mata kuliah ini. Mahasiswa jalur Cloud/Cyber (`PL-2`) dan UI/UX (`PL-3`) tidak terbebani di tingkat Core.
3. **Ketersediaan Slot Jam Tanpa Menambah SKS Kelulusan:**  
   Di Semester 6, prodi sudah mengalokasikan slot **`STA-601` berbobot 3 SKS (+P)** yang semula diisi oleh *Metode Numerik*. Mengganti Metode Numerik dengan Big Data Engineering memanfaatkan slot yang sudah ada secara tepat guna, **tanpa mengubah neraca 146 SKS paket kelulusan**.

### 5.3 Model Rekomendasi: Sinergi Berjenjang (*Tiered Pipeline Architecture*)
Rekomendasi terbaik adalah menerapkan **alur data pipeline berjenjang (*pipeline architecture*)** yang membagi peran secara elegan dari Semester 4 hingga Semester 7:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ALUR DATA & AI PIPELINE SISTEKIN 2026                           │
└────────────────────────────────────────────────────────────────────────────────────────┘

  [Semester 4 - CORE STI]
  STI-415 Data Warehouse & Business Intelligence (3 SKS, +P)
  ➔ Peran: Fondasi Data Enterprise, Skema Bintang/Salju Relasional (Kimball), Batch ETL.
      │
      ▼
  [Semester 5 - CORE STI]
  STI-520 Data Mining & Visualisasi Data (3 SKS)
  ➔ Peran: Analisis Algoritmik Data Tabular Lokal (Pandas, Scikit-Learn, Visual Storytelling).
      │
      ▼
  [Semester 6 - PEMINATAN P1 (MANDIRI)] 🌟
  STA-601 Rekayasa Big Data & Komputasi Terdistribusi (3 SKS, +P)
  ➔ Peran: Skalabilitas Data Masif (Apache Spark, PySpark, Data Lakehouse, Kafka Streaming).
      │
      ▼
  [Semester 7 - PEMINATAN P1 (MANDIRI)]
  STA-701 MLOps and AI Pipeline (3 SKS, +P)
  ➔ Peran: Deployment & Automasi Siklus Hidup Model AI Produksi dari Pipeline Big Data.
```

---

## 6. ANALISIS KOMPARATIF: BIG DATA ANALYSIS VS. BIG DATA ENGINEERING UNTUK PRODI SISTEKIN

Sebuah pertanyaan strategis berikutnya adalah:  
> *"Jika mata kuliah ini diarahkan ke ranah data masif, apakah lebih tepat menggunakan orientasi **Big Data Analysis (Analytics)** atau **Big Data Engineering (Rekayasa Data)** bagi Program Studi SISTEKIN?"*

Berikut adalah analisis komparatif multidimensi yang mendasari penentuan orientasi mata kuliah:

### 6.1 Pembeda Fundamental: Analysis vs. Engineering di Dunia Industri

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        PERBEDAAN PERAN DI INDUSTRI TEKNOLOGI                           │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│         BIG DATA ANALYSIS (ANALYTICS)     │            BIG DATA ENGINEERING            │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ • Pertanyaan Kunci: "Wawasan bisnis apa   │ • Pertanyaan Kunci: "Bagaimana cara        │
│   yang tersembunyi di balik data masif?"  │   menyedot, membersihkan, dan mengalirkan  │
│                                           │   data 10 TB/detik agar AI bisa jalan?"    │
│ • Fokus Utama: Statistik, visualisasi,    │ • Fokus Utama: Arsitektur cluster, data    │
│   pola perilaku pengguna, evaluasi metriks│   pipelines, skalabilitas, latensi,        │
│   prediksi, pembuatan dashboard eksekutif.│   throughput, toleransi kegagalan (fault). │
│ • Perangkat Lunak: Python (Pandas/Seaborn)│ • Perangkat Lunak: Apache Spark, PySpark,  │
│   Tableau, PowerBI, Google Looker Studio. │   Apache Kafka, Delta Lakehouse, S3/MinIO. │
│ • Profil Pengguna: Data Analyst, Business │ • Profil Pengguna: Data Engineer, Big Data │
│   Intelligence Analyst, Data Scientist.   │   Architect, Machine Learning Engineer.    │
│ • DNA Rumpun Asal: Sains Data, Statistika,│ • DNA Rumpun Asal: TEKNOLOGI INFORMASI &   │
│   Manajemen Bisnis / Sistem Informasi.    │   SISTEM INFORMASI (SISTEKIN).             │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

### 6.2 Audit Redundansi Kurikulum: Analisis Data Sudah "Sangat Padat" di Core
Jika prodi memilih orientasi **Big Data Analysis**, mata kuliah ini akan mengalami **tumpang tindih (*curricular redundancy*) parah** dengan mata kuliah Core yang sudah ada. 

Kurikulum SISTEKIN 2026 saat ini telah memiliki **6 mata kuliah Core yang secara mendalam mengajarkan analisis data**:
1. `FST-408` Statistika & Probabilitas (Sem 4) $\rightarrow$ Analisis inferensial, uji hipotesis, dan distribusi probabilitas.
2. `STI-413` Machine Learning (Sem 4, Core) $\rightarrow$ Analisis prediktif, regresi, klasifikasi, evaluasi model.
3. `STI-414` NLP & Text Mining (Sem 4, Core) $\rightarrow$ Analisis data teks tak terstruktur dan sentimen.
4. `STI-415` Data Warehouse & BI (Sem 4, Core) $\rightarrow$ Analisis dimensi bisnis, agregasi data, dan visualisasi dashboard.
5. `STI-520` Data Mining & Visualisasi Data (Sem 5, Core) $\rightarrow$ Penemuan pola, klastering DBSCAN, aturan asosiasi, dan *visual storytelling*.
6. `STI-624` Deep Learning & Neural Networks (Sem 6, Core) $\rightarrow$ Analisis pola citra dan runtun waktu non-linier kompleks.

> ⚠️ **Risiko Kurikuler:**  
> Jika `STA-601` dijadikan *Big Data Analysis*, mahasiswa hanya akan mengulang materi Data Mining (`STI-520`) dan Machine Learning (`STI-413`), hanya saja ukuran dataset CSV-nya diganti menjadi lebih besar. Ini adalah pemborosan 3 SKS yang tidak menambah daya saing lulusan.

### 6.3 Di Mana Kekosongan Sebenarnya? Kesenjangan Mutlak Ada pada "ENGINEERING"
Sebaliknya, keahlian **membangun infrastruktur rekayasa data skala industri** saat ini berstatus **0 SKS (KOSONG SAMA SEKALI)** di seluruh kurikulum SISTEKIN:
* Mahasiswa tahu cara melatih algoritma model AI (diajarkan di `STI-413` dan `STI-624`).
* **TETAPI mahasiswa TIDAK TAHU:**
  * Bagaimana cara mengalirkan 50.000 transaksi/detik dari sensor IoT (`STI-521`) dan aplikasi web tanpa server tumbang?
  * Bagaimana cara membagi beban data ke puluhan node worker komputasi terdistribusi menggunakan **Apache Spark**?
  * Bagaimana mengonfigurasi partisi topik dan toleransi kegagalan pada message streaming **Apache Kafka**?
  * Bagaimana arsitektur penyimpanan data modern berbasis **Data Lakehouse (Delta Lake / Parquet)** yang mendukung transaksi ACID?

### 6.4 Keselarasan DNA Prodi SISTEKIN & Positioning "Integrator AI Nyata"
1. **Marwah Rekayasa (*Engineering*) bagi Lulusan Sarjana Komputer:**  
   Prodi bernama **Sistem dan Teknologi Informasi (SISTEKIN)** di bawah Fakultas Sains dan **Teknologi Informasi**. Kata kunci utamanya adalah **SISTEM** (*arsitektur, integrasi komponen*) dan **TEKNOLOGI** (*infrastruktur, keandalan, performa komputasi*).
2. **Kebutuhan Nyata Industri (Rasio Kebutuhan Tim Data):**  
   Di industri teknologi (FinTech, E-Commerce, Telekomunikasi, Perbankan), rasio kebutuhan tenaga kerja adalah:
   $$\text{1 Data Scientist / AI Researcher} : \mathbf{2\text{ s.d. }3\text{ Data Engineers}}$$
   Perusahaan jauh lebih sulit merekrut **Data Engineer** karena keahlian arsitektur data terdistribusi jarang diajarkan secara komprehensif di jenjang S1.
3. **Penyempurnaan Formulasi CPL `KK2`:**  
   CPL `KK2` secara tegas berbunyi: *"Mampu merancang dan **merekayasa arsitektur data**, pipeline ETL/ELT terdistribusi, serta MLOps..."* Fokusnya adalah **REKAYASA SISTEM DATA**, bukan sekadar analisis deskriptif.

### 6.5 Rekomendasi Proporsi Muatan Silabus STA-601 (70% Engineering + 30% Analytical Integration)
Meskipun berorientasi rekayasa (*engineering*), mata kuliah ini tetap mengintegrasikan aspek analitik untuk membuktikan bahwa infrastruktur data yang dibangun berfungsi sempurna melayani model kecerdasan artifisial:
* **70% Data Engineering (Fondasi Utama):**
  - Arsitektur Cluster Komputasi Terdistribusi (Master-Worker, HDFS, Object Storage S3/MinIO).
  - Pemrosesan Terdistribusi Skala Besar dengan **Apache Spark & PySpark**.
  - Modern Data Lakehouse Architecture (ACID Transactions, Delta Lake, Apache Iceberg).
  - Ingesti Data Real-Time Streaming menggunakan **Apache Kafka**.
* **30% Analytical Integration (Pembuktian Manfaat):**
  - Menjalankan kueri analitik SQL masif terdistribusi (**Spark SQL**).
  - Menjalankan algoritma machine learning terdistribusi (**Spark MLlib**) langsung di atas cluster data untuk membuktikan bahwa data pipeline siap memasok data ke model AI.

---

## 7. KESIMPULAN & REKOMENDASI ARSITEKTUR KURIKULUM

### 7.1 Kesimpulan Utama
1. **Pada Tingkat CORE (Wajib):** Baik Metode Numerik maupun Riset Operasi **TIDAK PERLU** diwajibkan. Fondasi matematika wajib 10 SKS (`STI-102`, `STI-204`, `STI-205`, `FST-408`) telah 100% memenuhi standar APTIKOM SI dan TI tanpa membebani mahasiswa jalur non-data.
2. **Kelemahan Opsi Riset Operasi:** Riset Operasi adalah mata kuliah yang sangat baik, namun orientasinya lebih dekat ke *Prescriptive Decision Analytics / Manajemen Operasi*. Riset Operasi tidak menyelesaikan kesenjangan hilangnya materi Big Data/PySpark yang sudah dijanjikan di CPL `KK2`.
3. **Kesenjangan Terbesar (*The True Missing Piece*):** Profil lulusan **PL-1 (Intelligent IS Developer & Data/AI Engineer)** saat ini memiliki mata rantai yang terputus antara *Machine Learning* lokal (`STI-413`/`STI-520`) menuju *MLOps* skala enterprise (`STA-701`). Mahasiswa belum dibekali kemampuan mengolah data skala besar (terabytes/streaming).
4. **Keputusan Pemisahan vs Integrasi:** Big Data dan Komputasi Terdistribusi **WAJIB DIPISAHKAN sebagai MK Mandiri 3 SKS (+P)** di `STA-601` agar tidak menimbulkan *cognitive overload* dan salah sasaran di tingkat Core.
5. **Keputusan Orientasi (Analysis vs Engineering):** Mata kuliah ini **MUTLAK BERORIENTASI BIG DATA ENGINEERING**, karena ranah analisis data sudah sangat padat dibina oleh 6 mata kuliah Core eksisting.

### 7.2 Rekomendasi Tindak Lanjut

#### Rekomendasi 1: Tetapkan `STA-601` Menjadi Rekayasa Big Data
Mengubah identitas mata kuliah elektif `STA-601` menjadi:
* **Kode & Nama:** `STA-601 Rekayasa Big Data dan Komputasi Terdistribusi` (*Big Data Engineering & Distributed Systems*)
* **Bobot & Semester:** 3 SKS (+Praktikum: 100m Teori + 170m Lab) — Semester 6
* **Prasyarat:** `STI-207 Basis Data`, `STI-415 Data Warehouse & BI`
* **Materi Pokok:** 
  - Arsitektur Data Terdistribusi & Distributed File Systems (HDFS, Object Storage S3/MinIO)
  - NoSQL Database Tingkat Lanjut (Document & Wide-Column Stores)
  - Pemrosesan Data Terdistribusi menggunakan **Apache Spark & PySpark**
  - *Data Ingestion & Event Streaming* menggunakan **Apache Kafka**
  - Konsep Modern Data Lakehouse (Delta Lake, Apache Iceberg, Parquet)
  - Integrasi Analitik & Machine Learning Terdistribusi (**Spark SQL & Spark MLlib**)
  - Orkestrasi Data Pipeline Terdistribusi

#### Rekomendasi 2: Harmonisasi Boundary Guardrails Dokumen 043
Memperbarui baris *Out-of-Scope* dan *Handoff Anchor* pada `STI-520 Data Mining & Visualisasi Data`:
```diff
  #### STI-520 — Data Mining & Visualisasi Data
  * 🟢 IN-SCOPE: Eksplorasi Data Lanjut (EDA), Association Rule Mining, Advanced Clustering, Anomaly Detection.
- * ❌ OUT-OF-SCOPE: Dilarang arsitektur cluster Big Data Hadoop/Spark, deployment pipeline data streaming.
- * 🔄 HANDOFF ANCHOR: Menguasai wawasan data; menyerahkan sistem pendukung keputusan ke STA-501.
+ * ❌ OUT-OF-SCOPE: Dilarang arsitektur cluster Big Data terdistribusi (itu ranah STA-601); 
+   deployment streaming event-driven platform (itu ranah STI-625).
+ * 🔄 HANDOFF ANCHOR: Menguasai analisis data tabular lokal; menyerahkan pemrosesan data skala besar 
+   dan pipeline terdistribusi ke STA-601 (Big Data Engineering).
```

#### Rekomendasi 3: Penempatan Riset Operasi pada Pool Elektif Cross-Track (Dokumen 025)
Topik **Riset Operasi & Sains Manajemen** tidak dibuang, melainkan direkomendasikan masuk ke dalam **Pool Mata Kuliah Pilihan Bebas / Lintas Minat (*Cross-Track Electives*) 2027** pada Dokumen 025. Mata kuliah ini dapat dipilih oleh mahasiswa yang tertarik pada optimasi rantai pasok digital (*Smart Supply Chain*), logistik cerdas, dan pemodelan bisnis *Technopreneurship* (`PL-4`).

---

*Disahkan sebagai Dokumen Analisis Resmi 047 — Tim Pengembang Kurikulum OBE SISTEKIN 2026*  
**Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang**


