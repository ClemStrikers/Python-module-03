import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = \
            input("Enter new coordinates as floats in format 'x,y,z': ")
        parts: list[str] = user_input.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        valid: bool = True
        coords: list[float] = []
        for p in parts:
            try:
                coords.append(float(p))
            except ValueError as e:
                print(f"Error on parameter '{p}': {e}")
                valid = False
                break

        if valid:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_1: float = math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2)
    print(f"Distance to center: {round(dist_1, 4)}")

    print("\nGet a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()

    diff_x: float = pos2[0] - pos1[0]
    diff_y: float = pos2[1] - pos1[1]
    diff_z: float = pos2[2] - pos1[2]
    dist_2: float = math.sqrt(diff_x ** 2 + diff_y ** 2 + diff_z ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(dist_2, 4)}")


if __name__ == "__main__":
    main()
