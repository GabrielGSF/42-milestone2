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


def ft_week_growth(plant: Plant) -> None:
    day = 1
    plant.total_grow = 0
    while (day <= 7):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()
        day += 1
    print(f"Growth this week: {plant.total_grow:.1f}cm\n")


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    plants = [
        Plant('rose', 25, 30, 0.8),
        Plant('sunflower', 80, 45, 1),
        Plant('cactus', 15, 120, 0.2)
    ]
    for plant in plants:
        plant.show()
        ft_week_growth(plant)


if __name__ == "__main__":
    ft_plant_growth()
