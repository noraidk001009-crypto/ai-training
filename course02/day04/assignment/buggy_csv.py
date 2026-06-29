import csv
import os

filename = "fights.csv"
write_header = not os.path.exists(filename) or os.path.getsize(filename) == 0

with open(filename, "a", newline="") as f:
    w = csv.writer(f)
    if write_header:
        w.writerow(["round", "command", "player_hp", "dragon_hp", "note"])
    w.writerow([1, "fight", 20, 15, ""])
