# 026 — FORMULASI LENGKAP PL, CPL, CPMK & SUB-CPMK: SEMESTER 5 & SEMESTER 6

**Tanggal:** 18 Agustus 2026  
**Peran:** Arsitek Kurikulum & Asesor LAM INFOKOM / IABEE  
**Sumber Rujukan:** Dokumen 008 (PL), 009 (14 CPL), 011 (Tabel MK), 020–025  
**Standar Konstruksi:** Taksonomi Bloom (C4–C6), Kata Kerja Operasional Gagne, dan Formula **ABCD** (*Audience, Behavior, Condition, Degree*).

---

# BAGIAN I: FORMULASI MATA KULIAH WAJIB SEMESTER 5 (21 SKS)

---

### 1. STI-501: Deep Learning dan Neural Networks (3 SKS, +P)
* **Profil Lulusan Terkait:** PL-01, PL-06 (Flagship AI & Data)
* **CPL yang Dibebankan:** **KK1** (Model AI Lanjut), **KK2** (Deep Learning & Neural Architectures)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **menganalisis** prinsip matematika jaringan saraf tiruan (*Multi-Layer Perceptron / MLP, Backpropagation, Gradient Descent, Activation Functions: ReLU, Sigmoid, Softmax*) dan penanganan *Vanishing/Exploding Gradient*. | **C4** |
| **CPMK-2** | Mahasiswa mampu **mengonstruksi** arsitektur *Convolutional Neural Networks (CNN: ResNet, VGG, MobileNet)* untuk tugas klasifikasi citra dan deteksi objek menggunakan kerangka kerja **PyTorch**. | **C6** |
| **CPMK-3** | Mahasiswa mampu **mengonstruksi** arsitektur *Recurrent Neural Networks (RNN, LSTM, GRU)* dan mekanisme *Self-Attention / Transformer* untuk pemrosesan data sekuensial dan teks alami (NLP). | **C6** |
| **CPMK-4** | Mahasiswa mampu **mengoptimalkan** pelatihan model deep learning melalui teknik regularisasi (*Dropout, Batch Normalization, Weight Decay*) dan *Transfer Learning* untuk mencapai akurasi tinggi pada dataset terbatas. | **C5** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 1.1:** Mampu memprogram feedforward dan backpropagation manual pada PyTorch tensor (C4).
* **Sub-CPMK 1.2:** Mampu merancang layer konvolusi, pooling, dan fully connected layer untuk pengenalan pola gambar (C5).
* **Sub-CPMK 1.3:** Mampu menerapkan Transfer Learning menggunakan model pra-terlatih (Pretrained ResNet/Vision Transformer) (C4).
* **Sub-CPMK 1.4:** Mampu melatih model LSTM untuk prediksi runtun waktu (*time series forecasting*) (C5).
* **Sub-CPMK 1.5:** Mampu memvisualisasikan kurva loss/accuracy dan feature map representasi laten (C4).

---

### 2. STI-503: Data Mining & Visualization (3 SKS, +P)
* **Profil Lulusan Terkait:** PL-01, PL-06
* **CPL yang Dibebankan:** **P2** (Konsep Data Analytics), **KK2** (Penambangan Pola & Visualisasi Data Lanjut)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **menerapkan** metodologi standar industri penambangan data (**CRISP-DM**: *Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment*). | **C3** |
| **CPMK-2** | Mahasiswa mampu **menemukan** pola asosiasi (*Association Rule Mining: Algoritma Apriori dan FP-Growth*) pada transaksi bisnis multiskala (*Market Basket Analysis*). | **C4** |
| **CPMK-3** | Mahasiswa mampu **menganalisis** pengelompokan data kompleks (*Clustering Lanjut: DBSCAN, Gaussian Mixture Models, Hierarchical*) dan deteksi anomali (*Anomaly / Outlier Detection: Isolation Forest*). | **C4** |
| **CPMK-4** | Mahasiswa mampu **membangun** visualisasi data bercerita (*Data Storytelling & Interactive Visual Analytics*) menggunakan pustaka grafis modern (**Plotly / Seaborn / D3.js**). | **C6** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 2.1:** Mampu mengevaluasi nilai *Support, Confidence*, dan *Lift Ratio* pada aturan asosiasi (C4).
* **Sub-CPMK 2.2:** Mampu menangani klaster berbentuk non-sferikal menggunakan DBSCAN dan mengevaluasi metrik Silhouette (C4).
* **Sub-CPMK 2.3:** Mampu mendeteksi data pencilan (*anomaly score*) pada transaksi finansial/log server (C4).
* **Sub-CPMK 2.4:** Mampu merancang visualisasi interaktif multi-dimensi untuk presentasi wawasan data bisnis (C6).

---

### 3. STI-504: Internet of Things (IoT) (3 SKS, +P)
* **Profil Lulusan Terkait:** PL-03, PL-06 (Integrator Sistem Cerdas & Cyber-Physical)
* **CPL yang Dibebankan:** **P3** (Infrastruktur IoT/Sensor), **KK3** (Rekayasa Perangkat Keras & Edge Gateway)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **menguraikan** arsitektur sistem IoT 4-lapisan (*Perception, Network, Edge/Middleware, Application Layer*) dan karakteristik protokol IoT (**MQTT, CoAP, HTTP REST, LoRaWAN**). | **C2** |
| **CPMK-2** | Mahasiswa mampu **mengonfigurasi** mikrokontroler (*ESP32 / NodeMCU / Arduino*) yang terhubung dengan sensor analog/digital dan aktuator secara presisi. | **C4** |
| **CPMK-3** | Mahasiswa mampu **membangun** sistem komunikasi data telemetri menggunakan protokol MQTT (*Broker Eclipse Mosquitto, Publisher, Subscriber, QoS 0/1/2*) secara real-time. | **C6** |
| **CPMK-4** | Mahasiswa mampu **mengintegrasikan** perangkat IoT dengan dasbor pemantauan awan (*Cloud IoT Platform: Blynk / ThingsBoard / Node-RED*) dan sistem penyimpanan basis data *Time-Series*. | **C6** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 3.1:** Mampu membaca sinyal sensor suhu, kelembaban, gerak, jarak, dan gas pada ESP32 (C3).
* **Sub-CPMK 3.2:** Mampu memprogram pengiriman payload data berformat JSON via WiFi dan MQTT (C4).
* **Sub-CPMK 3.3:** Mampu merancang alur logika otomatisasi di Node-RED untuk kontrol aktuator jarak jauh (C5).
* **Sub-CPMK 3.4:** Mampu membangun purwarupa solusi IoT (*Smart Home / Smart Agriculture*) terintegrasi cloud (C6).

---

### 4. STI-505: Pemrograman Aplikasi Mobile (3 SKS, +P)
* **Profil Lulusan Terkait:** PL-02, PL-04
* **CPL yang Dibebankan:** **P4** (Arsitektur Mobile), **KK5** (Pengembangan Aplikasi Mobile Multiplatform)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **menganalisis** arsitektur aplikasi mobile, siklus hidup activity/widget, dan perbedaan pendekatan *Native vs Cross-Platform* (Flutter / React Native). | **C4** |
| **CPMK-2** | Mahasiswa mampu **membangun** antarmuka aplikasi mobile responsif multi-layar menggunakan **Flutter (Dart)** dengan mematuhi pedoman *Material Design 3 / Apple HIG*. | **C6** |
| **CPMK-3** | Mahasiswa mampu **mengimplementasikan** arsitektur manajemen state modern (*Provider / BLoC / Riverpod*) dan persistensi data lokal (*SQLite / Hive / SharedPreferences*). | **C4** |
| **CPMK-4** | Mahasiswa mampu **mengintegrasikan** aplikasi mobile dengan RESTful API eksternal, otentikasi biometrik/OAuth, dan fitur perangkat keras (Kamera, GPS Geolocation, Push Notification). | **C5** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 4.1:** Mampu menyusun widget layout kompleks (Row, Column, Stack, ListView, CustomScrollView) (C3).
* **Sub-CPMK 4.2:** Mampu menerapkan state management BLoC untuk pemisahan logika bisnis dan antarmuka (C4).
* **Sub-CPMK 4.3:** Mampu mengimplementasikan CRUD lokal dengan SQLite/Isar Database (C4).
* **Sub-CPMK 4.4:** Mampu melakukan integrasi Google Maps API dan Geolocation pada aplikasi mobile (C4).
* **Sub-CPMK 4.5:** Mampu mengemas file rilis APK/AAB yang teroptimasi untuk publikasi Google Play Store (C4).

---

### 5. STI-506: Manajemen Proyek Teknologi Informasi (3 SKS, Teori)
* **Profil Lulusan Terkait:** PL-04, PL-05 (Persiapan Capstone Project Sem 6)
* **CPL yang Dibebankan:** **KK6** (Manajemen Proyek Agile & Tata Kelola Proyek TI)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **menyusun** dokumen inisiasi dan perencanaan proyek TI (*Project Charter, Work Breakdown Structure / WBS, Project Schedule Network Diagram*) berbasis standar **PMBOK**. | **C6** |
| **CPMK-2** | Mahasiswa mampu **mengestimasi** estimasi biaya, sumber daya, dan durasi proyek (*Cost & Time Estimation: Function Point Analysis, COCOMO, Pert Chart*) secara akurat. | **C4** |
| **CPMK-3** | Mahasiswa mampu **menerapkan** metodologi manajemen proyek adaptif (**Agile Scrum**: *Product Backlog, Sprint Planning, Daily Scrum, Sprint Review, Retrospective*) menggunakan alat kolaborasi **Jira / Trello**. | **C4** |
| **CPMK-4** | Mahasiswa mampu **mengevaluasi** kemajuan proyek menggunakan analisis nilai hasil (*Earned Value Management / EVM: CPI, SPI, EAC*) dan menyusun rencana mitigasi risiko proyek. | **C5** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 5.1:** Mampu mendekomposisi ruang lingkup proyek perangkat lunak ke dalam WBS hierarkis (C4).
* **Sub-CPMK 5.2:** Mampu menentukan Jalur Kritis (*Critical Path Method / CPM*) pada jadwal proyek (C4).
* **Sub-CPMK 5.3:** Mampu mengelola User Stories, Story Points, dan Burndown Chart di Jira (C4).
* **Sub-CPMK 5.4:** Mampu menghitung varians biaya (CV) dan varians jadwal (SV) dengan rumus EVM (C4).

---

# BAGIAN II: FORMULASI MATA KULIAH WAJIB SEMESTER 6 (20 SKS)

---

### 6. STI-601: Integrasi Layanan Cerdas Berbasis AI (3 SKS, +P)
* **Profil Lulusan Terkait:** PL-01, PL-06 (Flagship AI Integration)
* **CPL yang Dibebankan:** **P2** (Arsitektur AI Terdistribusi), **KK1** (Deployment Model AI ke API & SI)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **merancang** arsitektur *Machine Learning Serving* berkecepatan tinggi (*Inference Latency Optimization*) menggunakan kerangka kerja **FastAPI / ONNX Runtime / Triton Inference Server**. | **C6** |
| **CPMK-2** | Mahasiswa mampu **mengemas** model AI dan dependensinya ke dalam kontainer (*Docker Containerization*) untuk deployment mikroservis cerdas yang terisolasi. | **C4** |
| **CPMK-3** | Mahasiswa mampu **membangun** pipa penelusuran semantik (*Retrieval-Augmented Generation / RAG*) mengintegrasikan *Vector Database* (**Milvus / Pinecone / ChromaDB**) dan *Large Language Models (LLM API)*. | **C6** |
| **CPMK-4** | Mahasiswa mampu **menguji** ketahanan dan skalabilitas layanan AI di bawah beban trafik tinggi (*Load Testing & Batch/Stream Inference*) secara terukur. | **C5** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 6.1:** Mampu mengekspor model PyTorch/scikit-learn ke format terstandar ONNX (C3).
* **Sub-CPMK 6.2:** Mampu membuat endpoint REST API async untuk inference model klasifikasi/prediksi (C4).
* **Sub-CPMK 6.3:** Mampu melakukan embedding teks dan kueri similarity search pada Vector DB (C5).
* **Sub-CPMK 6.4:** Mampu membuat Dockerfile dan docker-compose multi-service (API + Vector DB + Cache) (C5).

---

### 7. STI-602: Smart City dan Pemerintahan Digital (3 SKS, +P)
* **Profil Lulusan Terkait:** PL-03, PL-05
* **CPL yang Dibebankan:** **P3** (Sistem Skala Luas & SPBE), **KK3** (Integrasi Solusi Perkotaan Cerdas)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
### 6. MKU-203: Kuliah Pengabdian Masyarakat / KKN Digital (3 SKS, +P)
* **Profil Lulusan Terkait:** Seluruh PL (PL-01 s.d. PL-06)
* **CPL yang Dibebankan:** **S1** (Kepedulian Sosial & Integritas), **KU1** (Problem Solving di Masyarakat), **KU2** (Komunikasi Komunitas)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **mengidentifikasi** permasalahan dan potensi transformasi digital pada masyarakat mitra, desa, atau UMKM secara partisipatif. | **C4, A3** |
| **CPMK-2** | Mahasiswa mampu **merancang** dan **mengimplementasikan** program kerja pemberdayaan berbasis teknologi informasi (literasi digital, sistem informasi desa, website UMKM, otomasi administrasi). | **C6** |
| **CPMK-3** | Mahasiswa mampu **mengevaluasi** dampak program pengabdian dan menyusun laporan pertanggungjawaban serta video dokumentasi luaran pengabdian masyarakat. | **C5, KU2** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 6.1:** Mampu melakukan survei lapangan dan Focus Group Discussion (FGD) bersama perangkat desa/mitra (C4).
* **Sub-CPMK 6.2:** Mampu mengeksekusi solusi sistem dan teknologi informasi terapan sesuai kebutuhan riil masyarakat (C6).
* **Sub-CPMK 6.3:** Mampu mendiseminasikan hasil luaran KKN Digital pada publikasi media massa atau seminar pengabdian (C5).

---

# BAGIAN II: FORMULASI MATA KULIAH WAJIB SEMESTER 6 (20 SKS)

---

### 7. STI-601: Integrasi Layanan Cerdas Berbasis AI (3 SKS, +P)
* **Profil Lulusan Terkait:** PL-01 (Intelligent IS Dev), PL-03 (Smart Sys Integrator)
* **CPL yang Dibebankan:** **P2** (Integrasi AI), **KK1** (AI Deployment & API Orchestration)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **merancang** arsitektur *AI Serving Layer* untuk membungkus model pembelajaran mesin ke dalam RESTful API / gRPC berlatensi rendah (**FastAPI / TorchServe / Triton**). | **C6** |
| **CPMK-2** | Mahasiswa mampu **mengonstruksi** alur kerja pencarian semantik dan *Retrieval-Augmented Generation (RAG)* menggunakan *Vector Database* (**Milvus / Pinecone / Chroma**). | **C6** |
| **CPMK-3** | Mahasiswa mampu **mengintegrasikan** *Large Language Model (LLM)* dan model kecerdasan artifisial multimodal ke dalam aplikasi enterprise melalui teknik *Prompt Engineering* dan *Function Calling*. | **C5** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 7.1:** Mampu melakukan konversi dan optimasi model AI ke format ONNX/TensorRT (C4).
* **Sub-CPMK 7.2:** Mampu memprogram embedding generator dan indexing dokumen pada Vector DB (C4).
* **Sub-CPMK 7.3:** Mampu membangun pipeline RAG terpadu dengan orkestrasi LangChain / LlamaIndex (C6).
* **Sub-CPMK 7.4:** Mampu melakukan load testing dan monitoring performa latency API AI (C5).

---

### 8. STI-602: Smart City & Pemerintahan Digital (3 SKS, +P)
* **Profil Lulusan Terkait:** PL-03, PL-05
* **CPL yang Dibebankan:** **P3** (Sistem Perkotaan & SPBE), **KK3** (Integrasi Sensor & Data Spasial)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **menganalisis** 6 pilar kota cerdas (*Smart Governance, Smart Economy, Smart Living, Smart Mobility, Smart Environment, Smart People*) dan arsitektur **SPBE** (*Sistem Pemerintahan Berbasis Elektronik*). | **C4** |
| **CPMK-2** | Mahasiswa mampu **mengintegrasikan** data spasial dan sensor lingkungan (*Geographic Information System / GIS & IoT Sensors*) ke dalam dasbor command center kota cerdas. | **C5** |
| **CPMK-3** | Mahasiswa mampu **merancang** purwarupa layanan publik digital inklusif (*Citizen-Centric E-Government Services*) yang memenuhi standar interoperabilitas data pemerintah (Satu Data Indonesia). | **C6** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 8.1:** Mampu menelaah domain arsitektur SPBE (Layanan, Proses Bisnis, Data, Aplikasi, Keamanan) (C4).
* **Sub-CPMK 8.2:** Mampu memprocess peta spasial menggunakan QGIS dan visualisasi GeoJSON (C3).
* **Sub-CPMK 8.3:** Mampu mengintegrasikan data sensor kualitas udara/banjir ke portal dashboard kota (C5).
* **Sub-CPMK 8.4:** Mampu merancang arsitektur interoperabilitas data API antar-organisasi publik (C6).

---

### 9. STI-603: Keamanan Informasi Lanjut (3 SKS, Teori)
* **Profil Lulusan Terkait:** PL-03, PL-05
* **CPL yang Dibebankan:** **P3** (Keamanan Siber Enterprise), **KK3** (Incident Response), **KK4** (Investigasi & Forensik Digital)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **menganalisis** metodologi investigasi forensik digital (*Digital Forensics: Chain of Custody, Disk Forensics, Memory Forensics, Network Forensics*) sesuai standar ISO 27037. | **C4** |
| **CPMK-2** | Mahasiswa mampu **merancang** prosedur penanganan insiden keamanan siber (*Computer Security Incident Response Team / CSIRT: Preparation, Detection, Containment, Eradication, Recovery*). | **C5** |
| **CPMK-3** | Mahasiswa mampu **melakukan** simulasi uji penetrasi keamanan (*Penetration Testing / Ethical Hacking*) pada jaringan dan sistem operasi menggunakan kerangka kerja MITRE ATT&CK. | **C4** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 9.1:** Mampu melakukan akuisisi image bit-by-bit harddisk menggunakan alat forensik FTK Imager (C3).
* **Sub-CPMK 9.2:** Mampu menganalisis artefak RAM memory dump menggunakan Volatility Framework (C4).
* **Sub-CPMK 9.3:** Mampu menyusun *Playbook Penanganan Insiden Ransomware* dan *Data Breach* (C5).
* **Sub-CPMK 9.4:** Mampu melakukan vulnerability scanning jaringan menggunakan Nessus / Nmap (C4).

---

### 10. STI-604: Digital Platform Engineering (3 SKS, +P)
* **Profil Lulusan Terkait:** PL-02, PL-04
* **CPL yang Dibebankan:** **KK5** (Arsitektur Platform Terdistribusi), **P4** (Microservices Plumbing)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **merancang** arsitektur sistem terdistribusi berskala besar (*Distributed Systems: Microservices Pattern, Service Registry, API Gateway Kong/Ocelot, Event-Driven Architecture*). | **C6** |
| **CPMK-2** | Mahasiswa mampu **mengimplementasikan** komunikasi asinkronus berkecepatan tinggi antar-layanan menggunakan *Message Broker / Streaming Platform* (**Apache Kafka / RabbitMQ**). | **C4** |
| **CPMK-3** | Mahasiswa mampu **membangun** strategi *Distributed Caching* (**Redis**) dan manajemen isolasi basis data terdistribusi (*Database-per-service & Saga Pattern*). | **C5** |
| **CPMK-4** | Mahasiswa mampu **mengonfigurasi** *Continuous Integration / Continuous Deployment (CI/CD)* pipeline menggunakan GitHub Actions / GitLab CI untuk otomatisasi testing dan rilis. | **C4** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 10.1:** Mampu mendekomposisi arsitektur monolitik menjadi bounded context microservices (C4).
* **Sub-CPMK 10.2:** Mampu memprogram producer, consumer, dan topic partition di Apache Kafka (C4).
* **Sub-CPMK 10.3:** Mampu mengimplementasikan caching Redis untuk optimasi query throughput tinggi (C4).
* **Sub-CPMK 10.4:** Mampu membangun pipeline CI/CD otomatis dengan pengujian unit test dan docker build (C5).

---

### 11. FST-611: Metodologi Penelitian (2 SKS, Teori — Bersama FSTI)
* **Profil Lulusan Terkait:** Seluruh PL
* **CPL yang Dibebankan:** **KU1** (Metode Ilmiah), **KU2** (Penulisan Ilmiah), **KU3** (Kajian Literatur Kritis)

| Kode CPMK | Rumusan CPMK (Formula ABCD) | Level Bloom |
|---|---|:---:|
| **CPMK-1** | Mahasiswa mampu **mengidentifikasi** kesenjangan riset (*Research Gap*) melalui telaah literatur sistematis (*Systematic Literature Review / SLR*) pada jurnal internasional/nasional bereputasi. | **C4** |
| **CPMK-2** | Mahasiswa mampu **memilih** metode penelitian komputasi yang tepat (*Design Science Research Methodology / DSRM*, Eksperimen Kuantitatif, Analisis Performa Algoritma). | **C4** |
| **CPMK-3** | Mahasiswa mampu **menyusun** proposal penelitian Tugas Akhir / Skripsi yang lengkap, sistematis, mematuhi etika akademik, dan siap diseminarkan pada forum Pra-Skripsi di Semester 7. | **C6** |

#### Rincian Sub-CPMK:
* **Sub-CPMK 11.1:** Mampu merumuskan latar belakang masalah, pertanyaan penelitian, dan batasan masalah yang terukur (C4).
* **Sub-CPMK 11.2:** Mampu menggunakan Reference Manager (Mendeley/Zotero) dengan gaya sitasi IEEE/APA (C3).
* **Sub-CPMK 11.3:** Mampu merancang kerangka konseptual penelitian dan rencana pengujian validitas instrumen riset (C5).
* **Sub-CPMK 11.4:** Mampu menyusun draft Bab 1, Bab 2, dan Bab 3 Proposal Skripsi sesuai template resmi FSTI (C6).

---

*Dokumen ini merupakan formulasi resmi CPMK dan Sub-CPMK berbasis OBE untuk seluruh Mata Kuliah Wajib Semester 5 dan 6 Program Studi SISTEKIN UWG 2026.*
