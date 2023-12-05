#!/usr/bin/env python3

""" day 2 """
import re
from functools import reduce
from textwrap import dedent


BAG_STATE = {
    "blue": 14,
    "green": 13,
    "red": 12,
}


def prod(factors):
    """compute the product of factors"""
    return reduce(lambda x, y: x * y, factors, 1)


def evaluate_pull(pull):
    """evaluate pull"""
    qty, color = pull.groups()
    return int(qty) <= BAG_STATE[color]


def parse_move(move):
    """parse move"""
    pulls_raw = move.split(",")
    move_object = {"power": {}, "pulls": [], "valid": True}
    for pull_raw in pulls_raw:
        pull_groups = re.match(r" ([0-9]{1,2}) (blue|green|red)", pull_raw)
        qty, color = pull_groups.groups()
        move_object["pulls"].append((color, qty))
        move_object["valid"] &= int(qty) <= BAG_STATE[color]
        move_object["power"][color] = max(
            int(qty), move_object["power"].get(color, 1)
        )
    return move_object


def parse_game(game):
    """parse game"""
    game_id, moves_raw = game.split(":")
    moves = moves_raw.split(";")
    moves_validated = [parse_move(move) for move in moves]
    colors = ["blue", "green", "red"]
    power = prod(
        max(move["power"].get(color, 1) for move in moves_validated)
        for color in colors
    )
    valid = all(move["valid"] for move in moves_validated)
    game_parsed = {
        "game_id": game_id,
        "valid": valid,
        "power": power,
    }
    return game_parsed


def pt1(lines):
    """day two part one"""
    return sum(
        int(parsed["game_id"].split()[1])
        for line in lines
        if (parsed := parse_game(line))["valid"]
    )


def pt2(lines):
    """day two part two"""
    return sum(int(parse_game(line)["power"]) for line in lines)


example_one = dedent(
    """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """
)[1:-1]


def main(prefix=""):
    """day two"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one_lines = example_one.split("\n")
    assert pt1(example_one_lines) == 8
    # 2061 too low (but correct for someone else)
    ans1 = pt1(lines)
    assert ans1 == 2551
    print(ans1)

    print("Part 2")
    assert pt2(example_one_lines) == 2286
    ans2 = pt2(lines)
    # assert ans2 ==
    print(ans2)


if __name__ == "__main__":
    main()
