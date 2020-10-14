from Bear import Bear, Direction
from Tourist import Tourist


class BerrySquare:
    def __init__(self, berries, bear=None, tourist=None):
        self.berries = berries
        self.bear = bear
        self.tourist = tourist

    def grow(self):
        if 1 <= self.berries < 10:
            self.berries += 1

    def __str__(self):
        if self.bear and self.tourist:
            return 'X'
        if self.bear:
            return 'B'
        if self.tourist:
            return 'T'
        return str(self.berries)


class BerryField:
    def __init__(self, grid, bear_list, tourist_list):
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        self.convert(bear_list, tourist_list)
        self.total_berries = self.total()

    def convert(self, bear_list, tourist_list):
        for i in range(self.h):
            for j in range(self.w):
                self.grid[i][j] = BerrySquare(self.grid[i][j])
        for b in bear_list:
            row, col, d = b[0], b[1], b[2]
            self.grid[row][col].bear = Bear(b[0], b[1], b[2])
        for t in tourist_list:
            row, col = t[0], t[1]
            self.grid[row][col].tourist = Tourist(t[0], t[1])

    def total(self):
        total = 0
        for i in range(self.h):
            for j in range(self.w):
                total += self.grid[i][j].berries
        return total

    def grow(self):
        for i in range(self.h):
            for j in range(self.w):
                self.grid[i][j].grow()

    def spread(self):
        ds = Direction.Directions
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j].berries == 10:
                    for key in ds:
                        d = ds[key]
                        try:
                            if self.grid[i + d[0]][j + d[1]].berries == 0 and i + d[0] >= 0 and j + d[1] >= 0:
                                self.grid[i + d[0]][j + d[1]].berries = 1
                        except IndexError:
                            pass

    def __str__(self):
        s = f'Field has {self.total_berries} berries.\n'
        for i in range(self.h):
            for j in range(self.w):
                s += f'{self.grid[i][j].__str__():>4}'
            s += '\n'
        return s
