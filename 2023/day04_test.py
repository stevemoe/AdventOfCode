# TIM 2023
# Advent of Code
# Tag 4: Scratchcards
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day04 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day04_example.txt")
    assert solve_part_1(puzzle) == 13
    puzzle = dummy_puzzle("day04.txt")
    assert solve_part_1(puzzle) == 23750


def test_part_2():
    puzzle = dummy_puzzle("day04_example.txt")
    assert solve_part_2(puzzle) == 30
    puzzle = dummy_puzzle("day04.txt")
    assert solve_part_2(puzzle) == 13261850

