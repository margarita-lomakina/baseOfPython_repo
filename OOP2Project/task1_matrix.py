class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.check_matrix()

    def __str__(self):
        str_matrix = f''
        for line in self.matrix:
            for el in line:
                str_matrix = str_matrix + f'{str(el):5}'
            str_matrix += f'\n'
        return str_matrix

    def check_matrix(self):
        lengths = list(map(len, self))
        if not min(lengths) == max(lengths):
            raise ValueError('Матрица должна быть прямоугольной')

    @property
    def size(self):
        return len(self.matrix[0]), len(self.matrix)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        b = self.i
        self.i += 1
        if b < len(self.matrix):
            return self.matrix[b]
        raise StopIteration

    def __add__(self, other):
        sum_matrix =[]
        if self.size == other.size:
            for line in zip(self, other):
                sum_matrix.append(list(map((lambda x: x[0] + x[1]), zip(line[0], line[1]))))
            return Matrix(sum_matrix)
        print('Not similar size of matrix')
        return Matrix([])


mx1 = Matrix([[1, 234], [80, 5]])
mx2 = Matrix([[1, 2], [2, 3]])
print(mx1 + mx2)
print(mx1.size)

mx3 = Matrix([[2, 3, 4], [5, 6], [1, 2, 3, 4], [8]])

