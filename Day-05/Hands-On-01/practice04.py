import numpy as np


listt = np.arange(10, 51, 10)
# listt = [5 for _ in range(5)]

maxx = max(listt)
minn = min(listt)

if(maxx == minn):
    print([0 for _ in range(len(listt))])
else:
    normaized = map(lambda x: ((x - minn)/(maxx - minn)), listt)
    print(list(map(float, normaized)))