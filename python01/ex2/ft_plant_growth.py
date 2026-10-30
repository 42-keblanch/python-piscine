#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = .8) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate

    def get_height(self) -> float:
        return self._height

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age += 1

    def pass_one_day(self) -> None:
        self.age()
        self.grow()


def main() -> None:
    rose: Plant = Plant("Rose", 25, 30)
    plant_init_size = rose.get_height()
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.pass_one_day()
        rose.show()
    print(f"Growth this week: {(rose.get_height() - plant_init_size):.1f}cm")


if __name__ == "__main__":
    main()
