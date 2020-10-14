import unittest
import os

from utilities import col_name_check, index_check, task_name_check
from utilities import corrupt_child_check, circular_check, duplicate_check
from read_file import *


class MyTest(unittest.TestCase):

    def setUp(self):
        f = open('test.txt', 'w+')
        f.close()

    def test_utilities(self):
        self.assertFalse(col_name_check('word_id', 'id'))
        self.assertRaises(OverflowError, index_check, 100000)
        self.assertRaises(OverflowError, task_name_check, 'a' * 101)

        pair_list = [(0, 1), (1, 2)]
        self.assertRaises(KeyError, corrupt_child_check, (0, 0))
        self.assertRaises(KeyError, circular_check, (2, 1), pair_list)
        self.assertRaises(KeyError, duplicate_check, (1, 2), pair_list)

    def test_read_file_column(self):
        test_dict = {0: 1}
        with open('test.txt', 'w') as f:
            f.write('col1, col2, col3')
        self.assertRaises(ValueError, Orders.read_orders,
                          'test.txt', test_dict)
        self.assertRaises(ValueError, Dependencies.read_dependencies,
                          'test.txt', test_dict)

    def test_read_file_corrupt_input_amount(self):
        with open('test.txt', 'w') as f:
            f.write('col1, col2 \n')
            f.write('0, 1, 2')
        test_dict = {0: 1}
        self.assertRaises(ValueError, Orders.read_orders,
                          'test.txt', test_dict)
        self.assertRaises(ValueError, Dependencies.read_dependencies,
                          'test.txt', test_dict)

    def test_read_file_corrupt_type(self):
        with open('test.txt', 'w') as f:
            f.write('col1, col2 \n')
            f.write('a, 1')
        test_dict = {0: 1}
        self.assertRaises(ValueError, Orders.read_orders,
                          'test.txt', test_dict)
        self.assertRaises(ValueError, Dependencies.read_dependencies,
                          'test.txt', test_dict)

    def test_duplicate(self):
        with open('test.txt', 'w') as f:
            f.write('col1, col2 \n')
            f.write('0, 1')
        test_dict = {0: 1}
        self.assertRaises(KeyError, Orders.read_orders,
                          'test.txt', test_dict)
        self.assertRaises(KeyError, Dependencies.read_dependencies,
                          'test.txt', test_dict)

    def test_not_exists_dependencies(self):
        with open('test.txt', 'w') as f:
            f.write('id, child_id \n')
            f.write('1, 2')
        test_dict = {0: 1}
        self.assertRaises(KeyError, Dependencies.read_dependencies,
                          'test.txt', test_dict)

    def test_circular_dependencies(self):
        with open('test.txt', 'w') as f:
            f.write('id, child_id \n')
            f.write('1, 0')
        test_dict = {0: 1}
        self.assertRaises(KeyError, Dependencies.read_dependencies,
                          'test.txt', test_dict)

    def tearDown(self):
        os.remove('test.txt')


if __name__ == "__main__":
    unittest.main()
