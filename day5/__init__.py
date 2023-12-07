#!/usr/bin/env python3

""" day 5 """
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


cats = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]


def map_to_fn(map_raw):
    maps = map_raw.split("\n")
    maps2 = [map_.split(" ") for map_ in maps]
    maps3 = [
        (int(start), int(dest), int(length)) for (dest, start, length) in maps2
    ]

    def trans(num):
        for start, dest, length in maps3:
            if start <= num < start + length:
                return (num - start) + dest
        return num

    return trans


def apply(funcs, init):
    """apply"""
    acc = init
    for func in funcs:
        acc = func(acc)
    return acc


def pt1(lines):
    """day five part one"""
    seeds_raw = lines[0]
    seeds = [int(i) for i in seeds_raw.split(": ")[1].split(" ")]
    maps = dict(
        [map_.split(" map:\n") for map_ in "\n".join(lines[2:]).split("\n\n")]
    )
    progs = {i: map_to_fn(map_) for i, map_ in enumerate(maps.values())}
    locs = [apply(progs.values(), seed) for seed in seeds]
    return min(locs)


def pt2(lines):
    """day five part two"""
    seeds_raw = lines[0]
    seed_ranges = [int(i) for i in seeds_raw.split(": ")[1].split(" ")]
    seed_starts = seed_ranges[::2]
    seed_lengths = seed_ranges[1::2]
    # print(f"seed_lengths: {seed_lengths}")
    # seeds = sum(
    #     [
    #         list(range(seed_starts[i], seed_starts[i] + seed_lengths[i]))
    #         for i in range(len(seed_starts))
    #     ],
    #     [],
    # )
    maps = dict(
        [map_.split(" map:\n") for map_ in "\n".join(lines[2:]).split("\n\n")]
    )
    progs = {i: map_to_fn(map_) for i, map_ in enumerate(maps.values())}
    # locs = [for seed in seeds]
    # print(f"total seeds: {sum(seed_lengths)}")
    loc_min = float("inf")
    for i, seed_start in enumerate(seed_starts):
        for j in range(seed_lengths[i]):
            seed = seed_start + j
            progress = (
                None if seed % 1000000 else print(seed)
            )  # pylint: disable
            assert progress is None
            val = apply(progs.values(), seed)
            if val < loc_min:
                loc_min = val
    return loc_min


EXAMPLE_ONE = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""[
    1:-1
]


def main(prefix=""):
    """day five"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one_lines = EXAMPLE_ONE.split("\n")
    eg1 = pt1(example_one_lines)
    assert eg1 == 35
    ans1 = pt1(lines)
    assert ans1 == 84470622
    print(ans1)

    print("Part 2")
    eg2 = pt2(example_one_lines)
    assert eg2 == 46
    print(eg2)
    # This method takes ~7 hours to yield the answer.
    # ans2 = pt2(lines)
    # assert ans2 == 26714516
    # print(ans2)
    print("No optimized solution implemented!")


if __name__ == "__main__":
    main()
