# TIM 2023
# Advent of Code
# Tag 1: Trebuchet?!
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def is_int(char):
    return True if char.isdigit() else False


def extract_values(calibration_text, part):
    value = []
    if part == 1:
        value = list(map(lambda x: int(x), (filter(is_int, calibration_text))))
    else:
        value = find_numbers(calibration_text)
    value = (value[0] * 10) + (value[-1])
    print("value:", value)
    return int(value)


def find_numbers(calibration_text):
    print(list(enumerate(calibration_text)))
    value = list(filter(lambda x: x is not None, (map(lambda char: is_number(char, calibration_text), enumerate(calibration_text)))))
    print("value:", value)
    return value


def is_number(char, calibration_text):
    numbers_as_strings = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    if is_int(char[1]):
        return int(char[1])
    else:
        for number in numbers_as_strings:
            if number == calibration_text[slice(char[0], char[0] + len(number))]:
                print(char[1], number, calibration_text[slice(char[0], char[0] + len(number))])
                print(numbers_as_strings[number])
                num = numbers_as_strings[number]
                print("num", num)
                return num
    return None


def count_values(puzzle, part):
    return sum(map(lambda calibration_text: extract_values(calibration_text, part), puzzle))


def solve_part_1(puzzle):
    return count_values(puzzle, 1)


def solve_part_2(puzzle):
    solution = count_values(puzzle, 2)
    return solution


if __name__ == "__main__":
    puzzle = read_puzzle("day01.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
