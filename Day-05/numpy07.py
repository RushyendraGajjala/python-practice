import numpy as np

# Random number generation and setting seeds
# Without setting seed

rng = np.random.default_rng()

rand_arr1 = rng.integers(1, 15, size=5)
print(rand_arr1)

rand_arr2 = np.random.rand(2, 3)
print(rand_arr2)

rand_integers = np.random.randint(1, 10, size=(2, 3))
print(rand_integers)