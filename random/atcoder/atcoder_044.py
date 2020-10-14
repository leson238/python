# n = int(input())
# k = int(input())
# x = int(input())
# y = int(input())
# r = 0
# if k >= n:
#     r = n * x
# else:
#     r = (n - k) * y + k * x
# print(r)

# problem B
# from string import ascii_lowercase
# s = input()
# r = 'Yes'
# for l in ascii_lowercase:
#     if s.count(l) % 2 == 1:
#         r = 'No'
#         break
# print(r)

# problem C
# from itertools import combinations
# n, a = map(int, input().split())
# l = list(map(int, input().split()))
# c = 0
# for r in range(1, n+1):
#     temp = list(combinations(l, r))
#     for item in temp:
#         if sum(item)/len(item) == a:
#             c += 1
# print(c)

# problem D

import math


def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n // b) + n % b


n = int(input())
s = int(input())


def find_b(n, s):
    if n == s:
        return 1
    p = int(math.sqrt(n))
    i = 2
    while i < (n-s)/p + 1:
        if f(i, n) == s:
            return i
        i += 1
    while p > 1:
        b = int((n-s)/p + 1)
        if f(b, n) == s:
            return b
        p -= 1
    return -1


print(find_b(n, s))
