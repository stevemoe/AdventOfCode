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


def calculate_conversion_range(conversion_text):
    conversion_range = {"source": int(conversion_text[1]), "length": int(conversion_text[-1]),
                        "target": int(conversion_text[0])}
    return conversion_range


def get_seeds(puzzle):
    # seed_line = list(filter(lambda x: x.startswith("seeds: "), puzzle))
    matches = re.search(r"(?<=seeds: )(\d+ ?)+", puzzle[0])
    seeds = matches.group(0).split() if matches else []
    return seeds


def get_seeds_from_range(puzzle):
    # seed_line = list(filter(lambda x: x.startswith("seeds: "), puzzle))
    matches = re.findall(r"(\d+)\s+(\d+)", puzzle[0])
    seed_list = []
    seeds = list((int(match[0]), int(match[1])) for match in matches)
    print(seeds)
    seed_ranges = []
    for seed in seeds:
        # print(seed[0], "min - max", seed[0] + seed[1])
        seed_ranges.append(range(seed[0], seed[0] + seed[1]))
        for i in range(seed[1]):
            seed_list.append(seed[0] + i)

    # # print(seed_ranges)
    # for index, seed_range in enumerate(seed_ranges):
    #     for i in range(1 + index, len(seed_ranges)):
    #         filtered = range(max(seed_range[0], seed_ranges[i][0]), min(seed_range[-1], seed_ranges[i][-1]) + 1)

    return set(seed_list)


def seed_in_range(seed, calc_ranges):
    for calc_range in calc_ranges:
        calc_range = calculate_conversion_range(calc_range)
        if calc_range["source"] <= seed <= calc_range["source"] + calc_range["length"]:
            return (seed - calc_range["source"]) + calc_range["target"]
    return seed


def solve_part_1(puzzle):
    seeds = get_seeds(puzzle)
    conversions = puzzle[1:]
    location_list = []
    for seed in seeds:
        source = seed
        for conversion in conversions:
            text = conversion.splitlines()
            text = list(map(lambda x: x.strip(), text))

            conversion_text = list(map(lambda x: x.split(), filter(lambda x: x[0].isdigit(), text)))
            source = seed_in_range(int(source), conversion_text)
        location_list.append(source)
    return min(location_list)


def apply_range(seed_range, conversion):
    intersected_ranges = []
    for (destination, source, length) in conversion:
        src_end = source + length
        filtered_ranges = []
        while seed_range:
            (start, end) = seed_range.pop()
            before = (start, min(end, source))
            inter = (max(start, source), min(src_end, end))
            after = (max(src_end, start), end)
            if before[1] > before[0]:
                filtered_ranges.append(before)
            if inter[1] > inter[0]:
                intersected_ranges.append((inter[0] - source + destination, inter[1] - source + destination))
            if after[1] > after[0]:
                filtered_ranges.append(after)
        seed_range = filtered_ranges
    return intersected_ranges + seed_range


def solve_part_2(puzzle):
    matches = re.findall(r"(\d+)\s+(\d+)", puzzle[0])
    seeds = list((int(match[0]), int(match[1])) for match in matches)
    location_list = []
    for start, length in seeds:
        seed_range = [(start, start + length)]
        for f in puzzle[1:]:
            conversion = list((int(match[0]), int(match[1]), int(match[-1])) for match in re.findall(r"(\d+)\s+(\d+)\s(\d+)", f))
            # print(conversion)   # [(50, 98, 2), (52, 50, 48)]
            seed_range = apply_range(seed_range, conversion)

        location_list.append(min(seed_range)[0])

    return min(location_list)


if __name__ == "__main__":
    puzzle = read_puzzle("day05.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
