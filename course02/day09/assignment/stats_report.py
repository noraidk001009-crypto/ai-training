import csv 
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
for name in ("clean_fights.csv", "fights.csv"):
    csv_path = HERE / name
    if csv_path.exists():
        break
else:
    csv_path = HERE.parent / "demos" / "sample_fights.csv"

rows = list(csv.DictReader(open(csv_path, encoding="utf-8")))
total = len(rows)
cmds = Counter(r.get("command", "").strip().lower() for r in rows)
fight_count = cmds.get("fight", 0)
wins = sum(
    1
    for r in rows
    if "win" in r.get("note", "").lower()
    or str(r.get("dragon_hp", "")).strip() == "0"
)
win_rate = (wins / total * 100) if total else 0.0
most_cmd, most_count = cmds.most_common(1)[0] if cmds else ("—", 0)

report = f"""# Fight stats report

Total rounds: {total}
Fight commands: {fight_count}
Wins: {wins}
Win rate: {win_rate:.0f}%

The most-used command was "{most_cmd}" ({most_count} of {total} rounds).
You won {wins} out of {total} rounds, a {win_rate:.1f}% win rate.
"""

report_path = HERE / "REPORT.txt"
report_path.write_text(report, encoding="utf-8")
print(f"Wrote {report_path.name} from {csv_path.name}")
