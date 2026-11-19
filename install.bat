@echo off
REM One-command setup for the AI lab programs (Windows CMD).
REM Usage: open CMD in this folder and run:  install.bat

where python >nul 2>nul
if errorlevel 1 (
    echo Python was not found. Install it from https://www.python.org/downloads/
    echo and tick "Add python.exe to PATH" during setup, then run install.bat again.
    pause
    exit /b 1
)

echo Installing packages from requirements.txt ...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo pip install failed - see the error above.
    pause
    exit /b 1
)

echo Checking that every module used by the programs can be imported ...
python -c "import random, itertools, math, collections, heapq; print('All modules OK - run any program with: python 1.py')"
if errorlevel 1 (
    echo A module failed to import - see the error above.
    pause
    exit /b 1
)

pause
