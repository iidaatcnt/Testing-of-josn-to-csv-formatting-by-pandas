import unittest

import pandas as pd

class SampleTest(unittest.TestCase):
    """
    $ python -m unittest test_sample.py
    """

    def test_str(self):
        a = 'Hello world'
        b = 'Hello world'
        self.assertEqual(a, b)

    def test_list(self):
        a = ['pen', 'apple', 'pineapple']
        b = ['pen', 'apple', 'pineapple']
        self.assertListEqual(a, b)

    # @unittest.skip('skip!')
    def test_tuple(self):
        a = ('name', 'Taro', 'age', 26)
        b = ('name', 'Taro', 'age', 26)
        self.assertTupleEqual(a, b)

    def test_CountEqual(self):
        a = ('name', 'Taro', 'age', 26)
        b = (26, 'Taro', 'age', 'name')
        self.assertCountEqual(a, b)

    def test_CountEqual(self):
        a = ('name', 'Taro', 'age', 26)
        b = (26, 'Taro', 'age', 'name')
        self.assertCountEqual(a, b)

    @unittest.skip('skip!')
    def test_df(self):
        df = pd.DataFrame({'age': [24, 42], 'state': ['NY', 'CA'], 'point': [64, 92]})