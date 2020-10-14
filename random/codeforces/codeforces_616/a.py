t = int(input())
odd = ['1', '3', '5', '7', '9']
for _ in range(t):
    n = int(input())
    s = list(input())
    x = [i for i in s if i in odd]
    if len(x) <= 1:
        print(-1)
    else:
        print(''.join(x[:2]))
