class ConsoleTextView:
    instructions = 'Enter q to quit, r to restart with the same deck, n to restart with a new deck, b to show board, ' \
                   's for game stats, and h for help\n '
    initial_dialogue = '\nFreeCell Solitaire: Implemented by Jason Zhang\nTo execute a card move, specify the source ' \
                       'pile, card index, and the target pile in the following format: C1 13 O3 '
    set_up_dialogue = '\nCustomize your FreeCell Solitaire game by specifying the number of cascade and open piles ' \
                      'you would like.\n\nThe default is 4 cascade and 4 open piles.\n\nTo play the default game, ' \
                      'hit enter at the prompt.'
    end_dialogue = 'Game ended.'
    invalid_input_dialogue = '\nInvalid number of inputs\n'
    game_won_dialogue = 'You won!'

    def __init__(self, model):
        self.model = model

    def render_board(self):
        print(self.model)

    def render_instructions(self):
        print(self.instructions)

    def render_initial_dialogue(self):
        print(self.initial_dialogue)

    def render_set_up_dialogue(self):
        print(self.set_up_dialogue)

    def render_end_dialogue(self):
        print(self.end_dialogue)

    def render_error_message(self, error):
        print(f'\nInvalid move: {error}\n')

    def render_invalid_input_message(self):
        print(self.invalid_input_dialogue)

    def render_game_won_dialogue(self):
        print(self.game_won_dialogue)

    def render_game_stats(self):
        print(self.model.game_stats())

