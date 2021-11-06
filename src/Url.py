class Url(object):
        def __init__(self):
            self.url = 'https://api.trello.com/1/'
        
        def getBaseUrl(self):
            return self.url
        
        def getBoadId(self):
            return 'mako-today-board'
    

        def getURLForAllBoards(self):
            url = self.getBaseUrl() + 'members/me/boards/'
            return url

        def getURLForBoards(self):
            url = self.getURLForAllBoards() + self.getBoadId()
            return url
        
        