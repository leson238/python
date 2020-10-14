from sys import stdin, stdout

def count(lst):
    over = []
    under = []
    c = 0
    for pair in lst:
        if pair[0] - pair[1] < 0:
            over.append(pair[0] - pair[1])
        elif pair[0] - pair[1] > 0:
            under.append(pair[0] - pair[1])
    while len(over) > 0:
        last = over.pop()
        for i in under:
            if last + i == 0:
                c+=1
                under.remove(i)
    return c
    

lst = []
n = int(input())
for i in range(n):
  inp = stdin.readline().rstrip().split()
  lst.append([int(inp[0]), int(inp[1])])
c = count(lst)
stdout.write(str(c))
    

    
    