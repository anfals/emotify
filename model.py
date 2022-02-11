import requests


class HuggingEmotify:
    def __init__(self):
        self.API_URL = "https://api-inference.huggingface.co/models/jpreilly123/emojify_mvp"
        self.headers = {
            "Authorization": "Bearer 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"}

    def query(self, payload):
        response = requests.post(
            self.API_URL, headers=self.headers, json=payload)
        return response.json()
