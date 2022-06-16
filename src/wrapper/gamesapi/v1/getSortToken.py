# Gets an ordered list of all sorts

import requests
import json

def getSortToken():
    url = "https://games.roblox.com/v1/games/sorts"
    headers = { "Accept": "application/json" }

    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
