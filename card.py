from enum import Enum


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value.value}{self.suit.value}'

    def __str__(self):
        return f'{self.value.value}{self.suit.value}'


class Value(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


class Suit(Enum):
    Clubs = "♧"
    Diamonds = "♢"
    Hearts = "♡"
    Spades = "♤"
