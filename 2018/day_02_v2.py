from collections import Counter
import time
import itertools


def read_input_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def count_multiple_letters_in_ids(ids, number_of_letters):
    return len(list(filter(lambda box_id: count_letters(box_id, number_of_letters), ids)))


def count_letters(box_id, number_of_letters):
    if number_of_letters in Counter(box_id).values():
        return True


def find_correct_box_id(ids):
    correct_box_ids = list(next(filter(lambda box_id: find_closest_matching_ids(box_id[0], box_id[1]), itertools.product(ids, ids))))
    return correct_box_ids[0]


def find_closest_matching_ids(id_1, id_2):
    same_letters = [1 if letter == id_2[num] else 0 for num, letter in enumerate(id_1)]
    if same_letters.count(0) == 1:
        global letter_index
        letter_index = same_letters.index(0)
        return True


def remove_letter_by_index(string, index):
    return string[:index] + string[index + 1:]


def solve_puzzle_1(ids):
    return count_multiple_letters_in_ids(ids, 2) * count_multiple_letters_in_ids(ids, 3)


def solve_puzzle_2(ids):
    return remove_letter_by_index(find_correct_box_id(ids), letter_index)


start = time.time()
start = pfc()
letter_index = 0
box_ids = read_input_file("input/day_02.txt").splitlines()
print("Puzzle 1: Checksum is", solve_puzzle_1(box_ids), pfc()-start)
print("Puzzle 2: Common letters between two correct box IDs:", solve_puzzle_2(box_ids))
end = time.time()
print("Code execution time in s:", end - start)
