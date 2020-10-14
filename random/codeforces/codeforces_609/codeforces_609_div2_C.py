n, k = map(int, input().split())
x = input()
r = 0
prefix = x[:k]
div = len(x) // k
remain = len(x) % k
s = '1'
while s < x:
    s = prefix*div + prefix[:remain]
    prefix = str(int(prefix)+1)
print(len(x))
print(int(s))
