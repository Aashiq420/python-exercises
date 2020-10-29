import unittest
from mathematics import *

class TestMathematicsTestCase(unittest.TestCase):

    def test_add(self):
        assert add(2,2) == 4, "2 plus 2 should equal 4"

    def test_subtract(self):
        assert subtract(5,3) == 2, "5 minus 3 should equal 2"

    def test_multiply(self):
        assert multiply(3,4) == 12, "3 times 4 should equal 12"

    def test_divide(self):
        assert divide(10,5) == 2, "10 divided by 5 should equal 2"
