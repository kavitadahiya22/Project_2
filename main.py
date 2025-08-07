"""
Main FastAPI application for Penetration Testing with Custom AI agents
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, BackgroundTasks
from typing import Dict, Any, AsyncGenerator
import logging
import os
from dotenv import load_dotenv

from agents.pentest_crew import PentestCrew
from models.request_models import PentestRequest, PentestResponse
from utils.ollama_manager import OllamaManager

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=getattr(logging, os.getenv("LOG_LEVEL", "INFO")))
logger = logging.getLogger(__name__)

# Initialize managers
ollama_manager = OllamaManager()
pentest_crew = PentestCrew()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Lifespan event handler for FastAPI"""
    # Startup
    logger.info("Starting Penetration Testing API...")
    
    # Check if Ollama is available but don't block startup
    try:
        ollama_available = await ollama_manager.is_available()
        if ollama_available:
            # Try to ensure model is available but don't block
            model_available = await ollama_manager.is_model_available()
            if not model_available:
                logger.warning("Ollama Deepseek model not found - will try to download in background")
                # Start download in background without blocking
                import asyncio
                asyncio.create_task(ollama_manager.download_model())
            else:
                logger.info("Ollama Deepseek model is ready")
        else:
            logger.warning("Ollama service not available - some features may not work")
    except Exception as e:
        logger.warning(f"Could not connect to Ollama during startup: {e}")
        logger.info("API will start anyway - Ollama features may be limited")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Penetration Testing API...")

# Initialize FastAPI app with lifespan
app = FastAPI(
    title="Penetration Testing API with Custom AI Agents",
    description="An API that exposes penetration testing capabilities using custom AI agents powered by Ollama Deepseek model",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Penetration Testing API with Custom AI Agents", "version": "1.0.0"}

@app.get("/health")
async def health_check() -> Dict[str, Any]:
    """Health check endpoint"""
    return {"status": "healthy", "ollama_available": await ollama_manager.is_available()}

@app.post("/invoke-pentest", response_model=PentestResponse)
async def invoke_pentest(request: PentestRequest, background_tasks: BackgroundTasks):
    """
    Invoke penetration testing using custom AI agents
    """
    try:
        logger.info(f"Starting penetration test for target: {request.target}")
        
        # Validate request
        if not request.target:
            raise HTTPException(status_code=400, detail="Target is required")
        
        # Execute penetration testing crew
        result = await pentest_crew.execute_pentest(request)
        
        logger.info("Penetration test completed successfully")
        return result
        
    except Exception as e:
        logger.error(f"Penetration test failed: {e}")
        raise HTTPException(status_code=500, detail=f"Penetration test failed: {str(e)}")

@app.get("/models")
async def get_available_models():
    """Get available Ollama models"""
    try:
        models = await ollama_manager.get_available_models()
        return {"models": models}
    except Exception as e:
        logger.error(f"Failed to get models: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get models: {str(e)}")

@app.post("/download-model")
async def download_model(background_tasks: BackgroundTasks):
    """Download the Deepseek model if not already available"""
    try:
        background_tasks.add_task(ollama_manager.download_model)
        return {"message": "Model download started in background"}
    except Exception as e:
        logger.error(f"Failed to start model download: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to start model download: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host=host, port=port)
