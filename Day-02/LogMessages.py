import datetime as dt

while(True):
    inputt = input()
    with open("Test05.txt","a") as f:
        timestamp = dt.datetime.now()
        f.write(f"{inputt} : {timestamp}\n")
        if(inputt == "clear"):
            f.write("-----------------\n")
            break
print("Exited from while loop")