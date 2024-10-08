# TIM 2023
# Advent of Code
# Tag 13: Point of Incidence
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day13 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day13_example.txt")
    assert solve_part_1(puzzle) == 405
    puzzle = dummy_puzzle("day13_example_custom.txt")
    assert solve_part_1(puzzle) == 709
    puzzle = dummy_puzzle("day13_example_custom2.txt")
    assert solve_part_1(puzzle) == 600


def test_part_2():
    puzzle = dummy_puzzle("day13_example.txt")
    assert solve_part_2(puzzle) == None

