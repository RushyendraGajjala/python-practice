import pandas as pd

s1 = pd.Series([_ for _ in range(1, 11)])
print(s1)

s2 = pd.Series([_ for _ in range(1, 11)], index=[_ for _ in range(1, 11)])
print(s2)

data = {"Names": ["Srinivas", "Rishi"], "Ages":[23, 22]}
sample = pd.DataFrame(data, index=[1, 2])
print(sample)