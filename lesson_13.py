# Задание 1

import random

matrix_1 = []
matrix_2 = []

for i in range(10):
    row_1 = []
    row_2 = []
    for j in range(10):
        row_1.append(random.randint(-100, 100))
        row_2.append(random.randint(-100, 100))
    matrix_1.append(row_1)
    matrix_2.append(row_2)

matrix_3 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_3.append(row)

print("matrix_1 = [")
for row in matrix_1:
    print(row, ",")
print("]")

print("\nmatrix_2 = [")
for row in matrix_2:
    print(row, ",")
print("]")

print("\nmatrix_3 = [")
for row in matrix_3:
    print(row, ",")
print("]")