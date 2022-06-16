# Get the vote status successfully.

import requests
import json

def getGameVotes(ids):
    url = "https://games.roblox.com/v1/games/votes?universeIds="
    if (type(ids) == list or type(ids) == dict):
        for id in ids:
            url += id + ","
        url = url[:-1]
    else:
        url += id
    headers = { "Accept": "application/json" }

    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
