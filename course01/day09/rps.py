import random
options = ["rock", "paper", "scissors"]
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
        if move == "": print("Invalid."); continue
        comp = random.choice(options); print("You:", move, "| Computer:", comp)
        if move == comp: print("Tie!")
        elif move == "rock" and comp == "scissors" or move == "scissors" and comp == "paper" or move == "paper" and comp == "rock":
            you = you + 1; print("You win!", you, "-", cpu)
        else: cpu = cpu + 1; print("CPU wins.", you, "-", cpu)
    if you > cpu: print("YOU WIN!", you, "-", cpu)
    else: print("CPU wins.", you, "-", cpu)
main()
