from enum import Enum
from card import Card


class PokerHandRanking(Enum):
    HIGH_CARD = 10
    ONE_PAIR = 9
    TWO_PAIR = 8
    THREE_OF_A_KIND = 7
    STRAIGHT = 6
    FLUSH = 5
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 3
    STRAIGHT_FLUSH = 2
    ROYAL_FLUSH = 1


def sort_array(cards_array):
    A = cards_array.copy()

    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx].value > A[j].value:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]

    return A


def get_counter(cards_array):
    counter = [0 for i in range(13)]
    for card in cards_array:
        counter[card.value - 1] += 1
    return counter


def check_high_card(cards_array):  # TODO: Check if necessary to consider if cards_array is empty.
    high_card_list = [cards_array[len(cards_array) - 1]]

    return high_card_list


def check_one_pair(cards_array):
    one_pair_list = []

    counter_list = get_counter(cards_array)

    for x, count in enumerate(counter_list):
        if count == 2:
            for card in cards_array:
                if card.value == x + 1:
                    one_pair_list.append(card)

    return one_pair_list
    # one_pair_list = []
    #
    # previous_card = None
    # for card in cards_array:
    #     if previous_card is not None and card.value == previous_card.value:
    #         one_pair_list.append(card)
    #         one_pair_list.append(previous_card)
    #         return one_pair_list
    #     previous_card = card
    #
    # return one_pair_list


def check_two_pair(cards_array):  # TODO Seems to be complicated in comparison to other checks.
    # two_pair_list = []
    #
    #
    # previous_card = None
    # for card in cards_array:
    #     if previous_card is not None and card.value == previous_card.value:
    #         two_pair_list.append(card)
    #         two_pair_list.append(previous_card)
    #     previous_card = card
    #
    # return two_pair_list
    pass


def check_three_of_a_kind(cards_array):
    return False


def check_straight(cards_array):
    return False


def check_flush(cards_array):
    return False


def check_full_house(cards_array):
    return False


def check_four_of_a_kind(cards_array):
    return False


def check_straight_flush(cards_array):
    return False


def check_royal_flush(cards_array):
    return False


def check_poker_hand_ranking(cards):
    sorted_cards = sort_array(cards)

    check_high_card_list = check_high_card(sorted_cards)
    check_one_pair_list = check_one_pair(sorted_cards)

    if check_one_pair_list:
        return PokerHandRanking.ONE_PAIR, check_one_pair_list
    elif check_high_card_list:
        return PokerHandRanking.HIGH_CARD, check_high_card_list
    # if check_one_pair(cards):
    #     return PokerHandRanking.ONE_PAIR
    # elif check_two_pair(cards):
    #     return PokerHandRanking.TWO_PAIR
    # elif check_three_of_a_kind(cards):
    #     return PokerHandRanking.THREE_OF_A_KIND
    # elif check_straight(cards):
    #     return PokerHandRanking.STRAIGHT
    # elif check_flush(cards):
    #     return PokerHandRanking.FLUSH
    # elif check_full_house(cards):
    #     return PokerHandRanking.FULL_HOUSE
    # elif check_four_of_a_kind(cards):
    #     return PokerHandRanking.FOUR_OF_A_KIND
    # elif check_straight_flush(cards):
    #     return PokerHandRanking.STRAIGHT_FLUSH
    # elif check_royal_flush(cards):
    #     return PokerHandRanking.ROYAL_FLUSH
    # else:
    #     return PokerHandRanking.HIGH_CARD
