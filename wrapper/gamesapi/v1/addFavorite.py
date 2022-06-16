# Favors (or unfavors) a game for the authenticated user

import requests
import json

def addFavorite(id, session: requests.Session):
    url = "https://games.roblox.com/v1/games/{}/favorites".format(id)
    data = { "isFavorited": "true" }
    headers = { "Accept": "application/json" }
    return json.loads(session.get(url, json=data, headers=headers).content.decode("utf-8"))
    