def check_hp(hp):
    return hp > 0  # BUG: should allow 0

assert check_hp(0)
print("ok")
