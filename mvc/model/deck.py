from mvc.model.card import Card, Value, Suit
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for value in Value:
            for suit in Suit:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)
