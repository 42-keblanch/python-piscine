#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    input_ok: bool = False
    while not input_ok:
        user_input: str = input("Enter new coordinates as\
 floats in format 'x,y,z': ")
        if (user_input.count(',') != 2):
            print("Invalid format")
            continue
        tmp: list[str, str, str]



if __name__ == "__main__":
    main()
