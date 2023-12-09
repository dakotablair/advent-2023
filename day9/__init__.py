#!/usr/bin/env python3

""" day 9 """

import re
from functools import reduce
from math import lcm

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


class Node:  # pylint: disable=too-few-public-methods
    """node"""

    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


def pt1(lines):
    """day nine part one"""
    return len(lines)


def pt2(lines):  # pylint: disable=too-many-locals
    """day nine part two"""
    return len(lines)


EXAMPLE_ONE = """
"""[
    1:-1
]


def main(prefix=""):
    """day nine"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one_lines = EXAMPLE_ONE.split("\n")
    eg1 = pt1(example_one_lines)
    # assert eg1 == 2
    print(f"{eg1=}")
    ans1 = pt1(lines)
    # assert ans1 == 19099
    print(f"{ans1=}")

    print("Part 2")
    ans2 = pt2(lines)
    # assert ans2 == 17099847107071
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
