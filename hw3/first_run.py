import numpy as np
from matrix import Matrix

np.random.seed(0)
a_np = np.random.randint(0, 10, (10, 10))
b_np = np.random.randint(0, 10, (10, 10))

a = Matrix(a_np.tolist())
b = Matrix(b_np.tolist())

sum_matrix = a + b
prod_matrix = a * b
matmul_matrix = a @ b

with open('artifacts/task1/matrix+.txt', 'w') as f:
    f.write(str(sum_matrix))

with open('artifacts/task1/matrix*.txt', 'w') as f:
    f.write(str(prod_matrix))

with open('artifacts/task1/matrix@.txt', 'w') as f:
    f.write(str(matmul_matrix))