t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = n//k
    r = min(n, (a+1)*(k//2) + a*(k-k//2))
    print(r)
