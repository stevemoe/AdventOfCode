# TIM 2023
# Advent of Code
# Tag 4: Scratchcards
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine
from functools import reduce
from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return list(map(lambda x: x.split(":")[1], f.read().splitlines()))


def calculate_points(matching_numbers):
    return reduce(lambda points, x: points + 1 if points == 0 else points * 2, matching_numbers, 0)


def get_matching_numbers(game):
    winning_numbers = game.split("|")[0].split()
    own_numbers = game.split("|")[1].split()
    return list(filter(lambda x: x in winning_numbers, own_numbers))


def get_winning_points(card):
    return calculate_points(get_matching_numbers(card))


def add_up_matching_numbers(game):
    return tuple((game, len(get_matching_numbers(game))))


def solve_part_1(puzzle):
    return sum(map(get_winning_points, puzzle))


def solve_part_2(puzzle):
    puzzle_dict = dict(map(lambda x: (x, 1), puzzle))
    for card in enumerate(puzzle):
        win = add_up_matching_numbers(card[1])
        for x in range(1, puzzle_dict[win[0]] + 1):
            for y in range(1, win[1] + 1):
                puzzle_dict[puzzle[card[0] + y]] += 1
    return sum(puzzle_dict.values())


if __name__ == "__main__":
    puzzle = read_puzzle("day04.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
