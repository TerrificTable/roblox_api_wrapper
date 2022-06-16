# Get the favorites count of the a specific game

import requests
import json

def getFavoriteCount(id):
    url = "https://games.roblox.com/v1/games/{}/favorites/count".format(id)
    headers = { "Accept": "application/json" }

    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
    