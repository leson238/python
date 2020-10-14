t = int(input())
for _ in range(t):
    n = int(input())
    if n < 2*3*4:
        print("NO")
    else:
        r = []
        i = 2
        j = 3
        while j > 1:
            l = len(r)
            for k in range(i, int(n**(1/j) + 2)):
                if n % k == 0:
                    r.append(k)
                    n //= k
                    i = k + 1
                    j -= 1
                    break
            if len(r) == l or len(r) == 2:
                break
        if len(r) == 2 and n > int(r[-1]):
            r.append(n)
            print('YES')
            print(' '.join(map(str, r)))
        else:
            print('NO')
