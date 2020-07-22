import unittest
from src.pub import Pub 

# new class
class TestPub(unittest.TestCase):
    
    def setUp(self):
        pub = Pub('Prancing Pony', 100.00)

    # test functions
    def test_pub_has_name(self):
        name = self.pub.name 
        self.assertEqual('Prancing Pony', name)