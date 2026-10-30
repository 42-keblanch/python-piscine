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


def main() -> None:
    rose: Plant = Plant("Rose", 15, 10)
    print("Plant created:", end=" ")
    rose.show()
    print()
    rose.set_height(25)
    print(f"Height updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print()
    rose.set_height(-25)
    rose.set_age(-30)
    print("\nCurrent state:", end=" ")
    rose.show()


if __name__ == "__main__":
    main()
