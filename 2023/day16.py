# TIM 2023
# Advent of Code
# Tag 16: The Floor Will Be Lava
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc
import queue as q

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)


def bfs(graph, start, suche):
    visited = {start}
    queue = [start]
    path = []
    while queue:
        node = queue.pop(0)
        x, y, direction = node
        print(x, y, direction)
        if not (x < 0 or y < 0 or x >= len(graph) or y >= len(graph)):
            suche[x][y] = suche[x][y] + 1
        # abbruchbedingung node größer als graph

        # for n in neighbours:
        #     visited[n] = node
        #     queue.append(n)


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def solve_part_1(puzzle):
    energized_tiles = []
    graph = {}
    for i, line in enumerate(puzzle):
        for j, char in enumerate(line):
            graph[i, j] = char
    start = (0, 0, RIGHT)
    # graph[start] = ">"
    # for i, line in enumerate(puzzle):
    #     for j, char in enumerate(line):
    #         if char == ">" or char == "-":
    #             graph[i, j + 1] = ">"
    #         if char == "/":
    #             graph[i - 1, j] = "^"
    #         if char == "\\":
    #             graph[i + 1, j] = "v"
    #         if char == "|":
    #             graph[i - 1, j] = "^"
    #             graph[i + 1, j] = "v"

    print_beam(graph)
    bfs(graph, start, "v")
    return sum(energized_tiles)


def print_beam(beam):
    # Finde die maximalen Indizes für die Schleifen
    max_i = max(key[0] for key in beam.keys()) + 1
    max_j = max(key[1] for key in beam.keys()) + 1
    # Erstelle eine leere 2D-Liste mit den entsprechenden Dimensionen
    beam_2d = [['' for _ in range(max_j)] for _ in range(max_i)]
    # Fülle die 2D-Liste mit den Werten aus dem beam-Dictionary
    for (i, j), value in beam.items():
        beam_2d[i][j] = value
    # Gib die 2D-Liste in der Konsole aus
    print("Beam:")
    for row in beam_2d:
        print(''.join(row))


def solve_part_2(puzzle):
    return puzzle


if __name__ == "__main__":
    puzzle = read_puzzle("day16.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
