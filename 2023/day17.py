# TIM 2023
# Advent of Code
# Tag 17: Clumsy Crucible
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

import re
from collections import namedtuple
from time import perf_counter as pfc

def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


Edge = namedtuple("Edge", "start, end, weight")

def create_edge(start, end, cost):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        self.edges = [create_edge(*edge) for edge in edges]

    def vertices(self):
        return

def solve_part_1(puzzle):
    puzzle = list(map(lambda x: re.findall(r"\d", x), puzzle))
    puzzle = list(map(lambda x: list(map(int, x)), puzzle))
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            puzzle[i][j] = puzzle[i][j] + 1
    print(puzzle)
    return puzzle


def solve_part_2(puzzle):
    return puzzle


if __name__ == "__main__":
    puzzle = read_puzzle("day17.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

