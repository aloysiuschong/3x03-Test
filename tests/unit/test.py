import unittest
from main import *

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        pass
    
    def test_app(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_add(self):
        self.assertEqual(test_add(1,2), 3)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()