# -*- coding: utf-8 -*-
import os
import re
import glob

workdir = r"d:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI"

# Define the Master Canonical 67 Courses (55 Paket Ditempuh + 12 Elektif Tambahan)
CANONICAL_COURSES = {
    # MKWU (8 MK / 13 SKS)
    "MKU-101": ("Agama I", 2, 1, "MKWU"),
    "MKU-102": ("Pancasila", 2, 1, "MKWU"),
    "MKU-103": ("Bahasa Indonesia", 2, 1, "MKWU"),
    "MKU-204": ("Kewirausahaan I", 2, 2, "MKWU"),
    "MKU-405": ("Kewarganegaraan", 2, 4, "MKWU"),
    "MKU-406": ("Agama II", 0, 4, "MKWU"),
    "MKU-507": ("Kuliah Pengabdian Masyarakat", 3, 5, "MKWU"),
    "MKU-508": ("Kewirausahaan II", 0, 5, "MKWU"),
    
    # FSTI Common Core (13 MK / 36 SKS)
    "FST-101": ("Dasar Teknologi Digital", 2, 1, "FSTI"),
    "FST-102": ("Algoritma dan Pemrograman", 3, 1, "FSTI"),
    "FST-203": ("Struktur Data dan Algoritma", 3, 2, "FSTI"),
    "FST-204": ("Pengantar Kecerdasan Artifisial & Data", 2, 2, "FSTI"),
    "FST-205": ("Basic English for IT", 2, 2, "FSTI"),
    "FST-206": ("Etika Profesi & Hukum Digital", 2, 2, "FSTI"),
    "FST-207": ("Sistem Basis Data", 3, 2, "FSTI"),
    "FST-408": ("Probabilitas dan Statistika", 3, 4, "FSTI"),
    "FST-610": ("Capstone Project FSTI", 3, 7, "FSTI"),
    "FST-611": ("Metodologi Penelitian", 2, 6, "FSTI"),
    "FST-612": ("Praktik Kerja Lapangan", 3, 7, "FSTI"),
    "FST-613": ("Pra-Skripsi", 2, 7, "FSTI"),
    "FST-714": ("Skripsi", 6, 8, "FSTI"),

    # Core STI (28 MK / 79 SKS)
    "STI-101": ("Pengantar Sistem dan Teknologi Informasi", 2, 1, "Core STI"),
    "STI-102": ("Kalkulus", 3, 1, "Core STI"),
    "STI-103": ("Arsitektur dan Organisasi Sistem Teknologi Informasi", 3, 1, "Core STI"),
    "STI-201": ("Matematika Diskrit dan Logika", 3, 2, "Core STI"),
    "STI-202": ("Aljabar Linear dan Matriks", 3, 2, "Core STI"),
    "STI-301": ("Analisis dan Perancangan Sistem Informasi", 3, 3, "Core STI"),
    "STI-302": ("Sistem Cerdas", 2, 3, "Core STI"),
    "STI-303": ("UI/UX Design & Prototyping", 3, 3, "Core STI"),
    "STI-304": ("Rekayasa Perangkat Lunak", 3, 3, "Core STI"),
    "STI-305": ("Sistem Operasi", 3, 3, "Core STI"),
    "STI-306": ("Web Front End Development", 3, 3, "Core STI"),
    "STI-307": ("Jaringan Komputer", 3, 3, "Core STI"),
    "STI-401": ("Machine Learning", 3, 4, "Core STI"),
    "STI-402": ("Data Warehouse & Business Intelligence", 3, 4, "Core STI"),
    "STI-403": ("Pengantar NLP & Temu Balik Informasi", 2, 4, "Core STI"),
    "STI-404": ("Komputasi Awan", 3, 4, "Core STI"),
    "STI-405": ("Dasar Keamanan Informasi", 2, 4, "Core STI"),
    "STI-407": ("Web Back End Development", 3, 4, "Core STI"),
    "STI-501": ("Deep Learning & Neural Networks", 3, 5, "Core STI"),
    "STI-503": ("Data Mining & Visualisasi Data", 3, 5, "Core STI"),
    "STI-504": ("Internet of Things", 3, 5, "Core STI"),
    "STI-505": ("Pemrograman Aplikasi Mobile", 3, 5, "Core STI"),
    "STI-506": ("Manajemen Proyek TI", 3, 5, "Core STI"),
    "STI-601": ("Integrasi Layanan Cerdas AI", 3, 6, "Core STI"),
    "STI-602": ("Smart City & Pemerintahan Digital", 2, 6, "Core STI"),
    "STI-603": ("Keamanan Informasi Lanjut", 3, 6, "Core STI"),
    "STI-604": ("Digital Platform Engineering", 3, 6, "Core STI"),
    "STI-701": ("Pengembangan Startup Digital", 3, 7, "Core STI"),

    # Peminatan 1: Integrated Smart Systems (6 MK / 18 SKS)
    "STA-01": ("Decision Support Systems", 3, 5, "Peminatan 1"),
    "STA-02": ("Metode Komputasi Numerik Terapan", 3, 6, "Peminatan 1"),
    "STA-03": ("Sistem Agen Cerdas & Multi-Agent", 3, 6, "Peminatan 1"),
    "STA-04": ("MLOps & AI Model Deployment", 3, 7, "Peminatan 1"),
    "STA-05": ("Natural Language Processing & LLM", 3, 7, "Peminatan 1"),
    "STA-06": ("Smart Surveillance & Vision Analytics", 3, 7, "Peminatan 1"),

    # Peminatan 2: Cloud Infrastructure & Cybersecurity (6 MK / 18 SKS)
    "STB-01": ("Keamanan Jaringan & Forensik Digital", 3, 5, "Peminatan 2"),
    "STB-02": ("Cloud Architecture & DevOps", 3, 6, "Peminatan 2"),
    "STB-03": ("Penetration Testing & Red Teaming", 3, 6, "Peminatan 2"),
    "STB-04": ("IT Governance & Compliance COBIT 2019", 3, 7, "Peminatan 2"),
    "STB-05": ("Keamanan Cloud & Kriptografi Terapan", 3, 7, "Peminatan 2"),
    "STB-06": ("Rekayasa Ketahanan Sistem & SRE", 3, 7, "Peminatan 2"),

    # Peminatan 3: Digital Platform Engineering (6 MK / 18 SKS)
    "STC-01": ("Interaksi Manusia & Komputer Lanjut", 3, 5, "Peminatan 3"),
    "STC-02": ("Enterprise Architecture Frameworks", 3, 6, "Peminatan 3"),
    "STC-03": ("Pengembangan Aplikasi Cross-Platform", 3, 6, "Peminatan 3"),
    "STC-04": ("Digital Business Ecosystems & Platform Strategy", 3, 7, "Peminatan 3"),
    "STC-05": ("Cloud-Native Application Development", 3, 7, "Peminatan 3"),
    "STC-06": ("Product Management & Growth Hacking", 3, 7, "Peminatan 3"),
}

print(f"Total Canonical Courses: {len(CANONICAL_COURSES)} MK")

# Scan all markdown files
md_files = sorted(glob.glob(os.path.join(workdir, "*.md")))

issues = []

for fpath in md_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        lines = text.splitlines()

    for idx, line in enumerate(lines):
        line_no = idx + 1
        
        # Check for obsolete course codes or patterns
        for old_pattern in ["FST-208", "STI-104", "STI-203", "STI-204", "STI-205", "STI-208"]:
            if re.search(r'\b' + old_pattern + r'\b', line):
                # allow historical mentions only if specified
                if fname not in ["016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md"]:
                    issues.append(f"[{fname}:{line_no}] Obsolete code '{old_pattern}' found: {line.strip()}")

print(f"\nAudit complete. Found {len(issues)} issues.")
for iss in issues:
    safe_iss = iss.encode('ascii', errors='replace').decode('ascii')
    print("  ->", safe_iss)
