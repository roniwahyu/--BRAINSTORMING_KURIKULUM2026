@echo off
chcp 65001 > nul
echo ======================================================================
echo    STARTING LIVE WATCHER FOR 011 TABLES (SISTEKIN UWG 2026)
echo ======================================================================
echo.
python "%~dp0_tools\watch_and_auto_export.py"
pause
