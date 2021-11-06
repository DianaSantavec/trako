from InitialRun import *

class Trako(object):

    def __init__(self):
        pass

    
    def setupUserToken(self):
        init = InitialRun()
        init.setup()

        
    
    def getData(self):
        raise NotImplementedError()
    
    def uploadData(self):
        raise NotImplementedError()

obj = Trako()
obj.setupUserToken()
sys.exit(0)