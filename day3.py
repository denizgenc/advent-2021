#!/usr/bin/env python
from adventinput import get_data


def get_result(binary_strings):
    digit_sums = [0] * len(binary_strings[0])
    for s in binary_strings:
        for idx, char in enumerate(s):
            digit_sums[idx] += int(char)
    
    # Stupidest shit I've ever written
    gamma_rate_digits = [int((i / len(binary_strings)) > 0.5) for i in digit_sums]
    epsilon_rate_digits = [i ^ 1 for i in gamma_rate_digits]

    gamma_rate = int("".join([str(i) for i in gamma_rate_digits]), 2)
    epsilon_rate = int("".join([str(i) for i in epsilon_rate_digits]), 2)

    return gamma_rate * epsilon_rate

if __name__ == "__main__":
    binary_strings = get_data(3)

    print(get_result(binary_strings))
