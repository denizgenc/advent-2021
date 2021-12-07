#!/usr/bin/env python
from typing import List, Tuple

from adventinput import get_data

def get_result(commands: List[Tuple[str, int]]) -> int:
    horizontal = 0
    depth = 0
    for direction, distance in commands:
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
        else:
            print("This shouldn't have happened")
            exit(1)

    return horizontal * depth

def get_result_2(commands: List[Tuple[str, int]]) -> int:
    horizontal = 0
    depth = 0
    angle = 0
    for direction, amount in commands:
        if direction == "forward":
            horizontal += amount
            depth += angle * amount
        elif direction == "down":
            angle += amount
        elif direction == "up":
            angle -= amount
        else:
            print("This shouldn't have happened")
            exit(1)

    return horizontal * depth

if __name__ == "__main__":
    commands = [(a, int(b)) for a, b in [line.split() for line in get_data(2)]]

    print(get_result(commands))
    print(get_result_2(commands))
