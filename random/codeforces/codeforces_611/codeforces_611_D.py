
n, m = map(int, input().split())
# save starting position to a queue
q = list(map(int, input().split()))

res = []
ans = 0
d = {}
i = 0
# save pos: distance to a tree in map d
for p in q:
    d[p] = 0

# while the queue is not empty, take the first out and check
while len(q) != 0:
    # break if the result list have enough position for people
    if len(res) == m:
        break
    cur = q[i]
    i += 1
    # if the distance to a tree available, add it to the answer
    if d[cur] != 0:
        ans += d[cur]
        res.append(cur)
    # check pos adjacent to current pos
    if cur - 1 not in d:
        d[cur - 1] = d[cur] + 1
        q.append(cur - 1)
    if cur + 1 not in d:
        d[cur + 1] = d[cur] + 1
        q.append(cur + 1)


print(ans)
print(" ".join(map(str, res)))
