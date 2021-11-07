class Url(object):
        def __init__(self):
            self.url = 'https://api.trello.com/1/'
        
        def getBaseUrl(self):
            return self.url

        def getURLForAllBoards(self):
            url = self.getBaseUrl() + 'members/me/boards/'
            return url

        def getURLForMakoOrganization(self, makoOrganizationName):
            url = self.getURLForMakoOrganizationCreation() + makoOrganizationName
            return url

        def getURLForMakoBoard(self, boardName):
            url = self.getURLForAllBoards() + boardName
            return url
        
        def getURLForCreateMakoBoard(self):
            url = self.getBaseUrl() + 'boards/'
            return url

        def getURLForMakoOrganizationCreation(self):
            url = self.getBaseUrl() + 'organizations/'
            return url