# TIM 2023
# Advent of Code
# Tag 22: Sand Slabs
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day22 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day22_example.txt")
    assert solve_part_1(puzzle) == 5


def test_part_2():
    puzzle = dummy_puzzle("day22_example.txt")
    assert solve_part_2(puzzle) == None

