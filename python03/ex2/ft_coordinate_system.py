#!/usr/bin/env python3

import math


# type Vec3 = tuple[float, float, float]
Vec3 = tuple[float, float, float]


class PositionParseError(Exception):
    pass


def dist(v1: Vec3, v2: Vec3) -> float:
    x: float = v2[0] - v1[0]
    y: float = v2[1] - v1[1]
    z: float = v2[2] - v1[2]
    x2: float = x * x
    y2: float = y * y
    z2: float = z * z
    return math.sqrt(x2 + y2 + z2)


def to_float(usr_str: str) -> float:
    try:
        ret: float = float(usr_str)
    except ValueError as ex:
        print(f"Error on parameter '{usr_str}': {ex}")
        raise PositionParseError
    except Exception as ex:
        print(f"Unexpected eror: {ex}")
        raise PositionParseError
    else:
        return ret


def extract_pos(usr_pos: list[str]) -> Vec3:
    x: float = to_float(usr_pos[0])
    y: float = to_float(usr_pos[1])
    z: float = to_float(usr_pos[2])
    position: Vec3 = (x, y, z)
    return position


def get_player_pos() -> Vec3:
    while 1:
        user_input: str = input("Enter new coordinates as\
 floats in format 'x,y,z': ")
        if (user_input.count(',') != 2):
            print("Invalid syntax")
            continue
        try:
            position: Vec3 = extract_pos(user_input.split(','))
        except PositionParseError:
            continue
        except Exception as ex:
            print(f"Unexpected eror: {ex}")
            continue
        else:
            return position


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    pos1: Vec3 = get_player_pos()
    print(f"Got a first tuple: ({pos1[0]:.1f},\
 {pos1[1]:.1f}, {pos1[2]:.1f})")
    print(f"It includes: X={pos1[0]:.1f},\
 Y={pos1[1]:.1f}, Z={pos1[2]:.1f}")
    print(f"Distance to center: {dist((0, 0, 0), pos1):.4f}")

    print("\nGet a second set of coordinates")
    pos2: Vec3 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates:\
 {dist(pos2, pos1):.4f}")


if __name__ == "__main__":
    main()
