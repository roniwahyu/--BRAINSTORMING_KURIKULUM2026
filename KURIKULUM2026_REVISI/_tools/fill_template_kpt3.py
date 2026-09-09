# -*- coding: utf-8 -*-
"""Fill remaining KPT tables: kedalaman BK (15), eval MK lama (16), MK baru (17),
RPS komponen (31), matriks penilaian CPL (34), evaluasi aspek (4), stakeholder (5)."""
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

def clear_row(table, idx):
    for c in table.rows[idx].cells:
        set_cell(c, "")

# ============================================================
# Table 4: Evaluasi Aspek Kurikulum (header + 10 data rows)
# Columns: Aspek | Kondisi Saat Ini | Permasalahan | Rekomendasi
# ============================================================
t = doc.tables[4]
eval_aspek = [
    ("Profil Lulusan","K2025 belum menetapkan profil lulusan berbasis peran yang eksplisit","Kurikulum 2025 belum berorientasi penuh pada OBE","Ditetapkan 4 PL berbasis peran + 3 PEO (Dok 002)"),
    ("CPL","CPL K2025 belum terstruktur 4 ranah SN-Dikti","Belum ada genealogi sumber & indikator kinerja","Ditetapkan 14 CPL terstandar + genealogi (Dok 003, 009)"),
    ("Struktur Mata Kuliah","56 MK / 146 SKS, seluruhnya wajib, tanpa peminatan","Tidak ada jalur spesialisasi & fleksibilitas MBKM","55 MK / 146 SKS + 3 peminatan @18 SKS (Dok 005)"),
    ("Bahan Kajian","BoK belum dipetakan eksplisit ke CPL","Kurang audit redundansi/gap","36 BK (21 IS2020 + 15 IT2017) + audit zero redundancy (Dok 016, 017)"),
    ("RPS","Format RPS belum memuat kolom Indikator & Kriteria","Keselarasan konstruktif belum lengkap","RPS 67 MK + kolom Indikator/Kriteria (Dok 007, 037)"),
    ("Asesmen","Belum ada formula ketercapaian CPL","IKU 7 belum terukur","Skema 4 titik asesmen + formula CPL (Dok 008)"),
    ("MBKM","Belum ada skema konversi MBKM","Fleksibilitas 3 semester belum diakomodasi","9 BKP + rekognisi transkrip/SKPI (Dok 006, 034)"),
    ("Sumber Daya","Kualifikasi dosen & lab perlu penguatan","Rasio dosen & sarana lab","[PERLU DATA UPPS] rencana penguatan SDM & lab"),
    ("Manajemen","SPMI kurikulum belum terdokumentasi utuh","Bukti fisik SPMI belum lengkap","Tabel N + bukti fisik PPEPP (Dok 023 Bab XI)"),
    ("Pembiayaan","Anggaran pengembangan kurikulum","Kecukupan pendanaan","[PERLU DATA UPPS]"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(eval_aspek):
        set_cell(cells[0], eval_aspek[i-1][0])
        set_cell(cells[1], eval_aspek[i-1][1])
        set_cell(cells[2], eval_aspek[i-1][2])
        set_cell(cells[3], eval_aspek[i-1][3])
    else:
        for c in cells: set_cell(c, "")

# ============================================================
# Table 5: Hasil Masukan Stakeholder (header + 6 data rows)
# ============================================================
t = doc.tables[5]
stake = [
    ("Dosen","Perlu penegasan peminatan & penguatan AI","Struktur 3 peminatan & pipeline AI 5 tahap"),
    ("Mahasiswa","Perlu fleksibilitas TA non-skripsi & MBKM","4 opsi TA non-skripsi + 9 BKP MBKM"),
    ("Alumni","[PERLU DATA UPPS — prodi belum berkohor lulusan]","Tracer study disiapkan (Dok 010)"),
    ("Pengguna Lulusan","Kebutuhan AI, cloud, cybersecurity, UI/UX","14 CPL + 3 peminatan selaras kebutuhan industri"),
    ("Mitra Industri","Kolaborasi magang & sertifikasi kompetensi","MBKM 20 SKS + capstone bersama industri"),
    ("Asosiasi Profesi","Kesesuaian BoK APTIKOM IS2020/IT2017","36 BK diadopsi dari IS2020 & IT2017"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(stake):
        set_cell(cells[0], stake[i-1][0])
        set_cell(cells[1], stake[i-1][1])
        set_cell(cells[2], stake[i-1][2])
    else:
        for c in cells: set_cell(c, "")

# ============================================================
# Table 6: Benchmarking (header + 2 data rows)
# ============================================================
t = doc.tables[6]
bench = [
    ("Prodi S1 Sistem Informasi (APTIKOM IS2020)","Profil lulusan, CPL, BoK","Adopsi 21 BK IS2020 & struktur OBE","14 CPL + 21 BK IS2020 terpetakan"),
    ("Prodi S1 Teknologi Informasi (APTIKOM IT2017)","CPL, BoK, praktik profesional","Adopsi 15 BK IT2017 & global practice","15 BK IT2017 + BK-IT15 global practice"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(bench):
        set_cell(cells[0], bench[i-1][0])
        set_cell(cells[1], bench[i-1][1])
        set_cell(cells[2], bench[i-1][2])
        set_cell(cells[3], bench[i-1][3])
    else:
        for c in cells: set_cell(c, "")

# ============================================================
# Table 15: Kedalaman & Keluasan BK (header + 5 data rows)
# ============================================================
t = doc.tables[15]
bk_depth = [
    ("BK-IS01..IS21 (Sistem Informasi)","Dasar s.d. Lanjut","Sedang s.d. Luas","Diturunkan menjadi 28 MK Core STI + 13 MK FSTI"),
    ("BK-IT01..IT15 (Teknologi Informasi)","Dasar s.d. Lanjut","Sedang s.d. Luas","Diturunkan menjadi MK Core STI + 18 MK peminatan"),
    ("AI/ML/Data (IS16, IS18, IT02)","Lanjut (C5–C6)","Luas","Pipeline AI 5 tahap: STI-307→STI-413→STI-626→STI-624"),
    ("Cloud/Cyber (IS19, IT05, IT06)","Menengah s.d. Lanjut","Sedang","STI-417 Cloud → STI-418/519 Security → peminatan P2"),
    ("Platform/UI-UX (IS17, IT04, IT10)","Menengah s.d. Lanjut","Sedang","STI-308 UI/UX → STI-311/416 Web → peminatan P3"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(bk_depth):
        set_cell(cells[0], bk_depth[i-1][0])
        set_cell(cells[1], bk_depth[i-1][1])
        set_cell(cells[2], bk_depth[i-1][2])
        set_cell(cells[3], bk_depth[i-1][3])
    else:
        for c in cells: set_cell(c, "")

# ============================================================
# Table 16: Evaluasi MK Kurikulum Berjalan (header + 5 rows)
# Columns: No | MK Lama | SKS | CPL | Status | Tindak Lanjut
# ============================================================
t = doc.tables[16]
mk_lama = [
    ("1","56 MK Kurikulum 2025","146","CPL K2025","Dievaluasi terhadap 14 CPL K2026","Ekivalensi 5 kategori (Dok 024)"),
    ("2","34 MK (E1 - Penuh)","—","Selaras penuh","Dipertahankan","Alih nilai langsung"),
    ("3","11 MK (E2 - Bersyarat)","—","Selaras bersyarat","Direvisi","Uji penyetaraan"),
    ("4","8 MK (E3 - Gabungan)","—","Digabung","Digabung","Klaster peleburan G1-G4"),
    ("5","1 MK (E4 - Pecah) + 2 MK (E5 - Tanpa Padanan)","—","Pecah/Hapus","Direkonstruksi/Dihapus","MK pengganti dirumuskan (Dok 026)"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(mk_lama):
        for j in range(min(6, len(cells))):
            set_cell(cells[j], mk_lama[i-1][j])
    else:
        for c in cells: set_cell(c, "")

# ============================================================
# Table 17: Pembentukan MK Baru (header + 5 rows)
# Columns: No | CPL | BK | MK | SKS | Alasan
# ============================================================
t = doc.tables[17]
mk_baru = [
    ("1","KK1, KK2","BK-IS16/18","STI-624 Integrasi Layanan Cerdas Berbasis AI","3","Penciri AI & smart systems"),
    ("2","KK3","BK-IS19/IT05","STI-417 Komputasi Awan","3","Fondasi cloud"),
    ("3","KK5","BK-IS17/IT10","STI-308 UI/UX Design & Prototyping","3","Penciri platform"),
    ("4","KK6","BK-IS15/IT13","STI-728 Inovasi Teknologi & Startup Digital","3","Penciri technopreneurship"),
    ("5","KK1-KK6","BK peminatan","18 MK Pilihan Peminatan (STA/STB/STC)","54","3 jalur spesialisasi @18 SKS"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(mk_baru):
        for j in range(min(6, len(cells))):
            set_cell(cells[j], mk_baru[i-1][j])
    else:
        for c in cells: set_cell(c, "")

# ============================================================
# Table 31: Komponen RPS (header + 18 rows) -> contoh STI-103
# ============================================================
t = doc.tables[31]
rps = [
    ("Nama Program Studi","Sistem dan Teknologi Informasi (SISTEKIN)"),
    ("Nama Mata Kuliah","Arsitektur dan Organisasi Sistem Teknologi Informasi"),
    ("Kode Mata Kuliah","STI-103"),
    ("Semester","1 (Ganjil)"),
    ("Bobot SKS","3 SKS (2 Teori + 1 Praktik)"),
    ("Dosen Pengampu","[PERLU DATA UPPS]"),
    ("CPL yang Dibebankan","P1 (Fondasi Matematika & Sains Komputasi), P3 (Infrastruktur TI)"),
    ("CPMK","Mahasiswa mampu menjelaskan arsitektur dan organisasi sistem komputer/TI (C2), menganalisis komponen sistem (C4), serta merancang arsitektur sistem sederhana (C6)"),
    ("Sub-CPMK","16 tahapan belajar mingguan (lihat RPS lengkap Dok 007 & 037)"),
    ("Deskripsi Singkat MK","Mata kuliah ini membekali pemahaman arsitektur dan organisasi sistem TI — pengganti Logika Informatika — sebagai fondasi Sistem Operasi, Jaringan Komputer, dan Cloud"),
    ("Bahan Kajian","BK-IS03 (IT Infrastructure), BK-IT01 (IT Fundamentals)"),
    ("Pustaka Utama","Stallings, Computer Organization and Architecture; Tanenbaum, Structured Computer Organization"),
    ("Pustaka Pendukung","Materi CC2020 & IT2017 terkait arsitektur sistem"),
    ("Media Pembelajaran","Slide, LMS, simulator arsitektur, papan tulis virtual"),
    ("Metode Pembelajaran","Ceramah interaktif, diskusi kelompok, studi kasus, praktikum"),
    ("Metode Asesmen","Tugas 1 (20%), UTS (30%), Tugas 2 (20%), UAS (30%)"),
    ("Mata Kuliah Prasyarat","— (Tidak ada)"),
    ("Tanggal Penyusunan","September 2026"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(rps):
        set_cell(cells[0], rps[i-1][0], bold=True)
        set_cell(cells[1], rps[i-1][1])
    else:
        for c in cells: set_cell(c, "")

# ============================================================
# Table 34: Matriks Penilaian CPL (header + 5 rows)
# Columns: CPL | MK Pendukung | Instrumen | Target | Waktu
# ============================================================
t = doc.tables[34]
cpl_pen = [
    ("S1","MKWU + FST-206 Etika","Rubrik sikap, observasi","100% lulus","Setiap semester"),
    ("P1-P4","28 MK Core STI + 13 MK FSTI","Tes, proyek, praktikum","Capaian CPL ≥ 70%","Setiap semester"),
    ("KK1-KK6","MK peminatan + Capstone","Rubrik analitik + holistik","Capaian CPL ≥ 70%","Sem 5-8"),
    ("KU1-KU3","Seluruh MK + PKL","Presentasi, laporan, portofolio","Capaian CPL ≥ 70%","Setiap semester"),
    ("14 CPL (Kohor)","Seluruh MK pembina","Formula ketercapaian CPL","≥ 50% mahasiswa lulus CPL","Tiap semester (LAM K9)"),
]
for i in range(1, len(t.rows)):
    cells = t.rows[i].cells
    if i - 1 < len(cpl_pen):
        set_cell(cells[0], cpl_pen[i-1][0])
        set_cell(cells[1], cpl_pen[i-1][1])
        set_cell(cells[2], cpl_pen[i-1][2])
        set_cell(cells[3], cpl_pen[i-1][3])
        set_cell(cells[4], cpl_pen[i-1][4])
    else:
        for c in cells: set_cell(c, "")

doc.save(SRC)
print("SAVED. Tables:", len(doc.tables))
