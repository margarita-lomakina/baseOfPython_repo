class Cell:
    def __init__(self, cells_number):
        self.cells_number = cells_number

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        if self.cells_number > other.cells_number:
            return Cell(self.cells_number - other.cells_number)
        else:
            print('Subtraction prohibited')
            return None

    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)

    def __truediv__(self, other):
        return Cell(self.cells_number // other.cells_number)

    def make_order(self, line_length):
        n_rows = self.cells_number // line_length
        last_row = self.cells_number % line_length
        return (('*' * line_length + '\n') * n_rows) + '*' * last_row


cell_1 = Cell(18)
cell_2 = Cell(23)
cell_3 = cell_1 + cell_2
cell_4 = cell_3 - cell_2
cell_1 = cell_3 / cell_1
cell_2 = cell_1 * cell_4
print(cell_1.make_order(5), cell_1.cells_number, sep='\n', end='\n\n')
print(cell_2.make_order(5), cell_2.cells_number, sep='\n', end='\n\n')
print(cell_3.make_order(5), cell_3.cells_number, sep='\n', end='\n\n')
print(cell_4.make_order(5), cell_4.cells_number, sep='\n', end='\n\n')

cell_5 = cell_1 - cell_2

