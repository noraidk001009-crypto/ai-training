class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.poison_uses = 1

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def is_alive(self):
        return self.hp > 0

hero = Player("Nora", 20)
hero.take_damage(5)
print(hero.name, "HP:", hero.hp)
