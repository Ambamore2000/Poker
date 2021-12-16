import random

from card import Card


class Deck:
    def __init__(self):
        ace_of_clubs = Card(1, 'C')
        two_of_clubs = Card(2, 'C')
        three_of_clubs = Card(3, 'C')
        four_of_clubs = Card(4, 'C')
        five_of_clubs = Card(5, 'C')
        six_of_clubs = Card(6, 'C')
        seven_of_clubs = Card(7, 'C')
        eight_of_clubs = Card(8, 'C')
        nine_of_clubs = Card(9, 'C')
        ten_of_clubs = Card(10, 'C')
        jack_of_clubs = Card(11, 'C')
        queen_of_clubs = Card(12, 'C')
        king_of_clubs = Card(13, 'C')
        ace_of_spades = Card(1, 'S')
        two_of_spades = Card(2, 'S')
        three_of_spades = Card(3, 'S')
        four_of_spades = Card(4, 'S')
        five_of_spades = Card(5, 'S')
        six_of_spades = Card(6, 'S')
        seven_of_spades = Card(7, 'S')
        eight_of_spades = Card(8, 'S')
        nine_of_spades = Card(9, 'S')
        ten_of_spades = Card(10, 'S')
        jack_of_spades = Card(11, 'S')
        queen_of_spades = Card(12, 'S')
        king_of_spades = Card(13, 'S')
        ace_of_hearts = Card(1, 'H')
        two_of_hearts = Card(2, 'H')
        three_of_hearts = Card(3, 'H')
        four_of_hearts = Card(4, 'H')
        five_of_hearts = Card(5, 'H')
        six_of_hearts = Card(6, 'H')
        seven_of_hearts = Card(7, 'H')
        eight_of_hearts = Card(8, 'H')
        nine_of_hearts = Card(9, 'H')
        ten_of_hearts = Card(10, 'H')
        jack_of_hearts = Card(11, 'H')
        queen_of_hearts = Card(12, 'H')
        king_of_hearts = Card(13, 'H')
        ace_of_diamonds = Card(1, 'D')
        two_of_diamonds = Card(2, 'D')
        three_of_diamonds = Card(3, 'D')
        four_of_diamonds = Card(4, 'D')
        five_of_diamonds = Card(5, 'D')
        six_of_diamonds = Card(6, 'D')
        seven_of_diamonds = Card(7, 'D')
        eight_of_diamonds = Card(8, 'D')
        nine_of_diamonds = Card(9, 'D')
        ten_of_diamonds = Card(10, 'D')
        jack_of_diamonds = Card(11, 'D')
        queen_of_diamonds = Card(12, 'D')
        king_of_diamonds = Card(13, 'D')
        self.cards_array = [ace_of_clubs, two_of_clubs, three_of_clubs, four_of_clubs, five_of_clubs,
                            six_of_clubs, seven_of_clubs, eight_of_clubs, nine_of_clubs, ten_of_clubs,
                            jack_of_clubs, queen_of_clubs, king_of_clubs,
                            ace_of_spades, two_of_spades, three_of_spades, four_of_spades, five_of_spades,
                            six_of_spades, seven_of_spades, eight_of_spades, nine_of_spades, ten_of_spades,
                            jack_of_spades, queen_of_spades, king_of_spades,
                            ace_of_hearts, two_of_hearts, three_of_hearts, four_of_hearts, five_of_hearts,
                            six_of_hearts, seven_of_hearts, eight_of_hearts, nine_of_hearts, ten_of_hearts,
                            jack_of_hearts, queen_of_hearts, king_of_hearts,
                            ace_of_diamonds, two_of_diamonds, three_of_diamonds, four_of_diamonds, five_of_diamonds,
                            six_of_diamonds, seven_of_diamonds, eight_of_diamonds, nine_of_diamonds, ten_of_diamonds,
                            jack_of_diamonds, queen_of_diamonds, king_of_diamonds]
        for i in range(4):
            random.shuffle(self.cards_array)

    def draw_card(self):
        top_card = self.cards_array[0]
        self.cards_array.pop(0)
        return top_card