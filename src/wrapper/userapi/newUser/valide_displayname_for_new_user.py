# Validate a display name for a new user

import requests

def validateDisplayName(displayName, birthdate):
    headers = {
        'Accept: application/json'
    }
    url = "https://users.roblox.com/v1/display-names/validate?displayName={}&birthdate={}".format(displayName, birthdate)
    
    r = requests.get(url, headers=headers)
    return r.content.decode("utf-8")
