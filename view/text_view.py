class TextView:
    instructions = 'Enter q to quit, r to restart with the same deck, n to restart with a new deck, s to show board, ' \
                   'and h for help\n '
    initial_dialogue = '\nFreeCell Solitaire: Implemented by Jason Zhang\nTo execute a card move, specify the source ' \
                       'pile, card index, and the target pile in the following format: C1 13 O3 '

    def __init__(self, model):
        self.model = model

    def render_board(self):
        print(self.model)

    def render_instructions(self):
        print(self.instructions)

    def render_initial_dialogue(self):
        print(self.initial_dialogue)
