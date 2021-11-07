from Url import *
from Headers import *
import requests

class Board(object):
    def __init__(self):
        self.boardName = 'mako'
        self.organizationName = 'makoorganization'
        self.organizationDisplayName = 'Mako-organization'
        self.accessUrl = Url()
        self.accessHeaders = Header()

    def printInvalidToken(self):
        print('Token is not valid')
    
    def printInvalidUrl(self):
        print('Url is not valid')
    
    def getAllBoards(self):
        url = self.accessUrl.getURLForAllBoards()  
        header = self.accessHeaders.getHeaderForBoards()

        response = requests.get(url, params=header)

        if (response.status_code == 401):
            self.printInvalidToken()
            raise ValueError()
        elif (response.status_code == 404):
            self.printInvalidUrl()
            raise ValueError()
        else:
            boards_in_json = response.json()
            return boards_in_json

    
    def checkMakoOrganization(self):
        url = self.accessUrl.getURLForMakoOrganization(self.organizationName)
        header = self.accessHeaders.getHeaderForMakoOrganization()

        print(url)
        print(header)

        response = requests.get(url, params=header)

        if (response.status_code == 404):
            return 404
        elif (response.status_code == 401):
            self.printInvalidToken()
            return 401
        else:
            return 200
        print(response)

    def createMakoWorkspace(self):
        url = self.accessUrl.getURLForMakoOrganizationCreation()
        header = self.accessHeaders.getHeaderForMakoOrganizationCreation(self.organizationName, self.organizationDisplayName)

        response = requests.request("POST", url, params=header) 
        if (response.status_code == 401 or response.status_code == 404):
            return False
        else:
            return True
        
        
    def createMakoBoard(self):
        url = self.accessUrl.getURLForCreateMakoBoard()
        header = self.accessHeaders.getHeaderForBoardCreation(self.boardName, self.organizationName)

        response = requests.request("POST", url, params=header)   
        if (response.status_code == 401 or response.status_code == 404):
            return False
        else:
            return True     

    def checkMakoBoard(self):
        url = self.accessUrl.getURLForMakoBoard(self.boardName)
        header = self.accessHeaders.getHeaderForMakoBoard()

        response = requests.get(url, params=header)

        if (response.status_code == 404):
            return 404
        elif(response.status_code == 401):
            return 401
        else:
            return 200


    def getDataFromBoard(self):
        accessUrl = Url()
        url = accessUrl.getURLForMakoBoard()
        

        data = ''
        return data