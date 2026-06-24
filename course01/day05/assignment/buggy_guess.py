secret = 42
for i in range(7):  
    g = int(input("Guess: "))
    if g == secret:
        print("Win!")
        break
