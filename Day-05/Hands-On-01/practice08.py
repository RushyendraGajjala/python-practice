import numpy as np

np.random.seed(21)

rand_floats = np.random.rand(5)

print(rand_floats)

maxx = max(rand_floats)
minn = min(rand_floats)

if(maxx == minn):
    print([0 for _ in range(len(rand_floats))])
else:
    normalize = map(lambda x: round((x-minn) / (maxx - minn), 3), rand_floats)
    print(list(map(float, normalize)))