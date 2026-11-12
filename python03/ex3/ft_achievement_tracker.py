#!/usr/bin/env python3

import random


p1_name: str = "Sora"
p2_name: str = "Riku"
p3_name: str = "Kairi"
p4_name: str = "Namine"
achievements: list[str] = ['Crafting Genius', 'World Savior',
                           'Master Explorer', 'Collector Supreme',
                           'Untouchable', 'Boss Slayer', 'Strategist',
                           'Unstoppable', 'Speed Runner', 'Survivor',
                           'Treasure Hunter', 'First Steps', 'Sharp Mind',
                           'Hidden Path Finder'
                           ]


def gen_player_achievements() -> set[str]:
    ach_count: int = random.randint(int(len(achievements) / 2),
                                    len(achievements) - 1)
    ach: set[str] = set()
    for _ in range(ach_count):
        i: int = random.randint(0, len(achievements) - 1)
        ach.add(achievements[i])
    return ach


def main() -> None:
    p1_ach: set[str] = gen_player_achievements()
    p2_ach: set[str] = gen_player_achievements()
    p3_ach: set[str] = gen_player_achievements()
    p4_ach: set[str] = gen_player_achievements()
    all_ach: set[str] = p1_ach.union(p2_ach.union(p3_ach.union(p4_ach)))
    common_ach: set[str] = p1_ach.intersection(p2_ach.intersection(
        p3_ach.intersection(p4_ach)))
    p1_only: set[str] = p1_ach.difference(p2_ach.union(p3_ach.union(p4_ach)))
    p2_only: set[str] = p2_ach.difference(p1_ach.union(p3_ach.union(p4_ach)))
    p3_only: set[str] = p3_ach.difference(p2_ach.union(p1_ach.union(p4_ach)))
    p4_only: set[str] = p4_ach.difference(p2_ach.union(p3_ach.union(p1_ach)))
    p1_miss: set[str] = set(achievements).difference(p1_ach)
    p2_miss: set[str] = set(achievements).difference(p2_ach)
    p3_miss: set[str] = set(achievements).difference(p3_ach)
    p4_miss: set[str] = set(achievements).difference(p4_ach)

    print("=== Achievement Tracker System ===\n")

    print(f"Player {p1_name}: {p1_ach}")
    print(f"Player {p2_name}: {p2_ach}")
    print(f"Player {p3_name}: {p3_ach}")
    print(f"Player {p4_name}: {p4_ach}\n")

    print(f"All distinct achievements: {all_ach}\n")

    print(f"Common achievements: {common_ach}\n")

    print(f"Only {p1_name}: {p1_only}")
    print(f"Only {p2_name}: {p2_only}")
    print(f"Only {p3_name}: {p3_only}")
    print(f"Only {p4_name}: {p4_only}\n")

    print(f"{p1_name} is missing: {p1_miss}")
    print(f"{p2_name} is missing: {p2_miss}")
    print(f"{p3_name} is missing: {p3_miss}")
    print(f"{p4_name} is missing: {p4_miss}")


if __name__ == "__main__":
    main()
