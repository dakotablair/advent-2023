#!/usr/bin/env python3

""" day 7 """

from collections import Counter
from functools import reduce

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


def get_type(hand):  # pylint: disable=too-many-return-statements
    """identify camel cards type for each hand"""
    hand_count = Counter(hand)
    counts = hand_count.most_common()
    mul1 = counts[0][1]
    if mul1 == 5:
        return 7
    mul2 = counts[1][1]
    if mul1 == 1:
        return 1
    if mul1 == 2:
        if mul2 == 1:
            return 2
        return 3
    if mul1 == 3:
        if mul2 == 1:
            return 4
        if mul2 == 2:
            return 5
    if mul1 == 4:
        return 6
    return 0


def get_type_pt2(hand):  # pylint: disable=too-many-return-statements
    """identify camel cards type for each hand"""
    hand_count = Counter(hand)
    counts = hand_count.most_common()
    mul1 = counts[0][1]
    if mul1 == 5:
        return 7
    mul1 += hand_count["J"] if counts[0][0] != "J" else counts[1][1]
    if mul1 == 5:
        return 7
    many_js = counts[0][0] == "J" or counts[1][0] == "J"
    mul2 = counts[1][1] if not many_js else counts[2][1]
    if mul1 == 1:
        return 1
    if mul1 == 2:
        if mul2 == 1:
            return 2
        return 3
    if mul1 == 3:
        if mul2 == 1:
            return 4
        if mul2 == 2:
            return 5
    if mul1 == 4:
        return 6
    return 0


def hand_key(handbid):
    """compute hand key part 1"""
    hand, _ = handbid.split(" ")
    ranks = "23456789TJQKA"[::-1]
    hand_ranks = (ranks.find(card) for card in hand)
    return (-get_type(hand), *hand_ranks)


def hand_key_pt2(handbid):
    """compute hand key part 2"""
    hand, _ = handbid.split(" ")
    ranks = "J23456789TQKA"[::-1]
    hand_ranks = (ranks.find(card) for card in hand)
    return (-get_type_pt2(hand), *hand_ranks)


def pt1(lines):
    """day seven part one"""
    handbids = sorted(lines, key=hand_key, reverse=True)
    return sum(
        (i + 1) * int(handbid.split(" ")[1])
        for i, handbid in enumerate(handbids)
    )


def pt2(lines):
    """day seven part two"""
    handbids = sorted(lines, key=hand_key_pt2, reverse=True)
    return sum(
        (i + 1) * int(handbid.split(" ")[1])
        for i, handbid in enumerate(handbids)
    )


EXAMPLE_ONE = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""[
    1:-1
]


def main(prefix=""):
    """day seven"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one_lines = EXAMPLE_ONE.split("\n")
    eg1 = pt1(example_one_lines)
    assert eg1 == 6440
    ans1 = pt1(lines)
    assert ans1 == 241344943
    print(ans1)

    print("Part 2")
    eg2 = pt2(example_one_lines)
    assert eg2 == 5905
    ans2 = pt2(lines)
    # assert ans2 == 45647654
    print(ans2)


if __name__ == "__main__":
    main()
