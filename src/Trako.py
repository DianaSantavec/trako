from InitialRun import *
from Board import *

class Trako(object):

    def __init__(self):
        pass
    
    def setupUserToken(self):
        init = InitialRun()
        init.setup()

    
    def getData(self):
        raise NotImplementedError()
        #board = Board()
        #data = getDataFromBoard()
        
        #return data
        
    
    def uploadData(self):
        raise NotImplementedError()
