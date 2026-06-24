class Player:
    def __init__(name, hp):  # BUG: missing self
        self.name = name
        self.hp = hp

p = Player("Nora", 10)
print(p.hp)
