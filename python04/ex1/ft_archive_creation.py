#!/usr/bin/env python3

import sys
import typing


def print_archive(archive: str) -> None:
    print("---\n")
    print(archive)
    print("\n---")


def main(filename: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    # Opening given file
    print(f"Accessing file '{filename}'")
    try:
        # default open mode: r(ead)
        f: typing.IO[str] = open(filename)
    except IOError as ex:
        print(f"An error occured while opening file '{filename}': {ex}")
        return
    except Exception as ex:
        print(f"An unexpected error occured while opening the file \
'{filename}': {ex}")
        return

    # reading and printing the file
    # default read mode: r(ead)
    archive: str = f.read()
    print_archive(archive)

    # Closing the file
    # since io.close can possibly raise, use try/except block. Unlikely since
    # we only read.
    try:
        f.close()
    except Exception as ex:
        print(f"An unexpected error occured while closing the file: {ex}")
    else:
        print(f"File '{filename}' closed.")

    # Outputing the transformed data
    print("Transform data:")
    trans_arch: str = archive.replace('\n', '#\n')
    print_archive(trans_arch)

    # Getting new file name
    new_filename = input("Enter new file name (or empty to not save):")
    if not new_filename:
        print("Not saving data.")
        return

    # Opening new file
    try:
        f = open(new_filename, "w")
    except IOError as ex:
        print(f"An error occured while opening file '{new_filename}': {ex}")
        return
    except Exception as ex:
        print(f"An unexpected error occured while opening the file \
'{new_filename}': {ex}")
        return

    # Saving data to file
    print(f"Saving data to {new_filename}...")
    try:
        f.write(trans_arch)
    except IOError as ex:
        print(f"An error occured while writing to the file \
'{new_filename}': {ex}")
    except Exception as ex:
        print(f"An unexpected error occured while writing to the file \
'{new_filename}': {ex}")
    else:
        print(f"Data saved to {new_filename}.")
    finally:
        try:
            f.close()
        except Exception as ex:
            print(f"An unexpected error occured while closing the file: {ex}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No file given as parameter. \
Usage: python3 ft_ancient_text.py <filename>")
    else:
        main(sys.argv[1])
