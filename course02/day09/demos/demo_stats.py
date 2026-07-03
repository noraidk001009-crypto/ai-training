import csv
from collections import Counter
from pathlib import Path

rows = list(csv.DictReader(open(Path(__file__).parent / "sample_fights.csv")))
cmds = Counter(r["command"].strip() for r in rows)
wins = sum(1 for r in rows if "win" in r.get("note", "").lower())
print("Command counts:", dict(cmds))
print("Wins tagged:", wins)
