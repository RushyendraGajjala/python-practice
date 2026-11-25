import numpy as np
from numpy.ma.core import reshape

arr01 = np.arange(1, 10)
matrix1 = arr01.reshape((3, 3))
matrix2 = matrix1.copy()

print(matrix1)

print("-----------------")

print("Sum  : ", np.sum(matrix1))
print("Max  : ", np.max(matrix1))
print("Mean : ", np.mean(matrix1))

print("-----------------")

print(f"Transpose of Matrix: \n{matrix1.transpose()}")

print("-----------------")

print(f"Addition: \n{matrix1 + matrix2}")

print("-----------------")

print(f"Multiplication: \n{matrix1 * matrix2}")