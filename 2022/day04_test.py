# TIM 2022
# Advent of Code
# Tag 1: Aufgabenname
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day04 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle():
    return read_puzzle("day04_example1.txt")


def test_part_1():
    puzzle = dummy_puzzle()
    assert solve_part_1(puzzle) == 2


def test_part_2():
    puzzle = dummy_puzzle()
    assert solve_part_2(puzzle) == 2