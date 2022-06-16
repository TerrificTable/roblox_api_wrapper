# Get place details

import requests
import json

def getGameDetails(placeIds):
    url = "https://games.roblox.com/v1/games/multiget-place-details?"
    if (type(placeIds) == list or type(placeIds) == dict):
        for id in placeIds:
            url += "placeIds=" + id + "&"
        url = url[:-1]
    else:
        url += "placeIds=" + id
    headers = { "Accept": "application/json" }

    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
