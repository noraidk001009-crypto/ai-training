from assignment.fight_log import log_round

POISON_DAMAGE = 2


def fight(player, dragon_hp, round_num):
    damage = 0
    note = "miss"
    if player.roll_d6() >= 4:
        attack = player.roll_d20()
        damage = attack
        dragon_hp -= attack
        if dragon_hp < 0:
            dragon_hp = 0
        print("Hit! Dragon HP:", dragon_hp)
        note = "hit"
        if attack > 12 and dragon_hp > 0:
            counter = player.roll_d6() + player.roll_d6()
            if counter < 5:
                counter = 5
            player.hp -= counter
            if player.hp < 0:
                player.hp = 0
            print(f"Dragon counter-attacks for {counter}! Your HP: {player.hp}")
            note = "hit+counter"
            # A fierce counter can leave the player poisoned.
            if player.roll_d6() >= 5:
                player.poison += 3
                print("The dragon's fangs poison you for 3 turns!")
    else:
        print("Miss! The dragon does not counter-attack.")
    log_round(round_num, "fight", damage, player.hp, dragon_hp, note=note)
    return dragon_hp


def apply_poison(player, dragon_hp, round_num):
    """Deal poison damage at the start of a turn and log it. No-op when not poisoned."""
    if player.poison <= 0:
        return
    player.hp -= POISON_DAMAGE
    if player.hp < 0:
        player.hp = 0
    player.poison -= 1
    print(f"Poison bites for {POISON_DAMAGE}! Your HP: {player.hp} (poison turns left: {player.poison})")
    log_round(round_num, "poison", POISON_DAMAGE, player.hp, dragon_hp,
              note=f"{player.poison} turns left")


def defend(player, dragon_hp, round_num):
    cleared = 1 if player.poison > 0 else 0
    if cleared:
        player.poison -= 1
        print("You brace and shake off some venom.")
    else:
        print("You brace. Next hit hurts less (not implemented yet).")
    log_round(round_num, "defend", 0, player.hp, dragon_hp, note=f"cleared {cleared} poison")
