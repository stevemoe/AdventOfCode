# TIM 2023
# Advent of Code
# Tag 10: Pipe Maze
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


list_left = ["L", "-", "F"]
list_right = ["J", "-", "7"]
list_up = ["F", "|", "7"]
list_down = ["J", "|", "L"]
start = "S"
face_up = ["J", "|", "L"]


def get_next_coords(coords, previous_coords, puzzle, coords_start):
    y, x = coords
    if puzzle[y][x] in list_right:
        try:
            if (left := puzzle[y][x - 1]) in list_left and (y, x - 1) != previous_coords:
                if (act := puzzle[y][x]) not in list_left or act == "-":
                    return y, x - 1
        except IndexError:
            pass
    if puzzle[y][x] in list_left:
        try:
            if (right := puzzle[y][x + 1]) in list_right and (y, x + 1) != previous_coords:
                if (act := puzzle[y][x]) not in list_right or act == "-":
                    return y, x + 1
        except IndexError:
            pass
    if puzzle[y][x] in list_up:
        try:
            if (down := puzzle[y + 1][x]) in list_down and (y + 1, x) != previous_coords:
                if (act := puzzle[y][x]) not in list_down or act == "|":
                    return y + 1, x
        except IndexError:
            pass
    if puzzle[y][x] in list_down:
        try:
            if (up := puzzle[y - 1][x]) in list_up and (y - 1, x) != previous_coords:
                if (act := puzzle[y][x]) not in list_up or act == "|":
                    return y - 1, x
        except IndexError:
            pass
    if puzzle[y][x] in list_up:
        try:
            if (down := puzzle[y + 1][x]) in list_down and (y + 1, x) != previous_coords:
                if (act := puzzle[y][x]) not in list_down or act == "|":
                    return y + 1, x
        except IndexError:
            pass
    return coords_start


def solve_part_1(puzzle):
    print(puzzle)
    start_line = 0
    start_index = 0
    for line in puzzle:
        if "S" in line:
            start_line = puzzle.index(line)
            start_index = line.index("S")
            print(f"start_line: {start_line}")
            print(f"start_index: {start_index}")
            break

    coords_start = (start_line, start_index)

    coords_list_right = [coords_start]
    coords_list_left = [coords_start]
    coords_list_up = [coords_start]
    coords_list_down = [coords_start]

    if (right := puzzle[start_line][start_index + 1]) in list_right:
        coords_list_right.append((start_line, start_index + 1))
        while True:
            y, x = coords_list_right[-1]
            next_coords = get_next_coords(coords_list_right[-1], coords_list_right[-2], puzzle, coords_start)
            coords_list_right.append(next_coords)
            if coords_list_right[-1] == coords_start:
                coords_list_right.pop()
                break
    if left := puzzle[start_line][start_index - 1] in list_left:
        coords_list_right.append((start_line, start_index - 1))
        while True:
            y, x = coords_list_left[-1]
            next_coords = get_next_coords(coords_list_left[-1], coords_list_left[-2], puzzle, coords_start)
            coords_list_left.append(next_coords)
            if coords_list_left[-1] == coords_start:
                coords_list_left.pop()
                break
    if up := puzzle[start_line - 1][start_index] in list_up:
        coords_list_up.append((start_line - 1, start_index))
        while True:
            y, x = coords_list_up[-1]
            next_coords = get_next_coords(coords_list_up[-1], coords_list_up[-2], puzzle, coords_start)
            coords_list_up.append(next_coords)
            if coords_list_up[-1] == coords_start:
                coords_list_up.pop()
                break
    if down := puzzle[start_line + 1][start_index] in list_down:
        coords_list_down.append((start_line + 1, start_index))
        while True:
            y, x = coords_list_down[-1]
            next_coords = get_next_coords(coords_list_down[-1], coords_list_down[-2], puzzle, coords_start)
            coords_list_down.append(next_coords)
            if coords_list_down[-1] == coords_start:
                coords_list_down.pop()
                break

    x = [len(coords_list_left), len(coords_list_right), len(coords_list_up), len(coords_list_down)]
    paths = [coords_list_left, coords_list_right, coords_list_up, coords_list_down]
    path = max(paths, key=len)

    puzzle_path = puzzle.copy()
    # print(path)
    for line, index in path:
        puzzle_path[line] = puzzle_path[line][:index] + puzzle_path[line][index:].replace(puzzle_path[line][index], "X",
                                                                                          1)

    ctr_in = 0
    # print("\n".join(puzzle))
    for index, line in enumerate(puzzle_path):
        border_cnt = 0

        for i in range(len(line)):
            # print(f"puzzle[index][i]: {puzzle[index][i]}")
            if line[i] == "X" and border_cnt == 0 and puzzle[index][i] in face_up:
                border_cnt += 1
            elif border_cnt == 1 and line[i] == "X":
                # print(border_cnt)
                border_cnt = 0
            if border_cnt == 1 and line[i] == ".":
                ctr_in += 1
            # print(f"ctr_in: {ctr_in}")

            # print(f"border_cnt: {border_cnt}")
    # print(f"ctr_in: {ctr_in}")
    # print(puzzle_path)
    # print("\n".join(puzzle_path))

    return int(max(x) / 2)


def solve_part_2(puzzle):
    start_line = 0
    start_index = 0
    for line in puzzle:
        if "S" in line:
            start_line = puzzle.index(line)
            start_index = line.index("S")
            print(f"start_line: {start_line}")
            print(f"start_index: {start_index}")
            break

    coords_start = (start_line, start_index)

    coords_list_right = [coords_start]
    coords_list_left = [coords_start]
    coords_list_up = [coords_start]
    coords_list_down = [coords_start]

    if (right := puzzle[start_line][start_index + 1]) in list_right:
        coords_list_right.append((start_line, start_index + 1))
        while True:
            y, x = coords_list_right[-1]
            next_coords = get_next_coords(coords_list_right[-1], coords_list_right[-2], puzzle, coords_start)
            coords_list_right.append(next_coords)
            if coords_list_right[-1] == coords_start:
                coords_list_right.pop()
                break
    if left := puzzle[start_line][start_index - 1] in list_left:
        coords_list_right.append((start_line, start_index - 1))
        while True:
            y, x = coords_list_left[-1]
            next_coords = get_next_coords(coords_list_left[-1], coords_list_left[-2], puzzle, coords_start)
            coords_list_left.append(next_coords)
            if coords_list_left[-1] == coords_start:
                coords_list_left.pop()
                break
    if up := puzzle[start_line - 1][start_index] in list_up:
        coords_list_up.append((start_line - 1, start_index))
        while True:
            y, x = coords_list_up[-1]
            next_coords = get_next_coords(coords_list_up[-1], coords_list_up[-2], puzzle, coords_start)
            coords_list_up.append(next_coords)
            if coords_list_up[-1] == coords_start:
                coords_list_up.pop()
                break
    if down := puzzle[start_line + 1][start_index] in list_down:
        coords_list_down.append((start_line + 1, start_index))
        while True:
            y, x = coords_list_down[-1]
            next_coords = get_next_coords(coords_list_down[-1], coords_list_down[-2], puzzle, coords_start)
            coords_list_down.append(next_coords)
            if coords_list_down[-1] == coords_start:
                coords_list_down.pop()
                break

    x = [len(coords_list_left), len(coords_list_right), len(coords_list_up), len(coords_list_down)]
    paths = [coords_list_left, coords_list_right, coords_list_up, coords_list_down]
    path = max(paths, key=len)

    puzzle_path = puzzle.copy()
    print(path)
    for line, index in path:
        puzzle_path[line] = puzzle_path[line][:index] + puzzle_path[line][index:].replace(puzzle_path[line][index], "X",
                                                                                          1)

    ctr_in = 0
    print("\n".join(puzzle))
    if path[1][0] < path[0][0]:
        print(f"s is facing up")
    else:
        print(f"s is not facing up")
    for index, line in enumerate(puzzle_path):
        border_cnt = 0
        print("next line ...............")
        for i in range(len(line)):
            print(f"border_cnt: {border_cnt}")
            print(f"puzzle[index][i]: {puzzle[index][i]}")
            if line[i] == "X" and puzzle[index][i] in face_up:
                border_cnt += 1
            # elif border_cnt == 1 and line[i] == "X":
            #     print(border_cnt)
            #     border_cnt = 0
            if border_cnt % 2 != 0 and border_cnt != 0 and line[i] == "." :
                print(f"border_cnt: {border_cnt}")
                ctr_in += 1
            print(f"ctr_in: {ctr_in}")

            # print(f"border_cnt: {border_cnt}")
    print(f"ctr_in: {ctr_in}")
    print(puzzle_path)
    print("\n".join(puzzle_path))

    return ctr_in


if __name__ == "__main__":
    puzzle = read_puzzle("day10.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
