class Constant:
    SIDE = 3
    CENTER = 6
    ARM = 2
    HEIGHT = 5


def draw():
    w = ((Constant.SIDE + 2) + Constant.ARM) * \
        2 + (Constant.CENTER + 2)
    h = (Constant.HEIGHT + 1) * 3
    board = [[" " for _ in range(w)] for _ in range(h)]
    # Upper arm
    for i in range(1, 1 + Constant.SIDE):
        board[0][i] = "x"
    for i in range((Constant.SIDE + 2) + Constant.ARM + 1, (Constant.SIDE + 2) + Constant.ARM + Constant.CENTER + 1):
        board[0][i] = "x"
    for i in range(1, 1 + Constant.HEIGHT):
        board[i][0] = "X"
        board[i][Constant.SIDE + 1] = "X"
        for j in range(1, Constant.SIDE + 1):
            board[i][j] = "-"
    for i in range(1, Constant.SIDE + 2 + Constant.ARM):
        board[Constant.HEIGHT + 1][i] = "x"
    # Lower arm
    for i in range(Constant.HEIGHT + 1 + 1, (Constant.HEIGHT + 1) * 2):
        board[i][(Constant.SIDE + 2) + Constant.ARM * 2 +
                 Constant.CENTER + 2] = "X"
        board[i][w - 1] = "X"
        for j in range((Constant.SIDE + 2) + Constant.ARM * 2 +
                       Constant.CENTER + 2 + 1, w - 1):
            board[i][j] = "-"
    for i in range((Constant.SIDE + 2) + Constant.ARM + (Constant.CENTER + 2) + Constant.ARM + 1, w - 1):
        board[Constant.HEIGHT + 1][i] = "x"
    for i in range((Constant.SIDE + 2) + Constant.ARM + (Constant.CENTER + 2), w):
        board[(Constant.HEIGHT + 1) * 2][i] = "x"
    # Trunk
    for i in range(1, h):
        board[i][Constant.SIDE + 2 + Constant.ARM] = "X"
        board[i][Constant.SIDE + 2 +
                 Constant.ARM + Constant.CENTER + 1] = "X"
    for i in range((Constant.SIDE + 2) + Constant.ARM + 1, (Constant.SIDE + 2) + Constant.ARM + 1 + Constant.CENTER):
        board[(Constant.HEIGHT + 1)][i] = "~"
        for j in range((Constant.HEIGHT + 1) * 2, h):
            board[j][i] = "~"
    s = (Constant.SIDE + 2) + Constant.ARM + 1
    e = s + Constant.CENTER
    for j in range(1, (Constant.HEIGHT + 1)):
        board[j][s:e] = ["-"] * Constant.CENTER
        board[j][s:s + j] = ["/"] * j
    k = 1
    for j in range((Constant.HEIGHT + 1) + 1, (Constant.HEIGHT + 1) * 2):
        board[j][s:e] = ["-"] * Constant.CENTER
        board[j][e - k:e] = ["\\"] * k
        k += 1
    return board


def board_print(board):
    h = len(board)
    w = len(board[0])
    for i in range(h):
        for j in range(w):
            print(board[i][j], end="")
        print()


board = draw()
board_print(board)
print("\n\n\n")
Constant.CENTER = 12
# Constant.HEIGHT = 12
# Constant.SIDE = 6
board = draw()
board_print(board)
