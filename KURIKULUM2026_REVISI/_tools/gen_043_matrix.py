# -*- coding: utf-8 -*-
"""
Generator Dokumen 043: Matriks CPL - CPMK - BoK - Boundary Guardrails per Mata Kuliah.
Sumber data:
  - Dok 005: daftar MK, semester, SKS, tipe, prasyarat.
  - Dok 007: CPL yang dibebankan + rumusan CPMK (ABCD) -- diekstrak ke _tmp_cpmk.json / _tmp_cpl.json.
  - Dok 037: BoK, Boundary Guardrails (IN-SCOPE / OUT-OF-SCOPE / Handoff Anchor).
Tidak menambahkan klaim yang tidak ada di sumber.
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
REV = os.path.dirname(BASE)

# ---------------------------------------------------------------------------
# Ekstraksi CPMK dan CPL dari Dok 007 (self-contained; tidak butuh file tmp).
# ---------------------------------------------------------------------------
_SRC007 = os.path.join(REV, "007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md")
_TXT007 = open(_SRC007, encoding="utf-8").read()

def _extract_007():
    import re
    blocks = re.split(r"\n(?=### \d+\. )", _TXT007)
    cpmk, cpl = {}, {}
    for b in blocks:
        m = re.match(r"### \d+\. (\S+)", b)
        if not m:
            continue
        code = m.group(1)
        mm = re.search(r"\*\*CPL yang Dibebankan\*\* \| (.*?)\n", b)
        if mm:
            cpl[code] = mm.group(1).rstrip(" |").strip()
        rows = re.findall(
            r"\|\s*\*\*(CPMK-\d+)\*\*\s*\|\s*(.*?)\s*\|\s*\*\*([RC]\d+)\*\*\s*\|\s*([^\n|]*)\s*\|",
            b,
        )
        cpmk[code] = [
            {"k": k, "rum": r.strip(), "bloom": bl, "cpl": c.strip().strip("`").strip()}
            for k, r, bl, c in rows
        ]
    return cpmk, cpl

CPMK, CPL = _extract_007()

# ---------------------------------------------------------------------------
# Data MK (kode -> info) bersumber Dok 005.
# ---------------------------------------------------------------------------
MK = {
    # ---------------- CORE STI Sem 1 ----------------
    "STI-101": dict(nama="Pengantar Sistem dan Teknologi Informasi", sks="2", tipe="Teori", sem=1,
        prasy="-", rumpun="Sistem Informasi & Tata Kelola"),
    "STI-102": dict(nama="Kalkulus", sks="3", tipe="Teori", sem=1,
        prasy="-", rumpun="Matematika & Sains Komputasi"),
    "STI-103": dict(nama="Arsitektur dan Organisasi Sistem Teknologi Informasi", sks="3", tipe="Teori", sem=1,
        prasy="-", rumpun="Infrastruktur, Sistem & Komputasi Awan"),
    # ---------------- CORE STI Sem 2 ----------------
    "STI-204": dict(nama="Matematika Diskrit dan Logika", sks="3", tipe="Teori", sem=2,
        prasy="STI-103", rumpun="Matematika & Sains Komputasi"),
    "STI-205": dict(nama="Aljabar Linear dan Matriks", sks="3", tipe="Teori", sem=2,
        prasy="STI-102", rumpun="Matematika & Sains Komputasi"),
    # ---------------- CORE STI Sem 3 ----------------
    "STI-306": dict(nama="Analisis dan Perancangan Sistem Informasi", sks="3", tipe="Teori", sem=3,
        prasy="STI-101, FST-207", rumpun="Sistem Informasi & Tata Kelola"),
    "STI-307": dict(nama="Sistem Cerdas", sks="2", tipe="Teori", sem=3,
        prasy="STI-204, FST-204", rumpun="Kecerdasan Artifisial"),
    "STI-308": dict(nama="UI/UX Design & Prototyping", sks="3", tipe="+P", sem=3,
        prasy="FST-101", rumpun="Interaksi Manusia-Komputer & UX"),
    "STI-309": dict(nama="Rekayasa Perangkat Lunak", sks="3", tipe="Teori", sem=3,
        prasy="FST-203", rumpun="Rekayasa Perangkat Lunak"),
    "STI-310": dict(nama="Sistem Operasi", sks="3", tipe="Teori", sem=3,
        prasy="STI-103", rumpun="Infrastruktur, Sistem & Komputasi Awan"),
    "STI-311": dict(nama="Web Front End Development", sks="3", tipe="+P", sem=3,
        prasy="FST-102", rumpun="Platform & Pengembangan Web/Mobile"),
    "STI-312": dict(nama="Jaringan Komputer", sks="3", tipe="+P", sem=3,
        prasy="STI-103", rumpun="Infrastruktur, Sistem & Komputasi Awan"),
    # ---------------- CORE STI Sem 4 ----------------
    "STI-413": dict(nama="Machine Learning", sks="3", tipe="+P", sem=4,
        prasy="STI-205, STI-307", rumpun="Kecerdasan Artifisial"),
    "STI-414": dict(nama="Pengantar NLP & Information Retrieval", sks="2", tipe="+P", sem=4,
        prasy="STI-307", rumpun="Kecerdasan Artifisial"),
    "STI-415": dict(nama="Data Warehouse & Business Intelligence", sks="3", tipe="+P", sem=4,
        prasy="FST-207", rumpun="Data Management & Analitik"),
    "STI-416": dict(nama="Web Back End Development", sks="3", tipe="+P", sem=4,
        prasy="FST-207, STI-311", rumpun="Platform & Pengembangan Web/Mobile"),
    "STI-417": dict(nama="Komputasi Awan (Cloud Computing)", sks="3", tipe="Teori", sem=4,
        prasy="STI-312, STI-310", rumpun="Infrastruktur, Sistem & Komputasi Awan"),
    "STI-418": dict(nama="Dasar Keamanan Informasi", sks="2", tipe="Teori", sem=4,
        prasy="STI-312", rumpun="Keamanan Informasi & Tata Kelola"),
    # ---------------- CORE STI Sem 5 ----------------
    "STI-519": dict(nama="Keamanan Informasi Lanjut", sks="3", tipe="Teori", sem=5,
        prasy="STI-418", rumpun="Keamanan Informasi & Tata Kelola"),
    "STI-520": dict(nama="Data Mining & Visualisasi Data", sks="3", tipe="+P", sem=5,
        prasy="STI-413, STI-415", rumpun="Data Management & Analitik"),
    "STI-521": dict(nama="Internet of Things (IoT)", sks="3", tipe="+P", sem=5,
        prasy="STI-312, STI-310", rumpun="IoT & Sistem Tertanam"),
    "STI-522": dict(nama="Pemrograman Aplikasi Mobile", sks="3", tipe="+P", sem=5,
        prasy="STI-311, STI-416", rumpun="Platform & Pengembangan Web/Mobile"),
    "STI-523": dict(nama="Manajemen Proyek TI", sks="3", tipe="Teori", sem=5,
        prasy="STI-306, STI-309", rumpun="Sistem Informasi & Tata Kelola"),
    # ---------------- CORE STI Sem 6 ----------------
    "STI-624": dict(nama="Integrasi Layanan Cerdas Berbasis AI", sks="3", tipe="+P", sem=6,
        prasy="STI-413, STI-416", rumpun="Kecerdasan Artifisial"),
    "STI-625": dict(nama="Smart City & Pemerintahan Digital", sks="2", tipe="Teori", sem=6,
        prasy="STI-521", rumpun="Sistem Informasi & Tata Kelola"),
    "STI-626": dict(nama="Deep Learning & Neural Networks", sks="3", tipe="+P", sem=6,
        prasy="STI-413", rumpun="Kecerdasan Artifisial"),
    "STI-627": dict(nama="Digital Platform Engineering", sks="3", tipe="+P", sem=6,
        prasy="STI-416", rumpun="Platform & Pengembangan Web/Mobile"),
    # ---------------- CORE STI Sem 7 ----------------
    "STI-728": dict(nama="Inovasi Teknologi dan Startup Digital", sks="3", tipe="+P", sem=7,
        prasy="STI-627, MKU-204", rumpun="Digital Innovation & Entrepreneurship"),
    # ---------------- PEMINATAN Sem 5 ----------------
    "STA-501": dict(nama="Decision Support Systems", sks="3", tipe="+P", sem=5,
        prasy="STI-307", rumpun="P1 Integrated Smart Systems"),
    "STB-501": dict(nama="Network Security and Digital Forensics", sks="3", tipe="+P", sem=5,
        prasy="STI-312, STI-418", rumpun="P2 Cloud Infra & Cybersecurity"),
    "STC-501": dict(nama="User Experience Research & Design", sks="3", tipe="+P", sem=5,
        prasy="STI-308", rumpun="P3 Digital Platform Engineering"),
    # ---------------- PEMINATAN Sem 6 ----------------
    "STA-601": dict(nama="Computational Methods and Numerics", sks="3", tipe="+P", sem=6,
        prasy="STI-102, STI-205", rumpun="P1 Integrated Smart Systems"),
    "STA-602": dict(nama="Intelligent Agent Systems", sks="3", tipe="+P", sem=6,
        prasy="STI-307", rumpun="P1 Integrated Smart Systems"),
    "STB-601": dict(nama="Cloud Architecture & DevOps", sks="3", tipe="+P", sem=6,
        prasy="STI-417", rumpun="P2 Cloud Infra & Cybersecurity"),
    "STB-602": dict(nama="Cybersecurity Risk Management", sks="3", tipe="Teori", sem=6,
        prasy="STI-418", rumpun="P2 Cloud Infra & Cybersecurity"),
    "STC-601": dict(nama="Rekayasa & Otomasi Proses Bisnis (BPA)", sks="3", tipe="+P", sem=6,
        prasy="STI-306", rumpun="P3 Digital Platform Engineering"),
    "STC-602": dict(nama="Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech)", sks="3", tipe="+P", sem=6,
        prasy="STI-416", rumpun="P3 Digital Platform Engineering"),
    # ---------------- PEMINATAN Sem 7 ----------------
    "STA-701": dict(nama="MLOps and AI Pipeline", sks="3", tipe="+P", sem=7,
        prasy="STI-413, STI-624", rumpun="P1 Integrated Smart Systems"),
    "STA-702": dict(nama="Conversational AI and Intelligent Assistant", sks="3", tipe="+P", sem=7,
        prasy="STI-413, STI-416", rumpun="P1 Integrated Smart Systems"),
    "STA-703": dict(nama="Smart Surveillance and IoT Analytics", sks="3", tipe="+P", sem=7,
        prasy="STI-626, STI-521", rumpun="P1 Integrated Smart Systems"),
    "STB-701": dict(nama="IT Governance & Compliance (COBIT 2019)", sks="3", tipe="Teori", sem=7,
        prasy="STI-101", rumpun="P2 Cloud Infra & Cybersecurity"),
    "STB-702": dict(nama="IT Service Management (ITIL 4)", sks="3", tipe="Teori", sem=7,
        prasy="STI-101", rumpun="P2 Cloud Infra & Cybersecurity"),
    "STB-703": dict(nama="Enterprise Architecture (TOGAF)", sks="3", tipe="Teori", sem=7,
        prasy="STI-306", rumpun="P2 Cloud Infra & Cybersecurity"),
    "STC-701": dict(nama="Immersive Media & XR Development", sks="3", tipe="+P", sem=7,
        prasy="STI-311", rumpun="P3 Digital Platform Engineering"),
    "STC-702": dict(nama="SaaS Architecture & Multi-Tenancy", sks="3", tipe="+P", sem=7,
        prasy="STI-416", rumpun="P3 Digital Platform Engineering"),
    "STC-703": dict(nama="Digital Product Management & Agile Practices", sks="3", tipe="Teori", sem=7,
        prasy="STI-523", rumpun="P3 Digital Platform Engineering"),
}

# ---------------------------------------------------------------------------
# BoK per MK.  Untuk MK yang ada di Dok 037 (klaster & peminatan) dipakai
# rujukan BoK-nya sesuai Dok 037.  Untuk MK core lain dirujuk dari katalog BoK
# Dok 037 bagian 2 berdasarkan isi CPMK (Dok 007).
# ---------------------------------------------------------------------------
BOK = {
    # ---- Core Sem 1 ----
    "STI-101": ["BK-IS01", "BK-IS15"],
    "STI-102": ["BK-IS10", "BK-IT01"],
    "STI-103": ["BK-IS03", "BK-IT01"],
    # ---- Core Sem 2 ----
    "STI-204": ["BK-IS10", "BK-IT01"],
    "STI-205": ["BK-IS10", "BK-IS18"],
    # ---- Core Sem 3 ----
    "STI-306": ["BK-IS07", "BK-IS09"],
    "STI-307": ["BK-IS16", "BK-IT02"],
    "STI-308": ["BK-IS17", "BK-IT10"],
    "STI-309": ["BK-IS07", "BK-IT11"],
    "STI-310": ["BK-IS03", "BK-IT01"],
    "STI-311": ["BK-IS12", "BK-IT04"],
    "STI-312": ["BK-IS03", "BK-IT03"],
    # ---- Core Sem 4 ----
    "STI-413": ["BK-IS18", "BK-IT02"],
    "STI-414": ["BK-IS16", "BK-IT02"],
    "STI-415": ["BK-IS02", "BK-IS13"],
    "STI-416": ["BK-IS12", "BK-IT04"],
    "STI-417": ["BK-IS19", "BK-IT05"],
    "STI-418": ["BK-IS06", "BK-IT06"],
    # ---- Core Sem 5 ----
    "STI-519": ["BK-IS06", "BK-IT06"],
    "STI-520": ["BK-IS02", "BK-IS13"],
    "STI-521": ["BK-IS03", "BK-IT14"],
    "STI-522": ["BK-IS12", "BK-IT04"],
    "STI-523": ["BK-IS08", "BK-IT08"],
    # ---- Core Sem 6 ----
    "STI-624": ["BK-IS19", "BK-IT02"],
    "STI-625": ["BK-IS04", "BK-IS03"],
    "STI-626": ["BK-IS18", "BK-IT02"],
    "STI-627": ["BK-IS12", "BK-IT07"],
    # ---- Core Sem 7 ----
    "STI-728": ["BK-IS15", "BK-IT13"],
    # ---- Peminatan STA (P1) ----
    "STA-501": ["BK-IS13", "BK-IS16", "BK-IT09"],
    "STA-601": ["BK-IS10", "BK-IS18", "BK-IT02"],
    "STA-602": ["BK-IS16", "BK-IT02"],
    "STA-701": ["BK-IS18", "BK-IS19", "BK-IT07"],
    "STA-702": ["BK-IS16", "BK-IT02", "BK-IT04"],
    "STA-703": ["BK-IS16", "BK-IT02", "BK-IT14"],
    # ---- Peminatan STB (P2) ----
    "STB-501": ["BK-IS06", "BK-IT06"],
    "STB-601": ["BK-IS19", "BK-IT05", "BK-IT07"],
    "STB-602": ["BK-IS06", "BK-IT12"],
    "STB-701": ["BK-IS05", "BK-IT08"],
    "STB-702": ["BK-IS05", "BK-IT08"],
    "STB-703": ["BK-IS04", "BK-IT07"],
    # ---- Peminatan STC (P3) ----
    "STC-501": ["BK-IS17", "BK-IT10"],
    "STC-601": ["BK-IS09", "BK-IT11"],
    "STC-602": ["BK-IS12", "BK-IT04", "BK-IT07"],
    "STC-701": ["BK-IS12", "BK-IT04", "BK-IT10"],
    "STC-702": ["BK-IS04", "BK-IT04", "BK-IT07"],
    "STC-703": ["BK-IS01", "BK-IS08", "BK-IT13"],
}

# ---------------------------------------------------------------------------
# Nama BoK (Dok 037 bagian 2).
# ---------------------------------------------------------------------------
BOK_NAME = {
    "BK-IS01": "Foundations of Information Systems",
    "BK-IS02": "Data and Information Management",
    "BK-IS03": "IT Infrastructure and Networking",
    "BK-IS04": "Enterprise Architecture",
    "BK-IS05": "IS Management and Governance",
    "BK-IS06": "Information Security and Risk Management",
    "BK-IS07": "Systems Analysis and Design",
    "BK-IS08": "Project Management",
    "BK-IS09": "Business Process Management",
    "BK-IS10": "Applied Mathematics and Logic",
    "BK-IS11": "Programming Fundamentals & OOP",
    "BK-IS12": "Web and Mobile App Development",
    "BK-IS13": "Data Analytics and Business Intelligence",
    "BK-IS14": "IT Audit and Compliance",
    "BK-IS15": "Digital Innovation and Entrepreneurship",
    "BK-IS16": "Artificial Intelligence & Intelligent Systems",
    "BK-IS17": "Human-Computer Interaction & UX",
    "BK-IS18": "Machine Learning and Data Science",
    "BK-IS19": "Cloud Architecture & DevOps",
    "BK-IS20": "Ethics, Use and Implications for Society",
    "BK-IS21": "Internship and Professional Practice",
    "BK-IT01": "Information Technology Fundamentals",
    "BK-IT02": "Applied AI & Intelligent Technologies",
    "BK-IT03": "Networking & Communications",
    "BK-IT04": "Platform Technologies & Web/Mobile",
    "BK-IT05": "Cloud Computing & Virtualization",
    "BK-IT06": "Cybersecurity Principles & Defense",
    "BK-IT07": "System Integration and Architecture",
    "BK-IT08": "IT Service Management & Governance",
    "BK-IT09": "Data Analytics & Information Visualization",
    "BK-IT10": "User Experience & Interaction Design",
    "BK-IT11": "Software Development Practices",
    "BK-IT12": "IT Risk Management and Compliance",
    "BK-IT13": "Technology Entrepreneurship",
    "BK-IT14": "IoT and Embedded Smart Systems",
    "BK-IT15": "Global Professional Practice",
}

# ---------------------------------------------------------------------------
# Boundary Guardrails per MK: (IN-SCOPE, OUT-OF-SCOPE, HANDOFF).
# Untuk MK yang dibahas di Dok 037 diambil inti guardrails-nya (diringkas dari
# Dok 037).  Untuk MK core tertentu dilengkapi dari rumpun & CPMK (Dok 007)
# tanpa menambah klaim baru.  Teks ringkas agar tabel tetap terbaca.
# ---------------------------------------------------------------------------
GUARD = {
    # ============ CORE Sem 1 ============
    "STI-101": (
        "Konsep data-informasi-pengetahuan, komponen SI, sistem enterprise "
        "(TPS/MIS/DSS/ERP/CRM/SCM), transformasi digital (AI, Cloud, IoT), "
        "pengantar tata kelola TI & cybersecurity.",
        "Implementasi koding sistem / algoritma pemrograman terperinci; "
        "perancangan arsitektur cloud teknis; pentesting.",
        "Memberi konteks bisnis & peta TI; menyerahkan pengembangan sistem ke "
        "FST-102/STI-306 dan fondasi infrastruktur ke STI-103.",
    ),
    "STI-102": (
        "Limit, kontinuitas, turunan (univariat & multivariat), integral, "
        "aplikasi pada optimasi & Gradient Descent.",
        "Koding numerik; pembuktian aljabar abstrak; metode numerik diskrit "
        "(itu ranah STA-601).",
        "Turunan/integral kontinu jadi dasar STI-205 (aljabar linear) dan "
        "STI-413 (ML); komputasi aproksimasi diserahkan ke STA-601.",
    ),
    "STI-103": (
        "Representasi biner/BL, gerbang logika, CPU (ALU/register), "
        "Fetch-Decode-Execute, hierarki memori & cache, I/O, virtualisasi "
        "hardware, arsitektur server data center.",
        "Logika predikat/aljabar relasi (STI-204); manajemen thread OS "
        "(STI-310); konfigurasi router (STI-312).",
        "Memahami mesin fisik; menyerahkan manajemen perangkat lunak sistem ke "
        "STI-310 dan komunikasi data ke STI-312.",
    ),
    # ============ CORE Sem 2 ============
    "STI-204": (
        "Logika proposisi & predikat, tabel kebenaran, relasi, himpunan "
        "terurut, aljabar Boolean, kombinatorika, graf & pohon, FSA (DFA/NFA).",
        "Gerbang logika fisik/gerbang mikroprosesor (STI-103); kalkulus "
        "diferensial-integral kontinu.",
        "Logika formal & struktur diskrit jadi fondasi STI-307 (Sistem Cerdas) "
        "dan STI-413.",
    ),
    "STI-205": (
        "SPL, eliminasi Gauss-Jordan, ruang vektor, basis & dimensi, nilai "
        "eigen, diagonalisasi, dekomposisi SVD & reduksi PCA (Python/NumPy).",
        "Koding numerik penuh untuk fungsi non-linier (STA-601); pemodelan "
        "dataset ML.",
        "Matriks linear menjadi prasyarat STI-413 (ML) dan fondasi STA-601.",
    ),
    # ============ CORE Sem 3 ============
    "STI-306": (
        "Elisitasi kebutuhan, BPMN 2.0, UML fungsional & struktural, dokumen "
        "SRS (IEEE 830).",
        "Koding aplikasi & unit testing (STI-309); estimasi biaya proyek "
        "(STI-523).",
        "Cetak biru kebutuhan; menyerahkan konstruksi & pengujian ke STI-309, "
        "manajemen ke STI-523.",
    ),
    "STI-307": (
        "Pencarian heuristik (A*, Greedy, Minimax), knowledge representation, "
        "sistem pakar (forward/backward chaining), fuzzy inference.",
        "ML statistik / neural network / deep learning (STI-413/STI-626); "
        "agen otonom & MAS (STA-602).",
        "Inferensi simbolik deterministik; menyerahkan ML probabilistik ke "
        "STI-413 dan NLP ke STI-414.",
    ),
    "STI-308": (
        "Teori warna, tipografi, prinsip Gestalt, arsitektur informasi, "
        "wireframe, prototyping Figma, usability testing dasar (SUS/10 "
        "heuristics).",
        "Riset pengguna kualitatif mendalam & A/B testing (STC-501); koding "
        "frontend (STI-311).",
        "Purwarupa interaktif; menyerahkan riset ilmiah pengguna ke STC-501 dan "
        "frontend ke STI-311.",
    ),
    "STI-309": (
        "Model proses (Waterfall, V-Model, Scrum), arsitektur perangkat lunak, "
        "design pattern & SOLID, SQA, unit/integration testing, ISO/IEC 25010.",
        "Elisitasi kebutuhan bisnis dari nol (STI-306); EVM & kontrak proyek "
        "(STI-523).",
        "Menjamin kualitas kode; menyerahkan tata kelola jadwal/biaya ke STI-523.",
    ),
    "STI-310": (
        "Kernel OS, proses & thread, CPU scheduling, sinkronisasi & deadlock, "
        "manajemen memori virtual, file system (Linux/POSIX).",
        "Gerbang logika fisik (STI-103); konfigurasi routing/IP (STI-312); "
        "deployment Kubernetes (STB-601).",
        "Manajemen resource mesin lokal; menyerahkan interkoneksi antar-mesin "
        "ke STI-312.",
    ),
    "STI-311": (
        "HTML5/CSS3 (Flexbox, Grid), JavaScript ES6+ (DOM, Async/Await), SPA "
        "React (Hooks, Context), konsumsi REST API client-side.",
        "Koding server-side/koneksi DB (STI-416); backend business logic.",
        "Antarmuka web interaktif; menyerahkan penyediaan data server-side ke "
        "STI-416.",
    ),
    "STI-312": (
        "Model OSI & TCP/IP, subnetting VLSM/CIDR, IPv6, protokol transport, "
        "routing (OSPF), layanan jaringan (DNS/DHCP/NAT), ACL dasar.",
        "Manajemen memori OS (STI-310); konfigurasi cloud publik (STI-417); "
        "pentesting exploit (STI-519).",
        "Komunikasi data jaringan; menyerahkan komputasi cloud ke STI-417 dan "
        "keamanan ke STI-418.",
    ),
    # ============ CORE Sem 4 ============
    "STI-413": (
        "Data tabular & pipeline scikit-learn, regresi, decision tree, random "
        "forest, SVM, K-Means, PCA, hyperparameter tuning, metrik evaluasi.",
        "PyTorch/TensorFlow, CNN/RNN, deep learning (STI-626); sistem otonom "
        "BDI & teori permainan (STA-602).",
        "Pemodelan data tabular klasik; menyerahkan data tak terstruktur "
        "(citra/sekuensial) ke STI-626.",
    ),
    "STI-414": (
        "Text preprocessing, VSM, TF-IDF, N-Gram, BM25, evaluasi IR, "
        "Word2Vec/GloVe dasar, klasifikasi teks klasik (Naive Bayes, SVM teks).",
        "Transformer mendalam/LLM, RAG, LangChain (STA-702).",
        "Representasi matematis teks & pencarian dokumen; menyerahkan bahasa "
        "generatif ke STA-702.",
    ),
    "STI-415": (
        "Arsitektur DWH Kimball, star/snowflake schema, fact & dimension, SCD, "
        "pipeline ETL, OLAP, dashboard BI (Power BI/Tableau).",
        "Normalisasi 3NF OLTP (FST-207); association rule mining & klastering "
        "tingkat lanjut (STI-520).",
        "Data multidimensional & KPI; menyerahkan penemuan pola tersembunyi ke "
        "STI-520.",
    ),
    "STI-416": (
        "Arsitektur server-side, RESTful API design, JWT & RBAC, ORM/ODM, "
        "session & caching dasar (Redis), validasi input, dokumentasi "
        "Swagger/OpenAPI, deploy kontainer.",
        "Layout CSS/HTML (STI-311); message broker skala besar (STI-627); "
        "frontend mobile (STI-522).",
        "Layanan backend modular; menyerahkan aksesibilitas mobile ke STI-522 "
        "dan skalabilitas terdistribusi ke STI-627.",
    ),
    "STI-417": (
        "Model layanan IaaS/PaaS/SaaS/FaaS, virtualisasi & hypervisor, provisi "
        "VM, object storage, VPC dasar, kontainer Docker mandiri.",
        "Orkestrasi Kubernetes multi-node, Terraform IaC enterprise, CI/CD "
        "GitOps (STB-601).",
        "Fondasi provisi cloud; menyerahkan automasi & orkestrasi skala besar "
        "ke STB-601.",
    ),
    "STI-418": (
        "CIA Triad, kriptografi simetris/asimetris & hashing, digital signature, "
        "kontrol akses (RBAC), OWASP Top 10 dasar, kerangka NIST CSF & ISO 27001 "
        "pengantar.",
        "Hacking exploit web aktif, forensik memori lanjut, audit COBIT formal "
        "(STB-701); pertahanan teknis jaringan (STB-501).",
        "Prinsip keamanan; menyerahkan pertahanan jaringan ke STB-501 dan "
        "keamanan aplikasi/pentest ke STI-519.",
    ),
    # ============ CORE Sem 5 ============
    "STI-519": (
        "Penetration testing (PTES, MITRE ATT&CK), vulnerability assessment "
        "(OpenVAS/Nessus), OWASP Top 10, BurpSuite, reverse engineering dasar "
        "(Ghidra), incident response, audit ISO/IEC 27001.",
        "Konfigurasi subnetting router (STI-312); analisis risiko finansial "
        "organisasi & BCP/DRP (STB-602).",
        "Menjamin perangkat lunak prodi bebas celah keamanan kritikal; fokus "
        "layer aplikasi (Layer 7).",
    ),
    "STI-520": (
        "CRISP-DM, EDA, association rule (Apriori, FP-Growth), klastering "
        "lanjut (DBSCAN, Hierarchical), deteksi outlier (Isolation Forest, "
        "LOF), visualisasi interaktif (Plotly, Seaborn), PCA/t-SNE.",
        "Query SQL dasar & desain tabel relasional (FST-207); dashboard KPI "
        "eksekutif statis (STI-415).",
        "Menemukan pola dari data historis yang sudah diorganisasi di "
        "FST-207/STI-415.",
    ),
    "STI-521": (
        "Pemrograman ESP32, sensor analog/digital & aktuator, MQTT (Mosquitto), "
        "Node-RED, dashboard cloud IoT (ThingsBoard/Blynk), time-series DB.",
        "Deep learning video streaming CCTV / AI vision (STA-703); analitik "
        "video; perangkat keras edge AI.",
        "Dasar pengumpulan & transmisi data sensor; menyerahkan AI vision edge "
        "ke STA-703.",
    ),
    "STI-522": (
        "Flutter/Dart, lifecycle, UI widget, sensor perangkat (GPS, kamera, "
        "push), SQLite/Hive, sinkronisasi offline-to-online via REST API, "
        "rilis aplikasi.",
        "Membangun backend dari awal (konsumsi API dari STI-416); arsitektur "
        "server-side.",
        "Aplikasi mobile siap rilis; mengkonsumsi API backend yang disediakan "
        "STI-416.",
    ),
    "STI-523": (
        "Project Charter, WBS, estimasi (COCOMO II, PERT), CPM, Gantt, agile "
        "Scrum (sprint, daily, review, retrospective), Jira, manajemen risiko, "
        "Earned Value Management (CPI/SPI/EAC).",
        "Koding aplikasi & testing perangkat lunak (STI-309); strategi "
        "discovery pasar & metrik produk (STC-703).",
        "Tata kelola jadwal/biaya/sumber daya; menyerahkan kesuksesan pasar "
        "produk ke STC-703.",
    ),
    # ============ CORE Sem 6 ============
    "STI-624": (
        "Konversi model ke ONNX/TensorRT, RESTful/gRPC inference service, "
        "kontainerisasi model, RAG & vector database, load testing, monitoring "
        "laten."
    ,
        "Riset/training arsitektur deep learning dari nol (STI-626); pengaturan "
        "lifecycle MLOps penuh & CI/CD/CT (STA-701)."
    ,
        "Mengoperasikan layanan AI; menyerahkan otomasi lifecycle & monitoring "
        "drift produksi ke STA-701."
    ),
    "STI-625": (
        "Arsitektur SPBE (Perpres), Web GIS (Leaflet/Mapbox), telemetri "
        "perkotaan, interoperabilitas data (Satu Data Indonesia), masterplan "
        "smart city."
    ,
        "CeT blueprint TOGAF korporasi multi-layer (STB-703); kebijakan perda "
        "tata ruang."
    ,
        "Domain pemerintahan publik; menyerahkan arsitektur enterprise korporat "
        "ke STB-703."
    ),
    "STI-626": (
        "MLP & backpropagation, CNN (ResNet, VGG), transfer learning, object "
        "detection (YOLO), RNN/LSTM/GRU, Transformer self-attention, "
        "regularisasi, optimasi akselerasi."
    ,
        "Mengulang regresi linier/decision tree (STI-413); deployment "
        "Kubernetes, CI/CD, monitoring drift (STA-701)."
    ,
        "Menghasilkan bobot model teroptimasi; menyerahkan otomasi lifecycle & "
        "deployment ke STA-701."
    ),
    "STI-627": (
        "Microservices & DDD, event-driven, message broker (Kafka/RabbitMQ), "
        "API Gateway, circuit breaker, Saga, containerization, CI/CD pipeline, "
        "observability."
    ,
        "Koding CRUD sederhana (STI-416); tata kelola multitenansi bisnis "
        "(STC-702)."
    ,
        "Platform digital terdistribusi; menyerahkan multitenansi & monetisasi "
        "SaaS ke STC-702."
    ),
    # ============ CORE Sem 7 ============
    "STI-728": (
        "Lean Startup, problem-solution fit, MVP fungsional, metrik pertumbuhan "
        "(AARRR, CAC, LTV, Burn Rate), investor pitch deck, Demo Day."
    ,
        "Implementasi teknis deep learning/MVP rekayasa (STI-626/STI-627); "
        "desain UI (STI-308)."
    ,
        "Memvalidasi kejelasan pasar bisnis & pitching; startup yang "
        "dibina menjadi wadah penerapan capstone/PKL (Capstone FSTI, PKL)."
    ),
    # ============ PEMINATAN P1 (STA) ============
    "STA-501": (
        "Pengambilan keputusan multikriteria (SAW, WP, AHP, TOPSIS, PROMETHEE, "
        "Fuzzy AHP), uji konsistensi (CR), aplikasi web DSS interaktif, "
        "analisis sensitivitas."
    ,
        "Pemodelan ML regresi/klasifikasi data (STI-413); penyajian BI atur "
        "dimensi (STI-415)."
    ,
        "Menyerahkan perangkingan alternatif keputusan bisnis; tidak "
        "mempelajari desain ML (STI-413)."
    ),
    "STA-601": (
        "Representasi floating-point & galat (IEEE 754), akar non-linier "
        "(Newton-Raphson, Secant), solusi SPL numerik, interpolasi Spline, "
        "integrasi Romberg/Gauss-Legendre, PDB (RK4), optimasi SGD/Gradient "
        "Descent."
    ,
        "Menghitung limit/turunan murni manual tanpa kode (STI-102); melatih "
        "jaringan deep (STI-626)."
    ,
        "Algoritma aproksimasi & optimasi numerik; menyerahkan pemodelan deep "
        "learning ke STI-626."
    ),
    "STA-602": (
        "Arsitektur agen (BDI), Multi-Agent Systems (MAS), protokol FIPA-ACL, "
        "framework Python Mesa/JADE, reinforcement learning dasar, negosiasi "
        "& koordinasi agen."
    ,
        "Inferensi sistem pakar rule-based (STI-307); training deep "
        "reinforcement learning skala besar (STI-626)."
    ,
        "Agen otonom terdistribusi; menyerahkan NN besar ke STI-626 dan "
        "pengambilan keputusan tunggal ke STI-307."
    ),
    "STA-701": (
        "MLOps lifecycle (CI/CD/CT), registry model (MLflow), otomasi "
        "retraining & monitoring drift, eksperimen tracking, feature store, "
        "deployment model & canary."
    ,
        "Riset/training arsitektur model baru (STI-626); deployment layanan "
        "inference via FastAPI/ONNX mendalam (STI-624)."
    ,
        "Otomasi & tata kelola model produksi; menyerahkan pembuatan layanan "
        "inference ke STI-624."
    ),
    "STA-702": (
        "LLM/Transformer (fine-tuning), prompt engineering, RAG (LangChain, "
        "vectordb), agentic AI & tool-use, evaluasi percakapan."
    ,
        "Analisis NLP statistik klasik VSM (STI-414); layanan API web kembali "
        "(STI-416/STI-624)."
    ,
        "Bahasa generatif & percakapan; menyerahkan pencarian dokumen klasik "
        "ke STI-414."
    ),
    "STA-703": (
        "Video analytics & edge AI, deteksi objek/re-id real-time (YOLO), "
        "pengiriman telemetri, dashboard monitoring IoT, integrasi kamera."
    ,
        "Telemetri sensor ESP32 & MQTT dasar (STI-521); membangun backend web "
        "penuh."
    ,
        "Analitik AI pada video/edge; menyerahkan akuisisi sensor MQTT ke "
        "STI-521."
    ),
    # ============ PEMINATAN P2 (STB) ============
    "STB-501": (
        "IDS/IPS (Snort, Suricata), analisis PCAP (Wireshark, Zeek), akuisisi "
        "bukti digital (bit-stream image), forensik memori/disk (Autopsy, "
        "Volatility), chain of custody."
    ,
        "Pentest aplikasi web Layer 7 (STI-519); audit kepatuhan COBIT formal "
        "(STB-701)."
    ,
        "Pertahanan & investigasi jaringan; menyerahkan insiden aplikasi "
        "aplikatif ke STI-519."
    ),
    "STB-601": (
        "Infrastructure as Code (Terraform), orkestrasi Kubernetes "
        "(Deployments, StatefulSets, Ingress, PV), Helm, GitOps (ArgoCD), CI/CD "
        "pipeline kontainer."
    ,
        "Provisi VM & kontainer Docker tunggal (STI-417); arsitektur aplikasi "
        "microservices (STI-627)."
    ,
        "Automasi & orkestrasi infrastruktur; menyerahkan desain aplikasi "
        "microservices ke STI-627."
    ),
    "STB-602": (
        "Penilaian risiko kualitatif/kuantitatif (SLE, ARO, ALE), ISO/IEC "
        "27005, NIST SP 800-30, Risk Treatment Plan, BIA, BCP & DRP."
    ,
        "Alat pentest exploit teknis (STI-519); kontrol akses OWASP web "
        "(STI-416)."
    ,
        "Tata kelola risiko & keberlanjutan bisnis; menyerahkan deteksi exploit "
        "teknis ke STI-519."
    ),
    "STB-701": (
        "Tata kelola TI COBIT 2019 (EDM, APO, BAI, DSS, MEA), pemetaan "
        "kuadran strategis CMMI, metrik kinerja tata kelola."
    ,
        "Framework IT service operational (ITIL-4, STB-702); pengukuran "
        "kepatuhan teknis pentest."
    ,
        "Strategi tata kelola; menyerahkan layanan operasional berkelanjutan "
        "ke STB-702."
    ),
    "STB-702": (
        "ITIL 4 (Service Value System, praktik Core/Improve/Drive), SLA/OLA, "
        "incident, problem, change & release management, service desk."
    ,
        "Kebijakan strategi tata kelola (STB-701); audit kepatuhan keuangan "
        "(STB-701/STB-602)."
    ,
        "Layanan TI berkelanjutan; memanfaatkan otomasi infrastruktur STB-601."
    ),
    "STB-703": (
        "Pendekatan TOGAF ADM (Architecture Vision s.d. Migration), pemodelan "
        "arsitektur (ArchiMate), business/data/application/technology "
        "architecture."
    ,
        "Blueprint SPBE selesai; fokus pada proyek bisnis sistem informasi "
        "(STI-625); pemodelan UML detail (STI-306)."
    ,
        "Peta arsitektur enterprise korporat; menyerahkan sistem domain publik "
        "ke STI-625."
    ),
    # ============ PEMINATAN P3 (STC) ============
    "STC-501": (
        "Metodologi UX Research (in-depth interview, contextual inquiry), "
        "persona & CJM, kuantifikasi usability (SUS, NPS), enterprise design "
        "system, WCAG."
    ,
        "Tutorial dasar Figma & prototyping (STI-308); koding frontend "
        "(STI-311)."
    ,
        "Validasi data empiris perilaku pengguna; menyerahkan eksekusi prototipe "
        "visual ke STI-308."
    ),
    "STC-601": (
        "Otomasi proses bisnis (RPA UI Path), BPMN lanjut, pemodelan BPM "
        "(Camunda), integrasi sistem (ESB/API), middleware."
    ,
        "Elisitasi kebutuhan tahap awal (STI-306); koding aplikasi baru dari "
        "nol (STI-309)."
    ,
        "Orkestrasi proses & integrasi sistem lama; menyerahkan pengembangan "
        "aplikasi baru ke STI-309."
    ),
    "STC-602": (
        "Aplikasi industri vertikal: FinTech (transaksi, e-wallet, AML/risk "
        "rule) & EdTech (LMS, SIS, proctoring), integrasi pembayaran (payment "
        "gateway)."
    ,
        "CRUD aplikasi generik (STI-416); aturan pembayaran/transaksi di luar "
        "domain STI-416."
    ,
        "Spesialisasi domain vertikal; menyerahkan infrastruktur platform umum "
        "ke STI-627/STC-702."
    ),
    "STC-701": (
        "Teknologi XR (AR, VR, MR), 3D asset & WebGL/Three.js, interaksi "
        "kontroller & spatial, AI/Computer Vision untuk immersive."
    ,
        "Riset UX pengguna dasar (STC-501); pengembangan web 2D konvensional "
        "(STI-311/STI-416)."
    ,
        "Produk immersive interaktif; menyerahkan usability research "
        "perilaku ke STC-501."
    ),
    "STC-702": (
        "Arsitektur SaaS (multi-tenant, tenant isolation), monetisasi & "
        "metering (plan, quota), on-boarding tenant, sharing schema & shared "
        "DB."
    ,
        "Membangun microservice event-driven skalabel (STI-627); penyusunan "
        "PRD & metrik produk (STC-703)."
    ,
        "Mesin multitenansi SaaS; menyerahkan strategi go-to-market produk ke "
        "STC-703."
    ),
    "STC-703": (
        "Product vision & OKRs, Product Discovery, prioritisasi RICE/Kano, "
        "penyusunan PRD (user stories, acceptance criteria), agile product "
        "management, metrik produk (activation, retention, revenue)."
    ,
        "Manajemen jadwal/biaya/sumber daya pengembangan (STI-523); riset user "
        "behavioral (STC-501)."
    ,
        "Strategi & tanggung jawab kesuksesan produk; menyerahkan "
        "penjadwalan dividen pengembangan teknis ke STI-523."
    ),
}
print("OK", len(MK), "MK loaded;", len(BOK), "BoK mapped;", len(GUARD), "guardrail mapped.")

# ---------------------------------------------------------------------------
# RENDER
# ---------------------------------------------------------------------------
SEM_CORE = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
SEM_PEM  = {5: [], 6: [], 7: []}
for code, info in MK.items():
    if code.startswith("STI-"):
        SEM_CORE[info["sem"]].append(code)
    else:
        SEM_PEM[info["sem"]].append(code)

# urutkan kode berdasarkan nomor urut dok 007 (kontinu)
def key(code):
    num = "".join(ch for ch in code if ch.isdigit())
    return (len(num), num)

out = []
out.append("# 043 — MATRIKS CPL, CPMK, BoK, DAN BOUNDARY GUARDRAILS PER MATA KULIAH")
out.append("## Matriks Kompilasi Per Semester — Core STI & Peminatan (Kurikulum OBE SISTEKIN 2026)")
out.append("")
out.append("**Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang**")
out.append("")
out.append("> Dokumen kerja ini mengikat **CPL yang Dibebankan**, **Rumusan CPMK (ABCD + Level Bloom)**, **Bahan Kajian (BoK)**, dan **Boundary Guardrails (IN-SCOPE / OUT-OF-SCOPE / Handoff Anchor)** untuk setiap mata kuliah, disusun **per semester**. Urutan: **Bagian A — MK Core Prodi (STI)**; **Bagian B — MK Peminatan (STA/STB/STC)** per jalur.")
out.append("")
out.append("**Sumber data:** Dok 005 (struktur semester & SKS), Dok 007 (CPL & CPMK ABCD), Dok 037 (BoK & Boundary Guardrails). *Primer untuk BoK sesuai Batas yang ditetapkan Dok 037; untuk beberapa MK core yang tidak dibahas eksplisit di klaster Dok 037, BoK dirujuk dari katalog BoK bagian 2 Dok 037 berdasarkan isi CPMK.*")
out.append("")
out.append("---")
out.append("")

def mk_block(sem, no, code):
    info = MK[code]
    cpl_ov = CPL.get(code, "") or ""
    bok = BOK.get(code, [])
    bok_str = " & ".join(f"`{b}` {BOK_NAME.get(b,'')}" for b in bok)
    g = GUARD.get(code, ("", "", ""))
    cpmk_rows = CPMK.get(code, [])
    out.append(f"### {no}. {code} — {info['nama']}")
    out.append("")
    out.append(f"| Atribut | Spesifikasi |")
    out.append("|---|---|")
    out.append(f"| **Semester / SKS / Tipe** | {info['sem']} / {info['sks']} SKS / {info['tipe']} |")
    out.append(f"| **Rumpun MK** | {info['rumpun']} |")
    out.append(f"| **Prasyarat** | {info['prasy']} |")
    out.append(f"| **CPL yang Dibebankan** | {cpl_ov} |")
    out.append(f"| **Bahan Kajian (BoK)** | {bok_str} |")
    out.append("")
    out.append("**CPMK (Capaian Pembelajaran Mata Kuliah):**")
    out.append("")
    out.append("| Kode | Rumusan CPMK (ABCD) | Bloom | CPL |")
    out.append("|---|---|:--:|:--:|")
    for c in cpmk_rows:
        cpl_cell = c['cpl']  # sudah bersih dari backtick di _extract_007
        out.append(f"| **{c['k']}** | {c['rum']} | **{c['bloom']}** | `{cpl_cell}` |")
    out.append("")
    out.append("**Boundary Guardrails** (dari Dok 037):")
    out.append("")
    out.append("| Guardrail | Batas Materi |")
    out.append("|---|---|")
    out.append(f"| **IN-SCOPE** (wajib diajarkan) | {g[0]} |")
    out.append(f"| **OUT-OF-SCOPE** (dilarang) | {g[1]} |")
    out.append(f"| **Handoff Anchor** (titik transisi) | {g[2]} |")
    out.append("")
    out.append("---")
    out.append("")

# ---------------- BAGIAN A: CORE STI ----------------
out.append("## BAGIAN A — MATRIKS MK CORE PRODI (STI) PER SEMESTER")
out.append("")
no = 1
for sem in sorted(SEM_CORE):
    if not SEM_CORE[sem]:
        continue
    out.append(f"### A-{sem}. SEMESTER {sem}")
    out.append("")
    for code in sorted(SEM_CORE[sem], key=key):
        mk_block(sem, no, code)
        no += 1

# ---------------- BAGIAN B: PEMINATAN ----------------
out.append("## BAGIAN B — MATRIKS MK PEMINATAN PER SEMESTER")
out.append("")
nama_lintasan = {"STA": "P1 Integrated Smart Systems", "STB": "P2 Cloud Infrastructure & Cybersecurity", "STC": "P3 Digital Platform Engineering"}
for sem in sorted(SEM_PEM):
    if not SEM_PEM[sem]:
        continue
    out.append(f"### B-{sem}. SEMESTER {sem}")
    out.append("")
    for depend in ("STA", "STB", "STC"):
        for code in sorted([c for c in SEM_PEM[sem] if c.startswith(depend)], key=key):
            mk_block(sem, no, code)
            no += 1

dest = os.path.join(REV, "043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md")
open(dest, "w", encoding="utf-8").write("\n".join(out))
print("WROTE", dest, len(out), "lines")
