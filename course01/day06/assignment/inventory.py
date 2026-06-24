inventory = ["sword", "potion"]


def add_item(item):
    inventory.append(item)


def list_all():
    print("Bag:", inventory)
    for item in inventory:
        print("-", item)


def has_item(item):
    return item in inventory


add_item("shield")
list_all()

if has_item("key"):
    print("You have the key!")
else:
    print("No key yet.")
