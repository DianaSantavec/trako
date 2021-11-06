class Authentication(object):
    def __init__(self):
        """
        token: token for trello that user generates
        """
        self.token = '' #open file and get token
        self.key = 'fcf13eab00317ac32b50020c2ff8ef81'
    
    def getAuthParameters(self):
        parameters = {'key':self.key, 'token':self.token}
        return  parameters
    

