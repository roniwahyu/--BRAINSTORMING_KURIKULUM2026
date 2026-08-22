"""
Script untuk memverifikasi dan memperbarui nama & kode MKU di seluruh file markdown (.md)
"""
import glob
import os
import re

DIR = r'd:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI'

# Pemetaan perbaikan
REPLACEMENTS = [
    # MKU-101
    (r'Pendidikan Agama I(?!\s*II)', 'Agama I'),
    (r'PENDIDIKAN AGAMA I(?!\s*II)', 'AGAMA I'),
    # MKU-102
    (r'Pendidikan Pancasila', 'Pancasila'),
    (r'PENDIDIKAN PANCASILA', 'PANCASILA'),
    # MKU-405
    (r'Pendidikan Kewarganegaraan\s*\(KWN\)', 'Kewarganegaraan'),
    (r'Pendidikan Kewarganegaraan', 'Kewarganegaraan'),
    (r'Pend\.\s*Kewarganegaraan\s*\(KWN\)', 'Kewarganegaraan'),
    (r'PENDIDIKAN KEWARGANEGARAAN\s*\(KWN\)', 'KEWARGANEGARAAN'),
    (r'PENDIDIKAN KEWARGANEGARAAN', 'KEWARGANEGARAAN'),
    # MKU-507
    (r'KPM\s*\(\s*Kuliah Pengabdian Masyarakat\s*\)', 'KPM (Kuliah Pengabdian Kepada Masyarakat)'),
    (r'KPM\s*\(\s*Pengabdian Masy\.\s*\)', 'KPM (Kuliah Pengabdian Kepada Masyarakat)'),
    (r'Kuliah Pengabdian Masyarakat', 'Kuliah Pengabdian Kepada Masyarakat'),
]

def process_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    for pattern, repl in REPLACEMENTS:
        content = re.sub(pattern, repl, content)
        
    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {os.path.basename(fpath)}")
    else:
        print(f"No change needed: {os.path.basename(fpath)}")

for fpath in glob.glob(os.path.join(DIR, '*.md')):
    process_file(fpath)
