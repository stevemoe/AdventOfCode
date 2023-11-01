from collections import Counter
import time

def read_input_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def count_multiple_letters_in_ids(ids, number):
    number_of_multiple_letters = list(filter(lambda box_id: count_letters(box_id, number), ids))
    return len(number_of_multiple_letters)


def count_letters(box_id, number):
    if number in Counter(box_id).values():
        return True


def find_correct_box_id(ids):
    correct_box_id = str(next(filter(lambda own_id: find_closest_matching_ids(own_id, ids), ids), None))
    return correct_box_id


def find_closest_matching_ids(own_id, ids):
    for other_id in ids:
        same_letters = [1 if letter == other_id[num] else 0 for num, letter in enumerate(own_id)]
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
letter_index = None
box_ids = read_input_file("input/day_02.txt").splitlines()
print("Puzzle 1: Checksum is", solve_puzzle_1(box_ids))
print("Puzzle 2: Common letters between two correct box IDs:", solve_puzzle_2(box_ids))
end = time.time()
print("Code execution time:", end - start)
