import os

from combat import fight, defend, apply_poison
from character import Warrior, Wizard
from save import save_game, load_game, delete_save
from assignment.fight_log import log_round, start_new_game
from assignment.boss_loader import choose_boss


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def choose_player():
    print("Choose your class: warrior, wizard")
    while True:
        choice = input("class> ").lower()
        if choice == "warrior":
            return Warrior("Warrior", 20)
        elif choice == "wizard":
            return Wizard("Wizard", 20)
        else:
            print("Unknown class")


def start_game():
    """Auto-load a saved fight, or offer to start a new game."""
    saved = load_game()
    if saved is None:
        print("No save found. Starting a new game!")
        return choose_player(), choose_boss()

    player, boss = saved
    print(f"Save found: {player.name} {player.hp} HP vs {boss['name']} {boss['hp']} HP.")
    if input("Continue (c) or new game (n)? ").lower() == "n":
        print("Starting a new game!")
        return choose_player(), choose_boss()
    print("Continuing your saved fight!")
    return player, boss


def main():
    clear_screen()
    player, boss = start_game()
    start_new_game()
    print(f"{player.name} enters the {boss['name']} fight! Commands: fight, defend, save, quit")
    round_num = 1
    while boss["hp"] > 0 and player.hp > 0:
        # Poison ticks at the start of each turn (and is logged inside apply_poison).
        apply_poison(player, boss, round_num)
        if player.hp <= 0:
            break
        cmd = input("> ").lower()
        if cmd == "fight":
            fight(player, boss, round_num)
        elif cmd == "defend":
            defend(player, boss, round_num)
        elif cmd == "save":
            save_game(player, boss)
            continue
        elif cmd == "quit":
            save_game(player, boss)
            print("Saved and quit. See you next time!")
            return
        else:
            print("Unknown command")
            continue
        round_num += 1
    if player.hp <= 0:
        winner = boss["name"]
        print(f"You died! The {boss['name']} wins.")
    else:
        winner = "player"
        print(f"You win! {boss['name']} is defeated.")
    log_round(round_num, "end", 0, player.hp, boss["hp"], winner=winner)
    delete_save()


if __name__ == "__main__":
    main()
