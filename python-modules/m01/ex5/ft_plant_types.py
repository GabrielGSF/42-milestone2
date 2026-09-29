#! /usr/bin/python3

class Plant:
    """Initialize a Plant instance."""
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def basic_show(self) -> str:
        return (f"{self.name}: "
                f"{self.height:.1f}cm, {self.age} days old ")


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
        else:
            print(f"{self.name} is blooming beutifully!")

    def show(self) -> None:
        print(f"{self.basic_show()}\n Color: {self.color}")


class Tree(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Produce shade - print name and size"""
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm "
              f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        print(f"{self.basic_show()}\n "
              f"Trunk diameter: {self.trunk_diameter:.1f}cm")
        self.produce_shade()


class Vegetable(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season.capitalize()
        self.nutritional_value = nutritional_value

    def grow(self, days: int, grow_rate: float, nut_rate: float) -> None:
        """Get nutricional value"""
        print(f"[make {self.name} grow and age for {days} days]")
        day = 1
        while day <= days:
            self.nutritional_value += nut_rate
            self.age += 1
            self.height += grow_rate
            day += 1

    def show(self) -> None:
        print(f"{self.basic_show()}\n "
              f"Harvest season: {self.harvest_season}\n "
              f"Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 15, 10, "red")
    oak = Tree("oak", 200, 365, 5)
    tomato = Vegetable("tomato", 5, 10, "april", 0)
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    rose.bloom()
    print()
    print("=== Tree")
    oak.show()
    print()
    print("=== Vegetable")
    tomato.show()
    tomato.grow(20, 2.1, 1)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
