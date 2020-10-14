n = int(input())
l = list(map(int, input().split()))
s1 = set(l)
s2 = set(range(1, n+1))
fill = list(s2-s1)


def gen_list(a, b):
    i = 0
    while i < len(a):
        if b[i] == a[i]:
            if i < len(a)-1:
                b[i], b[i+1] = b[i+1], b[i]
            else:
                b[0], b[i] = b[i], b[0]
            i -= 1
        i += 1
    return b


# print(gen_list([1, 2, 3, 4, 5, 6, 7]))
a = []
for i in range(n):
    if l[i] == 0:
        a.append(i+1)

b = gen_list(a, fill)
j = 0
for i in range(n):
    if l[i] == 0:
        l[i] = b[j]
        j += 1
    print(l[i], end=' ')
