# Validate a display name for an existing user.

import requests

def validateDisplayName(userid, displayname):
    headers = {
        "Accept": "application/json",
        "cookie": ""
    }
    url = "https://users.roblox.com/v1/users/{}/display-names/validate?displayName={}".format(userid, displayname)

    r = requests.get(url, headers=headers)
    return r.content.decode("utf-8")
