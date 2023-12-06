# TIM 2023
# Advent of Code
# Tag 6: Wait For It
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from math import prod, sqrt
from time import perf_counter as pfc
from colorama import init, Fore


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def possible_ways_to_win(time, distance):
    wins = []
    for charge_duration in range(time + 1):
        boat_distance = (time - charge_duration) * charge_duration
        draw_vertical_line(boat_distance, distance)
        if boat_distance > distance:
            wins.append(charge_duration)
    return len(wins)


def solve_quadratic_formula(time, distance):
    root = sqrt(time ** 2 - (4 * ((-distance) * -1)))
    x1 = (-time + root) / (2 * -1)
    x2 = (-time - root) / (2 * -1)
    return x1, x2


def calculate_win_count(time, distance):
    x1, x2 = solve_quadratic_formula(time, distance)
    return int(max(x1, x2) - min(x1, x2))


def draw_vertical_line(length, distance):
    if distance <= 300:
        win = length > distance
        print(Fore.__dict__["GREEN" if win else "RED"] + '-' * int(length / 1) + Fore.RESET)


def solve_part_1(puzzle):
    times = list(map(int, puzzle[0].split()[1:]))
    distances = list(map(int, puzzle[1].split()[1:]))
    number_of_wins_per_race = list(map(lambda time, distance: possible_ways_to_win(time, distance), times, distances))
    return prod(number_of_wins_per_race)


def solve_part_2(puzzle):
    time, distance = (int(line.split(':')[1:][0].replace(' ', '')) for line in puzzle)
    return calculate_win_count(time, distance)


if __name__ == "__main__":
    init(autoreset=True)
    puzzle = read_puzzle("day06.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
