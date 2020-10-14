# problem A
# n = int(input())
# r = n*(n+1)//2
# print(r)

# problem B
# s = input()
# l = list(s)
# i = 0
# r = []
# while i < len(l):
#     if len(r) == 0:
#         if s[i] == 'B':
#             pass
#         else:
#             r.append(s[i])
#     else:
#         if s[i] == 'B':
#             r.pop()
#         else:
#             r.append(s[i])
#     i += 1
# print(''.join(r))

# problem C
# n = int(input())
# s = list(map(int, input().split()))
# total = sum(s)
# lower_mean = total // n
# upper_mean = total // n + 1
# r1 = sum([(x-lower_mean) ** 2 for x in s])
# r2 = sum([(x-upper_mean) ** 2 for x in s])
# r = min(r1, r2)
# print(r)

# problem D
s = input()


def unbalanced(st):
    for c in st:
        if st.count(c) > (len(st) // 2):
            return True
    return False


def test_str(st):
    r = (-1, -1)
    for j in range(1, 3):
        for i in range(len(s) - j):
            if unbalanced(s[i:i+j+1]):
                r = (i+1, i+j+1)
                return r
    return r


print(test_str(s)[0], test_str(s)[1])
