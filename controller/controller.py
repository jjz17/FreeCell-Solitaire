from model.game import FreeCellModel
from view.text_view import TextView


class Controller:
    def __init__(self):
        self.model = FreeCellModel(4, 4)
        self.view = TextView(self.model)

    def play(self):
        print('\nCustomize your FreeCell Solitaire game by specifying the number of cascade and open piles you would '
              'like.\n\nThe default is 4 cascade and 4 open piles.\n\nTo play the default game, hit enter at the prompt.')
        self.model.customize_model()
        # started = False
        # while not started:
        #     try:
        #         num_cascade = input('# Cascade Piles: ')
        #         if num_cascade.split():
        #             num_open = input('# Open Piles: ')
        #             num_cascade = Controller.valid_integer_check(num_cascade)
        #             num_open = Controller.valid_integer_check(num_open)
        #             try:
        #                 self.model = FreeCellModel(num_cascade, num_open)
        #                 self.view = TextView(self.model)
        #                 started = True
        #             except ValueError as e:
        #                 print(e)
        #         else:
        #             started = True
        #     except TypeError as e:
        #         print(e)
        self.model.play()

    @staticmethod
    def valid_integer_check(integer):
        try:
            return int(integer)
        except ValueError:
            raise TypeError('Not an integer')


def main():
    controller = Controller()
    controller.play()


if __name__ == "__main__":
    main()
