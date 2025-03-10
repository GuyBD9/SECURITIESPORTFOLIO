# controllers/ai_controller.py
from ai.ollama_model import OllamaModel

class AIController:
    def __init__(self):
        self.ai_model = OllamaModel()

    def consult_ai(self, question: str) -> str:
        return self.ai_model.query(question)
