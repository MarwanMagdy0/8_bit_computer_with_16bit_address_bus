@echo OFF
set /p fname=Enter file name: 
python ../main.py "examples/%fname%"
pause