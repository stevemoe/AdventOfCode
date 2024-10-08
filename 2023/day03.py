# TIM 2023
# Advent of Code
# Tag 3: Gear Ratios
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc
import math
from dataclasses import dataclass
import re



def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def is_symbol(char):
    # print("char",char)
    return not char.isdigit() and char != "."


def is_number(char):
    return char if char.isdigit() else " "


def find_symbol(puzzle):
    symbols = list(map(is_symbol, puzzle))
    return list(map(lambda x: x[0] if x[1] else 0, enumerate(symbols)))


def symbol_next_to_number(symbols, puzzle):
    return True


def sum_of_numbers(sublist):
    total = 0
    for item in sublist:
        if item.isdigit():  # Überprüfe, ob der Eintrag eine Zahl ist
            total += int(item)  # Addiere die Zahl zur Gesamtsumme hinzu
    return total


def find_number(symbols, puzzle):
    symbols_line = symbols[0]
    print("symbols1", symbols[1])
    symbols = list(filter(lambda x: x is not 0, symbols[1]))
    print(symbols)
    numbers = []
    if len(symbols) != 0:
        for symbol in symbols:
            print("symbols_line", symbols_line)
            line_above = puzzle[symbols_line - 1]
            same_line = puzzle[symbols_line]
            line_under = puzzle[symbols_line + 1]
            for x in range(-1, 2):
                # print("line_above", line_above[x])
                if line_above[symbol + x].isdigit():
                    print("line_above", line_above[symbol + x])
                    print("number_above", line_above[symbol + x - 2:symbol + x + 1])
                    print("".join(filter(lambda x: x.isdigit(), line_above[symbol + x - 2:symbol + x + 1])))
                    if x == -1:
                        numbers.append(
                            "".join(filter(lambda x: x.isdigit(), line_above[symbol + x - 2:symbol + x + 1])))
                    elif x == 0:
                        numbers.append(
                            "".join(filter(lambda x: x.isdigit(), line_above[symbol + x - 1:symbol + x + 2])))
                    else:
                        numbers.append(
                            "".join(filter(lambda x: x.isdigit(), line_above[symbol + x - 1:symbol + x + 3])))
                if same_line[symbol + x].isdigit():
                    print("same_line", same_line[symbol + x])
                    print("number_same", same_line[symbol + x - 2:symbol + x + 2])
                    numbers.append("".join(filter(lambda x: x.isdigit(), same_line[symbol + x - 2:symbol + x + 2])))
                if line_under[symbol + x].isdigit():
                    print("line_under", line_under[symbol + x])
                    print("number_under", line_under[symbol + x - 2:symbol + x + 2])
                    if x == -1:
                        numbers.append(
                            "".join(filter(lambda x: x.isdigit(), line_under[symbol + x - 2:symbol + x + 1])))
                    elif x == 0:
                        numbers.append(
                            "".join(filter(lambda x: x.isdigit(), line_under[symbol + x - 1:symbol + x + 2])))
                    else:
                        numbers.append(
                            "".join(filter(lambda x: x.isdigit(), line_under[symbol + x - 1:symbol + x + 2])))

                # print("line_above", line_above[symbol])
                # print("line_above", line_above[symbol+1])

            print("numbers", set(numbers))

        # print(list(filter(lambda x: x[1], puzzle[symbols])))
    return list(set(numbers))


def solve_part_1(puzzle):
    line = list(map(lambda x: x.split("."), puzzle))
    print(line)
    numbers = list(map(int, filter(lambda x: x.isdigit(), puzzle)))
    print(puzzle)
    symbols = list(enumerate(map(find_symbol, puzzle)))
    print("symbols", symbols)

    numbers = list(map(lambda x: find_number(x, puzzle), symbols))
    print("numbers", numbers)
    return sum(sum_of_numbers(sublist) for sublist in numbers)


def solve_part_2(puzzle):
    return puzzle






if __name__ == "__main__":
    text = "617*44..."

    pattern = r'\d{1,3}'
    matches = re.findall(pattern, text)

    print("matches")
    print(matches)

    puzzle = read_puzzle("day03.txt")
    # start = pfc()
    # result1 = solve_part_1(puzzle)
    # print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    # start = pfc()
    # result2 = solve_part_2(puzzle)
    # print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
