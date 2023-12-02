# TIM 2023
# Advent of Code
# Tag 2: Cube Conundrum
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine
from functools import reduce
from math import prod
from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def control_set_2(game_set):

    print("set_tuples", game_set)
    possible = list(map(lambda x: int(x[0]) <= loads[x[1]], set_tuples))
    return False if False in possible else True


def count_cubes(game):
    game = game.replace(";", ",")
    sets = list(map(lambda x: tuple(x.split(" ")), map(str.strip, game.split(","))))
    # print(sets)
    min_load = {"red": 0, "green": 0, "blue": 0}
    for set in sets:
        if min_load[set[1]] < int(set[0]):
            min_load[set[1]] = int(set[0])
        else:
            None
    # possible_sets = list(map(lambda x: ((min_load[x[1]] = x[0]) if min_load[x[1]] < x[0] else (min_load[x[1]] ), sets))
    print(min_load)
    print(prod(min_load.values()))
    return prod(min_load.values())


def control_set(game_set):
    loads = {"red": 12, "green": 13, "blue": 14}
    set_tuples = list(map(lambda x: tuple(x.split(" ")), map(str.strip, game_set.split(","))))
    possible = list(map(lambda x: int(x[0]) <= loads[x[1]], set_tuples))
    return False if False in possible else True


def get_sets(game):
    sets = list(map(str.strip, game.split(";")))
    possible_sets = list(map(control_set, sets))
    return possible_sets

def solve_part_1(puzzle):
    games = list(map(lambda x: x.split(":")[1], puzzle))
    print("games:", games)
    ctr = 0
    solution = list(map(lambda x: x[0] + 1 if False not in get_sets(x[1]) else 0, enumerate(games)))
    print(solution)
    return sum(solution)


def solve_part_2(puzzle):
    games = list(map(lambda x: x.split(":")[1], puzzle))
    solution = list(map(count_cubes, games))
    return sum(solution)


if __name__ == "__main__":
    puzzle = read_puzzle("day02.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
