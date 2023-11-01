from collections import Counter
import time

start = time.time()

with open("input/day_02.txt", "r") as f:
    box_ids = f.read().splitlines()

print()
two_letter_count = 0
three_letter_count = 0
common_letters = None


def calculate_letter_counts():
    letter_counter = Counter(box_id)
    if 2 in letter_counter.values(): #evtl filter verwenden
        global two_letter_count
        two_letter_count += 1
    if 3 in letter_counter.values():
        global three_letter_count
        three_letter_count += 1


def find_smallest_difference():
    for other_box_id in box_ids:
        index = find_index_of_different_letter(box_id, other_box_id)
        if index is not None:
            return remove_letter_by_index(box_id, index)


def find_index_of_different_letter(own_box_id, other_box_id):
    same_letters = [1 if letter == other_box_id[num] else 0 for num, letter in enumerate(own_box_id)]
    if same_letters.count(0) == 1:
        return same_letters.index(0)


def remove_letter_by_index(string, index):
    return string[:index] + string[index + 1:]


for box_id in box_ids:
    calculate_letter_counts()
    if common_letters is None:
        common_letters = find_smallest_difference()

checksum = two_letter_count * three_letter_count

print("Checksum:", checksum)

print("Common letters between two correct box IDs:", common_letters)


end = time.time()
print("Code execution in ms:", end - start)