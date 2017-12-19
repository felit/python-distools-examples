import unittest
from example02 import hello

class MyTestCase(unittest.TestCase):
    def test_something(self):
        hello.world()
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
