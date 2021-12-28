from model.deck import Deck
from model.card import Card, Value, Suit

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

five_diamond = Card(Value.Five, Suit.Diamonds)
four_spade = Card(Value.Four, Suit.Spades)
five_club = Card(Value.Five, Suit.Clubs)
four_heart = Card(Value.Four, Suit.Hearts)

print(five_diamond.same_color(four_heart))
print(five_diamond.same_color(four_spade))
print(five_club.same_color(four_heart))
print(five_club.same_color(four_spade))

print({1}.issubset({1, 2}))
