# TIM 2023
# Advent of Code
# Tag 12: Hot Springs
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day12 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day12_example.txt")
    assert solve_part_1(puzzle) == 21


def test_part_2():
    puzzle = dummy_puzzle("day12_example.txt")
    assert solve_part_2(puzzle) == 525152

