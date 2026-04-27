@echo off
echo ===============================
echo   EJECUTANDO IA GMCOMPONENTS
echo ===============================

cd /d %~dp0

echo.
echo Activando entorno (si existe)...

REM 👉 Si usas entorno virtual, descomenta esta línea:
REM call venv\Scripts\activate

echo.
echo Ejecutando test_ia.py...
python test_ia.py

echo.
echo ===============================
echo   PROCESO FINALIZADO
echo ===============================

pause