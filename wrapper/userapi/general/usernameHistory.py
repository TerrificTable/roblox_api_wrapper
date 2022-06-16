# Retrieves the username history for a particular user.

import requests

def getUsernameHistory(userid):
    headers = {
        "Accept": "application/json"
    }
    url = "https://users.roblox.com/v1/users/{}/username-history?limit=100&sortOrder=Asc".format(userid)

    r = requests.get(url, headers=headers)
    return r.content.decode("utf-8")
    