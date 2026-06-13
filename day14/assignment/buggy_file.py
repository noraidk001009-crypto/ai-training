with open("x.txt", "w") as f:
    f.write("hi\n")

with open("x.txt") as f:
    print("Content:", f.read().strip())