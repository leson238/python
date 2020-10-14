from itertools import combinations
t = int(input())
for i in range(0, t*2, 2):
    j = 1
    m = 0
    n, s = map(int, input().split())
    verse = list(map(int, input().split()))
    if sum(verse) <= s:
        print(0)
    else:
        sub_arr = verse[:j]
        while j < len(verse):
            m += verse[j]
            j += 1
        if m - max(sub_arr) + verse[j+1] + verse[j+2] <= s:
            print(sub_arr.index(max(sub_arr) + 1))
        else:
            print(j + 1)
