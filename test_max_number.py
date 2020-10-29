import unittest
from max_number import *

class TestFindMaxTestCase(unittest.TestCase):

    def test_max_number(self):
        assert find_max([99, 1, 50, 6]) == 99, "The max number should be 99"

    def test_descending(self):
        assert descending([2, 3, 1]) == [3, 2, 1], "In descending order the biggest number comes first"