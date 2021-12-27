class Pile:
    def __init__(self, cards):
        self.cards = cards

    def append(self, element):
        self.cards.append(element)

    def pop(self, index):
        return self.cards.pop(index)

    def get_last_card(self):
        return self.cards[-1]


class FoundationPile(Pile):
    def legal_move_check(self):
        pass


class OpenPile(Pile):
    pass


class CascadePile(Pile):
    pass