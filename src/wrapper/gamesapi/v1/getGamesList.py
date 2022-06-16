# Gets a list of games

import requests
import random
import json

class getGameList:
    def __init__(self,
                keyword = "",
                sessionId = "",
                sortPosition = "",
                isSeeAllPage: bool = "",
                pageId = "",
                contextUniverseId = "",
                contextCountryRegionId = "",
                maxRows = "",
                startRows = "",
                gameSetTargetId = "",
                sortOrder = "",
                exclusiveStartId = "",
                genreFilter = "",
                timeFilter = "",
                gameFilter = "",
                sortToken = ""
            ):
        self.keyword                = keyword
        self.sessionId              = sessionId
        self.sortPosition           = sortPosition
        self.isSeeAllPage           = isSeeAllPage
        self.pageId                 = pageId
        self.contextUniverseId      = contextUniverseId
        self.contextCountryRegionId = contextCountryRegionId
        self.maxRows                = maxRows
        self.startRows              = startRows
        self.gameSetTargetId        = gameSetTargetId
        self.sortOrder              = sortOrder
        self.exclusiveStartId       = exclusiveStartId
        self.genreFilter            = genreFilter
        self.gameFilter             = gameFilter
        self.timeFilter             = timeFilter
        self.sortToken              = sortToken

        self.getList()


    def getList(self):
        headers = {
            "Accept": "application/json"
        }
        baseurl = "https://games.roblox.com/v1/games/list?_={}".format(random.randint(0, 10000000) * 1000)
        url = baseurl
        if (self.keyword != ""): url += "&keyword=" + self.keyword
        if (self.sessionId != ""): url += "&sessionId=" + self.sessionId
        if (self.sortPosition != ""): url += "&sortPosition=" + self.sortPosition
        if (self.isSeeAllPage != ""): url += "&isSeeAllPage=" + self.isSeeAllPage
        if (self.pageId != ""): url += "&pageId=" + self.pageId
        if (self.contextUniverseId != ""): url += "&contextUniverseId=" + self.contextUniverseId
        if (self.contextCountryRegionId != ""): url += "&contextCountryRegionId=" + self.contextCountryRegionId
        if (self.maxRows != ""): url += "&maxRows=" + self.maxRows
        if (self.startRows != ""): url += "&startRows=" + self.startRows
        if (self.gameSetTargetId != ""): url += "&gameSetTargetId=" + self.gameSetTargetId
        if (self.sortOrder != ""): url += "&sortOrder=" + self.sortOrder
        if (self.exclusiveStartId != ""): url += "&exclusiveStartId=" + self.exclusiveStartId
        if (self.genreFilter != ""): url += "&genreFilter=" + self.genreFilter
        if (self.gameFilter != ""): url += "&gameFilter=" + self.gameFilter
        if (self.timeFilter != ""): url += "&timeFilter=" + self.timeFilter
        if (self.sortToken != ""): url += "&sortToken=" + self.sortToken

        r = requests.get(url, headers=headers)
        jsonData = json.loads(r.content.decode("utf-8"))
        self.awnser = jsonData
        self.games = self.awnser["games"]
        self.gameAmount = len(self.games)

        return self.awnser

    def getGameIndex(self, index: int):
        return self.games[index]
