def is_unique(word):
    s = set()
    for c in word:
        if c not in s:
            s.add(c)
        else:
            return False
    return True
# O(n) time
# O(n) space


print(is_unique("aaa"))
print(is_unique("abc"))
print(is_unique("  "))
