class AuthValues (object):
    def __init__ (self, key, token):
        self.key = key
        self.token = token
    
    def getKey(self):
        return self.key
    
    def getParameters(self):
        parameters = ['key':self.key, 'token':self.token]
        return  parameters


class Parameters (object):
    def __init__ (self, authValues):
        self.key = authValues[0]
        self.token = authValues[1]
    
    def __init__ (self, authValues, )
    def generate_url(self):
        url = 
    
    def generate_url(self)