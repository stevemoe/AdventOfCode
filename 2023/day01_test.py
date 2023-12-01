# TIM 2023
# Advent of Code
# Tag 1: Trebuchet?!
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day01 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle_example = dummy_puzzle("day01_example.txt")
    assert solve_part_1(puzzle_example) == 142
    puzzle = dummy_puzzle("day01.txt")
    assert solve_part_1(puzzle) == 54644


def test_part_2():
    puzzle = dummy_puzzle("day01_example2.txt")
    assert solve_part_2(puzzle) == 281
    puzzle = dummy_puzzle("day01.txt")
    assert solve_part_2(puzzle) == 53348