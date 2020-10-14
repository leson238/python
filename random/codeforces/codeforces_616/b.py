t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    f = True
    k = 0
    if len(l) == 1 and 0 in l:
        print('No')
        continue
    for i in range(len(l)):
        if l[i] < i:
            k = i - 1
            break
    if k < len(l) - 2:
        for i in range(k+1, len(l)):
            if l[i] < abs(i + 1 - len(l)) or l[i] >= l[k]:
                f = False
                break
    if l[k] == 0:
        if 0 in l[k+1:]:
            f = False
    if f:
        print('Yes')
    else:
        print('No')
