# 

import requests
import json

class searchUserbyName:
    def __init__(self, keyword, limit: int = 100):
        self.keyword = keyword
        self.limit = limit
        self.searchUserbyName()

    def searchUserbyName(self):
        headers = {
            "Accept": "application/json"
        }
        if (self.limit < 10): self.limit = 10
        if (self.limit < 25 and self.limit > 10): self.limit = 25
        if (self.limit < 59 and self.limit > 25): self.limit = 50
        if (self.limit > 100 or self.limit > 50): self.limit = 100
        url = "https://users.roblox.com/v1/users/search?keyword={}&limit={}".format(self.keyword, self.limit)
        
        r = requests.get(url, headers=headers)
        
        jsonData = json.loads(r.content.decode("utf-8"))
        self.awnser = jsonData
        self.data = self.awnser["data"]
        self.results = len(self.data)

        return self.data

    def getUserInfo(self, index: int):
        return self.data[index]
