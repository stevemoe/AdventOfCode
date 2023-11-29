# TIM 2023
# Advent of Code
# Tag 5: Supply Stacks
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def create_dictionary(rearangement_procedure):
    return {"move": [int(s) for s in rearangement_procedure.split() if s.isdigit()][0], "from": [int(s) for s in rearangement_procedure.split() if s.isdigit()][1],
            "to": [int(s) for s in rearangement_procedure.split() if s.isdigit()][2]}


def get_rearangement_procedures(puzzle):
    rearangement_procedures = []
    for line in puzzle:
        if line != "" and line[0] == "m":
            rearangement_procedures.append(line)
    rearangement_procedures = list(map(create_dictionary, rearangement_procedures))
    return rearangement_procedures


def get_stack_section(puzzle):
    stack_section = []
    for line in puzzle:
        if line == "":
            return stack_section
        else:
            stack_section.append(line)


def get_stack_indexes(indexes_line):
    return list(map(lambda x: int(x), filter(lambda x: x.strip(), indexes_line)))


def get_initial_stacks(puzzle):
    for line in puzzle:
        if line[0] != "[" and line[1] == "1":
            stacks = list(filter(lambda x: x.strip(), line))
            return stacks


def get_stacks(stack_section):
    stacks = {}
    for stack in get_stack_indexes(stack_section[-1]):
        stacks.update({stack: []})
        for x in range(len(stack_section) - 1):
            if stack_section[x][(stack - 1) * 4 + 1] != " ":
                stacks[stack].append(stack_section[x][(stack - 1) * 4 + 1])
    return stacks


def rearrange_stacks(rearrangement_procedures, stacks):
    rearranged_stacks = stacks
    for procedure in rearrangement_procedures:
        for i in range(procedure["move"]):
            if len(rearranged_stacks[procedure["from"]]) > 0:
                crate = rearranged_stacks[procedure["from"]].pop(0)
                rearranged_stacks[procedure["to"]].insert(0, crate)
    return rearranged_stacks



def rearrange_stacks_extended(rearrangement_procedures, stacks):
    rearranged_stacks = stacks
    for procedure in rearrangement_procedures:
        crates = ""
        for i in range(procedure["move"]):
            if len(rearranged_stacks[procedure["from"]]) > 0:
                crates += rearranged_stacks[procedure["from"]].pop(0)

        for crate in crates[::-1]:
            rearranged_stacks[procedure["to"]].insert(0, crate)
        print(crates)
    print(rearranged_stacks)
    return rearranged_stacks


def solve_part_1(puzzle):
    top_crates = ""
    stack_section = get_stack_section(puzzle)
    print(stack_section)
    stacks = get_stacks(stack_section)
    print(stacks)
    rearrangement_procedures = get_rearangement_procedures(puzzle)
    rearranged_stacks = rearrange_stacks(rearrangement_procedures, stacks)
    for stack in rearranged_stacks:
        top_crates += rearranged_stacks[stack][0]
    return top_crates


def solve_part_2(puzzle):
    top_crates = ""
    stack_section = get_stack_section(puzzle)
    print(stack_section)
    stacks = get_stacks(stack_section)
    print(stacks)
    rearrangement_procedures = get_rearangement_procedures(puzzle)
    rearranged_stacks = rearrange_stacks_extended(rearrangement_procedures, stacks)
    for stack in rearranged_stacks:
        top_crates += rearranged_stacks[stack][0]
    return top_crates


if __name__ == "__main__":
    puzzle = read_puzzle("day05.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
