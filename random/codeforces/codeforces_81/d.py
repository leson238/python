t = int(input())


def gcd(a, b):
    return gcd(b, a % b) if b > 0 else a


def countGCD(a, b, g):
    ans = 0
    for i in range(a, b+1):
        if (gcd(i, b) == g):
            print(i, b)
            ans = ans + 1
    return ans


for _ in range(t):
    a, m = map(int, input().split())
    g = gcd(a, m)
    print(countGCD(a, a + m - 1, g))
