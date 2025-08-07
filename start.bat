@echo off
echo Starting Penetration Testing API with Custom AI Agents
echo ==========================================

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Check if Ollama is running
echo Checking Ollama service...
curl -s http://localhost:11434/api/version >nul 2>&1
if errorlevel 1 (
    echo.
    echo WARNING: Ollama service is not running!
    echo Please start Ollama service in another terminal:
    echo   ollama serve
    echo.
    echo Then download the Deepseek model:
    echo   ollama pull deepseek-r1:1.5b
    echo.
    pause
)

REM Start the API server
echo Starting API server...
echo API Documentation will be available at: http://localhost:8000/docs
echo.
python main.py
