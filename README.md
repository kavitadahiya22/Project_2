# Penetration Testing API with Custom Agents

A comprehensive Python-based penetration testing API that leverages custom AI agents and the Ollama Deepseek model to perform automated security assessments.

## Features

- **FastAPI REST API** with comprehensive endpoints
- **Custom Agent Framework** with specialized penetration testing agents:
  - Network Reconnaissance Agent
  - Vulnerability Assessment Agent
  - Exploitation Validation Agent
  - Reporting Agent
- **Ollama Integration** with automatic Deepseek model management
- **Modular Architecture** for easy extension and maintenance
- **Professional Reporting** with structured vulnerability findings
- **Async Processing** for handling long-running penetration tests

## Project Structure

```
Project_2/
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Python dependencies
├── setup.py                   # Automated setup script
├── test_client.py             # API testing client
├── .env                       # Environment configuration
├── models/
│   ├── __init__.py
│   └── request_models.py      # Pydantic models for API
├── agents/
│   ├── __init__.py
│   ├── base_agent.py          # Base agent class
│   ├── network_recon_agent.py # Network reconnaissance
│   ├── vuln_assessment_agent.py # Vulnerability assessment
│   ├── exploitation_agent.py  # Safe exploitation validation
│   ├── reporting_agent.py     # Report generation
│   └── pentest_crew.py        # Main crew orchestrator
└── utils/
    ├── __init__.py
    └── ollama_manager.py       # Ollama model management
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Internet connection for downloading models
- Windows, macOS, or Linux

### Option 1: Automated Setup

1. **Clone or navigate to the project directory**
   ```powershell
   cd "c:\Users\KavitaDeshwal\Desktop\cybr\Project_2\Project_2"
   ```

2. **Run the automated setup script**
   ```powershell
   python setup.py
   ```

3. **Activate the virtual environment and start the API**
   ```powershell
   venv\Scripts\activate
   python main.py
   ```

### Option 2: Manual Setup

1. **Install Ollama**
   - Download from: https://ollama.com/download
   - Start the service: `ollama serve`

2. **Download the Deepseek model**
   ```powershell
   ollama pull deepseek-r1:1.5b
   ```

3. **Create Python virtual environment**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install Python dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

5. **Start the API server**
   ```powershell
   python main.py
   ```

## API Usage

### Access the API Documentation
Once the server is running, visit: http://localhost:8000/docs

### Main Endpoints

#### 1. Health Check
```http
GET /health
```

#### 2. Invoke Penetration Test
```http
POST /invoke-pentest
```

**Request Body:**
```json
{
  "target": "192.168.1.1",
  "pentest_type": "network",
  "scope": ["ssh", "http", "https"],
  "depth": 3,
  "timeout": 300
}
```

**Response:**
```json
{
  "success": true,
  "message": "Penetration test completed successfully",
  "task_id": "pentest_20241201_123456",
  "result": {
    "target": "192.168.1.1",
    "pentest_type": "network",
    "status": "completed",
    "vulnerabilities": [...],
    "summary": "Assessment completed",
    "recommendations": [...]
  }
}
```

#### 3. Available Models
```http
GET /models
```

#### 4. Download Model
```http
POST /download-model
```

## Testing

Run the included test client to verify everything works:

```powershell
python test_client.py
```

## Agent Architecture

### 1. Network Reconnaissance Agent
- Performs network discovery and port scanning
- Identifies live hosts and running services
- Maps network topology and attack surface

### 2. Vulnerability Assessment Agent
- Analyzes discovered services for vulnerabilities
- Researches CVE databases and security advisories
- Assigns CVSS scores and risk ratings

### 3. Exploitation Agent
- Safely validates vulnerabilities through PoC exploits
- Demonstrates potential impact without causing damage
- Documents evidence and exploitation paths

### 4. Reporting Agent
- Generates professional penetration testing reports
- Creates executive summaries and technical findings
- Provides prioritized remediation recommendations

## Configuration

Environment variables in `.env`:

```env
OLLAMA_HOST=localhost:11434
OLLAMA_MODEL=deepseek-r1:1.5b
LOG_LEVEL=INFO
APP_HOST=0.0.0.0
APP_PORT=8000
```

## Security Considerations

- This tool is designed for authorized penetration testing only
- Always obtain proper authorization before testing any systems
- The exploitation agent uses safe validation techniques
- All activities are logged for audit purposes

## Troubleshooting

### Common Issues

1. **Ollama service not running**
   - Ensure Ollama is installed and running: `ollama serve`

2. **Model not found**
   - Download the model: `ollama pull deepseek-r1:1.5b`

3. **Import errors**
   - Ensure virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

4. **API timeout**
   - Penetration tests can take several minutes
   - Increase timeout values if needed

## License

This project is intended for educational and authorized security testing purposes only.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For issues and questions, please create an issue in the repository or contact the development team.