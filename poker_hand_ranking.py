from enum import Enum


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


# 0 = King, 1 = Queen, 2 = Jack,
# 3 = Ten, 4 = Nine, 5 = Eight,
# 6 = Seven, 7 = Six, 8 = Five,
# 9 = Four, 10 = Three, 11 = Two,
# 12 = Ace
def get_counter(cards_array):
    counter = [0 for i in range(13)]
    for card in cards_array:
        counter[card.value - 1] += 1

    counter.reverse()
    return counter


# 0 = Ace, 1 = King, 2 = Queen,
# 3 = Jack, 4 = Ten, 5 = Nine,
# 6 = Eight, 7 = Seven, 8 = Six,
# 9 = Five, 10 = Four, 11 = Three,
# 12 = Two
def get_counter_ace_highest(cards_array):
    A = get_counter(cards_array)

    A.reverse()

    A.append(A[0])
    A.pop(0)

    A.reverse()

    return A


def get_sorted_cards(cards_array):
    A = cards_array.copy()

    for i in range(len(A)):
        min_idx = i

        for j in range(i + 1, len(A)):
            if A[min_idx].value > A[j].value:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

    A.reverse()

    return A


def get_sorted_cards_ace_highest(cards_array):
    A = get_sorted_cards(cards_array)

    A.reverse()

    one_counter = 0

    for card in A:
        if card.value == 1:
            A.append(card)
            one_counter += 1
        else:
            break

    for x in range(one_counter):
        A.pop(0)

    A.reverse()

    return A


def check_high_card(cards_array):
    high_card_list = []

    cards_ace_highest_list = get_sorted_cards_ace_highest(cards_array)
    for card in cards_ace_highest_list:
        if len(high_card_list) == 5:
            break
        high_card_list.append(card)

    return high_card_list


def check_one_pair(cards_array):
    one_pair_list = []

    counter_ace_highest_list = get_counter_ace_highest(cards_array)
    cards_ace_highest_list = get_sorted_cards_ace_highest(cards_array)

    value_of_highest_pair = None
    for x, count in enumerate(counter_ace_highest_list):
        if x == 0:
            value = 1
        else:
            value = 14 - x
        if count == 2:
            value_of_highest_pair = value
            break

    if value_of_highest_pair is not None:
        for card in cards_ace_highest_list:
            if len(one_pair_list) >= 2:
                break
            if card.value == value_of_highest_pair:
                one_pair_list.append(card)

    return one_pair_list


def check_two_pair(cards_array):
    two_pair_list = []

    counter_ace_highest_list = get_counter_ace_highest(cards_array)
    cards_ace_highest_list = get_sorted_cards_ace_highest(cards_array)

    values_of_highest_pair = []
    for x, count in enumerate(counter_ace_highest_list):
        if x == 0:
            value = 1
        else:
            value = 14 - x
        if count == 2:
            values_of_highest_pair.append(value)
            if len(values_of_highest_pair) >= 2:
                break

    if len(values_of_highest_pair) == 2:
        for card in cards_ace_highest_list:
            if len(two_pair_list) >= 4:
                break
            for values in values_of_highest_pair:
                if card.value == values:
                    two_pair_list.append(card)

    return two_pair_list


def check_three_of_a_kind(cards_array):
    pass


def check_straight(cards_array):
    pass


def check_flush(cards_array):
    pass


def check_full_house(cards_array):
    pass


def check_four_of_a_kind(cards_array):
    pass


def check_straight_flush(cards_array):
    pass


def check_royal_flush(cards_array):
    pass


def check_poker_hand_ranking(cards):

    check_two_pair_list = check_two_pair(cards)
    check_one_pair_list = check_one_pair(cards)
    check_high_card_list = check_high_card(cards)

    if check_two_pair_list:
        return PokerHandRanking.TWO_PAIR, check_two_pair_list
    elif check_one_pair_list:
        return PokerHandRanking.ONE_PAIR, check_one_pair_list
    elif check_high_card_list:
        return PokerHandRanking.HIGH_CARD, check_high_card_list
