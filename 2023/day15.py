# TIM 2023
# Advent of Code
# Tag 15: Lens Library
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from functools import reduce
from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()[0].split(",")


def calc_hash(step):
    return reduce(lambda a, b: ((a + b) * 17) % 256, map(lambda x: ord(x), step), 0)


def solve_part_1(puzzle):
    return sum(map(calc_hash, puzzle))


def solve_part_2(puzzle):
    boxes = list(map(lambda x: {}, range(256)))
    for step in puzzle:
        if "-" in step:
            label = step[:-1]
            box = boxes[calc_hash(label)]
            if label in box:
                box.pop(label)
        else:
            label, focal = step.split("=")
            box = boxes[calc_hash(label)]
            box[label] = int(focal)



    focusing_power = 0
    for box in boxes:
        for index, (label, focal) in enumerate(box.items()):
            focusing_power += (boxes.index(box) + 1) * (index + 1) * focal
    return focusing_power


if __name__ == "__main__":
    puzzle = read_puzzle("day15.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
