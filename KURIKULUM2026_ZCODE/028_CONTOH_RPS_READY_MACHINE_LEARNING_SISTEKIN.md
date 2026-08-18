# 028 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## PROGRAM STUDI SISTEM DAN TEKNOLOGI INFORMASI (SISTEKIN)
### FAKULTAS SAINS DAN TEKNOLOGI INFORMASI — UNIVERSITAS WIDYAGAMA MALANG

---

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 DOKUMEN KURIKULUM OBE                                  │
│                             RENCANA PEMBELAJARAN SEMESTER                              │
│             Mata Kuliah: MACHINE LEARNING | Kode: STI-401 | Bobot: 3 SKS (+P)          │
│                Standar Akreditasi: LAM INFOKOM / IABEE / SN-Dikti No. 53/2023          │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. IDENTITAS MATA KULIAH

| Item | Keterangan |
|---|---|
| **Program Studi** | Sistem dan Teknologi Informasi (SISTEKIN) — Program Sarjana (S1) |
| **Fakultas** | Fakultas Sains dan Teknologi Informasi (FSTI) |
| **Nama Mata Kuliah** | **Machine Learning** |
| **Nama Bahasa Inggris**| *Machine Learning* |
| **Kode Mata Kuliah** | **STI-401** |
| **Bobot SKS** | **3 SKS (2 SKS Teori + 1 SKS Praktikum Lab)** |
| **Semester Penawaran**| Semester 4 (Genap) |
| **Rumpun Keilmuan (RMK)**| Sistem Cerdas & Sains Data (*Intelligent Systems & Data Science*) |
| **Mata Kuliah Prasyarat**| `FST-207 Basis Data` (Lulus minimal C) & `FST-408 Statistika & Probabilitas` |
| **Dosen Pengembang RPS** | Tim Dosen KBK Sistem Cerdas SISTEKIN |
| **Koordinator RMK** | Dr. Ir. Roni Wahyu, S.Kom., M.T. |
| **Ketua Program Studi**| Ketua Program Studi SISTEKIN FSTI UWG |

---

## 2. OTORISASI DAN PENGESAHAN

| Peran | Nama Terang & Gelar | Tanda Tangan / Status | Tanggal |
|---|---|:---:|:---:|
| **Dosen Pengembang RPS** | Tim Dosen KBK Sistem Cerdas | *(Tervalidasi Digital)* | 18 Agustus 2026 |
| **Koordinator RMK** | Dr. Ir. Roni Wahyu, S.Kom., M.T. | *(Disetujui)* | 18 Agustus 2026 |
| **Ketua Program Studi** | Ketua Prodi SISTEKIN | *(Disahkan)* | 18 Agustus 2026 |

---

## 3. CAPAIAN PEMBELAJARAN MATA KULIAH (CPL $\rightarrow$ CPMK $\rightarrow$ SUB-CPMK)

### 3.1 Profil Lulusan (PL) yang Didukung
* **PL-01:** *Intelligent Information System Developer* (Pengembang SI Cerdas)
* **PL-06:** *Data Analyst & Machine Learning Engineer* (Perekayasa Data & ML)

### 3.2 CPL yang Dibebankan pada Mata Kuliah
* **P2 (Pengetahuan):** Menguasai konsep dasar sistem informasi, arsitektur data, dan kecerdasan artifisial.
* **KK1 (Keterampilan Khusus):** Mampu merancang, melatih, dan mengintegrasikan model kecerdasan artifisial/machine learning ke dalam sistem informasi bisnis.
* **KK2 (Keterampilan Khusus):** Mampu melakukan penyiapan data (*preprocessing*), ekstraksi fitur (*feature engineering*), dan evaluasi performa model prediktif berbasis dataset empiris.

### 3.3 Capaian Pembelajaran Mata Kuliah (CPMK) — Formula ABCD & Bloom
* **CPMK-1 (C3):** Mahasiswa (*A*) mampu **menerapkan** alur kerja rekayasa data Machine Learning (*Exploratory Data Analysis, Data Cleaning, Imputation, Feature Encoding, Feature Scaling*) (*B*) menggunakan bahasa pemrograman Python dan pustaka scikit-learn/pandas (*C*) secara tepat dan bebas dari kebocoran data (*data leakage*) (*D*).
* **CPMK-2 (C5):** Mahasiswa (*A*) mampu **mengonstruksi** dan **melatih** model pembelajaran terbimbing (*Supervised Learning: Linear Regression, Logistic Regression, Decision Tree, Random Forest, Support Vector Machine*) (*B*) pada dataset tabular (*C*) dengan parameter optimal (*D*).
* **CPMK-3 (C5):** Mahasiswa (*A*) mampu **mengonstruksi** model pembelajaran tak-terbimbing (*Unsupervised Learning: K-Means Clustering, Hierarchical Clustering, Principal Component Analysis / PCA*) (*B*) untuk segmentasi data dan reduksi dimensi (*C*) dengan validasi skor siluet yang valid (*D*).
* **CPMK-4 (C5, C6):** Mahasiswa (*A*) mampu **mengevaluasi** performa model menggunakan metrik terstandar (*Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC, RMSE, k-fold Cross-Validation*) (*B*) serta **membangun** purwarupa aplikasi prediktif terintegrasi (*ML Deployment Prototype*) (*C*) dengan akurasi dan stabilitas yang dapat dipertanggungjawabkan (*D*).

### 3.4 Pemetaan CPMK $\rightarrow$ Sub-CPMK

| Kode Sub-CPMK | Rumusan Sub-CPMK (Kemampuan Akhir Tiap Tahapan Belajar) | Terkait CPMK | Level Bloom |
|:---:|---|:---:|:---:|
| **Sub-CPMK 1** | Mampu menguraikan paradigma Machine Learning (Supervised, Unsupervised, Reinforcement) dan arsitektur alur kerja ML. | CPMK-1 | C2 |
| **Sub-CPMK 2** | Mampu melakukan manipulasi dataset, eksplorasi statistik, dan penanganan missing values/outliers menggunakan Pandas & NumPy. | CPMK-1 | C3 |
| **Sub-CPMK 3** | Mampu merekayasa fitur (One-Hot Encoding, Ordinal Encoding, MinMax/Standard Scaling) tanpa data leakage. | CPMK-1 | C3 |
| **Sub-CPMK 4** | Mampu memodelkan dan menguji algoritma Regresi Linier Berganda dan Regresi Polinomial untuk estimasi nilai kontinu. | CPMK-2 | C4 |
| **Sub-CPMK 5** | Mampu mengimplementasikan Klasifikasi Logistik (*Logistic Regression*) dan mengevaluasi batas keputusan (*decision boundary*). | CPMK-2 | C4 |
| **Sub-CPMK 6** | Mampu merancang pohon keputusan (*Decision Tree*) dan ansambel *Random Forest* dengan analisis *Gini Impurity / Information Gain*. | CPMK-2 | C5 |
| **Sub-CPMK 7** | Mampu menerapkan algoritma *Support Vector Machine (SVM)* dengan optimasi fungsi kernel linier/RBF. | CPMK-2 | C4 |
| **Sub-CPMK 8** | Mampu mengevaluasi performa klasifikasi menggunakan Confusion Matrix, F1-Score, dan kurva ROC-AUC secara kritis. | CPMK-4 | C5 |
| **Sub-CPMK 9** | Mampu melakukan penalaan hiperparameter (*Hyperparameter Tuning*) dengan Grid Search dan Random Search CV. | CPMK-4 | C5 |
| **Sub-CPMK 10** | Mampu mengelompokkan data tanpa label menggunakan algoritma K-Means dan menentukan jumlah klaster optimal (*Elbow & Silhouette*). | CPMK-3 | C4 |
| **Sub-CPMK 11** | Mampu mereduksi dimensionalitas fitur berdimensi tinggi menggunakan *Principal Component Analysis (PCA)* dengan retensi variansi $\ge 90\%$. | CPMK-3 | C5 |
| **Sub-CPMK 12** | Mampu melakukan serialisasi model terlatih (*Model Serialization* via Joblib/Pickle) dan membungkusnya menjadi API inferensi berbasis web. | CPMK-4 | C6 |
| **Sub-CPMK 13** | Mampu menyelesaikan proyek tim berbasis masalah nyata (*Project-Based Learning*) dan mempresentasikannya secara profesional. | CPMK-1 s.d 4 | C6, KU2 |

---

## 4. DESKRIPSI SINGKAT & BAHAN KAJIAN

### 4.1 Deskripsi Mata Kuliah
Mata kuliah **Machine Learning (STI-401)** membekali mahasiswa dengan penguasaan teoretis dan keterampilan praktis dalam merancang, melatih, mengevaluasi, dan menerapkan algoritma pembelajaran mesin untuk pemecahan masalah bisnis dan rekayasa sistem informasi cerdas. Pembelajaran mencakup siklus pemodelan data end-to-end, supervised learning, unsupervised learning, validasi performa model, serta serialisasi model untuk kesiapan integrasi aplikasi nyata. Perkuliahan diselenggarakan dengan pendekatan **Case Method** dan **Project-Based Learning (PjBL)** berbantuan laboratorium komputasi Python.

### 4.2 Bahan Kajian (Body of Knowledge APTIKOM)
* **`SI-BK13` / `TI-BK22`:** Artificial Intelligence Concepts, Machine Learning Algorithms & Predictive Analytics.
* **`SI-BK18`:** Emerging Intelligent Systems & Automated Inference.
* **`SI-BK11` / `TI-BK18`:** Applied Mathematics for Computing & Statistical Modeling.

---

## 5. PUSTAKA DAN MEDIA PEMBELAJARAN

### 5.1 Pustaka Utama
1. Géron, Aurélien. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems (3rd Edition)*. O'Reilly Media.
2. Raschka, Sebastian, & Mirjalili, Vahid. (2020). *Python Machine Learning: Machine Learning and Deep Learning with Python, scikit-learn, and TensorFlow 2 (3rd Edition)*. Packt Publishing.
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning: with Applications in Python*. Springer.

### 5.2 Pustaka Pendukung
1. Panduan Kurikulum OBE APTIKOM Program Studi Sistem Informasi v2.0 (2024).
2. Dokumen Kurikulum SISTEKIN UWG 2026 (Dokumen 006 s.d. 027).

### 5.3 Perangkat Lunak & Media Pembelajaran
* **Software/Tools:** Python 3.11+, Jupyter Lab / Google Colab Pro, VS Code, Git/GitHub, scikit-learn, pandas, numpy, seaborn, joblib.
* **Hardware:** Laboratorium Komputasi Sains Data FSTI UWG.

---

## 6. RANCANGAN PEMBELAJARAN 16 MINGGU (SEMESTER 4)

```
Beban Belajar per Minggu (3 SKS = 150 menit tatap muka + 170 menit praktikum lab + 180 menit tugas mandiri):
• Kuliah Teori & Diskusi Case Method : 2 x 50 menit
• Praktikum Hands-on Laboratorium    : 1 x 170 menit
• Belajar Mandiri & Pengerjaan Proyek: 2 x 60 menit
```

| Mg | Sub-CPMK | Indikator Penilaian | Kriteria & Bentuk Asesmen | Metode Pembelajaran (Estimasi Waktu) | Materi Pembelajaran (Pustaka) | Bobot (%) |
|:---:|---|---|---|---|---|:---:|
| **1** | **Sub-CPMK 1** | Ketepatan menjelaskan taksonomi ML, alur kerja CRISP-DM, dan setup lingkungan komputasi Python. | Kriteria: Ketepatan konseptual.<br>Bentuk: Kuis 1 & Lab Setup. | • Kuliah Teori (100m)<br>• Lab hands-on: Setup environment conda/colab (170m) | • Paradigma ML (Supervised, Unsupervised, RL)<br>• Python Data Science Stack Setup | **3%** |
| **2** | **Sub-CPMK 2** | Kemampuan memuat dataset, eksplorasi data (*EDA*), pembersihan data, dan visualisasi distribusi fitur. | Kriteria: Kualitas kode EDA.<br>Bentuk: Praktikum Lab 1. | • Case-based Learning (100m)<br>• Lab: EDA Titanic/Housing dataset (170m) | • Pandas DataFrame manipulation<br>• Handling missing values & outliers | **4%** |
| **3** | **Sub-CPMK 3** | Ketepatan melakukan transformasi fitur (*One-Hot/Ordinal Encoding, Standard/MinMax Scaler*) dan train-test split tanpa leakage. | Kriteria: Kebersihan pipeline data.<br>Bentuk: Tugas Mandiri 1. | • Kuliah Interaktif (100m)<br>• Lab: Preprocessing Pipeline (170m) | • Feature Engineering & Scaling<br>• scikit-learn `Pipeline` & `ColumnTransformer` | **4%** |
| **4** | **Sub-CPMK 4** | Kemampuan memodelkan Regresi Linier, interpretasi koefisien regresi, dan penghitungan metrik MSE/R2-Score. | Kriteria: Akurasi prediksi harga.<br>Bentuk: Praktikum Lab 2. | • Kuliah Teori Math (100m)<br>• Lab: Regression Case Study (170m) | • Ordinary Least Squares (OLS)<br>• Multiple Linear Regression & Polynomial | **5%** |
| **5** | **Sub-CPMK 5** | Kemampuan memodelkan Regresi Logistik biner/multikelas, fungsi sigmoid, dan penentuan ambang probabilitas. | Kriteria: Analisis probabilitas.<br>Bentuk: Praktikum Lab 3. | • Case Method (100m)<br>• Lab: Customer Churn Prediction (170m) | • Logistic Function, Log-Loss Cost<br>• Decision Boundary Visualization | **5%** |
| **6** | **Sub-CPMK 6** | Kemampuan mengonstruksi pohon keputusan, memangkas pohon (*pruning*), dan membangun ansambel *Random Forest*. | Kriteria: Optimalitas pohon & feature importance.<br>Bentuk: Tugas Mandiri 2. | • Problem-Based Learning (100m)<br>• Lab: Credit Risk Scoring (170m) | • Information Gain & Gini Impurity<br>• Bagging & Random Forest Classifier | **6%** |
| **7** | **Sub-CPMK 7** | Ketepatan memilih fungsi kernel SVM (*Linear, RBF, Poly*) dan menganalisis batas margin hyperplane optimal. | Kriteria: Ketepatan pemisahan margin.<br>Bentuk: Praktikum Lab 4. | • Kuliah Teori & Diskusi (100m)<br>• Lab: SVM High-dimensional classification (170m) | • Support Vector Machines (SVM)<br>• Kernel Trick & Hyperplane Optimization | **5%** |
| **8** | **EVALUASI TENGAH SEMESTER (UTS) — Ujian Teori Komprehensif & Ujian Praktikum Hands-on (Bobot: 15%)** | | | | | **15%** |
| **9** | **Sub-CPMK 8** | Ketepatan menganalisis *Confusion Matrix*, menghitung Precision/Recall/F1-Score, dan menganalisis trade-off kurva ROC-AUC. | Kriteria: Ketajaman analisis metrik.<br>Bentuk: Case Study Analysis. | • Case Method (100m)<br>• Lab: Medical Diagnosis Metric Evaluation (170m) | • Classification Metrics in Imbalanced Data<br>• Precision-Recall Curve & ROC-AUC | **6%** |
| **10** | **Sub-CPMK 9** | Kemampuan melakukan k-fold Cross-Validation dan otomatisasi penalaan hiperparameter (*GridSearchCV & RandomizedSearchCV*). | Kriteria: Efisiensi pencarian parameter.<br>Bentuk: Praktikum Lab 5. | • Kuliah & Demo (100m)<br>• Lab: Tuning Hyperparameter on Complex Data (170m) | • K-Fold Stratified Cross-Validation<br>• Hyperparameter Tuning Strategy | **5%** |
| **11** | **Sub-CPMK 10** | Kemampuan mengelompokkan data pelanggan dengan K-Means, menentukan k optimal (*Elbow & Silhouette*), dan profiling klaster. | Kriteria: Kualitas interpretasi klaster.<br>Bentuk: Praktikum Lab 6. | • Case Method (100m)<br>• Lab: Customer Segmentation Case (170m) | • K-Means & K-Medoids Clustering<br>• Cluster Validation & Business Profiling | **6%** |
| **12** | **Sub-CPMK 11** | Kemampuan mereduksi dimensi data menggunakan PCA dan memvisualisasikan fitur tereduksi dalam grafik 2D/3D. | Kriteria: Retensi variansi $\ge 90\%$.<br>Bentuk: Tugas Mandiri 3. | • Kuliah Aljabar Linier Terapan (100m)<br>• Lab: Image/Sensor PCA Dimensionality (170m) | • Principal Component Analysis (PCA)<br>• Eigenvalue Decomposition on Covariance | **5%** |
| **13** | **Sub-CPMK 12** | Kemampuan melakukan serialisasi model (*Joblib/Pickle*) dan membuat API inferensi sederhana dengan FastAPI / Streamlit. | Kriteria: Kelayakan aplikasi deploy.<br>Bentuk: Praktikum Lab 7. | • Project-Based Learning (100m)<br>• Lab: Model Serving Web Interface (170m) | • Model Export & Serialization<br>• Streamlit Web UI / FastAPI Endpoint | **6%** |
| **14** | **Sub-CPMK 13** | Kemampuan merancang arsitektur proyek ML tim end-to-end, presentasi progres milestone, dan peer-review kode. | Kriteria: Kejelasan arsitektur PjBL.<br>Bentuk: Milestone Review Proyek. | • PjBL Studio (100m)<br>• Lab: Team Project Sprint (170m) | • End-to-End Machine Learning Workflow<br>• Git Collaboration for Data Science | **5%** |
| **15** | **Sub-CPMK 13** | Demonstrasi produk proyek ML tim, pengujian fungsional, dan penyusunan laporan teknis berstandar IEEE. | Kriteria: Kelayakan produk & laporan.<br>Bentuk: Final Project Demo & Laporan. | • PjBL Presentation (100m)<br>• Lab: Live System Demonstration (170m) | • Final Project Exhibition & Tech Demo<br>• IEEE Technical Paper Documentation | **15%** |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Ujian Portofolio Proyek Akhir & Sidang Demonstrasi Sistem (Bobot: 10%)** | | | | | **10%** |

---

## 7. SISTEM EVALUASI & PEMBOBOTAN ASESMEN OBE

Struktur penilaian mematuhi **Indikator Kinerja Utama (IKU 7)** dengan bobot metode pemecahan kasus (*Case Method*) dan proyek berbasis tim (*Project-Based Learning*) $\ge 50\%$:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        KOMPOSISI PENILAIAN MATA KULIAH (100%)                          │
│                                                                                        │
│  [A] Evaluasi Partisipatif & Case Method (Tugas Lab Mingguan)      : 25%               │
│  [B] Proyek Terpadu Berbasis Tim (PjBL Final Project & Demo)       : 35%               │
│  [C] Ujian Tengah Semester (UTS - Teori Komprehensif & Coding Lab) : 20%               │
│  [D] Ujian Akhir Semester (UAS - Portofolio & Ujian Akhir)         : 20%               │
│  ────────────────────────────────────────────────────────────────────────────          │
│  TOTAL KOMPONEN ASESMEN OBE                                        : 100%              │
│  (Total Komponen Case Method + PjBL = 60% ──→ MEMENUHI STANDAR IKU 7 DIKTI ✅)          │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 7.1 Matriks Penilaian CPMK $\leftrightarrow$ Komponen Evaluasi

| Kode CPMK | Level Bloom | Tugas & Lab Mingguan (25%) | Proyek PjBL Tim (35%) | UTS (20%) | UAS (20%) | Total Kontribusi CPMK |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CPMK-1** | **C3** | 8% | 5% | 7% | — | **20%** |
| **CPMK-2** | **C5** | 7% | 10% | 8% | 5% | **30%** |
| **CPMK-3** | **C5** | 5% | 5% | 5% | 5% | **20%** |
| **CPMK-4** | **C5, C6** | 5% | 15% | — | 10% | **30%** |
| **TOTAL** | | **25%** | **35%** | **20%** | **20%** | **100%** |

---

## 8. RUBRIK PENILAIAN ANALITIK OBE

### 8.1 Rubrik Penilaian Proyek Terpadu PjBL (Bobot 35%)

| Dimensi Penilaian | Sangat Baik (85–100 / A) | Baik (70–84 / B) | Cukup (55–69 / C) | Kurang (<55 / D-E) |
|---|---|---|---|---|
| **Kualitas Rekayasa Data & Pipeline (25%)** | Preprocessing sempurna, bebas data leakage, eksplorasi EDA mendalam, pipeline modular terstruktur rapi. | Preprocessing tepat, pipeline berjalan baik, dokumentasi EDA cukup lengkap. | Preprocessing dasar, ada potensi data leakage minor, visualisasi minim. | Preprocessing salah, data leakage parah, kode berantakan. |
| **Pemilihan Model & Optimasi (25%)** | Menguji $\ge 3$ algoritma, tuning hiperparameter sistematis via CV, perbandingan metrik kritis dan tepat. | Menguji 2 algoritma, tuning parameter dasar, pemilihan metrik relevan. | Hanya 1 algoritma, tanpa tuning parameter, metrik evaluasi kurang pas. | Model asal pilih, tidak ada evaluasi performa yang valid. |
| **Purwarupa Aplikasi & Deploy (25%)** | Model terserialisasi dengan baik, UI Streamlit/FastAPI interaktif, responsif, dan error handling andal. | Model terserialisasi, UI sederhana berfungsi baik tanpa error fatal. | Model berjalan di notebook saja, UI belum sepenuhnya terintegrasi. | Aplikasi gagal berjalan (*crash*), tidak ada antarmuka. |
| **Laporan Ilmiah & Presentasi (25%)** | Naskah IEEE format rapi, analisis hasil tajam, presentasi lisan sangat meyakinkan, pembagian tugas tim merata. | Format laporan rapi, analisis cukup baik, presentasi lancar. | Laporan kurang terstruktur, analisis dangkal, presentasi kaku. | Laporan plagiat/tidak rapi, tidak siap presentasi. |

---

*Rencana Pembelajaran Semester (RPS) ini disusun sebagai dokumen operasional kurikulum terstandar OBE dan siap diterapkan pada Sistem Informasi Akademik (SIAKAD) Program Studi SISTEKIN UWG.*
