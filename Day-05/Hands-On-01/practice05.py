import random
import numpy as np

rng = np.random.default_rng()

nums = rng.integers(1, 100, size=5)

print(nums)

print(f"Maximum: {max(nums)}")
print(f"Minimum: {min(nums)}")