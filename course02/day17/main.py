import csv #引入csv模块
import random #引入random模块
from pathlib import Path #引入pathlib模块
CSV_PATH = Path(__file__).with_name("fights.csv") #定义CSV_PATH
HEADER = [ #定义HEADER
    "fight_id",
    "winner",
    "rounds",
    "fights",
    "defends",
    "heals",
    "player_hp_end",
    "boss_hp_end",
]

PLAYER_MAX_HP = 30 #定义PLAYER_MAX_HP
BOSS_NAME = "Dragon" #定义BOSS_NAME
BOSS_MAX_HP = 40 #定义BOSS_MAX_HP


def next_fight_id():
    if not CSV_PATH.exists() or CSV_PATH.stat().st_size == 0: #如果CSV_PATH不存在或大小为0，则返回1
        return 1
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    ids = [] #定义ids列表
    for row in rows:
        try:
            ids.append(int(row.get("fight_id", 0))) #将row的fight_id转换为整数并添加到ids列表中
        except (TypeError, ValueError):
            continue
    return max(ids, default=0) + 1 #返回ids列表中的最大值加1


def append_fight_row(row):
    write_header = not CSV_PATH.exists() or CSV_PATH.stat().st_size == 0 #如果CSV_PATH不存在或大小为0，则返回True
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER) #创建一个csv.DictWriter对象
        if write_header:
            writer.writeheader() #写入header
        writer.writerow(row)
    print(f"Logged fight #{row['fight_id']} -> {CSV_PATH.name}") #打印日志


def clamp(n, lo=0, hi=None):
    """Keep n in [lo, hi]. hi=None means no upper cap."""
    n = max(lo, n)
    if hi is not None:
        n = min(hi, n)
    return n


def do_fight(player_hp, boss_hp):
    """Player attacks, then boss counters if still alive."""
    damage = random.randint(5, 10) #生成一个5到10之间的随机整数             
    boss_hp = clamp(boss_hp - damage) #将boss_hp减去damage并返回
    print(f"You fight! Deal {damage} damage. {BOSS_NAME} HP: {boss_hp}")    
    if boss_hp > 0:
        counter = random.randint(6, 10) #生成一个6到10之间的随机整数    
        player_hp = clamp(player_hp - counter) #将player_hp减去counter并返回
        print(f"{BOSS_NAME} bites back for {counter}! Your HP: {player_hp}")
    return player_hp, boss_hp


def do_defend(player_hp, boss_hp):
    """Brace: take reduced damage. No damage to boss."""
    raw = random.randint(6, 10) #生成一个6到10之间的随机整数    
    taken = raw // 2 #将raw除以2并返回
    player_hp = clamp(player_hp - taken) #将player_hp减去taken并返回
    print(
        f"You defend! {BOSS_NAME} hits for {raw}, you block half "
        f"and take {taken}. Your HP: {player_hp}"
    )
    return player_hp, boss_hp


def do_heal(player_hp, boss_hp):
    """Drink a potion: restore HP (capped at max), then boss still hits."""
    restored = random.randint(8, 14)
    before = player_hp
    player_hp = clamp(player_hp + restored, hi=PLAYER_MAX_HP)
    gained = player_hp - before
    print(
        f"You heal! Restore {gained} HP "
        f"(tried {restored}, max {PLAYER_MAX_HP}). Your HP: {player_hp}"
    )
    counter = random.randint(6, 10)
    player_hp = clamp(player_hp - counter)
    print(f"{BOSS_NAME} strikes while you drink for {counter}! Your HP: {player_hp}")
    return player_hp, boss_hp


def play_one_fight():
    player_hp = PLAYER_MAX_HP #定义player_hp
    boss_hp = BOSS_MAX_HP #定义boss_hp
    rounds = 0 #定义rounds
    fights = 0 #定义fights
    defends = 0
    heals = 0 #定义heals

    print("=" * 40) #打印40个=
    print("  war with dragon") #打印war with dragon
    print(f"  A malevolent {BOSS_NAME} wants to eat humans")
    print("  and destroy the village.") #打印and destroy the village.                   
    print("=" * 40) #打印40个=
    print(f"Your HP: {player_hp}  |  {BOSS_NAME} HP: {boss_hp}")    
    print("Commands: fight / defend / heal / quit")

    while player_hp > 0 and boss_hp > 0:
        cmd = input("> ").strip().lower() #输入命令
        if cmd == "quit":
            print("You flee. Fight not logged.") #打印You flee. Fight not logged.
            return None
        if cmd == "fight":
            rounds += 1 #rounds加1  
            fights += 1 #fights加1
            player_hp, boss_hp = do_fight(player_hp, boss_hp)
        elif cmd == "defend":
            rounds += 1 #rounds加1
            defends += 1 #defends加1
            player_hp, boss_hp = do_defend(player_hp, boss_hp)
        elif cmd == "heal":
            rounds += 1
            heals += 1
            player_hp, boss_hp = do_heal(player_hp, boss_hp)
        else:
            print("Unknown command. Use: fight, defend, heal, quit")
            continue

        print(f"[round {rounds}] You {player_hp} HP | {BOSS_NAME} {boss_hp} HP") #打印[round {rounds}] You {player_hp} HP | {BOSS_NAME} {boss_hp} HP

    if boss_hp <= 0:
        winner = "player" #定义winner
        print(f"You win! {BOSS_NAME} is defeated. (BossHP=0)")
    else:
        winner = "boss" #定义winner
        print(f"You lose! {BOSS_NAME} eats you. (PlayerHP=0)")

    return {
        "fight_id": next_fight_id(), #定义fight_id  
        "winner": winner,
        "rounds": rounds, #定义rounds
        "fights": fights, #定义fights
        "defends": defends, #定义defends
        "heals": heals, # must match HEADER / CSV columns
        "player_hp_end": player_hp, #定义player_hp_end
        "boss_hp_end": boss_hp, #定义boss_hp_end
    }


def main():
    result = play_one_fight() #调用play_one_fight函数
    if result is not None:
        append_fight_row(result) #调用append_fight_row函数


if __name__ == "__main__":
    main() #调用main函数
