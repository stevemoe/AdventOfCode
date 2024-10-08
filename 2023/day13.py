# TIM 2023
# Advent of Code
# Tag 13: Point of Incidence
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

import functools
from time import perf_counter as pfc
from collections import Counter


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().split("\n\n")


# ###.#..##..
# .####.#...#
# ..#..##..#. <
# ..#..##..#. <
# .#.##.#...#
# .###..##.#. <<
# .###..##.#. <<
# .#.##.#...#
# ..#..##..#.
# ..#..##..#.
# .####.#...#


def horizontal_mirror_line(pattern):
    same_line = Counter(pattern)
    print(f"same_line: {same_line}")
    ctr = 0
    same_lines = list(map(lambda x: x[0], filter(lambda x: x[1] > 1, same_line.items())))
    print(f"same_line: {same_lines}")
    # print(f"same_lines: {same_lines}")
    # if pattern[-1] in same_lines or pattern[0] in same_lines:
    #     # print(f"pattern: {pattern}")
    #     for i in range(len(pattern) - 1):
    #         ctr += 1
    #         if pattern[i] == pattern[i + 1]:
    #             if pattern[-1 - len(same_lines)] == pattern[i]:
    #                 return ctr
    #             elif pattern[0 + len(same_lines)] == pattern[i]:
    #                 return ctr
    #             # print(f"pattern[i]: {pattern[i]}")
    #             return ctr

    if pattern[0] in same_lines or pattern[-1] in same_lines:
        for i in range(len(pattern) - 1):
            ctr += 1
            if pattern[i] == pattern[i + 1]:
                if i == len(same_lines) - 1:
                    print(f"i: {i}, len(same_lines): {len(same_lines) - 1}")
                    return ctr
                elif i + len(same_lines) == len(pattern) - 1:
                    print(f"i bottom: {i + len(same_lines)}, len(pattern): {len(pattern) - 1}")
                    return ctr
                # print(f"pattern[i]: {pattern[i]}")

    return 0


def vertical_mirror_line(pattern):
    pattern_trans = list(map(lambda line: functools.reduce(lambda x, y: x + y, line), map(list, zip(*pattern))))
    ctr = horizontal_mirror_line(pattern_trans)
    if ctr > 0:
        print(f"pattern {pattern}")
        print(f"pattern_trans:\n{"\n".join(pattern_trans)}")
        print(f"ctr: {ctr}")
    return ctr


def solve_part_1(puzzle):
    patterns = list(map(lambda x: x.split("\n"), puzzle))
    # print(patterns)
    rows_count = 0
    colums_count = 0
    for pattern in patterns:
        # print(pattern)
        rows_count += horizontal_mirror_line(pattern)
        # print(f"rows_count: {rows_count}")
        colums_count += vertical_mirror_line(pattern)
    # rows_count *= 100
    print(f"rows_count: {rows_count}")
    print(f"colums_count: {colums_count}")
    print(f"rows_count + colums_count: {100 * rows_count + colums_count}")
    print("-------------------------------------------------------")
    return 100 * rows_count + colums_count * 1


def solve_part_2(puzzle):
    return puzzle


if __name__ == "__main__":
    puzzle = read_puzzle("day13.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
