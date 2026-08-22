@echo off
chcp 65001 > nul
echo ======================================================================
echo    TRIGGER GENERATE ULANG SEMUA DOKUMEN HTML (SISTEKIN UWG 2026)
echo ======================================================================
echo.

python "%~dp0_tools\convert_md_to_html.py"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SELESAI] Seluruh file HTML dan Portal index.html berhasil diperbarui!
) else (
    echo.
    echo [GAGAL] Terjadi kesalahan saat memproses file HTML.
)

echo.
pause
