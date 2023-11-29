# TIM 2022
# Advent of Code
# Tag 5: Supply Stacks
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day05 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day05_example1.txt")
    assert solve_part_1(puzzle) == "CMZ"


def test_part_2():
    puzzle = dummy_puzzle("day05_example1.txt")
    assert solve_part_2(puzzle) == "MCD"