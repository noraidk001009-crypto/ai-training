inventory = ["sword", "potion"]


def add_item(item):
    inventory.append(item)


def list_all():
    print("Bag:", inventory)
    for item in inventory:
        print("-", item)


add_item("shield")
list_all()

answer = input("Do you have the key? (yes/no): ").strip().lower()
if answer in ("yes", "y"):
    add_item("key")
    print("Key added to your bag!")
elif answer in ("no", "n"):
    print("No key for now.")
else:
    print("Please answer yes or no.")

list_all()

if "key" in inventory:
    print("You have a key!")
else:
    print("You do not have a key.")
