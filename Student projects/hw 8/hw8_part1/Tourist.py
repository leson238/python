class Tourist:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.go_home = False
        self.turn_passed_no_bears = 0

    def should_run(self, field):
        total_bear = 0
        for i in range(max(0, self.row - 4), min(field.h, self.row + 4)):
            for j in range(max(0, self.col - 4), min(field.w, self.col + 4)):
                if field[i][j] == 'B':
                    total_bear += 1
        if total_bear == 0:
            self.turn_passed_no_bears += 1
        if total_bear >= 3 or self.turn_passed_no_bears:
            self.go_home = True

    def __str__(self):
        s = f'Tourist at ({self.row},{self.col}), {self.turn_passed_no_bears} turns without seeing a bear.'
        if self.go_home:
            s += ' - Left the Field'
        return s
