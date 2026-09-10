import os
import re

base = r'd:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI'
f005_path = os.path.join(base, '005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md')

with open(f005_path, 'r', encoding='utf-8') as f:
    c005 = f.read()

# -----------------------------------------------------------------------------
# 1. TAMBAHKAN SEKSI 1.4 KELOMPOK MK PILIHAN PEMINATAN
# -----------------------------------------------------------------------------
sec14_text = """
### 1.4 KELOMPOK MATA KULIAH PILIHAN PEMINATAN (ELEKTIF) (18 MK DITAWARKAN / 18 SKS DITEMPUH)

Mata kuliah keahlian spesialisasi yang ditawarkan dalam 3 jalur peminatan (*Integrated Smart Systems*, *Cloud Infrastructure & Cybersecurity*, dan *Digital Platform Engineering*). Setiap mahasiswa menempuh **1 paket peminatan penuh (6 MK / 18 SKS)** yang terdistribusi secara terstruktur pada Semester 5 (1 MK / 3 SKS), Semester 6 (2 MK / 6 SKS), dan Semester 7 (3 MK / 9 SKS):

| No | Kode MK | Nama Mata Kuliah | SKS | Tipe | Semester | Prasyarat | Jalur Peminatan |
|:---:|:---:|---|:---:|:---:|:---:|---|---|
| 1 | `STA-501` | Decision Support Systems | 3 | +P | Sem 5 | `STI-307` | P1: Integrated Smart Systems |
| 2 | `STA-601` | Computational Methods and Numerics | 3 | +P | Sem 6 | `STI-102`, `STI-205` | P1: Integrated Smart Systems |
| 3 | `STA-602` | Intelligent Agent Systems | 3 | +P | Sem 6 | `STI-307` | P1: Integrated Smart Systems |
| 4 | `STA-701` | MLOps and AI Pipeline | 3 | +P | Sem 7 | `STI-413`, `STI-624` | P1: Integrated Smart Systems |
| 5 | `STA-702` | Conversational AI and Intelligent Assistant | 3 | +P | Sem 7 | `STI-413`, `STI-416` | P1: Integrated Smart Systems |
| 6 | `STA-703` | Smart Surveillance and IoT Analytics | 3 | +P | Sem 7 | `STI-626`, `STI-521` | P1: Integrated Smart Systems |
| 7 | `STB-501` | Network Security and Digital Forensics | 3 | +P | Sem 5 | `STI-312`, `STI-418` | P2: Cloud Infra & Cybersecurity |
| 8 | `STB-601` | Cloud Architecture & DevOps | 3 | +P | Sem 6 | `STI-417` | P2: Cloud Infra & Cybersecurity |
| 9 | `STB-602` | Cybersecurity Risk Management | 3 | Teori | Sem 6 | `STI-418` | P2: Cloud Infra & Cybersecurity |
| 10 | `STB-701` | IT Governance & Compliance (COBIT 2019) | 3 | Teori | Sem 7 | `STI-101` | P2: Cloud Infra & Cybersecurity |
| 11 | `STB-702` | IT Service Management (ITIL 4) | 3 | Teori | Sem 7 | `STI-101` | P2: Cloud Infra & Cybersecurity |
| 12 | `STB-703` | Enterprise Architecture (TOGAF) | 3 | Teori | Sem 7 | `STI-306` | P2: Cloud Infra & Cybersecurity |
| 13 | `STC-501` | User Experience Research & Design | 3 | +P | Sem 5 | `STI-308` | P3: Digital Platform Engineering |
| 14 | `STC-601` | Rekayasa & Otomasi Proses Bisnis (BPA) | 3 | +P | Sem 6 | `STI-306` | P3: Digital Platform Engineering |
| 15 | `STC-602` | Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech) | 3 | +P | Sem 6 | `STI-416` | P3: Digital Platform Engineering |
| 16 | `STC-701` | Immersive Media & XR Development | 3 | +P | Sem 7 | `STI-311` | P3: Digital Platform Engineering |
| 17 | `STC-702` | SaaS Architecture & Multi-Tenancy | 3 | +P | Sem 7 | `STI-416` | P3: Digital Platform Engineering |
| 18 | `STC-703` | Digital Product Management & Agile Practices | 3 | Teori | Sem 7 | `STI-523` | P3: Digital Platform Engineering |
| **TOTAL** | — | **18 Mata Kuliah Pilihan Ditawarkan (Portofolio SIAKAD)** | **54** | — | — | **Ditempuh 6 MK (18 SKS) per Mahasiswa** | **3 Jalur Peminatan Seimbang** |
"""

target_sec1 = "| **TOTAL** | — | **28 Mata Kuliah Inti Program Studi** | **79** | — | — | **54,1% Beban Kurikulum** |\n\n---\n"
replacement_sec1 = "| **TOTAL** | — | **28 Mata Kuliah Inti Program Studi** | **79** | — | — | **54,1% Beban Kurikulum** |\n\n---\n" + sec14_text + "\n---\n"

if target_sec1 in c005:
    c005 = c005.replace(target_sec1, replacement_sec1)
    print("Seksi 1.4 berhasil disisipkan setelah Seksi 1.3.")
else:
    print("Target Seksi 1.3 tidak ditemukan!")

# -----------------------------------------------------------------------------
# 2. TAMBAHKAN CALLOUT PILIHAN PEMINATAN PADA SEKSI 3 (SEMESTER 5, 6, 7)
# -----------------------------------------------------------------------------
sem5_subtotal = "| **SUBTOTAL** | — | **Total SKS Semester 5 (7 MK + 1 MK 0 SKS)** | **21** | — | — | **Kumulatif: 101 SKS** |"
sem5_notes = sem5_subtotal + """\n
> [!NOTE]
> **Daftar Pilihan Mata Kuliah Peminatan 1 (Semester 5 — Ambil 1 MK / 3 SKS sesuai jalur):**
> * **Peminatan 1 (Smart Systems):** `STA-501` Decision Support Systems (+P, 3 SKS, Prasyarat: `STI-307`)
> * **Peminatan 2 (Cloud & Cyber):** `STB-501` Network Security and Digital Forensics (+P, 3 SKS, Prasyarat: `STI-312`, `STI-418`)
> * **Peminatan 3 (Platform Eng):** `STC-501` User Experience Research & Design (+P, 3 SKS, Prasyarat: `STI-308`)"""

sem6_subtotal = "| **SUBTOTAL** | — | **Total SKS Semester 6 (7 MK)** | **19** | — | — | **Kumulatif: 120 SKS** |"
sem6_notes = sem6_subtotal + """\n
> [!NOTE]
> **Daftar Pilihan Mata Kuliah Peminatan 2 & 3 (Semester 6 — Ambil 2 MK / 6 SKS sesuai jalur):**
> * **Peminatan 1 (Smart Systems):** `STA-601` Computational Methods and Numerics (+P, 3 SKS) & `STA-602` Intelligent Agent Systems (+P, 3 SKS)
> * **Peminatan 2 (Cloud & Cyber):** `STB-601` Cloud Architecture & DevOps (+P, 3 SKS) & `STB-602` Cybersecurity Risk Management (Teori, 3 SKS)
> * **Peminatan 3 (Platform Eng):** `STC-601` Rekayasa & Otomasi Proses Bisnis (+P, 3 SKS) & `STC-602` Rekayasa Aplikasi Industri Vertikal (+P, 3 SKS)"""

sem7_subtotal = "| **SUBTOTAL** | — | **Total SKS Semester 7 (7 MK)** | **20** | — | — | **Kumulatif: 140 SKS** |"
sem7_notes = sem7_subtotal + """\n
> [!NOTE]
> **Daftar Pilihan Mata Kuliah Peminatan 4, 5 & 6 (Semester 7 — Ambil 3 MK / 9 SKS sesuai jalur):**
> * **Peminatan 1 (Smart Systems):** `STA-701` MLOps and AI Pipeline (+P, 3 SKS), `STA-702` Conversational AI and Intelligent Assistant (+P, 3 SKS), `STA-703` Smart Surveillance and IoT Analytics (+P, 3 SKS)
> * **Peminatan 2 (Cloud & Cyber):** `STB-701` IT Governance & Compliance COBIT 2019 (Teori, 3 SKS), `STB-702` IT Service Management ITIL 4 (Teori, 3 SKS), `STB-703` Enterprise Architecture TOGAF (Teori, 3 SKS)
> * **Peminatan 3 (Platform Eng):** `STC-701` Immersive Media & XR Development (+P, 3 SKS), `STC-702` SaaS Architecture & Multi-Tenancy (+P, 3 SKS), `STC-703` Digital Product Management & Agile Practices (Teori, 3 SKS)"""

c005 = c005.replace(sem5_subtotal, sem5_notes)
c005 = c005.replace(sem6_subtotal, sem6_notes)
c005 = c005.replace(sem7_subtotal, sem7_notes)
print("Catatan pilihan peminatan berhasil ditambahkan pada tabel rincian Semester 5, 6, dan 7.")

# -----------------------------------------------------------------------------
# 3. PERLUAS SEKSI 4: TABEL RINCIAN 3 PEMINATAN
# -----------------------------------------------------------------------------
sec4_detail = """

### 4.1 PEMINATAN 1: INTEGRATED SMART SYSTEMS (FLAGSHIP — 6 MK / 18 SKS)
Fokus keahlian: Rekayasa sistem berbasis AI, machine learning pipelines, deep learning vision & language, agen cerdas, serta analitik IoT terintegrasi (Profil Lulusan: `PL-1`).

| No | Kode MK | Nama Mata Kuliah | SKS | Tipe | Semester | Prasyarat Akademik | Bahan Kajian Utama |
|:---:|:---:|---|:---:|:---:|:---:|---|---|
| 1 | `STA-501` | Decision Support Systems | 3 | +P | Sem 5 | `STI-307` Sistem Cerdas | BK-IS17 Business Analytics, AHP/TOPSIS |
| 2 | `STA-601` | Computational Methods and Numerics | 3 | +P | Sem 6 | `STI-102`, `STI-205` Aljabar Linear | BK-IS10 / BK-IT01 Komputasi Saintifik |
| 3 | `STA-602` | Intelligent Agent Systems | 3 | +P | Sem 6 | `STI-307` Sistem Cerdas | BK-IT02 Multi-Agent Systems, Reinforcement |
| 4 | `STA-701` | MLOps and AI Pipeline | 3 | +P | Sem 7 | `STI-413`, `STI-624` Integrasi AI | BK-IS18 Machine Learning Engineering |
| 5 | `STA-702` | Conversational AI and Intelligent Assistant | 3 | +P | Sem 7 | `STI-413`, `STI-416` Web Back End | BK-IT02 LLM, RAG Architecture, Prompt Eng |
| 6 | `STA-703` | Smart Surveillance and IoT Analytics | 3 | +P | Sem 7 | `STI-626`, `STI-521` IoT | BK-IT02 Video Analytics, Edge AI, Vision |

### 4.2 PEMINATAN 2: CLOUD INFRASTRUCTURE & CYBERSECURITY (VOLUME — 6 MK / 18 SKS)
Fokus keahlian: Arsitektur cloud computing, otomatisasi DevOps, tata kelola keamanan siber, manajemen risiko, forensik digital, dan enterprise architecture (Profil Lulusan: `PL-2`).

| No | Kode MK | Nama Mata Kuliah | SKS | Tipe | Semester | Prasyarat Akademik | Bahan Kajian Utama |
|:---:|:---:|---|:---:|:---:|:---:|---|---|
| 1 | `STB-501` | Network Security and Digital Forensics | 3 | +P | Sem 5 | `STI-312`, `STI-418` Dasar Keamanan | BK-IT06 Cyber Defense, Forensik Jaringan |
| 2 | `STB-601` | Cloud Architecture & DevOps | 3 | +P | Sem 6 | `STI-417` Komputasi Awan | BK-IT05 Cloud Systems, CI/CD, Kubernetes |
| 3 | `STB-602` | Cybersecurity Risk Management | 3 | Teori | Sem 6 | `STI-418` Dasar Keamanan Informasi | BK-IS06 Risk Management, ISO 27005, NIST |
| 4 | `STB-701` | IT Governance & Compliance (COBIT 2019) | 3 | Teori | Sem 7 | `STI-101` Pengantar Sistem & TI | BK-IS07 IT Governance, COBIT 2019 Focus |
| 5 | `STB-702` | IT Service Management (ITIL 4) | 3 | Teori | Sem 7 | `STI-101` Pengantar Sistem & TI | BK-IS08 Service Management, ITIL 4 Foundation |
| 6 | `STB-703` | Enterprise Architecture (TOGAF) | 3 | Teori | Sem 7 | `STI-306` Analisis & Perancangan SI | BK-IS04 Enterprise Architecture, TOGAF Standard |

### 4.3 PEMINATAN 3: DIGITAL PLATFORM ENGINEERING (NICHE & TECHNO — 6 MK / 18 SKS)
Fokus keahlian: Rekayasa antarmuka pengguna interaktif (UI/UX research), otomasi proses bisnis, arsitektur multi-tenant SaaS, media imersif XR, dan manajemen produk digital agile (Profil Lulusan: `PL-3` & `PL-4`).

| No | Kode MK | Nama Mata Kuliah | SKS | Tipe | Semester | Prasyarat Akademik | Bahan Kajian Utama |
|:---:|:---:|---|:---:|:---:|:---:|---|---|
| 1 | `STC-501` | User Experience Research & Design | 3 | +P | Sem 5 | `STI-308` UI/UX Design & Prototyping | BK-IS13 Human-Centered Design, Usability |
| 2 | `STC-601` | Rekayasa & Otomasi Proses Bisnis (BPA) | 3 | +P | Sem 6 | `STI-306` Analisis & Perancangan SI | BK-IS09 Business Process, Workflow & RPA |
| 3 | `STC-602` | Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech) | 3 | +P | Sem 6 | `STI-416` Web Back End Development | BK-IS05 Application Domains, Microservices |
| 4 | `STC-701` | Immersive Media & XR Development | 3 | +P | Sem 7 | `STI-311` Web Front End Development | BK-IT14 Computer Graphics, Unity/WebXR |
| 5 | `STC-702` | SaaS Architecture & Multi-Tenancy | 3 | +P | Sem 7 | `STI-416` Web Back End Development | BK-IT08 Distributed Systems, Multi-Tenancy |
| 6 | `STC-703` | Digital Product Management & Agile Practices | 3 | Teori | Sem 7 | `STI-523` Manajemen Proyek TI | BK-IS14 Product Management, Scrum, Lean |
"""

sec4_target = "| **P3: Digital Platform Engineering** *(Niche & Techno)* | **PL-3:** UI/UX Designer & Platform Engineer | 1. `STC-501` UX Research & Design (+P, Sem 5)<br>2. `STC-601` Rekayasa & Otomasi Proses Bisnis (+P, Sem 6)<br>3. `STC-602` Rekayasa Aplikasi Industri Vertikal (+P, Sem 6)<br>4. `STC-701` Immersive Media & XR Development (+P, Sem 7)<br>5. `STC-702` SaaS Architecture & Multi-Tenancy (+P, Sem 7)<br>6. `STC-703` Digital Product Management (Teori, Sem 7) |"

if sec4_target in c005:
    c005 = c005.replace(sec4_target, sec4_target + "\n" + sec4_detail)
    print("Seksi 4.1 - 4.3 berhasil ditambahkan ke Dokumen 005.")
else:
    print("Target Seksi 4 tidak ditemukan!")

with open(f005_path, 'w', encoding='utf-8') as f:
    f.write(c005)

print("Pembaruan Dokumen 005 selesai dengan sukses!")
