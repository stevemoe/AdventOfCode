# TIM 2023
# Advent of Code
# Tag 10: Pipe Maze
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day10 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day10_example.txt")
    assert solve_part_1(puzzle) == 4
    # puzzle = dummy_puzzle("day10_example2.txt")
    # assert solve_part_1(puzzle) == 8
    # puzzle = dummy_puzzle("day10.txt")
    # assert solve_part_1(puzzle) == 6701
    # puzzle = dummy_puzzle("day10_example_part2_1.txt")
    # assert solve_part_1(puzzle) == 2


def test_part_2():
    # puzzle = dummy_puzzle("day10_example.txt")
    # assert solve_part_2(puzzle) == 1
    # puzzle = dummy_puzzle("day10_example2.txt")
    # assert solve_part_2(puzzle) == 1
    # puzzle = dummy_puzzle("day10_example_part2_1.txt")
    # assert solve_part_2(puzzle) == 4
    # puzzle = dummy_puzzle("day10_example_part2_2.txt")
    # assert solve_part_2(puzzle) == 8
    puzzle = dummy_puzzle("day10_example_part2_3.txt")
    assert solve_part_2(puzzle) == 10
