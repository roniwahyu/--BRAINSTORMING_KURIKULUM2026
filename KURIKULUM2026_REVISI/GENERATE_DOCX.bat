@echo off
chcp 65001 > nul
echo =====================================================================
echo   GENERATE DOCX — KURIKULUM OBE SISTEKIN 2026
echo =====================================================================
echo.
echo Menjalankan konversi seluruh dokumen Markdown (.md) ke Microsoft Word (.docx)...
python _tools/convert_md_to_docx.py
echo.
echo [SELESAI] Seluruh dokumen DOCX berhasil digenerate!
pause
