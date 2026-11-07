#! /usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(wilting: bool) -> None:
    if wilting:
        raise PlantError("The tomato is wilting!")


def check_water(tank_level: int) -> None:
    if tank_level <= 0:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        check_water(-10)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        check_plant(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo")
    test_custom_errors()
