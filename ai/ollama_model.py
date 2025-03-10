import requests

class OllamaModel:
    def __init__(self, server_url: str = "http://localhost:11434"):
        self.server_url = server_url

    def query(self, question: str) -> str:
        """
        Sends a query to the local Ollama AI server and returns the answer.
        """
        try:
            # Updated endpoint, if applicable:
            response = requests.post(f"{self.server_url}/api/query", json={"question": question})
            if response.status_code == 200:
                return response.json().get("answer", "No answer available")
            else:
                return f"Error: Status {response.status_code}"
        except Exception as e:
            return f"Exception occurred: {str(e)}"
