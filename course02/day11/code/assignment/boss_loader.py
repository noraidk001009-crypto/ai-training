import json
from pathlib import Path

BOSSES_FILE = Path(__file__).parent / "bosses.json"


def load_bosses():
    """Read every boss definition from bosses.json."""
    with open(BOSSES_FILE, encoding="utf-8") as f:
        return json.load(f)


def get_boss(name):
    """Return a fresh boss dict picked by name, or None if no boss matches."""
    bosses = load_bosses()
    chosen = next((b for b in bosses if b["name"].lower() == name.lower()), None)
    if chosen is None:
        return None
    # Copy so a fight mutating hp never changes the data we loaded.
    return dict(chosen)


def choose_boss():
    """Interactively let the player pick a boss by number or name."""
    bosses = load_bosses()
    print("Choose your boss:")
    for i, boss in enumerate(bosses, 1):
        print(f"  {i}. {boss['name']} (HP {boss['hp']}, ATK {boss['atk']})")
    while True:
        choice = input("boss> ").strip()
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(bosses):
                return dict(bosses[num - 1])
        elif choice:
            by_name = get_boss(choice)
            if by_name is not None:
                return by_name
        print("Unknown boss, try again.")


if __name__ == "__main__":
    # Same demo as the lesson, now reading the assignment's bosses.
    for boss in load_bosses():
        print(boss["name"], "HP", boss["hp"], "ATK", boss["atk"])
