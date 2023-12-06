# TIM 2023
# Advent of Code
# Tag 6: Wait For It
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day06 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day06_example.txt")
    assert solve_part_1(puzzle) == 288


def test_part_2():
    puzzle = dummy_puzzle("day06_example.txt")
    assert solve_part_2(puzzle) == 71503

