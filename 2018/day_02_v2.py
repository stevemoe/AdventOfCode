from collections import Counter

def read_input_file(dir):
    with open(dir, "r") as f:
        return f.read()


def count_multiple_letters(number):
    number_of_multiple_letters = list(filter(lambda box_id: count_letters(box_id, number), box_ids))
    return len(number_of_multiple_letters)


def count_letters(id, number):
    id_counter = Counter(id)
    if number in id_counter.values():
        return True


def solve_puzzle_1(two_letters, three_letters):
    return two_letters * three_letters


box_ids = read_input_file("input/day_02.txt").splitlines()


print("Checksum for first puzzle is:", solve_puzzle_1(count_multiple_letters(2), count_multiple_letters(3)))
