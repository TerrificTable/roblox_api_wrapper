# Get the spotlight games successfully

import requests
import json


def getSpotlightGames():
    headers = {
        "Accept": "application/json"
    }
    url = "https://games.roblox.com/v1/games/list-spotlight"
    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
