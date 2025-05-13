import ollama

class LocalLLM:
    def __init__(self, model_name="deepseek-coder:6.7b"):
        self.model_name = model_name

    def generate(self, prompt):
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response['message']['content']
        except Exception as e:
            return f"[LLM Error] {str(e)}"
