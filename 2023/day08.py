# TIM 2023
# Advent of Code
# Tag 8: Haunted Wasteland
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def removew(puzzle):
        return list(map(lambda line: "".join(list(map(lambda x: x.strip(), line.split()))), puzzle))



def solve_part_1(puzzle):
    # print(f"puzzle: {puzzle}")
    puzzle = removew(puzzle)
    steps_total = 0
    left_right = puzzle[0]
    steps_dict = {"L": 0, "R": 1}
    nav = dict(map(lambda x: tuple(x.split("=")) , filter(lambda x: "=" in x, puzzle)))
    # nav: {'AAA': '(BBB,CCC)'} -> nav: {'AAA': ['BBB', 'CCC']}
    nav = dict(map(lambda x: (x[0], x[1].strip("()").split(",")), nav.items()))
    node = "AAA"
    maze_end = "ZZZ"
    while node != maze_end:
        for index, step in enumerate(left_right):
            # print(f"step: {step}, nav: {nav[node][steps_dict[step]]}")
            node = nav[node][steps_dict[step]]
            if node == "ZZZ":
                steps_total += 1
                break
            steps_total += 1

    return steps_total


def solve_part_2(puzzle):
    puzzle = removew(puzzle)
    steps_total = 0
    left_right = puzzle[0]
    steps_dict = {"L": 0, "R": 1}
    nav = dict(map(lambda x: tuple(x.split("=")), filter(lambda x: "=" in x, puzzle)))
    # nav: {'AAA': '(BBB,CCC)'} -> nav: {'AAA': ['BBB', 'CCC']}
    nav = dict(map(lambda x: (x[0], x[1].strip("()").split(",")), nav.items()))
    maze_start = list(filter(lambda x: x[-1] == "A", nav.keys()))
    # print(f"maze_start: {maze_start}")
    nodes = list(filter(lambda x: x[-1] == "A", nav.keys()))
    maze_end = any(list(map(lambda x: x[-1] == "Z", nodes)))
    # print(f"maze_end: {maze_end}")

    while not maze_end:
        for index, step in enumerate(left_right):
            # print(f"step: {step}, nav: {nav[maze][steps_dict[step]]}")

            nodes = list(map(lambda x: nav[x][steps_dict[step]], nodes))
            if all(list(map(lambda x: x[-1] == "Z", nodes))):
                print(list(map(lambda x: x[-1] == "Z", nodes)))
                maze_end = True
                steps_total += 1
                break
            steps_total += 1
            print(f"steps_total: {steps_total}")
    return steps_total


if __name__ == "__main__":
    puzzle = read_puzzle("day08.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

