# TIM 2023
# Advent of Code
# Tag 2: Cube Conundrum
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day02 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day02_example.txt")
    assert solve_part_1(puzzle) == 8
    puzzle = dummy_puzzle("day02.txt")
    assert solve_part_1(puzzle) == 2061


def test_part_2():
    puzzle = dummy_puzzle("day02_example.txt")
    assert solve_part_2(puzzle) == 2286
    puzzle = dummy_puzzle("day02.txt")
    assert solve_part_2(puzzle) == 72596
