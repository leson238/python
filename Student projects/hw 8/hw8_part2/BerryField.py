class Direction:
    Directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1),
        'NE': (-1, 1),
        'NW': (-1, -1),
        'SE': (1, 1),
        'SW': (1, -1)
    }


class BerrySquare:
    def __init__(self, code):
        self.berries = 0
        self.bear = False
        self.tourist = False
        if isinstance(code, int):
            self.berries = code
        else:
            if code == 'B':
                self.bear = True
            else:
                self.tourist = True

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
    def __init__(self, grid):
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        self._convert()
        self.total_berries = self._total()

    def _convert(self):
        for i in range(self.h):
            for j in range(self.w):
                self.grid[i][j] = BerrySquare(self.grid[i][j])

    def _total(self):
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
                            if self.grid[i + d[0]][j + d[1]].berries == 0:
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
