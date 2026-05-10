@echo off
REM Sales & Revenue Dashboard - Quick Setup Script
REM This script sets up and runs the dashboard

echo.
echo ========================================
echo  Sales & Revenue Dashboard Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo Step 1: Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat

echo Step 3: Installing dependencies...
pip install -q streamlit pandas numpy plotly
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    echo Please try running this again, or run manually:
    echo   venv\Scripts\pip install streamlit pandas numpy plotly
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Installation Complete!
echo ========================================
echo.
echo Launching dashboard...
echo Opening browser to http://localhost:8501
echo.
echo Press Ctrl+C in the terminal to stop the dashboard
echo.

streamlit run dashboard.py

pause
