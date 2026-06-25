def fight(player, dragon_hp):
    if player.roll_d6() >= 4:
        attack = player.roll_d20()
        dragon_hp -= attack
        if dragon_hp < 0:
            dragon_hp = 0
        print("Hit! Dragon HP:", dragon_hp)
        if attack > 12 and dragon_hp > 0:
            counter = player.roll_d6() + player.roll_d6()
            if counter < 5:
                counter = 5
            player.hp -= counter
            if player.hp < 0:
                player.hp = 0
            print(f"Dragon counter-attacks for {counter}! Your HP: {player.hp}")
    else:
        print("Miss! The dragon does not counter-attack.")
    return dragon_hp


def defend():
    print("You brace. Next hit hurts less (not implemented yet).")
