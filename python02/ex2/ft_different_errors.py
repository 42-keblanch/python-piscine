#!/usr/bin/env python3

def op_value_error() -> int:
    return int("abc")


def op_zero_division() -> int:
    return int(1 / 0)


def op_file_not_found() -> int:
    f = open("/non/existant/file", "r")
    f.close()
    return 1


def op_type_error() -> int:
    return "abc" + 3


def op_ok() -> int:
    return 1


def garden_operations(op: int) -> None:
    operations = [op_value_error,
                  op_zero_division,
                  op_file_not_found,
                  op_type_error,
                  op_ok
                  ]

    try:
        operations[op]()
    except ValueError as ex:
        print(f"Caught ValueError: {ex}")
    except ZeroDivisionError as ex:
        print(f"Caught ZeroDivisionError: {ex}")
    except FileNotFoundError as ex:
        print(f"Caught FileNotFoundError: {ex}")
    except TypeError as ex:
        print(f"Caught TypeError: {ex}")
    else:
        print("Operation completed successfully")


def main() -> None:
    print("=== Garden Error Types Demo ===")

    print("Testing operation 0...")
    garden_operations(0)

    print("Testing operation 1...")
    garden_operations(1)

    print("Testing operation 2...")
    garden_operations(2)

    print("Testing operation 3...")
    garden_operations(3)

    print("Testing operation 4...")
    garden_operations(4)

    print("\nAll error types tested succesfully!")


if __name__ == "__main__":
    main()
