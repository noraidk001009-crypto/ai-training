import csv
from pathlib import Path

# All games share one CSV file; each game is separated by a blank line.
LOG_FILE = Path(__file__).with_name("fights.csv")

HEADER = ["round", "command", "damage", "player_hp", "dragon_hp", "winner", "note"]

# True right after start_new_game(), so the next logged row inserts a blank
# separator line before it (unless the file is brand new / empty).
_new_game_pending = False


def start_new_game():
    """Begin a fresh game: the next logged row will be separated by a blank line."""
    global _new_game_pending
    _new_game_pending = True
    return LOG_FILE


def log_round(round_num, command, damage, player_hp, dragon_hp="", winner="", note=""):
    """Append one row to fights.csv, separating each new game with a blank line."""
    global _new_game_pending
    file_empty = not LOG_FILE.exists() or LOG_FILE.stat().st_size == 0
    with open(LOG_FILE, "a", newline="") as f:
        w = csv.writer(f)
        if file_empty:
            w.writerow(HEADER)
        elif _new_game_pending:
            # Blank line between games for readability.
            f.write("\n")
        _new_game_pending = False
        w.writerow([round_num, command, damage, player_hp, dragon_hp, winner, note])
