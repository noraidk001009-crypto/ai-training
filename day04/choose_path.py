answer = input("choose a path (1/2/3): ")
item = input("Do you have xingqiu? (y/n): ")

if answer == "1" and item == "y":
    print("You slay the monster and win!")
elif answer == "1" and item == "n":
    print("You lose:(.")
elif answer == "2":
    print("You find treasure.")
else:
    print("You get lost.")