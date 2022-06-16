# Get private servers from private server ids

import requests
import json

def getPrivateServers(privId):
    url = "https://games.roblox.com/v1/private-servers?privateServerIds=" + privId
    headers = { "Accept": "application/json" }

    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
