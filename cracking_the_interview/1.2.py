def is_permutation(origin, new):
    d = {}
    for c in origin:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in new:
        if c not in d:
            return False
        if d[c] > 0:
            d[c] -= 1
        else:
            return False
    for k in d:
        if d[k] > 0:
            return False
    return True

# time O(n)
# space O(n)


print(is_permutation("aab", "baa"))
print(is_permutation("abc", "abd"))
