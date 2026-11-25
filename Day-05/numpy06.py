import numpy as np

arr1 = np.arange(1, 7)

evens = arr1[arr1 % 2 == 0]
print(f"Even : {evens}")
print(f"Odd  : {arr1[arr1 % 2 != 0]}")

print(f"Elements greater than 3: {arr1[arr1 > 3]}")
arr1[arr1 > 3 ] = 0
print(f"After operation: {arr1}")