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

    def getHeaderForMakoBoard(self):
        header = self.auth.getAuthParameters()
        header['Accept'] = 'application/json'
        return header
