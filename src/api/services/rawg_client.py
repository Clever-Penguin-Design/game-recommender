import os
import httpx
from typing import Any, Dict, List


class RawgClient:
    BASE_URL = "https://api.rawg.io/api"

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("RAWG_API_KEY")
        if not self.api_key:
            raise ValueError("RAWG_API_KEY not set")

    async def get_games(self, page: int = 1, page_size: int = 10) -> List[Dict[str, Any]]:
        """
        Retrieve a list of games from RAWG.
        """
        url = f"{self.BASE_URL}/games"
        params = {
            "key": self.api_key,
            "page": page,
            "page_size": page_size,
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, params=params)
                response.raise_for_status()
            except httpx.HTTPError as e:
                raise RuntimeError(f"RAWG API request failed: {e}")

        data = response.json().get("results", [])
        return data