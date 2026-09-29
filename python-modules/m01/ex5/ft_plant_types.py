#! /usr/bin/python3

class Plant:
    """Initialize a Plant instance."""
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def basic_show(self) -> str:
        return (f"{self.name}: "
                f"{self.height}cm, {self.age} days old ")


class Flower(Plant):
    """Initialize a Plant subclass"""
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        if not (self.bloomed):
            print(f"{self.name} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")
            self.bloomed = True
        print(f"{self.name} is blooming beutifully!")

    def show(self) -> None:
        print(f"{self.basic_show()}\n Color: {self.color}")
        self.bloom()


class Tree(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Produce shade - print name and size"""
        print(f'{self.name} provides {int(3.14 * self.trunk_diameter ** 2)} '
              f'square meters of shade\n')

    def show(self) -> None:
        print(f"{self.basic_show()}, {self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nut_value(self) -> None:
        """Get nutricional value"""
        print(f"{self.name} is rich in {self.nutritional_value}\n")

    def show(self) -> None:
        print(f"{self.basic_show()}, {self.harvest_season} harvest")
        self.nut_value()


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 15, 10, "red")
    # oak = Tree("oak", 500, 1825, 50),
    # tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C"),
    print("=== Flower")
    rose.show()
    rose.show()


if __name__ == "__main__":
    ft_plant_types()
