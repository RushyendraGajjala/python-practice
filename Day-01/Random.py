import random
from math import floor, ceil

import my_module as m

print(random.randint(2,5))
print(random.getrandbits(5))

print(m.my_favourite_number)

randomNum = random.random()
print(ceil(randomNum * 10))

random_fl = random.uniform(10,20)
print(floor(random_fl))

randInt = random.randint(0, 1)
print("Tails" if randInt == 0 else "Heads")