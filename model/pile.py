from typing import List

from model.card import Value, Card


class Pile:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def append(self, element: Card):
        self.cards.append(element)

    def pop(self, index: int) -> Card:
        return self.cards.pop(index)

    def len(self) -> int:
        return len(self.cards)

    def last_card(self) -> Card:
        return self.cards[-1]

    def legal_move_from_check(self, index: int, target):
        pass


class FoundationPile(Pile):
    def legal_move_from_check(self, index: int, target: Pile):
        raise ValueError('Cannot move cards from foundation piles')

    def legal_move_to_check(self, card):
        if len(self.cards) == 0:
            if card.value != Value.Ace:
                raise ValueError('Cannot start foundation pile with a non-Ace card')
        else:
            if not (self.last_card().value_one_less_than(card) and self.last_card().same_suit(card)):
                raise ValueError('Invalid card')


class OpenPile(Pile):
    def legal_move_from_check(self, index: int, target: Pile):
        # If pile is empty
        if len(self.cards) == 0:
            raise ValueError('Cannot move card from empty open pile')
        elif index == 0:
            card = self.cards[index]
            return target.legal_move_to_check(card)
        else:
            raise ValueError('Index must be positive')

    def legal_move_to_check(self, card: Card):
        if len(self.cards) != 0:
            raise ValueError('Cannot move cards to full open pile')


class CascadePile(Pile):
    def legal_move_from_check(self, index: int, target: Pile):
        if index == len(self.cards) - 1:
            card = self.cards[index]
            return target.legal_move_to_check(card)
        else:
            raise IndexError('Cannot move card that is not at the end of the pile')

    def legal_move_to_check(self, card: Card):
        if not card.value_one_less_than(self.last_card()) or card.same_color(self.last_card()):
            raise ValueError('Invalid card')
