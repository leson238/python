neighbor = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [4, 2]
}


def k_dialer(pos, n):
    """
    1 2 3
    4 5 6
    7 8 9
      0
    """

    if pos == 5:
        return 0
    from collections import deque
    q = deque()
    q.append(pos)
    l = len(q)
    for i in range(n):
        for j in range(l):
            f = q.popleft()
            for el in neighbor[f]:
                q.append(el)
            # print(q)
        l = len(q)
    return l


def k_dialer2(pos, n):
    prior_case = [1]*10
    curr_case = [0]*10
    curr_n = 1
    while curr_n <= n:
        curr_case = [0]*10
        curr_n += 1

        for p in range(10):
            for el in neighbor[p]:
                curr_case[p] += prior_case[el]
        print(prior_case)
        print(curr_case)
        prior_case = curr_case

    return curr_case[pos]


def repeatedString(s, n):
    ls = len(s)
    a_in_s = s.count('a')
    extra = s[:n % ls]
    print(extra)
    extra_a = extra.count('a')
    print(a_in_s)
    print(extra_a)
    print(n//ls)
    return a_in_s * (n//ls) + extra_a


def maxPairs(skillLevel, minDiff):
    # Write your code here
    skillLevel = sorted(skillLevel)
    pair = 0
    f = 0
    s = 0
    while f < len(skillLevel):
        if skillLevel[f] - skillLevel[s] < minDiff:
            f += 1
        else:
            print(f, s)
            pair += 1
            s += 1
    print(pair)
    return pair


def minimumSwaps(arr):
    # temp = [0] * (len(arr) + 1)
    # for pos, val in enumerate(arr):
    #     temp[val] = pos
    #     # pos += 1
    swaps = 0
    pos = {}
    for i, el in enumerate(arr):
        pos[el] = i
    for i in range(len(arr)):
        if arr[i] != i + 1:
            swaps += 1
            val = arr[i]
            # swap pos i with position of value i + 1 take from dict
            arr[i], arr[pos[i + 1]] = arr[pos[i + 1]], arr[i]
            # update position of value to postion of i + 1
            pos[val] = pos[i + 1]
    return swaps


def arrayManipulation(n, queries):
    from collections import Counter
    c = Counter()
    for a, b, k in queries:
        c[a] += k
        c[b+1] -= k
        print(c)
    arrSum = 0
    maxSum = 0
    # c= sorted(c)[:-1]
    print(c)
    for i in sorted(c)[:-1]:
        print(i)
        arrSum += c[i]
        maxSum = max(maxSum, arrSum)
    return maxSum


def find_max(lst):
    l = 0
    r = len(lst) - 1
    while l <= r:
        m = (l+r) // 2
        if lst[m] > lst[m+1] or m == len(lst) - 1:
            return lst[m]
        print(lst[m])
        if lst[m] >= lst[l]:
            l = m + 1
        else:
            r = m - 1


def two_ways_2sum(a, b):
    sum_map = set()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            s = a[i] + a[j]
            sum_map.add(s)
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            s = b[i] + b[j]
            if s in sum_map:
                return True
    return False


print(find_max([2, 3, 4, 5, 6, 7, 8, 9, 1]))
