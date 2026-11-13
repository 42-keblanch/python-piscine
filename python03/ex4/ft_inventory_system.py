#!/usr/bin/env python3

import sys


def parse_inventory(items: list[str]) -> dict[str, int]:
    invt: dict[str, int] = {}
    for item in items:
        if item.count(':') != 1:
            print(f"Error - invalid parameter '{item}'")
            continue
        pair: list[str] = item.split(':')
        if pair[0] in invt:
            print(f"Redundant item '{pair[0]}' - discarding")
            continue
        try:
            if (int(pair[1]) < 1):
                raise ValueError("Quantity cannot be less than 1")
            invt.update({pair[0]: int(pair[1])})
        except ValueError as ex:
            print(f"Quantity error for '{pair[0]}': {ex}")
            continue
        except Exception as ex:
            print(f"Unexpected error while parsing: {ex}")
            continue
    return invt


def main(args: list[str]) -> None:
    print("=== Inventory System Analysis ===")

    hi_key: str = "No items in inventory"
    hi_val: int = 0
    lo_key: str = "No items in inventory"
    lo_val: int = 0
    args.pop(0)
    invt: dict[str, int] = parse_inventory(args)
    invt_keys: list[str] = list(invt.keys())

    print(f"Got inventory: {invt}")
    print(f"Item list: {invt_keys}")
    print(f"total quantity of the {len(invt.keys())}\
 items: {sum(invt.values())}")

    for key in invt_keys:
        if invt[key] > hi_val:
            hi_val = invt[key]
            hi_key = key
        if lo_val == 0 or invt[key] < lo_val:
            lo_val = invt[key]
            lo_key = key
        print(f"Item {key} represents\
 {(invt[key] * 100 / sum(invt.values())):.1f}%")

    print(f"Item most aboundant: {hi_key} with quantity {hi_val}")
    print(f"Item least aboundant: {lo_key} with quantity {lo_val}")

    invt.update({"magic_item": 1})
    print(f"Updated inventory: {invt}")


if __name__ == "__main__":
    main(sys.argv)
