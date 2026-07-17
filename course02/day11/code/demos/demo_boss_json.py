import json
from pathlib import Path

def load_bosses():
    with open(Path(__file__).parent / "bosses.json") as f:
        return json.load(f)

for boss in load_bosses():
    print(boss["name"], "HP", boss["hp"], "ATK", boss["atk"])
