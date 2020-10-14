import sys


def max_2_power(n):
    s = bin(n)[2:]
    length = len(s)
    if n < 2**length:
        return length - 1
    return length


sys.stdin.readline()
for line in sys.stdin:
    try:
        n = int(line.strip('\n'))
        s1 = n * (n + 1) // 2
        n2 = max_2_power(n)
        s2 = 2**(n2 + 1) - 1
        r = s1 - 2 * s2
        sys.stdout.write(str(r) + '\n')
    except ValueError:
        break
