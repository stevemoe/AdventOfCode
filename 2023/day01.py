# TIM 2023
# Advent of Code
# Tag 1: Trebuchet?!
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def combine_numbers_to_value(value):
    return (value[0] * 10) + value[-1]


def extract_values_from_digits(text):
    numbers = list(map(lambda x: int(x), filter(lambda char: char.isdigit(), text)))
    return combine_numbers_to_value(numbers)


def extract_values_from_text(text):
    numbers = list(filter(lambda x: x is not None,
                          map(lambda char: translate_numbers_from_text(char[1], char[0], text), enumerate(text))))
    return combine_numbers_to_value(numbers)


def translate_numbers_from_text(char, index, text):
    numbers_as_strings = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                          "nine": 9}
    if char.isdigit():
        return int(char)
    else:
        for number in numbers_as_strings:
            if char == number[0] and number == text[index:index + len(number)]:
                return numbers_as_strings[number]


def add_up_values(puzzle, part):
    return sum(
        map(lambda calibration_text: extract_values_from_digits(
            calibration_text) if part == 1 else extract_values_from_text(
            calibration_text), puzzle))


def solve_part_1(puzzle):
    return add_up_values(puzzle, 1)


def solve_part_2(puzzle):
    return add_up_values(puzzle, 2)


if __name__ == "__main__":
    puzzle = read_puzzle("day01.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
