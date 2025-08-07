"""
Base agent class for penetration testing - Custom implementation
"""
import asyncio
import logging
from typing import Optional, Dict, Any
import os
from dotenv import load_dotenv
import requests

load_dotenv()
logger = logging.getLogger(__name__)

class BaseAgent:
    """Base class for all penetration testing agents"""
    
    def __init__(self):
        self.ollama_host = os.getenv("OLLAMA_HOST", "localhost:11434")
        self.ollama_model = os.getenv("OLLAMA_MODEL", "deepseek-r1:1.5b")
        self.role = ""
        self.goal = ""
        self.backstory = ""
    
    def setup_agent(self, role: str, goal: str, backstory: str):
        """Setup agent configuration"""
        self.role = role
        self.goal = goal
        self.backstory = backstory
    
    async def execute_task(self, task_description: str, context: Optional[str] = None) -> str:
        """Execute a task using the agent's capabilities"""
        try:
            # Build the prompt with agent's role and context
            prompt = self._build_prompt(task_description, context)
            
            # Execute the ollama request
            result = await self._call_ollama(prompt)
            
            logger.info(f"Agent {self.role} completed task")
            return result
            
        except Exception as e:
            logger.error(f"Agent {self.role} task failed: {e}")
            return f"Task failed: {str(e)}"
    
    async def _call_ollama(self, prompt: str) -> str:
        """Call Ollama API directly"""
        try:
            import ollama
            
            # Use ollama client
            loop = asyncio.get_event_loop()
            client = ollama.Client(host=f"http://{self.ollama_host}")
            
            response = await loop.run_in_executor(
                None,
                lambda: client.generate(
                    model=self.ollama_model,
                    prompt=prompt,
                    stream=False
                )
            )
            
            return response['response']
            
        except ImportError:
            # Fallback to HTTP requests if ollama client fails
            return await self._call_ollama_http(prompt)
        except Exception as e:
            logger.error(f"Ollama call failed: {e}")
            return f"Failed to get AI response: {str(e)}"
    
    async def _call_ollama_http(self, prompt: str) -> str:
        """Fallback HTTP call to Ollama API"""
        try:
            url = f"http://{self.ollama_host}/api/generate"
            payload: Dict[str, Any] = {
                "model": self.ollama_model,
                "prompt": prompt,
                "stream": False
            }
            
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None,
                lambda: requests.post(url, json=payload, timeout=120)
            )
            
            if response.status_code == 200:
                return response.json().get('response', 'No response from AI')
            else:
                return f"HTTP Error {response.status_code}: {response.text}"
                
        except Exception as e:
            logger.error(f"HTTP Ollama call failed: {e}")
            return f"Failed to connect to Ollama: {str(e)}"
    
    def _build_prompt(self, task_description: str, context: Optional[str] = None) -> str:
        """Build a comprehensive prompt for the LLM"""
        prompt = f"""You are a {self.role}.

Your goal: {self.goal}

Your background: {self.backstory}

Task: {task_description}
"""
        
        if context:
            prompt += f"\nContext from previous tasks:\n{context}\n"
        
        prompt += """
Please provide a detailed, professional response that includes:
1. Analysis of the current situation
2. Step-by-step approach
3. Technical findings or recommendations
4. Risk assessment where applicable
5. Next steps or additional considerations

Format your response clearly with proper sections and technical details.
"""
        
        return prompt
