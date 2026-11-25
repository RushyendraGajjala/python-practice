import numpy as np

# Aggregation functions: It compute summary statistics for arrays

matrix1 = np.arange(1, 7).reshape((2, 3))
print(matrix1)

print("---------------")
print(f"Sum: {np.sum(matrix1)}")
print(f"Mean: {np.mean(matrix1)}")
print(f"Max: {np.max(matrix1)}")
print(f"Min: {np.min(matrix1)}")
print(f"Standard Deviation: {np.std(matrix1)}")
print(f"Sum along rows: {np.sum(matrix1, axis=1)}")
print(f"Sum along columns: {np.sum(matrix1, axis=0)}")