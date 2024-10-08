# TIM 2023
# Advent of Code
# Tag 12: Hot Springs
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine
import re
import time
from time import perf_counter as pfc
import functools

def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


@functools.cache
def factorial(n):
    return n * factorial(n-1) if n else 1

@functools.cache
def calculate_arrangements(springs, nums):
    if len(nums) == 0:
        return 1 * '#' not in springs
    elif len(springs) == 0 or ('?' not in springs and '#' not in springs):
        return 0
    else:
        first_candidate = re.match(f"^\.*[?#]{{{nums[0]}}}(?!#)", springs)
        prefix = re.match("^\.*#+|^\.*\?", springs)
        if first_candidate is None:
            if re.match("^\.*#", springs):
                return 0
            return calculate_arrangements(springs[len(prefix[0]):], nums)

        first_candidate = first_candidate[0]

        # use first candidate
        res = calculate_arrangements(springs[len(first_candidate) + 1:], nums[1:])

        # dont use first candidate
        res2 = 0
        if not re.match("^\.*#", springs):
            res2 = calculate_arrangements(springs[len(prefix[0]):], nums)
        return res + res2
    return


@functools.cache
def calculate_arrangements5(springs, nums):
    nums *= 5
    springs = ((springs + '?') * 5)[:-1]
    if len(nums) == 0:
        return 1 * '#' not in springs
    elif len(springs) == 0 or ('?' not in springs and '#' not in springs):
        return 0
    else:
        first_candidate = re.match(f"^\.*[?#]{{{nums[0]}}}(?!#)", springs)
        prefix = re.match("^\.*#+|^\.*\?", springs)
        if first_candidate is None:
            if re.match("^\.*#", springs):
                return 0
            return calculate_arrangements(springs[len(prefix[0]):], nums)

        first_candidate = first_candidate[0]

        # use first candidate
        res = calculate_arrangements(springs[len(first_candidate) + 1:], nums[1:])

        # dont use first candidate
        res2 = 0
        if not re.match("^\.*#", springs):
            res2 = calculate_arrangements(springs[len(prefix[0]):], nums)
        return res + res2
    return


def convert_spring(spring):
    # spring = "???.###" => "3.###"
    # spring = "???.#.#" => "3.#.#"
    # spring = "???.#.." => "3.#.."
    for i,x in enumerate(spring):
        if x == ".":
            spring = str(len(spring[:i])) + "." + spring[i + 1:]

    # print(f"Spring: {spring}")


def solve_part_1(puzzle):
    # ['#.#.### 1,1,3', '.#...#....###. 1,1,3',...]
    springs = sum(list(map(lambda x: x.split()[:1], puzzle)), [])
    conv_springs = list(map(convert_spring, springs))
    # print(f"conv springs: {conv_springs}")
    damaged_springs = list(map(lambda x: x.split()[1:], puzzle))
    damaged_springs = sum(damaged_springs, [])
    damaged_springs = list(map(lambda x: x.split(","), damaged_springs))
    damaged_springs = list(map(lambda x: tuple(map(int, x)), damaged_springs))
    springs = list(zip(springs, damaged_springs))



    # print(f"Springs: {springs}")
    # print(f"Damaged Springs: {damaged_springs}")
    arrangements = list(map(lambda x: calculate_arrangements(x[0], x[1]), springs))
    return sum(arrangements)


def solve_part_2(puzzle):
    # ['#.#.### 1,1,3', '.#...#....###. 1,1,3',...]
    springs = sum(list(map(lambda x: x.split()[:1], puzzle)), [])
    conv_springs = list(map(convert_spring, springs))
    # print(f"conv springs: {conv_springs}")
    damaged_springs = list(map(lambda x: x.split()[1:], puzzle))
    damaged_springs = sum(damaged_springs, [])
    damaged_springs = list(map(lambda x: x.split(","), damaged_springs))
    damaged_springs = list(map(lambda x: tuple(map(int, x)), damaged_springs))
    springs = list(zip(springs, damaged_springs))

    # print(f"Springs: {springs}")
    # print(f"Damaged Springs: {damaged_springs}")
    arrangements = list(map(lambda x: calculate_arrangements5(x[0], x[1]), springs))
    return sum(arrangements)


if __name__ == "__main__":
    puzzle = read_puzzle("day12.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

