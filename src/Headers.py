from Authentication import *

class Header(object):
    
    def __init__(self):
        self.boadId = 'mako-today-board'

    def getHeaderForBoards(self):
        auth = Authentication()
        header = auth.getAuthParameters() #check good practice
        header['Accept'] = 'application/json'
        return header