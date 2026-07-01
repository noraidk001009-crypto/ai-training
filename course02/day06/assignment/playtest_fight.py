import json
import random
from pathlib import Path


def load_bosses():
    with open(Path(__file__).parent / "bosses.json") as f:
        return json.load(f)


def fight(boss, seed):
    rng = random.Random(seed)
    player_hp, player_atk = 20, 5
    boss_hp = boss["hp"]
    turns = 0
    while player_hp > 0 and boss_hp > 0:
        turns += 1
        boss_hp -= player_atk + rng.randint(-1, 1)
        if boss_hp <= 0:
            break
        player_hp -= boss["atk"] + rng.randint(-1, 1)
    won = boss_hp <= 0
    return won, turns, max(player_hp, 0)


for boss in load_bosses():
    print(f"== {boss['name']} (hp {boss['hp']}, atk {boss['atk']}) ==")
    for i in range(1, 3):
        won, turns, hp_left = fight(boss, seed=i)
        outcome = "WIN" if won else "LOSE"
        print(f"  Fight {i}: {outcome} in {turns} turns, player HP left {hp_left}")
