def roll_dice(sides):
    import random
    return random.randint(1, sides)

def attack_roll(bonus=0):
    return roll_dice(20) + bonus

def apply_damage(hp, damage):
    return max(0, hp - damage)

print("D6 roll:", roll_dice(6))
print("Attack roll (+3):", attack_roll(3))
print("HP after 4 damage:", apply_damage(10, 4))