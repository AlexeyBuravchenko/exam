import unittest
from exam import calc

class MyTestCase(unittest.TestCase):
    test = calc(1,3)
    def test_something(self):
        self.assertEqual(self.test,4)


if __name__ == '__main__':
    unittest.main()
