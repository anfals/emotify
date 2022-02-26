import requests
import json

# class HuggingEmotify:
#     def __init__(self):
#         self.API_URL = "https://api-inference.huggingface.co/models/jpreilly123/emojify_mvp"
#         self.headers = {
#             "Authorization": "Bearer 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"}

#     def query(self, payload):
#         response = requests.post(
#             self.API_URL, headers=self.headers, json=payload)
#         return response.json()


class ModelCloudRun:
    def __init__(self):
        self.API_URL = 'https://flask-app-b6jw7kny2q-wm.a.run.app'

    def predict(self, tweet):
        task = 'predict'
        PARAMS = {'tweet': tweet}
        response = requests.get('https://flask-app-b6jw7kny2q-wm.a.run.app/{}'.format(task),
                                params=PARAMS)

        if response.status_code == 200:
            return json.loads(response.text)
