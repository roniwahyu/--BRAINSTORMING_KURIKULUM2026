# 022 — AUDIT KRITIS BEBAN BOK, TUMPANG TINDIH SUBSTANSI & KELEMAHAN KURIKULUM SISTEKIN 2026
## Analisis Stres-Uji Pedagogis, Redundansi Terselubung & Mitigasi Operasional Kurikulum OBE

**Tanggal:** 18 Agustus 2026  
**Peran:** Arsitek Kurikulum & Asesor LAM INFOKOM / IABEE  
**Sumber Rujukan:** Dokumen 006–021 `KURIKULUM2026_ZCODE`  
**Fungsi Dokumen:** Dokumen diagnosis kritis, mitigasi risiko implementasi, dan pedoman operasional perumusan RPS, CPMK, serta rubrik asesmen OBE.

---

## 1. EKSEKUTIF SUMMARY: 4 AREA TEMUAN AUDIT

Setelah seluruh keputusan struktur makro (VMTS, PL/PEO, 14 CPL, 19 BoK IS2020, 27 BoK IT2017, dan 3 Peminatan Seimbang @ 6 MK / 18 SKS) berhasil diselaraskan di Dokumen [020] dan [021], audit stres-uji (*stress-testing audit*) menemukan 4 area risiko yang wajib dimitigasi sebelum masuk ke perumusan RPS/CPMK mikro:

1. **Konsentrasi BoK Berlebih (*Over-Saturation*):** Dominasi `SI-BK18` (AI / 11 MK), `SI-BK07` (Programming / 11 MK), dan kepadatan `SI-BK11` (Matematika / 15 SKS).
2. **Tumpang Tindih Substansi Terselubung (*Subtle Overlaps*):** Klaster Data di Semester 5 (DW-BI vs Data Mining), Triple Governance di Peminatan P2, dan batas irisan Integrasi AI vs Platform Engineering.
3. **Anomali Beban Semester (*Semester Load Imbalance*):** **"Semester 5 Overload Trap"** dengan 5 MK Wajib Praktikum Laboratorium sekaligus (total 6–7 MK praktikum dalam 1 semester).
4. **Kelayakan Operasional & Kesiapan Sumber Daya:** Kebutuhan komputasi GPU, kit perangkat keras IoT, dan sertifikasi keahlian dosen pengampu.

---

## 2. AUDIT KONSENTRASI BoK BERLEBIH (*OVER-SATURATED BoK*)

```
Visualisasi Konsentrasi BoK dalam Kurikulum 2026:
● SI-BK18 (Emerging Tech / AI)   : 11 MK (Sangat Padat)  ███████████
● SI-BK07 (Programming / App Dev): 11 MK (Sangat Padat)  ███████████
● SI-BK11 (Matematika & Statistik):  5 MK (15 SKS Total)   █████
● SI-BK06 (Governance & Strategy):  5 MK (Konsentrasi P2) █████
```

| Area BoK | Jumlah MK / SKS | Diagnosa Kelemahan & Risiko | Rekomendasi Mitigasi RPS |
|---|:---:|---|---|
| **`SI-BK11` (Matematika Komputasi)** | **5 MK (15 SKS)**<br>*(Kalkulus, Logika, Diskrit, Aljabar, Probstat)* | **Terlalu padat untuk PTS.** Mahasiswa SISTEKIN dibebani 15 SKS matematika murni di Semester 1–4. Berisiko menurunkan tingkat kelulusan (*passing rate*) dan menjadi *bottleneck* sebelum mahasiswa masuk ke MK AI terapan. | **Gunakan pendekatan Computational Mathematics:** Silabus Kalkulus & Aljabar Linear wajib menggunakan visualisasi Python/NumPy, bukan kalkulasi rumus manual abstrak, agar langsung dirasakan relevansinya dengan machine learning. |
| **`SI-BK18` (AI & Emerging Tech)** | **11 MK** | Dominasi AI sangat masif di MK Wajib dan P1. Risiko: Jika dosen kurang siap, materi berpotensi redundan hanya membahas konsep ML dasar yang diulang-ulang. | **Wajibkan pemisahan domain tegas pada RPS:**<br>- STI-401 = Algoritma Klasik (Regression/Tree/SVM)<br>- STI-501 = Deep Neural (CNN/Transformer)<br>- STI-601 = AI Deployment & API Serving<br>- STA-01 s.d 06 = Sub-domain spesifik (Agent, MLOps, LLM). |
| **`SI-BK07` (Pemrograman Aplikasi)** | **11 MK** | FST-102, FST-203, Web FE, Web BE, Mobile, Integrasi AI, Platform Eng, MLOps, DevOps, SaaS, Vertikal App. Beban tugas *coding* tanpa henti dari Sem 1 s.d 7. | Terapkan **Integrated Project Assignment**: Tugas besar pemrograman dihubungkan antar-MK dalam satu semester agar mahasiswa tidak membuat 3–4 aplikasi berbeda. |

---

## 3. TUMPANG TINDIH SUBSTANSI TERSELUBUNG (*SUBTLE OVERLAPS*)

### 3.1 Klaster Analitik Data: Pemisahan Berjenjang *DW-BI (Sem 4) vs Data Mining (Sem 5)* — ✅ TERSELESAIKAN
* **Solusi Pertukaran:** `STI-402 DW-BI` (3 SKS, +P) dipindahkan ke **Semester 4**, sedangkan `STI-506 Manpro TI` (3 SKS) dipindahkan ke **Semester 5**.
* **Keunggulan Pedagogis:** Menghilangkan tabrakan ETL/Visualisasi di semester yang sama dan menciptakan alur belajar berjenjang yang sempurna:
  $$\text{Basis Data (Sem 2)} \longrightarrow \text{Data Warehouse \& BI (Sem 4)} \longrightarrow \text{Data Mining \& Visualization (Sem 5)}$$
* **Garis Batas Silabus yang Ditetapkan:**
  * **STI-402 DW-BI (Sem 4):** Fokus murni pada **Enterprise Data Infrastructure**: *Dimensional Modeling, Star/Snowflake Schema, Data Mart, OLAP Cube, ETL Pipeline, Data Governance*.
  * **STI-503 Data Mining (Sem 5):** Fokus murni pada **Discovery Analytics**: *Pattern Discovery, Clustering (K-Means/DBSCAN), Association Rules (Apriori/FP-Growth), Anomaly Detection, Non-Deep ML*.

### 3.2 Klaster Peminatan P2: *The Triple Governance Trap*
* **Masalah:** `STB-03 Cyber Risk`, `STB-04 COBIT Governance`, dan `STB-05 ITIL Service Management`.
* **Potensi Redundansi:** Jika mahasiswa P2 mengambil ketiganya, mereka menempuh **9 SKS kuliah tata kelola berbasis dokumen/audit**, yang bertolak belakang dengan profil teknis *"Cloud Infrastructure & Cybersecurity"*.
* **Garis Batas Silabus & Arahan Akademik:**
  * Mahasiswa P2 **diarahkan** mengambil kombinasi seimbang: 2 MK Teknis (`STB-01 Forensik` + `STB-02 DevOps`) + 1 MK Arsitektur (`STB-06 TOGAF`) + maksimal 1 MK Tata Kelola (`STB-03` atau `STB-04`).
  * RPS masing-masing harus tegas: STB-03 (ISO 27001/31000 Risk), STB-04 (COBIT 2019 IT Alignment), STB-05 (ITIL 4 Service Value Chain).

### 3.3 Integrasi Layanan Cerdas (Sem 6) vs Digital Platform Engineering (Sem 7)
* **Masalah:** `STI-601 Integrasi AI` vs `STI-701 Platform Engineering`.
* **Potensi Redundansi:** Keduanya bersinggungan di materi *API Gateway, Microservices, dan Container/Docker*.
* **Garis Batas Silabus yang Ditetapkan:**
  * **STI-601 (Sem 6):** Fokus pada **Machine Learning Serving Layer**: Membungkus model AI (PyTorch/ONNX) menjadi API berkecepatan tinggi, Vector Database (Milvus/Pinecone), RAG Pipeline, dan batch/stream inference.
  * **STI-701 (Sem 7):** Fokus pada **Enterprise Platform Plumbing**: Event-Driven Architecture, Message Broker (Apache Kafka/RabbitMQ), Service Mesh (Istio), distributed caching (Redis), dan high-availability infrastructure.

---

## 4. ANOMALI BEBAN SEMESTER: RESOLUSI *"SEMESTER 5 OVERLOAD TRAP"* — ✅ TERSELESAIKAN

### 4.1 Peta Sebaran Mata Kuliah Praktikum Laboratorium (+P / Hands-on) Terkini

```
Distribusi Mata Kuliah Praktikum Lab (+P) Pasca-Pertukaran:
Sem 1: █ (1 MK / 3 SKS)
Sem 2: ██ (2 MK / 6 SKS)
Sem 3: ███ (3 MK / 9 SKS)
Sem 4: ███ (3 MK / 9 SKS: ML, DW-BI, Web BE) ──→ Sangat Seimbang
Sem 5: ████ (4 MK Wajib Lab + 1 MK Manpro TI Teori) ──→ BEBAN AMAN & SEHAT
Sem 6: ███ + 🔄 (3 MK Wajib Lab + Pilihan)
Sem 7: ███ + 🔄 (3 MK Wajib Lab + Pilihan)
Sem 8: █ (Skripsi / Capstone TA)
```

### 4.2 Hasil Resolusi Penyeimbangan Semester 4 & 5
* **Semester 4 (Genap - 19 SKS):** Mengakomodasi `STI-402 DW-BI` (+P, 3 SKS) bersama `Machine Learning` (+P, 3 SKS) dan `Web Back End` (+P, 3 SKS). Total 3 MK Lab (+ 4 MK Teori & MKWU) $\rightarrow$ **Sangat Seimbang**.
* **Semester 5 (Ganjil - 21 SKS):** Mengakomodasi `STI-506 Manpro TI` (Non-+P, 3 SKS). Total 4 MK Lab Wajib (Deep Learning, Data Mining, IoT, Mobile) + 1 MK Manajerial (Manpro TI).
* **Dampak Keunggulan Tambahan:** Pembelajaran *Manpro TI* di Semester 5 kini berada tepat **1 semester sebelum eksekusi *Capstone Project* di Semester 6**, memberikan retensi metodologi *Agile/Scrum* yang optimal bagi mahasiswa.

---

## 5. KELAYAKAN OPERASIONAL & KEBUTUHAN SUMBER DAYA

| Aspek Infrastruktur | Kebutuhan Riil Kurikulum 2026 | Rekomendasi Solusi Efisiensi Biaya |
|---|---|---|
| **GPU & Server Komputasi AI** | Deep Learning, MLOps, AI Integration, Smart Surveillance membutuhkan hardware GPU (NVIDIA CUDA). | Hindari pembelian server lokal yang mahal; manfaatkan kemitraan cloud akademis: *Google Colab Pro, Kaggle GPU, AWS Academy, Microsoft Learn for Educators*. |
| **Lab Hardware IoT & Sensor** | IoT (Sem 5) dan Smart City (Sem 6) membutuhkan kit mikrokontroler (ESP32, sensor array, LoRa gateway). | Terapkan kebijakan *Personal IoT Starter Kit* mandiri bagi mahasiswa atau penyediaan 1 set kit per kelompok Capstone di laboratorium. |
| **Kesiapan Dosen Pengampu** | MK spesialis: *MLOps, TOGAF, BPMN Automation, Cloud DevOps, Spatial XR*. | Rencanakan program sertifikasi dosen berskala bertahap (AWS Certified Architect, TOGAF Foundation, TensorFlow Certified) pada periode transisi 2026–2027. |

---

## 6. PANDUAN UNTUK FASE KERJA SELANJUTNYA (MIKRO RPS & CPMK)

Hasil audit ini menjadi rujukan wajib (*mandatory design guidelines*) saat menyusun RPS dan instrumen asesmen OBE:

1. **Formulasi CPMK Berbasis Gagne/Bloom:** Pastikan kata kerja operasional di Semester 1–2 berfokus pada C2–C3, Semester 3–4 pada C3–C4, dan Semester 5–8 pada C4–C6.
2. **Penerapan Case Method & PjBL ($\ge 50\%$ Bobot Nilai):** Sesuai IKU 7 Dikti, instrumen evaluasi harus mengutamakan penilaian portofolio dan pemecahan kasus nyata.
3. **Penyusunan Rubrik Penilaian Capstone Project (FST-610) & Skripsi (FST-714):** Rubrik analitik wajib memuat penilaian multidisiplin, komunikasi lisan, kerja tim, dan kualitas artefak perangkat lunak.

---

*Dokumen ini merupakan Single Source of Truth untuk evaluasi kritis, manajemen risiko pedagogis, dan pedoman penyusunan RPS mikro Program Studi SISTEKIN UWG 2026.*

