import ollama
from screengenie.helpers.config import load_config

class LocalLLM:
    def __init__(self):
        cfg = load_config()
        self.model_name = cfg["llm"].get("model_name", "deepseek-coder:6.7b")

    def generate(self, prompt):
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            return response["message"]["content"]
        except Exception as e:
            return f"[LLM Error] {e}"

