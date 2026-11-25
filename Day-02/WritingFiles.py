with open("sample01.txt", "w") as file:
    file.write("Hello there!\n")
    file.writelines(["Ohhh"," My", " Gawd!"])
    print("Content written in File")

try:
    with open("sample02.txt", "r") as file:
        print(file.read())
        print("Done")
except:
    print("Error")