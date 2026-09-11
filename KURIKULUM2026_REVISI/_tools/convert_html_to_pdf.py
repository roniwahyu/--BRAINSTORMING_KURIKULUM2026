# -*- coding: utf-8 -*-
"""
HTML to PDF Converter Engine
Program Studi Sistem dan Teknologi Informasi (SISTEKIN) FSTI UWG
Mengonversi dokumen HTML kurikulum menjadi dokumen PDF berkualitas tinggi
menggunakan Chromium/Edge Headless Engine dengan rendering Math & Diagram.
"""

import os
import sys
import glob
import subprocess
import time

WORKDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def find_browser():
    """Mencari executable browser Chrome atau Edge."""
    candidates = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
        r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
        os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe'),
        os.path.expandvars(r'%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe'),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def convert_html_to_pdf(browser_exe, html_path, pdf_path):
    """Mengonversi satu file HTML ke PDF menggunakan Chromium headless."""
    html_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    cmd = [
        browser_exe,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--run-all-compositor-stages-before-draw',
        '--virtual-time-budget=2000',
        f'--print-to-pdf={os.path.abspath(pdf_path)}',
        html_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if res.returncode == 0 and os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
        return True, os.path.getsize(pdf_path)
    else:
        return False, res.stderr

def convert_all(files=None):
    browser_exe = find_browser()
    if not browser_exe:
        print("[ERROR] Tidak ditemukan browser Chrome atau Edge pada sistem!")
        sys.exit(1)
        
    print(f"[INFO] Menggunakan Browser Engine: {browser_exe}")
    
    if files:
        html_files = [os.path.join(WORKDIR, f) if not os.path.isabs(f) else f for f in files]
    else:
        # Default: ambil semua HTML dokumen kurikulum kecuali template/sementara
        html_files = sorted(glob.glob(os.path.join(WORKDIR, "*.html")))
        
    print(f"[INFO] Ditemukan {len(html_files)} file HTML untuk dikonversi ke PDF.\n")
    
    success_count = 0
    start_total = time.time()
    
    for idx, html_path in enumerate(html_files, 1):
        base_name = os.path.splitext(os.path.basename(html_path))[0]
        pdf_name = f"{base_name}.pdf"
        pdf_path = os.path.join(WORKDIR, pdf_name)
        
        print(f"[{idx}/{len(html_files)}] Mengonversi {os.path.basename(html_path)} ...", end="", flush=True)
        start_t = time.time()
        try:
            ok, result = convert_html_to_pdf(browser_exe, html_path, pdf_path)
            elapsed = time.time() - start_t
            if ok:
                success_count += 1
                print(f" -> [SUKSES] ({result:,} bytes, {elapsed:.1f}s)")
            else:
                print(f" -> [GAGAL] Error: {result}")
        except Exception as e:
            print(f" -> [ERROR]: {e}")
            
    total_elapsed = time.time() - start_total
    print(f"\n=====================================================================")
    print(f"[SELESAI] {success_count}/{len(html_files)} file PDF berhasil dibuat ({total_elapsed:.1f}s)")
    print(f"=====================================================================")

if __name__ == '__main__':
    # Jika ada argumen baris perintah, konversi file tersebut saja
    if len(sys.argv) > 1:
        target_args = sys.argv[1:]
        convert_all(target_args)
    else:
        convert_all()
