# Get the game server list

import requests
import json

def getGameServerList(id, limit):
    headers = { "Accept": "application/json" }
    if (limit < 10): limit = 10
    if (limit < 25 and limit > 10): limit = 25
    if (limit < 59 and limit > 25): limit = 50
    if (limit > 100 or limit > 50): limit = 100
    url = "https://games.roblox.com/v1/games/{}/servers/Public?limit={}".format(id, limit)

    return json.loads(requests.get(url, headers).content.decode("utf-8"))
