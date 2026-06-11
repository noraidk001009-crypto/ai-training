import random
options = ["rock", "paper", "scissors"]
def main():
    you, cpu = 0, 0
    print("Rock / Paper / Scissors\nBest of 3 - first to 2 wins!\n")
    while you < 2 and cpu < 2:
        raw = input("Your move (rock/paper/scissors, quit to stop): ")
        c = raw.strip().lower()
        if c == "quit": print("Bye!"); return
        move = ""
        if c in ("rock", "r"): move = "rock"
        elif c in ("paper", "p"): move = "paper"
        elif c in ("scissors", "s"): move = "scissors"
        if move == "": print("Invalid."); continue
        comp = random.choice(options); print("You:", move, "| Computer:", comp)
        if move == comp: print("Tie!")
        elif move == "rock" and comp == "scissors" or move == "scissors" and comp == "paper" or move == "paper" and comp == "rock":
            you = you + 1; print("You win!", you, "-", cpu)
        else: cpu = cpu + 1; print("CPU wins.", you, "-", cpu)
    if you > cpu: print("YOU WIN!", you, "-", cpu)
    else: print("CPU wins.", you, "-", cpu)
main()

# 第 1 行  import random
#   导入 random 模块，用来让电脑随机出拳（Day 10）
#
# 第 2 行  options = ["rock", "paper", "scissors"]
#   列表 list，存放三种出拳：石头 / 布 / 剪刀（Day 6）
#
# 第 3 行  def main():
#   定义 main 函数，主程序都写在里面（Day 8）
#
# 第 4 行  you, cpu = 0, 0
#   两个计分变量，玩家 you 和电脑 cpu，都从 0 开始（Day 2）
#
# 第 5 行  print("Rock / Paper / Scissors\n...")
#   打印游戏规则；\n 表示换行（Day 1 print）
#
# 第 6 行  while you < 2 and cpu < 2:
#   循环：双方都还没到 2 分就继续下一回合（Day 7 while，Day 4 and）
#
# 第 7 行  raw = input("Your move ...")
#   等待玩家键盘输入，raw 保存原始输入（Day 1 input）
#
# 第 8 行  c = raw.strip().lower()
#   去掉首尾空格并转小写，例如 "  Rock  " -> "rock"（Day 6）
#
# 第 9 行  if c == "quit": print("Bye!"); return
#   输入 quit 就打印 Bye! 并立刻结束 main 函数退出游戏（Day 4 if，Day 8 return）
#
# 第 10 行  move = ""
#   move 先设为空字符串，表示还没有合法出拳（Day 2 变量）
#
# 第 11 行  if c in ("rock", "r"): move = "rock"
#   输入 rock 或简写 r，move 设为 "rock"（Day 4 if，Day 6 in）
#
# 第 12 行  elif c in ("paper", "p"): move = "paper"
#   输入 paper 或 p，move 设为 "paper"（Day 4 elif）
#
# 第 13 行  elif c in ("scissors", "s"): move = "scissors"
#   输入 scissors 或 s，move 设为 "scissors"
#
# 第 14 行  if move == "": print("Invalid."); continue
#   输入无效就提示 Invalid.，跳过本轮回到 while 开头（Day 5 continue）
#
# 第 15 行  comp = random.choice(options); print(...)
#   random.choice 从列表随机选电脑出拳；再打印双方出拳（Day 10，Day 1 print）
#
# 第 16 行  if move == comp: print("Tie!")
#   双方出拳相同，平局（Day 4 if）
#
# 第 17 行  elif move == "rock" and comp == "scissors" or ...
#   石头赢剪刀、剪刀赢布、布赢石头，玩家赢这一回合（Day 4 and / or）
#
# 第 18 行  you = you + 1; print("You win!", you, "-", cpu)
#   玩家赢一局，you 加 1，打印当前比分（Day 2）
#
# 第 19 行  else: cpu = cpu + 1; print("CPU wins.", you, "-", cpu)
#   不是平局且玩家没赢，就是电脑赢，cpu 加 1（Day 4 else）
#
# 第 20 行  if you > cpu: print("YOU WIN!", you, "-", cpu)
#   循环结束，玩家分更高，宣布玩家获胜
#
# 第 21 行  else: print("CPU wins.", you, "-", cpu)
#   否则宣布电脑获胜
#
# 第 22 行  main()
#   调用 main()，程序从这里开始运行（Day 8 调用函数）
