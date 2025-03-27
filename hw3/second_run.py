import numpy as np
from matrix_from_mixins import Matrix


np.random.seed(0)
a = Matrix(np.random.randint(0, 10, (10, 10)))
b = Matrix(np.random.randint(0, 10, (10, 10)))

matrix_add = a + b
matrix_mul = a * b
matrix_matmul = a @ b

matrix_add.save_to_file('artifacts/task2/matrix+.txt')
matrix_mul.save_to_file('artifacts/task2/matrix*.txt')
matrix_matmul.save_to_file('artifacts/task2/matrix@.txt')