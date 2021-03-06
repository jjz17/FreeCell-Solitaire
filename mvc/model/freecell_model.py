from mvc.model.deck import Deck
from mvc.model.pile import Pile, FoundationPile, CascadePile, OpenPile


def legal_move_check(source: Pile, index: int, target: Pile) -> bool:
    if source == target:
        raise ValueError('Source and target piles must be different')
    source.legal_move_from_check(index, target)


def move(source: Pile, index: int, target: Pile):
    # Move the card
    target.append(source.pop(index))


def valid_pile_type_check(pile_type: str, source=True):
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


def valid_index_check(index: str):
    try:
        index = int(index)
        # to scale index down to start at 0
        return index - 1
    except ValueError:
        raise TypeError('Index must be an integer')


def valid_integer_check(integer: str):
    try:
        return int(integer)
    except ValueError:
        raise TypeError('Not an integer')


class FreeCellModel:
    def __init__(self, num_cascade_piles: int, num_open_piles: int):
        self.deck = Deck()
        self.deck.shuffle()
        self.foundation_piles = []
        self.cascade_piles = []
        self.open_piles = []
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

    def set_piles(self, num_cascade_piles: int, num_open_piles: int):
        if num_cascade_piles < 4:
            raise ValueError('Must have at least 4 Cascade piles')
        if num_open_piles < 2:
            raise ValueError('Must have at least 2 Open piles')
        self.foundation_piles = [FoundationPile([]) for i in range(4)]
        self.init_cascade_piles(num_cascade_piles)
        self.open_piles = [OpenPile([]) for i in range(num_open_piles)]

    def init_cascade_piles(self, num_piles: int):
        # Create cascade piles
        self.cascade_piles = [CascadePile([]) for i in range(num_piles)]
        # Add cards to cascade piles
        for count, card in enumerate(self.deck.cards):
            self.cascade_piles[count % num_piles].cards.append(card)

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

    def execute_move(self, source_string: str, index_string: str = 'auto', target_string: str = ''):
        # Validate inputs (proper formatting)
        source_pile_type = valid_pile_type_check(source_string[0])
        source_pile_ind = valid_index_check(source_string[1:])
        target_pile_type = valid_pile_type_check(target_string[0], source=False)
        target_pile_ind = valid_index_check(target_string[1:])

        source = self.select_pile(source_pile_type, source_pile_ind)
        target = self.select_pile(target_pile_type, target_pile_ind)

        # Source and target are guaranteed to be valid piles

        if index_string == 'auto':
            index = source.len() - 1
        else:
            index = valid_index_check(index_string)

        # Raises error if move is illegal
        legal_move_check(source, index, target)

        move(source, index, target)

    # Handles index out of bounds
    def select_pile(self, pile_type: str, pile_ind: int):
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

    def game_stats(self):
        num_foundation = self.cards_in_foundation()
        remaining = 52 - num_foundation
        return {'cards in foundation': num_foundation, 'cards to sort': remaining,
                '# cascade': len(self.cascade_piles),
                '# open': len(self.open_piles)}

    def cards_in_foundation(self):
        return sum([pile.len() for pile in self.foundation_piles])

    def game_won_check(self):
        return self.cards_in_foundation() == 52

    def progress(self):
        return self.cards_in_foundation() / 52
