#! /usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize Plant Instance"""
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        """Print Plant information"""
        print(f'{self.name}: {self.height}cm, {self.age} days old')


def ft_garden_data() -> None:
    plants = [
        Plant('rose', 25, 30),
        Plant('sunflower', 80, 45),
        Plant('cactus', 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    ft_garden_data()
