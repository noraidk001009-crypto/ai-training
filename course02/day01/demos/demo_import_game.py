"""Tiny multi-file pattern — expand this idea."""
from player import Player
from enemies import Dragon

def main():
    hero = Player(name="Nora", hp=20)
    boss = Dragon(hp=15)
    print(hero)
    print(boss)

if __name__ == "__main__":
    main()
