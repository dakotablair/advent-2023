#!/usr/bin/env python3

""" day 6 """
import re

from functools import reduce
from math import floor, sqrt

# from textwrap import dedent

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


def apply(funcs, init):
    """apply"""
    acc = init
    for func in funcs:
        acc = func(acc)
    return acc


def ways_to_win(dist, time):
    """ways to win"""
    disc = time**2 - 4 * dist
    if disc < 0:
        return 0
    x_1 = (time + sqrt(disc)) / 2
    x_2 = (time - sqrt(disc)) / 2
    ways = floor(x_1) - floor(x_2) if x_1 > x_2 else floor(x_1) - floor(x_2)
    return ways if int(abs(x_1 - x_2)) != abs(x_1 - x_2) else ways - 1


def pt1(lines):
    """day six part one"""
    times_raw, dists_raw = lines
    times_str = re.sub(r"\W+", " ", times_raw.split(":")[1]).strip().split(" ")
    dists_str = re.sub(r"\W+", " ", dists_raw.split(":")[1]).strip().split(" ")
    times = [int(time) for time in times_str]
    dists = [int(dist) for dist in dists_str]
    records = [ways_to_win(dist, time) for time, dist in zip(times, dists)]
    return prod(records)


def pt2(lines):
    """day six part two"""
    times_raw, dists_raw = lines
    times_str = "".join(
        re.sub(r"\W+", " ", times_raw.split(":")[1]).strip().split(" ")
    )
    dists_str = "".join(
        re.sub(r"\W+", " ", dists_raw.split(":")[1]).strip().split(" ")
    )
    return ways_to_win(int(dists_str), int(times_str))


EXAMPLE_ONE = """
Time:      7  15   30
Distance:  9  40  200
"""[
    1:-1
]


def main(prefix=""):
    """day six"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one_lines = EXAMPLE_ONE.split("\n")
    eg1 = pt1(example_one_lines)
    assert eg1 == 288
    ans1 = pt1(lines)
    assert ans1 == 316800
    print(ans1)

    print("Part 2")
    eg2 = pt2(example_one_lines)
    assert eg2 == 71503
    ans2 = pt2(lines)
    assert ans2 == 45647654
    print(ans2)


if __name__ == "__main__":
    main()
