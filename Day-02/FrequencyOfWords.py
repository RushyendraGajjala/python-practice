import re

content = list()
with open("Test04.txt", "r") as f:
        cont = f.read()
        content = [item.lower() for item in re.findall(r"\w+", cont)]
        print(content)

dictt = dict()

for i in content:
    if i in dictt:
        dictt[i] += 1
    else:
        dictt[i] = 1

dictt = dict(sorted(dictt.items(), key = lambda item: item[1], reverse=True))
print(dictt)
