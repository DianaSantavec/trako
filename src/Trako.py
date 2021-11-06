from InitialRun import *

class Trako(object):

    def __init__(self):
        #raise NotImplementedError()
        print ('hi')

    
    def setupUserToken(self):
        #raise NotImplementedError()
        init = InitialRun()
        init.setup()

        
    
    def getData(self):
        raise NotImplementedError()
    
    def uploadData(self):
        raise NotImplementedError()

obj = Trako()
obj.setupUserToken()
sys.exit(0)