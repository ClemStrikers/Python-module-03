import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    args: list[str] = sys.argv[1:]

    for arg in args:
        if ":" not in arg:
            print(f"Error- invalid parameter '{arg}'")
            continue

        parts: list[str] = arg.split(":")
        item: str = parts[0]
        raw_val: str = parts[1]

        if item in inventory.keys():
            print(f"Redundant item '{item}'- discarding")
            continue

        try:
            val: int = int(raw_val)
            inventory[item] = val
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    if len(inventory) == 0:
        return

    print(f"Got inventory: {inventory}")

    items_list: list[str] = list(inventory.keys())
    print(f"Item list: {items_list}")

    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {len(items_list)} items: {total_qty}")

    for item in items_list:
        qty: int = inventory[item]
        percentage: float = round((qty / total_qty) * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant: str = items_list[0]
    least_abundant: str = items_list[0]

    for item in items_list:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant} with quantity "
          f"{inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} with quantity "
          f"{inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
