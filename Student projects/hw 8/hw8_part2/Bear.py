from BerryField import Direction


class Bear:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.is_asleep = False
        self.asleep_turn = 0
        self._berries_ate = 0
        self.out_of_map = False
        self._should_wake()

    def walk(self, field):
        d = Direction.Directions
        field.grid[self.row][self.col].bear = False
        while True:
            if self.is_asleep:
                self.asleep_turn -= 1
                self._should_wake()
                break
            square = field.grid[self.row][self.col]
            if square.tourist:
                self.is_asleep = True
                self.asleep_turn = 2
                square.tourist = False
                square.bear = True
                return (self.row, self.col)
            self._berries_ate += square.berries
            square.berries = 0 if self._berries_ate < 30 else self._berries_ate - 30
            if self._berries_ate >= 30:
                break
            else:
                self.row = self.row + d[self.direction][0]
                self.col = self.col + d[self.direction][1]
            if self.run_out(field):
                self.out_of_map = True
                break
        if not self.out_of_map:
            field.grid[self.row][self.col].bear = True
            self._berries_ate = 0

    def run_out(self, field):
        return (self.row < 0 or self.row >= field.h or self.col < 0 or self.col >= field.w)

    def _should_wake(self):
        if self.asleep_turn == 0:
            self.is_asleep = False

    def __str__(self):
        s = f'Bear at ({self.row},{self.col}) moving {self.direction}'
        if self.is_asleep:
            s += f' - Asleep for {self.asleep_turn} more turns'
        if self.out_of_map:
            s += f' - Left the field'
        return s
