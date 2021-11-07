import unittest
from src.Authentication import *
from src.Url import *
from src.Headers import *

class TestCommunication(unittest.TestCase):
    
    def test_Authentication(self):
        auth = Authentication('some_token')
        expectedAuth = {'key':'fcf13eab00317ac32b50020c2ff8ef81', 'token':'some_token'}
        self.assertEqual(auth.getAuthParameters(),expectedAuth)

    def test_GetBoardUrl(self):
        auth = Authentication('some_token')
        url = Url()
        self.assertEqual(url.getURLForBoards(), 'https://api.trello.com/1/boards/mako-today-board')

    def test_GetBoardHeader(self):
        auth = Authentication('some_token')
        header = Header()
        header.getHeaderForBoards(auth)
        expected_header = {'key':'fcf13eab00317ac32b50020c2ff8ef81', 'token':'some_token', 'Accept': 'application/json'}
