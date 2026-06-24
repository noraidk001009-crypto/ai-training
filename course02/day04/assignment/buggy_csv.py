import csv
with open("fights.csv", "a", newline="") as f:
    w = csv.writer(f)
    w.writerow(["round", "command", "player_hp", "dragon_hp", "note"])  # BUG every time
    w.writerow([1, "fight", 20, 15, ""])
