#!/usr/bin/env python3

PLANT_DEFAULT_HEIGHT = 0
PLANT_DEFAULT_AGE = 0


class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)
        self._growth_rate = growth_rate

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            if hasattr(self, "_height"):
                print("Height update rejected")
            else:
                self._height = PLANT_DEFAULT_HEIGHT
                print("Plant created with default height of 0")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            print(f"{self._name}: Error, age can't be negative")
            if hasattr(self, "_age"):
                print("Age update rejected")
            else:
                self._age = PLANT_DEFAULT_AGE
                print("Plant created with default age of 0")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age += 1

    def pass_one_day(self) -> None:
        self.age()
        self.grow()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8, color: str = "Purple") -> None:
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._is_blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet.")

    def bloom(self) -> None:
        self._is_blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8, trunk_diameter: float = 10) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of \
{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8,
                 harvest_season: str = "April") -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season
        self._nutrional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutrional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutrional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("Rose", 15, 10)
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200, 365)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5, 10, 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.pass_one_day()
    tomato.show()


if __name__ == "__main__":
    main()
