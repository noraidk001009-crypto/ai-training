secret = 67
for i in range(7):
    g = int(input("Guess: "))
    if g == secret:
        print("Win!")
        break
    elif g < secret:
        print("Too low — guess higher.")
    else:
        print("Too high — guess lower.")