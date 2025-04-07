import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
<<<<<<< HEAD
=======
        response.raise_for_status()  # Raises exception for 4XX/5XX status codes
>>>>>>> 3f60f6a759b70b0fda440f70f14fc5e260b5084d
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
<<<<<<< HEAD

=======
>>>>>>> 3f60f6a759b70b0fda440f70f14fc5e260b5084d
