# Get the user's vote status for a game

import requests
import json

def getGameVotable(id, session: requests.Session):
    headers = { "Accept": "application/json" }
    url = "https://games.roblox.com/v1/games/{}/votes/user".format(id)
    return json.loads(session.get(url, headers=headers).content.decode("utf-8"))
