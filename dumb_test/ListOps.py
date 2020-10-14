def check_integer(f):
    def wrapper(*args, **kwargs):
        from numbers import Number
        if not isinstance(args[1], Number):
            raise TypeError(f"Factor {args[1]} must be a numeric type")
        return f(*args, **kwargs)
    return wrapper


class ListOps:
    """
    This custom list can do numeric operation on all of its element through naive operator
    """

    def __init__(self, lst=[]):
        from collections.abc import Iterable
        if not isinstance(lst, Iterable):
            raise TypeError(f"{lst} is not iterable")
        self.lst = lst

    def append(self, obj):
        """
        Add item to list
        """
        self.lst.append(obj)

    def pop(self):
        """
        Pop last item from list
        """
        self.lst.pop()

    def __getitem__(self, key):
        size = len(lst)
        if not isinstance(key, int):
            raise ValueError("Index must be integer")
        if key < -size or key >= size:
            raise IndexError("Index out of range")
        return self.lst[key]

    @check_integer
    def __add__(self, factor):
        return [x + factor for x in self.lst]

    @check_integer
    def __sub__(self, factor):
        return [x - factor for x in self.lst]

    @check_integer
    def __mul__(self, factor):
        return [x * factor for x in self.lst]

    @check_integer
    def __truediv__(self, factor):
        return [x / factor for x in self.lst]

    @check_integer
    def __floordiv__(self, factor):
        return [x // factor for x in self.lst]

    def __str__(self):
        return str(self.lst)
