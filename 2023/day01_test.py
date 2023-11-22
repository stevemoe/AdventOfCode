# TIM 2022
# Advent of Code
# Tag 1: Aufgabenname
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day01 import solve_part_1, solve_part_2


def dummy_puzzle():
    return ["Dies", "ist", "ein", "Test"]


def test_part_1():
    puzzle = dummy_puzzle()
    assert solve_part_1(puzzle) == ["Dies", "ist", "ein", "Test"]


def test_part_2():
    puzzle = dummy_puzzle()
    assert solve_part_2(puzzle) == 2