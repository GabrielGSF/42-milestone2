#! /usr/bin/python3

class Plant:
    def __init__(self, name: str) -> None:
        """Initialize Plant Instance"""
        self.name = name.capitalize()
        self.__height = 15
        self.__age = 10
        print("Plant created: ", end='')

    def get_height(self) -> float:
        """Returns plant height"""
        return self.__height

    def get_age(self) -> int:
        """Returns plant age"""
        return self.__age

    def set_height(self, height: float) -> None:
        """Set plant height"""
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative: {height}cm")
            print("Height update [REJECTED]")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set plant age"""
        if (age < 0):
            print(f"{self.name}: Error, age can't be negative: {age} days")
            print("Age upadate [REJECTED]")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def show(self) -> None:
        print(f"{self.name}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant('rose')
    plant.show()
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-27)
    plant.set_age(-15)
    print()
    print("Current state: ", end='')
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
