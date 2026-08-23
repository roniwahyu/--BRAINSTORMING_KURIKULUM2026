# -*- coding: utf-8 -*-
import os

filepath = r"d:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI\012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md"

with open(filepath, 'rb') as f:
    raw = f.read()

# Replace any malformed or corrupted sequences if present
text = raw.decode('utf-8', errors='ignore')

# Fix corrupted Tree View section
old_broken_part = text[text.find("### 🌲 PILAR 1"):text.find("### 🌲 PILAR 3")]

clean_part = """### 🌲 PILAR 1: AI, DATA SCIENCE & INTELLIGENT SYSTEMS (PL-1 & P1)

```text
[SEM 8]  FST-714 Skripsi / Tugas Akhir (Topik AI / Data Science / Intelligent Systems)
   │
[SEM 7]  ├── STA-04 MLOps & AI Model Deployment (+P) ─────────┐
         ├── STA-05 Natural Language Processing & LLM (+P) ────┤
         ├── STA-06 Smart Surveillance & Vision Analytics ─────┤
         │                                                     │
[SEM 6]  ├── STI-601 Integrasi Layanan Cerdas AI (+P) ─────────┤
         ├── STA-03 Sistem Agen Cerdas & Multi-Agent (+P) ─────┤
         ├── STA-02 Metode Komputasi Numerik Terapan (+P) ─────┤
         │                                                     │
[SEM 5]  ├── STI-501 Deep Learning & Neural Networks (+P) ─────┴── STI-401 Machine Learning (+P) [SEM 4]
         │                                                           │
         ├── STI-503 Data Mining & Visualisasi Data (+P) ────────────┼── STI-402 Data Warehouse & BI [SEM 4]
         │                                                           │
         ├── STA-01 Decision Support Systems (+P) ───────────────────┼── STI-403 Pengantar NLP & IR [SEM 4]
         │                                                           │     │
[SEM 4]  └── STI-401 Machine Learning (+P) ──────────────────────────┴─────┼── STI-302 Sistem Cerdas [SEM 3]
               │                                                           │     │
[SEM 3]        └── STI-302 Sistem Cerdas [SEM 3] ──────────────────────────┼─────┴── STI-201 Matdis & STI-202 Aljabar [SEM 2]
                     │                                                     │
[SEM 2]              ├── STI-201 Matematika Diskrit dan Logika ────────────┼── STI-103 Arsitektur & Organisasi STI [SEM 1]
                     ├── STI-202 Aljabar Linear Terapan & Matriks ─────────┼── STI-102 Kalkulus [SEM 1]
                     ├── FST-207 Sistem Basis Data (+P) ───────────────────┼── FST-102 Algoritma & Pemrograman [SEM 1]
                     └── FST-408 Statistika & Probabilitas ────────────────┘
```

#### 🔍 Analisis Kritis & Justifikasi Pedagogis Pilar 1:
1. **Peran Kunci `STI-403 Pengantar NLP & IR` (Sem 4):** Menjadi jembatan esensial untuk `STA-05 Conversational AI` (Sem 7) yang berbasis LLM/RAG. Tanpa fondasi tokenisasi, TF-IDF, vector space model, dan embedding di Sem 4, pemahaman generative AI di Sem 7 akan bersifat superficial.
2. **Keterpaduan Deep Learning & Machine Learning:** `STI-401 Machine Learning` (Sem 4) mengajarkan *classical tabular & loss minimization*, yang menjadi landasan wajib bagi `STI-501 Deep Learning` (Sem 5) yang memperdalam *backpropagation, CNN, RNN/LSTM, dan Attention Mechanism*.
3. **MLOps sebagai Muara Rekayasa:** `STA-04 MLOps` (Sem 7) mensintesis model machine learning dengan containerization dan pipeline deployment (menghubungkan pilar AI dengan pilar Cloud/DevOps).

---

### 🌲 PILAR 2: CLOUD INFRASTRUCTURE & CYBERSECURITY (PL-2 & P2)

```text
[SEM 8]  FST-714 Skripsi / Tugas Akhir (Topik Cloud Native & Cyber Resilience)
   │
[SEM 7]  ├── STB-04 IT Governance & Compliance COBIT 2019 ────┐
         ├── STB-05 Keamanan Cloud & Kriptografi Terapan ──────┤
         ├── STB-06 Rekayasa Ketahanan Sistem & SRE (+P) ──────┤
         │                                                     │
[SEM 6]  ├── STB-02 Cloud Architecture & DevOps (+P) ──────────┼── STI-404 Komputasi Awan (Cloud) [SEM 4]
         ├── STB-03 Penetration Testing & Red Teaming (+P) ────┤     │
         ├── STI-603 Keamanan Informasi Lanjut ────────────────┤     │
         │                                                     │     │
[SEM 5]  ├── STI-504 Internet of Things (IoT) (+P) ────────────┼── STI-307 Jaringan Komputer [SEM 3]
         ├── STB-01 Keamanan Jaringan & Forensik Digital ──────┤     │
         │                                                     │     │
[SEM 4]  ├── STI-404 Komputasi Awan (Cloud Computing) ─────────┴─────┼── STI-305 Sistem Operasi [SEM 3]
         └── STI-405 Dasar Keamanan Informasi ───────────────────────┘     │
               │                                                           │
[SEM 3]        ├── STI-307 Jaringan Komputer (+P) ─────────────────────────┼── STI-103 Arsitektur & Organisasi STI [SEM 1]
               └── STI-305 Sistem Operasi ─────────────────────────────────┴── STI-103 Arsitektur & Organisasi STI [SEM 1]
                     │                                                          │
[SEM 2]              ├── FST-206 Etika Profesi & Hukum Digital ─────────────────┴── FST-101 Dasar Teknologi Digital [SEM 1]
[SEM 1]              └── STI-103 Arsitektur dan Organisasi Sistem Teknologi Informasi
```

#### 🔍 Analisis Kritis & Justifikasi Pedagogis Pilar 2:
1. **Dwi-Fondasi Sem 3 (OS & Jarkom):** `STI-305 Sistem Operasi` (proses, memori, kernel, virtualisasi) dan `STI-307 Jaringan Komputer` (TCP/IP, subnetting, routing) berakar langsung dari `STI-103 Arsitektur dan Organisasi Sistem Teknologi Informasi` di Sem 1, dan menjadi fondasi ganda bagi `STI-404 Cloud` dan `STI-405 Security`.
2. **Kematangan Bertahap Cyber Defense:** 
   * Sem 2: Regulasi & UU ITE (`FST-206`)
   * Sem 4: CIA Triad, Kripto Klasik, Risk (`STI-405`)
   * Sem 5: Wireshark, Packet Inspection, Autopsy (`STB-01`)
   * Sem 6: Ethical Hacking, OWASP Top 10, Kali Linux (`STB-03` & `STI-603`)
   * Sem 7: Zero-Trust Cloud & GRC Enterprise (`STB-04` & `STB-05`).

---

"""

new_text = text[:text.find("### 🌲 PILAR 1")] + clean_part + text[text.find("### 🌲 PILAR 3"):]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("SUCCESS: 012 updated cleanly.")
