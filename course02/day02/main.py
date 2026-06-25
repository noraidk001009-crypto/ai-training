from combat import fight, defend
from character import Warrior, Wizard


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


def main():
    player = choose_player()
    dragon_hp = 50
    print(f"{player.name} enters the dragon fight! Commands: fight, defend, quit")
    while dragon_hp > 0 and player.hp > 0:
        cmd = input("> ").lower()
        if cmd == "fight":
            dragon_hp = fight(player, dragon_hp)
        elif cmd == "defend":
            defend()
        elif cmd == "quit":
            break
        else:
            print("Unknown command")
    if player.hp <= 0:
        print("You died! The dragon wins.")
    else:
        print("You win!")


if __name__ == "__main__":
    main()
