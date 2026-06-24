with open("highscore.txt", "w") as f:
    f.write("9000\n")
with open("highscore.txt") as f:
    print("Best:", f.read().strip())
