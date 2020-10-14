n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    r, g, b = sorted(l)
    if r + g >= b - 1:
        print("Yes")
    else:
        print("No")
