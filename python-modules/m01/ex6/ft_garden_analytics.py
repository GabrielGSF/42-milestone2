#! /usr/bin/python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age
        self._stats = self.Stats()

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def add_grow(self, growth: float) -> None:
        self._stats.record_grow()
        self.height += growth

    def add_age(self, days: int) -> None:
        self._stats.record_age()
        self.age += days

    def show_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def check_age(age_days: int) -> bool:
        if (age_days >= 365):
            return True
        else:
            return False

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        if not (self.bloomed):
            self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.bloomed):
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self, seeds: int = 0) -> None:
        self.seeds = seeds
        super().bloom()

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    _stats: Stats

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm "
              f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")

    print("\n=== Flower")
    rose = Flower("rose", 15, 10, 'red')
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.add_grow(8)
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.add_grow(30)
    sunflower.add_age(20)
    sunflower.bloom(42)
    sunflower.show()
    display_stats(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    ft_garden_analytics()
