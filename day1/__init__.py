#!/usr/bin/env python3

""" day 1 """
import re


def pt1(lines):
    """ part one """
    reone = r'^(.)(.*)(.)$'
    scrubs = [
        ans
        for line in lines
        if (ans := re.sub(r'[^0-9]', "", line))
    ]
    nums = [int(re.sub(reone, r'\1\3', line)) for line in scrubs]
    return sum(i if i > 10 else 11*i for i in nums)


def pt2(lines):
    """ part two """
    digits = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    regex = r'([0-9]|one|two|three|four|five|six|seven|eight|nine)'
    regexr = r'([0-9]|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno)'

    answers = []
    for line in lines:
        matched = re.search(regex, line)
        matchedr = re.search(regexr, line[::-1])
        total = 0
        if matched:
            total += 10*int(digits[matched.groups()[0]])
        if matchedr:
            total += int(digits[matchedr.groups()[0][::-1]])
        answers.append(total)
    return sum(answers)


def main(prefix=""):
    """ main """
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    example_one_lines = example_one.split("\n")
    assert pt1(example_one_lines) == 142

    print(pt1(lines))

    print("Part 2")
    example_two = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
a1c"""
    example_two_lines = example_two.split("\n")
    assert pt2(example_two_lines) == 281 + 11

    print(pt2(lines))


if __name__ == "__main__":
    main()
