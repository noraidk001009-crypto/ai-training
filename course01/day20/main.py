import random
def roll_d6():
    return random.randint(1, 6)

def main():
    print("Welcome to the game!")
    print("Type 'fight' to fight the dragon, or 'quit' to quit.")
    poison_active = False
    while True:
        command = input("> ").lower()
        if command == "fight":
            print("You fight the dragon!")
            print("You roll the dice to choose how many chance you have to fight.")
            your_roll = roll_d6()
            if poison_active:
                your_roll += 1
                poison_active = False
            dragon_roll = roll_d6()

            print(f"You rolled {your_roll}, the dragon rolled {dragon_roll}.")

            if your_roll > dragon_roll:
                print("You win the fight!")
            else:
                print("You lose the fight!")
        elif command == "poison":
            poison_active = True
            print("You use poison! Your next dice roll will be +1.")
        elif command == "quit":
            print("You quit the game.")
            break
main()