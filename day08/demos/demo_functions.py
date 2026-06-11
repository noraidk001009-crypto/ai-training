def greet(name):
    return f"Hello, {name}!"

def roll_d6():
    import random
    return random.randint(1, 6)

print(greet("Nora"))
print("Roll:", roll_d6())
