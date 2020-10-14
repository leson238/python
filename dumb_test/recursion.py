d = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}


def letterCombinations(digits):
    def helper(lst, n):
        if n == 0:
            return []
        if n == 1:
            return d[lst[0]]
        last_el = lst.pop()
        res = []
        for el in helper(lst, n - 1):
            for c in d[last_el]:
                res.append(el + c)
        return res
    digits = list(map(int, list(digits)))
    res = helper(digits, len(digits))
    return res


def letterCombinations2(digits):
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return d[int(digits)]
    digits = list(map(int, list(digits)))
    res = d[digits[0]]
    from collections import deque
    q = deque(digits)
    q.popleft()
    while q:
        key = q.popleft()
        temp_res = []
        for comb in res:
            for char in d[key]:
                temp_res.append(comb + char)
        res = temp_res
    return res


def generateParenthesis(n):
    if n == 0:
        return ['']
    res = []
    for c in range(n):
        for l in generateParenthesis(c):
            for r in generateParenthesis(n-1-c):
                print(c, l, r)
                print(f"({l}){r}")
                res.append(f"({l}){r}")
    return res


def word_search(board, word):
    def scan(pos, letter, board):
        h = len(board)
        w = len(board[0])
        res = []
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for d in dirs:
            x = pos[0] + d[0]
            y = pos[1] + d[1]
            if x < 0 or x > h - 1 or y < 0 or y > w - 1:
                continue
            if board[x][y] == letter:
                res.append((x, y))
        return set(res)
    h = len(board)
    w = len(board[0])
    from collections import deque
    first_letter = word[0]
    start_pos = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == first_letter:
                start_pos.append((i, j))
    for pos in start_pos:
        pos_q = deque()
        word_q = deque(list(word))
        word_q.popleft()
        used = set()
        pos_q.append(pos)
        while word_q:
            letter = word_q.popleft()
            print(letter)
            print(pos_q)
            for i in range(len(pos_q)):
                s_pos = pos_q.popleft()
                pos_list = scan(s_pos, letter, board)
                print(pos_list)
                # if not pos_list:
                #     used.remove(s_pos)
                for next_pos in pos_list:
                    if next_pos not in used:
                        pos_q.append(next_pos)
                if pos_list:
                    used.add(s_pos)
            if not pos_q:
                break
        # print(pos_q)
        if not word_q and pos_q:
            return True
    return False


print(word_search(
    [["A", "B", "C", "E"],
     ["S", "F", "E", "S"],
     ["A", "D", "E", "E"]],
    "ABCESEEEFS"))
