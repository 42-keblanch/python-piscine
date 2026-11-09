#!/usr/bin/env python3

import sys


def main(arguments: list[str]) -> None:
    print("=== Command Quest ===")
    try:
        l_len: int = len(arguments)

        print(f"Program name: {arguments[0]}")

        if l_len == 1:
            print("No arguments provided!")
        else:
            print(f"Arguments received: {l_len - 1}")
            for i in range(1, l_len):
                print(f"Argument {i}: {arguments[i]}")

        print(f"Total arguments: {l_len}")
    except Exception as ex:
        print(f"An unexpected error happened: {ex}")


if __name__ == "__main__":
    main(sys.argv)
