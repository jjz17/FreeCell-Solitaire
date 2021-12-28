from game import FreeCellModel


class Controller:
    def __init__(self):
        self.model = FreeCellModel(4, 4)

    def play(self):
        print('Customize your FreeCell Solitaire game by specifying the number of cascade and open piles you would '
              'like.\n The default is 4 cascade and 4 open piles.\n To play the default game, hit enter at the prompt.')
        num_cascade = int(input('# Cascade Piles: '))
        num_open = int(input('# Open Piles: '))
        if num_cascade != 4 or num_open != 4:
            self.model = FreeCellModel(num_cascade, num_open)
        self.model.play()

def main():
    controller = Controller()
    controller.play()


if __name__ == "__main__":
    main()