from InitialRun import *
from Board import *

class Trako(object):

    def __init__(self):
        pass
    
    def setupUserToken(self):
        init = InitialRun()
        init.setup()

    
    def getData(self):
        board = Board()
        board.getAllCards()
        #raise NotImplementedError()
        #board = Board()
        #data = getDataFromBoard()
        
        #return data
        
    
    def uploadData(self):
        raise NotImplementedError()

obj = Trako()
#obj.setupUserToken()
obj.getData()
sys.exit(0)