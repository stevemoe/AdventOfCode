# TIM 2023
# Advent of Code
# Tag 5: If You Give A Seed A Fertilizer
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine
from functools import reduce
from time import perf_counter as pfc
import re


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().split("\n\n")


def find_corresponding_soil_number():
    soil_number = 81
    return soil_number


def calculate_conversion_range(puzzle):
    conversion_range = {"start": 98, "end": 99}
    return conversion_range


def get_seeds(puzzle):
    seed_line = list(filter(lambda x: x.startswith("seeds: "), puzzle))
    matches = re.search(r"(?<=seeds: )(\d+ ?)+", puzzle[0])
    seeds = matches.group(0).split() if matches else []
    return seeds


def get_conversion_tuples(conversion_text):
    target, source, range_length = conversion_text
    # print(source, target, range_length)
    conversion_tuples = []
    for i in range(int(range_length)):
        conversion_tuples.append((int(source) + i, int(target) + i))
        # print(conversion_tuples)

    return conversion_tuples


def seed_in_conversion_map(seed, conversion_map):
    for conversion in conversion_map:
        for conversion_tuple in conversion:
            if seed == conversion_tuple[0]:
                return conversion_tuple[1]
    return seed


def get_seed_to_soil(source, conversions):
    text = conversions.splitlines()
    text = list(map(lambda x: x.strip(), text))
    conversion_text = list(map(lambda x: x.split(), filter(lambda x: x[0].isdigit(), text)))
    conversion_map = list(tuple(map(get_conversion_tuples, conversion_text)))
    new_source = list(map(lambda seed: seed_in_conversion_map(int(seed), conversion_map), source))
    return new_source


def solve_part_1(puzzle):
    find_corresponding_soil_number()
    seeds = get_seeds(puzzle)
    location_numbers = list(reduce(lambda seed, conversions: get_seed_to_soil(seed, conversions), puzzle[1:], seeds))
    print(location_numbers)
    print(min(location_numbers))
    return min(location_numbers)


def solve_part_2(puzzle):
    return puzzle


if __name__ == "__main__":
    puzzle = read_puzzle("day05.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
