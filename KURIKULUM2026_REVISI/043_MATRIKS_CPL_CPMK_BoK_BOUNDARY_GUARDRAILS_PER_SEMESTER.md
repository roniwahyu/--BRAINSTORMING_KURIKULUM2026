# 043 — MATRIKS CPL, CPMK, BoK, DAN BOUNDARY GUARDRAILS PER MATA KULIAH
## Matriks Kompilasi Per Semester — Core STI & Peminatan (Kurikulum OBE SISTEKIN 2026)

**Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang**

> Dokumen kerja ini mengikat **CPL yang Dibebankan**, **Rumusan CPMK (ABCD + Level Bloom)**, **Bahan Kajian (BoK)**, dan **Boundary Guardrails (IN-SCOPE / OUT-OF-SCOPE / Handoff Anchor)** untuk setiap mata kuliah, disusun **per semester**. Urutan: **Bagian A — MK Core Prodi (STI)**; **Bagian B — MK Peminatan (STA/STB/STC)** per jalur.

**Sumber data:** Dok 005 (struktur semester & SKS), Dok 007 (CPL & CPMK ABCD), Dok 037 (BoK & Boundary Guardrails). *Primer untuk BoK sesuai Batas yang ditetapkan Dok 037; untuk beberapa MK core yang tidak dibahas eksplisit di klaster Dok 037, BoK dirujuk dari katalog BoK bagian 2 Dok 037 berdasarkan isi CPMK.*

---

## BAGIAN A — MATRIKS MK CORE PRODI (STI) PER SEMESTER

### A-1. SEMESTER 1

### 1. STI-101 — Pengantar Sistem dan Teknologi Informasi

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 1 / 2 SKS / Teori |
| **Rumpun MK** | Sistem Informasi & Tata Kelola |
| **Prasyarat** | - |
| **CPL yang Dibebankan** | `P2` (Konsep Sistem Informasi & Transformasi Digital) |
| **Bahan Kajian (BoK)** | `BK-IS01` Foundations of Information Systems & `BK-IS15` Digital Innovation and Entrepreneurship |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menguraikan** komponen pembentuk sistem informasi, siklus data-ke-informasi, dan perannya dalam organisasi (*B*) melalui studi kasus bisnis (*C*) secara komprehensif (*D*). | **C2** | `P2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **membandingkan** jenis-jenis sistem informasi enterprise (TPS, MIS, DSS, ERP, CRM, SCM) (*B*) pada ekosistem industri modern (*C*) dengan analisis komparasi yang valid (*D*). | **C4** | `P2` |
| **CPMK-3** | Mahasiswa (*A*) mampu **merumuskan** usulan solusi transformasi digital berbasis AI, Cloud, dan IoT (*B*) terhadap permasalahan proses bisnis konvensional (*C*) secara etis dan layak bisnis (*D*). | **C5** | `P2` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Konsep data-informasi-pengetahuan, komponen SI, sistem enterprise (TPS/MIS/DSS/ERP/CRM/SCM), transformasi digital (AI, Cloud, IoT), pengantar tata kelola TI & cybersecurity. |
| **OUT-OF-SCOPE** (dilarang) | Implementasi koding sistem / algoritma pemrograman terperinci; perancangan arsitektur cloud teknis; pentesting. |
| **Handoff Anchor** (titik transisi) | Memberi konteks bisnis & peta TI; menyerahkan pengembangan sistem ke FST-102/STI-306 dan fondasi infrastruktur ke STI-103. |

---

### 2. STI-102 — Kalkulus

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 1 / 3 SKS / Teori |
| **Rumpun MK** | Matematika & Sains Komputasi |
| **Prasyarat** | - |
| **CPL yang Dibebankan** | `P1` (Matematika Sains Komputasi & Fondasi AI) |
| **Bahan Kajian (BoK)** | `BK-IS10` Applied Mathematics and Logic & `BK-IT01` Information Technology Fundamentals |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menghitung** limit fungsi aljabar/transenden dan memeriksa kontinuitas (*B*) menggunakan kaidah kalkulus baku (*C*) secara teliti dan benar (*D*). | **C3** | `P1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menerapkan** konsep turunan fungsi multivariat dan gradien (*B*) pada permasalahan laju perubahan dan optimasi ekstremum (*C*) dengan prosedur matematis standar (*D*). | **C3** | `P1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menganalisis** permasalahan integral tentu dan tak tentu (*B*) menggunakan teknik substitusi dan integrasi parsial (*C*) untuk pemodelan fungsi komputasi (*D*). | **C4** | `P1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **merumuskan** aplikasi kalkulus diferensial-integral (*B*) pada algoritma optimasi penurunan gradien (Gradient Descent) dan luasan data (*C*) secara matematis (*D*). | **C4** | `P1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Limit, kontinuitas, turunan (univariat & multivariat), integral, aplikasi pada optimasi & Gradient Descent. |
| **OUT-OF-SCOPE** (dilarang) | Koding numerik; pembuktian aljabar abstrak; metode numerik diskrit (itu ranah STA-601). |
| **Handoff Anchor** (titik transisi) | Turunan/integral kontinu jadi dasar STI-205 (aljabar linear) dan STI-413 (ML); komputasi aproksimasi diserahkan ke STA-601. |

---

### 3. STI-103 — Arsitektur dan Organisasi Sistem Teknologi Informasi

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 1 / 3 SKS / Teori |
| **Rumpun MK** | Infrastruktur, Sistem & Komputasi Awan |
| **Prasyarat** | - |
| **CPL yang Dibebankan** | `P1` (Representasi Data Biner & Logika), `P3` (Arsitektur Perangkat Keras, Virtualisasi & Infrastruktur TI), `KU1` (Pemikiran Logis Rekayasa Sistem) |
| **Bahan Kajian (BoK)** | `BK-IS03` IT Infrastructure and Networking & `BK-IT01` Information Technology Fundamentals |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** representasi data biner, heksadesimal, floating point IEEE 754, dan siklus eksekusi instruksi Von Neumann (*B*) pada arsitektur prosesor (*C*) secara tepat dan akurat (*D*). | **C3** | `P1, P3` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menganalisis** rancangan rangkaian logika kombinasional dan sekuensial (*B*) menggunakan gerbang logika biner dan flip-flop (*C*) sebagai dasar operasi Arithmetic Logic Unit (ALU) (*D*). | **C4** | `P1, KU1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **membandingkan** karakteristik arsitektur prosesor CISC (x86_64) vs RISC (ARM64 / RISC-V), hirarki memori cache L1/L2/L3, dan akselerator komputasi GPU/NPU (*B*) dalam skenario beban kerja komputasi nyata (*C*) secara kritis (*D*). | **C4** | `P3, KU1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengevaluasi** mekanisme bus sistem, interupsi I/O, abstraksi virtualisasi hardware (Hypervisor), dan organisasi server data center (*B*) untuk mendukung infrastruktur cloud modern (*C*) secara komprehensif (*D*). | **C5** | `P3, KU1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Representasi biner/BL, gerbang logika, CPU (ALU/register), Fetch-Decode-Execute, hierarki memori & cache, I/O, virtualisasi hardware, arsitektur server data center. |
| **OUT-OF-SCOPE** (dilarang) | Logika predikat/aljabar relasi (STI-204); manajemen thread OS (STI-310); konfigurasi router (STI-312). |
| **Handoff Anchor** (titik transisi) | Memahami mesin fisik; menyerahkan manajemen perangkat lunak sistem ke STI-310 dan komunikasi data ke STI-312. |

---

### A-2. SEMESTER 2

### 4. STI-204 — Matematika Diskrit dan Logika

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 2 / 3 SKS / Teori |
| **Rumpun MK** | Matematika & Sains Komputasi |
| **Prasyarat** | STI-103 |
| **CPL yang Dibebankan** | `P1` (Fondasi Struktur Diskrit, Logika Komputasi & Graf), `KU1` (Penalaran Formal Kritis) |
| **Bahan Kajian (BoK)** | `BK-IS10` Applied Mathematics and Logic & `BK-IT01` Information Technology Fundamentals |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membuktikan** validitas argumen inferensi logika proposisi/predikat dan kebenaran algoritma (*B*) menggunakan tabel kebenaran, hukum aljabar logika, dan metode induksi matematika (*C*) secara runtut dan valid (*D*). | **C3** | `P1, KU1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menerapkan** konsep relasi ekuivalensi, himpunan terurut parsial (Poset), aljabar Boolean, dan kombinatorika (*B*) pada pemodelan struktur data dan logika query basis data (*C*) secara tepat (*D*). | **C3** | `P1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menganalisis** struktur Graf dan Pohon (Tree) (*B*) menggunakan matriks representasi (Adjacency Matrix) dan algoritma penelusuran lintasan (*C*) untuk optimasi jaringan data/komputer (*D*). | **C4** | `P1, KU1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengonstruksi** model otomata berhingga (Finite State Automata / FSA: DFA dan NFA) (*B*) untuk pengenalan pola bahasa formal dan transisi status sistem komputasi (*C*) secara akurat (*D*). | **C4** | `P1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Logika proposisi & predikat, tabel kebenaran, relasi, himpunan terurut, aljabar Boolean, kombinatorika, graf & pohon, FSA (DFA/NFA). |
| **OUT-OF-SCOPE** (dilarang) | Gerbang logika fisik/gerbang mikroprosesor (STI-103); kalkulus diferensial-integral kontinu. |
| **Handoff Anchor** (titik transisi) | Logika formal & struktur diskrit jadi fondasi STI-307 (Sistem Cerdas) dan STI-413. |

---

### 5. STI-205 — Aljabar Linear dan Matriks

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 2 / 3 SKS / Teori |
| **Rumpun MK** | Matematika & Sains Komputasi |
| **Prasyarat** | STI-102 |
| **CPL yang Dibebankan** | `P1` (Aljabar Linear, Ruang Vektor & Dekomposisi Matriks) |
| **Bahan Kajian (BoK)** | `BK-IS10` Applied Mathematics and Logic & `BK-IS18` Machine Learning and Data Science |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menyelesaikan** Sistem Persamaan Linear (SPL) (*B*) menggunakan eliminasi Gauss-Jordan dan matriks invers (*C*) secara tepat (*D*). | **C3** | `P1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menganalisis** struktur ruang vektor, kombinasi linier, kebebasan linier, basis, dan dimensi (*B*) pada ruang $\mathbb{R}^n$ (*C*) dengan kaidah aljabar formal (*D*). | **C4** | `P1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menghitung** nilai eigen (Eigenvalues), vektor eigen (Eigenvectors), dan diagonalisasi matriks (*B*) pada matriks transformasi linier (*C*) secara presisi (*D*). | **C3** | `P1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **merumuskan** dekomposisi matriks SVD (Singular Value Decomposition) dan reduksi dimensi PCA (*B*) menggunakan pustaka Python NumPy (*C*) untuk pemrosesan data AI (*D*). | **C4** | `P1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | SPL, eliminasi Gauss-Jordan, ruang vektor, basis & dimensi, nilai eigen, diagonalisasi, dekomposisi SVD & reduksi PCA (Python/NumPy). |
| **OUT-OF-SCOPE** (dilarang) | Koding numerik penuh untuk fungsi non-linier (STA-601); pemodelan dataset ML. |
| **Handoff Anchor** (titik transisi) | Matriks linear menjadi prasyarat STI-413 (ML) dan fondasi STA-601. |

---

### A-3. SEMESTER 3

### 6. STI-306 — Analisis dan Perancangan Sistem Informasi

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 3 / 3 SKS / Teori |
| **Rumpun MK** | Sistem Informasi & Tata Kelola |
| **Prasyarat** | STI-101, FST-207 |
| **CPL yang Dibebankan** | `P2` (Pemodelan Proses Bisnis & Data), `KU1` (Problem Solving Analitik) |
| **Bahan Kajian (BoK)** | `BK-IS07` Systems Analysis and Design & `BK-IS09` Business Process Management |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **mengelisitasi** kebutuhan fungsional dan non-fungsional perangkat lunak (*B*) dari pemangku kepentingan industri (*C*) dalam bentuk dokumen spesifikasi kebutuhan SRS IEEE 830 (*D*). | **C4** | `KU1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **memodelkan** alur proses bisnis organisasi (*B*) menggunakan standar notasi BPMN 2.0 (*C*) dengan analisis efisiensi proses As-Is vs To-Be (*D*). | **C4** | `P2` |
| **CPMK-3** | Mahasiswa (*A*) mampu **merancang** pemodelan berorientasi objek (Use Case, Activity, Class, Sequence, State Machine) (*B*) menggunakan Unified Modeling Language (UML 2.5) (*C*) secara konsisten (*D*). | **C4** | `P2` |
| **CPMK-4** | Mahasiswa (*A*) mampu **menyusun** dokumen arsitektur dan desain perangkat lunak komprehensif (SDD) (*B*) untuk persiapan implementasi teknis (*C*) secara profesional (*D*). | **C5** | `P2` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Elisitasi kebutuhan, BPMN 2.0, UML fungsional & struktural, dokumen SRS (IEEE 830). |
| **OUT-OF-SCOPE** (dilarang) | Koding aplikasi & unit testing (STI-309); estimasi biaya proyek (STI-523). |
| **Handoff Anchor** (titik transisi) | Cetak biru kebutuhan; menyerahkan konstruksi & pengujian ke STI-309, manajemen ke STI-523. |

---

### 7. STI-307 — Sistem Cerdas

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 3 / 2 SKS / Teori |
| **Rumpun MK** | Kecerdasan Artifisial |
| **Prasyarat** | STI-204, FST-204 |
| **CPL yang Dibebankan** | `P2` (Representasi Pengetahuan & Penalaran AI), `KK1` (Sistem Cerdas Bisnis) |
| **Bahan Kajian (BoK)** | `BK-IS16` Artificial Intelligence & Intelligent Systems & `BK-IT02` Applied AI & Intelligent Technologies |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** algoritma pencarian heuristic (A*, Greedy Best-First, Minimax) (*B*) pada permasalahan optimasi ruang status (*C*) dengan kompleksitas ruang/waktu terukur (*D*). | **C3** | `P2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang** sistem pakar (*Expert System*) dengan metode penalaran Forward Chaining dan Backward Chaining (*B*) berbasis basis aturan (*C*) secara logis dan konsisten (*D*). | **C4** | `P2, KK1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengimplementasikan** sistem inferensi logika fuzzy (Mamdani dan Sugeno) (*B*) untuk pengambilan keputusan dalam kondisi ketidakpastian (*C*) menggunakan Python Scikit-Fuzzy (*D*). | **C4** | `KK1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Pencarian heuristik (A*, Greedy, Minimax), knowledge representation, sistem pakar (forward/backward chaining), fuzzy inference. |
| **OUT-OF-SCOPE** (dilarang) | ML statistik / neural network / deep learning (STI-413/STI-626); agen otonom & MAS (STA-602). |
| **Handoff Anchor** (titik transisi) | Inferensi simbolik deterministik; menyerahkan ML probabilistik ke STI-413 dan NLP ke STI-414. |

---

### 8. STI-308 — UI/UX Design & Prototyping

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 3 / 3 SKS / +P |
| **Rumpun MK** | Interaksi Manusia-Komputer & UX |
| **Prasyarat** | FST-101 |
| **CPL yang Dibebankan** | `KK5` (Perancangan Antarmuka Pengguna & Pengalaman Pengguna Digital) |
| **Bahan Kajian (BoK)** | `BK-IS17` Human-Computer Interaction & UX & `BK-IT10` User Experience & Interaction Design |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **melakukan** riset pengguna (*User Research*) melalui wawancara, observasi, dan persona (*B*) menggunakan metodologi Design Thinking (*C*) dengan empati mendalam (*D*). | **C4** | `KK5` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang** arsitektur informasi, alur pengguna (*User Flow*), dan *Wireframe* (*B*) pada aplikasi web/mobile (*C*) secara terstruktur (*D*). | **C4** | `KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **membangun** purwarupa interaktif *High-Fidelity* dan *Design System* (*B*) menggunakan perangkat lunak Figma (*C*) dengan kepatuhan standar aksesibilitas WCAG (*D*). | **C6** | `KK5` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengevaluasi** kegunaan antarmuka (*Usability Testing*) (*B*) menggunakan System Usability Scale (SUS) dan Heuristic Evaluation (*C*) dengan analisis kuantitatif/kualitatif (*D*). | **C5** | `KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Teori warna, tipografi, prinsip Gestalt, arsitektur informasi, wireframe, prototyping Figma, usability testing dasar (SUS/10 heuristics). |
| **OUT-OF-SCOPE** (dilarang) | Riset pengguna kualitatif mendalam & A/B testing (STC-501); koding frontend (STI-311). |
| **Handoff Anchor** (titik transisi) | Purwarupa interaktif; menyerahkan riset ilmiah pengguna ke STC-501 dan frontend ke STI-311. |

---

### 9. STI-309 — Rekayasa Perangkat Lunak

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 3 / 3 SKS / Teori |
| **Rumpun MK** | Rekayasa Perangkat Lunak |
| **Prasyarat** | FST-203 |
| **CPL yang Dibebankan** | `P4` (Arsitektur Perangkat Lunak), `KK5` (Jaminan Kualitas & Pengujian Software) |
| **Bahan Kajian (BoK)** | `BK-IS07` Systems Analysis and Design & `BK-IT11` Software Development Practices |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **memilih** model proses pengembangan perangkat lunak (Waterfall, V-Model, Scrum, Kanban) (*B*) yang sesuai dengan karakteristik proyek industri (*C*) secara terjustifikasi (*D*). | **C4** | `P4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menerapkan** arsitektur perangkat lunak modular dan prinsip SOLID (*B*) pada perancangan subsistem software (*C*) dengan *coupling* rendah dan *cohesion* tinggi (*D*). | **C3** | `P4` |
| **CPMK-3** | Mahasiswa (*A*) mampu **merancang** skenario pengujian perangkat lunak White-Box (Basis Path, Cyclomatic Complexity) dan Black-Box (BVA, Equivalence Partitioning) (*B*) berdasarkan spesifikasi sistem (*C*) secara komprehensif (*D*). | **C4** | `KK5` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengevaluasi** kualitas perangkat lunak (*B*) berdasarkan standar ISO/IEC 25010 dan metrik pengujian otomatis (*C*) secara objektif (*D*). | **C5** | `KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Model proses (Waterfall, V-Model, Scrum), arsitektur perangkat lunak, design pattern & SOLID, SQA, unit/integration testing, ISO/IEC 25010. |
| **OUT-OF-SCOPE** (dilarang) | Elisitasi kebutuhan bisnis dari nol (STI-306); EVM & kontrak proyek (STI-523). |
| **Handoff Anchor** (titik transisi) | Menjamin kualitas kode; menyerahkan tata kelola jadwal/biaya ke STI-523. |

---

### 10. STI-310 — Sistem Operasi

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 3 / 3 SKS / Teori |
| **Rumpun MK** | Infrastruktur, Sistem & Komputasi Awan |
| **Prasyarat** | STI-103 |
| **CPL yang Dibebankan** | `P3` (Kernel OS, Konkurensi & Manajemen Memori), `KK3` (Infrastruktur Sistem) |
| **Bahan Kajian (BoK)** | `BK-IS03` IT Infrastructure and Networking & `BK-IT01` Information Technology Fundamentals |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menganalisis** siklus hidup proses, mekanisme thread, dan algoritma penjadwalan CPU (*B*) pada sistem multi-tasking (*C*) dengan perhitungan rata-rata waktu tunggu (*D*). | **C4** | `P3` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menyelesaikan** permasalahan sinkronisasi proses (Race Condition, Deadlock) (*B*) menggunakan Semaphore, Mutex, dan Algoritma Banker (*C*) secara matematis (*D*). | **C3** | `P3, KK3` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengevaluasi** kinerja manajemen memori virtual (Paging, Segmentasi, Page Replacement) dan alokasi sistem berkas (*B*) pada arsitektur sistem operasi modern (*C*) dengan analisis page fault minimum (*D*). | **C5** | `P3` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Kernel OS, proses & thread, CPU scheduling, sinkronisasi & deadlock, manajemen memori virtual, file system (Linux/POSIX). |
| **OUT-OF-SCOPE** (dilarang) | Gerbang logika fisik (STI-103); konfigurasi routing/IP (STI-312); deployment Kubernetes (STB-601). |
| **Handoff Anchor** (titik transisi) | Manajemen resource mesin lokal; menyerahkan interkoneksi antar-mesin ke STI-312. |

---

### 11. STI-311 — Web Front End Development

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 3 / 3 SKS / +P |
| **Rumpun MK** | Platform & Pengembangan Web/Mobile |
| **Prasyarat** | FST-102 |
| **CPL yang Dibebankan** | `P4` (Pemrograman Web Modern), `KK5` (Single Page Application / SPA) |
| **Bahan Kajian (BoK)** | `BK-IS12` Web and Mobile App Development & `BK-IT04` Platform Technologies & Web/Mobile |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membangun** struktur halaman web responsif multi-device (*B*) menggunakan HTML5 Semantik, CSS3 Flexbox/Grid, dan Variabel CSS (*C*) dengan tampilan estetik (*D*). | **C3** | `P4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** logika interaktivitas client-side (*B*) menggunakan JavaScript Modern (ES6+, DOM Manipulation, Async/Await, Fetch API) (*C*) secara modular (*D*). | **C3** | `P4` |
| **CPMK-3** | Mahasiswa (*A*) mampu **membangun** aplikasi Single Page Application (SPA) berbasis komponen (*B*) menggunakan framework React.js (Hooks, Context API, React Router) (*C*) dengan arsitektur state terpusat (*D*). | **C6** | `KK5` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengintegrasikan** aplikasi front-end dengan RESTful API eksternal (*B*) serta **mengoptimalkan** performa loading (*C*) dengan skor Google Lighthouse $\ge 85$ (*D*). | **C5** | `KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | HTML5/CSS3 (Flexbox, Grid), JavaScript ES6+ (DOM, Async/Await), SPA React (Hooks, Context), konsumsi REST API client-side. |
| **OUT-OF-SCOPE** (dilarang) | Koding server-side/koneksi DB (STI-416); backend business logic. |
| **Handoff Anchor** (titik transisi) | Antarmuka web interaktif; menyerahkan penyediaan data server-side ke STI-416. |

---

### 12. STI-312 — Jaringan Komputer

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 3 / 3 SKS / +P |
| **Rumpun MK** | Infrastruktur, Sistem & Komputasi Awan |
| **Prasyarat** | STI-103 |
| **CPL yang Dibebankan** | `P3` (Protokol Jaringan TCP/IP & Subnetting), `KK3` (Konfigurasi Switch/Router Enterprise) |
| **Bahan Kajian (BoK)** | `BK-IS03` IT Infrastructure and Networking & `BK-IT03` Networking & Communications |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **merancang** skema pengalamatan jaringan IPv4 (*B*) menggunakan teknik Variable Length Subnet Mask (VLSM) dan CIDR (*C*) dengan efisiensi alokasi IP optimal (*D*). | **C4** | `P3` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengonfigurasi** perangkat Switch dan Router (*B*) untuk implementasi VLAN, Trunking, dan Inter-VLAN Routing (*C*) menggunakan Cisco Packet Tracer (*D*). | **C3** | `KK3` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengimplementasikan** protokol routing dinamis OSPF (*B*) pada topologi jaringan multi-router (*C*) dengan tabel routing konvergen (*D*). | **C3** | `KK3` |
| **CPMK-4** | Mahasiswa (*A*) mampu **menganalisis** lalu lintas protokol lapisan aplikasi (HTTP, DNS, DHCP) dan keamanan Access Control List (ACL) (*B*) menggunakan Wireshark (*C*) secara kritis (*D*). | **C4** | `P3, KK3` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Model OSI & TCP/IP, subnetting VLSM/CIDR, IPv6, protokol transport, routing (OSPF), layanan jaringan (DNS/DHCP/NAT), ACL dasar. |
| **OUT-OF-SCOPE** (dilarang) | Manajemen memori OS (STI-310); konfigurasi cloud publik (STI-417); pentesting exploit (STI-519). |
| **Handoff Anchor** (titik transisi) | Komunikasi data jaringan; menyerahkan komputasi cloud ke STI-417 dan keamanan ke STI-418. |

---

### A-4. SEMESTER 4

### 13. STI-413 — Machine Learning

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 4 / 3 SKS / +P |
| **Rumpun MK** | Kecerdasan Artifisial |
| **Prasyarat** | STI-205, STI-307 |
| **CPL yang Dibebankan** | `P2` (Arsitektur Data & Model AI), `KK1` (Pelatihan & Evaluasi Model ML), `KK2` (Rekayasa Fitur) |
| **Bahan Kajian (BoK)** | `BK-IS18` Machine Learning and Data Science & `BK-IT02` Applied AI & Intelligent Technologies |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** alur kerja rekayasa data Machine Learning (EDA, Imputation, Encoding, Scaling) (*B*) menggunakan Python dan scikit-learn (*C*) bebas data leakage (*D*). | **C3** | `KK2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengonstruksi dan melatih** model pembelajaran terbimbing (Linear Regression, Logistic Regression, Decision Tree, Random Forest, SVM) (*B*) pada dataset tabular (*C*) dengan parameter optimal (*D*). | **C5** | `KK1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengonstruksi** model pembelajaran tak-terbimbing (K-Means, Hierarchical, PCA) (*B*) untuk segmentasi data dan reduksi dimensi (*C*) dengan validasi siluet yang valid (*D*). | **C5** | `P2, KK1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Data tabular & pipeline scikit-learn, regresi, decision tree, random forest, SVM, K-Means, PCA, hyperparameter tuning, metrik evaluasi. |
| **OUT-OF-SCOPE** (dilarang) | PyTorch/TensorFlow, CNN/RNN, deep learning (STI-626); sistem otonom BDI & teori permainan (STA-602). |
| **Handoff Anchor** (titik transisi) | Pemodelan data tabular klasik; menyerahkan data tak terstruktur (citra/sekuensial) ke STI-626. |

---

### 14. STI-414 — Pengantar NLP & Information Retrieval

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 4 / 2 SKS / +P |
| **Rumpun MK** | Kecerdasan Artifisial |
| **Prasyarat** | STI-307 |
| **CPL yang Dibebankan** | `KK1` (Perancangan Sistem Cerdas berbasis AI/NLP), `P2` (Konsep & Rekayasa SI Cerdas) |
| **Bahan Kajian (BoK)** | `BK-IS16` Artificial Intelligence & Intelligent Systems & `BK-IT02` Applied AI & Intelligent Technologies |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan tahapan pemrosesan awal teks** (*Text Preprocessing: tokenisasi, normalisasi, stopword removal, stemming/lemmatisasi*) (*B*) pada korpus teks bahasa alami (*C*) secara akurat (*D*). | **C3** | `KK1, P2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menganalisis dan membangun model representasi teks serta sistem temu balik informasi** (*Information Retrieval: TF-IDF, Vector Space Model, BM25, Inverted Index*) (*B*) untuk pencarian dokumen relevan (*C*) dengan presisi dan recall terukur (*D*). | **C4** | `KK1, P2` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengembangkan model klasifikasi teks dan analisis sentimen** (*B*) menggunakan teknik machine learning dan word embedding (*Word2Vec, FastText*) (*C*) dengan metrik F1-score optimal (*D*). | **C4** | `KK1, P2` |
| **CPMK-4** | Mahasiswa (*A*) mampu **merancang purwarupa aplikasi pemrosesan bahasa alami atau mesin pencari cerdas** (*B*) dengan mengintegrasikan API/library NLP modern (*HuggingFace / spaCy / NLTK*) (*C*) sebagai solusi cerdas kebutuhan pengguna (*D*). | **C5** | `KK1, P2` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Text preprocessing, VSM, TF-IDF, N-Gram, BM25, evaluasi IR, Word2Vec/GloVe dasar, klasifikasi teks klasik (Naive Bayes, SVM teks). |
| **OUT-OF-SCOPE** (dilarang) | Transformer mendalam/LLM, RAG, LangChain (STA-702). |
| **Handoff Anchor** (titik transisi) | Representasi matematis teks & pencarian dokumen; menyerahkan bahasa generatif ke STA-702. |

---

### 15. STI-415 — Data Warehouse & Business Intelligence

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 4 / 3 SKS / +P |
| **Rumpun MK** | Data Management & Analitik |
| **Prasyarat** | FST-207 |
| **CPL yang Dibebankan** | `P2` (Pemodelan Dimensi & Arsitektur DWH), `KK2` (Pipeline ETL & Dashboard BI) |
| **Bahan Kajian (BoK)** | `BK-IS02` Data and Information Management & `BK-IS13` Data Analytics and Business Intelligence |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **merancang** skema multidimensi Data Warehouse (Star Schema, Snowflake Schema) (*B*) berdasarkan proses bisnis organisasi (*C*) dengan penanganan Slowly Changing Dimensions (SCD) yang tepat (*D*). | **C4** | `P2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **membangun** pipeline Extract-Transform-Load (ETL) otomatis (*B*) menggunakan software integrasi data (Pentaho/Airflow) (*C*) dengan data cleaning yang valid (*D*). | **C6** | `KK2` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengimplementasikan** operasi kubus data OLAP dan kueri analitik tingkat lanjut (*B*) menggunakan SQL Window Functions (*C*) secara optimal (*D*). | **C3** | `P2` |
| **CPMK-4** | Mahasiswa (*A*) mampu **membangun** dashboard Business Intelligence eksekutif interaktif (*B*) menggunakan Power BI / Tableau (*C*) dengan visualisasi KPI yang komunikatif (*D*). | **C6** | `KK2` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Arsitektur DWH Kimball, star/snowflake schema, fact & dimension, SCD, pipeline ETL, OLAP, dashboard BI (Power BI/Tableau). |
| **OUT-OF-SCOPE** (dilarang) | Normalisasi 3NF OLTP (FST-207); association rule mining & klastering tingkat lanjut (STI-520). |
| **Handoff Anchor** (titik transisi) | Data multidimensional & KPI; menyerahkan penemuan pola tersembunyi ke STI-520. |

---

### 16. STI-416 — Web Back End Development

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 4 / 3 SKS / +P |
| **Rumpun MK** | Platform & Pengembangan Web/Mobile |
| **Prasyarat** | FST-207, STI-311 |
| **CPL yang Dibebankan** | `P4` (Arsitektur RESTful API & Keamanan Server), `KK5` (Backend Engineering & ORM) |
| **Bahan Kajian (BoK)** | `BK-IS12` Web and Mobile App Development & `BK-IT04` Platform Technologies & Web/Mobile |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membangun** RESTful API modular (*B*) menggunakan Node.js/Express atau Python FastAPI (*C*) dengan penanganan rute, middleware, dan sanitasi input yang aman (*D*). | **C3** | `P4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengintegrasikan** backend API dengan database relasional/NoSQL (*B*) menggunakan Object-Relational Mapping (ORM/ODM) (*C*) dengan operasi CRUD transaksional (*D*). | **C3** | `KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengimplementasikan** sistem autentikasi dan otorisasi (*B*) berbasis JSON Web Token (JWT) dan Role-Based Access Control (RBAC) (*C*) dengan enkripsi password Bcrypt (*D*). | **C4** | `P4, KK5` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mendokumentasikan** API menggunakan Swagger/OpenAPI serta **mendeploy** backend (*B*) ke server cloud dengan kontainer Docker (*C*) secara andal (*D*). | **C6** | `KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Arsitektur server-side, RESTful API design, JWT & RBAC, ORM/ODM, session & caching dasar (Redis), validasi input, dokumentasi Swagger/OpenAPI, deploy kontainer. |
| **OUT-OF-SCOPE** (dilarang) | Layout CSS/HTML (STI-311); message broker skala besar (STI-627); frontend mobile (STI-522). |
| **Handoff Anchor** (titik transisi) | Layanan backend modular; menyerahkan aksesibilitas mobile ke STI-522 dan skalabilitas terdistribusi ke STI-627. |

---

### 17. STI-417 — Komputasi Awan (Cloud Computing)

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 4 / 3 SKS / Teori |
| **Rumpun MK** | Infrastruktur, Sistem & Komputasi Awan |
| **Prasyarat** | STI-312, STI-310 |
| **CPL yang Dibebankan** | `P3` (Arsitektur Cloud & Virtualisasi), `KK3` (Orkestrasi Kontainer & Skalabilitas) |
| **Bahan Kajian (BoK)** | `BK-IS19` Cloud Architecture & DevOps & `BK-IT05` Cloud Computing & Virtualization |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membandingkan** model layanan cloud (IaaS, PaaS, SaaS, FaaS) dan model deployment (*B*) pada penyedia cloud publik (AWS/GCP/Azure) (*C*) secara kritis (*D*). | **C4** | `P3` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang dan mengemas** aplikasi ke dalam kontainer (*B*) menggunakan Dockerfile dan Docker Compose (*C*) dengan *layer caching* yang efisien (*D*). | **C4** | `P3, KK3` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengonfigurasi** arsitektur jaringan Virtual Private Cloud (VPC), Subnetting, Security Group, dan IAM (*B*) pada infrastruktur cloud (*C*) dengan standar keamanan ketat (*D*). | **C3** | `KK3` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengevaluasi** arsitektur sistem cloud berskala besar (*B*) dengan Load Balancing, Auto-Scaling, dan toleransi bencana (*High Availability*) (*C*) secara terstruktur (*D*). | **C5** | `P3, KK3` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Model layanan IaaS/PaaS/SaaS/FaaS, virtualisasi & hypervisor, provisi VM, object storage, VPC dasar, kontainer Docker mandiri. |
| **OUT-OF-SCOPE** (dilarang) | Orkestrasi Kubernetes multi-node, Terraform IaC enterprise, CI/CD GitOps (STB-601). |
| **Handoff Anchor** (titik transisi) | Fondasi provisi cloud; menyerahkan automasi & orkestrasi skala besar ke STB-601. |

---

### 18. STI-418 — Dasar Keamanan Informasi

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 4 / 2 SKS / Teori |
| **Rumpun MK** | Keamanan Informasi & Tata Kelola |
| **Prasyarat** | STI-312 |
| **CPL yang Dibebankan** | `P3` (Prinsip Keamanan CIA & Kriptografi), `KK3` (Mitigasi Kerentanan Sistem) |
| **Bahan Kajian (BoK)** | `BK-IS06` Information Security and Risk Management & `BK-IT06` Cybersecurity Principles & Defense |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** algoritma kriptografi simetris (AES), asimetris (RSA), fungsi hash (SHA-256), dan digital signature (*B*) pada proteksi data (*C*) secara matematis (*D*). | **C3** | `P3` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menganalisis** kerentanan aplikasi web dan sistem (*B*) berdasarkan metodologi OWASP Top 10 (*C*) menggunakan alat bantu pemindai kerentanan (*D*). | **C4** | `KK3` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengevaluasi** insiden keamanan siber (*B*) menggunakan kerangka kerja NIST Cybersecurity Framework dan ISO/IEC 27001 (*C*) dengan rencana mitigasi yang tepat (*D*). | **C5** | `P3, KK3` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | CIA Triad, kriptografi simetris/asimetris & hashing, digital signature, kontrol akses (RBAC), OWASP Top 10 dasar, kerangka NIST CSF & ISO 27001 pengantar. |
| **OUT-OF-SCOPE** (dilarang) | Hacking exploit web aktif, forensik memori lanjut, audit COBIT formal (STB-701); pertahanan teknis jaringan (STB-501). |
| **Handoff Anchor** (titik transisi) | Prinsip keamanan; menyerahkan pertahanan jaringan ke STB-501 dan keamanan aplikasi/pentest ke STI-519. |

---

### A-5. SEMESTER 5

### 19. STI-519 — Keamanan Informasi Lanjut

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 5 / 3 SKS / Teori |
| **Rumpun MK** | Keamanan Informasi & Tata Kelola |
| **Prasyarat** | STI-418 |
| **CPL yang Dibebankan** | `P3` (Audit Keamanan ISO 27001), `KK3` (Manajemen Risiko Siber), `KK4` (Uji Penetrasi Sistem) |
| **Bahan Kajian (BoK)** | `BK-IS06` Information Security and Risk Management & `BK-IT06` Cybersecurity Principles & Defense |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **merancang dan mengeksekusi** tahapan uji penetrasi keamanan (*Penetration Testing*) (*B*) sesuai standar PTES dan MITRE ATT&CK (*C*) dengan etika *Red Teaming* profesional (*D*). | **C4** | `KK4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **melakukan** audit sistem manajemen keamanan informasi (*B*) berdasarkan klausul dan kontrol keamanan ISO/IEC 27001:2022 (*C*) dalam bentuk dokumen Statement of Applicability (SoA) (*D*). | **C4** | `P3, KK3` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menyusun** rencana tanggap insiden (*Incident Response Plan*) dan melakukan analisis forensik digital dasar (*B*) pada kasus insiden kebocoran data (*C*) secara terstruktur (*D*). | **C5** | `KK3, KK4` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Penetration testing (PTES, MITRE ATT&CK), vulnerability assessment (OpenVAS/Nessus), OWASP Top 10, BurpSuite, reverse engineering dasar (Ghidra), incident response, audit ISO/IEC 27001. |
| **OUT-OF-SCOPE** (dilarang) | Konfigurasi subnetting router (STI-312); analisis risiko finansial organisasi & BCP/DRP (STB-602). |
| **Handoff Anchor** (titik transisi) | Menjamin perangkat lunak prodi bebas celah keamanan kritikal; fokus layer aplikasi (Layer 7). |

---

### 20. STI-520 — Data Mining & Visualisasi Data

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 5 / 3 SKS / +P |
| **Rumpun MK** | Data Management & Analitik |
| **Prasyarat** | STI-413, STI-415 |
| **CPL yang Dibebankan** | `P2` (Analitik Pola Bisnis), `KK2` (Algoritma Asosiasi, Klastering & Data Storytelling) |
| **Bahan Kajian (BoK)** | `BK-IS02` Data and Information Management & `BK-IS13` Data Analytics and Business Intelligence |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** algoritma penambangan aturan asosiasi (Apriori, FP-Growth) (*B*) pada data transaksi belanja (*C*) dengan analisis Support, Confidence, dan Lift Ratio yang valid (*D*). | **C3** | `KK2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** algoritma klastering tingkat lanjut (DBSCAN, Hierarchical Clustering) (*B*) pada data spasial/multivariat (*C*) dengan evaluasi skor Davies-Bouldin (*D*). | **C4** | `KK2` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mendeteksi** anomali dan pencilan (*Outliers*) (*B*) menggunakan algoritma Isolation Forest dan Local Outlier Factor (*C*) secara akurat (*D*). | **C4** | `P2, KK2` |
| **CPMK-4** | Mahasiswa (*A*) mampu **merancang** visualisasi data interaktif dan narasi wawasan bisnis (*Data Storytelling*) (*B*) menggunakan Python Plotly/Seaborn (*C*) secara estetik dan komunikatif (*D*). | **C6** | `KK2` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | CRISP-DM, EDA, association rule (Apriori, FP-Growth), klastering lanjut (DBSCAN, Hierarchical), deteksi outlier (Isolation Forest, LOF), visualisasi interaktif (Plotly, Seaborn), PCA/t-SNE. |
| **OUT-OF-SCOPE** (dilarang) | Query SQL dasar & desain tabel relasional (FST-207); dashboard KPI eksekutif statis (STI-415). |
| **Handoff Anchor** (titik transisi) | Menemukan pola dari data historis yang sudah diorganisasi di FST-207/STI-415. |

---

### 21. STI-521 — Internet of Things (IoT)

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 5 / 3 SKS / +P |
| **Rumpun MK** | IoT & Sistem Tertanam |
| **Prasyarat** | STI-312, STI-310 |
| **CPL yang Dibebankan** | `P3` (Protokol Komunikasi IoT & Telemetri), `KK3` (Perangkat Keras ESP32, MQTT & Cloud IoT) |
| **Bahan Kajian (BoK)** | `BK-IS03` IT Infrastructure and Networking & `BK-IT14` IoT and Embedded Smart Systems |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **memprogram** mikrokontroler ESP32 (*B*) untuk membaca sensor analog/digital dan mengendalikan aktuator (*C*) menggunakan antarmuka GPIO/I2C/SPI (*D*). | **C3** | `KK3` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** protokol telemetri IoT berkecepatan tinggi (MQTT) (*B*) menggunakan broker Mosquitto (*C*) dengan QoS dan enkripsi payload yang andal (*D*). | **C3** | `P3, KK3` |
| **CPMK-3** | Mahasiswa (*A*) mampu **merancang** alur otomasi middleware (*B*) menggunakan Node-RED (*C*) untuk pemrosesan logika data sensor secara real-time (*D*). | **C4** | `KK3` |
| **CPMK-4** | Mahasiswa (*A*) mampu **membangun** purwarupa produk IoT cerdas (*B*) yang terhubung ke dashboard cloud (ThingsBoard/Blynk) dan database time-series (*C*) secara terintegrasi (*D*). | **C6** | `KK3` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Pemrograman ESP32, sensor analog/digital & aktuator, MQTT (Mosquitto), Node-RED, dashboard cloud IoT (ThingsBoard/Blynk), time-series DB. |
| **OUT-OF-SCOPE** (dilarang) | Deep learning video streaming CCTV / AI vision (STA-703); analitik video; perangkat keras edge AI. |
| **Handoff Anchor** (titik transisi) | Dasar pengumpulan & transmisi data sensor; menyerahkan AI vision edge ke STA-703. |

---

### 22. STI-522 — Pemrograman Aplikasi Mobile

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 5 / 3 SKS / +P |
| **Rumpun MK** | Platform & Pengembangan Web/Mobile |
| **Prasyarat** | STI-311, STI-416 |
| **CPL yang Dibebankan** | `P4` (Arsitektur Mobile Multi-Platform), `KK5` (State Management BLoC & API Integrasi) |
| **Bahan Kajian (BoK)** | `BK-IS12` Web and Mobile App Development & `BK-IT04` Platform Technologies & Web/Mobile |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membangun** antarmuka aplikasi mobile responsif multi-device (*B*) menggunakan framework Flutter dan bahasa Dart (*C*) dengan prinsip Material Design 3 (*D*). | **C3** | `P4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** arsitektur state management yang scalable (*B*) menggunakan Business Logic Component (BLoC) Pattern (*C*) secara terstruktur (*D*). | **C4** | `KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengintegrasikan** persistensi data lokal (SQLite/SharedPreferences) dan sinkronisasi RESTful API (*B*) pada aplikasi mobile (*C*) dengan penanganan offline-mode yang andal (*D*). | **C4** | `KK5` |
| **CPMK-4** | Mahasiswa (*A*) mampu **membangun dan merilis** aplikasi mobile (*B*) dengan integrasi sensor perangkat keras (Kamera, GPS Geolocation) dan push notification Firebase (*C*) ke dalam paket APK/AAB rilis (*D*). | **C6** | `KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Flutter/Dart, lifecycle, UI widget, sensor perangkat (GPS, kamera, push), SQLite/Hive, sinkronisasi offline-to-online via REST API, rilis aplikasi. |
| **OUT-OF-SCOPE** (dilarang) | Membangun backend dari awal (konsumsi API dari STI-416); arsitektur server-side. |
| **Handoff Anchor** (titik transisi) | Aplikasi mobile siap rilis; mengkonsumsi API backend yang disediakan STI-416. |

---

### 23. STI-523 — Manajemen Proyek TI

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 5 / 3 SKS / Teori |
| **Rumpun MK** | Sistem Informasi & Tata Kelola |
| **Prasyarat** | STI-306, STI-309 |
| **CPL yang Dibebankan** | `KK6` (Perencanaan Ruang Lingkup, Penjadwalan & Pengendalian Biaya Proyek TI) |
| **Bahan Kajian (BoK)** | `BK-IS08` Project Management & `BK-IT08` IT Service Management & Governance |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **merumuskan** Project Charter, struktur rincian kerja (Work Breakdown Structure / WBS), dan matriks stakeholder (*B*) berdasarkan standar PMBOK v7 (*C*) secara komprehensif (*D*). | **C4** | `KK6` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menyusun** jadwal proyek realistis (*B*) menggunakan Critical Path Method (CPM) dan estimasi tiga titik PERT (*C*) dengan alokasi sumber daya optimal (*D*). | **C4** | `KK6` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menerapkan** metodologi Agile Project Management (*B*) menggunakan kerangka kerja Scrum dan perangkat lunak Jira (*C*) untuk pengelolaan sprint tim (*D*). | **C3** | `KK6` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengendalikan** kinerja proyek (*B*) menggunakan analisis Earned Value Management (EVM: CPI, SPI, EAC) dan mitigasi risiko (*C*) secara akurat (*D*). | **C5** | `KK6` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Project Charter, WBS, estimasi (COCOMO II, PERT), CPM, Gantt, agile Scrum (sprint, daily, review, retrospective), Jira, manajemen risiko, Earned Value Management (CPI/SPI/EAC). |
| **OUT-OF-SCOPE** (dilarang) | Koding aplikasi & testing perangkat lunak (STI-309); strategi discovery pasar & metrik produk (STC-703). |
| **Handoff Anchor** (titik transisi) | Tata kelola jadwal/biaya/sumber daya; menyerahkan kesuksesan pasar produk ke STC-703. |

---

### A-6. SEMESTER 6

### 24. STI-624 — Integrasi Layanan Cerdas Berbasis AI

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 3 SKS / +P |
| **Rumpun MK** | Kecerdasan Artifisial |
| **Prasyarat** | STI-413, STI-416 |
| **CPL yang Dibebankan** | `P2` (Arsitektur AI-as-a-Service), `KK1` (Model Serving, RAG, & Vektor Database) |
| **Bahan Kajian (BoK)** | `BK-IS19` Cloud Architecture & DevOps & `BK-IT02` Applied AI & Intelligent Technologies |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **mengoptimalkan dan mengonversi** model deep learning terlatih (*B*) ke format ONNX dan TensorRT (*C*) untuk inferensi berlatensi rendah (*D*). | **C4** | `KK1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **membangun** RESTful / gRPC Inference Service asinkron (*B*) menggunakan framework FastAPI dan kontainer Docker (*C*) dengan throughput tinggi (*D*). | **C6** | `P2, KK1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **merancang dan mengintegrasikan** sistem Retrieval-Augmented Generation (RAG) (*B*) menggunakan Vector Database (Milvus/Chroma) dan Large Language Models (LLM API) (*C*) secara akurat dan minim halusinasi (*D*). | **C6** | `KK1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengevaluasi** performa layanan AI (*B*) dengan pengujian beban (*Load Testing* Locust), monitoring latensi, dan pertahanan terhadap prompt injection (*C*) secara kritis (*D*). | **C5** | `KK1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Konversi model ke ONNX/TensorRT, RESTful/gRPC inference service, kontainerisasi model, RAG & vector database, load testing, monitoring laten. |
| **OUT-OF-SCOPE** (dilarang) | Riset/training arsitektur deep learning dari nol (STI-626); pengaturan lifecycle MLOps penuh & CI/CD/CT (STA-701). |
| **Handoff Anchor** (titik transisi) | Mengoperasikan layanan AI; menyerahkan otomasi lifecycle & monitoring drift produksi ke STA-701. |

---

### 25. STI-625 — Smart City & Pemerintahan Digital

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 2 SKS / Teori |
| **Rumpun MK** | Sistem Informasi & Tata Kelola |
| **Prasyarat** | STI-521 |
| **CPL yang Dibebankan** | `P3` (Infrastruktur Kota Cerdas & Arsitektur SPBE), `KK3` (Integrasi GIS & Telemetri Perkotaan) |
| **Bahan Kajian (BoK)** | `BK-IS04` Enterprise Architecture & `BK-IS03` IT Infrastructure and Networking |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menganalisis** arsitektur enterprise Sistem Pemerintahan Berbasis Elektronik (SPBE) (*B*) berdasarkan regulasi nasional Perpres No. 95/2018 (*C*) dengan pemetaan 6 domain SPBE (*D*). | **C4** | `P3` |
| **CPMK-2** | Mahasiswa (*A*) mampu **membangun** peta digital perkotaan interaktif (*B*) menggunakan Web GIS (Leaflet/Mapbox) dan integrasi sensor telemetri perkotaan (*C*) secara visual dan fungsional (*D*). | **C6** | `KK3` |
| **CPMK-3** | Mahasiswa (*A*) mampu **merancang** skema interoperabilitas data publik (*B*) berdasarkan prinsip Satu Data Indonesia dan RESTful API SPBE (*C*) dengan keamanan terstandar (*D*). | **C4** | `P3, KK3` |
| **CPMK-4** | Mahasiswa (*A*) mampu **menyusun** masterplan dan purwarupa sistem layanan publik cerdas (*B*) pada salah satu pilar Smart City (*C*) secara komprehensif (*D*). | **C6** | `P3, KK3` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Arsitektur SPBE (Perpres), Web GIS (Leaflet/Mapbox), telemetri perkotaan, interoperabilitas data (Satu Data Indonesia), masterplan smart city. |
| **OUT-OF-SCOPE** (dilarang) | CeT blueprint TOGAF korporasi multi-layer (STB-703); kebijakan perda tata ruang. |
| **Handoff Anchor** (titik transisi) | Domain pemerintahan publik; menyerahkan arsitektur enterprise korporat ke STB-703. |

---

### 26. STI-626 — Deep Learning & Neural Networks

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 3 SKS / +P |
| **Rumpun MK** | Kecerdasan Artifisial |
| **Prasyarat** | STI-413 |
| **CPL yang Dibebankan** | `KK1` (Pemodelan Deep Learning Vision & NLP), `KK2` (Rekayasa Dataset Citra & Teks) |
| **Bahan Kajian (BoK)** | `BK-IS18` Machine Learning and Data Science & `BK-IT02` Applied AI & Intelligent Technologies |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **mengonstruksi** arsitektur Multi-Layer Perceptron (MLP) dan mengimplementasikan algoritma Backpropagation (*B*) menggunakan framework PyTorch (*C*) secara matematis dan modular (*D*). | **C3** | `KK1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang, melatih, dan mengevaluasi** model Convolutional Neural Networks (CNN) dan arsitektur transfer learning (ResNet, VGG) (*B*) untuk klasifikasi citra medis/industri (*C*) dengan akurasi terukur (*D*). | **C5** | `KK1, KK2` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengonstruksi** model sekuensial (LSTM, GRU, Transformer Self-Attention) (*B*) untuk pemrosesan bahasa alami atau prediksi runtun waktu (*C*) dengan konvergensi loss yang stabil (*D*). | **C5** | `KK1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **membangun** aplikasi deep learning terpadu (*B*) dengan teknik regularisasi (Dropout, Batch Normalization) dan optimasi akselerasi GPU (*C*) secara andal (*D*). | **C6** | `KK1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | MLP & backpropagation, CNN (ResNet, VGG), transfer learning, object detection (YOLO), RNN/LSTM/GRU, Transformer self-attention, regularisasi, optimasi akselerasi. |
| **OUT-OF-SCOPE** (dilarang) | Mengulang regresi linier/decision tree (STI-413); deployment Kubernetes, CI/CD, monitoring drift (STA-701). |
| **Handoff Anchor** (titik transisi) | Menghasilkan bobot model teroptimasi; menyerahkan otomasi lifecycle & deployment ke STA-701. |

---

### 27. STI-627 — Digital Platform Engineering

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 3 SKS / +P |
| **Rumpun MK** | Platform & Pengembangan Web/Mobile |
| **Prasyarat** | STI-416 |
| **CPL yang Dibebankan** | `P4` (Arsitektur Microservices & Event Streaming), `KK5` (Platform Engineering & CI/CD Pipeline) |
| **Bahan Kajian (BoK)** | `BK-IS12` Web and Mobile App Development & `BK-IT07` System Integration and Architecture |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **merancang** arsitektur sistem berbasis layanan mikro (*Microservices Architecture*) (*B*) menggunakan prinsip Domain-Driven Design (DDD) (*C*) dengan batas layanan (*Bounded Context*) yang tepat (*D*). | **C4** | `P4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** komunikasi antar-layanan asinkron (*B*) menggunakan message streaming Apache Kafka / RabbitMQ (*C*) dengan penanganan jaminan pengiriman pesan (*D*). | **C3** | `KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengonfigurasi** API Gateway, Service Discovery, dan pola ketahanan sistem (Circuit Breaker, Saga Pattern) (*B*) pada klaster platform (*C*) untuk skalabilitas tinggi (*D*). | **C4** | `P4, KK5` |
| **CPMK-4** | Mahasiswa (*A*) mampu **membangun** pipeline Continuous Integration / Continuous Deployment (CI/CD) otomatis (*B*) menggunakan GitHub Actions dan observability distributed tracing (*C*) secara terintegrasi (*D*). | **C6** | `KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Microservices & DDD, event-driven, message broker (Kafka/RabbitMQ), API Gateway, circuit breaker, Saga, containerization, CI/CD pipeline, observability. |
| **OUT-OF-SCOPE** (dilarang) | Koding CRUD sederhana (STI-416); tata kelola multitenansi bisnis (STC-702). |
| **Handoff Anchor** (titik transisi) | Platform digital terdistribusi; menyerahkan multitenansi & monetisasi SaaS ke STC-702. |

---

### A-7. SEMESTER 7

### 28. STI-728 — Inovasi Teknologi dan Startup Digital

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / +P |
| **Rumpun MK** | Digital Innovation & Entrepreneurship |
| **Prasyarat** | STI-627, MKU-204 |
| **CPL yang Dibebankan** | `KK6` (Inovasi Produk Digital, Lean Startup, Validasi MVP & Pitching) |
| **Bahan Kajian (BoK)** | `BK-IS15` Digital Innovation and Entrepreneurship & `BK-IT13` Technology Entrepreneurship |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **melakukan** validasi problem-solusi (*Problem-Solution Fit*) (*B*) menggunakan metodologi Lean Startup dan wawancara pengguna awal (*C*) secara empiris (*D*). | **C4** | `KK6` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang dan membangun** Minimum Viable Product (MVP) fungsional (*B*) berbasis solusi teknologi cerdas (AI/Platform/IoT) (*C*) dengan siklus Build-Measure-Learn yang cepat (*D*). | **C6** | `KK6` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menganalisis** metrik pertumbuhan startup (AARRR Pirate Metrics, CAC, LTV, Burn Rate) (*B*) pada dashboard analitik produk (*C*) secara kuantitatif (*D*). | **C4** | `KK6` |
| **CPMK-4** | Mahasiswa (*A*) mampu **menyusun** Investor Pitch Deck 10-slide dan mempresentasikannya (*B*) di hadapan panel investor/penguji pada ajang Demo Day (*C*) secara persuasif dan profesional (*D*). | **C6** | `KK6` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Lean Startup, problem-solution fit, MVP fungsional, metrik pertumbuhan (AARRR, CAC, LTV, Burn Rate), investor pitch deck, Demo Day. |
| **OUT-OF-SCOPE** (dilarang) | Implementasi teknis deep learning/MVP rekayasa (STI-626/STI-627); desain UI (STI-308). |
| **Handoff Anchor** (titik transisi) | Memvalidasi kejelasan pasar bisnis & pitching; startup yang dibina menjadi wadah penerapan capstone/PKL (Capstone FSTI, PKL). |

---

## BAGIAN B — MATRIKS MK PEMINATAN PER SEMESTER

### B-5. SEMESTER 5

### 29. STA-501 — Decision Support Systems

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 5 / 3 SKS / +P |
| **Rumpun MK** | P1 Integrated Smart Systems |
| **Prasyarat** | STI-307 |
| **CPL yang Dibebankan** | `P2` (Teori Pengambilan Keputusan), `KK1` (Sistem Cerdas Bisnis), `KK2` (Analitik Multi-Kriteria) |
| **Bahan Kajian (BoK)** | `BK-IS13` Data Analytics and Business Intelligence & `BK-IS16` Artificial Intelligence & Intelligent Systems & `BK-IT09` Data Analytics & Information Visualization |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** metode pengambilan keputusan multi-kriteria klasik (SAW, WP, AHP) (*B*) pada kasus pemilihan alternatif bisnis (*C*) dengan uji konsistensi rasio $CR \le 0.1$ (*D*). | **C3** | `P2, KK1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** metode perankingan tingkat lanjut (TOPSIS, PROMETHEE, Fuzzy AHP) (*B*) dalam kode program Python (*C*) secara tepat (*D*). | **C4** | `KK1, KK2` |
| **CPMK-3** | Mahasiswa (*A*) mampu **membangun** aplikasi berbasis web Decision Support Systems interaktif (*B*) dengan visualisasi perbandingan alternatif dan analisis sensitivitas (*C*) secara terintegrasi (*D*). | **C6** | `KK1, KK2` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Pengambilan keputusan multikriteria (SAW, WP, AHP, TOPSIS, PROMETHEE, Fuzzy AHP), uji konsistensi (CR), aplikasi web DSS interaktif, analisis sensitivitas. |
| **OUT-OF-SCOPE** (dilarang) | Pemodelan ML regresi/klasifikasi data (STI-413); penyajian BI atur dimensi (STI-415). |
| **Handoff Anchor** (titik transisi) | Menyerahkan perangkingan alternatif keputusan bisnis; tidak mempelajari desain ML (STI-413). |

---

### 30. STB-501 — Network Security and Digital Forensics

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 5 / 3 SKS / +P |
| **Rumpun MK** | P2 Cloud Infra & Cybersecurity |
| **Prasyarat** | STI-312, STI-418 |
| **CPL yang Dibebankan** | `P3` (Pertahanan Jaringan & IDS/IPS), `KK3` (Hardening Sistem), `KK4` (Forensik Digital & Bukti Siber) |
| **Bahan Kajian (BoK)** | `BK-IS06` Information Security and Risk Management & `BK-IT06` Cybersecurity Principles & Defense |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **mengonfigurasi dan menyusun aturan** (*Rules*) Intrusion Detection / Prevention Systems (Snort / Suricata) (*B*) untuk mendeteksi serangan port scan, DoS, dan eksploitasi jaringan (*C*) secara akurat (*D*). | **C4** | `P3, KK3` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menganalisis** bukti transfer data mencurigakan dan jejak eksfiltrasi (*B*) melalui analisis lalu lintas paket jaringan (PCAP) menggunakan Wireshark/Zeek (*C*) secara kritis (*D*). | **C4** | `KK4` |
| **CPMK-3** | Mahasiswa (*A*) mampu **melakukan** akuisisi bukti digital (*Bit-Stream Image*) dan analisis forensik memori/disk (*B*) menggunakan Autopsy dan Volatility (*C*) sesuai prinsip Chain of Custody (*D*). | **C5** | `KK4` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | IDS/IPS (Snort, Suricata), analisis PCAP (Wireshark, Zeek), akuisisi bukti digital (bit-stream image), forensik memori/disk (Autopsy, Volatility), chain of custody. |
| **OUT-OF-SCOPE** (dilarang) | Pentest aplikasi web Layer 7 (STI-519); audit kepatuhan COBIT formal (STB-701). |
| **Handoff Anchor** (titik transisi) | Pertahanan & investigasi jaringan; menyerahkan insiden aplikasi aplikatif ke STI-519. |

---

### 31. STC-501 — User Experience Research & Design

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 5 / 3 SKS / +P |
| **Rumpun MK** | P3 Digital Platform Engineering |
| **Prasyarat** | STI-308 |
| **CPL yang Dibebankan** | `P4` (Arsitektur Informasi & Aksesibilitas), `KK5` (Riset UX Kuantitatif/Kualitatif & A/B Testing) |
| **Bahan Kajian (BoK)** | `BK-IS17` Human-Computer Interaction & UX & `BK-IT10` User Experience & Interaction Design |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **merancang dan mengeksekusi** metode riset pengguna kuantitatif dan kualitatif (Card Sorting, Tree Testing, Contextual Inquiry, Eye-Tracking Simulation) (*B*) pada produk digital (*C*) secara ilmiah (*D*). | **C4** | `KK5` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** eksperimen A/B Testing (*B*) dengan penetapan hipotesis, ukuran sampel statistik, dan analisis signifikansi konversi (*C*) secara valid (*D*). | **C4** | `KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **membangun** sistem desain tingkat lanjut (*Advanced Design Tokens*) dan dokumentasi komponen Storybook (*B*) dengan kepatuhan aksesibilitas WCAG 2.1 Level AAA (*C*) secara profesional (*D*). | **C6** | `P4, KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Metodologi UX Research (in-depth interview, contextual inquiry), persona & CJM, kuantifikasi usability (SUS, NPS), enterprise design system, WCAG. |
| **OUT-OF-SCOPE** (dilarang) | Tutorial dasar Figma & prototyping (STI-308); koding frontend (STI-311). |
| **Handoff Anchor** (titik transisi) | Validasi data empiris perilaku pengguna; menyerahkan eksekusi prototipe visual ke STI-308. |

---

### B-6. SEMESTER 6

### 32. STA-601 — Computational Methods and Numerics

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 3 SKS / +P |
| **Rumpun MK** | P1 Integrated Smart Systems |
| **Prasyarat** | STI-102, STI-205 |
| **CPL yang Dibebankan** | `P1` (Analisis Galat & Metode Numerik), `KK1` (Algoritma Optimasi Komputasi AI) |
| **Bahan Kajian (BoK)** | `BK-IS10` Applied Mathematics and Logic & `BK-IS18` Machine Learning and Data Science & `BK-IT02` Applied AI & Intelligent Technologies |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menganalisis** galat pemotongan (*Truncation Error*) dan pembulatan (*Round-off Error*) (*B*) pada representasi floating-point komputasi (*C*) secara matematis (*D*). | **C4** | `P1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** metode numerik untuk akar persamaan non-linier (Newton-Raphson, Secant) dan interpolasi Spline (*B*) menggunakan Python (*C*) dengan konvergensi cepat (*D*). | **C3** | `P1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menerapkan** algoritma integrasi numerik (Romberg, Gauss-Legendre) dan solusi Persamaan Diferensial Biasa (Runge-Kutta RK4) (*B*) pada simulasi sistem fisis (*C*) secara akurat (*D*). | **C4** | `P1, KK1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **merancang** algoritma optimasi numerik tak-terkendala dan Stochastic Gradient Descent (*B*) untuk pencarian minimum fungsi loss model AI (*C*) secara optimal (*D*). | **C6** | `KK1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Representasi floating-point & galat (IEEE 754), akar non-linier (Newton-Raphson, Secant), solusi SPL numerik, interpolasi Spline, integrasi Romberg/Gauss-Legendre, PDB (RK4), optimasi SGD/Gradient Descent. |
| **OUT-OF-SCOPE** (dilarang) | Menghitung limit/turunan murni manual tanpa kode (STI-102); melatih jaringan deep (STI-626). |
| **Handoff Anchor** (titik transisi) | Algoritma aproksimasi & optimasi numerik; menyerahkan pemodelan deep learning ke STI-626. |

---

### 33. STA-602 — Intelligent Agent Systems

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 3 SKS / +P |
| **Rumpun MK** | P1 Integrated Smart Systems |
| **Prasyarat** | STI-307 |
| **CPL yang Dibebankan** | `P2` (Arsitektur BDI & Multi-Agent), `KK1` (Reinforcement Learning & Agen Otonom) |
| **Bahan Kajian (BoK)** | `BK-IS16` Artificial Intelligence & Intelligent Systems & `BK-IT02` Applied AI & Intelligent Technologies |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **merancang** agen otonom berbasis arsitektur Belief-Desire-Intention (BDI) (*B*) untuk pengambilan keputusan proaktif (*C*) secara rasional (*D*). | **C4** | `P2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **membangun** simulasi Multi-Agent Systems (MAS) (*B*) menggunakan protokol komunikasi FIPA-ACL dan framework Python Mesa/JADE (*C*) dengan koordinasi terpadu (*D*). | **C6** | `P2, KK1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengimplementasikan** algoritma Reinforcement Learning (Q-Learning, Deep Q-Networks / DQN) (*B*) pada lingkungan simulasi Gymnasium (*C*) dengan kebijakan optimal (*D*). | **C4** | `KK1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **melatih** agen otonom menggunakan algoritma Policy Gradient (PPO) (*B*) pada skenario multi-agen kompetitif/kooperatif (*C*) secara stabil (*D*). | **C5** | `KK1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Arsitektur agen (BDI), Multi-Agent Systems (MAS), protokol FIPA-ACL, framework Python Mesa/JADE, reinforcement learning dasar, negosiasi & koordinasi agen. |
| **OUT-OF-SCOPE** (dilarang) | Inferensi sistem pakar rule-based (STI-307); training deep reinforcement learning skala besar (STI-626). |
| **Handoff Anchor** (titik transisi) | Agen otonom terdistribusi; menyerahkan NN besar ke STI-626 dan pengambilan keputusan tunggal ke STI-307. |

---

### 34. STB-601 — Cloud Architecture & DevOps

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 3 SKS / +P |
| **Rumpun MK** | P2 Cloud Infra & Cybersecurity |
| **Prasyarat** | STI-417 |
| **CPL yang Dibebankan** | `P3` (Infrastruktur Cloud Native), `P4` (Automasi CI/CD & IaC), `KK3` (Orkestrasi Kubernetes & GitOps) |
| **Bahan Kajian (BoK)** | `BK-IS19` Cloud Architecture & DevOps & `BK-IT05` Cloud Computing & Virtualization & `BK-IT07` System Integration and Architecture |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **memprovisi** infrastruktur cloud otomatis (*B*) menggunakan Infrastructure as Code (Terraform) (*C*) dengan modul deklaratif terstandar (*D*). | **C4** | `P3, P4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengorkestrasikan** aplikasi multi-kontainer (*B*) pada klaster Kubernetes (Deployments, StatefulSets, Ingress, PersistentVolumes) (*C*) dengan konfigurasi *high availability* (*D*). | **C4** | `KK3` |
| **CPMK-3** | Mahasiswa (*A*) mampu **membangun** pipeline Continuous Delivery berbasis GitOps (*B*) menggunakan ArgoCD dan Helm Charts (*C*) secara otomatis dan bebas *configuration drift* (*D*). | **C6** | `P4, KK3` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Infrastructure as Code (Terraform), orkestrasi Kubernetes (Deployments, StatefulSets, Ingress, PV), Helm, GitOps (ArgoCD), CI/CD pipeline kontainer. |
| **OUT-OF-SCOPE** (dilarang) | Provisi VM & kontainer Docker tunggal (STI-417); arsitektur aplikasi microservices (STI-627). |
| **Handoff Anchor** (titik transisi) | Automasi & orkestrasi infrastruktur; menyerahkan desain aplikasi microservices ke STI-627. |

---

### 35. STB-602 — Cybersecurity Risk Management

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 3 SKS / Teori |
| **Rumpun MK** | P2 Cloud Infra & Cybersecurity |
| **Prasyarat** | STI-418 |
| **CPL yang Dibebankan** | `P3` (Kerangka Kerja Risiko NIST & ISO 27005), `KK4` (Penilaian Risiko Kuantitatif & BCP/DRP) |
| **Bahan Kajian (BoK)** | `BK-IS06` Information Security and Risk Management & `BK-IT12` IT Risk Management and Compliance |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **melakukan** penilaian risiko keamanan siber kualitatif dan kuantitatif (SLE, ARO, ALE) (*B*) berdasarkan standar ISO/IEC 27005 dan NIST SP 800-30 (*C*) secara presisi (*D*). | **C4** | `P3, KK4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merumuskan** strategi penanganan risiko (Risk Treatment Plan) dan Business Impact Analysis (BIA) (*B*) pada proses bisnis kritis organisasi (*C*) dengan pemilihan kontrol keamanan terjustifikasi (*D*). | **C4** | `KK4` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menyusun** dokumen rencana keberlanjutan bisnis (*Business Continuity Plan / BCP*) dan rencana pemulihan bencana (*Disaster Recovery Plan / DRP*) (*B*) dengan target metrik RTO dan RPO realistis (*C*) secara komprehensif (*D*). | **C5** | `KK4` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Penilaian risiko kualitatif/kuantitatif (SLE, ARO, ALE), ISO/IEC 27005, NIST SP 800-30, Risk Treatment Plan, BIA, BCP & DRP. |
| **OUT-OF-SCOPE** (dilarang) | Alat pentest exploit teknis (STI-519); kontrol akses OWASP web (STI-416). |
| **Handoff Anchor** (titik transisi) | Tata kelola risiko & keberlanjutan bisnis; menyerahkan deteksi exploit teknis ke STI-519. |

---

### 36. STC-601 — Rekayasa & Otomasi Proses Bisnis (BPA)

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 3 SKS / +P |
| **Rumpun MK** | P3 Digital Platform Engineering |
| **Prasyarat** | STI-306 |
| **CPL yang Dibebankan** | `P2` (Pemodelan Proses Bisnis Lanjut), `P4` (Otomasi REST & Orkestrasi), `KK5` (Camunda Workflow Engine & Bot RPA) |
| **Bahan Kajian (BoK)** | `BK-IS09` Business Process Management & `BK-IT11` Software Development Practices |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menganalisis** performa proses bisnis dan mendeteksi kesenjangan (*Conformance Checking*) (*B*) menggunakan teknik Process Mining (*C*) secara empiris (*D*). | **C4** | `P2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang dan mengeksekusi** alur kerja otomatis (*B*) menggunakan Workflow Engine (Camunda BPMN 8 / Temporal) dan Decision Model and Notation (DMN) (*C*) secara terstandarisasi (*D*). | **C6** | `P2, P4, KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengembangkan** bot Robotic Process Automation (RPA) (*B*) menggunakan Python RPA / UiPath (*C*) untuk otomasi tugas repetitif dan ekstraksi dokumen OCR (*D*). | **C6** | `KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Otomasi proses bisnis (RPA UI Path), BPMN lanjut, pemodelan BPM (Camunda), integrasi sistem (ESB/API), middleware. |
| **OUT-OF-SCOPE** (dilarang) | Elisitasi kebutuhan tahap awal (STI-306); koding aplikasi baru dari nol (STI-309). |
| **Handoff Anchor** (titik transisi) | Orkestrasi proses & integrasi sistem lama; menyerahkan pengembangan aplikasi baru ke STI-309. |

---

### 37. STC-602 — Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech)

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 6 / 3 SKS / +P |
| **Rumpun MK** | P3 Digital Platform Engineering |
| **Prasyarat** | STI-416 |
| **CPL yang Dibebankan** | `P4` (Arsitektur Spesifik Domain), `KK5` (Payment Gateway, Buku Besar Digital, Standar SCORM/xAPI) |
| **Bahan Kajian (BoK)** | `BK-IS12` Web and Mobile App Development & `BK-IT04` Platform Technologies & Web/Mobile & `BK-IT07` System Integration and Architecture |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** arsitektur sistem pembayaran digital (*B*) dengan integrasi Payment Gateway API (Midtrans/Xendit) dan buku besar akuntansi ganda (*Double-Entry Ledger*) (*C*) secara aman dan konsisten (*D*). | **C4** | `P4, KK5` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** standar interoperabilitas pembelajaran digital (SCORM 1.2/2004 dan xAPI Tin-Can) (*B*) pada Learning Management System (LMS) (*C*) dengan pelacakan aktivitas belajar yang presisi (*D*). | **C4** | `P4, KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **membangun** platform aplikasi industri vertikal terpadu (*B*) dengan penanganan transaksi idempotensi (*Idempotency Key*) dan kepatuhan regulasi industri (*C*) secara andal (*D*). | **C6** | `KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Aplikasi industri vertikal: FinTech (transaksi, e-wallet, AML/risk rule) & EdTech (LMS, SIS, proctoring), integrasi pembayaran (payment gateway). |
| **OUT-OF-SCOPE** (dilarang) | CRUD aplikasi generik (STI-416); aturan pembayaran/transaksi di luar domain STI-416. |
| **Handoff Anchor** (titik transisi) | Spesialisasi domain vertikal; menyerahkan infrastruktur platform umum ke STI-627/STC-702. |

---

### B-7. SEMESTER 7

### 38. STA-701 — MLOps and AI Pipeline

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / +P |
| **Rumpun MK** | P1 Integrated Smart Systems |
| **Prasyarat** | STI-413, STI-624 |
| **CPL yang Dibebankan** | `P4` (Pipeline Otomasi ML), `KK1` (Continuous Training & Model Registry), `KK2` (Pelacakan Data) |
| **Bahan Kajian (BoK)** | `BK-IS18` Machine Learning and Data Science & `BK-IS19` Cloud Architecture & DevOps & `BK-IT07` System Integration and Architecture |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **mengelola** pelacakan versi data dan eksperimen model (*B*) menggunakan Data Version Control (DVC) dan MLflow Tracking (*C*) secara terstruktur (*D*). | **C4** | `KK2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **membangun** pipeline Continuous Training (CT) otomatis (*B*) menggunakan Kubeflow Pipelines / Apache Airflow (*C*) dengan trigger retraining teruji (*D*). | **C6** | `P4, KK1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mendeploy dan memantau** model AI produksi (*B*) dengan strategi Canary/Shadow Deployment serta deteksi Data/Concept Drift (*C*) menggunakan Evidently AI dan Prometheus (*D*). | **C5** | `KK1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | MLOps lifecycle (CI/CD/CT), registry model (MLflow), otomasi retraining & monitoring drift, eksperimen tracking, feature store, deployment model & canary. |
| **OUT-OF-SCOPE** (dilarang) | Riset/training arsitektur model baru (STI-626); deployment layanan inference via FastAPI/ONNX mendalam (STI-624). |
| **Handoff Anchor** (titik transisi) | Otomasi & tata kelola model produksi; menyerahkan pembuatan layanan inference ke STI-624. |

---

### 39. STA-702 — Conversational AI and Intelligent Assistant

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / +P |
| **Rumpun MK** | P1 Integrated Smart Systems |
| **Prasyarat** | STI-413, STI-416 |
| **CPL yang Dibebankan** | `P2` (Arsitektur Bahasa Alami Modern), `KK1` (Prompt Engineering, RAG & LLM Agents) |
| **Bahan Kajian (BoK)** | `BK-IS16` Artificial Intelligence & Intelligent Systems & `BK-IT02` Applied AI & Intelligent Technologies & `BK-IT04` Platform Technologies & Web/Mobile |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** teknik Prompt Engineering tingkat lanjut (Few-Shot, Chain-of-Thought, ReAct) (*B*) menggunakan framework LangChain (*C*) dengan output terstruktur (*D*). | **C3** | `KK1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang dan mengoptimalkan** sistem RAG multi-dokumen (*B*) menggunakan teknik Contextual Compression dan Reranking (*C*) dengan skor evaluasi RAGAS yang tinggi (*D*). | **C6** | `P2, KK1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **melakukan** Fine-Tuning model LLM open-source (*B*) menggunakan teknik Parameter-Efficient Fine-Tuning (QLoRA) (*C*) pada domain khusus (*D*). | **C4** | `KK1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **membangun** asisten virtual cerdas berbasis agen otonom (Tool Calling) (*B*) dengan integrasi multi-channel (WhatsApp API / Web Widget) (*C*) secara terpadu (*D*). | **C6** | `KK1` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | LLM/Transformer (fine-tuning), prompt engineering, RAG (LangChain, vectordb), agentic AI & tool-use, evaluasi percakapan. |
| **OUT-OF-SCOPE** (dilarang) | Analisis NLP statistik klasik VSM (STI-414); layanan API web kembali (STI-416/STI-624). |
| **Handoff Anchor** (titik transisi) | Bahasa generatif & percakapan; menyerahkan pencarian dokumen klasik ke STI-414. |

---

### 40. STA-703 — Smart Surveillance and IoT Analytics

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / +P |
| **Rumpun MK** | P1 Integrated Smart Systems |
| **Prasyarat** | STI-626, STI-521 |
| **CPL yang Dibebankan** | `P3` (Edge AI & Video Analytics), `KK1` (Computer Vision Real-Time), `KK3` (Integrasi Sensor & CCTV) |
| **Bahan Kajian (BoK)** | `BK-IS16` Artificial Intelligence & Intelligent Systems & `BK-IT02` Applied AI & Intelligent Technologies & `BK-IT14` IoT and Embedded Smart Systems |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **melatih dan mengoptimalkan** model deteksi objek modern (YOLOv8/YOLOv10) (*B*) pada dataset CCTV kustom (*C*) dengan mAP $\ge 0.80$ (*D*). | **C4** | `KK1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengimplementasikan** algoritma pelacakan multi-objek (ByteTrack / DeepSORT) dan pengenalan wajah biometrik (*B*) pada stream video RTSP real-time (*C*) dengan frame rate stabil $\ge 25$ FPS (*D*). | **C4** | `KK1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengonversi dan mendeploy** model vision cerdas (*B*) pada perangkat komputasi tepi (*Edge AI: NVIDIA Jetson / Raspberry Pi 5*) menggunakan TensorRT/OpenVINO (*C*) secara optimal (*D*). | **C6** | `P3, KK3` |
| **CPMK-4** | Mahasiswa (*A*) mampu **membangun** sistem pengawasan cerdas terpadu (*B*) dengan trigger alarm otomatis ke broker MQTT dan dasbor monitoring (*C*) secara andal (*D*). | **C6** | `P3, KK1, KK3` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Video analytics & edge AI, deteksi objek/re-id real-time (YOLO), pengiriman telemetri, dashboard monitoring IoT, integrasi kamera. |
| **OUT-OF-SCOPE** (dilarang) | Telemetri sensor ESP32 & MQTT dasar (STI-521); membangun backend web penuh. |
| **Handoff Anchor** (titik transisi) | Analitik AI pada video/edge; menyerahkan akuisisi sensor MQTT ke STI-521. |

---

### 41. STB-701 — IT Governance & Compliance (COBIT 2019)

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / Teori |
| **Rumpun MK** | P2 Cloud Infra & Cybersecurity |
| **Prasyarat** | STI-101 |
| **CPL yang Dibebankan** | `P3` (Tata Kelola TI Korporasi), `KK4` (Audit COBIT 2019, CMMI & Kepatuhan Regulasi) |
| **Bahan Kajian (BoK)** | `BK-IS05` IS Management and Governance & `BK-IT08` IT Service Management & Governance |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membedakan** prinsip Tata Kelola TI (*Governance*) vs Manajemen TI (*Management*) (*B*) berdasarkan kerangka kerja COBIT 2019 (*C*) secara komprehensif (*D*). | **C4** | `P3` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang** sistem tata kelola TI (*B*) menggunakan COBIT 2019 Design Toolkit dan analisis 11 Design Factors (*C*) sesuai strategi organisasi (*D*). | **C4** | `KK4` |
| **CPMK-3** | Mahasiswa (*A*) mampu **melakukan** audit kapabilitas proses tata kelola TI (*B*) berdasarkan model kapabilitas CMMI COBIT 2019 (Level 0 s.d. 5) (*C*) dengan bukti audit yang valid (*D*). | **C5** | `KK4` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Tata kelola TI COBIT 2019 (EDM, APO, BAI, DSS, MEA), pemetaan kuadran strategis CMMI, metrik kinerja tata kelola. |
| **OUT-OF-SCOPE** (dilarang) | Framework IT service operational (ITIL-4, STB-702); pengukuran kepatuhan teknis pentest. |
| **Handoff Anchor** (titik transisi) | Strategi tata kelola; menyerahkan layanan operasional berkelanjutan ke STB-702. |

---

### 42. STB-702 — IT Service Management (ITIL 4)

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / Teori |
| **Rumpun MK** | P2 Cloud Infra & Cybersecurity |
| **Prasyarat** | STI-101 |
| **CPL yang Dibebankan** | `P2` (Manajemen Layanan TI), `KK4` (Siklus Layanan ITIL 4, SLA/OLA, Manajemen Insiden) |
| **Bahan Kajian (BoK)** | `BK-IS05` IS Management and Governance & `BK-IT08` IT Service Management & Governance |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menguraikan** Service Value System (SVS), 4 Dimensi Manajemen Layanan, dan 7 Prinsip Panduan (*B*) berdasarkan kerangka kerja ITIL 4 (*C*) secara komprehensif (*D*). | **C2** | `P2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang dan menganalisis** alur kerja Service Desk, Incident Management, dan Problem Management (*B*) menggunakan analisis akar masalah (*Root Cause Analysis / Fishbone*) (*C*) secara terstruktur (*D*). | **C4** | `KK4` |
| **CPMK-3** | Mahasiswa (*A*) mampu **merancang** Katalog Layanan TI (*Service Catalog*) dan perjanjian tingkat layanan (*Service Level Agreement / SLA*) (*B*) untuk organisasi penyedia layanan TI (*C*) secara profesional (*D*). | **C5** | `P2, KK4` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | ITIL 4 (Service Value System, praktik Core/Improve/Drive), SLA/OLA, incident, problem, change & release management, service desk. |
| **OUT-OF-SCOPE** (dilarang) | Kebijakan strategi tata kelola (STB-701); audit kepatuhan keuangan (STB-701/STB-602). |
| **Handoff Anchor** (titik transisi) | Layanan TI berkelanjutan; memanfaatkan otomasi infrastruktur STB-601. |

---

### 43. STB-703 — Enterprise Architecture (TOGAF)

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / Teori |
| **Rumpun MK** | P2 Cloud Infra & Cybersecurity |
| **Prasyarat** | STI-306 |
| **CPL yang Dibebankan** | `P2` (Arsitektur Bisnis & Data), `P3` (Arsitektur Teknologi), `KK4` (Pemodelan ArchiMate & TOGAF ADM) |
| **Bahan Kajian (BoK)** | `BK-IS04` Enterprise Architecture & `BK-IT07` System Integration and Architecture |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menguraikan** siklus Architecture Development Method (ADM Fase Preliminary s.d. H) (*B*) berdasarkan standar The Open Group Architecture Framework (TOGAF) (*C*) secara komprehensif (*D*). | **C2** | `P2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **memodelkan** 4 pilar arsitektur enterprise (Business, Data, Application, Technology Architecture) (*B*) menggunakan bahasa pemodelan standar ArchiMate (*C*) secara konsisten (*D*). | **C4** | `P2, P3, KK4` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menyusun** dokumen cetak biru Architecture Definition Document (ADD) (*B*) dengan analisis kesenjangan (*Gap Analysis As-Is vs To-Be*) dan peta jalan migrasi (*Migration Roadmap*) (*C*) secara profesional (*D*). | **C5** | `KK4` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Pendekatan TOGAF ADM (Architecture Vision s.d. Migration), pemodelan arsitektur (ArchiMate), business/data/application/technology architecture. |
| **OUT-OF-SCOPE** (dilarang) | Blueprint SPBE selesai; fokus pada proyek bisnis sistem informasi (STI-625); pemodelan UML detail (STI-306). |
| **Handoff Anchor** (titik transisi) | Peta arsitektur enterprise korporat; menyerahkan sistem domain publik ke STI-625. |

---

### 44. STC-701 — Immersive Media & XR Development

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / +P |
| **Rumpun MK** | P3 Digital Platform Engineering |
| **Prasyarat** | STI-311 |
| **CPL yang Dibebankan** | `P4` (Grafika Komputer & WebXR), `KK5` (Augmented Reality & Virtual Reality) |
| **Bahan Kajian (BoK)** | `BK-IS12` Web and Mobile App Development & `BK-IT04` Platform Technologies & Web/Mobile & `BK-IT10` User Experience & Interaction Design |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membangun** adegan grafika 3D interaktif di browser (*B*) menggunakan WebXR dan Three.js (*C*) dengan pemuatan model 3D (glTF/GLB) yang optimal (*D*). | **C3** | `P4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang dan mengimplementasikan** aplikasi Augmented Reality (AR) mobile (*B*) dengan teknik Marker-Based dan Markerless Plane Detection (*C*) menggunakan ARCore / WebXR (*D*). | **C6** | `KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **membangun** simulasi Virtual Reality (VR) 6DoF interaktif (*B*) dengan audio spasial 3D dan navigasi teleportasi (*C*) dengan performa rendering mulus $\ge 60$ FPS (*D*). | **C6** | `KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Teknologi XR (AR, VR, MR), 3D asset & WebGL/Three.js, interaksi kontroller & spatial, AI/Computer Vision untuk immersive. |
| **OUT-OF-SCOPE** (dilarang) | Riset UX pengguna dasar (STC-501); pengembangan web 2D konvensional (STI-311/STI-416). |
| **Handoff Anchor** (titik transisi) | Produk immersive interaktif; menyerahkan usability research perilaku ke STC-501. |

---

### 45. STC-702 — SaaS Architecture & Multi-Tenancy

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / +P |
| **Rumpun MK** | P3 Digital Platform Engineering |
| **Prasyarat** | STI-416 |
| **CPL yang Dibebankan** | `P4` (Arsitektur Multi-Tenancy), `KK5` (Row-Level Security, Subscription Engine & Micro-Frontends) |
| **Bahan Kajian (BoK)** | `BK-IS04` Enterprise Architecture & `BK-IT04` Platform Technologies & Web/Mobile & `BK-IT07` System Integration and Architecture |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **merancang** strategi isolasi data multi-tenant (Shared Database with Row-Level Security vs Database-per-Tenant) (*B*) pada PostgreSQL (*C*) dengan jaminan isolasi data mutlak (*D*). | **C4** | `P4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **membangun** mesin penagihan berlangganan (*Subscription Engine*) otomatis (*B*) dengan integrasi Stripe API dan webhook (*C*) secara transaksional (*D*). | **C6** | `KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengimplementasikan** arsitektur Micro-Frontends dan *Feature Toggling* (*B*) pada platform SaaS (*C*) untuk aktivasi fitur dinamis per paket langganan (*D*). | **C4** | `P4, KK5` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Arsitektur SaaS (multi-tenant, tenant isolation), monetisasi & metering (plan, quota), on-boarding tenant, sharing schema & shared DB. |
| **OUT-OF-SCOPE** (dilarang) | Membangun microservice event-driven skalabel (STI-627); penyusunan PRD & metrik produk (STC-703). |
| **Handoff Anchor** (titik transisi) | Mesin multitenansi SaaS; menyerahkan strategi go-to-market produk ke STC-703. |

---

### 46. STC-703 — Digital Product Management & Agile Practices

| Atribut | Spesifikasi |
|---|---|
| **Semester / SKS / Tipe** | 7 / 3 SKS / Teori |
| **Rumpun MK** | P3 Digital Platform Engineering |
| **Prasyarat** | STI-523 |
| **CPL yang Dibebankan** | `P2` (Strategi Produk Digital & OKRs), `KK6` (Product Discovery, PRD, RICE Prioritization & Go-To-Market) |
| **Bahan Kajian (BoK)** | `BK-IS01` Foundations of Information Systems & `BK-IS08` Project Management & `BK-IT13` Technology Entrepreneurship |

**CPMK (Capaian Pembelajaran Mata Kuliah):**

| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |
|---|---|:--:|:--:|
| **CPMK-1** | Mahasiswa (*A*) mampu **merumuskan** Visi Produk, Strategi Produk, dan Objectives and Key Results (OKRs) (*B*) untuk produk digital rintisan (*C*) secara terukur (*D*). | **C4** | `P2, KK6` |
| **CPMK-2** | Mahasiswa (*A*) mampu **melakukan** Product Discovery dan prioritisasi backlog (*B*) menggunakan kerangka kerja RICE, Kano Model, dan MoSCoW (*C*) secara objektif (*D*). | **C4** | `KK6` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menyusun** dokumen Product Requirement Document (PRD) berstandar industri (*B*) dengan User Stories, Acceptance Criteria, dan strategi Go-To-Market (GTM) (*C*) secara komprehensif (*D*). | **C6** | `KK6` |

**Boundary Guardrails** (dari Dok 037):

| Guardrail | Batas Materi |
|---|---|
| **IN-SCOPE** (wajib diajarkan) | Product vision & OKRs, Product Discovery, prioritisasi RICE/Kano, penyusunan PRD (user stories, acceptance criteria), agile product management, metrik produk (activation, retention, revenue). |
| **OUT-OF-SCOPE** (dilarang) | Manajemen jadwal/biaya/sumber daya pengembangan (STI-523); riset user behavioral (STC-501). |
| **Handoff Anchor** (titik transisi) | Strategi & tanggung jawab kesuksesan produk; menyerahkan penjadwalan dividen pengembangan teknis ke STI-523. |

---
