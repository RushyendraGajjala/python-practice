import numpy as np

# Random number generation and setting seeds
# With setting seed
np.random.seed(9)

rand_arr2 = np.random.rand(2, 3)
print(rand_arr2)

rand_integers = np.random.randint(1, 10, size=(2, 3))
print(rand_integers)