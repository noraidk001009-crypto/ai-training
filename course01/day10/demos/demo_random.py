import random
loot = ["common", "rare", "legendary"]
for _ in range(5):
    print("Drop:", random.choice(loot))
