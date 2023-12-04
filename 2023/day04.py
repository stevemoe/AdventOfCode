# TIM 2023
# Advent of Code
# Tag 4: Scratchcards
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from functools import reduce
from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return list(map(lambda x: x.split(":")[1], f.read().splitlines()))  # remove "Card 1:" etc. from input


def get_matching_numbers(card):
    winning_numbers = card.split("|")[0].split()
    own_numbers = card.split("|")[1].split()
    return list(filter(lambda x: x in winning_numbers, own_numbers))


def calculate_winning_points(card):
    return reduce(lambda points, x: points + 1 if points == 0 else points * 2, get_matching_numbers(card), 0)


def initialize_card_dict(puzzle):
    return {card: 1 for card in puzzle}


def get_card_count(card_dict, card):
    return card_dict[card]


def update_card_count(card, card_dict, key):
    print(key, "=", card_dict[key], "=>", get_card_count(card_dict, card))
    card_dict[key] += get_card_count(card_dict, card)
    print(card_dict[key])
    print("------------------")


def solve_part_1(puzzle):
    return sum(map(calculate_winning_points, puzzle))


def solve_part_2(puzzle):
    card_dict = initialize_card_dict(puzzle)
    for card_index, card in enumerate(puzzle):
        match_count = len(get_matching_numbers(card))
        for match in range(1, match_count + 1):
            print(card, "match_count =", match, "/", match_count)
            update_card_count(card, card_dict, puzzle[card_index + match])
    return sum(card_dict.values())


if __name__ == "__main__":
    puzzle = read_puzzle("day04.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
