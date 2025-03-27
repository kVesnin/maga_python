from functools import lru_cache

class Matrix:
    def __init__(self, data):
        if not data:
            raise ValueError("Пустая матрица")
        rows = len(data)
        cols = len(data[0])
        for row in data:
            if len(row) != cols:
                raise ValueError("Все длины строк должны совпадать")
        self.data = data
        self.rows = rows
        self.cols = cols

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера")
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    @lru_cache(maxsize=None)
    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Число строк в первой матрице должно равняться числу столбцов во второй")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum_val = 0
                for k in range(self.cols):
                    sum_val += self.data[i][k] * other.data[k][j]
                row.append(sum_val)
            result.append(row)
        return Matrix(result)

    def _sum(self):
        result = 0
        for row in self.data:
            for el in row:
                result += el
        return result

    def __hash__(self):
        return int(self._sum() + self.rows * self.cols)

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
