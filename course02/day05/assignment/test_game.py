import os
import sys


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dice
from character import Character, Warrior, Wizard



POISON_DAMAGE = 2


def simulate_fight(player, dragon_hp=50, max_rounds=1000):
    """Play out one fight silently and return the winner ("player" or "dragon").

    This mirrors the combat rules in combat.py (poison tick -> attack -> counter
    -> poison) without any printing or logging, so it is safe to run thousands
    of times for win-rate estimation.
    """
    rounds = 0
    while dragon_hp > 0 and player.hp > 0 and rounds < max_rounds:
        rounds += 1
        # Poison ticks at the start of the turn.
        if player.poison > 0:
            player.hp = max(0, player.hp - POISON_DAMAGE)
            player.poison -= 1
            if player.hp <= 0:
                break
        # The player always attacks in the simulation.
        if player.roll_d6() >= 4:
            attack = player.roll_d20()
            dragon_hp = max(0, dragon_hp - attack)
            if attack > 12 and dragon_hp > 0:
                counter = max(5, player.roll_d6() + player.roll_d6())
                player.hp = max(0, player.hp - counter)
                if player.roll_d6() >= 5:
                    player.poison += 3
    return "player" if player.hp > 0 and dragon_hp <= 0 else "dragon"


def win_rates(player_cls, trials=5000, dragon_hp=50):
    """Estimate (player_rate, dragon_rate) over many simulated fights."""
    player_wins = 0
    for _ in range(trials):
        player = player_cls(player_cls.__name__, 20)
        if simulate_fight(player, dragon_hp) == "player":
            player_wins += 1
    player_rate = player_wins / trials
    return player_rate, 1 - player_rate


def check_win_rates():
    for player_cls in (Warrior, Wizard):
        player_rate, dragon_rate = win_rates(player_cls)
        print(f"{player_cls.__name__}: win rate {player_rate:.1%} "
              f"| Dragon win rate {dragon_rate:.1%}")

        assert 0.0 <= player_rate <= 1.0
        assert 0.0 <= dragon_rate <= 1.0
        assert abs((player_rate + dragon_rate) - 1.0) < 1e-9
    print("check_win_rates passed")

if __name__ == "__main__":
    check_win_rates()


