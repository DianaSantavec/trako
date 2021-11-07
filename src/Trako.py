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
        data = board.getAllCards()        
        return data
        
        
    
    def uploadData(self):
        raise NotImplementedError()

obj = Trako()
#obj.setupUserToken()
#obj.getData()
obj.uploadData()
sys.exit(0)