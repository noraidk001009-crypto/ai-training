import os

from combat import fight, defend, apply_poison
from character import Warrior, Wizard
from save import save_game, load_game, delete_save
from assignment.fight_log import log_round, start_new_game


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
        return choose_player(), 50

    player, dragon_hp = saved
    print(f"Save found: {player.name} {player.hp} HP vs Dragon {dragon_hp} HP.")
    if input("Continue (c) or new game (n)? ").lower() == "n":
        print("Starting a new game!")
        return choose_player(), 50
    print("Continuing your saved fight!")
    return player, dragon_hp


def main():
    clear_screen()
    player, dragon_hp = start_game()
    start_new_game()  
    print(f"{player.name} enters the dragon fight! Commands: fight, defend, save, quit")
    round_num = 1
    while dragon_hp > 0 and player.hp > 0:
        # Poison ticks at the start of each turn (and is logged inside apply_poison).
        apply_poison(player, dragon_hp, round_num)
        if player.hp <= 0:
            break
        cmd = input("> ").lower()
        if cmd == "fight":
            dragon_hp = fight(player, dragon_hp, round_num)
        elif cmd == "defend":
            defend(player, dragon_hp, round_num)
        elif cmd == "save":
            save_game(player, dragon_hp)
            continue
        elif cmd == "quit":
            save_game(player, dragon_hp)
            print("Saved and quit. See you next time!")
            return
        else:
            print("Unknown command")
            continue
        round_num += 1
    if player.hp <= 0:
        winner = "dragon"
        print("You died! The dragon wins.")
    else:
        winner = "player"
        print("You win!")
    log_round(round_num, "end", 0, player.hp, dragon_hp, winner=winner)
    delete_save()


if __name__ == "__main__":
    main()
