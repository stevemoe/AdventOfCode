# TIM 2023
# Advent of Code
# Tag 21: Step Counter
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day21 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day21_example.txt")
    assert solve_part_1(puzzle,6) == 16


def test_part_2():
    puzzle = dummy_puzzle("day21_example.txt")
    assert solve_part_2(puzzle, 6) == 16
    assert solve_part_2(puzzle, 10) == 50
    assert solve_part_2(puzzle, 50) == 1594
    # assert solve_part_2(puzzle, 100) == 6536
    # assert solve_part_2(puzzle, 500) == 167004
    # assert solve_part_2(puzzle, 1000) == 668697
    # assert solve_part_2(puzzle, 5000) == 16733044

