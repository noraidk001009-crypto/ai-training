import csv #引入csv模块
from pathlib import Path #引入pathlib模块

HERE = Path(__file__).resolve().parent
candidates = [ #定义candidates
    HERE / "fights.csv",
    HERE.parent / "fights.csv",
]
csv_path = next((p for p in candidates if p.exists()), None) #找到第一个存在的csv文件
if csv_path is None:
    raise FileNotFoundError("No fights.csv found — put it in day15/ or assignment/")

rows = [] #定义rows
with open(csv_path, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f): #读取csv文件 并转换为字典
        if not row.get("fight_id", "").strip():
            continue #如果fight_id为空，则跳过
        rows.append(row) #将row添加到rows中

total = len(rows) #计算总行数
player_wins = sum(1 for r in rows if r.get("winner", "").strip().lower() == "player") #计算玩家获胜次数
boss_wins = sum(1 for r in rows if r.get("winner", "").strip().lower() == "boss") #计算boss获胜次数

total_fights = sum(int(r.get("fights") or 0) for r in rows) #计算总fight次数
total_defends = sum(int(r.get("defends") or 0) for r in rows) #计算总defend次数
total_heals = sum(int(r.get("heals") or 0) for r in rows) #计算总heal次数
def avg(key, subset):
    if not subset: #如果subset为空，则返回0.0
        return 0.0
    return sum(int(r.get(key) or 0) for r in subset) / len(subset) #计算平均值

wins = [r for r in rows if r.get("winner", "").strip().lower() == "player"] #计算玩家获胜的行
losses = [r for r in rows if r.get("winner", "").strip().lower() == "boss"] #计算boss获胜的行

print(f"CSV: {csv_path}") #打印csv文件路径
print(f"Total fights: {total}") #打印总fight次数
print(f"Player wins: {player_wins}  |  Boss wins: {boss_wins}") #打印玩家获胜次数和boss获胜次数 
if total:
    print(f"Player win rate: {player_wins / total:.0%}") #打印玩家获胜率
print()
print("Command totals across all fights:")
print(f"  fight:  {total_fights}") #打印总fight次数
print(f"  defend: {total_defends}")
print(f"  heal:   {total_heals}") #打印总heal次数
most = max(
    [("fight", total_fights), ("defend", total_defends), ("heal", total_heals)],
    key=lambda x: x[1], #按次数排序
)
print(f"Most-used command: {most[0]} ({most[1]} times)") #打印最常用的命令和次数
print()
print("Averages when PLAYER wins:") #打印玩家获胜时的平均值
print(f"  rounds={avg('rounds', wins):.1f}  fights={avg('fights', wins):.1f}  " #打印回合数、fight次数、defend次数、heal次数
      f"defends={avg('defends', wins):.1f}  heals={avg('heals', wins):.1f}") #打印回合数、fight次数、defend次数、heal次数
print("Averages when BOSS wins:") #打印boss获胜时的平均值
print(f"  rounds={avg('rounds', losses):.1f}  fights={avg('fights', losses):.1f}  " #打印回合数、fight次数、defend次数、heal次数
      f"defends={avg('defends', losses):.1f}  heals={avg('heals', losses):.1f}") #打印回合数、fight次数、defend次数、heal次数
