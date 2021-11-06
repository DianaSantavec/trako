from Url import *
from Headers import *
import requests

class Board(object):
    def __init__(self):
        pass
    
    def getAllBoards(self):
        accessUrl = Url()
        url = accessUrl.getURLForAllBoards()

        accessHeaders = Header()
        header = accessHeaders.getHeaderForBoards()

        response = requests.get(url, params=header)
        if (response.status_code == 404 or response.status_code == 401):
            return False
        elif (response.status_code == 200):
            return True
        # API returns only 404, 401 and 200 by documentation
        return False