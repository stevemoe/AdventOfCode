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


def get_matching_numbers(game):
    winning_numbers = game.split("|")[0].split()
    own_numbers = game.split("|")[1].split()
    return list(filter(lambda x: x in winning_numbers, own_numbers))


def calculate_winning_points(card):
    return reduce(lambda points, x: points + 1 if points == 0 else points * 2, get_matching_numbers(card), 0)


def get_card_count(dict, card):
    return dict[card[1]]


def solve_part_1(puzzle):
    return sum(map(calculate_winning_points, puzzle))


def solve_part_2(puzzle):
    puzzle_dict = dict(map(lambda numbers: (numbers, 1), puzzle))
    for card in enumerate(puzzle):
        match_count = len(get_matching_numbers(card[1]))
        for match in range(1, match_count + 1):
            index = card[0] + match
            puzzle_dict[puzzle[index]] += get_card_count(puzzle_dict, card)
    return sum(puzzle_dict.values())


if __name__ == "__main__":
    puzzle = read_puzzle("day04.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
