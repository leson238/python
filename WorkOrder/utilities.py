"""
Collection of ultilities
"""
import sys


def col_name_check(col_name, desired_name):
    """
    Check if column name is correct according to the description
    """
    if col_name != desired_name:
        print(f'Warning: The column {col_name} should be {desired_name}')
        return False
    else:
        return True


def index_check(index, line_number=0):
    """
    Check if the index inside given range
    """
    if int(index) < 0 or int(index) > 10000:
        raise OverflowError(
            f'Out of bound error: Task index should be greater or equal zero and \
less than ten thousand. Please check orders.txt file at line {line_number}')
    return True


def task_name_check(task_name, line_number=0):
    """
    Check if task name length under 100
    """
    if len(task_name) > 100:
        raise OverflowError(
            f'Out of bound error: Task name should be less than 100 characters. \
Please check orders.txt file at line {line_number}')
    return True


def key_check(key, dictionary, line_number=0):
    """
    Check if a key not in a dictionary and custom handle error
    """
    if key not in dictionary.keys():
        raise KeyError(
            f'Corrupt relationship: There is no task with index {key}. \
Please check dependencies.txt file at line {line_number}')


def corrupt_child_check(pair, line_number=0):
    """
    A child cannot be the same with its parent
    """
    if pair[0] == pair[1]:
        raise KeyError(
            f'Corrupt relationship: Task with index {pair[0]} cannot be its own child. \
Please check dependencies.txt file at line {line_number}')


def circular_check(pair, pairs_list, line_number=0):
    """
    Check if a circular relationship exists (a -> b and b -> a)
    """
    if (pair[1], pair[0]) in pairs_list:
        raise KeyError(
            f'Corrupt relationship: Circular relation \
between task {pair[0]} and task {pair[1]}. \
Please check dependencies.txt file at line {line_number}')


def duplicate_check(pair, pairs_list, line_number=0):
    """
    Check if there is a duplicate
    """
    if pair in pairs_list:
        raise KeyError(
            f'Corrupt relationship: Duplicating relation \
between task {pair[0]} and task {pair[1]}. \
Please check dependencies.txt file at line {line_number}')


def _read_arg():
    if len(sys.argv) != 0:
        path = sys.argv.pop()
    else:
        raise Exception('Please type the command correctly: \
python main.py {path-to-orders-file} {path-to-dependencies-file} {path-to-output-file}')
    return path


def read_path(name):
    """
    Expect name of file: orders.txt, dependencies.txt or output.json
    """
    path = _read_arg()
    if name not in path:
        raise Exception(f'Expect file {name}')
    else:
        return path
