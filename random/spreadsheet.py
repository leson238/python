class Spreadsheet:
    def __init__(self, rows, columns):
        self.rows = rows 
        self.columns = columns
        self.sheet = []
        for row in range(rows):
            self.sheet.append([])
            for column in range(columns):
                self.sheet[row].append('|')
                if column == columns - 1:
                    self.sheet[row][column] = ''
    def update_cell(self, contents, row, column):
        if column == self.columns:
            self.sheet[row-1][column-1] = contents
        else:
            self.sheet[row-1][column-1] = str(contents) + '|'
        return self.sheet 
    def print_sheet(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.sheet[row][column], end='')
            print()
    #step 2:
    def extract_column(self, idx):
        col_val = []
        for row in range(self.rows):
            col_val.append(self.sheet[row][idx])
        return col_val
    def pretty_print(self):
        for column in range(self.columns):
            max_len = max([len(str(x)) for x in self.extract_column(column)])
        for row in range(self.rows):
            for column in range(self.columns):
                x = self.sheet[row][column]
                padding_spaces = (max_len - len(str(x))) * ' '
                x += padding_spaces
        self.print_sheet()
    def sum_formula(self, row1, col1, row2, col2):
        s = 0
        for row in range(row1-1, row2):
            for column in range(col1-1, col2):
                if self.sheet[row][column].isalpha():
                    pass 
                else:
                    s += self.sheet[row][column]
        print(s)
        return s
test = Spreadsheet(3,4)
test.update_cell('alice',2,1)
test.update_cell('bob',1,1)
test.update_cell(10,1,2)
test.update_cell(5,2,2)
test.print_sheet()
test.pretty_print()
# test.sum_formula(1,1,2,2)