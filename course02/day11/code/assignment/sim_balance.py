import contextlib  #引入上下文管理器
import csv  #引入csv模块
import io     #引入io模块
import sys  #引入sys模块
from pathlib import Path  #引入pathlib模块


CODE_DIR = Path(__file__).resolve().parent.parent  #获取代码目录    
if str(CODE_DIR) not in sys.path:  #如果代码目录不在sys.path中，则添加到sys.path中
    sys.path.insert(0, str(CODE_DIR))  #将代码目录添加到sys.path中

import matplotlib  #引入matplotlib模块
matplotlib.use("Agg")  #使用Agg后端，不使用屏幕显示
import matplotlib.pyplot as plt  #引入matplotlib.pyplot模块

from character import Warrior, Wizard  #引入character模块
from combat import fight, defend, apply_poison  #引入combat模块
from assignment.boss_loader import load_bosses
from assignment.fight_log import start_new_game, log_round, LOG_FILE  #引入fight_log模块

FIGHTS_PER_MATCHUP = 250  #设置每场战斗的次数
MAX_ROUNDS = 1000  #设置最大回合数

CLASSES = {  #设置职业  
    "Warrior": lambda: Warrior("Warrior", 20),
    "Wizard": lambda: Wizard("Wizard", 20),
}


def choose_command(player):  #选择命令
    return "defend" if player.poison > 0 else "fight"  #如果中毒，则防御，否则攻击


def simulate_one_fight(make_player, boss_template):  #模拟一场战斗
    start_new_game()  #开始新游戏
    player = make_player()
    boss = dict(boss_template)  # 创建一个boss的副本，避免修改原始模板

    round_num = 1
    while boss["hp"] > 0 and player.hp > 0 and round_num <= MAX_ROUNDS:
        apply_poison(player, boss, round_num)  #应用中毒效果
        if player.hp <= 0:
            break
        if choose_command(player) == "defend":
            defend(player, boss, round_num)  #防御
        else:
            fight(player, boss, round_num)  #攻击
        round_num += 1  #回合数加1  

    won = player.hp > 0 and boss["hp"] <= 0  #判断是否胜利
    winner = "player" if won else boss["name"]  #判断胜利者
    log_round(round_num, "end", 0, player.hp, boss["hp"], winner=winner)  #记录战斗结果
    return won, round_num


def run_simulation():
    if LOG_FILE.exists():  #如果战斗记录文件存在，则删除    
        LOG_FILE.unlink()  #删除战斗记录文件

    results = []  
    for boss in load_bosses():  #加载boss
        for cls_name, make_player in CLASSES.items():  #遍历职业
            wins = 0  #胜利次数
            total_rounds = 0  #总回合数
            
            with contextlib.redirect_stdout(io.StringIO()):
                for _ in range(FIGHTS_PER_MATCHUP):  #遍历每场战斗
                    won, rounds = simulate_one_fight(make_player, boss)  #模拟一场战斗
                    wins += won  #胜利次数加1
                    total_rounds += rounds  #总回合数加1
            results.append({
                "boss": boss["name"],  #boss名称
                "class": cls_name,  #职业名称
                "wins": wins,
                "games": FIGHTS_PER_MATCHUP,  #每场战斗的次数
                "win_rate": wins / FIGHTS_PER_MATCHUP,  #胜利率
                "avg_rounds": total_rounds / FIGHTS_PER_MATCHUP,  #平均回合数
            })
    return results  #返回结果


def print_summary(results):
    print(f"\n== Balance report ({FIGHTS_PER_MATCHUP} fights per matchup) ==")  #打印平衡报告
    print(f"{'Boss':<12}{'Class':<10}{'Win rate':<10}{'Avg rounds'}")  #打印boss名称，职业名称，胜利率，平均回合数
    for r in results:
        print(f"{r['boss']:<12}{r['class']:<10}"  #打印boss名称，职业名称
              f"{r['win_rate']*100:>5.0f}%    {r['avg_rounds']:>5.1f}")  #打印胜利率，平均回合数


def save_summary_csv(results):
    out = LOG_FILE.with_name("balance_summary.csv")  #创建一个文件
    with open(out, "w", newline="", encoding="utf-8") as f:  #打开文件      
        w = csv.DictWriter(f, fieldnames=["boss", "class", "wins", "games",
                                          "win_rate", "avg_rounds"])  #创建一个字典写入器
        w.writeheader()  #写入表头
        for r in results:  #遍历结果
            w.writerow(r)  #写入结果
    print(f"Saved {out.name}")  #打印保存的文件名


def save_win_rate_chart(results):
    labels = [f"{r['boss']}\n{r['class']}" for r in results]  #创建一个标签列表
    values = [r["win_rate"] * 100 for r in results]  #创建一个值列表
    colors = {"Dragon": "#C0392B", "Slime King": "#27AE60"}  #创建一个颜色列表
    bar_colors = [colors.get(r["boss"], "#888888") for r in results]  #创建一个条形颜色列表

    plt.figure(figsize=(7, 4))  #创建一个图形   
    plt.bar(labels, values, color=bar_colors)
    plt.axhline(50, color="#333333", linestyle="--", linewidth=1)  # 50% guide  
    plt.ylim(0, 100)  #设置y轴范围
    plt.ylabel("Win rate (%)")  #设置y轴标签
    plt.title(f"Player win rate by boss & class ({FIGHTS_PER_MATCHUP} fights each)")  #设置标题
    plt.tight_layout()  #自动调整子图之间的间距

    out = LOG_FILE.with_name("win_rate.png")  #创建一个文件
    plt.savefig(out)  #保存图形
    print(f"Saved {out.name}")  #打印保存的文件名


def main():
    results = run_simulation()  #运行模拟
    print_summary(results)  #打印总结
    save_summary_csv(results)  #保存总结csv
    save_win_rate_chart(results)  #保存胜率图


if __name__ == "__main__":
    main()  #运行主函数
