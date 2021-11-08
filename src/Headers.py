from Authentication import *

class Header(object):
    
    def __init__(self):
        self.boadId = 'mako-today-board'
        self.auth = Authentication()

    def getHeaderForBoards(self):
        header = self.auth.getAuthParameters()
        header['Accept'] = 'application/json'
        return header
    
    def getHeaderForMakoOrganization(self):
        header = self.auth.getAuthParameters()
        header['Accept'] = 'application/json'
        return header


    def getHeaderForBoardCreation(self, boardName, organizationName):
        header = self.auth.getAuthParameters()
        header['name'] = boardName
        header['idOrganization'] = organizationName
        return header
    
    def getHeaderForMakoOrganizationCreation(self, name, displayName):
        header = self.auth.getAuthParameters()
        header['displayName'] = displayName
        header['name'] = name
        return header

    def getHeaderForMakoBoard(self, boardId):
        header = self.auth.getAuthParameters()
        header['Accept'] = 'application/json'
        header['id'] = boardId
        return header
    
    def getHeaderForMakoCards(self):
        header = self.auth.getAuthParameters()
        header['Accept'] = 'application/json'
        return header
    
    def getHeaderForCard(self):
        header = self.auth.getAuthParameters()
        header['Accept'] = 'application/json'
        return header

    def getHeaderForList(self):
        header = self.auth.getAuthParameters()
        header['Accept'] = 'application/json'
        return header
    
    def getHeaderForCardCreation(self, name, description, due_date, listId):
        header = self.auth.getAuthParameters()
        header['name'] = name
        header['desc'] = description
        header['due'] = due_date
        header['idList'] = listId
        return header

    def getHeaderForAllLists(self):
        header = self.auth.getAuthParameters()
        header['Accept'] = 'application/json'
        return header

    def getHeaderForDeleteMakoCards(self):
        header = self.auth.getAuthParameters()
        header['Accept'] = 'application/json'
        return header
