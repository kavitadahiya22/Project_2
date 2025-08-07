"""
Installation and setup script for the Penetration Testing API
"""
import subprocess
import sys
import os
import requests
import time

def run_command(command: str, description: str):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_ollama_service():
    """Check if Ollama service is running"""
    try:
        response = requests.get("http://localhost:11434/api/version", timeout=5)
        return response.status_code == 200
    except:
        return False

def install_ollama():
    """Install Ollama if not present"""
    print("\n🔍 Checking Ollama installation...")
    
    if check_ollama_service():
        print("✅ Ollama is already running")
        return True
    
    print("📥 Ollama not found. Installing Ollama...")
    
    # Download and install Ollama for Windows
    install_cmd = 'curl -fsSL https://ollama.com/install.sh | sh'
    if os.name == 'nt':  # Windows
        print("Please install Ollama manually from: https://ollama.com/download")
        print("After installation, run: ollama serve")
        return False
    
    if not run_command(install_cmd, "Installing Ollama"):
        return False
    
    # Start Ollama service
    print("🚀 Starting Ollama service...")
    if os.name != 'nt':
        run_command("ollama serve &", "Starting Ollama service")
        time.sleep(5)  # Wait for service to start
    
    return check_ollama_service()

def download_deepseek_model():
    """Download Deepseek model"""
    print("\n📦 Downloading Deepseek model...")
    
    if not check_ollama_service():
        print("❌ Ollama service is not running. Please start it first.")
        return False
    
    # Download the model
    return run_command("ollama pull deepseek-r1:1.5b", "Downloading Deepseek model")

def setup_python_environment():
    """Set up Python virtual environment and install dependencies"""
    print("\n🐍 Setting up Python environment...")
    
    # Create virtual environment
    if not run_command("python -m venv venv", "Creating virtual environment"):
        return False
    
    # Activate virtual environment and install requirements
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate && pip install -r requirements.txt"
    else:  # Linux/Mac
        activate_cmd = "source venv/bin/activate && pip install -r requirements.txt"
    
    return run_command(activate_cmd, "Installing Python dependencies")

def main():
    """Main setup function"""
    print("🚀 Setting up Penetration Testing API with Custom AI Agents")
    print("=" * 50)
    
    success = True
    
    # Step 1: Setup Python environment
    if not setup_python_environment():
        print("❌ Failed to setup Python environment")
        success = False
    
    # Step 2: Install Ollama
    if not install_ollama():
        print("❌ Failed to install/start Ollama")
        success = False
    
    # Step 3: Download Deepseek model
    if success and not download_deepseek_model():
        print("❌ Failed to download Deepseek model")
        success = False
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Setup completed successfully!")
        print("\n🚀 To start the API server:")
        if os.name == 'nt':
            print("   venv\\Scripts\\activate")
        else:
            print("   source venv/bin/activate")
        print("   python main.py")
        print("\n📖 API Documentation will be available at: http://localhost:8000/docs")
    else:
        print("❌ Setup failed. Please check the errors above and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
