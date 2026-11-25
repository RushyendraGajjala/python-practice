import numpy as np

# Basic Operations on Array

arr1 = np.array([i for i in range(1, 6)])
arr2 = np.array([i for i in range(6, 11)])

print(arr1 + arr2)
print(arr1 * arr2)
print(arr1 / arr2)

print("-------------------")
a1 = [1, 2, 3]
a2 = [4, 5, 6]
print(a1 + a2)
# print(a1 * a2) -- Error
print("-------------------")

arr3 = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
print(np.sqrt(arr3))
print(np.sum(arr3))
print(np.mean(arr3))
print(np.max(arr3))