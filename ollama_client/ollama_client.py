import os
from dotenv import load_dotenv
import ollama

# Load environment variables
load_dotenv()

class OllamaClient:
    def __init__(self, model: str = None):
        self.model = model or os.getenv("OLLAMA_MODEL", "deepseek-r1:latest")

    def send_prompt(self, prompt: str):
        try:
            response = ollama.generate(model=self.model, prompt=prompt)
            return response.get("response", "")
        except Exception as e:
            print(f"[ERROR] Failed to connect to Ollama: {e}")
            return None
