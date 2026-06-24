while True:
    try:
        n = int(input("Number: "))
        break
    except ValueError:
        print("Please type a number.")