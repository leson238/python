"""
Input reading module
"""
from utilities import col_name_check, task_name_check, index_check
from utilities import key_check, circular_check, duplicate_check


class Orders:
    """
    Read orders.txt file
    """
    WORKS_DICT = {}

    @staticmethod
    def read_orders(path, works_dict):
        """
        Expect:
            path: orders.txt file path
        """
        with open(path) as file:
            try:
                col_1, col_2 = file.readline().strip().split(',')
                col_name_check(col_1, 'id')
                col_name_check(col_2, 'name')
            except ValueError:
                raise ValueError(f'Corrupting amount of columns')

            line_number = 1
            for line in file.readlines():
                line_number += 1
                try:
                    index, name = line.strip().split(',')
                    index_check(index, line_number=line_number)
                    task_name_check(name, line_number=line_number)
                    if int(index) not in works_dict:
                        works_dict[int(index)] = name
                    else:
                        raise KeyError(
                            f'Redefining work {index} at line {line_number}')
                except ValueError:
                    raise ValueError(
                        f'Corrupt input value, please check orders.txt file at line {line_number}')


class Dependencies:
    """
    Read dependencies.txt file
    """
    CHILDREN = []
    _PAIRS = set()
    RELATIONSHIP = {}

    @staticmethod
    def read_dependencies(path, works_dict):
        """
        Expect:
            path: dependencies.txt file path
            works_dict: works dictionary
        """
        with open(path) as file:
            try:
                col_1, col_2 = file.readline().strip().split(',')
                col_name_check(col_1, 'id')
                col_name_check(col_2, 'child_id')
            except ValueError:
                raise ValueError(f'Corrupt amount of columns')
            line_number = 1
            for line in file.readlines():
                line_number += 1
                try:
                    parent, child = map(int, line.strip().split(','))
                    key_check(parent, works_dict, line_number=line_number)
                    key_check(child, works_dict, line_number=line_number)
                    circular_check((parent, child),
                                   Dependencies._PAIRS, line_number=line_number)
                    duplicate_check((parent, child), Dependencies._PAIRS,
                                    line_number=line_number)
                    if parent not in Dependencies.RELATIONSHIP:
                        Dependencies.RELATIONSHIP[parent] = [child]
                    else:
                        Dependencies.RELATIONSHIP[parent].append(child)
                    Dependencies.CHILDREN.append(child)
                    Dependencies._PAIRS.add((parent, child))
                except ValueError:
                    raise ValueError(
                        f'Corrupt input value, \
                        please check dependencies.txt file at line {line_number}')
