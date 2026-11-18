import sys


def parse_input(args: list[str]) -> dict[str, int]:
    inv: dict[str, int] = {}
    for arg in args:
        item = arg.split(":")
        if (len(item) != 2) or item[0] == "":
            print(f"Error - invalid parameter '{arg}'")
            continue
        key = item[0]
        try:
            value = int(item[1])
            if value < 0:
                raise ValueError("quantity cannot be negative")
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue
        if key in inv:
            print(f"Redundant item '{key}' - discarding")
        else:
            inv.update({key: value})
    return inv


if __name__ == '__main__':
    print("=== Inventory System Analysis ===")

    inventory = parse_input(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    sum_vals = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {sum_vals}")

    if sum_vals > 0:
        for item in item_list:
            item_percent = round((inventory[item] / sum_vals)*100, 1)
            print(f"Item {item} represents {item_percent}%")

    if inventory:
        most = item_list[0]
        least = item_list[0]
        for item in item_list:
            if inventory[item] > inventory[most]:
                most = item
            if inventory[item] < inventory[least]:
                least = item
        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")
