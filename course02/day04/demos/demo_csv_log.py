import csv
from pathlib import Path

LOG = Path("fights.csv")

def log_fight(round_num, command, player_hp, dragon_hp, note=""):
    new_file = not LOG.exists()
    with open(LOG, "a", newline="") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["round", "command", "player_hp", "dragon_hp", "note"])
        w.writerow([round_num, command, player_hp, dragon_hp, note])

log_fight(1, "fight", 20, 12, "hit")
log_fight(2, "defend", 18, 12, "blocked")
print("Logged to fights.csv")
