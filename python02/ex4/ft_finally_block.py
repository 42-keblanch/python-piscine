#!/usr/bin/env python3

plants: list[str] = ["Tomato",
                     "Lettuce",
                     "Carrots"
                     ]


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError("Invalid plant name to water: '" + plant_name + "'")
    else:
        print(f"Watering {plant_name}: [OK]")


def watering_system() -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as ex:
        print(f"Caught PlantError: {ex}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering systems")


def main() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    watering_system()

    print("\nTesting invalid plants...")
    plants[1] = "lettuce"
    watering_system()

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
