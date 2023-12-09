# TIM 2023
# Advent of Code
# Tag 8: Haunted Wasteland
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

import math
from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def remove_whitespace(puzzle):
    return list(map(lambda line: "".join(list(map(lambda x: x.strip(), line.split()))), puzzle))


def count_steps(node, maze_end, nav, steps_dict, movement):
    steps_total = 0
    while node != maze_end:
        for move in movement:
            node = nav[node][steps_dict[move]]
            steps_total += 1
    return steps_total


def solve_part_1(puzzle):
    puzzle = remove_whitespace(puzzle)
    maze_start = "AAA"
    maze_end = "ZZZ"
    movement = puzzle[0]
    steps_dict = {"L": 0, "R": 1}
    nav = dict(map(lambda x: (x[0], x[1].strip("()").split(",")),
                   dict(map(lambda x: tuple(x.split("=")), filter(lambda x: "=" in x, puzzle))).items()))
    count_steps(maze_start, maze_end, nav, steps_dict, movement)

    return count_steps(maze_start, maze_end, nav, steps_dict, movement)


def solve_part_2(puzzle):
    puzzle = remove_whitespace(puzzle)
    movement = puzzle[0]
    steps_dict = {"L": 0, "R": 1}
    nav = dict(map(lambda x: (x[0], x[1].strip("()").split(",")),
                   dict(map(lambda x: tuple(x.split("=")), filter(lambda x: "=" in x, puzzle))).items()))
    nodes = list(filter(lambda x: x[-1] == "A", nav.keys()))
    a_nodes_dict = dict(map(lambda x: (x, 0), nodes))

    for node in nodes:
        steps_total = 0
        node_act = node
        while node_act[-1] != "Z":
            for move in movement:
                node_act = nav[node_act][steps_dict[move]]
                steps_total += 1
        a_nodes_dict[node] = steps_total
    return math.lcm(*a_nodes_dict.values())


if __name__ == "__main__":
    puzzle = read_puzzle("day08.txt")
    puzzle = remove_whitespace(puzzle)
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
