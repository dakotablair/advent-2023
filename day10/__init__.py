#!/usr/bin/env python3

""" day 10 """

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


TOKENS = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((0, 1), (1, 0)),
}
NABE = ((-1, 0), (0, 1), (1, 0), (0, -1))
CONNECTED = {(-1, 0): "|LJ", (0, 1): "-LF", (1, 0): "|7F", (0, -1): "-J7"}


def pt1(lines):
    """day ten part one"""
    array = {i: dict(enumerate(line)) for i, line in enumerate(lines)}
    start = [
        (i, line.find("S"))
        for i, line in enumerate(lines)
        if line.find("S") >= -1
    ][0]
    s_r, s_c = start
    queue = [start]
    dist = 0
    dists = {s_r: {s_c: 0}}
    visited = {(s_r, s_c)}
    while len(queue) > 0:
        r_h, c_h = queue.pop(0)
        for r_o, c_o in NABE:
            if not 0 < r_h + r_o < len(lines) or not 0 < c_h + c_o < len(
                lines[0]
            ):
                continue
            token = array[r_h + r_o][c_h + c_o]
            token_r = r_h + r_o
            token_c = c_h + c_o
            # TODO: increase dists at some point, but when?
            if (
                token in CONNECTED[(r_o, c_o)]
                and (token_r, token_c) not in visited
            ):
                dists[token_r][token_c] = dist + 1
                queue.append((token_r, token_c))
                visited.add((token_r, token_c))
    dist_max = sorted(dists.items(), key=lambda x: x[1], reverse=True)[0][1]
    return dist_max


def pt2(lines):  # pylint: disable=too-many-locals
    """day ten part two"""
    return len(lines)


EXAMPLE_ONE = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""[
    1:-1
]


EXAMPLE_TWO = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""[
    1:-1
]


def main(prefix=""):
    """day ten"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one_lines = EXAMPLE_ONE.split("\n")
    eg1 = pt1(example_one_lines)
    print(eg1)
    assert lines
    # assert eg1 == 114
    # ans1 = pt1(lines)
    # assert ans1 == 19099
    # print(f"{ans1}")

    # print("Part 2")
    # eg1pt2 = pt2(example_one_lines)
    # assert eg1pt2 == 2
    # ans2 = pt2(lines)
    # assert ans2 == 1019
    # print(f"{ans2}")


if __name__ == "__main__":
    main()
