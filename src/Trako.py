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
        
        
    
    def uploadData(self,listOfTasks):
        """
        expects list of Data objects
        """
        board = Board()
        board.deleteOldData()
        board.uploadToBoard(listOfTasks)

obj = Trako()
#obj.setupUserToken()
data = obj.getData()
for item in data:
    item.time_estimate = '1'

obj.uploadData(data)
sys.exit(0)