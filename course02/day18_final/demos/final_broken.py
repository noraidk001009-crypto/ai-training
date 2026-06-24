import csv

def average_player_hp(path):
    with open(path) as f:
        rows = list(csv.DictReader(f))
    total = 0
    for r in rows:
        total += int(r["player_hp"])
    return total / len(rows)  # BUG on empty file

print(average_player_hp("fights.csv"))
