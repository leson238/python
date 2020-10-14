matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


class Hungarian:
    def __init__(self, square_matrix):
        self.matrix = square_matrix
        self.operating = self._copy_matrix()
        self.size = len(matrix)

    def _copy_matrix(self):
        return [row.copy() for row in self.matrix]

    def _check_complete(self):
        zero_row = []
        zero_col = []
        for row in self.operating:
            zero_row.append(row.count(0))
        for i in range(size):
            col = []
            for j in range(size):
                col.append(self.operating[j][i])
            zero_col.append(col.count(0))
        return all(x >= 1 for x in zero_row) and all(x >= 1 for x in zero_col)

    def result(self):
        if self._check_complete():

    def _step_one(self):
        m = self._copy_matrix()
        for row in m:
            m_cost = min(row)
            row = [x - m_cost for x in row]
        for i in range(size):
            col = []
            for j in range(size):
                col.append(m[j][i])
