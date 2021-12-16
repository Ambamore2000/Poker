class Player:

    def __init__(self, deck):
        self.first_card = deck.draw_card()
        self.second_card = deck.draw_card()

    def get_cards_in_hand(self):
        return [self.first_card, self.second_card]
