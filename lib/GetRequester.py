import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raises exception for 4XX/5XX status codes
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
