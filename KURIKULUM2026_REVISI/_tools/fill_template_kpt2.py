# -*- coding: utf-8 -*-
"""Fill semester structure tables (20-27) + supporting tables in the KPT book."""
import copy
from docx import Document

SRC = "D:/!!MYDOCUMENTS2026/!!!SISTEKIN2026/!!BRAINSTORMING_KURIKULUM2026/KURIKULUM2026_REVISI/BUKU_KPT_SISTEKIN_2026_FINAL.docx"
doc = Document(SRC)

def set_cell(cell, text, bold=False):
    cell.text = ""
    p = cell.paragraphs[0]
    run = p.add_run(text)
    run.bold = bold

def duplicate_row(table, src_idx):
    src = table.rows[src_idx]._tr
    new_tr = copy.deepcopy(src)
    table._tbl.append(new_tr)
    return table.rows[-1]

# Semester structure: each entry (Kode, Nama, SKS, Jenis)
semesters = [
    [ # Sem 1
        ("FST-101","Dasar Teknologi Digital","2","FSTI"),
        ("FST-102","Algoritma dan Pemrograman","3","FSTI"),
        ("STI-101","Pengantar Sistem dan Teknologi Informasi","2","Core STI"),
        ("STI-102","Kalkulus","3","Core STI"),
        ("STI-103","Arsitektur dan Organisasi Sistem TI","3","Core STI"),
        ("MKU-101","Agama I","2","MKWU"),
        ("MKU-102","Pancasila","2","MKWU"),
        ("MKU-103","Bahasa Indonesia","2","MKWU"),
    ],
    [ # Sem 2
        ("STI-204","Matematika Diskrit dan Logika","3","Core STI"),
        ("STI-205","Aljabar Linear dan Matriks","3","Core STI"),
        ("FST-203","Struktur Data dan Algoritma","3","FSTI"),
        ("FST-204","Pengantar Kecerdasan Artifisial & Data","2","FSTI"),
        ("FST-205","Basic English for IT","2","FSTI"),
        ("FST-206","Etika Profesi & Hukum Digital","2","FSTI"),
        ("FST-207","Sistem Basis Data","3","FSTI"),
        ("MKU-204","Kewirausahaan I","2","MKWU"),
    ],
    [ # Sem 3
        ("STI-306","Analisis dan Perancangan Sistem Informasi","3","Core STI"),
        ("STI-307","Sistem Cerdas","2","Core STI"),
        ("STI-308","UI/UX Design & Prototyping","3","Core STI"),
        ("STI-309","Rekayasa Perangkat Lunak","3","Core STI"),
        ("STI-310","Sistem Operasi","3","Core STI"),
        ("STI-311","Web Front End Development","3","Core STI"),
        ("STI-312","Jaringan Komputer","3","Core STI"),
    ],
    [ # Sem 4
        ("STI-413","Machine Learning","3","Core STI"),
        ("STI-414","Pengantar NLP & Information Retrieval","2","Core STI"),
        ("STI-415","Data Warehouse & Business Intelligence","3","Core STI"),
        ("STI-416","Web Back End Development","3","Core STI"),
        ("STI-417","Komputasi Awan (Cloud Computing)","3","Core STI"),
        ("STI-418","Dasar Keamanan Informasi","2","Core STI"),
        ("FST-408","Probabilitas dan Statistika","3","FSTI"),
        ("MKU-405","Kewarganegaraan","2","MKWU"),
    ],
    [ # Sem 5
        ("STI-519","Keamanan Informasi Lanjut","3","Core STI"),
        ("STI-520","Data Mining & Visualisasi Data","3","Core STI"),
        ("STI-521","Internet of Things (IoT)","3","Core STI"),
        ("STI-522","Pemrograman Aplikasi Mobile","3","Core STI"),
        ("STI-523","Manajemen Proyek TI","3","Core STI"),
        ("MKU-507","Kuliah Pengabdian Kepada Masyarakat (KPM)","3","MKWU"),
        ("PEM-1","MK Pilihan Peminatan 1","3","Peminatan"),
    ],
    [ # Sem 6
        ("STI-624","Integrasi Layanan Cerdas Berbasis AI","3","Core STI"),
        ("STI-625","Smart City & Pemerintahan Digital","2","Core STI"),
        ("STI-626","Deep Learning & Neural Networks","3","Core STI"),
        ("STI-627","Digital Platform Engineering","3","Core STI"),
        ("FST-611","Metodologi Penelitian","2","FSTI"),
        ("PEM-2","MK Pilihan Peminatan 2","3","Peminatan"),
        ("PEM-3","MK Pilihan Peminatan 3","3","Peminatan"),
    ],
    [ # Sem 7
        ("STI-728","Inovasi Teknologi dan Startup Digital","3","Core STI"),
        ("FST-610","Capstone Project FSTI","3","FSTI"),
        ("FST-612","Praktik Kerja Lapangan (PKL)","3","FSTI"),
        ("FST-613","Pra-Skripsi / Seminar Proposal","2","FSTI"),
        ("PEM-4","MK Pilihan Peminatan 4","3","Peminatan"),
        ("PEM-5","MK Pilihan Peminatan 5","3","Peminatan"),
        ("PEM-6","MK Pilihan Peminatan 6","3","Peminatan"),
    ],
    [ # Sem 8
        ("FST-714","Skripsi / Tugas Akhir","6","FSTI"),
    ],
]

# Tables 20..27 = semester 1..8 (verified: table 20 = Sem1, ... table 27 = Sem8)
for sem_i in range(8):
    t = doc.tables[20 + sem_i]
    data = semesters[sem_i]
    # header row = 0, data rows from 1
    for i in range(1, len(t.rows)):
        cells = t.rows[i].cells
        if i - 1 < len(data):
            set_cell(cells[0], str(i))
            set_cell(cells[1], data[i-1][0])
            set_cell(cells[2], data[i-1][1])
            set_cell(cells[3], data[i-1][2])
            set_cell(cells[4], data[i-1][3])
        else:
            for c in cells:
                set_cell(c, "")
    # add rows if needed
    for i in range(len(t.rows) - 1, len(data)):
        r = duplicate_row(t, 1)
        cells = r.cells
        set_cell(cells[0], str(i+1))
        set_cell(cells[1], data[i][0])
        set_cell(cells[2], data[i][1])
        set_cell(cells[3], data[i][2])
        set_cell(cells[4], data[i][3])
    # Add a TOTAL row as last row
    total_sks = sum(int(x[2]) for x in data)
    # append total row
    r = duplicate_row(t, 1)
    cells = r.cells
    set_cell(cells[0], "")
    set_cell(cells[1], "")
    set_cell(cells[2], "TOTAL SEMESTER " + str(sem_i+1), True)
    set_cell(cells[3], str(total_sks), True)
    set_cell(cells[4], "")

# ============================================================
# Table 7: Tujuan Program Studi + Strategi (header + 5 rows)
# Columns: Tujuan | Strategi Pencapaian | Indikator Keberhasilan
# ============================================================
t = doc.tables[7]
tujuan = [
    ("Menghasilkan lulusan yang menguasai kompetensi terintegrasi sistem informasi, infrastruktur TI, dan rekayasa AI aplikatif berdaya saing global.",
     "Kurikulum OBE dengan 14 CPL, jalur peminatan, dan Case Method/PjBL.",
     "IPK lulusan; capaian CPL ≥ target; masa tunggu kerja < 6 bulan."),
    ("Menghasilkan produk riset terapan dan publikasi ilmiah bereputasi.",
     "Roadmap penelitian prodi, kolaborasi riset dosen-mahasiswa.",
     "Jumlah publikasi & produk riset per tahun."),
    ("Melahirkan inovator dan wirausahawan digital (tech founders).",
     "Kewirausahaan I–II, Startup Digital, Capstone, inkubasi.",
     "Jumlah startup/produk yang dihasilkan mahasiswa."),
    ("Membangun jejaring kolaborasi tri-dharma dengan industri dan asosiasi profesi.",
     "MoU industri, MBKM, kuliah praktisi, sertifikasi (APTIKOM/IEEE/ACM).",
     "Jumlah MoU aktif dan kegiatan kolaboratif per tahun."),
    ("Menghasilkan lulusan beretika, adaptif, dan berkarakter profesional.",
     "MKWU, Etika Profesi, integritas akademik, lifelong learning.",
     "Skor integritas & kepuasan pengguna lulusan."),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(tujuan):
        set_cell(cells[0], tujuan[i-1][0])
        set_cell(cells[1], tujuan[i-1][1])
        set_cell(cells[2], tujuan[i-1][2])
    else:
        for c in cells:
            set_cell(c, "")

# ============================================================
# Table 12: Matriks CPL dengan KKNI/SN-Dikti (header + 9 rows)
# Columns: Kode CPL | Unsur KKNI/SN-Dikti | Keterangan Kesesuaian
# ============================================================
t = doc.tables[12]
cpl_kkni = [
    ("S1","Sikap & Tata Nilai","SN-Dikti Sikap Butir 1–10; dilebur 1 rumusan terukur"),
    ("KU1","Keterampilan Umum","SN-Dikti KU Butir 1 & 3 (pemikiran logis-kritis)"),
    ("KU2","Keterampilan Umum","SN-Dikti KU Butir 4 & 6 (komunikasi & jejaring)"),
    ("KU3","Keterampilan Umum","SN-Dikti KU Butir 2,5,7,8,9 (keputusan & lifelong)"),
    ("P1","Penguasaan Pengetahuan","IS2020 P05 + IT2017 P1 (matematika & sains komputasi)"),
    ("P2","Penguasaan Pengetahuan","IS2020 P01/P04/P09/P16 (SI & proses bisnis)"),
    ("P3","Penguasaan Pengetahuan","IS2020 P03/P06/P07/P08 (infrastruktur, cloud, governance)"),
    ("P4","Penguasaan Pengetahuan","IS2020 P02/P10-P14 (software, data, UI/UX)"),
    ("KK1","Keterampilan Khusus","IS2020 K01/K09/K13/K16 + IT2017 KK1"),
    ("KK2","Keterampilan Khusus","IS2020 K01/K13/K16 + IT2017 KK1"),
    ("KK3","Keterampilan Khusus","IS2020 K02/K05/K06/K17 + IT2017 KK2/KK3"),
    ("KK4","Keterampilan Khusus","IS2020 K05/K06/K07/K14 + IT2017 KK3"),
    ("KK5","Keterampilan Khusus","IS2020 K03/K04/K08/K10/K11/K12 + IT2017 KK1"),
    ("KK6","Keterampilan Khusus","IS2020 K08/K15 + IT2017 KK1"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(cpl_kkni):
        set_cell(cells[0], cpl_kkni[i-1][0], bold=True)
        set_cell(cells[1], cpl_kkni[i-1][1])
        set_cell(cells[2], cpl_kkni[i-1][2])
for i in range(len(t.rows) - 1, len(cpl_kkni)):
    r = duplicate_row(t, 1)
    cells = r.cells
    set_cell(cells[0], cpl_kkni[i][0], bold=True)
    set_cell(cells[1], cpl_kkni[i][1])
    set_cell(cells[2], cpl_kkni[i][2])

# ============================================================
# Table 32: MBKM semester (header + 3 rows)
# ============================================================
t = doc.tables[32]
mbkm = [
    ("Semester 6","Magang Bersertifikat (MSIB) / Pertukaran","20","Konversi ke peminatan MK-2/3 + STI-624/625/626/627 + FST-611"),
    ("Semester 7","Magang / Studi Independen / Wirausaha","20","Konversi ke peminatan MK-4/5/6 + STI-728 + FST-610/612/613"),
    ("Semester 6–7","KKNT, Asistensi Mengajar, Riset, Kemanusiaan, Bela Negara","20","Terstruktur/bebas/hibrida (lihat Bab X)"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(mbkm):
        set_cell(cells[0], mbkm[i-1][0])
        set_cell(cells[1], mbkm[i-1][1])
        set_cell(cells[2], mbkm[i-1][2])
        set_cell(cells[3], mbkm[i-1][3])

# ============================================================
# Table 33: Rekognisi BKP (header + 3 rows)
# ============================================================
t = doc.tables[33]
bkp = [
    ("Magang/Praktik Kerja","Terstruktur + Hibrida","Peminatan + STI-624/627 + FST-612","20","Logbook, laporan, nilai mitra"),
    ("Studi/Proyek Independen","Terstruktur + Hibrida","Peminatan + FST-610 + STI-728","20","Produk/prototipe, laporan"),
    ("Wirausaha","Terstruktur + Hibrida","STI-728 Startup + peminatan","20","Proposal, laporan, produk/startup"),
    ("Pertukaran Mahasiswa","Terstruktur","Transfer kredit MK setara CPL","20","Transkrip PT mitra"),
    ("KKNT/Asistensi/Riset/Kemanusiaan/Bela Negara","Terstruktur + Bebas","MKWU + soft skills + MK pengabdian","20","Logbook, laporan, nilai mitra"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(bkp):
        set_cell(cells[0], bkp[i-1][0])
        set_cell(cells[1], bkp[i-1][1])
        set_cell(cells[2], bkp[i-1][2])
        set_cell(cells[3], bkp[i-1][3])
        set_cell(cells[4], bkp[i-1][4])
for i in range(len(t.rows) - 1, len(bkp)):
    r = duplicate_row(t, 1)
    cells = r.cells
    set_cell(cells[0], bkp[i][0])
    set_cell(cells[1], bkp[i][1])
    set_cell(cells[2], bkp[i][2])
    set_cell(cells[3], bkp[i][3])
    set_cell(cells[4], bkp[i][4])

doc.save(SRC)
print("SAVED. Tables:", len(doc.tables))
