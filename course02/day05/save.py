import json
from pathlib import Path

from character import Warrior, Wizard

SAVE = Path("save_slot.json")

CLASSES = {"warrior": Warrior, "wizard": Wizard}


def save_game(player, dragon_hp):
    """Write the current fight to the save slot as JSON."""
    state = {
        "class": player.name.lower(),
        "player_hp": player.hp,
        "dragon_hp": dragon_hp,
    }
    with open(SAVE, "w") as f:
        json.dump(state, f, indent=2)
    print("Game saved.")


def load_game():
    """Return (player, dragon_hp), or None if there is no save file yet."""
    if not SAVE.exists():
        return None
    with open(SAVE) as f:
        state = json.load(f)
    cls = CLASSES[state["class"]]
    player = cls(state["class"].capitalize(), state["player_hp"])
    return player, state["dragon_hp"]


def delete_save():
    """Remove the save slot (e.g. after the fight ends)."""
    if SAVE.exists():
        SAVE.unlink()
