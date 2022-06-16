# Set the display name for the authorized user.

import requests

def setDisplayNameForAuthUser(userid, request: set):
    headers = {
        'Accept: application/json' 
    }
    url = "https://users.roblox.com/v1/users/{}/display-names".format(userid)

    r = requests.get(url, headers=headers)
    return r.content.decode("utf-8")
