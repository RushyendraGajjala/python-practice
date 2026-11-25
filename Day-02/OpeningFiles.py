with open("Sample.txt", "r") as file:
    print(file.read())
    file.seek(0)
    print("--------------------------")
    print(file.readline())
    print("--------------------------")
    file.seek(0)
    print(file.readlines())