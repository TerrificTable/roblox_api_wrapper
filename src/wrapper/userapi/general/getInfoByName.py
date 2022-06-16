# Gets the age bracket of the user

import requests
import json

class infoByName:
    def __init__(self, username, excludeBanned: bool = False) -> None:
        self.username = username
        self.excludeBanned = excludeBanned
        self.getUserInfoByName()

    def getUserInfoByName(self):
        data = {
            "usernames": [
                self.username
            ],
            "excludeBannedUsers": "true" if self.excludeBanned else "false"
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        url = "https://users.roblox.com/v1/usernames/users"

        r = requests.post(url, headers=headers, json=data)
        jsonData = json.loads(r.content.decode("utf-8"))

        self.awnser = jsonData
        self.requestedUsername = self.awnser["data"][0]["requestedUsername"]
        self.id = self.awnser["data"][0]["id"]
        self.name = self.awnser["data"][0]["name"]
        self.displayName = self.awnser["data"][0]["displayName"]


        return self.awnser
