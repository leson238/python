t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())
    if (a+b+c+n) % 3 == 0 and (((a+b+c+n) // 3) >= max(a, b, c)):
        print("YES")
    else:
        print("NO")
