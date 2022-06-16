
import requests
import json

def isFavorite(placeid, session: requests.Session):
    headers = { "Accept": "application/json" }
    url ="https://games.roblox.com/v1/games/3233893879/favorites"
    return json.loads(session.get(url, headers=headers).content.decode("utf-8"))
