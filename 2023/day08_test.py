# TIM 2023
# Advent of Code
# Tag 8: Haunted Wasteland
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day08 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    puzzle = dummy_puzzle("day08_example.txt")
    assert solve_part_1(puzzle) == 2
    puzzle = dummy_puzzle("day08_example2.txt")
    assert solve_part_1(puzzle) == 6



def test_part_2():
    puzzle = dummy_puzzle("day08_example_part2.txt")
    assert solve_part_2(puzzle) == 6

