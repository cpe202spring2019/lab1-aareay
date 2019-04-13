import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        "Max_list_iter tests"
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1, 2, 3]), 3)
        self.assertEqual(max_list_iter([1, 1]), 1)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([1, 2, -4, -5, 9]), 9)
        self.assertEqual(max_list_iter([-12321, -123, -1]), -1)
        self.assertEqual(max_list_iter([1, 0, -1]), 1)

    def test_reverse_rec(self):
        var = None
        with self.assertRaises(ValueError):
            max_list_iter(var)
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec( [1, 2, 3, 4, 5]), [5, 4, 3, 2, 1] )
        self.assertEqual(reverse_rec( [1]), [1])
        self.assertEqual(reverse_rec( [1, 4, 5, 123]), [123, 5, 4, 1])
        

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

        list_val = [0, 1, 4, 7, 12, 13, 13, 16]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(7, low, high, list_val), 3)
        
        with self.assertRaises(ValueError):
            bin_search(7, low, high, None)
        self.assertEqual(bin_search(144, low, high, list_val), None)

if __name__ == "__main__":
        unittest.main()

    
