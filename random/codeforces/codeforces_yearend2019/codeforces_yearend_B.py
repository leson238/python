t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    r = 'NO'
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) >= 2:
            r = 'YES'
            print(r)
            print(i + 1, i + 2)
            break
    if r == 'NO':
        print(r)
