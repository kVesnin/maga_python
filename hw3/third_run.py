from matrix import Matrix


A = Matrix([[1, 2], [3, 4]])
C = Matrix([[4, 3], [2, 1]])

B = D = Matrix([[1, 0], [0, 1]])

AB = A @ B
CD = C @ D

for name, obj in [('A', A), ('B', B), ('C', C), ('D', D), ('AB', AB), ('CD', CD)]:
    with open(f'artifacts/task3/{name}.txt', 'w') as f:
        f.write(str(obj))

with open('artifacts/task3/hash.txt', 'w') as f:
    f.write(f"Hash AB: {hash(AB)}\nHash CD: {hash(CD)}")