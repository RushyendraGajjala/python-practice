import numpy as np

# Creating Array in NumPy
# -> From a List
# -> Using built-in function

arr = np.array([i for i in range(1, 11)])
print(arr)

print("-----------------------")

zeros = np.zeros((3, 3))
print(zeros)

print("-----------------------")

ones = np.ones((2, 4))
print(ones)

print("-----------------------")

zero = np.zeros(5)
print(zero)

print("-----------------------")

range_arr = np.arange(0, 10, 2)
print(range_arr)

print("-----------------------")

linspace_arr = np.linspace(0, 1, 5)
print(linspace_arr)
# Linspace: it creates or divides the numbers equally in specified interval.
