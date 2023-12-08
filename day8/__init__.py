#!/usr/bin/env python3

""" day 8 """

import re
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


class Node:  # pylint: disable=too-few-public-methods
    """node"""

    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


def get_nodes(lines):
    """get nodes"""
    nodes_raw = lines[2:]
    nodes_raw_dict = dict([node_raw.split(" = ") for node_raw in nodes_raw])
    node_names = nodes_raw_dict.keys()
    nodes = {node_name: Node(node_name) for node_name in node_names}
    for node_name in node_names:
        tmp = re.match(
            r"\(([0-9A-Z]{3}), ([0-9A-Z]{3})\)", nodes_raw_dict[node_name]
        ).groups()
        left, right = tmp
        node_cur = nodes[node_name]
        node_cur.left = nodes[left]
        node_cur.right = nodes[right]
    return nodes


def pt1(lines):
    """day eight part one"""
    nav = lines[0]
    nodes = get_nodes(lines)
    head = nodes["AAA"]
    steps = 0
    index = 0
    nav_map = {"L": "left", "R": "right"}
    while head.name != "ZZZ":
        index %= len(nav)
        direction = nav[index % len(nav)]
        head = getattr(head, nav_map[direction])
        index += 1
        steps += 1
    return steps


def pt2(lines):
    """day eight part two"""
    nav = lines[0]
    nodes = get_nodes(lines)
    heads = [nodes[name] for name in nodes.keys() if name[2] == "A"]
    # tails = [node.name for node in nodes if node.name[2] == 'Z']
    steps = 0
    index = 0
    nav_map = {"L": "left", "R": "right"}

    def done():
        return all(head.name[2] == "Z" for head in heads)

    while not done():
        progress = None if steps % 1000000 else print(steps)  # pylint: disable
        assert progress is None
        index %= len(nav)
        direction = nav[index % len(nav)]
        heads = [getattr(head, nav_map[direction]) for head in heads]
        index += 1
        steps += 1
    return steps


EXAMPLE_ONE = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""[
    1:-1
]


EXAMPLE_TWO = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""[
    1:-1
]


EXAMPLE_THREE = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""[
    1:-1
]


def main(prefix=""):
    """day eight"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one_lines = EXAMPLE_ONE.split("\n")
    example_two_lines = EXAMPLE_TWO.split("\n")
    eg1 = pt1(example_one_lines)
    assert eg1 == 2
    eg2 = pt1(example_two_lines)
    assert eg2 == 6
    ans1 = pt1(lines)
    assert ans1 == 19099
    print(ans1)

    print("Part 2")
    example_three_lines = EXAMPLE_THREE.split("\n")
    pt2eg1 = pt2(example_one_lines)
    print(pt2eg1)
    pt2eg2 = pt2(example_two_lines)
    print(pt2eg2)
    pt2eg3 = pt2(example_three_lines)
    print(pt2eg3)
    # assert eg2 == 5905
    ans2 = pt2(lines)
    # # assert ans2 == 45647654
    print(ans2)


if __name__ == "__main__":
    main()
