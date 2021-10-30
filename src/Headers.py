from src.Authentication import *

class Header(object):
    
    def __init__(self):
        self.boadId = 'mako-today-board'

    def getHeaderForBoards(self, auth):
        header = auth.getAuthParameters() #check good practice
        header['Accept'] = 'application/json'
        return header