from model.deck import Deck
from model.pile import FoundationPile, CascadePile, OpenPile


class FreeCellModel:
    def __init__(self, num_cascade_piles, num_open_piles):
        self.deck = Deck()
        self.deck.shuffle()
        self.set_piles(num_cascade_piles, num_open_piles)

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

    def set_piles(self, num_cascade_piles, num_open_piles):
        if num_cascade_piles < 4:
            raise ValueError('Must have at least 4 Cascade piles')
        if num_open_piles < 2:
            raise ValueError('Must have at least 2 Open piles')
        self.foundation_piles = [FoundationPile([]) for i in range(4)]
        self.init_cascade_piles(num_cascade_piles)
        self.open_piles = [OpenPile([]) for i in range(num_open_piles)]

    def init_cascade_piles(self, num_piles):
        # Create cascade piles
        self.cascade_piles = [CascadePile([]) for i in range(num_piles)]
        # Add cards to cascade piles
        for count, card in enumerate(self.deck.cards):
            self.cascade_piles[count % num_piles].cards.append(card)

    def customize_model(self):
        customized = False
        while not customized:
            try:
                num_cascade_piles = input('# Cascade Piles: ')
                if num_cascade_piles.split():
                    num_open_piles = input('# Open Piles: ')
                    num_cascade_piles = FreeCellModel.valid_integer_check(num_cascade_piles)
                    num_open_piles = FreeCellModel.valid_integer_check(num_open_piles)
                    try:
                        self.set_piles(num_cascade_piles, num_open_piles)
                        customized = True
                    except ValueError as e:
                        print(e)
                else:
                    customized = True
            except TypeError as e:
                print(e)

    def reset_board(self):
        num_cascade_piles = len(self.cascade_piles)
        num_open_piles = len(self.open_piles)
        self.foundation_piles = [FoundationPile([]) for i in range(4)]
        self.init_cascade_piles(num_cascade_piles)
        self.open_piles = [OpenPile([]) for i in range(num_open_piles)]

    def reset_game(self):
        num_cascade_piles = len(self.cascade_piles)
        num_open_piles = len(self.open_piles)
        self.deck.shuffle()
        self.foundation_piles = [FoundationPile([]) for i in range(4)]
        self.init_cascade_piles(num_cascade_piles)
        self.open_piles = [OpenPile([]) for i in range(num_open_piles)]

    def execute_move(self, source_string, index_string, target_string):
        # Validate inputs (proper formatting)
        source_pile_type = FreeCellModel.valid_pile_type_check(source_string[0])
        source_pile_ind = FreeCellModel.valid_index_check(source_string[1:])
        index = FreeCellModel.valid_index_check(index_string)
        target_pile_type = FreeCellModel.valid_pile_type_check(target_string[0], source=False)
        target_pile_ind = FreeCellModel.valid_index_check(target_string[1:])

        source = self.select_pile(source_pile_type, source_pile_ind)
        target = self.select_pile(target_pile_type, target_pile_ind)

        # Source and target are guaranteed to be valid piles

        # Raises error if move is illegal
        self.legal_move_check(source, index, target)

        self.move(source, index, target)

    def legal_move_check(self, source, index, target):
        if source == target:
            raise ValueError('Source and target piles must be different')
        return source.legal_move_from_check(index, target)

    def move(self, source, index, target):
        # Move the card
        target.append(source.pop(index))

    # Handles index out of bounds
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
                raise ValueError('Invalid pile type identifier, source piles are either C or O')
        else:
            if pile_type in ['C', 'O', 'F']:
                return pile_type
            else:
                raise ValueError('Invalid pile type identifier, target piles are either C, O, or F')

    @staticmethod
    def valid_index_check(index):
        try:
            index = int(index)
            # to scale index down to start at 0
            return index - 1
        except ValueError:
            raise TypeError('Index must be an integer')

    @staticmethod
    def valid_integer_check(integer):
        try:
            return int(integer)
        except ValueError:
            raise TypeError('Not an integer')

    def play(self):
        instructions = 'Enter q to quit, r to restart with the same deck, n to restart with a new deck, s to show board, and h for help\n'
        print('\nFreeCell Solitaire: Implemented by Jason Zhang\n')
        print('To execute a card move, specify the source pile, card index, '
              'and the target pile in the following format: C1 13 O3')
        print(instructions)
        # Display board
        print(self)
        playing = True
        while playing:
            user_input = input('Next move: ')
            if user_input == 'q':
                playing = False
            elif user_input == 'r':
                self.reset_board()
                print(self)
            elif user_input == 'n':
                self.reset_game()
                print(self)
            elif user_input == 's':
                print(self)
            elif user_input == 'h':
                print(instructions)
            else:
                # print(f'You input {user_input}')
                args = user_input.split()
                if len(args) != 3:
                    print('\nInvalid number of inputs\n')
                    continue
                try:
                    self.execute_move(args[0], args[1], args[2])
                except Exception as e:
                    print(f'\nInvalid move: {e}\n')
                print(self)
        print('Process complete')


def main():
    model = FreeCellModel(4, 4)
    model.play()


if __name__ == "__main__":
    main()
