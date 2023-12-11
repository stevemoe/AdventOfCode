# TIM 2023
# Advent of Code
# Tag 11: Cosmic Expansion
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def manhatten_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y2 - y1)


def calc_expansion(puzzle):
    expand_lines = [x for x, line in enumerate(puzzle) if all(char == "." for char in line)]
    expand_cols = [col for col in range(len(puzzle[0])) if all(puzzle[row][col] == "." for row in range(len(puzzle)))]
    return {"lines": expand_lines, "cols": expand_cols}


def find_galaxy_coords(puzzle):
    galaxies = []
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))
    return galaxies


def calculate_distances(galaxies, expansions, expansion):
    distances = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            (x1, y1), (x2, y2) = galaxies[i], galaxies[j]
            man_dist = manhatten_distance(x1, y1, x2, y2)
            for exp_col in expansions["cols"]:
                if x1 < exp_col < x2:
                    man_dist += expansion - 1
                elif x2 < exp_col < x1:
                    man_dist += expansion - 1
            for exp_line in expansions["lines"]:
                if y1 < exp_line < y2:
                    man_dist += expansion - 1
            distances.append(man_dist)
    return distances


def solve_part_1(puzzle, expansion=1):
    expansions = calc_expansion(puzzle)
    galaxies = find_galaxy_coords(puzzle)
    return sum(calculate_distances(galaxies, expansions, expansion))


def solve_part_2(puzzle, expansion=1):
    expansions = calc_expansion(puzzle)
    galaxies = find_galaxy_coords(puzzle)
    return sum(calculate_distances(galaxies, expansions, expansion))


if __name__ == "__main__":
    puzzle = read_puzzle("day11.txt")
    start = pfc()
    result1 = solve_part_1(puzzle, 2)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    puzzle = read_puzzle("day11.txt")
    start = pfc()
    result2 = solve_part_2(puzzle, 1000000)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
