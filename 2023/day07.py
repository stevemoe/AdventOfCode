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
    # print(card_values)
    # print(hand)
    card_counter = Counter(hand[0])
    # print(card_counter)
    values = list(map(lambda x: card_values[x], hand[0]))
    # print("values", card_counter.values())
    # print(list(card_counter.values()).count(2) == 2)
    if 5 in card_counter.values():
        # print("five of a kind")
        return (hand[0], hand[1], 6 ,values)
    elif 4 in card_counter.values():
        # print("four of a kind")
        return (hand[0], hand[1], 5, values)
    elif 3 in card_counter.values() and 2 in card_counter.values():
        # print("full house")
        return (hand[0], hand[1], 4, values)
    elif 3 in card_counter.values():
        # print("three of a kind")
        return (hand[0], hand[1], 3, values)
    elif 2 in card_counter.values() and list(card_counter.values()).count(2) == 2:
        # print("two pairs")
        return (hand[0], hand[1], 2, values)
    elif 2 in card_counter.values():
        # print("pair")
        return (hand[0], hand[1], 1, values)
    else:
        # print("high card")
        return (hand[0], hand[1], 0, values)


def calculate_rank2(hand):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    card_values = dict(zip(reversed(cards), range(13)))
    # print(card_values)
    # print(hand)
    card_counter = Counter(hand[0])
    # print(card_counter)
    values = list(map(lambda x: card_values[x], hand[0]))
    # print("values", card_counter.values())
    # print(list(card_counter.values()).count(2) == 2)
    if 5 in card_counter.values():
        # print("five of a kind")
        return (hand[0], hand[1], 6 ,values)
    elif 4 in card_counter.values():
        # print("four of a kind")
        return (hand[0], hand[1], 5, values)
    elif 3 in card_counter.values() and 2 in card_counter.values():
        # print("full house")
        return (hand[0], hand[1], 4, values)
    elif 3 in card_counter.values():
        # print("three of a kind")
        return (hand[0], hand[1], 3, values)
    elif 2 in card_counter.values() and list(card_counter.values()).count(2) == 2:
        # print("two pairs")
        return (hand[0], hand[1], 2, values)
    elif 2 in card_counter.values():
        # print("pair")
        return (hand[0], hand[1], 1, values)
    else:
        # print("high card")
        return (hand[0], hand[1], 0, values)

def compare(entry):
    return entry[3]



def solve_part_1(puzzle):
    hands = list(map(lambda x: (x.split()[0], int(x.split()[1])), puzzle))
    strength_of_hands = list(map(calculate_rank, hands))
    # print("strength_of_hands", strength_of_hands)
    hands_by_type = list()
    five_of_a_kind = list(filter(lambda x: x[2] == 6, strength_of_hands))
    four_of_a_kind = list(filter(lambda x: x[2] == 5, strength_of_hands))
    full_house = list(filter(lambda x: x[2] == 4, strength_of_hands))
    three_of_a_kind = list(filter(lambda x: x[2] == 3, strength_of_hands))
    two_pairs = list(filter(lambda x: x[2] == 2, strength_of_hands))
    pair = list(filter(lambda x: x[2] == 1, strength_of_hands))
    high_card = list(filter(lambda x: x[2] == 0, strength_of_hands))





    # print(three_of_a_kind)
    five_of_a_kind_sorted = sorted(five_of_a_kind, key=compare, reverse=False)
    four_of_a_kind_sorted = sorted(four_of_a_kind, key=compare, reverse=False)
    full_house_sorted = sorted(full_house, key=compare, reverse=False)
    three_of_a_kind_sorted = sorted(three_of_a_kind, key=compare, reverse=False)
    two_pairs_sorted = sorted(two_pairs, key=compare, reverse=False)
    pair_sorted = sorted(pair, key=compare, reverse=False)
    high_card_sorted = sorted(high_card, key=compare, reverse=False)
    # print(three_of_a_kind_sorted)
    ranked_hands=[]
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
    # ranked_hands = [five_of_a_kind_sorted, four_of_a_kind_sorted, full_house_sorted, three_of_a_kind_sorted, pair_sorted, high_card_sorted]
    # ranked_hands = sorted(ranked_hands, key=lambda x: x[2], reverse=True)
    # print(ranked_hands)

    total_winnings = 0
    for index, hand in enumerate(ranked_hands):
        # print(hand[1] * (index + 1))
        # print(hand[0], hand[1], index + 1)
        total_winnings += hand[1] * (index + 1)
    # for hand in strength_of_hands:
    # print(strength_of_hands)
    rank = 0
    print("total_winnings",total_winnings)
    return total_winnings


def solve_part_2(puzzle):
    hands = list(map(lambda x: (x.split()[0], int(x.split()[1])), puzzle))
    strength_of_hands = list(map(calculate_rank2, hands))
    # print("strength_of_hands", strength_of_hands)
    hands_by_type = list()
    five_of_a_kind = list(filter(lambda x: x[2] == 6, strength_of_hands))
    four_of_a_kind = list(filter(lambda x: x[2] == 5, strength_of_hands))
    full_house = list(filter(lambda x: x[2] == 4, strength_of_hands))
    three_of_a_kind = list(filter(lambda x: x[2] == 3, strength_of_hands))
    two_pairs = list(filter(lambda x: x[2] == 2, strength_of_hands))
    pair = list(filter(lambda x: x[2] == 1, strength_of_hands))
    high_card = list(filter(lambda x: x[2] == 0, strength_of_hands))

    # print(three_of_a_kind)
    five_of_a_kind_sorted = sorted(five_of_a_kind, key=compare, reverse=False)
    four_of_a_kind_sorted = sorted(four_of_a_kind, key=compare, reverse=False)
    full_house_sorted = sorted(full_house, key=compare, reverse=False)
    three_of_a_kind_sorted = sorted(three_of_a_kind, key=compare, reverse=False)
    two_pairs_sorted = sorted(two_pairs, key=compare, reverse=False)
    pair_sorted = sorted(pair, key=compare, reverse=False)
    high_card_sorted = sorted(high_card, key=compare, reverse=False)
    # print(three_of_a_kind_sorted)
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
    # ranked_hands = [five_of_a_kind_sorted, four_of_a_kind_sorted, full_house_sorted, three_of_a_kind_sorted, pair_sorted, high_card_sorted]
    # ranked_hands = sorted(ranked_hands, key=lambda x: x[2], reverse=True)
    # print(ranked_hands)

    total_winnings = 0
    for index, hand in enumerate(ranked_hands):
        # print(hand[1] * (index + 1))
        # print(hand[0], hand[1], index + 1)
        total_winnings += hand[1] * (index + 1)
    # for hand in strength_of_hands:
    # print(strength_of_hands)
    rank = 0
    print("total_winnings", total_winnings)
    return total_winnings


if __name__ == "__main__":
    puzzle = read_puzzle("day07.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

