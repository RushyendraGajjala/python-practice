import numpy as np

# Generating 3D matrix

np.random.seed(9)

matrix = np.random.randint(1, 60, size=(3, 3, 3))
print(matrix)

print("------------------\n")

print(f"The sum of rows: {np.sum(matrix, axis=1)}")
print(f"The sum of columns: {np.sum(matrix, axis=0)}")
print(f"The sum of z-axis: {np.sum(matrix, axis=-1)}")