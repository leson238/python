from Bear import Direction


class Tourist:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.go_home = False
        self.disappear = False
        self.turn_passed_no_bears = 0

    def should_run(self, field):
        if field.grid[self.row][self.col].bear:
            self.disappear = True
            return
        total_bear = 0
        for i in range(max(0, self.row - 5), min(field.h, self.row + 5)):
            for j in range(max(0, self.col - 5), min(field.w, self.col + 5)):
                if field.grid[i][j].bear:
                    if ((i - self.row)**2 + (j - self.col)**2) <= 16:
                        total_bear += 1
        if total_bear == 0:
            self.turn_passed_no_bears += 1
        else:
            self.turn_passed_no_bears = 0
        if total_bear >= 3 or self.turn_passed_no_bears >= 3:
            self.go_home = True

    def __str__(self):
        s = f'Tourist at ({self.row},{self.col}), {self.turn_passed_no_bears} turns without seeing a bear.'
        if self.go_home or self.disappear:
            s += ' - Left the Field'
        return s
