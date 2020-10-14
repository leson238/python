t = int(input())
for _ in range(t):
    n, k1, k2 = map(int, input().split())
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    if max(p1) > max(p2):
        print('YES')
    else:
        print('NO')
