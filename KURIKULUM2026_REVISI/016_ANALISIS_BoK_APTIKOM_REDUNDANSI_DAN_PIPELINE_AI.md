# 016 — ANALISIS FORENSIK BoK APTIKOM, AUDIT REDUNDANSI, DAN PIPA TANGGA PEMBELAJARAN AI SISTEKIN 2026
## Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang

**Dokumen Kajian Autentik Keselarasan Bahan Kajian APTIKOM IS2020 & IT2017, Penataan Mata Kuliah Redundan, dan Blueprint Kurikulum Kecerdasan Artifisial Modern**  
**Standar Rujukan:** Panduan Kurikulum OBE APTIKOM SI v2.0 (IS2020), Panduan Kurikulum OBE TI 2023 (IT2017/CC2020), Standar IABEE Criteria & LAM INFOKOM.

---

## 1. PENDAHULUAN & LATAR BELAKANG AUDIT

Dalam upaya menyusun kurikulum OBE Program Studi Sistem dan Teknologi Informasi (SISTEKIN) yang presisi, bermutu tinggi, dan berdaya saing global (*lean and high-impact curriculum*), diperlukan audit forensik berbasis bukti (*evidence-based*) terhadap keselarasan Bahan Kajian (Body of Knowledge / BoK) APTIKOM serta eliminasi tumpang tindih (*redundancy*) antar-mata kuliah.

Dokumen ini mendokumentasikan hasil analisis kritis terhadap:
1. **Identifikasi Autentik Struktur Bersama FSTI (39 SKS / 14 MK)** berdasarkan data ground truth fakultas.
2. **Audit Redundansi 4 Klaster Mata Kuliah** berdasarkan topik silabus baku APTIKOM IS2020 dan IT2017.
3. **Penajaman Posisi `STI-302 Sistem Cerdas` (Symbolic & Fuzzy AI)** versus **`FST-204 Pengantar AI & Data` (Literasi GenAI & LLM)**.
4. **Blueprint Pipa Tangga Pembelajaran AI Berjenjang (*Zero-Overlap 5-Stage AI Pipeline*)** dari Semester 2 hingga Semester 6.

---

## 2. GROUND TRUTH AUTENTIK MATA KULIAH FAKULTAS (FSTI COMMON CORE 39 SKS)

Berdasarkan dokumen resmi kurikulum bersama Fakultas Sains dan Teknologi Informasi (FSTI), struktur 14 Mata Kuliah Wajib Fakultas (39 SKS) telah terpetakan secara definitif:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   TABEL GROUND TRUTH 14 MATA KULIAH FAKULTAS (FSTI) — 39 SKS                     │
├────┬───────────┬───────────────────────────────────────────┬─────┬──────────┬────────────────────┤
│ No │ Kode MK   │ Nama Mata Kuliah FSTI                     │ SKS │ Semester │ Prasyarat Formal   │
├────┼───────────┼───────────────────────────────────────────┼:---:┼:--------:┼────────────────────┤
│ 1  │ `FST-101` │ Dasar Teknologi Digital                   │  2  │    1     │ —                  │
│ 2  │ `FST-102` │ Algoritma dan Pemrograman (+P)            │  3  │    1     │ —                  │
│ 3  │ `FST-203` │ Struktur Data dan Strategi Algoritma (+P) │  3  │    2     │ `FST-102`          │
│ 4  │ `FST-204` │ Pengantar Kecerdasan Artifisial & Data    │  3  │    2     │ —                  │
│ 5  │ `FST-205` │ Basic English                             │  2  │    2     │ —                  │
│ 6  │ `FST-206` │ Etika dan Hukum Digital                   │  2  │    2     │ —                  │
│ 7  │ `FST-207` │ Basis Data (+P)                           │  3  │    2     │ —                  │
│ 8  │ `FST-408` │ Statistika & Probabilitas                 │  3  │    4     │ —                  │
│ 9  │ `FST-409` │ English for IT Professionals              │  2  │    4     │ `FST-205`          │
│ 10 │ `FST-610` │ Capstone Project FSTI                     │  3  │   6-7    │ —                  │
│ 11 │ `FST-611` │ Metodologi Penelitian                     │  2  │   6-7    │ $\ge 76$ SKS       │
│ 12 │ `FST-612` │ Praktik Kerja Lapangan (PKL)              │  3  │   6-7    │ $\ge 100$ SKS      │
│ 13 │ `FST-613` │ Pra-Skripsi / Seminar Proposal            │  2  │  6-7-8   │ $\ge 100$ SKS      │
│ 14 │ `FST-714` │ Skripsi / Tugas Akhir                     │  6  │   7-8    │ $\ge 120$ SKS      │
├────┴───────────┴───────────────────────────────────────────┼:---:┼──────────┴────────────────────┤
│ TOTAL BEBAN BERSAMA FAKULTAS (14 MATA KULIAH)              │ 39  │ SKS Terstandarisasi FSTI      │
└────────────────────────────────────────────────────────────┴:---:┴───────────────────────────────┘
```

> **📌 Temuan Kunci Asal-Usul `FST-409`:**  
> Kode `FST-409` secara autentik adalah **`English for IT Professionals` (2 SKS, Sem 4)**, membuktikan bahwa penamaan lama "Riset Operasi" pada kode ini adalah murni kesalahan penulisan (*historical typo*).

---

## 3. AUDIT FORENSIK TOPIK BAHAN KAJIAN (BoK) APTIKOM & REDUNDANSI KURIKULUM

Berikut adalah hasil komparasi rinci per topik (*topic-by-topic cross examination*) terhadap silabus baku APTIKOM:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    AUDIT KESELARASAN BoK APTIKOM VS REDUNDANSI MATA KULIAH SISTEKIN                             │
├────┬─────────────────────────────┬───────────────────────────┬──────────────────────────────────────────────────┤
│ No │ Mata Kuliah di SISTEKIN     │ Kode & Topik BoK APTIKOM  │ Bukti Redundansi / Tumpang Tindih                │
├────┼─────────────────────────────┼───────────────────────────┼──────────────────────────────────────────────────┤
│ 1  │ • STI-103 Logika Inf (3 SKS)│ BK-IS10:                  │ • APTIKOM IS2020 & IT2017 TIDAK PERNAH memisahkan│
│    │ • STI-201 Matdis (3 SKS)    │ Applied Mathematics       │   Logika Informatika dan Matematika Diskrit.     │
│    │                             │ and Logic                 │ • Seluruh materi logika proposisi, predikat, &   │
│    │                             │                           │   aljabar boolean adalah Bab 1-3 Matdis.         │
│    │                             │                           │   ➔ Tumpang tindih: 40-50% materi berulang.      │
├────┼─────────────────────────────┼───────────────────────────┼──────────────────────────────────────────────────┤
│ 2  │ • FST-204 Pengantar AI (3)  │ BK-IS16 / BK-IT02:        │ • FST-204 adalah literasi global & GenAI,        │
│    │ • STI-302 Sistem Cerdas (2) │ AI & Intelligent Systems  │   sedangkan STI-302 difokuskan pada Symbolic AI  │
│    │                             │                           │   dan Logika Fuzzy (FLC) untuk IoT & DSS.        │
│    │                             │                           │   ➔ Bebas tumpang tindih jika RPS dispesifikasi. │
├────┼─────────────────────────────┼───────────────────────────┼──────────────────────────────────────────────────┤
│ 3  │ • STI-401 Machine Learn (3) │ BK-IS13 (BI & Analytics)  │ • APTIKOM membagi analitik data secara tegas:    │
│    │ • STI-402 DW & BI (3 SKS)   │            vs             │   1. BI & Data Analytics (DW/Dashboard = STI-402)│
│    │ • STI-503 Data Mining (3 SKS│ BK-IS18 (Machine Learning)│   2. Predictive Modeling (ML/DL = STI-401/501).  │
│    │                             │                           │ • STI-503 harus difokuskan pada Visualisasi Data │
│    │                             │                           │   Bisnis dan Exploratory Data Analysis (EDA).    │
├────┼─────────────────────────────┼───────────────────────────┼──────────────────────────────────────────────────┤
│ 4  │ • STI-603 Keamanan Lanjut(3)│ BK-IS06 / BK-IT06:        │ • STI-603 di Wajib Prodi mengajarkan ISO 27001 & │
│    │ • STB-03 Cyber Risk Mgmt (3)│ Information Security and  │   Risk Assessment Framework.                     │
│    │                             │ Risk Management           │ • STB-03 di Peminatan 2 direposisi menjadi Cloud │
│    │                             │                           │   Security & DevSecOps agar berbasis teknis lab. │
└────┴─────────────────────────────┴───────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 4. PENAJAMAN PERAN: `FST-204` (BIRD'S-EYE VIEW GEN-AI) VS `STI-302` (SYMBOLIC & FUZZY AI)

Untuk menjamin tidak adanya tumpang tindih antara mata kuliah bersama fakultas dan mata kuliah program studi, ditetapkan demarkasi kurikulum yang tegas:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│              DEMARKASI SILABUS: FST-204 (FAKULTAS) VS STI-302 (CORE PRODI)                       │
├──────────────────────────────────────────────────┬───────────────────────────────────────────────┤
│ FST-204: PENGANTAR AI & DATA (3 SKS, SEM 2)      │ STI-302: SISTEM CERDAS (2 SKS, SEM 3)         │
│ (Fokus: Literasi Global, Generative AI & Data)   │ (Fokus: Symbolic Reasoning & Fuzzy Systems)   │
├──────────────────────────────────────────────────┼───────────────────────────────────────────────┤
│ • Bird's-Eye View Lanskap AI & Sains Data        │ • Heuristic Search Algorithms (A*, Minimax)   │
│ • Generative AI, Large Language Models (LLM)     │ • Sistem Pakar (Forward & Backward Chaining)  │
│ • Prompt Engineering & AI Productivity Tools     │ • Logika Fuzzy (Mamdani, Sugeno, Tsukamoto)   │
│ • Etika Penggunaan AI, Bias, Hak Cipta & UU PDP  │ • Fuzzy Logic Controller (FLC) untuk IoT/Edge │
│ • Konsep Data Structured, Semi, Unstructured     │ • Knowledge Graph & Ontologi Sistem Cerdas    │
└──────────────────────────────────────────────────┴───────────────────────────────────────────────┘
```

---

## 5. BLUEPRINT PIPA TANGGA PEMBELAJARAN AI SISTEKIN 2026 (ZERO-OVERLAP)

Program Studi SISTEKIN mengimplementasikan kurikulum kecerdasan artifisial terintegrasi yang berjenjang dari hulu (konsep dasar) hingga hilir (penerapan industri):

```
                               ┌─────────────────────────────────────────────────┐
                               │ SEMESTER 6: STI-601 Integrasi Layanan Cerdas AI │
                               │ • API AI/LLM Microservices • Web/Mobile Deploy  │
                               └────────────────────────▲────────────────────────┘
                                                        │
                               ┌────────────────────────┴────────────────────────┐
                               │ SEMESTER 5: STI-501 Deep Learning (+P)          │
                               │ • Computer Vision • CNN • PyTorch Architecture  │
                               └────────────────────────▲────────────────────────┘
                                                        │
                 ┌──────────────────────────────────────┴──────────────────────────────────────┐
                 │                                                                             │
  ┌──────────────┴──────────────────────────────┐               ┌──────────────────────────────┴──────────────┐
  │ SEMESTER 4: STI-401 Machine Learning (+P)   │               │ SEMESTER 4: STI-403 Pengantar NLP & IR (+P) │
  │ • Statistical AI • Scikit-Learn • Regresi/Tree│               │ • Text Preprocessing • TF-IDF • Vector Space│
  └──────────────▲──────────────────────────────┘               └────────────────────────▲────────────────────┘
                 │                                                                       │
                 └──────────────────────────────────────┬────────────────────────────────┘
                                                        │
                               ┌────────────────────────┴────────────────────────┐
                               │ SEMESTER 3: STI-302 Sistem Cerdas (2 SKS)       │
                               │ • Symbolic AI • Rule-Based • Fuzzy Logic Engine │
                               └────────────────────────▲────────────────────────┘
                                                        │
                               ┌────────────────────────┴────────────────────────┐
                               │ SEMESTER 2: FST-204 Pengantar AI & Data (3 SKS) │
                               │ • Bird's-Eye View • GenAI • LLM • Etika & Data  │
                               └─────────────────────────────────────────────────┘
```

---

## 6. REKOMENDASI FORMAL TINDAK LANJUT KURIKULUM

1. **Penggabungan Logika ke Matematika Diskrit:** Menyatukan `STI-103 Logika Informatika` ke dalam **`STI-201 Matematika Diskrit & Logika (3 SKS)`** untuk merampingkan rumpun sains komputasi.
2. **Kesesuaian 100% dengan FSTI:** Mengunci 14 mata kuliah FSTI (39 SKS) termasuk **`FST-409 English for IT Professionals (2 SKS)`** sebagai pilar internasionalisasi lulusan.
3. **Pengesahan Pipa AI:** Menjadikan Pipa Tangga AI 5-Tahap ini sebagai keunggulan diferensiasi (*flagship distinctive positioning*) Program Studi SISTEKIN Universitas Widyagama Malang.

---
*Disahkan sebagai Dokumen Resmi 016 — Analisis BoK APTIKOM, Audit Redundansi, dan Pipeline AI SISTEKIN 2026.*  
**Tim Pengembang Kurikulum Program Studi Sistem dan Teknologi Informasi — FSTI Universitas Widyagama Malang**
