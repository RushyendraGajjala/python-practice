import numpy as np

matrix = np.arange(1,17).reshape((4, 4))

print("-------------------")
print(matrix)
print("-------------------")

for i in matrix:
    print(f"The Sum of {i} is {sum(i)}")

print("-------------------")

for i in range(len(matrix[0])):
    print(f"The sume of column {i+1} is {matrix[0][i] + matrix[1][i] + matrix[2][i] + matrix[3][i]}")
