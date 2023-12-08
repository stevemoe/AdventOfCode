# TIM 2023
# Advent of Code
# Tag 7: Camel Cards
# Autor: Stefan Mohr (stefan.mo)
# Requirements: keine

from time import perf_counter as pfc
from collections import Counter

TYPES_TOTAL = 7


def read_puzzle(filename):
    with open("inputs/" + filename, "r") as f:
        return f.read().splitlines()


def find_hand_type(card_counter):
    if 5 in card_counter:
        return 6
    if 4 in card_counter:
        return 5
    if 3 in card_counter and 2 in card_counter:
        return 4
    if 3 in card_counter:
        return 3
    if list(card_counter).count(2) == 2:
        return 2
    if 2 in card_counter:
        return 1
    return 0


def find_hand_type_with_joker(cards):
    joker_count = cards.count("J")

    if joker_count == 5:
        return 6

    remaining_cards = cards.replace("J", "")
    max_same = max(Counter(remaining_cards).values())
    total_same = joker_count + max_same

    if total_same == 5:
        return 6
    elif total_same == 4:
        return 5
    elif total_same == 3:
        return 4 if len(Counter(remaining_cards).values()) == 2 else 3
    elif total_same == 2:
        return 1
    else:
        return 0


def determine_hand_attributes(hand, deck, joker):
    cards, bid = hand
    card_count = Counter(cards).values()
    card_values = list(map(lambda card: deck[card], cards))
    if joker and "J" in cards:
        hand_type = find_hand_type_with_joker(cards)
        return cards, bid, hand_type, card_values
    else:
        hand_type = find_hand_type(card_count)
        return cards, bid, hand_type, card_values


def compare(hand):
    return hand[3]


def rank_hands(hands, deck, joker):
    return sum(
        map(lambda type_number: sorted(filter(lambda x: (hand_type := x[2]) == type_number,
                                              map(lambda hand: determine_hand_attributes(hand, deck, joker), hands)),
                                       key=compare), range(TYPES_TOTAL)), [])


def calculate_total_winnings(puzzle, deck, joker=False):
    hands = list(map(lambda x: (x.split()[0], int(x.split()[1])), puzzle))
    ranked_hands = rank_hands(hands, deck, joker)
    return sum(map(lambda x: (bid := x[1][1]) * (rank := x[0]), enumerate(ranked_hands, start=1)))


def solve_part_1(puzzle):
    deck = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    return calculate_total_winnings(puzzle, deck)


def solve_part_2(puzzle):
    deck = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}
    joker = True
    return calculate_total_winnings(puzzle, deck, joker)


if __name__ == "__main__":
    puzzle = read_puzzle("day07.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print(f"Teil 1: {result1} ({pfc() - start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
