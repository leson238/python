from collections import Counter, OrderedDict
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())))
count_a = Counter(a)
count_b = Counter(b)
c_b = count_b.most_common(1)[0][1]
m_b = count_b.most_common(1)[0][0]
res = []
for d in count_a.most_common(n):
    if d[1] == c_b:
        m_a = d[0] % m
        res.append(m_b - m_a if m_b >= m_a else m_b + m - m_a)
    if d[1] < c_b:
        break
res = sorted(res)
for r in res:
    if sorted([(x + r) % m for x in a]) == b:
        print(r)
        break
