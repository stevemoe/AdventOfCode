# TIM 2023
# Advent of Code
# Tag 6: Tuning Trouble
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day06 import solve_part_1, solve_part_2, read_puzzle

test = "test"
def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    assert solve_part_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert solve_part_1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert solve_part_1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert solve_part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert solve_part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_part_2():
    assert solve_part_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == None
    assert solve_part_2("bvwbjplbgvbhsrlpgdmjqwftvncz") == None
    assert solve_part_2("nppdvjthqldpwncqszvftbrmjlhg") == None
    assert solve_part_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == None
    assert solve_part_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == None

