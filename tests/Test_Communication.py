import unittest
from src.Authentication import *

class TestCommunication(unittest.TestCase):
    
    def Test_Authentication(self):
        auth = Authentication('some_token')
        expectedAuth = {'key':'fcf13eab00317ac32b50020c2ff8ef81', 'token':'some_token'}
        self.assertEqual(auth.getAuthParameters(),expectedAuth)

    