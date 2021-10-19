'Tests for CustomMeta'

import unittest
from main import CustomMeta


class CustomClass(metaclass=CustomMeta):
    'Class for tests'
    x = 50

    def __init__(self, val=99):
        self.val = val

    @staticmethod
    def line():
        'Returns 100'
        return 100

    @staticmethod
    def useful_func():
        'Calms pylint down'
        return 200


class TestCustomMeta(unittest.TestCase):
    'Test custom meta methods'

    def test_class_creation(self):
        'Tests class creation'

        inst = CustomClass()
        inst.custom_x  # pylint: disable=pointless-statement, no-member
        inst.custom_val  # pylint: disable=pointless-statement, no-member
        inst.custom_line()  # pylint: disable=pointless-statement, no-member

        self.assertRaises(AttributeError, lambda: inst.x)
        self.assertRaises(AttributeError, lambda: inst.val)
        self.assertRaises(AttributeError, lambda: inst.line)


if __name__ == '__main__':
    unittest.main()
