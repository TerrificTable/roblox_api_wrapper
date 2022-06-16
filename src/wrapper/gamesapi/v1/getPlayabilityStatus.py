# Gets a list of universe playability statuses for the authenticated user

import requests
import json

def getPlayabilityStatus(ids):
    url = "https://games.roblox.com/v1/games/multiget-playability-status?universeIds="
    if (type(ids) == list or type(ids) == dict):
        for id in ids:
            url += id + ","
        url = url[:-1]
    else:
        url += id
    headers = { "Accept": "application/json" }

    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
