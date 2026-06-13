choice = ""
while choice != "2":
    choice = input("1=Play 2=Quit: ")
    if choice == "1":
        secret = 7
        print("Guess a number from 1 to 10.")
        while True:
            guess = int(input("Guess: "))
            if guess == secret:
                print("You win!")
                break
            if guess < secret:
                print("Too low!")
            else:
                print("Too high!")
print("Bye!")
