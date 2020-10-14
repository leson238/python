
from classes.Mark import Mark


def test_negative_mark():
    mark = Mark(1, 1, -1)
    assert mark.mark == 0


def test_over_100_mark():
    mark = Mark(1, 1, 200)
    assert mark.mark == 100
