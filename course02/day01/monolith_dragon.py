"""Refactored — uses dice.py and combat.py."""
from combat import fight, defend


def main():
    player_hp = 20
    dragon_hp = 50
    print("Dragon fight! Commands: fight, defend, quit")
    while dragon_hp > 0 and player_hp > 0:
        cmd = input("> ").lower()
        if cmd == "fight":
            dragon_hp = fight(dragon_hp)
        elif cmd == "defend":
            defend()
        elif cmd == "quit":
            break
        else:
            print("Unknown command")
    print("You win!")


if __name__ == "__main__":
    main()
