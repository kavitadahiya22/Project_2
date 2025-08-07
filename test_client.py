"""
Simple test client for the Penetration Testing API
"""
import requests
import json
from typing import Dict, Any

API_BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        print(f"✅ Health check: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_pentest():
    """Test penetration testing endpoint"""
    print("🧪 Testing penetration testing endpoint...")
    
    # Sample request
    pentest_request: Dict[str, Any] = {
        "target": "192.168.1.1",
        "pentest_type": "network",
        "scope": ["ssh", "http", "https"],
        "depth": 3,
        "timeout": 300
    }
    
    try:
        print(f"📤 Sending pentest request: {json.dumps(pentest_request, indent=2)}")
        response = requests.post(
            f"{API_BASE_URL}/invoke-pentest",
            json=pentest_request,
            timeout=600  # 10 minutes timeout
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Pentest completed successfully!")
            print(f"📄 Task ID: {result.get('task_id')}")
            print(f"📊 Summary: {result.get('result', {}).get('summary', 'N/A')}")
            return True
        else:
            print(f"❌ Pentest failed: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Pentest request failed: {e}")
        return False

def test_models():
    """Test models endpoint"""
    print("🤖 Testing models endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/models")
        models = response.json()
        print(f"✅ Available models: {models}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Models check failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Testing Penetration Testing API")
    print("=" * 40)
    
    # Test 1: Health check
    if not test_health():
        print("❌ API is not running or not healthy")
        return
    
    # Test 2: Models check
    test_models()
    
    # Test 3: Pentest endpoint (this will take a while)
    print("\n⏳ Starting penetration test (this may take several minutes)...")
    test_pentest()
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    main()
