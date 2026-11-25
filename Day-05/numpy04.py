import numpy as np

# Array and Scalar Broadcasting
arr = np.array([1, 2, 3])
print(arr + 10)

print()
print("----------------")
print()

matrix = np.arange(1, 7).reshape((2, 3))
temp = np.arange(1, 4)

print(matrix)
print(temp)

print(matrix + temp)