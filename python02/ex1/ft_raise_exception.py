#!/usr/bin/env python3

MAX_TEMP: int = 40
MIN_TEMP: int = 0


def input_temperature(data: str) -> int:
    n_data: int = int(data)

    if n_data < MIN_TEMP:
        raise ValueError(f"{n_data}°C is too cold for plants\
 (min {MIN_TEMP}°C)")

    if n_data > MAX_TEMP:
        raise ValueError(f"{n_data}°C is too hot for plants\
 (max {MAX_TEMP}°C)")

    return n_data


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
    print("=== Garden Temperature Checker ===\n")

    data: str = "21"
    test_temperature(data)

    data = "abc"
    test_temperature(data)

    data = "-42"
    test_temperature(data)

    data = "100"
    test_temperature(data)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
