import os
import requests

class YouTubeToText:
    def __init__(self, api_key: str, base_url: str="https://api.youtubetotext.com"):
        self.base = base_url.rstrip('/')
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def transcript(self, video_id: str, lang: str=None):
        """
        Fetches transcript.
        lang: comma-separated codes, e.g. 'en,es,fr'
        """
        params = {}
        if lang:
            params["lang"] = lang
        response = requests.get(
            f"{self.base}/transcript/{video_id}",
            headers=self.headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
