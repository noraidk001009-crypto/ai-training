import csv #引入csv模块
from pathlib import Path #引入pathlib模块

import matplotlib #引入matplotlib模块

matplotlib.use("Agg") #使用Agg后端
import matplotlib.pyplot as plt #引入matplotlib.pyplot模块

HERE = Path(__file__).resolve().parent #定义HERE
candidates = [
    HERE / "fights.csv",    #定义candidates
    HERE.parent / "fights.csv", #定义candidates 
]
csv_path = next((p for p in candidates if p.exists()), None) #找到第一个存在的csv文件
if csv_path is None:
    raise FileNotFoundError("No fights.csv found — put it in day15/ or assignment/") #如果csv文件不存在，则抛出异常

rows = [] #定义rows
with open(csv_path, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f): #读取csv文件 并转换为字典
        if not row.get("fight_id", "").strip():
            continue #如果fight_id为空，则跳过
        rows.append(row)

totals = {
    "fight": sum(int(r.get("fights") or 0) for r in rows), #计算总fight次数
    "defend": sum(int(r.get("defends") or 0) for r in rows), #计算总defend次数
    "heal": sum(int(r.get("heals") or 0) for r in rows), #计算总heal次数
}
labels = list(totals.keys()) #定义labels
values = [totals[k] for k in labels]
colors = {"fight": "#2E86AB", "defend": "#28A745", "heal": "#E67E22"} #定义colors

fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(labels, values, color=[colors[c] for c in labels]) #定义bars
ax.set_xlabel("Command") #设置x轴标签
ax.set_ylabel("Times used (all fights)") #设置y轴标签       
ax.set_title(f"Commands in capstone fights (n={len(rows)})") #设置标题
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, value, str(value),
            ha="center", va="bottom") #设置文本
fig.tight_layout() #设置布局

out = HERE / "capstone_chart.png" #定义out
fig.savefig(out, dpi=120) #保存图片
print(f"Saved {out.name} from {csv_path}") #打印保存的文件名和csv文件路径
print("Command totals:", totals) #打印命令总数
