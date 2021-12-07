#!/usr/bin/env python
import adventinput

def get_results(data):
    # Boring method
    # increased = 0
    # for a, b in zip(data[:-1], data[1:]):
    #     if b > a:
    #         increased += 1
    # return increased

    # Fun method
    return sum([b > a for a, b in zip(data[:-1], data[1:])])

if __name__ == "__main__":
    data = [int(i) for i in adventinput.get_data(1)]

    print(get_results(data))

    windows = [a + b + c for a, b, c in zip(data[:-2], data[1:-1], data[2:])]

    print(get_results(windows))
