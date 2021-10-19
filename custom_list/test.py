'Tests for CustomList'

import unittest
from main import CustomList


class TestCustomList(unittest.TestCase):
    'Test custom list methods'

    def test_same_type_add(self):
        'Test same type addition'
        left = CustomList([5, 1, 3, 7])
        right = CustomList([1, 2, 7])
        self.assertIsInstance(left + right, CustomList)
        self.assertTrue(list.__eq__(left + right, [6, 3, 10, 7]))
        self.assertIsInstance(right + left, CustomList)
        self.assertTrue(list.__eq__(right + left, [6, 3, 10, 7]))

    def test_same_type_sub(self):
        'Test same type subtraction'
        left = CustomList([5, 1, 3, 7])
        right = CustomList([1, 2, 7])
        self.assertIsInstance(left - right, CustomList)
        self.assertTrue(list.__eq__(left - right, [4, -1, -4, 7]))
        self.assertIsInstance(right - left, CustomList)
        self.assertTrue(list.__eq__(right - left, [-4, 1, 4, -7]))

    def test_list_add(self):
        'Test built-in list addition'
        left = CustomList([5, 1, 3, 7])
        right = [1, 2, 7]
        self.assertIsInstance(left + right, CustomList)
        self.assertTrue(list.__eq__(left + right, [6, 3, 10, 7]))
        self.assertIsInstance(right + left, CustomList)
        self.assertTrue(list.__eq__(right + left, [6, 3, 10, 7]))

    def test_list_sub(self):
        'Test built-in list subtraction'
        left = CustomList([5, 1, 3, 7])
        right = [1, 2, 7]
        self.assertIsInstance(left - right, CustomList)
        self.assertTrue(list.__eq__(left - right, [4, -1, -4, 7]))
        self.assertIsInstance(right - left, CustomList)
        self.assertTrue(list.__eq__(right - left, [-4, 1, 4, -7]))

    def test_same_type_comparison(self):
        'Test same type comparison'
        left = CustomList([0, 10])
        right = CustomList([1, 2, 3])
        self.assertTrue(left > right)
        self.assertTrue(right < left)
        self.assertTrue(left >= right)
        self.assertTrue(right <= left)
        self.assertTrue(left != right)
        right = CustomList([1, 2, 3, 4])
        self.assertTrue(left == right)
        self.assertTrue(left <= right)
        self.assertTrue(left >= right)

    def test_list_comparison(self):
        'Test built-in list comparison'
        left = [0, 10]
        right = CustomList([1, 2, 3])
        self.assertTrue(left > right)
        self.assertFalse(left < right)
        self.assertTrue(left >= right)
        self.assertFalse(left <= right)
        self.assertTrue(left != right)
        right = CustomList([1, 2, 3, 4])
        self.assertTrue(left == right)
        self.assertTrue(left <= right)
        self.assertTrue(left >= right)


if __name__ == '__main__':
    unittest.main()
