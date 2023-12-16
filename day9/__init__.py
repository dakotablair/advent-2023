#!/usr/bin/env python3

""" day 9 """

from functools import reduce

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


def diffs(nums):
    """take differences of elements"""
    return [
        nums[index + 1] - num
        for index, num in enumerate(nums)
        if index + 1 < len(nums)
    ]


def extrapolate(hists):
    """Use successive differences to extrapolate a new value."""
    hists_rev = hists[::-1]
    for index, hist in enumerate(hists_rev):
        if index == 0:
            hist.append(0)
            continue
        hist.append(hist[-1] + hists_rev[index - 1][-1])
    return hists[0][-1]


def lextrapolate(hists):
    """Use successive differences to extrapolate a new value in reverse."""
    hists_rev = hists[::-1]
    out = []
    for index, hist in enumerate(hists_rev):
        if index == 0:
            out.append([0, *hist])
            continue
        out.append([(hist[0] - out[index - 1][0]), *hist])
    return out[-1][0]


def pt1(lines):
    """day nine part one"""
    exts = []
    for line in lines:
        nums = [int(num) for num in line.split(" ")]
        succ_diffs = [nums]
        diff_cur = nums
        while any(bool(num) for num in diff_cur):
            diff_cur = diffs(diff_cur)
            succ_diffs.append(diff_cur)
        exts.append(extrapolate(succ_diffs))
    return sum(exts)


def pt2(lines):  # pylint: disable=too-many-locals
    """day nine part two"""
    exts = []
    for line in lines:
        nums = [int(num) for num in line.split(" ")]
        succ_diffs = [nums]
        diff_cur = nums
        while any(bool(num) for num in diff_cur):
            diff_cur = diffs(diff_cur)
            succ_diffs.append(diff_cur)
        exts.append(lextrapolate(succ_diffs))
    return sum(exts)


EXAMPLE_ONE = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
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
    assert eg1 == 114
    ans1 = pt1(lines)
    # assert ans1 == 19099
    print(f"{ans1}")

    print("Part 2")
    eg1pt2 = pt2(example_one_lines)
    assert eg1pt2 == 2
    ans2 = pt2(lines)
    assert ans2 == 1019
    print(f"{ans2}")


if __name__ == "__main__":
    main()
