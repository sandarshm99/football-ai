import os
import requests

from dotenv import load_dotenv


load_dotenv()


class SportmonksClient:

    def __init__(self):
        self.token = os.getenv("SPORTMONKS_TOKEN")

        if not self.token:
            raise ValueError("SPORTMONKS_TOKEN is not configured")

        self.base_url = "https://api.sportmonks.com/v3/football"

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"

        response = requests.get(
            url,
            params={"api_token": self.token},
            timeout=10,
        )

        response.raise_for_status()

        return response.json()