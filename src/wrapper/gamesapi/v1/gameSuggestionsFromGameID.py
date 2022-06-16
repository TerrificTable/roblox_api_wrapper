# Get games recommendations based on a given universe

import requests
import json

def getSugguestions(id):
    url = "https://games.roblox.com/v1/games/recommendations/game/" + id
    headers = { "Accept": "application/json" }

    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
