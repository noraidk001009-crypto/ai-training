import csv
import sys
from pathlib import Path

def clean_row(row):
    cmd = (row.get("command") or "").strip()
    if not cmd:
        return None
    try:
        ph = int(row["player_hp"])
        dh = int(row["dragon_hp"])
    except ValueError:
        return None
    return {
        "round": row["round"],
        "command": cmd,
        "player_hp": ph,
        "dragon_hp": dh,
        "note": row.get("note", ""),
    }


def main():
    here = Path(__file__).resolve().parent  
    source = here / "messy_source.csv" 
    output = here / "clean_fights.csv" 

    fieldnames = ["round", "command", "player_hp", "dragon_hp", "note"] # 定义字段名
    seen_rounds = set() # 定义已处理回合集合
    clean_rows = [] # 定义清洗后的行列表

    with source.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f): 
            cleaned = clean_row(row) 
            if cleaned is None: 
                continue
            if cleaned["round"] in seen_rounds:
                continue # 如果回合已处理，则跳过
            seen_rounds.add(cleaned["round"]) # 添加回合到已处理集合
            clean_rows.append(cleaned) # 添加清洗后的行到列表           

    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames) # 创建写入器
        writer.writeheader() # 写入表头     
        writer.writerows(clean_rows) # 写入数据

    print("\n--- Cleaned data ---")
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(clean_rows)


if __name__ == "__main__":
    main()
