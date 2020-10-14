from collections import defaultdict


def convert_to_canonical_form(st):
    i = 1
    res = ''
    char_canonical_map = defaultdict(int)
    for char in st:
        if char not in char_canonical_map:
            char_canonical_map[char] = i
            i += 1
    for char in st:
        res += (str(char_canonical_map[char]) + '-')
    return res


def find_set_isomorphic(lst):
    word_canonical_map = defaultdict(list)
    res = []
    for word in lst:
        canonical_form = convert_to_canonical_form(word)
        word_canonical_map[canonical_form].append(word)
    for canonical_form in word_canonical_map:
        res.append(word_canonical_map[canonical_form])
    return res


print(find_set_isomorphic(['leet', 'boot', 'baby', 'xaxy', 'abcd']))
print([[i for i in range(j, j+3)] for j in range(0, 20, 3)])
