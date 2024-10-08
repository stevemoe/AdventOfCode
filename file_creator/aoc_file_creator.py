from aocd.models import Puzzle
from pathlib import Path
from datetime import datetime


def format_day(day):
    if day < 10:
        return "0" + str(day)
    else:
        return str(day)


def create_input_file(puzzle):
    try:
        with open(input_folder / ("day" + format_day(puzzle.day) + ".txt"), "x") as f:
            return f.write(puzzle.input_data)
    except FileExistsError:
        print("Input file already exists")


def create_example_input_file(puzzle):
    try:
        with open(input_folder / ("day" + format_day(puzzle.day) + "_example.txt"), "x") as f:
            return f.write(puzzle.examples[0].input_data)
    except FileExistsError:
        print("Example input file already exists")

def create_python_file(puzzle):
    try:
        with open(data_folder / ("day" + format_day(puzzle.day) + ".py"), "x") as f:
            return f.write(build_header(puzzle) + build_input() + build_code(puzzle))
    except FileExistsError:
        print("Python file already exists")


def build_header(puzzle, requirements="keine"):
    lines = []
    lines.append("# TIM 2023")
    lines.append("# Advent of Code")
    lines.append("# Tag " + str(puzzle.day) + ": " + puzzle.title)
    lines.append("# Autor: Stefan Mohr (stefan.mo)")
    lines.append("# Requirements: " + requirements)
    return "\n".join(lines) + "\n\n"


def build_input():
    lines = []
    lines.append("from time import perf_counter as pfc")
    return "\n".join(lines) + "\n\n"


def build_code(puzzle):
    lines = []
    lines.append("def read_puzzle(filename):")
    lines.append("    with open(\"inputs/\" + filename, \"r\") as f:")
    lines.append("        return f.read().splitlines()")
    lines.append("\n")
    lines.append("def solve_part_1(puzzle):")
    lines.append("    return puzzle")
    lines.append("\n")
    lines.append("def solve_part_2(puzzle):")
    lines.append("    return puzzle")
    lines.append("\n")
    lines.append("if __name__ == \"__main__\":")
    lines.append("    puzzle = read_puzzle(\"day" + format_day(puzzle.day) + ".txt\")")
    lines.append("    start = pfc()")
    lines.append("    result1 = solve_part_1(puzzle)")
    lines.append("    print(f\"Teil 1: {result1} ({pfc()-start:.4f}s)\")")
    lines.append("    start = pfc()")
    lines.append("    result2 = solve_part_2(puzzle)")
    lines.append("    print(f\"Teil 2: {result2} ({pfc() - start:.4f}s)\")")
    return "\n".join(lines) + "\n\n"


# def build_test_code(puzzle):
#     lines = []
#     lines.append("from day" + format_day(puzzle.day) + " import solve_part_1, solve_part_2, read_puzzle")
#     lines.append("\n")
#     lines.append("def dummy_puzzle(filename):")
#     lines.append("    return read_puzzle(filename)")
#     lines.append("\n")
#     lines.append("def test_part_1():")
#     for example in puzzle.examples:
#         lines.append("    assert solve_part_1(\"\"\"" + str(example.input_data) + "\"\"\") == \"" + str(example.answer_a + "\"" ))
#     lines.append("\n")
#     lines.append("def test_part_2():")
#     for example in puzzle.examples:
#         lines.append("    assert solve_part_2(\"\"\"" + example.input_data + "\"\"\") == \"" + str(example.answer_b + "\""))
#     return "\n".join(lines) + "\n\n"


def build_test_code(puzzle):
    lines = []
    lines.append("from day" + format_day(puzzle.day) + " import solve_part_1, solve_part_2, read_puzzle")
    lines.append("\n")
    lines.append("def dummy_puzzle(filename):")
    lines.append("    return read_puzzle(filename)")
    lines.append("\n")
    lines.append("def test_part_1():")
    lines.append("    puzzle = dummy_puzzle(\"day" + format_day(puzzle.day) + "_example.txt\")")
    for example in puzzle.examples:
        if example.answer_a is None or int(example.answer_a):
            lines.append("    assert solve_part_1(puzzle) == " + str(example.answer_a))
        else:
            lines.append("    assert solve_part_1(puzzle) == \"" + str(example.answer_a) + "\"" )
    lines.append("\n")
    lines.append("def test_part_2():")
    lines.append("    puzzle = dummy_puzzle(\"day" + format_day(puzzle.day) + "_example.txt\")")
    for example in puzzle.examples:
        print(example)
        if example.answer_b is None or int(example.answer_b):
            lines.append("    assert solve_part_2(puzzle) == " + str(example.answer_b))
        else:
            lines.append("    assert solve_part_2(puzzle) == \"" + str(example.answer_b) + "\"")
    return "\n".join(lines) + "\n\n"


def create_test_file(puzzle):
    try:
        with open(data_folder / ("day" + format_day(puzzle.day) + "_test.py"), "x") as f:
            return f.write(build_header(puzzle, "pytest") + build_test_code(puzzle))
    except FileExistsError:
        print("Test file already exists")

year = 2023
day = 20

if datetime.now().month == 12:
    year = datetime.now().year
    day = datetime.now().day

puzzle = Puzzle(year=year, day=day)
data_folder = Path("../" + str(puzzle.year))
input_folder = Path(data_folder / "inputs/")

create_input_file(puzzle)
create_example_input_file(puzzle)
create_python_file(puzzle)
create_test_file(puzzle)
