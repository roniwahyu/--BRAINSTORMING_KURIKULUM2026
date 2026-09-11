@echo off
chcp 65001 > nul
echo =====================================================================
echo   GENERATE PDF — KURIKULUM OBE SISTEKIN 2026
echo =====================================================================
echo.
echo Menjalankan konversi dokumen HTML ke PDF berkualitas tinggi via Headless Chromium...
python _tools/convert_html_to_pdf.py
echo.
echo [SELESAI] Seluruh dokumen PDF berhasil digenerate!
pause
