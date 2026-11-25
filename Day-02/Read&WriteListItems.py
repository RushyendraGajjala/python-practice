listt = [
    "This is the first item",
    "This is the second item",
    "This is the third item",
    "This is the fourth item",
    "This is the fifth item",
]

def writeAndRead(fileName):
    try:
        with open(fileName, "w") as file:
            file.writelines(item+"\n" for item in listt)
        with open(fileName, "r") as file:
            print(file.read())
    except:
        print("Something went wrong")

writeAndRead("Test02.txt")