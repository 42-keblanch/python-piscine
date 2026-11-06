#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant_error() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as ex:
        print(f"Caught PlantError: {ex}")


def test_water_error() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as ex:
        print(f"Caught WaterError: {ex}")


def test_garden_errors() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as ex:
        print(f"Caught GardenError: {ex}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as ex:
        print(f"Caught GardenError: {ex}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    test_plant_error()

    print("\nTesting WaterError...")
    test_water_error()

    print("\nTesting catching all garden errors...")
    test_garden_errors()

    print("\nAll custom error types work correctly")


if __name__ == "__main__":
    main()
