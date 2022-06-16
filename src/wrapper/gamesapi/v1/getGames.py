# Gets a list of games' detail

import requests
import json


def getGames(ids):
    headers = {
        "Accept": "application/json"
    }
    url = "https://games.roblox.com/v1/games?universeIds={}".format(ids)

    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
