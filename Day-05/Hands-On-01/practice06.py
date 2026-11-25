import numpy as np

np.random.seed(9)

matrix = np.random.randint(1, 100, size=(5,5))

print(matrix)
print(f"Sum: {np.sum(matrix)}")
print(f"Mean: {np.mean(matrix)}")
print(f"Standard Deviation: {np.std(matrix)}")

print("\n--------------\nAfter Filtering replacing values lower than 50\n")

matrix[matrix < 50] = 0

print(matrix)
print(f"Sum: {np.sum(matrix)}")
print(f"Mean: {np.mean(matrix)}")
print(f"Standard Deviation: {np.std(matrix)}")