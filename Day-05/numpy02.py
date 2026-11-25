import numpy as np

# We can Reshape an Array

arr1 = np.array([i for i in range(1, 11)])
reshaped = arr1.reshape(2, 5)

print(reshaped)

print("-----------------------")

# If we expand an array then each element have its own list of single item. list of no of items of lists
# adds up new axis for each element
arr2 = np.array([_ for _ in range(1, 9)])
expanded = arr2[:, np.newaxis]

print(expanded)
