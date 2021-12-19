from card import Card
from deck import Deck
from player import Player
from poker_hand_ranking import check_poker_hand_ranking


def print_board_cards(board):
    print("---BOARD---")
    for card in board:
        print(card.value, card.suit)


def print_cards(cards):
    for card in cards:
        print(card.value, card.suit)


def print_player_cards(players):
    for y, p in enumerate(players):
        print("Player {}".format(y))
        print(p.first_card.value, p.first_card.suit)
        print(p.second_card.value, p.second_card.suit)


if __name__ == '__main__':
    print("Welcome to Poker!")
    player_count = int(input("How many players will be playing?"))

    deck = Deck()

    players_array = []

    for x in range(player_count):
        new_player = Player(deck)
        players_array.append(new_player)

    print_player_cards(players_array)

    #board_array = [Card(13, 'S'), Card(10, 'S'), Card(11, 'S'), Card(1, 'S'), Card(12, 'S')]
    board_array = [deck.draw_card(), deck.draw_card(), deck.draw_card(), deck.draw_card(), deck.draw_card()]

    print_board_cards(board_array)

    for x, player in enumerate(players_array):
        print("-- Player {} --".format(x))

        board_and_player_cards = []
        for card in board_array:
            board_and_player_cards.append(card)
        board_and_player_cards.append(player.first_card)
        board_and_player_cards.append(player.second_card)

        to_highlight = check_poker_hand_ranking(board_and_player_cards)

        print(to_highlight[0])
        print_cards(to_highlight[1])
