#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)
    edelweiss: Plant = Plant("Leontopodium nivale", 16, 759)
    rose.show()
    sunflower.show()
    cactus.show()
    edelweiss.show()


if __name__ == "__main__":
    main()
