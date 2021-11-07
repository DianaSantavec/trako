from Url import *
from Headers import *
from Data import *
import requests
import os
import re
import datetime

class Board(object):
    def __init__(self):
        self.boardName = 'mako'
        self.organizationName = 'makoorganization'
        self.organizationDisplayName = 'Mako-organization'
        self.accessUrl = Url()
        self.accessHeaders = Header()
        self.idPath = '../.secrets/id'

    def printInvalidToken(self):
        print('Token is not valid')
    
    def printInvalidUrl(self):
        print('Url is not valid')

    def getBoardId(self):
        filesize = os.path.getsize(self.idPath)
        if (filesize == 0):
            id = self.createMakoBoard()
            file = open(self.idPath,'w')
            file.write(id)
            file.close()
            return id
        else:
            file = open(self.idPath,'r')
            return file.read()
    
    
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

        response = requests.get(url, params=header)

        if (response.status_code == 404):
            return 404
        elif (response.status_code == 401):
            self.printInvalidToken()
            return 401
        else:
            return 200
        

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
            return -1
        else:
            json_response = response.json()
            return json_response['id']

    def checkMakoBoard(self):
        id = self.getBoardId()
        url = self.accessUrl.getURLForMakoBoard()
        header = self.accessHeaders.getHeaderForMakoBoard(id)

        response = requests.get(url, params=header)

        if (response.status_code == 404):
            return 404
        elif(response.status_code == 401):
            return 401
        else:
            return 200
        
    def get_status_name(self, listId):
        url = self.accessUrl.getURLForList(listId)
        header = self.accessHeaders.getHeaderForList()
        response = requests.get(url, params=header)

        response_json = response.json()
        return response_json['name']


    def getCardInfo(self,card_id):
        url = self.accessUrl.getURLForCard(card_id)
        header = self.accessHeaders.getHeaderForCard()

        response = requests.get(url, params=header)
        response_json = response.json()
        string = response_json['desc'].split('\n')
        project = string[0]
        subproject = string[1]
        time_estimate = string[2]
        string = response_json['name'].rsplit('-')
        description = string[0]
        work_time = string[1]
        due_date_and_time = response_json['due']
        match = re.search(r'\d{4}-\d{2}-\d{2}', due_date_and_time)
        due_date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()

        status = self.get_status_name(response_json['idList'])

        data = Data(project, subproject, description, time_estimate, due_date, status, work_time)
        return data


    def getAllCards(self):
        id = self.getBoardId()
        url = self.accessUrl.getURLForMakoCards(id)
        header = self.accessHeaders.getHeaderForMakoCards()

        response = requests.get(url, params=header)
        response_json = response.json()
        
        data_array = []
        for card in response_json:
            data_array.append(self.getCardInfo(card['id']))

        return data_array