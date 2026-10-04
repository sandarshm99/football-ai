import requests


class FootballJsonClient:

    def __init__(self):
        self.base_url = (
            "https://raw.githubusercontent.com/"
            "openfootball/football.json/master"
        )

    def get(self, path):
        url = f"{self.base_url}/{path}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.json()