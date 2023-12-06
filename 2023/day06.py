# TIM 2023
# Advent of Code
# Tag 6: Wait For It
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine
from math import prod
from time import perf_counter as pfc
from colorama import init, Fore


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def possible_ways_to_win(time, distance):
    print(f"possible_ways_to_win({time}, {distance})")
    button_press_time = []
    for i in range(time + 1):
        # print(f"i = {i}, max_button_press_time = {button_press_time}")
        x = (time - i) * i
        # print(f"x = {x}")
        draw_vertical_line(x, x > distance)
        if x > distance:
            button_press_time.append(i)
    return len(button_press_time)


def possible_ways_to_win2(time, distance):
    print(f"possible_ways_to_win({time}, {distance})")
    button_press_time = []
    longer = False
    while not longer:

        for i in range(time + 1):
            # print(f"i = {i}, max_button_press_time = {button_press_time}")
            x = (time - i) * i
            # print(f"x = {x},{x > distance}, distance = {distance}, i = {i}")
            if distance <= 300:
                draw_vertical_line(x, x > distance)

            if x > distance:
                longer = True
                button_press_time.append((i)*2 )
                break
    longer = False
    # while not longer:
    #
    #     for i in range(time + 1, 0, -1):
    #         # print(f"i = {i}, max_button_press_time = {button_press_time}")
    #         x = (time - i) * i
    #         # print(f"x = {x},{x > distance}, distance = {distance}, i = {i}")
    #         if x > distance:
    #             longer = True
    #             button_press_time.append(time - i)
    #             break
    # # print(button_press_time)
    # print(time - (button_press_time[0] + button_press_time[1]))
    print("button_press_time", button_press_time)
    return time - (button_press_time[0]-1)

    # return len([i for i in range(time + 1) if (time - i) * i > distance])


def draw_vertical_line(length, win=False):
    print(Fore.__dict__["GREEN" if win else "RED"] + '-' * int(length / 1) + Fore.RESET)


def solve_part_1(puzzle):
    # puzzle = ['Time:      7  15   30', 'Distance:  9  40  200']
    times = [int(x) for x in puzzle[0].split()[1:]]
    distances = [int(x) for x in puzzle[1].split()[1:]]

    # number_of_wins_per_race = [possible_ways_to_win(t, d) for t, d in zip(times, distances)]
    number_of_wins_per_race = [possible_ways_to_win2(t, d) for t, d in zip(times, distances)]

    print(number_of_wins_per_race)
    return prod(number_of_wins_per_race)


def solve_part_2(puzzle):
    time, distance = (int(line.split(':')[1:][0].replace(' ', '')) for line in puzzle)
    # print(time) # 71530
    return possible_ways_to_win2(time, distance)


if __name__ == "__main__":
    init(autoreset=True)
    puzzle = read_puzzle("day06.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
