# 035 — RESTRUKTURISASI KODE MK PEMINATAN (STA, STB, STC) BERBASIS SEMESTER
## Standarisasi Kodifikasi 3-Digit (Reset ke 01 per Semester) Kurikulum OBE 2026
**Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang**

---

### 1. LATAR BELAKANG DAN RASIONALITAS AKADEMIK

Pada implementasi awal draf Kurikulum 2026, 18 Mata Kuliah Pilihan Peminatan (*Elective Tracks*) menggunakan skema penomoran serial datar 2-digit (`STA-01..06`, `STB-01..06`, `STC-01..06`). Skema tersebut memiliki keterbatasan:
1. **Tidak Informatif terhadap Semester Penawaran:** Dari kode mata kuliah, mahasiswa, dosen Penasihat Akademik (PA), maupun operator SIAKAD tidak dapat langsung mengenali semester penawaran mata kuliah tersebut.
2. **Inkonsistensi Format Kodifikasi:** Seluruh kelompok mata kuliah lain di Kurikulum 2026 telah menerapkan digit semester pada digit pertama:
   - **MKWU:** `MKU-101..103` (Sem 1), `MKU-204` (Sem 2), `MKU-405..406` (Sem 4), `MKU-507..508` (Sem 5).
   - **FSTI:** `FST-101..102` (Sem 1), `FST-203..207` (Sem 2), `FST-408` (Sem 4), `FST-611` (Sem 6), `FST-610..613` (Sem 7), `FST-714` (Sem 8).
   - **Core STI:** `STI-101..103` (Sem 1) s.d. `STI-728` (Sem 7).
3. **Zero Risk Kolisi Kurikulum 2025:** Berdasarkan audit forensik terhadap basis data Laporan Kurikulum SIAKAD 2025 (`Laporan Daftar Kurikulum Prodi Sistekin.pdf`), Kurikulum 2025 tidak pernah memiliki mata kuliah berawalan `STA`, `STB`, ataupun `STC` (0 kemunculan), sehingga transisi ke format 3-digit sepenuhnya bebas konflik.

Sesuai arahan Tim Kurikulum, disepakati penerapan **Model 2: Penomoran 3-Digit dengan Reset ke 01 pada Setiap Semester**:
$$\mathbf{ST[A/B/C]\text{-}[Semester][Nomor\ Urut\ dalam\ Semester\ (2\ Digit)]}$$

---

### 2. TABEL DEFINITIF PEMETAAN KODE MK PEMINATAN (18 MK PORTOFOLIO)

| Sem | Rumpun Peminatan | Nama Mata Kuliah | SKS | Tipe | Kode Lama | **Kode Baru Definitif** | Prasyarat Akademik |
|:---:|:---|---|:---:|:---:|:---:|:---:|---|
| **5** | P1: Integrated Smart Systems | Decision Support Systems | 3 | +P | `STA-01` | **`STA-501`** | `STI-307` Sistem Cerdas |
| **5** | P2: Cloud Infra & Cyber | Network Security and Digital Forensics | 3 | +P | `STB-01` | **`STB-501`** | `STI-312` Jaringan Komputer, `STI-418` Dasar Keamanan Info |
| **5** | P3: Digital Platform Eng | User Experience Research & Design | 3 | +P | `STC-01` | **`STC-501`** | `STI-308` UI/UX Design & Prototyping |
| **6** | P1: Integrated Smart Systems | Computational Methods and Numerics | 3 | +P | `STA-02` | **`STA-601`** | `STI-102` Kalkulus, `STI-205` Aljabar Linear |
| **6** | P1: Integrated Smart Systems | Intelligent Agent Systems | 3 | +P | `STA-03` | **`STA-602`** | `STI-307` Sistem Cerdas |
| **6** | P2: Cloud Infra & Cyber | Cloud Architecture & DevOps | 3 | +P | `STB-02` | **`STB-601`** | `STI-417` Komputasi Awan |
| **6** | P2: Cloud Infra & Cyber | Cybersecurity Risk Management | 3 | Teori | `STB-03` | **`STB-602`** | `STI-418` Dasar Keamanan Informasi |
| **6** | P3: Digital Platform Eng | Rekayasa & Otomasi Proses Bisnis (BPA) | 3 | +P | `STC-02` | **`STC-601`** | `STI-306` Analisis & Perancangan Sistem Info |
| **6** | P3: Digital Platform Eng | Rekayasa Aplikasi Industri Vertikal | 3 | +P | `STC-03` | **`STC-602`** | `STI-416` Web Back End Development |
| **7** | P1: Integrated Smart Systems | MLOps and AI Pipeline | 3 | +P | `STA-04` | **`STA-701`** | `STI-413` Machine Learning, `STI-624` Integrasi AI |
| **7** | P1: Integrated Smart Systems | Conversational AI & Intelligent Assistant | 3 | +P | `STA-05` | **`STA-702`** | `STI-413` Machine Learning, `STI-416` Web Back End |
| **7** | P1: Integrated Smart Systems | Smart Surveillance & IoT Analytics | 3 | +P | `STA-06` | **`STA-703`** | `STI-626` Deep Learning, `STI-521` IoT |
| **7** | P2: Cloud Infra & Cyber | IT Governance & Compliance (COBIT 2019) | 3 | Teori | `STB-04` | **`STB-701`** | `STI-101` Pengantar STI |
| **7** | P2: Cloud Infra & Cyber | IT Service Management (ITIL 4) | 3 | Teori | `STB-05` | **`STB-702`** | `STI-101` Pengantar STI |
| **7** | P2: Cloud Infra & Cyber | Enterprise Architecture (TOGAF) | 3 | Teori | `STB-06` | **`STB-703`** | `STI-306` Analisis & Perancangan Sistem Info |
| **7** | P3: Digital Platform Eng | Immersive Media & XR Development | 3 | +P | `STC-04` | **`STC-701`** | `STI-311` Web Front End Development |
| **7** | P3: Digital Platform Eng | SaaS Architecture & Multi-Tenancy | 3 | +P | `STC-05` | **`STC-702`** | `STI-416` Web Back End Development |
| **7** | P3: Digital Platform Eng | Digital Product Management & Agile | 3 | Teori | `STC-06` | **`STC-703`** | `STI-523` Manajemen Proyek TI |

---

### 3. PENYELARASAN DOKUMEN USULAN 2027 (DOKUMEN 025)

Skema reset per semester ini secara langsung memfasilitasi keteraturan penomoran pada usulan perluasan keranjang mata kuliah pilihan (*expanded basket*) untuk siklus 2027:

| Sem | Peminatan | Usulan Tambahan 2027 | SKS | Kode Baru |
|:---:|---|---|:---:|:---:|
| **5** | P1: Smart Systems | Computer Vision & Citra Digital | 3 | **`STA-502`** |
| **5** | P1: Smart Systems | Analisis Time Series & Prediktif | 3 | **`STA-503`** |
| **5** | P2: Cloud & Cyber | Linux System & Server Administration | 3 | **`STB-502`** |
| **5** | P2: Cloud & Cyber | Virtualization & Software-Defined Network | 3 | **`STB-503`** |
| **5** | P3: Digital Platform | Design Systems & Micro-Interactions | 3 | **`STC-502`** |
| **5** | P3: Digital Platform | E-Commerce Platform & Payment API | 3 | **`STC-503`** |
| **6** | P1: Smart Systems | Big Data Engineering & Stream Analytics | 3 | **`STA-603`** |
| **6** | P1: Smart Systems | Edge AI & Embedded Machine Learning | 3 | **`STA-604`** |
| **6** | P2: Cloud & Cyber | Penetration Testing & Ethical Hacking | 3 | **`STB-603`** |
| **6** | P2: Cloud & Cyber | Cloud Native Architecture & Kubernetes | 3 | **`STB-604`** |
| **6** | P3: Digital Platform | Microservices Architecture & API Gateway | 3 | **`STC-603`** |
| **6** | P3: Digital Platform | Cross-Platform Mobile Engineering | 3 | **`STC-604`** |
| **7** | P1: Smart Systems | Generative AI Engineering & LLM App | 3 | **`STA-704`** |
| **7** | P1: Smart Systems | Autonomous Systems & Robot Navigation | 3 | **`STA-705`** |
| **7** | P2: Cloud & Cyber | Security Operations Center (SOC) & SIEM | 3 | **`STB-704`** |
| **7** | P2: Cloud & Cyber | Cloud Security & Zero Trust Architecture | 3 | **`STB-705`** |
| **7** | P3: Digital Platform | Enterprise Resource Planning (ERP) Systems | 3 | **`STC-704`** |
| **7** | P3: Digital Platform | Web3 & Decentralized Platform Engineering | 3 | **`STC-705`** |

---

### 4. LOG IMPLEMENTASI & HASIL VERIFIKASI

1. **Jangkauan Eksekusi Atomik:**
   - 21 Berkas Markdown utama (`000`, `004`, `005`, `007`, `009D`, `011`, `012`, `016`, `017`, `019`, `023`, `024`, `025`, `026`, `027`, `028`, `030`, `031`, `039`, `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md`, dan `AGENTS.md`) telah diperbarui secara serentak.
   - 8 Skrip pendukung automasi Python telah disesuaikan.
2. **Audit Zero Residual:**
   - Pemindaian menyeluruh via `scan_peminatan_occurrences.py` mengonfirmasi **0 kemunculan kode lama** (`STA-01..06`, `STB-01..06`, `STC-01..06`) di seluruh repositori.
3. **Audit Ground Truth SIAKAD K2025:**
   - Pengujian terprogram via `verify_k2025_ground_truth.py` menghasilkan **LULUS 11/11 kelompok uji** (termasuk verifikasi semester MK elektif dan rekognisi portofolio 67 MK).
4. **Audit Zero Discrepancy:**
   - Verifikasi melalui `verify_zero_discrepancy.py` menghasilkan **100% PERFECT ALIGNMENT** pada seluruh 45 berkas Markdown.

---
*Disahkan sebagai Dokumen Resmi 035 — Restrukturisasi Kode MK Peminatan SISTEKIN 2026.*  
**Tim Pengembang Kurikulum FSTI Universitas Widyagama Malang**
