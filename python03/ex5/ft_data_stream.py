#!/usr/bin/env python3

import typing
import random


NB_ITER: int = 1000
PLAYERS: list[str] = ["Sora", "Riku", "Kairi", "Namine", "Roxas",
                      "Xion", "Axel", "Aqua", "Ventus", "Terra"]
EVENTS: list[str] = ["swim", "eat", "run", "attack", "magic",
                     "object", "summon", "jump", "sleep", "glide"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(PLAYERS), random.choice(EVENTS)


def consume_event(
        ev_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while ev_list:
        yield ev_list.pop(random.randrange(len(ev_list)))


def main() -> None:
    print("=== Game Data Stream Processor ===")
    for i in range(NB_ITER):
        event: tuple[str, str] = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    ev_list: list[tuple[str, str]] = []
    for _ in range(10):
        ev_list.append(next(gen_event()))
    print(f"Built a list of 10 events: {ev_list}")
    for consumed_event in consume_event(ev_list):
        print(f"Got event from list: {consumed_event}")
        print(f"Remains in list: {ev_list}")


if __name__ == "__main__":
    main()
