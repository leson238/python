import sys
path = sys.path[0] + '\\aoc_2019_day10.txt'
ast_map = []
with open(path, 'r') as f:
    raw_map = f.readlines()
    for row in raw_map:
        ast_map.append(list(row.strip('\n')))
# print(ast_map)
width = len(ast_map[0])
height = len(ast_map)
def lighting_map(m):
    return [[' ']*len(m[0]) for i in range(len(m))]

def linear_check(x1,y1,x2,y2):
    a = abs(y2-y1)/abs(x2-x1)
    b = y1 - a*x1 
    

def scan_ast(x,y):
    for i in range(width):
        for j in range(height):
            if ast_map[i][j] == '#':

