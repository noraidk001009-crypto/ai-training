import dice


def fight(dragon_hp):
    if dice.roll_d6() >= 4:
        dragon_hp -= dice.roll_d20()
        if dragon_hp < 0:
            dragon_hp = 0
        print("Hit! Dragon HP:", dragon_hp)
    else:
        print("Miss!")
    return dragon_hp


def defend():
    print("You brace. Next hit hurts less (not implemented yet).")