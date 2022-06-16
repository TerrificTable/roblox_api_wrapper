# Gets detailed user information by id.

import json
import requests

class userInfo:
    def __init__(self, userid) -> None:
        self.userId = userid
        self.getInfo()

    def getInfo(self):
        headers = {
            "Accept": "application/json"
        }
        url = "https://users.roblox.com/v1/users/{}".format(self.userId)

        r = requests.get(url, headers=headers)
        awnser = r.content

        jsonData = json.loads(awnser)
        self.awnser = jsonData
        self.description = self.awnser["description"]
        self.creationDate = self.awnser["created"]
        self.banned = self.awnser["isBanned"]
        self.externalAppDisplayName = self.awnser["externalAppDisplayName"]
        self.id = self.awnser["id"]
        self.name = self.awnser["name"]
        self.displayName = self.awnser["displayName"]

        return self.awnser

    # def getDescription(self): return self.description
    # def getCreationDate(self): return self.created
    # def isBanned(self): return self.banned
    # def getExternalAppDisplayName(self): return self.externalAppDisplayName
    # def getUserID(self): return self.id
    # def getName(self): return self.name
    # def getDisplayName(self): return self.displayName
