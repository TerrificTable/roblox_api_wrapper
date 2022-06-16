# Set the user's vote for a game

import requests
import json

def voteForGame(id, session: requests.Session):
    url = "https://games.roblox.com/v1/games/{}/user-votes".format(id)
    data = { "vote": "true" }
    return json.loads(session.patch(url, headers={ "Accept": "application/json", "Content-Type": "application/json" }).content.decode("utf-8"))