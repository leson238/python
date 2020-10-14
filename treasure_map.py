from collections import deque
KEY = "3"
TREASURE = "4"


def find_dest(M, start, dest):
    q = deque()
    q.append(start)
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    steps = 0
    visited = set()
    visited.add(start)
    while q:
        for i in range(len(q)):
            node = q.popleft()
            x, y = node[0], node[1]
            if M[x][y] == dest:
                return {'steps': steps, "key": (x, y)}
            for dir in dirs:
                newX, newY = x+dir[0], y+dir[1]
                # check bounds:
                if newX >= 0 and newX <= len(M)-1 and newY >= 0 and newY <= len(M[0])-1:
                    # check cell:
                    if M[newX][newY] != '2':
                        # check if visited:
                        if (newX, newY) not in visited:
                            q.append((newX, newY))
                            visited.add((newX, newY))
        steps += 1
    return {'steps': steps, "key": (x, y)}


m = [["0", "1", "3"], ["1", "1", "4"], ["1", "3", "4"]]


def left(M, dest):
    for row in M:
        if dest in row:
            return True
    return False


r = []
r2 = {}
min_sum = 10**10
while left(m, KEY):
    s = (0, 0)
    info = find_dest(m, s, KEY)
    steps, key = info["steps"], info["key"]
    m[key[0]][key[1]] = '1'
    r.append(steps)
    m_copy = [row.copy() for row in m]
    r2[key] = []
    while left(m_copy, TREASURE):
        s = key
        info2 = find_dest(m, s, TREASURE)
        steps2 += info['steps']
        key2 = info['key']
        m[key2[0]][key2[1]] = '1'
        r2['distance'].append(steps)
    if sum(r2[key]) < min_sum:
        min_sum = sum(r2[key])

print(max(r))
