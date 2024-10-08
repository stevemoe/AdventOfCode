# TIM 2023
# Advent of Code
# Tag 14: Parabolic Reflector Dish
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def transpose(puzzle):
    return list(map(list, zip(*puzzle)))


def solve_part_1(puzzle):
    ctr, puzzle = tilt_north(puzzle)
    return ctr


def show_puzzle(puzzle):
    puzzle_show = list(map(lambda x: "".join(x), puzzle))
    print(f"puzzle_temp_show: \n{"\n".join(puzzle_show)}")


def tilt_north(puzzle):
    puzzle = transpose(puzzle)
    puzzle_tmp = []
    # print(f"puzzle: {puzzle}")
    ctr = 0
    for line in puzzle:
        # print(f"line: {line}")
        stone_moved = True
        while stone_moved:
            stone_moved = False
            for i in range(len(line) - 1):
                if line[i] == "." and line[i + 1] == "O":
                    # print(f"i: {i}")
                    val1 = line.pop(i)
                    val2 = line.pop(i)
                    line.insert(i, val2)
                    line.insert(i + 1, val1)
                    # print(f"line after pop: {line}")
                    stone_moved = True
            if not stone_moved:
                for index, char in enumerate(line):
                    if char == "O":
                        ctr += len(line) - index
        puzzle_tmp.append(line)
    return ctr, puzzle_tmp


def tilt_west(puzzle):
    puzzle_tmp = []
    # print(f"puzzle: {puzzle}")
    ctr = 0
    for line in puzzle:
        # print(f"line: {line}")
        stone_moved = True
        while stone_moved:
            stone_moved = False
            for i in range(len(line) - 1):
                if line[i] == "." and line[i + 1] == "O":
                    # print(f"i: {i}")
                    val1 = line.pop(i)
                    val2 = line.pop(i)
                    line.insert(i, val2)
                    line.insert(i + 1, val1)
                    # print(f"line after pop: {line}")
                    stone_moved = True
            if not stone_moved:
                for index, char in enumerate(line):
                    if char == "O":
                        ctr += len(line) - index
        puzzle_tmp.append(line)
    return ctr, puzzle_tmp


def tilt_south(puzzle):
    # print("tilt_south------------------")
    # show_puzzle(puzzle[::-1])
    puzzle = transpose(puzzle[::-1])
    # show_puzzle(puzzle)
    puzzle_tmp = []
    # print(f"puzzle: {puzzle}")
    ctr = 0
    for line in puzzle:
        # print(f"line: {line}")
        stone_moved = True
        while stone_moved:
            stone_moved = False
            for i in range(len(line) - 1):
                if line[i] == "." and line[i + 1] == "O":
                    # print(f"i: {i}")
                    val1 = line.pop(i)
                    val2 = line.pop(i)
                    line.insert(i, val2)
                    line.insert(i + 1, val1)
                    # print(f"line after pop: {line}")
                    stone_moved = True
            if not stone_moved:
                for index, char in enumerate(line):
                    if char == "O":
                        ctr += len(line) - index
        puzzle_tmp.append(line)
    puzzle_tmp = transpose(puzzle_tmp)
    # show_puzzle(puzzle_tmp)
    puzzle_tmp = puzzle_tmp[::-1]

    return ctr, puzzle_tmp


def tilt_east(puzzle):
    puzzle_tmp = []
    # print(f"puzzle: {puzzle}")
    ctr = 0
    for line in puzzle:
        # print(f"line: {line}")
        stone_moved = True
        while stone_moved:
            stone_moved = False
            for i in range(len(line) - 1):
                if line[i] == "." and line[i + 1] == "O":
                    # print(f"i: {i}")
                    val1 = line.pop(i)
                    val2 = line.pop(i)
                    line.insert(i, val2)
                    line.insert(i + 1, val1)
                    # print(f"line after pop: {line}")
                    stone_moved = True
            if not stone_moved:
                for index, char in enumerate(line):
                    if char == "O":
                        ctr += len(line) - index
        puzzle_tmp.append(line)
    puzzle_tmp = list(map(lambda x: list(reversed(x)), puzzle_tmp))
    return ctr, puzzle_tmp


def solve_part_2(puzzle):
    target = 1000000000
    puzzle_temp = puzzle
    ctr = 0
    first_cycle = []
    cycles = []
    cycles_true = []
    while True:
        ctr, puzzle = tilt_north(puzzle)
        # show_puzzle(transpose(puzzle))

        puzzle = transpose(puzzle)

        ctr, puzzle = tilt_west(puzzle)
        # show_puzzle(puzzle)

        ctr, puzzle = tilt_south(puzzle)
        # print(f"after south")
        # show_puzzle(puzzle)

        puzzle = list(map(lambda x: list(reversed(x)), puzzle))

        ctr, puzzle = tilt_east(puzzle)
        if puzzle in cycles:
            print(f"same")
            ctr = 0
            for i, line in enumerate(puzzle[::-1]):
                ctr += line.count("O") * (i + 1)
            if puzzle in cycles_true:
                print(f"same true")
                break
            cycles_true.append(puzzle)
        cycles.append(puzzle)
        # print(f"ctr: {ctr}")
    print(f"len(cycles): {len(cycles)}")
    print(f"1000000000 / {len(cycles_true)}: {1000000000 / len(cycles_true)}")
    for cycle in cycles_true:
        print(f"cycle: {cycles_true.index(cycle)}")
        ctr = 0
        for i, line in enumerate(cycle[::-1]):
            ctr += line.count("O") * (i + 1)
        print(f"ctr: {ctr}")
    ctr = 0
    for i, line in enumerate(cycles_true[len(cycles_true)-(len(cycles) - len(cycles_true)) -2][::-1]):
        ctr += line.count("O") * (i + 1)
    print(f"ctr: {ctr}")
    show_puzzle(first_cycle)
    show_puzzle(puzzle)
    return ctr


if __name__ == "__main__":
    puzzle = read_puzzle("day14.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
