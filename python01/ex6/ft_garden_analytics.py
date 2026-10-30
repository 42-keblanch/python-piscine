#!/usr/bin/env python3

PLANT_DEFAULT_HEIGHT = 0
PLANT_DEFAULT_AGE = 0


class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8) -> None:
        self._name: str = name
        self.set_height(height)
        self.set_age(age)
        self._growth_rate: float = growth_rate
        self._stats: Plant.Stats = self.Stats()

    class Stats:
        def __init__(self) -> None:
            self._nb_grow: int = 0
            self._nb_age: int = 0
            self._nb_show: int = 0

        def inc_nb_grow(self) -> None:
            self._nb_grow += 1

        def inc_nb_age(self) -> None:
            self._nb_age += 1

        def inc_nb_show(self) -> None:
            self._nb_show += 1

        def display(self) -> None:
            print(f"Stats: {self._nb_grow} grow, \
{self._nb_age} age, {self._nb_show} show")

    @classmethod
    def anonymous_plant(cls):
        return cls("Unknown plant", 0, 0)

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height: float = height
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
            self._age: int = age
        else:
            print(f"{self._name}: Error, age can't be negative")
            if hasattr(self, "_age"):
                print("Age update rejected")
            else:
                self._age = PLANT_DEFAULT_AGE
                print("Plant created with default age of 0")

    def get_stats(self) -> Stats:
        return self._stats

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._stats.inc_nb_show()

    def grow(self) -> None:
        self._height += self._growth_rate
        self._stats.inc_nb_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.inc_nb_age()

    def pass_one_day(self) -> None:
        self.age()
        self.grow()

    @staticmethod
    def is_over_a_year(days: int) -> bool:
        return days > 365


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8, color: str = "Purple") -> None:
        super().__init__(name, height, age, growth_rate)
        self._color: str = color
        self._is_blooming: bool = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet.")

    def bloom(self) -> None:
        self._is_blooming = True


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8, color: str = "Purple") -> None:
        super().__init__(name, height, age, growth_rate, color)
        self._seeds: int = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8, trunk_diameter: float = 10) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter
        self._stats: Tree.TreeStats = self.TreeStats()

    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._nb_shade: int = 0

        def inc_nb_shade(self) -> None:
            self._nb_shade += 1

        def display(self) -> None:
            super().display()
            print(f" {self._nb_shade} shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of \
{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide.")
        self._stats.inc_nb_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8,
                 harvest_season: str = "April") -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season: str = harvest_season
        self._nutrional_value: int = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutrional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutrional_value += 1


def plant_stats(plant: Plant) -> None:
    plant.get_stats().display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_over_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_over_a_year(400)}")

    print("\n=== Flower")
    rose: Flower = Flower("Rose", 15, 10, 8)
    rose.show()
    print(f"[statistics for {rose._name}]")
    plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print(f"[statistics for {rose._name}]")
    plant_stats(rose)

    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200, 365)
    oak.show()
    print(f"[statistics for {oak._name}]")
    plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak._name}]")
    plant_stats(oak)

    print("\n=== Seed")
    sunflower: Seed = Seed("Sunflower", 80, 45, 1.5, "Yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    for i in range(20):
        sunflower.pass_one_day()
    sunflower.bloom()
    sunflower.show()
    print(f"[statistics for {sunflower._name}]")
    plant_stats(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.anonymous_plant()
    anonymous.show()
    print(f"[statistics for {anonymous._name}]")
    plant_stats(anonymous)


if __name__ == "__main__":
    main()
