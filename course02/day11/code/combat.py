import dice

from assignment.fight_log import log_round

POISON_DAMAGE = 2


def fight(player, boss, round_num):
    """One attack round against the loaded boss. Mutates boss["hp"]."""
    damage = 0
    note = "miss"
    if player.roll_d6() >= 4:
        attack = player.roll_d20()
        damage = attack
        boss["hp"] -= attack
        if boss["hp"] < 0:
            boss["hp"] = 0
        print(f"Hit! {boss['name']} HP:", boss["hp"])
        note = "hit"
        if attack > 12 and boss["hp"] > 0:
            counter = boss["atk"] + dice.roll_d6()
            player.hp -= counter
            if player.hp < 0:
                player.hp = 0
            print(f"{boss['name']} counter-attacks for {counter}! Your HP: {player.hp}")
            note = "hit+counter"
            if dice.roll_d6() >= 3:
                player.poison += 2
                print(f"The {boss['name']}'s strike poisons you for 3 turns!")
    else:
        print(f"Miss! The {boss['name']} does not counter-attack.")
    log_round(round_num, "fight", damage, player.hp, boss["hp"], note=note)
    return boss["hp"]


def apply_poison(player, boss, round_num):
    """Deal poison damage at the start of a turn and log it. No-op when not poisoned."""
    if player.poison <= 0:
        return
    player.hp -= POISON_DAMAGE
    if player.hp < 0:
        player.hp = 0
    player.poison -= 1
    print(f"Poison bites for {POISON_DAMAGE}! Your HP: {player.hp} (poison turns left: {player.poison})")
    log_round(round_num, "poison", POISON_DAMAGE, player.hp, boss["hp"],
              note=f"{player.poison} turns left")


def defend(player, boss, round_num):
    cleared = 1 if player.poison > 0 else 0
    if cleared:
        player.poison -= 1
        print("You brace and shake off some venom.")
    else:
        print("You brace. Next hit hurts less (not implemented yet).")
    log_round(round_num, "defend", 0, player.hp, boss["hp"], note=f"cleared {cleared} poison")
