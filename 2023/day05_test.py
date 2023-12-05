# TIM 2023
# Advent of Code
# Tag 5: If You Give A Seed A Fertilizer
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day05 import solve_part_1, solve_part_2, read_puzzle, find_corresponding_soil_number, calculate_conversion_range


def dummy_puzzle(filename):
    return read_puzzle(filename)


# def test_calculate_conversion_range():
#     assert calculate_conversion_range("50 98 2") == {"start": 98, "end": 99}
#     assert calculate_conversion_range("52 50 48") == {"start": 52, "end": 99}


def test_part_1():
    puzzle = dummy_puzzle("day05_example.txt")
    assert solve_part_1(puzzle) == 35


def test_part_2():
    puzzle = dummy_puzzle("day05_example.txt")
    assert solve_part_2(puzzle) == None

