"""
=============================================================================
CONVERT ALL ASCII BOX TABLES TO PURE MARKDOWN TABLES
=============================================================================
Script ini mencari blok ASCII box drawing (┌───) di semua file .md dan
mengubahnya menjadi format tabel Markdown standar (| col | col |).
=============================================================================
"""

import os
import glob
import re

DIR = r'd:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI'

def convert_ascii_box_to_md_table(box_text):
    """Mengonversi 1 blok teks ASCII box menjadi tabel Markdown yang valid."""
    lines = box_text.strip().split('\n')
    data_rows = []
    
    for line in lines:
        line_clean = line.strip()
        # Lewati garis pembatas horizontal
        if re.match(r'^[┌├└┼┬┴─│\s─]+$', line_clean) and not any(c.isalnum() for c in line_clean):
            continue
            
        if '│' in line_clean:
            # Ambil cell
            cells = [c.strip() for c in line_clean.strip('│').split('│')]
            if any(cells):
                data_rows.append(cells)
                
    if not data_rows:
        return box_text
        
    # Cek jika ada judul tabel di baris pertama yang hanya 1 cell besar
    header_idx = 0
    if len(data_rows[0]) == 1 and len(data_rows) > 1:
        # Ini adalah title banner
        banner_title = data_rows[0][0]
        header_idx = 1
        if len(data_rows) <= 1:
            return f"**{banner_title}**\n"
    else:
        banner_title = None
        
    if header_idx >= len(data_rows):
        return box_text
        
    headers = data_rows[header_idx]
    col_count = len(headers)
    
    md_lines = []
    if banner_title:
        md_lines.append(f"### {banner_title}\n")
        
    # Header row
    md_lines.append("| " + " | ".join(headers) + " |")
    # Separator
    md_lines.append("| " + " | ".join(["---"] * col_count) + " |")
    
    # Body rows
    for row in data_rows[header_idx + 1:]:
        # Pad row jika kurang kolom
        padded_row = (row + [""] * col_count)[:col_count]
        # Bersihkan format
        clean_row = [c.replace('\n', ' ') for c in padded_row]
        md_lines.append("| " + " | ".join(clean_row) + " |")
        
    return "\n".join(md_lines)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig = content
    
    # Regex untuk mencari blok ``` ... ``` yang memuat karakter box '┌'
    pattern = re.compile(r'```[^\n]*\n([\s\S]*?┌[\s\S]*?└[\s\S]*?)\n```', re.MULTILINE)
    
    def replacer(match):
        box_text = match.group(1)
        return convert_ascii_box_to_md_table(box_text)
        
    new_content = pattern.sub(replacer, content)
    
    if new_content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated (Converted ASCII to MD Table): {os.path.basename(filepath)}")
    else:
        print(f"No ASCII box tables found: {os.path.basename(filepath)}")

def main():
    for f in sorted(glob.glob(os.path.join(DIR, '*.md'))):
        process_file(f)

if __name__ == '__main__':
    main()
