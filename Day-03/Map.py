from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
squ = map(lambda x: x ** 2, numbers)
squ = list(squ)
print(squ)

odd = filter(lambda x : x % 2 != 0, numbers)
print(list(odd))

even = filter(lambda x : x % 2 == 0, numbers)
print(list(even))

sum01 = reduce(lambda x, y: x + y, numbers)
sum02 = reduce(lambda x, y: x + y, squ)
print(sum01)
print(sum02)