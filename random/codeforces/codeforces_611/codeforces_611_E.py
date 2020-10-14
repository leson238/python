import math
n = int(input())
x = list(map(int, input().split()))
# saved to a dict
d = {}
for c in x:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

mx = 0
mn = 0
if len(d) == n:
    mx = n
    mn = math.ceil(n/2)
else:
    

print(mn, mx)
