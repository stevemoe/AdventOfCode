# TIM 2023
# Advent of Code
# Tag 7: Camel Cards
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc
from collections import Counter


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def calculate_rank(hand):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    card_values = dict(zip(reversed(cards), range(13)))
    card_counter = Counter(hand[0])
    values = list(map(lambda x: card_values[x], hand[0]))
    if 5 in card_counter.values():
        value = 6
    elif 4 in card_counter.values():
        value = 5
    elif 3 in card_counter.values() and 2 in card_counter.values():
        value = 4
    elif 3 in card_counter.values():
        value = 3
    elif 2 in card_counter.values() and list(card_counter.values()).count(2) == 2:
        value = 2
    elif 2 in card_counter.values():
        value = 1
    else:
        value = 0
    return (hand[0], hand[1], value, values)



def joker_val(hand):
    cards, bid, value, values, value_counter = hand
    joker_count = cards.count("J")
    if joker_count == 5:
        value = 6
        return (cards, bid, value, values, value_counter)
    else:
        remaining_cards = cards.replace("J", "")
        max_same = max(Counter(remaining_cards).values())
        if joker_count + max_same == 5:
            value = 6
        elif joker_count + max_same == 4:
            value = 5
        elif joker_count + max_same == 3:
            if len(Counter(remaining_cards).values()) == 2:
                value = 4
            else:
                value = 3
        elif joker_count + max_same == 2:
            value = 1

        return (cards, bid, value, values, value_counter)


def calculate_rank2(hand):
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    card_values = dict(zip(reversed(cards), range(13)))
    card_counter = Counter(hand[0])
    values = list(map(lambda x: card_values[x], hand[0]))
    value_counter = Counter(values)
    if 5 in card_counter.values():
        value = 6
    elif 4 in card_counter.values():
        value = 5
    elif 3 in card_counter.values() and 2 in card_counter.values():
        value = 4
    elif 3 in card_counter.values():
        value = 3
    elif 2 in card_counter.values() and list(card_counter.values()).count(2) == 2:
        value = 2
    elif 2 in card_counter.values():
        value = 1
    else:
        value = 0

    if "J" in hand[0]:
        hand = (hand[0], hand[1], value, values, value_counter)
        hand_modified = joker_val(hand)
        return (hand_modified[0], hand_modified[1], hand_modified[2], hand_modified[3])
    return (hand[0], hand[1], value, values)


def compare(entry):
    return entry[3]


def solve_part_1(puzzle):
    hands = list(map(lambda x: (x.split()[0], int(x.split()[1])), puzzle))
    strength_of_hands = list(map(calculate_rank, hands))
    hands_by_type = list()
    five_of_a_kind = list(filter(lambda x: x[2] == 6, strength_of_hands))
    four_of_a_kind = list(filter(lambda x: x[2] == 5, strength_of_hands))
    full_house = list(filter(lambda x: x[2] == 4, strength_of_hands))
    three_of_a_kind = list(filter(lambda x: x[2] == 3, strength_of_hands))
    two_pairs = list(filter(lambda x: x[2] == 2, strength_of_hands))
    pair = list(filter(lambda x: x[2] == 1, strength_of_hands))
    high_card = list(filter(lambda x: x[2] == 0, strength_of_hands))

    five_of_a_kind_sorted = sorted(five_of_a_kind, key=compare, reverse=False)
    four_of_a_kind_sorted = sorted(four_of_a_kind, key=compare, reverse=False)
    full_house_sorted = sorted(full_house, key=compare, reverse=False)
    three_of_a_kind_sorted = sorted(three_of_a_kind, key=compare, reverse=False)
    two_pairs_sorted = sorted(two_pairs, key=compare, reverse=False)
    pair_sorted = sorted(pair, key=compare, reverse=False)
    high_card_sorted = sorted(high_card, key=compare, reverse=False)
    ranked_hands = []
    for hand in high_card_sorted:
        ranked_hands.append(hand)
    for hand in pair_sorted:
        ranked_hands.append(hand)
    for hand in two_pairs_sorted:
        ranked_hands.append(hand)
    for hand in three_of_a_kind_sorted:
        ranked_hands.append(hand)
    for hand in full_house_sorted:
        ranked_hands.append(hand)
    for hand in four_of_a_kind_sorted:
        ranked_hands.append(hand)
    for hand in five_of_a_kind_sorted:
        ranked_hands.append(hand)

    total_winnings = 0
    for index, hand in enumerate(ranked_hands):
        total_winnings += hand[1] * (index + 1)
    return total_winnings


def solve_part_2(puzzle):
    hands = list(map(lambda x: (x.split()[0], int(x.split()[1])), puzzle))
    strength_of_hands = list(map(calculate_rank2, hands))
    five_of_a_kind = list(filter(lambda x: x[2] == 6, strength_of_hands))
    four_of_a_kind = list(filter(lambda x: x[2] == 5, strength_of_hands))
    full_house = list(filter(lambda x: x[2] == 4, strength_of_hands))
    three_of_a_kind = list(filter(lambda x: x[2] == 3, strength_of_hands))
    two_pairs = list(filter(lambda x: x[2] == 2, strength_of_hands))
    pair = list(filter(lambda x: x[2] == 1, strength_of_hands))
    high_card = list(filter(lambda x: x[2] == 0, strength_of_hands))

    five_of_a_kind_sorted = sorted(five_of_a_kind, key=compare, reverse=False)
    four_of_a_kind_sorted = sorted(four_of_a_kind, key=compare, reverse=False)
    full_house_sorted = sorted(full_house, key=compare, reverse=False)
    three_of_a_kind_sorted = sorted(three_of_a_kind, key=compare, reverse=False)
    two_pairs_sorted = sorted(two_pairs, key=compare, reverse=False)
    pair_sorted = sorted(pair, key=compare, reverse=False)
    high_card_sorted = sorted(high_card, key=compare, reverse=False)
    ranked_hands = []
    for hand in high_card_sorted:
        ranked_hands.append(hand)
    for hand in pair_sorted:
        ranked_hands.append(hand)
    for hand in two_pairs_sorted:
        ranked_hands.append(hand)
    for hand in three_of_a_kind_sorted:
        ranked_hands.append(hand)
    for hand in full_house_sorted:
        ranked_hands.append(hand)
    for hand in four_of_a_kind_sorted:
        ranked_hands.append(hand)
    for hand in five_of_a_kind_sorted:
        ranked_hands.append(hand)
    total_winnings = 0
    for index, hand in enumerate(ranked_hands):
        total_winnings += hand[1] * (index + 1)
    return total_winnings


if __name__ == "__main__":
    puzzle = read_puzzle("day07.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")