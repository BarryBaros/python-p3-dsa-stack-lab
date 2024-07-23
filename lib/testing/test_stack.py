import unittest
from Stack import Stack

class TestStack(unittest.TestCase):

    def test_search(self):
        '''Test Stack search() method. How far is the element in the stack? '''
        stk = Stack([5, 6, 7, 8, 9, 10])

        # Test for element present in the stack
        self.assertEqual(stk.search(10), 1, "Element 10 should be at position 1 from the top")
        self.assertEqual(stk.search(9), 2, "Element 9 should be at position 2 from the top")
        self.assertEqual(stk.search(8), 3, "Element 8 should be at position 3 from the top")
        self.assertEqual(stk.search(7), 4, "Element 7 should be at position 4 from the top")
        self.assertEqual(stk.search(6), 5, "Element 6 should be at position 5 from the top")
        self.assertEqual(stk.search(5), 6, "Element 5 should be at position 6 from the top")

        # Test for element not present in the stack
        self.assertEqual(stk.search(1), -1, "Element 1 should not be found in the stack")
        self.assertEqual(stk.search(11), -1, "Element 11 should not be found in the stack")

if __name__ == '__main__':
    unittest.main()
