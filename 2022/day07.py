# TIM 2023
# Advent of Code
# Tag 7: No Space Left On Device
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc

def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def solve_part_1(puzzle):
    return puzzle


def solve_part_2(puzzle):
    return puzzle


if __name__ == "__main__":
    puzzle = read_puzzle("day07.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

