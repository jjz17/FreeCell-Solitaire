from deck import Deck
from pile import FoundationPile, CascadePile, OpenPile
from card import Card


class FreeCellModel:
    def __init__(self, num_cascade_piles, num_open_piles):
        self.deck = Deck()
        self.deck.shuffle()
        self.foundation_piles = [FoundationPile([]) for i in range(4)]
        self.init_cascade_piles(num_cascade_piles)
        self.open_piles = [OpenPile([]) for i in range(num_open_piles)]

    def __str__(self):
        model_string = ''
        for count, foundation_pile in enumerate(self.foundation_piles):
            pile_string = ''
            for card in foundation_pile.cards:
                pile_string += f' {card.__str__()}'
            model_string += f'F{count + 1}:{pile_string}\n'
        for count, open_pile in enumerate(self.open_piles):
            pile_string = ''
            for card in open_pile.cards:
                pile_string += f' {card.__str__()}'
            model_string += f'O{count + 1}:{pile_string}\n'
        for count, cascade_pile in enumerate(self.cascade_piles):
            pile_string = ''
            for card in cascade_pile.cards:
                pile_string += f' {card.__str__()}'
            model_string += f'C{count + 1}:{pile_string}\n'
        return model_string

    def init_cascade_piles(self, num_piles):
        # Create cascade piles
        self.cascade_piles = [CascadePile([]) for i in range(num_piles)]
        # Add cards to cascade piles
        for count, card in enumerate(self.deck.cards):
            # index = count%num_piles
            # pile = self.cascade_piles[index]
            # new_card = Card(card.value, card.suit)
            # pile.cards.append(card)
            self.cascade_piles[count % num_piles].cards.append(card)


def main():
    # playing = True
    # while playing:
    #     user_input = input('Make a move, enter q to quit\n')
    #     if user_input == 'q':
    #         playing = False
    #     else:
    #         print(f'You input {user_input}')
    # print('Process complete')

    model = FreeCellModel(4, 4)
    print(model)


if __name__ == "__main__":
    main()
