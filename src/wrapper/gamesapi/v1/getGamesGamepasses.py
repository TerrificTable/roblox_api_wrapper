
import requests
import json

def getGamepasses(id, limit):
    headers = { "Accept": "application/json" }
    if (limit < 10): limit = 10
    if (limit < 25 and limit > 10): limit = 25
    if (limit < 59 and limit > 25): limit = 50
    if (limit > 100 or limit > 50): limit = 100
    url = "https://games.roblox.com/v1/games/{}/game-passes?limit={}".format(id, limit)

    return json.loads(requests.get(url, headers=headers).content.decode("utf-8"))
