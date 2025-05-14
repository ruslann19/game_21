from random import randrange

from .create_deck import create_deck


class Dealer:
    def __init__(self):
        self.deck = create_deck()

    def get_card(self):
        deck_len = len(self.deck)
        card_index = randrange(deck_len)

        card = self.deck[card_index]
        self.deck.pop(card_index)

        return card
