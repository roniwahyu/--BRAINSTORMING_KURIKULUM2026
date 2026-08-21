"""
=============================================================================
LIVE WATCHER: AUTO EXPORT 011 MARKDOWN TO EXCEL
=============================================================================
Script ini memantau perubahan pada file:
  011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md
Setiap kali file disimpan (Ctrl+S / Modifikasi), script akan otomatis
memanggil generator untuk mengupdate file Excel:
  011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.xlsx
=============================================================================
"""

import os
import sys
import time
import io
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
SRC_MD = os.path.join(PARENT_DIR, "011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md")

# Import modul konversi
sys.path.insert(0, SCRIPT_DIR)
import export_011_tables_to_excel

def get_mtime(path):
    try:
        return os.path.getmtime(path)
    except OSError:
        return None

def main():
    print("=====================================================================")
    print("  LIVE AUTO-WATCHER: 011 TABLES -> EXCEL (SISTEKIN 2026)")
    print("=====================================================================")
    print(f"Memantau: {SRC_MD}")
    print("Tekan Ctrl+C di terminal ini untuk berhenti.\n")

    if not os.path.exists(SRC_MD):
        print(f"[ERROR] File target tidak ditemukan: {SRC_MD}")
        return

    last_mtime = get_mtime(SRC_MD)
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Watcher aktif. Menunggu perubahan file markdown...")

    while True:
        try:
            time.sleep(1.5)
            current_mtime = get_mtime(SRC_MD)

            if current_mtime and current_mtime != last_mtime:
                last_mtime = current_mtime
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n[{timestamp}] Perubahan terdeteksi pada file markdown! Mengupdate Excel...")
                try:
                    export_011_tables_to_excel.convert()
                    print(f"[{timestamp}] Update Excel selesai secara otomatis!")
                except Exception as err:
                    print(f"[ERROR] Gagal generate Excel: {err}")
        except KeyboardInterrupt:
            print("\nWatcher dihentikan oleh pengguna.")
            break

if __name__ == '__main__':
    main()
