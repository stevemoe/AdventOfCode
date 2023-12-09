# TIM 2023
# Advent of Code
# Tag 9: Mirage Maintenance
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day09 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day09_example.txt")
    assert solve_part_1(puzzle) == 114


def test_part_2():
    puzzle = dummy_puzzle("day09_example.txt")
    assert solve_part_2(puzzle) == 2
