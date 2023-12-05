#!/usr/bin/env python3
""" Advent of Code 2023 """
from day1 import main as day1
from day2 import main as day2
from day3 import main as day3
from day4 import main as day4


def main():
    """main"""
    print("Day 1")
    day1(prefix="./day1/")

    print("Day 2")
    day2(prefix="./day2/")

    print("Day 3")
    day3(prefix="./day3/")

    print("Day 4")
    day4(prefix="./day4/")


if __name__ == "__main__":
    main()
