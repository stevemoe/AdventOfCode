# TIM 2023
# Advent of Code
# Tag 18: Lavaduct Lagoon
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return list(map(lambda x: x.split(), f.read().splitlines()))


def polygonArea(vertices):
    # A function to apply the Shoelace algorithm
    number_of_vertices = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(0, number_of_vertices - 1):
        sum1 = sum1 + vertices[i][0] * vertices[i + 1][1]
        sum2 = sum2 + vertices[i][1] * vertices[i + 1][0]

    # Add xn.y1
    sum1 = sum1 + vertices[number_of_vertices - 1][0] * vertices[0][1]
    # Add x1.yn
    sum2 = sum2 + vertices[0][0] * vertices[number_of_vertices - 1][1]

    area = abs(sum1 - sum2) / 2
    return area


def convert_hex_to_dec(hex):
    return int(hex, 16)


def solve_part_1(puzzle):
    step_count, vertices = get_vertices(puzzle)
    cubic_meters = polygonArea(vertices) + step_count // 2 + 1
    return cubic_meters


def solve_part_2(puzzle):
    correct_puzzle = list(map(lambda line: (line[-1][-2: -1], convert_hex_to_dec(line[-1][2:-2])), puzzle))
    step_count, vertices = get_vertices(correct_puzzle)
    cubic_meters = polygonArea(vertices) + step_count // 2 + 1
    return cubic_meters


def get_vertices(correct_puzzle):
    vertices = [(0, 0)]
    step_count = 0
    for line in correct_puzzle:
        x, y = vertices[-1]
        step_count += int(line[1])
        if line[0] == "0" or line[0] == "R":
            vertices.append((x + int(line[1]), y))
        elif line[0] == "2" or line[0] == "L":
            vertices.append((x - int(line[1]), y))
        elif line[0] == "3" or line[0] == "U":
            vertices.append((x, y - int(line[1])))
        elif line[0] == "1" or line[0] == "D":
            vertices.append((x, y + int(line[1])))
    return step_count, vertices


if __name__ == "__main__":
    puzzle = read_puzzle("day18.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
