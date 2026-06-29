def clamp_hp(hp):
    return max(0, hp)

def check_clamp():
    assert clamp_hp(-5) == 0
    assert clamp_hp(10) == 10
    print("All checks passed.")

check_clamp()
