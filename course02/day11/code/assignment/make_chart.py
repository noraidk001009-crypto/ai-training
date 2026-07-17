
import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).parent
candidates = [
    HERE.parent / "fights.csv",
    HERE / "fights.csv",
    HERE.parents[2] / "day10" / "assignment" / "fights.csv",
]
csv_path = next((p for p in candidates if p.exists() and p.stat().st_size > 0), None)
if csv_path is None:
    raise FileNotFoundError(
        "No fight CSV found. Run: python -m assignment.sim_balance"
    )

rows = list(csv.DictReader(open(csv_path, encoding="utf-8")))
cmds = Counter(
    r.get("command", "").strip().lower()
    for r in rows
    if r.get("command", "").strip().lower() in {"fight", "defend", "poison"}
)

labels = list(cmds.keys())
values = [cmds[k] for k in labels]
colors = {"fight": "#2E86AB", "defend": "#28A745", "poison": "#6F42C1"}

plt.bar(labels, values, color=[colors.get(c, "#888888") for c in labels])
plt.xlabel("Command")
plt.ylabel("Times used")
plt.title(f"Commands in {csv_path.stem} ({sum(values)} total)")
plt.tight_layout()

out = HERE / "my_chart.png"
plt.savefig(out)
print(f"Saved {out.name} from {csv_path.name}")
print("Command counts:", dict(cmds))
