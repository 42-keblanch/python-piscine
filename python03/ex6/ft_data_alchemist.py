#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players: list[str] = ["sora", "Riku", "kairi", "Namine", "roxas",
                          "Xion", "axel", "Aqua", "ventus", "Terra"]
    only_cap_plrs: list[str] = [x for x in players if x == x.capitalize()]
    all_cap_plrs: list[str] = [x.capitalize() for x in players]

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_cap_plrs}")
    print(f"New list with only capitalized names: {only_cap_plrs}")

    scores: dict[str, int] = {x: (random.randint(5, 25) * 100)
                              for x in all_cap_plrs}
    score_avg: float = sum(scores.values()) / len(scores.values())

    print(f"Score dict: {scores}")
    print(f"Score average is {score_avg:.2f}")

    scrs_abv_avg: dict[str, int] = {x: y for x, y in scores.items()
                                    if y > score_avg}

    print(f"High scores: {scrs_abv_avg}")


if __name__ == "__main__":
    main()
