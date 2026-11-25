try:
    with open("Test01.txt", "r") as file:
        lines = file.readlines()
        print(f"Number of lines in the file are { len(lines)}")
        file.seek(0)
        noOfWords = sum(len(line.split()) for line in lines)
        print(noOfWords)
        print(f"The count of letters in file are {len(file.read())} including space")
        file.seek(0)
        content = file.read().split()
        words = "".join(content)
        print(f"The count of letters in file are {len(words)} excluding space")

        print(f"The no of words are {len(content)}")
except:
    print("Something went wrong!")