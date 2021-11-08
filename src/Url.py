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

        def getURLForMakoBoard(self):
            url = self.getURLForAllBoards()
            return url
        
        def getURLForCreateMakoBoard(self):
            url = self.getBaseUrl() + 'boards/'
            return url

        def getURLForMakoOrganizationCreation(self):
            url = self.getBaseUrl() + 'organizations/'
            return url
        
        def getURLForMakoCards(self, id):
            url = self.getBaseUrl() + 'boards/' + id + '/cards'
            return url

        def getURLForCard(self, cardId):
            url = self.getBaseUrl() + 'cards/' + cardId
            return url
        
        def getURLForList(self, listId):
            url = self.getBaseUrl() + 'lists/' + listId
            return url

        def getURLForCardCreation(self):
            url = self.getBaseUrl() + 'cards/'
            return url
        
        def getURLForAllLists(self, boadId):
            url = self.getBaseUrl() + 'boards/' + boadId + '/lists'
            return url
        
        def getURLForDeleteMakoCards(self, cardId):
            url = self.getBaseUrl() + 'cards/' + cardId
            return url