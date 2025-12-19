@echo off
REM SHINIGAMI-EYE Installation Script for Windows
REM 神死眼 - The All-Seeing Eye

echo ============================================
echo     SHINIGAMI-EYE (神死眼) Installer
echo     All-Seeing Cybersecurity Framework
echo ============================================
echo.

REM Check Python
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)
echo ✓ Python found
echo.

REM Check pip
echo [2/5] Checking pip...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo Installing pip...
    python -m ensurepip --upgrade
)
echo ✓ pip is ready
echo.

REM Create virtual environment
echo [3/5] Setting up virtual environment (optional)...
set /p VENV="Create virtual environment? (recommended) [y/N]: "
if /i "%VENV%"=="y" (
    python -m venv venv
    call venv\Scripts\activate.bat
    echo ✓ Virtual environment created and activated
)
echo.

REM Install dependencies
echo [4/5] Installing dependencies...
python -m pip install -r requirements.txt
echo ✓ Dependencies installed
echo.

REM Install SHINIGAMI-EYE
echo [5/5] Installing SHINIGAMI-EYE...
python -m pip install -e .
echo ✓ SHINIGAMI-EYE installed
echo.

echo ============================================
echo     Installation Complete! 🎉
echo ============================================
echo.
echo Usage:
echo   shinigami-eye --help
echo   shinigami-eye portscan -t ^<target^>
echo   shinigami-eye webrecon -d ^<domain^>
echo   shinigami-eye full -t ^<target^>
echo.
echo ⚠️  Remember: Educational use only!
echo.
pause
