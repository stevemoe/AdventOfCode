# TIM 2023
# Advent of Code
# Tag 14: Parabolic Reflector Dish
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day14 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day14_example.txt")
    assert solve_part_1(puzzle) == 136


def test_part_2():
    puzzle = dummy_puzzle("day14_example.txt")
    assert solve_part_2(puzzle) == 64

