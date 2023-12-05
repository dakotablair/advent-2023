#!/usr/bin/env python3

""" day 4 """
from functools import reduce
from textwrap import dedent

DIGITS = {str(i) for i in range(10)}


def prod(factors):
    """compute the product of factors"""
    return reduce(lambda x, y: x * y, factors, 1)


def represents_int(rep):
    """does rep represent an integer?"""
    try:
        int(rep)
    except ValueError:
        return False
    return True


def pt1(lines):
    """day four part one"""
    # convert lines into array
    # array = {i: dict(enumerate(line)) for i, line in enumerate(lines)}
    values = []
    for line in lines:
        _, card = line.split(":")
        haves, wins = card.split("|")
        havess = {
            int(have) for have in haves.split(" ") if represents_int(have)
        }
        winss = {int(win) for win in wins.split(" ") if represents_int(win)}
        value = 2 ** (len(havess.intersection(winss)) - 1)
        values.append(value if value >= 1 else 0)
    return sum(values)


def pt2(lines):
    """day four part two"""
    card_counts = {i + 1: 1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        _, card = line.split(":")
        haves, wins = card.split("|")
        havess = {
            int(have) for have in haves.split(" ") if represents_int(have)
        }
        winss = {int(win) for win in wins.split(" ") if represents_int(win)}
        intersection = havess.intersection(winss)
        winnings = len(intersection)
        for j in range(winnings):
            card_counts[i + j + 2] += card_counts[i + 1]

    return sum(card_counts.values())


example_one = dedent(
    """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
)[1:-1]


def main(prefix=""):
    """day four"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one_lines = example_one.split("\n")
    eg1 = pt1(example_one_lines)
    assert eg1 == 13
    ans1 = pt1(lines)
    assert ans1 == 21485
    print(ans1)

    print("Part 2")
    eg2 = pt2(example_one_lines)
    assert eg2 == 30
    ans2 = pt2(lines)
    assert ans2 == 11024379
    print(ans2)


if __name__ == "__main__":
    main()
