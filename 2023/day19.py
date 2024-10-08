# TIM 2023
# Advent of Code
# Tag 19: Aplenty
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine
import re
from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().split("\n\n")


def reformat_parts(parts):
    parts_new = []
    for line in parts:
        line = re.findall(r"\w=\d+", line)
        parts_dict = {}
        for part in line:
            part = part.split("=")
            parts_dict[part[0]] = int(part[1])
        parts_new.append(parts_dict)
    return parts_new


def reformat_workflows(workflows):
    workflows_dict = {}
    for line in workflows:
        line_new = line.replace("}", "").split("{")
        workflows_dict[line_new[0]] = line_new[1].split(",")
    return workflows_dict


def solve_part_1(puzzle):
    workflows = reformat_workflows(puzzle[0].splitlines())
    parts = reformat_parts(puzzle[1].splitlines())
    ratings = []
    for line in parts:
        finished = False
        workflow = "in"
        print(f"rating: {ratings}")
        while not finished:
            if workflow != "A" and workflow != "R":
                for ws in workflows[workflow]:

                    print(f" Workflow: {workflow}, WS: {ws}")
                    if len(ws) <= 3:
                        if ws == "A":
                            finished = True
                            ratings.append(sum(line.values()))
                        elif ws == "R":
                            finished = True
                        else:
                            workflow = ws
                    elif ws[1] == "<":
                        part = ws[0]
                        if line[part] < int(re.findall(r"\d+", ws)[0]):
                            workflow = ws.split(":")[1]
                            if workflow == "A":
                                finished = True
                                ratings.append(sum(line.values()))
                            elif workflow == "R":
                                finished = True
                            break
                    elif ws[1] == ">":
                        part = ws[0]
                        if line[part] > int(re.findall(r"\d+", ws)[0]):
                            workflow = ws.split(":")[1]
                            if workflow == "A":
                                finished = True
                                ratings.append(sum(line.values()))
                            elif workflow == "R":
                                finished = True
                            break
    print(f"rating: {ratings}")
    return sum(ratings)


def solve_part_2(puzzle):
    return puzzle


if __name__ == "__main__":
    puzzle = read_puzzle("day19.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
