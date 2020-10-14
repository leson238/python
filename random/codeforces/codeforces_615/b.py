t = int(input())
m = {'U': (0, 1),
     'R': (1, 0)}
for _ in range(t):
    n = int(input())
    p = []
    for i in range(n):
        p.append(tuple(map(int, input().split())))
    p.sort()
    res = []
    lp = (0, 0)
    while (len(p)):
        np = p.pop(0)
        if np[1] < lp[1]:
            print('NO')
            res = []
            break
        res.append('R'*(np[0] - lp[0]) + 'U' * (np[1] - lp[1]))
        lp = np
    if len(res):
        print("YES")
        print(''.join(res))
