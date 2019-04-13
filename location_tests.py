import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("LA", -666, 420)
        self.assertEqual(repr(loc),"Location('LA', -666, 420)")
        loc = Location(1, 2, 3)
        self.assertEqual(repr(loc), "Location('1', 2, 3)") 

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("LA", -666, 420)
        self.assertNotEqual(loc, loc2)
        loc3 = loc
        self.assertEqual(loc, loc3)

if __name__ == "__main__":
        unittest.main()
