import csv
from pathlib import Path

path = Path(__file__).parent / "sample_fights.csv"
with open(path) as f:
    rows = list(csv.DictReader(f))

print("Total fights:", len(rows))
commands = [r["command"] for r in rows]
print("Commands:", set(commands))
