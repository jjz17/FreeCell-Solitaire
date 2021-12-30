from model.game import FreeCellModel
from view.text_view import ConsoleTextView


def valid_integer_check(integer):
    try:
        return int(integer)
    except ValueError:
        raise TypeError('Not an integer')


class Controller:
    def __init__(self):
        self.model = FreeCellModel(4, 4)
        self.view = ConsoleTextView(self.model)

    def set_up(self):
        self.view.render_set_up_dialogue()
        started = False
        while not started:
            try:
                num_cascade_piles = input('# Cascade Piles: ')
                if num_cascade_piles.split():
                    num_open_piles = input('# Open Piles: ')
                    num_cascade_piles = valid_integer_check(num_cascade_piles)
                    num_open_piles = valid_integer_check(num_open_piles)
                    try:
                        self.model.set_piles(num_cascade_piles, num_open_piles)
                        started = True
                    except ValueError as e:
                        print(e)
                else:
                    started = True
            except TypeError as e:
                print(e)

    def play(self):
        self.view.render_initial_dialogue()
        self.view.render_instructions()
        # Display board
        self.view.render_board()
        playing = True
        while playing:
            user_input = input('Next move: ')
            if user_input == 'q':
                playing = False
            elif user_input == 'r':
                self.model.reset_board()
                self.view.render_board()
            elif user_input == 'n':
                self.model.reset_game()
                self.view.render_board()
            elif user_input == 's':
                self.view.render_board()
            elif user_input == 'h':
                self.view.render_instructions()
            else:
                args = user_input.split()
                if len(args) != 3:
                    print('\nInvalid number of inputs\n')
                    continue
                try:
                    self.model.execute_move(args[0], args[1], args[2])
                except Exception as e:
                    print(f'\nInvalid move: {e}\n')
                self.view.render_board()
        print('Process complete')


def main():
    controller = Controller()
    controller.set_up()
    controller.play()


if __name__ == "__main__":
    main()
