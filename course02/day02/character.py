import dice

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def roll_d6(self):
        return dice.roll_d6()

    def roll_d20(self):
        return dice.roll_d20()


class Warrior(Character):
    def roll_d20(self):
        return dice.roll_d20() + 5


class Wizard(Character):
    def roll_d6(self):
        return dice.roll_d6() + 1
