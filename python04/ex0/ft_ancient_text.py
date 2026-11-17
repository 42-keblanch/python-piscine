#!/usr/bin/env python3

import sys
import typing


def main(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        # default open mode: r(ead)
        f: typing.IO[str] = open(filename)
    except IOError as ex:
        print(f"An error occured while opening file '{filename}': {ex}")
        return
    except Exception as ex:
        print(f"An unexpected error occured while opening the file: {ex}")
        return

    print("---\n")
    # default read mode: r(ead)
    print(f.read())
    print("\n---")
    # since io.close can possibly raise, use try/except block. Unlikely since
    # we only read.
    try:
        f.close()
    except Exception as ex:
        print(f"An unexpected error occured while closing the file: {ex}")
    else:
        print(f"File '{filename}' closed.")


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print("No file given as parameter. \
Usage: python3 ft_ancient_text.py <filename>")
