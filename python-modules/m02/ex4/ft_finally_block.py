#! /usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    try:
        print("Testing valid plants...")
        print("Opening watering system")
        valid_names = ("Tomato", "Lettuce", "Carrots")
        for name in valid_names:
            water_plant(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n"
              f".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    try:
        print("Testing invalid plants...")
        print("Opening watering system")
        invalid_names = ("Tomato", "lettuce", "carrot")
        for name in invalid_names:
            water_plant(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n"
              f".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
