#!/usr/bin/env python3

import sys


def main(arguments: list[str]) -> None:
    print("=== Player Score Analytics ===")
    l_len: int = len(arguments)
    scores: list[int] = []
    i: int = 0
    for j in range(1, l_len):
        try:
            scores.append(int(arguments[j]))
        except ValueError:
            print(f"Invalid parameter: '{arguments[j]}'")
        else:
            i += 1

    l_len = len(scores)
    if l_len == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py\
 <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Number of players: {l_len}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {(sum(scores) / l_len):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main(sys.argv)
