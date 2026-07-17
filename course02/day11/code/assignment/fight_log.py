import csv
from pathlib import Path

LOG_FILE = Path(__file__).with_name("fights.csv")

HEADER = ["round", "command", "damage", "player_hp", "boss_hp", "winner", "note"]

_new_game_pending = False


def start_new_game():
    """Begin a fresh game: the next logged row will be separated by a blank line."""
    global _new_game_pending
    _new_game_pending = True
    return LOG_FILE


def log_round(round_num, command, damage, player_hp, boss_hp="", winner="", note=""):
    """Append one row to fights.csv, separating each new game with a blank line."""
    global _new_game_pending
    file_empty = not LOG_FILE.exists() or LOG_FILE.stat().st_size == 0
    with open(LOG_FILE, "a", newline="") as f:
        w = csv.writer(f)
        if file_empty:
            w.writerow(HEADER)
        elif _new_game_pending:
            f.write("\n")
        _new_game_pending = False
        w.writerow([round_num, command, damage, player_hp, boss_hp, winner, note])
