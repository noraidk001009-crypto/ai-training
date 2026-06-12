import random
from datetime import datetime
from pathlib import Path

path = Path(__file__).resolve().parent / "highscore.txt"
options = ["rock", "paper", "scissors"]

def load_best():
    try:
        with open(path) as f:
            lines = [l.strip() for l in f if l.strip()]
        return lines[-1] if lines else "0"
    except FileNotFoundError:
        return "0"

def save_score(you, cpu):
    score = f"{you}-{cpu}"
    with open(path, "a") as f:
        f.write(f"{score} | {datetime.now():%Y-%m-%d %H:%M:%S}\n")
    return score

def main():
    best_score = load_best()
    you, cpu = 0, 0
    print("Rock / Paper / Scissors\nBest of 9 - first to 5 wins!\nBest:", best_score, "\n")
    while you < 5 and cpu < 5:
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
            you = you + 1
            print("You win!", you, "-", cpu)
        else:
            cpu = cpu + 1
            print("CPU wins.", you, "-", cpu)
    save_score(you, cpu)
    if you > cpu:
        print("YOU WIN!", you, "-", cpu)
    else:
        print("CPU wins.", you, "-", cpu)

main()
