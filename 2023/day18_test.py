# TIM 2023
# Advent of Code
# Tag 18: Lavaduct Lagoon
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day18 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day18_example.txt")
    assert solve_part_1(puzzle) == 62


def test_part_2():
    puzzle = dummy_puzzle("day18_example.txt")
    assert solve_part_2(puzzle) == 952408144115

