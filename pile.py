class Pile:
    def __init__(self, cards):
        self.cards = cards

    def append(self, element):
        self.cards.append(element)

    def pop(self, index):
        return self.cards.pop(index)


class FoundationPile(Pile):
    pass


class OpenPile(Pile):
    pass


class CascadePile(Pile):
    pass