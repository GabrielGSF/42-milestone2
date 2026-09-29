#! /usr/bin/python3

def print_garden_info(name: str, height: int, age: int) -> None:
    """Displays basic information from a plant"""
    print(
        "=== Welcome to My Garden ===\n"
        f"Plant: {name.capitalize()}\n"
        f"Height: {height}cm\n"
        f"Age: {age} days\n\n"
        "=== End of Program ==="
    )


if __name__ == "__main__":
    print_garden_info("rose", 25, 30)
