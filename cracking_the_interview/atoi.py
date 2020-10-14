def myAtoi(st: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    valid_set = {'-', '+', '0', '1', '2',
                 '3', '4', '5', '6', '7', '8', '9'}
    number_map = {'0': 0, '1': 1, '2': 2, '3': 3,
                  '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    str_min = str(INT_MIN)
    str_max = str(INT_MAX)
    f, s = 0, 0
    while f < len(st):
        while st[f] == ' ':
            f += 1
            s += 1
        while f < len(st) and st[f] in valid_set:
            f += 1

    r = 0
    base = 0
    neg = False
    if st[s] == '-':
        neg = True
    if st[s] not in number_map:
        s += 1
    length = f-s+1
    if length > 10:
        if neg:
            return INT_MIN
        return INT_MAX
    elif length == 10:
        if neg:
            for i in range(s, f):
                if st[i] > str_min[i - s]:
                    return INT_MIN
        else:
            for i in range(s, f):
                if st[i] > str_max[i - s]:
                    return INT_MAX
    while f >= s:
        r += number_map[st[f-1]] * 10 ** base
        base += 1
        f -= 1
    if neg:
        return -r
    return r


myAtoi('42')
