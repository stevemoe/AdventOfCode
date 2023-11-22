# TIM 2023
# Advent of Code
# Tag 1: Aufgabenname
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    # die Rückgabe sollte eine Liste von Strings sein (zeilenweises Lesen)
    return []


def solve_part_1(puzzle):
    return puzzle


def solve_part_2(puzzle):
    return 2


if __name__ == "__main__":
    puzzle = read_puzzle("day01.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
