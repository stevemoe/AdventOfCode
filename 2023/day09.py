
from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        input = f.read().splitlines()
        return list(map(lambda x: list(map(int, x)), map(lambda x: x.split(), input)))


def get_actual_line(line, nex_line, ctr):
    return line if ctr == 1 else nex_line

def find_sequence(line):
    next_value = 0
    ctr = 0
    next_line = line
    while not len(list(filter(lambda x: x == 0, next_line))) == len(next_line):
        ctr += 1
        actual_line = get_actual_line(line, next_line, ctr)

        next_line = []
        for i in range(0, len(actual_line)):

            if i < len(actual_line) - 1:
                next_line.append(actual_line[i + 1] - actual_line[i])
        next_value += next_line[-1]
    return next_value + line[-1]




def find_sequence2(line):
    ctr = 0
    next_line = line
    first_values =[]
    first_values_list =[0]
    lines = []
    while not len(list(filter(lambda x: x == 0, next_line))) == len(next_line):
        ctr += 1
        if ctr == 1:
            actual_line = line
        else:
            actual_line = next_line

        next_line = []
        for i in range(0, len(actual_line)):

            if i < len(actual_line) - 1:
                next_line.append(actual_line[i + 1] - actual_line[i])
        first_values.append(next_line[0])
        lines.append(next_line)
    first_values = list(reversed(first_values))
    first_values.append(line[0])
    for i in range(0, len(first_values)):
        if i < len(first_values) - 1:
            if i < len(first_values) - 1:
                first_values_list.append(first_values[i+1] - first_values_list[i])

    return first_values_list[-1]


def solve_part_1(puzzle):
    return sum(map(lambda x: find_sequence(x), puzzle))


def solve_part_2(puzzle):
    return sum(map(lambda x: find_sequence2(x), puzzle))


if __name__ == "__main__":
    puzzle = read_puzzle("day09.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
