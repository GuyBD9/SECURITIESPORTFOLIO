import requests

class OllamaModel:
    def __init__(self, server_url: str = "http://127.0.0.1:11434"):
        self.server_url = server_url

    def query(self, question: str) -> str:
        """
        Sends a query to the local Ollama AI server and returns the answer.
        """
        try:
            response = requests.post(f"{self.server_url}/api/generate", json={
                "model": "mistral",  # ודא שיש לך את המודל הזה
                "prompt": question,
                "stream": False
            })
            if response.status_code == 200:
                return response.json().get("response", "No answer available")
            else:
                return f"Error: Status {response.status_code}, {response.text}"
        except Exception as e:
            return f"Exception occurred: {str(e)}"
