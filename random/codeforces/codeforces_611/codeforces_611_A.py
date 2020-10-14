t = int(input())
for _ in range(t):
    h, m = map(int, input().split())
    r = 1440 - h * 60 - m
    print(r)
