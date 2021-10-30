class Url(object):
        def __init__(self):
            self.url = 'https://api.trello.com/1'
        
        def getBaseUrl(self):
            return self.url
        
        def getBoadId(self):
            return 'mako-today-board'
    

        def getURLForBoards(self):
            url = self.getBaseUrl() + '/boards/' + self.getBoadId()
            return url