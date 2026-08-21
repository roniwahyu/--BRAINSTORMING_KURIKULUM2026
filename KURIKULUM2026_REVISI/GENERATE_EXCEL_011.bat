@echo off
chcp 65001 > nul
echo ======================================================================
echo    TRIGGER GENERATE ULANG EXCEL 011 (SISTEKIN UWG 2026)
echo ======================================================================
echo Sumber : 011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md
echo Target : 011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.xlsx
echo.

python "%~dp0_tools\export_011_tables_to_excel.py"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SELESAI] File Excel berhasil diperbarui!
) else (
    echo.
    echo [GAGAL] Terjadi kesalahan saat memproses file.
)

echo.
pause
