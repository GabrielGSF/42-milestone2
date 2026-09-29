#! /usr/bin/python3

class Plant:
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                day_grow: float
            ) -> None:

        self.name = name.capitalize()
        self.height = height
        self.age_days = age
        self.day_grow = day_grow
        self.total_grow = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def grow(self):
        self.height += self.day_grow
        self.total_grow += self.day_grow

    def age(self):
        self.age_days += 1


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plants = [
        Plant('rose', 25, 30, 0.8),
        Plant('oak', 200, 365, 1),
        Plant('cactus', 5, 90, 2),
        Plant('sunflower', 80, 45, 0.2),
        Plant('fern', 15, 120, 0.1)
    ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
