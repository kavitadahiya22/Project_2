# PowerShell startup script for Penetration Testing API
Write-Host "Starting Penetration Testing API with Custom AI Agents" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green

# Check if virtual environment exists
if (-not (Test-Path "venv\Scripts\Activate.ps1")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

# Install/update dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Check if Ollama is running
Write-Host "Checking Ollama service..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:11434/api/version" -TimeoutSec 5 -ErrorAction Stop
    Write-Host "✅ Ollama service is running" -ForegroundColor Green
} catch {
    Write-Host ""
    Write-Host "⚠️  WARNING: Ollama service is not running!" -ForegroundColor Red
    Write-Host "Please start Ollama service in another terminal:" -ForegroundColor Yellow
    Write-Host "  ollama serve" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Then download the Deepseek model:" -ForegroundColor Yellow
    Write-Host "  ollama pull deepseek-r1:1.5b" -ForegroundColor Cyan
    Write-Host ""
    Read-Host "Press Enter to continue anyway..."
}

# Start the API server
Write-Host "Starting API server..." -ForegroundColor Yellow
Write-Host "API Documentation will be available at: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""

python main.py
