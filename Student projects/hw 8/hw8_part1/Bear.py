from BerryField import Direction


class Bear:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.is_asleep = False
        self.asleep_turn = 0
        self._berries_ate = 0
        self._should_wake()

    def walk(self, things_meet):
        d = Direction.Directions
        self.row = self.row + d[self.direction][0]
        self.col = self.col + d[self.direction][1]
        if type(things_meet) == int:
            self._berries_ate += things_meet
        elif type(things_meet) == str:
            if things_meet == 'T':
                self.is_asleep = True
                self.asleep_turn = 3

    def _should_wake(self):
        if self.asleep_turn == 0:
            self.is_asleep = False

    def __str__(self):
        s = f'Bear at ({self.row},{self.col}) moving {self.direction}'
        return s
