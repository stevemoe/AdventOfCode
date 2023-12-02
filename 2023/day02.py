# TIM 2023
# Advent of Code
# Tag 2: Cube Conundrum
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from math import prod
from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return list(map(lambda x: x.split(":")[1], f.read().splitlines()))  # remove "Game 1:" etc. from input


def get_power_of_set(game):
    draws = list(map(lambda x: reversed(tuple(x.split(" "))), map(str.strip, game.replace(";", ",").split(","))))
    min_load = {"red": 0, "green": 0, "blue": 0}
    for cube in draws:
        color, value = cube
        if min_load[color] < int(value):
            min_load[color] = int(value)
    return prod(min_load.values())


def control_set(game_set):
    cubes = {"red": 12, "green": 13, "blue": 14}
    set_tuples = list(map(lambda x: tuple(x.split(" ")), map(str.strip, game_set.split(","))))
    possible = list(map(lambda x: int(x[0]) <= cubes[x[1]], set_tuples))
    return False not in possible


def get_sets(game):
    return list(map(control_set, map(str.strip, game.split(";"))))


def solve_part_1(puzzle):
    return sum(list(map(lambda x: x[0] + 1 if False not in get_sets(x[1]) else 0, enumerate(puzzle))))


def solve_part_2(puzzle):
    return sum(list(map(get_power_of_set, puzzle)))


if __name__ == "__main__":
    puzzle = read_puzzle("day02.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
