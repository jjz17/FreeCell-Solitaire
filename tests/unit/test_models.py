from pytest_unordered import unordered

from mvc.model.deck import Deck
from mvc.model.card import Card, Value, Suit

import copy

def test_new_deck():
    '''
    GIVEN a new deck
    WHEN the deck is shuffled
    THEN check the number of cards has not changed
    '''
    deck = Deck()
    unshuffled_deck = Deck()
    assert len(deck.cards) == 52
    deck.shuffle()
    assert len(deck.cards) == 52
    assert unshuffled_deck.cards == unordered(deck.cards)