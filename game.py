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
            self.cascade_piles[count % num_piles].cards.append(card)

    def execute_move(self, source, index, target):
        # Validate inputs
        source_pile_type = FreeCellModel.valid_pile_type_check(source[0])
        source_pile_ind = FreeCellModel.valid_index_check(source[1:])
        index = FreeCellModel.valid_index_check(index)
        target_pile_type = FreeCellModel.valid_pile_type_check(target[0], source=False)
        target_pile_ind = FreeCellModel.valid_index_check(target[1:])

        # if source_pile_type == 'C':
        #     if target_pile_type == 'F':
        #         self.foundation_piles[target_pile_ind].append(self.cascade_piles[source_pile_ind].pop(index))
        # else:
        #     print('Failed')

        self.move(source_pile_type, source_pile_ind, index, target_pile_type, target_pile_ind)

    def move(self, source_pile_type, source_pile_ind, index, target_pile_type, target_pile_ind):
        source = self.select_pile(source_pile_type, source_pile_ind)
        target = self.select_pile(target_pile_type, target_pile_ind)

        pass

    def select_pile(self, pile_type, pile_ind):
        try:
            if pile_type == 'C':
                return self.cascade_piles[pile_ind]
            elif pile_type == 'O':
                return self.open_piles[pile_ind]
            else:
                return self.foundation_piles[pile_ind]
        # Handles index out of bounds
        except IndexError:
            raise IndexError('Index out of bounds')


    @staticmethod
    def valid_pile_type_check(pile_type, source=True):
        if source:
            if pile_type in ['C', 'O']:
                return pile_type
            else:
                raise ValueError('Invalid pile type identifier')
        else:
            if pile_type in ['C', 'O', 'F']:
                return pile_type
            else:
                raise ValueError('Invalid pile type identifier')

    @staticmethod
    def valid_index_check(index):
        try:
            index = int(index)
            # to scale index down to start at 0
            return index - 1
        except ValueError:
            raise TypeError('Index must be an integer')

    def play(self):
        print(self)
        playing = True
        while playing:
            user_input = input('Make a move, enter q to quit\n')
            if user_input == 'q':
                playing = False
            else:
                print(f'You input {user_input}')
                args = user_input.split()
                if len(args) != 3:
                    print('Invalid number of inputs')
                    continue
                # for arg in args:
                #     print(arg)
                try:
                    self.execute_move(args[0], args[1], args[2])
                except Exception as e:
                    print(f'Invalid move: {e}')
                print(self)
        print('Process complete')


def main():
    model = FreeCellModel(4, 4)
    # model.play()
    # print(model.__class__.valid_index_check('a'))
    # model.__class__.valid_pile_type_check('C')
    # print(FreeCellModel.valid_pile_type_check('C'))


if __name__ == "__main__":
    main()
