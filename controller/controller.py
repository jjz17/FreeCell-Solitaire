from model.game import FreeCellModel
from view.text_view import TextView


class Controller:
    def __init__(self):
        self.model = FreeCellModel(4, 4)
        self.view = TextView(self.model)

    def set_up(self):
        print('\nCustomize your FreeCell Solitaire game by specifying the number of cascade and open piles you would '
              'like.\n\nThe default is 4 cascade and 4 open piles.\n\nTo play the default game, hit enter at the prompt.')
        # self.model.customize_model()
        started = False
        while not started:
            try:
                num_cascade_piles = input('# Cascade Piles: ')
                if num_cascade_piles.split():
                    num_open_piles = input('# Open Piles: ')
                    num_cascade_piles = Controller.valid_integer_check(num_cascade_piles)
                    num_open_piles = Controller.valid_integer_check(num_open_piles)
                    try:
                        self.model.set_piles(num_cascade_piles, num_open_piles)
                        # self.view = TextView(self.model)
                        started = True
                    except ValueError as e:
                        print(e)
                else:
                    started = True
            except TypeError as e:
                print(e)

        # Model is now created


    def play(self):
        # instructions = 'Enter q to quit, r to restart with the same deck, n to restart with a new deck, s to show board, and h for help\n'
        # print('\nFreeCell Solitaire: Implemented by Jason Zhang\n')
        # print('To execute a card move, specify the source pile, card index, '
        #       'and the target pile in the following format: C1 13 O3')
        # print(instructions)
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

    @staticmethod
    def valid_integer_check(integer):
        try:
            return int(integer)
        except ValueError:
            raise TypeError('Not an integer')


def main():
    controller = Controller()
    controller.set_up()
    controller.play()


if __name__ == "__main__":
    main()
