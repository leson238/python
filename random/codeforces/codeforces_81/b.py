t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = input()
    cur = 0
    r = 0
    l = [0] * (n+1)
    for i in range(n):
        if s[i] == '0':
            l[i] = l[i-1] + 1
        else:
            l[i+1] = l[i-1] - 1
    if cur == x:
        r += 1
    while abs(cur) <= abs(x + max_diff + min_diff):
        for e in l[1:]:
            cur += e
            # print(cur)
            if cur == x:
                r += 1
        if r > n:
            r = -1
            break
    print(r)
