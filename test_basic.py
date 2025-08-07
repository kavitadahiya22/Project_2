"""
Simple API test without requiring Ollama to be fully ready
"""
import requests

API_BASE_URL = "http://localhost:8000"

def test_root_endpoint():
    """Test root endpoint - doesn't require Ollama"""
    print("🔍 Testing root endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/")
        print(f"✅ Root endpoint: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Root endpoint failed: {e}")
        return False

def test_health_basic():
    """Test health endpoint - basic functionality"""
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        print(f"✅ Health endpoint: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health endpoint failed: {e}")
        return False

def test_models_endpoint():
    """Test models endpoint"""
    print("🔍 Testing models endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/models")
        result = response.json()
        print(f"✅ Models endpoint: {result}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Models endpoint failed: {e}")
        return False

def main():
    """Run basic tests that don't require full model download"""
    print("🚀 Testing Penetration Testing API - Basic Tests")
    print("=" * 50)
    
    # Test endpoints that don't require full Ollama setup
    tests_passed = 0
    total_tests = 3
    
    if test_root_endpoint():
        tests_passed += 1
    
    if test_health_basic():
        tests_passed += 1
    
    if test_models_endpoint():
        tests_passed += 1
    
    print(f"\n📊 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("✅ Basic API functionality is working!")
        print("\n📝 Note: The Ollama model is still downloading.")
        print("   Once download completes, you can test the pentest endpoint.")
        print("   Use 'python test_client.py' for full testing.")
    else:
        print("❌ Some tests failed. Check the API server status.")

if __name__ == "__main__":
    main()
