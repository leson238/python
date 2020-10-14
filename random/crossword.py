# place first word horizontally
# try to place next word horizontally/vertically
# check for adjacencies
# check for grid's boundaries

def copy_matrix(matrix):
    return [matrix[i].copy() for i in range(len(matrix))]


def place_horizontally(word, matrix, p, i, j, accept_list):
    new_matrix = copy_matrix(matrix)
    start = j - p
    end = start + len(word)
    if end > len(matrix) or start < 0:
        print('Reaches outside grid')
        return (False, matrix)
    for c in word:
        cursor = j - p
        new_matrix[i][cursor] = c 
        j += 1
    if not check_for_problems(new_matrix, accept_list):
        print('Illegal adjacencies horizontal')
        return (False, matrix)
    else:      
        return (True, new_matrix)


def place_vertically(word, matrix, p, i, j, accept_list):
    new_matrix = copy_matrix(matrix)
    start = i - p
    end = start + len(word)
    if end > len(matrix) or start < 0:
        print('Reaches outside grid')
        return (False, matrix)
    for c in word:
        cursor = i - p
        new_matrix[cursor][j] = c 
        i += 1
    if not check_for_problems(new_matrix, accept_list):
        print('Illegal adjacencies vertical')
        return (False, matrix)
    else:
        return (True, new_matrix)


def string_preprocess(s, separator, accept_list):
    words = s.strip(separator)
    if len(words) > 0:
        word_list = words.split(separator)
        for word in word_list:
            if len(word) > 1 and word not in accept_list:
                return True


def check_for_problems(matrix, accept_list):
    current_word = ''      
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            current_word += matrix[j][i]
        if string_preprocess(current_word, ' ', accept_list):
            return False
        current_word = ''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            current_word += matrix[i][j]
        if string_preprocess(current_word, ' ', accept_list):
            return False
        current_word = ''
    return True


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(' '.join(str(el) for el in matrix[i]))


def crossword(words, start_row):
    matrix_size = 20
    separator = ' '
    matrix = [[separator]*matrix_size for i in range(matrix_size)]
    acceptable_words = []
    if len(words) > 0:
        # place first word horizontally in middle of the matrix
        first_word = words.pop(0)
        acceptable_words.append(first_word)
        start = (matrix_size - len(first_word)) // 2
        matrix_tuple = place_horizontally(first_word, matrix, 0, start_row, start, acceptable_words) 
        matrix = matrix_tuple[1]
        while len(words) > 0:
            should_stop = False
            next_word = words.pop(0)
            acceptable_words.append(next_word)
            for p in range(len(next_word)):
                for i in range(matrix_size):
                    for j in range(matrix_size):
                        if next_word[p] == matrix[i][j]:
                            matrix_tuple = place_vertically(next_word, matrix, p, i, j, acceptable_words)
                            if matrix_tuple[0]: 
                                matrix = matrix_tuple[1]
                                should_stop = True
                            else:
                                matrix_tuple = place_horizontally(next_word, matrix, p, i, j, acceptable_words)
                                matrix = matrix_tuple[1]
                                if matrix_tuple[0]:
                                    should_stop = True
                        if should_stop:
                            break
    return matrix


result = crossword(['addle', 'apple', 'clowning', 'incline', 'plan', 'burr', 'loon'], 9)
result2 = crossword(["abcdefghijklmnopqrst",
               "fffffggg",
               "ttttttttttuuuuuuuuuz",
               "yzzz",
               "qqqqqqqqqqqqqqy",
               "xxxxxxxxxaaaaaaa",
               "aaaaggg",
               "xxwwww",
               "wwwwvvvvve",
               "vvvvvvvvvvvvq",
               "mat",
               "mat",
               "make",
               "make",
               "maker",
               "remake",
               "hat",
               ], 8)
# print_matrix(result)
# print_matrix(result2)

with open('output.txt','w+') as f:
    for i in range(len(result)):
        f.write('  '.join(str(el) for el in result[i]) + '\n')
    f.write('\n\n\n')
    for i in range(len(result2)):
        f.write('  '.join(str(el) for el in result2[i]) + '\n')