import unittest

class TestCommunication(unittest.TestCase):
    
    def test_url_creation(self):
        parameters = ['key':'aaa', 'token':'bbb']
        url = generate_url('some/string', parameters)
        self.assertEqual(url, 'some/string?key=aaa&token=bbb')

