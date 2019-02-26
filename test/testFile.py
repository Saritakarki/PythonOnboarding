import unittest
from test.task2_1 import GiveString


class TestStringMethods(unittest.TestCase):

    test = GiveString()
    testString = test.get_string()

    def test_upper(self):
      self.assertEqual(self.testString.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()