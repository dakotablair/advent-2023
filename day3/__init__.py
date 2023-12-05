#!/usr/bin/env python3

""" day 3 """
import re
from functools import reduce
from textwrap import dedent

DIGITS = {str(i) for i in range(10)}


def prod(factors):
    """compute the product of factors"""
    return reduce(lambda x, y: x * y, factors, 1)


def nabe(row, col, length):
    """find positions adjacent to length characters"""
    # row-1, col-1 ... row-1, col+1
    # row, col-1, row, col+1
    # row+1, col-1 ... row+1, col+1
    return sum(
        [
            [(row - 1, col - 1 + offset) for offset in range(length + 2)],
            [(row, col - 1), (row, col + length)],
            [(row + 1, col - 1 + offset) for offset in range(length + 2)],
        ],
        [],
    )


def get_num(pos, line):
    """get a number from a line overlapping a position"""
    #      identify start by moving left in array until an edge
    #        or non digit token
    #      identify end by moving right in array until an edge
    #        or non digit token
    i = 0
    while pos + i > 0 and line[pos + i - 1] in DIGITS:
        i -= 1
    start = pos + i
    i = 0
    while pos + i < len(line) and line[pos + i] in DIGITS:
        i += 1
    end = pos + i
    return (start, end, line[start:end]) if start < end else False


def pt1(lines):
    """day three part one"""
    # convert lines into array
    array = {i: dict(enumerate(line)) for i, line in enumerate(lines)}
    # for each line find all numbers in line
    locs = {}
    part_nums = []
    for i, line in enumerate(lines):
        matchs = re.finditer(r"([0-9]+)", line)
        line_locs = [
            (int(line[slice(*match.span())]), match.span()) for match in matchs
        ]
        locs[i] = line_locs
        # search for symbols surrounding number
        for num, (start, end) in line_locs:
            tokens = [
                array.get(r, {0: "."}).get(c, ".")
                for (r, c) in nabe(i, start, end - start)
            ]
            symbol_in_nabe = (
                len([token for token in tokens if token != "."]) > 0
            )
            if symbol_in_nabe:
                part_nums.append(num)
    # add numbers with surrounding symbols
    return sum(part_nums)


def pt2(lines):
    """day three part two"""
    # convert lines into array
    # array = {i: dict(enumerate(line)) for i, line in enumerate(lines)}

    adjs = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    ratios = []
    for (i, line) in enumerate(lines):
        # find gears
        gears = re.finditer(r"(\*)", line)
        # for each gear
        for gear in gears:
            start = gear.start()
            # for each adjacent token collect numbers
            nums = set()
            for (r_0, c_0) in adjs:
                ans = (
                    get_num(start + c_0, lines[i + r_0])
                    if lines[i + r_0][start + c_0] in DIGITS
                    else False
                )
                if ans:
                    nums.add(ans)
            if len(nums) == 2:
                ratios.append(prod(int(num) for start, end, num in nums))
    return sum(ratios)


example_one = dedent(
    """
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
"""
)[1:-1]


def main(prefix=""):
    """day three"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one_lines = example_one.split("\n")
    assert pt1(example_one_lines) == 4361
    ans1 = pt1(lines)
    assert ans1 == 550934
    print(ans1)

    print("Part 2")
    assert pt2(example_one_lines) == 467835
    ans2 = pt2(lines)
    assert ans2 == 81997870
    print(ans2)


if __name__ == "__main__":
    main()
