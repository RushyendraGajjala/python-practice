def fileContent(filename):
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except:
        return "File not found"

def writeToFile(filename, content):
    try:
        with open(filename, "w") as f:
            f.writelines(content)
            print("Data written successfully")
    except:
        print("Something went wrong")

def readNewFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.readlines())
    except:
        print("File not found")

content = fileContent("Test02.txt")
writeToFile("Test03.txt", content)
readNewFile("Test03.txt")