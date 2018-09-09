import unittest

class TestIt(unittest.TestCase):

    def test_one(self):
        """1つ目のテストケース"""
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c,4)

    def test_two(self):
        """２つ目のテストケース"""
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c,3)
