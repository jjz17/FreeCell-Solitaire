import random

from deck import Deck
from game import FreeCellModel

deck = Deck()
print(deck.cards)
deck.shuffle()
print(deck.cards)
# for card in deck.cards:
#     print(card)
#
# list = [1,2,3,4,5]
# random.shuffle(list)
# print(list)
