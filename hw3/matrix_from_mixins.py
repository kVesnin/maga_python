import numpy as np


class DataAccessMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)

    @property
    def rows(self):
        return self._data.shape[0]

    @property
    def cols(self):
        return self._data.shape[1]


class ArithmeticMixin:
    def __add__(self, other):
        result = self.data + other.data
        return self.__class__(result)

    def __mul__(self, other):
        result = self.data * other.data
        return self.__class__(result)

    def __matmul__(self, other):
        result = self.data @ other.data
        return self.__class__(result)


class FileIOMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.data.tolist():
                f.write(' '.join(map(str, row)) + '\n')


class PrettyPrintMixin:
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data.tolist()])


class Matrix(DataAccessMixin, ArithmeticMixin, FileIOMixin, PrettyPrintMixin):
    def __init__(self, data):
        self.data = data


