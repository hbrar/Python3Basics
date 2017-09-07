import unittest
from fibonacci import fib

# class name can be arbitrary
class FibTest(unittest.TestCase):
    
    # name of these methods is arbitrary, but has to start with test
    def testCases(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)


if __name__ == "__main__":
    unittest.main()
    