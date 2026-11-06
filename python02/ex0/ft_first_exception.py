#!/usr/bin/env python3

def input_temperature(data: str) -> int:
    return int(data)


def test_temperature(data: str) -> None:
    print(f"Input data is '{data}'")
    try:
        n_data = input_temperature(data)
    except ValueError as ex:
        print(f"Caught input_temperature error: {ex}\n")
    except Exception as ex:
        print(f"Unkown error: {ex}\n")
    else:
        print(f"Temperature is now {n_data}°C\n")


def main() -> None:
    print("=== Garden Temperature ===\n")

    data: str = "25"
    test_temperature(data)

    data = "abc"
    test_temperature(data)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
