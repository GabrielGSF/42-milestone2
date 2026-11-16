import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        values: list[float] = []
        for part in parts:
            try:
                values.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                break
        else:
            return (values[0], values[1], values[2])


def calc_distance(
    set1: tuple[float, float, float],
    set2: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (set2[0] - set1[0]) ** 2
        + (set2[1] - set1[1]) ** 2
        + (set2[2] - set1[2]) ** 2
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    set1 = get_player_pos()
    print(f"Got a first tuple: {set1}")
    print(f"It includes: X={set1[0]}, Y={set1[1]}, Z={set1[2]}")
    distance1 = calc_distance((0.0, 0.0, 0.0), set1)
    print(f"Distance to center: {round(distance1, 4)}\n")

    print("Get a second set of coordinates")
    set2 = get_player_pos()
    distance2 = calc_distance(set2, set1)
    print(
        f"Distance between the 2 sets of coordinates: {round(distance2, 4)}"
    )
