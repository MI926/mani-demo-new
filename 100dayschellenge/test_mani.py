import unittest
from mani import print

class TestPrint(unittest.TestCase):

    def test_print_hello(self):
        self.assertEqual(print("hello"), None)
    
    def test_print_string(self):
        self.assertEqual(print("This is a test"), None)

    def test_print_number(self):
        self.assertEqual(print(123), None)
    
    def test_print_multiple_args(self):
        self.assertEqual(print("hello", 123, [1,2,3]), None)

if __name__ == '__main__':
    unittest.main()
