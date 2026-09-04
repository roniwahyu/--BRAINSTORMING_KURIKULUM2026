# -*- coding: utf-8 -*-
"""
Skrip Eksekusi Restrukturisasi Kode MK Core STI Kontinu (STI-101 s.d. STI-728).
Memperbarui seluruh file markdown dan python script di KURIKULUM2026_REVISI serta root AGENTS.md.
"""
import os
import re
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

MAP_CORE_STI = {
    # Sem 2
    "STI-201": "STI-204",  # Matematika Diskrit dan Logika
    "STI-202": "STI-205",  # Aljabar Linear dan Matriks
    # Sem 3
    "STI-301": "STI-306",  # Analisis dan Perancangan Sistem Informasi
    "STI-302": "STI-307",  # Sistem Cerdas
    "STI-303": "STI-308",  # UI/UX Design & Prototyping
    "STI-304": "STI-309",  # Rekayasa Perangkat Lunak
    "STI-305": "STI-310",  # Sistem Operasi
    "STI-306": "STI-311",  # Web Front End Development
    "STI-307": "STI-312",  # Jaringan Komputer
    # Sem 4
    "STI-401": "STI-413",  # Machine Learning
    "STI-403": "STI-414",  # Pengantar NLP & Information Retrieval
    "STI-402": "STI-415",  # Data Warehouse & Business Intelligence
    "STI-407": "STI-416",  # Web Back End Development
    "STI-404": "STI-417",  # Komputasi Awan (Cloud Computing)
    "STI-405": "STI-418",  # Dasar Keamanan Informasi
    # Sem 5
    "STI-501": "STI-519",  # Deep Learning & Neural Networks
    "STI-503": "STI-520",  # Data Mining & Visualisasi Data
    "STI-504": "STI-521",  # Internet of Things (IoT)
    "STI-505": "STI-522",  # Pemrograman Aplikasi Mobile
    "STI-506": "STI-523",  # Manajemen Proyek TI
    # Sem 6
    "STI-601": "STI-624",  # Integrasi Layanan Cerdas Berbasis AI
    "STI-602": "STI-625",  # Smart City & Pemerintahan Digital
    "STI-603": "STI-626",  # Keamanan Informasi Lanjut
    "STI-604": "STI-627",  # Digital Platform Engineering
    # Sem 7
    "STI-701": "STI-728",  # Inovasi Teknologi dan Startup Digital
}

# Regex single-pass dengan word boundary
PATTERN = re.compile(r'\b(' + '|'.join(re.escape(k) for k in sorted(MAP_CORE_STI.keys(), key=lambda x: -len(x))) + r')\b')

def replace_content(content):
    return PATTERN.sub(lambda m: MAP_CORE_STI[m.group(1)], content)

def main():
    print("=" * 78)
    print("EKSEKUSI RESTRUKTURISASI KODE MK CORE STI KONTINU (STI-101 s.d. STI-728)")
    print("=" * 78)

    # 1. Kumpulkan seluruh file markdown (kecuali Dokumen 027 yang mencatat tabel rencana asal->tujuan)
    md_files = glob.glob(os.path.join(BASE_DIR, "*.md"))
    agents_md = os.path.join(ROOT_DIR, "AGENTS.md")
    if os.path.exists(agents_md):
        md_files.append(agents_md)

    modified_md = 0
    total_replacements = 0

    for fpath in sorted(md_files):
        fname = os.path.basename(fpath)
        if fname == "027_RENCANA_RESTRUKTURISASI_KODE_MK_CORE_STI_KONTINU.md":
            # Jangan timpa dokumen rencana agar riwayat mapping 'Kode Lama -> Kode Baru' tetap utuh
            continue

        with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
            orig = fp.read()

        new_text = replace_content(orig)
        count = len(PATTERN.findall(orig))

        if count > 0:
            with open(fpath, "w", encoding="utf-8") as fp:
                fp.write(new_text)
            print(f"  [MD] {fname:60} : {count:4} pergantian selesai")
            modified_md += 1
            total_replacements += count

    print(f"\nTotal Markdown Diperbarui: {modified_md} file ({total_replacements} pergantian)")

    # 2. Perbarui skrip pendukung di _tools/
    tools_dir = os.path.join(BASE_DIR, "_tools")
    
    # export_024_awam.py
    awam_py = os.path.join(tools_dir, "export_024_awam.py")
    if os.path.exists(awam_py):
        with open(awam_py, "r", encoding="utf-8") as fp:
            txt = fp.read()
        txt = txt.replace('"STI-403": "STI-528"', '"STI-414": "STI-528"')
        txt = txt.replace('"STI-701": "STI-742"', '"STI-728": "STI-742"')
        txt = txt.replace("STI-307) menjadi prasyarat", "STI-312) menjadi prasyarat")
        txt = txt.replace("STI-307 Jaringan Komputer", "STI-312 Jaringan Komputer")
        with open(awam_py, "w", encoding="utf-8") as fp:
            fp.write(txt)
        print("  [PY] export_024_awam.py diperbarui")

    # verify_zero_discrepancy.py
    vzd_py = os.path.join(tools_dir, "verify_zero_discrepancy.py")
    if os.path.exists(vzd_py):
        with open(vzd_py, "r", encoding="utf-8") as fp:
            txt = fp.read()
        txt = txt.replace('"STI-201"', '"STI-204"')
        txt = txt.replace('STI-201', 'STI-204')
        with open(vzd_py, "w", encoding="utf-8") as fp:
            fp.write(txt)
        print("  [PY] verify_zero_discrepancy.py diperbarui")

    # deep_cross_audit.py
    dca_py = os.path.join(tools_dir, "deep_cross_audit.py")
    if os.path.exists(dca_py):
        with open(dca_py, "r", encoding="utf-8") as fp:
            txt = fp.read()
        txt = replace_content(txt)
        with open(dca_py, "w", encoding="utf-8") as fp:
            fp.write(txt)
        print("  [PY] deep_cross_audit.py diperbarui")

    # fix_012.py
    fix12_py = os.path.join(tools_dir, "fix_012.py")
    if os.path.exists(fix12_py):
        with open(fix12_py, "r", encoding="utf-8") as fp:
            txt = fp.read()
        txt = replace_content(txt)
        with open(fix12_py, "w", encoding="utf-8") as fp:
            fp.write(txt)
        print("  [PY] fix_012.py diperbarui")

    print("\n" + "=" * 78)
    print("MIGRASI KODE MK CORE STI KONTINU SELESAI DENGAN SUKSES!")
    print("=" * 78)

if __name__ == "__main__":
    main()
