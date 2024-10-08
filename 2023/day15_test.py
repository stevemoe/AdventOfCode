# TIM 2023
# Advent of Code
# Tag 15: Lens Library
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day15 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day15_example.txt")
    assert solve_part_1(puzzle) == 1320


def test_part_2():
    puzzle = dummy_puzzle("day15_example.txt")
    assert solve_part_2(puzzle) == 145
    puzzle = dummy_puzzle("day15.txt")
    # assert solve_part_2(puzzle) == 215827

