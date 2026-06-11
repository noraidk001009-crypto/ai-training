import random
options = ["rock", "paper", "scissors"] #three choice for computer to choose
def main():
    you, cpu = 0, 0 
    print("Rock / Paper / Scissors\nBest of 3 - first to 2 wins!\n")
    while you < 2 and cpu < 2:
        raw = input("Your move (rock/paper/scissors, quit to stop): ")
        c = raw.strip().lower()
        if c == "quit": print("Bye!"); return
        move = ""
        if c in ("rock", "r"): move = "rock" 
        elif c in ("paper", "p"): move = "paper"
        elif c in ("scissors", "s"): move = "scissors"
        elif c in ("handle", "h"): #secret bonus for player to cheat
            you = you + 1
            print("Secret bonus! +1 score!", you, "-", cpu)
            continue
        if move == "": print("Invalid."); continue
        comp = random.choice(options); # random choice for computer to choose
        print("You:", move, "| Computer:", comp) 
        if move == comp: print("Tie!")
        elif move == "rock" and comp == "scissors" or move == "scissors" and comp == "paper" or move == "paper" and comp == "rock":
            you = you + 1; print("You win!", you, "-", cpu) 
        else: cpu = cpu + 1; print("CPU wins.", you, "-", cpu)
main()
