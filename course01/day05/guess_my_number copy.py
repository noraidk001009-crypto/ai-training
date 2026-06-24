secret = 19 means the secret number is 19
for i in range(7): means we have 7 chances to guess the number
    g = int(input("Guess: "))get the guess from the user
    if g == secret:means if the guess is equal to the secret number
        print("Win!")if the guess is equal to the secret number, we print "Win!"
        break 
    elif g < secret:
        print("Too low — guess higher.")
    else:
        print("Too high — guess lower.")