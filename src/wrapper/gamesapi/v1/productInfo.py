# Gets a list of games' product info, used to purchase a game

import requests
import json

def getProductInfo(ids):
    headers = {
        "Accept": "application/json"
    }
    url = "https://games.roblox.com/v1/games/games-product-info?universeIds={}".format(ids)
    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
