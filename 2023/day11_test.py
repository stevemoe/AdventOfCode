# TIM 2023
# Advent of Code
# Tag 11: Cosmic Expansion
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day11 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day11_example.txt")
    assert solve_part_1(puzzle, 2) == 374
    puzzle = dummy_puzzle("day11.txt")
    assert solve_part_1(puzzle, 2) == 9445168


def test_part_2():
    puzzle = dummy_puzzle("day11_example.txt")
    # assert solve_part_2(puzzle, 1) == 374
    assert solve_part_2(puzzle, 10) == 1030
    assert solve_part_2(puzzle, 100) == 8410
    puzzle = dummy_puzzle("day11.txt")
    assert solve_part_2(puzzle, 1000000) == 742305960572

