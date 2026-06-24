import json
from pathlib import Path

SAVE = Path("save_slot.json")

def save_game(player_hp, dragon_hp):
    with open(SAVE, "w") as f:
        json.dump({"player_hp": player_hp, "dragon_hp": dragon_hp}, f, indent=2)

def load_game():
    if not SAVE.exists():
        return None
    with open(SAVE) as f:
        return json.load(f)

save_game(18, 9)
print("Loaded:", load_game())
