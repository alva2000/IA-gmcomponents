@echo off
cd /d %~dp0

echo ==========================
echo   INICIANDO IA SERVER
echo ==========================

start cmd /k python server.py



echo ==========================
echo   ABRIENDO FRONTEND
echo ==========================
timeout /t 30 > nul

start "" "frontend\index.html"