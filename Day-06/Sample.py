String = "A Bumble bee had a pet fox that jumped over a lazy dog quickly"

String = String.lower()
ls = "".join(String.split(" "))
stt = set(list(ls))


for i in stt:
    print(f"The count of {i} is {String.count(i)}")

