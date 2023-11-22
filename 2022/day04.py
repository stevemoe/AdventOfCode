# TIM 2023
# Advent of Code
# Tag 1: Aufgabenname
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()

def compare_shifts(shift):
    shift_1 = shift[:shift.find(",")]
    shift_2 = shift[shift.find(",") + 1:]
    shift_1 = {"start": shift_1[:shift_1.find("-")], "end": shift_1[shift_1.find("-") + 1:]}
    shift_2 = {"start": shift_2[:shift_2.find("-")], "end": shift_2[shift_2.find("-") + 1:]}
    if shift_1["start"] >= shift_2["start"] and shift_1["end"] <= shift_2["end"] or shift_2["start"] >= shift_1["start"] and shift_2["end"] <= shift_1["end"]:
        print(shift_1, shift_2)
        return True
    # elif shift_2["start"] >= shift_1["start"] and shift_2["end"] <= shift_1["end"]:
    #     print(shift_1, shift_2)
    #     return True
    else:
        return False

def solve_part_1(puzzle):
    assignment_pairs = len(list(filter(compare_shifts, puzzle)))
    return assignment_pairs


def solve_part_2(puzzle):
    return 2


if __name__ == "__main__":
    puzzle = read_puzzle("day04.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
