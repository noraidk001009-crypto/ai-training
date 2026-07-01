import csv
from pathlib import Path

path = Path(__file__).resolve().parents[2] / "day04" / "assignment" / "fights.csv"

with open(path) as f:
    rows = [r for r in csv.DictReader(f) if r.get("command")]

print("Total rows:", len(rows))
commands = {r["command"] for r in rows}
print("Commands used:", commands)
lowest_hp = min(int(r["player_hp"]) for r in rows)
print("Lowest player_hp:", lowest_hp)
