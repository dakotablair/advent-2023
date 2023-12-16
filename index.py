#!/usr/bin/env python3
""" Advent of Code 2023 """
from day1 import main as day1
from day2 import main as day2
from day3 import main as day3
from day4 import main as day4
from day5 import main as day5
from day6 import main as day6
from day7 import main as day7
from day8 import main as day8
from day9 import main as day9


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

    print("Day 5")
    day5(prefix="./day5/")

    print("Day 6")
    day6(prefix="./day6/")

    print("Day 7")
    day7(prefix="./day7/")

    print("Day 8")
    day8(prefix="./day8/")

    print("Day 9")
    day9(prefix="./day9/")


if __name__ == "__main__":
    main()
