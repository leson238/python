def multiple(x, n):
    l = bin(abs(n))[2:]
    length = len(l)
    result = 0
    for i in range(length):
        if l[i] != "0":
            result += (x << (length - 1) - i)
    if n < 0:
        result = -result
    return result


multiple(10, -5000)
