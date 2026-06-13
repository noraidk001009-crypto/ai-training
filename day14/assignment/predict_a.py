"""Assignment A — predict, then run to check."""
from pathlib import Path

path = Path(__file__).resolve().parent / "highscore.txt"

with open(path, "w") as f:
    f.write("5")

with open(path) as f:
    result = f.read()
    print("read() returns:", repr(result))
