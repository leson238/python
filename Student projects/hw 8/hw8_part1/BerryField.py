class Direction:
    Directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (-1, -1),
        'NE': (-1, 1),
        'NW': (-1, -1),
        'SE': (1, 1),
        'SW': (1, -1)
    }


class BerryField:
    def __init__(self, grid):
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        self.total_berries = self._total()

    def _total(self):
        total = 0
        for i in range(self.h):
            for j in range(self.w):
                try:
                    total += self.grid[i][j]
                except IndexError:
                    pass
        return total

    def grow(self):
        for i in range(self.h):
            for j in range(self.w):
                if 1 <= self.grid[i][j] < 10:
                    self.grid[i][j] += 1

    def spread(self):
        ds = Direction.Directions
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == 10:
                    for key in ds:
                        d = ds[key]
                        try:
                            if self.grid[i + d[0]][j + d[1]] == 0:
                                self.grid[i + d[0]][j + d[1]] = 1
                        except IndexError:
                            pass

    def __str__(self):
        s = f'Field has {self.total_berries} berries.\n'
        for i in range(self.h):
            for j in range(self.w):
                s += f'{self.grid[i][j]:>4}'
            s += '\n'
        return s
