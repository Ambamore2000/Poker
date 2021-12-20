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


# 0 = 'C', 1 = 'S'
# 2 = 'H', 3 = 'D'
def get_suit_counter(cards_array):
    counter = [0 for i in range(4)]
    for card in cards_array:
        counter_index = None
        if card.suit == 'C':
            counter_index = 0
        elif card.suit == 'S':
            counter_index = 1
        elif card.suit == 'H':
            counter_index = 2
        elif card.suit == 'D':
            counter_index = 3
        counter[counter_index] += 1

    return counter


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
            if card.value == value_of_highest_pair:
                one_pair_list.append(card)
                if len(one_pair_list) >= 2:
                    break

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
            for values in values_of_highest_pair:
                if card.value == values:
                    two_pair_list.append(card)
                    if len(two_pair_list) >= 4:
                        break

    return two_pair_list


def check_three_of_a_kind(cards_array):
    three_of_a_kind_list = []

    counter_ace_highest_list = get_counter_ace_highest(cards_array)
    cards_ace_highest_list = get_sorted_cards_ace_highest(cards_array)

    value_of_three_of_a_kind = None
    for x, count in enumerate(counter_ace_highest_list):
        if x == 0:
            value = 1
        else:
            value = 14 - x
        if count == 3:
            value_of_three_of_a_kind = value
            break

    if value_of_three_of_a_kind is not None:
        for card in cards_ace_highest_list:
            if card.value == value_of_three_of_a_kind:
                three_of_a_kind_list.append(card)
                if len(three_of_a_kind_list) >= 3:
                    break

    return three_of_a_kind_list


def check_straight_ace_highest(cards_array):
    counter_ace_highest_list = get_counter_ace_highest(cards_array)
    cards_ace_highest_list = get_sorted_cards_ace_highest(cards_array)

    straight_list = []

    values_of_straight = []
    previous_value = None
    for x, count in enumerate(counter_ace_highest_list):
        if x == 0:
            value = 1
        else:
            value = 14 - x
        if count >= 1:
            values_of_straight.append(value)
        else:
            if len(values_of_straight) >= 5:
                break
            values_of_straight = []

    if len(values_of_straight) >= 5:
        for card in cards_ace_highest_list:
            for value in values_of_straight:
                if card.value == value:
                    straight_list.append(card)

    return straight_list


def check_straight_not_ace_highest(cards_array):
    counter_list = get_counter(cards_array)
    cards_list = get_sorted_cards(cards_array)

    straight_list = []

    values_of_straight = []
    for x, count in enumerate(counter_list):
        value = 13 - x
        if count >= 1:
            values_of_straight.append(value)
        else:
            if len(values_of_straight) >= 5:
                break
            values_of_straight = []

    if len(values_of_straight) >= 5:
        for card in cards_list:
            for value in values_of_straight:
                if card.value == value:
                    straight_list.append(card)

    return straight_list


def check_straight(cards_array):
    straight_list = check_straight_ace_highest(cards_array)

    if not straight_list:
        straight_list = check_straight_not_ace_highest(cards_array)

    return straight_list


def check_flush(cards_array):
    flush_list = []

    suit_counter_list = get_suit_counter(cards_array)
    sorted_cards_list = get_sorted_cards(cards_array)

    value_of_flush = None
    for x, count in enumerate(suit_counter_list):
        if count >= 5:
            if x == 0:
                value_of_flush = 'C'
            elif x == 1:
                value_of_flush = 'S'
            elif x == 2:
                value_of_flush = 'H'
            elif x == 3:
                value_of_flush = 'D'

    if value_of_flush is not None:
        for card in sorted_cards_list:
            if card.suit == value_of_flush:
                flush_list.append(card)

    return flush_list


def check_full_house(cards_array):
    full_house_list = []

    three_of_a_kind_list = check_three_of_a_kind(cards_array)
    one_pair_list = check_one_pair(cards_array)

    if three_of_a_kind_list and one_pair_list:
        full_house_list.extend(three_of_a_kind_list)
        full_house_list.extend(one_pair_list)

    return full_house_list


def check_four_of_a_kind(cards_array):
    four_of_a_kind_list = []

    counter_ace_highest_list = get_counter_ace_highest(cards_array)
    cards_ace_highest_list = get_sorted_cards_ace_highest(cards_array)

    value_of_four_of_a_kind = None
    for x, count in enumerate(counter_ace_highest_list):
        if x == 0:
            value = 1
        else:
            value = 14 - x
        if count == 4:
            value_of_four_of_a_kind = value
            break

    if value_of_four_of_a_kind is not None:
        for card in cards_ace_highest_list:
            if card.value == value_of_four_of_a_kind:
                four_of_a_kind_list.append(card)
                if len(four_of_a_kind_list) >= 4:
                    break

    return four_of_a_kind_list


def check_straight_flush(cards_array):
    straight_list = check_straight(cards_array)
    flush_list = check_flush(cards_array)

    print("STRAIGHT:")
    for card in straight_list:
        print(card.value, card.suit)
    print("FLUSH:")
    for card in flush_list:
        print(card.value, card.suit)

    return []


def check_royal_flush(cards_array):
    pass


def check_poker_hand_ranking(cards):
    check_royal_flush_list = check_royal_flush(cards)
    check_straight_flush_list = check_straight_flush(cards)
    check_four_of_a_kind_list = check_four_of_a_kind(cards)
    check_full_house_list = check_full_house(cards)
    check_flush_list = check_flush(cards)
    check_straight_list = check_straight(cards)
    check_three_of_a_kind_list = check_three_of_a_kind(cards)
    check_two_pair_list = check_two_pair(cards)
    check_one_pair_list = check_one_pair(cards)
    check_high_card_list = check_high_card(cards)

    if check_royal_flush_list:
        return PokerHandRanking.ROYAL_FLUSH, check_royal_flush_list
    elif check_straight_flush_list:
        return PokerHandRanking.STRAIGHT_FLUSH, check_straight_flush_list
    elif check_four_of_a_kind_list:
        return PokerHandRanking.FOUR_OF_A_KIND, check_four_of_a_kind_list
    elif check_full_house_list:
        return PokerHandRanking.FULL_HOUSE, check_full_house_list
    elif check_flush_list:
        return PokerHandRanking.FLUSH, check_flush_list
    elif check_straight_list:
        return PokerHandRanking.STRAIGHT, check_straight_list
    elif check_three_of_a_kind_list:
        return PokerHandRanking.THREE_OF_A_KIND, check_three_of_a_kind_list
    elif check_two_pair_list:
        return PokerHandRanking.TWO_PAIR, check_two_pair_list
    elif check_one_pair_list:
        return PokerHandRanking.ONE_PAIR, check_one_pair_list
    elif check_high_card_list:
        return PokerHandRanking.HIGH_CARD, check_high_card_list
