"""
Convert simple txt to a meaningful JSON works order file.
"""

import json
import queue

from read_file import Orders, Dependencies
from utilities import read_path

Q = queue.Queue(0)


# Set up input

OUTPUT_PATH = read_path('output.json')
DEPENDENCIES_PATH = read_path('dependencies.txt')
ORDERS_PATH = read_path('orders.txt')

Orders.read_orders(ORDERS_PATH, Orders.WORKS_DICT)
WORKS_DICT = Orders.WORKS_DICT

Dependencies.read_dependencies(DEPENDENCIES_PATH, WORKS_DICT)
CHILDREN = Dependencies.CHILDREN
RELATIONSHIP = Dependencies.RELATIONSHIP


class Work:
    """
    Work base data structure
    """

    def __init__(self, index):
        self._add_id(index)
        self.name = WORKS_DICT[self.id]
        self.dependencies = []

    def _add_id(self, index):
        try:
            self.id = int(index)
        except (ValueError, TypeError):
            raise Exception('Corrupt index input')


class WorkOrder:
    """
    Works hierarchy
    """

    def __init__(self, works_dict, children, rls_dict):
        self._add_orders(works_dict, children)
        self.add_dependencies(rls_dict)

    def _add_orders(self, works_dict, children):
        """
        Look up roots in pre-fill dict.
        """
        self.orders = []
        for index in works_dict:
            if index not in children:
                self.orders.append(Work(index))
        if self.orders == []:
            raise ValueError(
                'Corrupting input: There is no independent task could be completed first.')

    def add_dependencies(self, rls_dict):
        """
        Add multiple roots, each root expands to multiple children - keep track of them using queue.
        """
        for root in self.orders:
            Q.put(root)
        while not Q.empty():
            curr_work = Q.get()
            idx = curr_work.id
            if idx in rls_dict:
                for index in rls_dict[curr_work.id]:
                    curr_work.dependencies.append(Work(index))
            for new_item in curr_work.dependencies:
                Q.put(new_item)

    def to_json(self):
        """
        Convert the object to JSON format
        """
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=2)


if __name__ == "__main__":
    FILE = open(OUTPUT_PATH, 'w+')
    FILE.write(WorkOrder(WORKS_DICT, CHILDREN, RELATIONSHIP).to_json())
    FILE.close()
