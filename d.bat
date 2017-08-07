@echo off
cd /d %~dp0
dir /b /d |find "%1">%temp%\tmp.tmp
set /p a=<%temp%\tmp.tmp
python %a% %2 %3 %4 %5 %6 %7 %8 %9 