from pytest_unordered import unordered

from mvc.model.deck import Deck
from mvc.model.card import Card, Value, Suit
from mvc.model.pile import Pile

import copy

def test_card():
    '''
    GIVEN two cards
    WHEN the cards are compared
    THEN check that they are equal iff they have the same value and suit
    '''
    five_diamond1 = Card(Value.Five, Suit.Diamonds)
    five_diamond2 = Card(Value.Five, Suit.Diamonds)
    five_heart = Card(Value.Five, Suit.Hearts)
    five_spade = Card(Value.Five, Suit.Spades)
    jack_diamond = Card(Value.Jack, Suit.Diamonds)

    assert five_diamond1  == five_diamond2
    assert five_diamond1 != five_heart
    assert five_diamond1 != five_spade
    assert five_diamond1 != jack_diamond

def test_deck():
    '''
    GIVEN a deck
    WHEN the deck is shuffled
    THEN check, ignoring ordering, that the deck's cards are equal
    '''
    deck = Deck()
    unshuffled_deck = Deck()
    assert len(deck.cards) == 52
    deck.shuffle()
    assert len(deck.cards) == 52
    assert unshuffled_deck.cards == unordered(deck.cards)

def test_pile():
    '''
    GIVEN a pile
    WHEN the pile's functions are called
    THEN check the expected behavior occurs
    '''
    deck = Deck()
    deck.shuffle()
    pile = Pile(deck.cards)
    assert pile.len() == 52
    pile.pop(0)
    assert pile.len() == 51

