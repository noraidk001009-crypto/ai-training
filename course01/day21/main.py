import random
def roll_d6():
    return random.randint(1, 6)

def main():
    print("Welcome to the game!")
    print("Type 'fight' to fight the dragon, 'defend' to block (limited uses), or 'quit' to quit.")
    dragon_hp = 7
    loss_count = 0
    poison_active = False
    MAX_POISON_USES = 3
    poison_uses_left = MAX_POISON_USES
    MAX_DEFENSE_USES = 2
    defense_uses_left = MAX_DEFENSE_USES
    while True:
        command = input("> ").lower()
        if command in ["fight", "FIGHT", "Fight","f","F"]:
            print(f"You fight the dragon! (Dragon HP: {dragon_hp})")
            print("You roll the dice to choose how many chance you have to fight.")
            your_roll = roll_d6()
            if poison_active:
                your_roll += 1
                poison_active = False
                print("Poison effect applied! This roll is +1.")
            dragon_roll = roll_d6()
            print(f"You rolled {your_roll}, the dragon rolled {dragon_roll}.")

            if your_roll > dragon_roll:
                dragon_hp -= 1
                print(f"You hit the dragon! Dragon HP: {dragon_hp}")
                if dragon_hp <= 0:
                    print("You defeated the dragon! You win the game!")
                    break
            elif your_roll < dragon_roll:
                loss_count += 1
                print(f"You lose the fight! (Losses: {loss_count}/4)")
                if loss_count > 3:
                    print("You have lost to the dragon too many times. Game over!")
                    break
            else:
                print("It's a tie! No damage dealt.")
        elif command in ["poison", "POISON", "Poison","p","P"]:
            if poison_uses_left <= 0:
                print("No poison left! You can't use poison anymore.")
                continue
            if poison_active:
                print("Poison is already active for your next roll.")
                continue
            poison_active = True
            poison_uses_left -= 1
            print(f"You use poison! Next dice roll will be +1. (Poison left: {poison_uses_left}/{MAX_POISON_USES})")
        elif command in ["defend", "DEFEND", "Defend", "d", "D"]:
            if defense_uses_left <= 0:
                print("No defense left! You can't defend anymore.")
                continue
            defense_uses_left -= 1
            print(f"You brace for the dragon's attack! (Defense left: {defense_uses_left}/{MAX_DEFENSE_USES})")
            your_roll = roll_d6()
            dragon_roll = roll_d6()
            print(f"You rolled {your_roll}, the dragon rolled {dragon_roll}.")

            if your_roll > dragon_roll:
                print("You blocked the dragon! No damage to either side.")
            elif your_roll < dragon_roll:
                print("The dragon strikes, but you hold your ground! (Does not count as a loss.)")
            else:
                print("It's a standoff! No one takes damage.")
        elif command == "quit":
            print("You quit the game.")
            break
        else:
            print("Invalid input. Please type 'fight', 'defend', 'poison', or 'quit'.")
            continue
main()