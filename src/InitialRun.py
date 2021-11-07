import os
import sys
from Board import *

class InitialRun(object):
    def __init__(self):
        self.secretsDir = '../.secrets'
        self.secretsFile = '../.secrets/token'

    def printMessageWithURL(self):
        print('''To allow Mako to create board, and to get data from the board,
key must be saved in .secrets/key file and will be valid for one month, or while you disable it
Key can be get on: https://trello.com/1/authorize?&name=MyPersonalToken&scope=read&scope=write&response_type=token&key=fcf13eab00317ac32b50020c2ff8ef81
After saving tocker, run this script again to setup board ''')

    def setupFileForToken(self):
        if (os.path.exists(self.secretsDir)):
            if (os.path.isfile(self.secretsFile)):
                    return True
        else:
            os.mkdir(self.secretsDir)
            file = open(self.secretsFile,'w')
            file.close()
            self.printMessageWithURL()
            return False

    def testToken(self):
        board = Board()
        if (board.checkMakoOrganization() == 401):
            raise ValueError()
            return False
        return True

    def initTrello(self):
        board = Board()
        if (board.checkMakoOrganization() == 404):
            board.createMakoWorkspace()
            board.createMakoBoard()
        else:
            if (board.checkMakoBoard() == 404):
                board.createMakoBoard()   
        
        return True
            

    
    def setup(self):

        if (self.setupFileForToken() == True):
            if (self.testToken() == True):
                self.initTrello()
        
        else:
            raise ValueError()
            return False