secret = 67
for i in range(7):
    while True:
        try:
            g = int(input("Guess: "))
            break
        except ValueError:
            print("Please type a number.")

    if g == secret:
        print("Win!")
        break
    elif g < secret:
        print("Too low — guess higher.")
    else:
        print("Too high — guess lower.")
