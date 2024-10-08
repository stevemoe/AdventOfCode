# TIM 2023
# Advent of Code
# Tag 21: Step Counter
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def solve_part_1(puzzle, number_of_steps):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    starting_points = []

    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == "S":
                starting_points.append((x, y))
                print(f"Found S at {x},{y}")
    for i in range(number_of_steps):
        points_new = []
        for points in starting_points:
            x, y = points
            for direction in directions:
                dx, dy = direction
                # print(f"Checking {x+dx},{y+dy}")
                if puzzle[y + dy][x + dx] == "." or puzzle[y + dy][x + dx] == "S":
                    points_new.append((x + dx, y + dy))
        starting_points = set(points_new)
    print(starting_points)
    return len(starting_points)


def is_oor(x, y, puzzle):
    if x < 0 or y < 0:
        return True
    if x >= len(puzzle[0]) or y >= len(puzzle):
        return True
    return False


def solve_part_2(puzzle, number_of_steps):
    puzzle_extended = []
    for line in puzzle:
        puzzle_extended.append(line * 3)
    puzzle_extended = puzzle_extended * 3
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    starting_points = []

    for y, line in enumerate(puzzle_extended):
        for x, char in enumerate(line):
            len_x = len(puzzle_extended[0])
            len_y = len(puzzle_extended)
            if char == "S" and int((len_x / 3)) < x < (int((len_x / 3 * 2))) and (int((len_y / 3))) < y < (
            int((len_y / 3 * 2))):
                starting_points.append((x, y))
    for i in range(number_of_steps):
        points_new = []
        for points in starting_points:
            x, y = points
            for direction in directions:
                dx, dy = direction
                # if is_oor(x + dx, y + dy, puzzle_extended):
                    # print(f"Checking {x + dx},{y + dy}")
                if not is_oor(x + dx, y + dy, puzzle_extended) and (
                        puzzle_extended[y + dy][x + dx] == "." or puzzle_extended[y + dy][x + dx] == "S"):
                    points_new.append((x + dx, y + dy))
        starting_points = set(points_new)
    print(starting_points)
    return len(starting_points)


if __name__ == "__main__":
    puzzle = read_puzzle("day21.txt")
    start = pfc()
    result1 = solve_part_1(puzzle, 64)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle, 26501365)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
