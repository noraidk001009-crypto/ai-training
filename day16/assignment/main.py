from game_logic import roll_d6


def main():
    print("=== Dice Roller ===")
    count = input("How many dice to roll? ").strip()
    try:
        n = int(count) if count else 1
    except ValueError:
        print("Invalid input. I'll roll 1 dice for you.")
        n = 1
    n = max(1, n)

    rolls = [roll_d6() for _ in range(n)]
    print("Rolls:", rolls)
    print("Total:", sum(rolls))


if __name__ == "__main__":
    main()
