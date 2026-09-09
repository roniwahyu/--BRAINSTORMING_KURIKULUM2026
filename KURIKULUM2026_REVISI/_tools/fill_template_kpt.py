# -*- coding: utf-8 -*-
"""
Fill Template_KPT_2024.docx (FSTI UWG) with SISTEKIN 2026 curriculum content.
Produces BUKU_KPT_SISTEKIN_2026_FINAL.docx
"""
import copy
from docx import Document
from docx.shared import Pt

SRC = "D:/!!MYDOCUMENTS2026/!!!SISTEKIN2026/!!BRAINSTORMING_KURIKULUM2026/KURIKULUM2026_REVISI/BUKU_KPT_SISTEKIN_2026_FINAL.docx"

doc = Document(SRC)

# ============================================================
# 1. PLACEHOLDER REPLACEMENT MAP
# ============================================================
R = {
    "[Nama Program Studi]": "Sistem dan Teknologi Informasi (SISTEKIN)",
    "[NAMA PROGRAM STUDI]": "SISTEM DAN TEKNOLOGI INFORMASI",
    "[TAHUN]": "2026",
    "[TAHUN KURIKULUM]": "2026",
    "[Tanggal Bulan Tahun]": "Malang, September 2026",
    "[Nama Kaprodi]": "Ketua Program Studi SISTEKIN",
    "[bidang keilmuan prodi]": "sistem dan teknologi informasi cerdas",
    "[bidang ilmu]": "sistem dan teknologi informasi",
    "[jumlah semester]": "8",
    "[jumlah SKS]": "146",
    "[jumlah SKS.]": "146",
    "[Gelar Lulusan]": "S.Kom.",
    "[Tuliskan visi keilmuan program studi]": (
        "Menjadi Program Studi Sistem dan Teknologi Informasi yang bermutu, mandiri, "
        "bermartabat, dan berwawasan global, serta unggul dalam pengembangan sistem dan "
        "teknologi informasi cerdas terintegrasi kecerdasan artifisial, serta "
        "technopreneurship berbasis kebutuhan masyarakat dan industri pada tahun 2045."
    ),
    "[Isi sesuai dokumen resmi universitas/fakultas]": (
        "[PERLU DATA UPPS] — kutipan VMTS Universitas/Fakultas beserta nomor SK penetapannya "
        "(Statuta & Renstra UWG, Dokumen VMTS FSTI)."
    ),
}

def replace_in_text(text):
    for k, v in R.items():
        text = text.replace(k, v)
    return text

# Replace in paragraphs (body)
for p in doc.paragraphs:
    for run in p.runs:
        if run.text:
            run.text = replace_in_text(run.text)

# Replace in tables (all cells)
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                for run in p.runs:
                    if run.text:
                        run.text = replace_in_text(run.text)

# Replace in headers/footers
for section in doc.sections:
    for p in section.header.paragraphs + section.footer.paragraphs:
        for run in p.runs:
            if run.text:
                run.text = replace_in_text(run.text)

# ============================================================
# 2. HELPERS
# ============================================================
def set_cell(cell, text, bold=False):
    """Clear a cell and set single-run text, preserving paragraph."""
    cell.text = ""
    p = cell.paragraphs[0]
    run = p.add_run(text)
    run.bold = bold

def fill_table_row(table, row_idx, values):
    """Fill a row of a table with list of string values."""
    row = table.rows[row_idx]
    for i, val in enumerate(values):
        if i < len(row.cells):
            set_cell(row.cells[i], val)

def duplicate_row(table, src_idx):
    """Duplicate a row (deep copy) and append to table end."""
    src = table.rows[src_idx]._tr
    new_tr = copy.deepcopy(src)
    table._tbl.append(new_tr)
    return table.rows[-1]

# ============================================================
# 3. FILL KEY TABLES
# Table index reference (from template inspection):
#  0=cover identitas, 1=pengesahan, 2=daftar singkatan, 3=identitas prodi,
#  4=evaluasi aspek, 5=stakeholder, 6=benchmarking, 7=tujuan-strategi,
#  8=PEO, 9=Profil Lulusan, 10=CPL, 11=matriks PL-CPL, 12=CPL-KKNI,
#  13=BK, 14=matriks CPL-BK, 15=kedalaman BK, 16=eval MK lama,
#  17=MK baru, 18=daftar MK, 19=rekapitulasi MK,
#  20..27 = struktur semester 1..8, 28=rekapitulasi SKS,
#  29=matriks CPL-MK, 30=konsentrasi, 31=komponen RPS,
#  32=MBKM semester, 33=rekognisi BKP, 34=matriks penilaian CPL
# ============================================================

# --- Table 3: Identitas Program Studi (16 rows: header + 15) ---
t = doc.tables[3]
identitas = {
    0: "Nama Perguruan Tinggi", 1: "Universitas Widyagama Malang",
    2: "Fakultas", 3: "Fakultas Sains dan Teknologi Informasi (FSTI)",
    4: "Nama Program Studi", 5: "Sistem dan Teknologi Informasi (SISTEKIN)",
    6: "Jenjang Pendidikan", 7: "Sarjana (S1) — KKNI Level 6",
    8: "Gelar Lulusan", 9: "S.Kom. [PERLU KONFIRMASI UPPS]",
    10: "Peringkat Akreditasi", 11: "[PERLU DATA UPPS — LAM INFOKOM/BAN-PT]",
    12: "Tahun Kurikulum", 13: "2026",
    14: "Visi Keilmuan Program Studi", 15: R["[Tuliskan visi keilmuan program studi]"],
}
# Fill rows 1..15 (data rows) of Table 3
for r_idx in range(1, len(t.rows)):
    cells = t.rows[r_idx].cells
    if len(cells) >= 2:
        # find label in first cell
        label = cells[0].text.strip()
        # map by row position (16 rows: 1 header + 15 data)
        pass

# ============================================================
# Table 3 uses 2-col layout; fill by enumerating actual rows
# ============================================================
t3_data = [
    ("Nama Perguruan Tinggi", "Universitas Widyagama Malang"),
    ("Fakultas", "Fakultas Sains dan Teknologi Informasi (FSTI)"),
    ("Nama Program Studi", "Sistem dan Teknologi Informasi (SISTEKIN)"),
    ("Jenjang Pendidikan", "Sarjana (S1) — KKNI Level 6"),
    ("Gelar Lulusan", "S.Kom. [PERLU KONFIRMASI UPPS]"),
    ("Peringkat Akreditasi", "[PERLU DATA UPPS — LAM INFOKOM/BAN-PT]"),
    ("Tahun Kurikulum", "2026"),
    ("Masa Tempuh", "8 semester (4 tahun); akselerasi 7 semester"),
    ("Beban Belajar", "146 SKS / 55 MK (minimal nasional 144 SKS)"),
    ("Website Program Studi", "[PERLU DATA UPPS]"),
    ("Email Program Studi", "[PERLU DATA UPPS]"),
    ("Nomor SK Izin Penyelenggaraan", "[PERLU DATA UPPS]"),
    ("Visi Keilmuan Program Studi", "Lihat Bab IV (VMTS 2045)"),
]
# Fill existing rows and add rows if needed
for i, (label, val) in enumerate(t3_data):
    target = i + 1
    if target < len(t.rows):
        cells = t.rows[target].cells
        if len(cells) >= 2:
            set_cell(cells[0], label, bold=True)
            set_cell(cells[1], val)
    else:
        r = duplicate_row(t, 1)
        cells = r.cells
        if len(cells) >= 2:
            set_cell(cells[0], label, bold=True)
            set_cell(cells[1], val)

# ============================================================
# Table 8: PEO (header + 5 rows) -> fill 3 PEO, clear rest
# ============================================================
t = doc.tables[8]
peos = [
    ("PEO-1", "Professional Practice and Systems Integration — Dalam 3–5 tahun setelah lulus, alumni mampu berkarier secara profesional dalam menganalisis, merancang, mengembangkan, mengintegrasikan, mengamankan, atau mengelola sistem dan teknologi informasi cerdas sesuai kebutuhan organisasi, industri, dan masyarakat."),
    ("PEO-2", "Digital Innovation and Technopreneurship — Dalam 3–5 tahun setelah lulus, alumni mampu menghasilkan inovasi, produk, layanan, perbaikan proses, atau usaha digital yang relevan, etis, berkelanjutan, dan memberikan nilai tambah bagi pengguna, organisasi, industri, atau masyarakat."),
    ("PEO-3", "Advanced Study, Research, and Lifelong Learning — Dalam 3–5 tahun setelah lulus, alumni mampu mengembangkan kompetensi melalui studi lanjut (S2/S3), penelitian terapan, sertifikasi profesional, komunitas keilmuan, atau pembelajaran sepanjang hayat serta menunjukkan kepemimpinan sesuai konteksnya."),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(peos):
        set_cell(cells[0], peos[i-1][0], bold=True)
        set_cell(cells[1], peos[i-1][1])
    else:
        set_cell(cells[0], "")
        set_cell(cells[1], "")

# ============================================================
# Table 9: Profil Lulusan (header + 5 rows) -> fill 4 PL
# ============================================================
t = doc.tables[9]
pls = [
    ("PL-1", "Intelligent Information Systems & Data/AI Engineer", "Sarjana yang mampu menganalisis kebutuhan organisasi, merancang arsitektur sistem informasi cerdas terintegrasi, merekayasa pipeline data, mengembangkan model ML/DL, serta menerapkan MLOps ke aplikasi enterprise nyata."),
    ("PL-2", "Cloud Infrastructure, Cybersecurity & Smart Systems Integrator", "Sarjana yang mampu merancang dan mengelola infrastruktur cloud (Cloud Native/DevOps), mengintegrasikan IoT dan sistem cerdas, mengamankan aset informasi, serta menegakkan tata kelola dan audit TI."),
    ("PL-3", "UI/UX Designer & Digital Platform Engineer", "Sarjana yang mampu merancang pengalaman pengguna berbasis riset (UI/UX), merekayasa antarmuka modern, membangun arsitektur microservices, serta mengintegrasikan platform digital terdistribusi skala besar."),
    ("PL-4", "Digital Technopreneur & IT Product Innovator", "Sarjana berjiwa kewirausahaan teknologi yang mampu memvalidasi pasar, merancang model bisnis (Lean Startup), membangun MVP, mengelola proyek Agile/Scrum, serta mendirikan tech startup berbasis sistem cerdas."),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(pls):
        set_cell(cells[0], pls[i-1][0], bold=True)
        set_cell(cells[1], pls[i-1][1])
        if len(cells) > 2:
            set_cell(cells[2], pls[i-1][2])
    else:
        for c in cells:
            set_cell(c, "")

# ============================================================
# Table 10: CPL (header + rows) -> 14 CPL
# ============================================================
t = doc.tables[10]
cpls = [
    ("S1", "Bertakwa kepada Tuhan Yang Maha Esa, menginternalisasi nilai, norma, etika digital dan hukum profesi, menjunjung tinggi kejujuran dan integritas, mampu bekerja sama secara produktif dalam tim lintas disiplin, serta menunjukkan sikap tanggung jawab atas pekerjaan di bidang keahliannya secara mandiri."),
    ("KU1", "Mampu menerapkan pemikiran logis, kritis, sistematis, dan inovatif dalam menganalisis permasalahan komputasi serta mengkaji implikasi pengembangan atau implementasi iptek sesuai kaidah, tata cara, dan etika ilmiah."),
    ("KU2", "Mampu mengomunikasikan gagasan, rancangan arsitektur, dan solusi teknis secara efektif baik lisan maupun tulisan, serta memelihara dan mengembangkan jaringan kerja kolaboratif dengan pemangku kepentingan industri."),
    ("KU3", "Mampu mengambil keputusan yang tepat berdasarkan analisis data dan informasi, bertanggung jawab atas pencapaian hasil kerja kelompok, melakukan evaluasi diri, serta mengelola pembelajaran mandiri sepanjang hayat (lifelong learning)."),
    ("P1", "Menguasai konsep dasar sains, matematika terapan (kalkulus, aljabar linear, statistika, matematika diskrit, logika) sebagai fondasi pemecahan masalah rekayasa sistem informasi dan komputasi cerdas yang kompleks."),
    ("P2", "Menguasai konsep teoretis sistem informasi, analisis & perancangan sistem, arsitektur enterprise, metodologi pengembangan perangkat lunak, serta proses bisnis organisasi untuk transformasi digital."),
    ("P3", "Menguasai prinsip dan konsep infrastruktur TI, jaringan komputer, komputasi awan (cloud), keamanan informasi & siber, tata kelola TI, serta manajemen proyek sistem dan teknologi informasi."),
    ("P4", "Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX)."),
    ("KK1", "Mampu menganalisis, merancang, dan mengembangkan sistem informasi cerdas terintegrasi kecerdasan artifisial (AI/ML, NLP, Computer Vision, Smart Sys, DSS) guna memecahkan masalah kompleks organisasi dan industri."),
    ("KK2", "Mampu merekayasa pipeline data skala besar (Data Engineering), membangun model machine learning/deep learning, serta menerapkan MLOps untuk solusi analitik dan visualisasi data bisnis."),
    ("KK3", "Mampu merancang, mengintegrasikan, dan mengelola infrastruktur komputasi awan (Cloud/DevOps), sistem sensor cerdas (IoT), dan ketahanan siber (Cybersecurity) secara andal, terukur, dan aman."),
    ("KK4", "Mampu merancang tata kelola TI (IT Governance), melakukan audit sistem informasi, serta memastikan kepatuhan terhadap standar industri dan manajemen risiko (COBIT, ITIL, ISO 27001)."),
    ("KK5", "Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (Microservices, Web/Mobile, API, SaaS, BPA)."),
    ("KK6", "Mampu merancang, memvalidasi model bisnis (Lean Startup/MVP), mengelola proyek agile, serta mendirikan usaha rintisan teknologi (technopreneurship) mandiri berbasis kebutuhan pasar."),
]
# Fill existing rows (header + 9 data = 10 rows), expand to 14
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(cpls):
        set_cell(cells[0], cpls[i-1][0], bold=True)
        set_cell(cells[1], cpls[i-1][1])
# Add remaining rows
for i in range(len(t.rows) - 1, len(cpls)):
    r = duplicate_row(t, 1)
    cells = r.cells
    set_cell(cells[0], cpls[i][0], bold=True)
    set_cell(cells[1], cpls[i][1])

# ============================================================
# Table 13: Bahan Kajian (header + rows) -> 36 BK
# ============================================================
t = doc.tables[13]
bks = [
    ("BK-IS01", "Foundations of Information Systems", "Konsep dasar sistem informasi, peran SI dalam organisasi, jenis-jenis SI, dan dampaknya terhadap proses bisnis."),
    ("BK-IS02", "Data and Information Management", "Pemodelan data, perancangan basis data relasional, SQL, NoSQL, integritas dan keamanan data."),
    ("BK-IS03", "IT Infrastructure and Networking", "Arsitektur infrastruktur TI, jaringan komputer, perangkat keras, dan komponen pendukung sistem."),
    ("BK-IS04", "Enterprise Architecture", "Arsitektur enterprise (TOGAF), penyelarasan strategi bisnis dengan TI, dan blueprint sistem organisasi."),
    ("BK-IS05", "IS Management and Governance", "Tata kelola TI (COBIT), manajemen layanan TI (ITIL), dan kepemimpinan sistem informasi."),
    ("BK-IS06", "Information Security and Risk Management", "Keamanan informasi, manajemen risiko, CIA Triad, ISO 27001, NIST CSF, dan BCP/DRP."),
    ("BK-IS07", "Systems Analysis and Design", "Analisis dan perancangan sistem, SDLC, pemodelan proses, dan desain arsitektur aplikasi."),
    ("BK-IS08", "Project Management", "Manajemen proyek TI, PMBOK, Agile/Scrum, perencanaan, eksekusi, dan pengendalian proyek."),
    ("BK-IS09", "Business Process Management", "Pemodelan proses bisnis (BPMN), perbaikan proses, otomasi, dan workflow."),
    ("BK-IS10", "Applied Mathematics and Logic", "Matematika terapan, logika proposisi, aljabar boolean, dan komputasi saintifik."),
    ("BK-IS11", "Programming Fundamentals & Object-Oriented", "Dasar pemrograman, struktur data, algoritma, dan paradigma berorientasi objek."),
    ("BK-IS12", "Web and Mobile Application Development", "Pengembangan aplikasi web dan mobile, frontend, backend, dan integrasi layanan."),
    ("BK-IS13", "Data Analytics and Business Intelligence", "Analisis data, business intelligence, data warehouse, dan visualisasi data."),
    ("BK-IS14", "IT Audit and Compliance", "Audit sistem informasi, kepatuhan regulasi, dan pengendalian internal TI."),
    ("BK-IS15", "Digital Innovation and Entrepreneurship", "Inovasi digital, model bisnis, kewirausahaan teknologi, dan transformasi digital."),
    ("BK-IS16", "Artificial Intelligence & Intelligent Systems", "Kecerdasan artifisial, sistem cerdas, representasi pengetahuan, dan penalaran."),
    ("BK-IS17", "Human-Computer Interaction & UX", "Interaksi manusia-komputer, usability, desain pengalaman pengguna, dan prototyping."),
    ("BK-IS18", "Machine Learning and Data Science", "Machine learning, data science, deep learning, dan operasionalisasi model (MLOps)."),
    ("BK-IS19", "Cloud Architecture & DevOps", "Arsitektur cloud, virtualisasi, kontainerisasi, CI/CD, dan DevOps."),
    ("BK-IS20", "Ethics, Use and Implications for Society", "Etika profesi, dampak sosial teknologi, privasi data, dan hukum digital."),
    ("BK-IS21", "Internship and Professional Practice", "Pengalaman kerja profesional, magang, dan praktik industri."),
    ("BK-IT01", "Information Technology Fundamentals", "Fondasi teknologi informasi, komponen sistem komputer, dan dasar komputasi."),
    ("BK-IT02", "Applied AI & Intelligent Technologies", "AI terapan, machine learning, NLP, computer vision, dan intelligent agent."),
    ("BK-IT03", "Networking & Communications", "Jaringan komputer, protokol, arsitektur jaringan, dan komunikasi data."),
    ("BK-IT04", "Platform Technologies & Web/Mobile", "Teknologi platform, web, mobile, dan arsitektur aplikasi modern."),
    ("BK-IT05", "Cloud Computing & Virtualization", "Cloud computing, virtualisasi, orkestrasi, dan manajemen infrastruktur cloud."),
    ("BK-IT06", "Cybersecurity Principles & Defense", "Prinsip keamanan siber, pertahanan, forensik, dan kriptografi."),
    ("BK-IT07", "System Integration and Architecture", "Integrasi sistem, arsitektur SOA/microservices, dan interoperabilitas."),
    ("BK-IT08", "IT Service Management & Governance", "Manajemen layanan TI, tata kelola, dan kepatuhan industri."),
    ("BK-IT09", "Data Analytics & Information Visualization", "Analisis data, visualisasi informasi, dan dashboard."),
    ("BK-IT10", "User Experience & Interaction Design", "UX, desain interaksi, usability testing, dan aksesibilitas."),
    ("BK-IT11", "Software Development Practices", "Praktik pengembangan perangkat lunak, kualitas kode, dan testing."),
    ("BK-IT12", "IT Risk Management and Compliance", "Manajemen risiko TI, kepatuhan, dan audit keamanan."),
    ("BK-IT13", "Technology Entrepreneurship", "Technopreneurship, startup, dan inovasi produk teknologi."),
    ("BK-IT14", "IoT and Embedded Smart Systems", "Internet of Things, sistem embedded, sensor, dan smart systems."),
    ("BK-IT15", "Global Professional Practice", "Praktik profesional global, komunikasi teknis, dan etika lintas budaya."),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(bks):
        set_cell(cells[0], bks[i-1][0], bold=True)
        set_cell(cells[1], bks[i-1][1])
        if len(cells) > 2:
            set_cell(cells[2], bks[i-1][2])
for i in range(len(t.rows) - 1, len(bks)):
    r = duplicate_row(t, 1)
    cells = r.cells
    set_cell(cells[0], bks[i][0], bold=True)
    set_cell(cells[1], bks[i][1])
    if len(cells) > 2:
        set_cell(cells[2], bks[i][2])

# ============================================================
# Table 19: Rekapitulasi MK (header + rows)
# ============================================================
t = doc.tables[19]
rekap = [
    ("Mata Kuliah Wajib Umum (MKWU)", "8 MK", "13 SKS"),
    ("Mata Kuliah Wajib Fakultas (FSTI)", "13 MK", "36 SKS"),
    ("Mata Kuliah Inti Program Studi (Core STI)", "28 MK", "79 SKS"),
    ("Mata Kuliah Pilihan Peminatan (Elektif)", "6 MK", "18 SKS"),
    ("TOTAL PAKET DITEMPUH MAHASISWA", "55 MK", "146 SKS"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(rekap):
        set_cell(cells[0], rekap[i-1][0])
        set_cell(cells[1], rekap[i-1][1])
        set_cell(cells[2], rekap[i-1][2])

# ============================================================
# Table 28: Rekapitulasi SKS per Semester (header + 9 rows)
# ============================================================
t = doc.tables[28]
sks_sem = [
    ("Semester 1", "19"),
    ("Semester 2", "20"),
    ("Semester 3", "20"),
    ("Semester 4", "21"),
    ("Semester 5", "21"),
    ("Semester 6", "19"),
    ("Semester 7", "20"),
    ("Semester 8", "6"),
    ("TOTAL", "146"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(sks_sem):
        set_cell(cells[0], sks_sem[i-1][0])
        set_cell(cells[1], sks_sem[i-1][1])

# ============================================================
# Table 30: Konsentrasi/Peminatan (header + 3 rows)
# ============================================================
t = doc.tables[30]
peminatan = [
    ("P1: Integrated Smart Systems", "STA-01..STA-06 (Decision Support, Computational Methods, Intelligent Agent, MLOps, Conversational AI, Smart Surveillance)", "18 SKS (6 MK)", "Sem 5, 6, 7"),
    ("P2: Cloud Infrastructure & Cybersecurity", "STB-01..STB-06 (Network Security, Cloud/DevOps, Cyber Risk Mgmt, IT Governance, ITIL, TOGAF)", "18 SKS (6 MK)", "Sem 5, 6, 7"),
    ("P3: Digital Platform Engineering", "STC-01..STC-06 (UX Research, BPA, Vertical App, XR, SaaS, Product Mgmt)", "18 SKS (6 MK)", "Sem 5, 6, 7"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(peminatan):
        set_cell(cells[0], peminatan[i-1][0])
        set_cell(cells[1], peminatan[i-1][1])
        set_cell(cells[2], peminatan[i-1][2])
        set_cell(cells[3], peminatan[i-1][3])

# ============================================================
# Table 18: Daftar Mata Kuliah (header + rows) -> 55 MK
# ============================================================
t = doc.tables[18]
mks = [
    # (No, Kode, Nama, SKS, Semester, Jenis, Prasyarat)
    ("1","MKU-101","Agama I","2","1","MKWU","—"),
    ("2","MKU-102","Pancasila","2","1","MKWU","—"),
    ("3","MKU-103","Bahasa Indonesia","2","1","MKWU","—"),
    ("4","FST-101","Dasar Teknologi Digital","2","1","FSTI","—"),
    ("5","FST-102","Algoritma dan Pemrograman","3","1","FSTI","—"),
    ("6","STI-101","Pengantar Sistem dan Teknologi Informasi","2","1","Core STI","—"),
    ("7","STI-102","Kalkulus","3","1","Core STI","—"),
    ("8","STI-103","Arsitektur dan Organisasi Sistem Teknologi Informasi","3","1","Core STI","—"),
    ("9","MKU-204","Kewirausahaan I","2","2","MKWU","—"),
    ("10","FST-203","Struktur Data dan Algoritma","3","2","FSTI","FST-102"),
    ("11","FST-204","Pengantar Kecerdasan Artifisial & Data","2","2","FSTI","FST-101"),
    ("12","FST-205","Basic English for IT","2","2","FSTI","—"),
    ("13","FST-206","Etika Profesi & Hukum Digital","2","2","FSTI","—"),
    ("14","FST-207","Sistem Basis Data","3","2","FSTI","FST-102"),
    ("15","STI-204","Matematika Diskrit dan Logika","3","2","Core STI","STI-103"),
    ("16","STI-205","Aljabar Linear dan Matriks","3","2","Core STI","STI-102"),
    ("17","STI-306","Analisis dan Perancangan Sistem Informasi","3","3","Core STI","STI-101, FST-207"),
    ("18","STI-307","Sistem Cerdas","2","3","Core STI","STI-204, FST-204"),
    ("19","STI-308","UI/UX Design & Prototyping","3","3","Core STI","FST-101"),
    ("20","STI-309","Rekayasa Perangkat Lunak","3","3","Core STI","FST-203"),
    ("21","STI-310","Sistem Operasi","3","3","Core STI","STI-103"),
    ("22","STI-311","Web Front End Development","3","3","Core STI","FST-102"),
    ("23","STI-312","Jaringan Komputer","3","3","Core STI","STI-103"),
    ("24","STI-413","Machine Learning","3","4","Core STI","STI-205, STI-307"),
    ("25","STI-414","Pengantar NLP & Information Retrieval","2","4","Core STI","STI-307"),
    ("26","STI-415","Data Warehouse & Business Intelligence","3","4","Core STI","FST-207"),
    ("27","STI-416","Web Back End Development","3","4","Core STI","FST-207, STI-311"),
    ("28","STI-417","Komputasi Awan (Cloud Computing)","3","4","Core STI","STI-312, STI-310"),
    ("29","STI-418","Dasar Keamanan Informasi","2","4","Core STI","STI-312"),
    ("30","FST-408","Probabilitas dan Statistika","3","4","FSTI","STI-102"),
    ("31","MKU-405","Kewarganegaraan","2","4","MKWU","—"),
    ("32","STI-519","Keamanan Informasi Lanjut","3","5","Core STI","STI-418"),
    ("33","STI-520","Data Mining & Visualisasi Data","3","5","Core STI","STI-413, STI-415"),
    ("34","STI-521","Internet of Things (IoT)","3","5","Core STI","STI-312, STI-310"),
    ("35","STI-522","Pemrograman Aplikasi Mobile","3","5","Core STI","STI-311, STI-416"),
    ("36","STI-523","Manajemen Proyek TI","3","5","Core STI","STI-306, STI-309"),
    ("37","MKU-507","Kuliah Pengabdian Kepada Masyarakat (KPM)","3","5","MKWU","≥80 SKS"),
    ("38","—","MK Pilihan Peminatan 1","3","5","Peminatan","sesuai jalur"),
    ("39","STI-624","Integrasi Layanan Cerdas Berbasis AI","3","6","Core STI","STI-413, STI-416"),
    ("40","STI-625","Smart City & Pemerintahan Digital","2","6","Core STI","STI-521"),
    ("41","STI-626","Deep Learning & Neural Networks","3","6","Core STI","STI-413"),
    ("42","STI-627","Digital Platform Engineering","3","6","Core STI","STI-416"),
    ("43","FST-611","Metodologi Penelitian","2","6","FSTI","≥76 SKS"),
    ("44","—","MK Pilihan Peminatan 2","3","6","Peminatan","sesuai jalur"),
    ("45","—","MK Pilihan Peminatan 3","3","6","Peminatan","sesuai jalur"),
    ("46","STI-728","Inovasi Teknologi dan Startup Digital","3","7","Core STI","STI-627, MKU-204"),
    ("47","FST-610","Capstone Project FSTI","3","7","FSTI","STI-523, ≥100 SKS"),
    ("48","FST-612","Praktik Kerja Lapangan (PKL)","3","7","FSTI","≥100 SKS"),
    ("49","FST-613","Pra-Skripsi / Seminar Proposal","2","7","FSTI","FST-611, ≥100 SKS"),
    ("50","—","MK Pilihan Peminatan 4","3","7","Peminatan","sesuai jalur"),
    ("51","—","MK Pilihan Peminatan 5","3","7","Peminatan","sesuai jalur"),
    ("52","—","MK Pilihan Peminatan 6","3","7","Peminatan","sesuai jalur"),
    ("53","FST-714","Skripsi / Tugas Akhir","6","8","FSTI","FST-613, ≥120 SKS"),
]
# Table 18 header: No | Kode MK | Nama | SKS | Semester | Jenis MK | Prasyarat
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(mks):
        for j in range(min(7, len(cells))):
            set_cell(cells[j], mks[i-1][j])
for i in range(len(t.rows) - 1, len(mks)):
    r = duplicate_row(t, 1)
    cells = r.cells
    for j in range(min(7, len(cells))):
        set_cell(cells[j], mks[i][j])

# ============================================================
# SAVE
# ============================================================
doc.save(SRC)
print("SAVED:", SRC)
print("Tables:", len(doc.tables))
print("Paragraphs:", len(doc.paragraphs))
