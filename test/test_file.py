import unittest
from test.task2_1 import GiveString


class TestStringMethods(unittest.TestCase):

    test = GiveString()
    testString = test.get_string()
    filterString = test.print_string()

    def test_upper(self):
      self.assertEqual(self.testString.upper(), self.filterString)


if __name__ == '__main__':
    unittest.main()