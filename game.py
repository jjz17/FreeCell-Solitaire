from deck import Deck


class FreeCellModel:
    def __init__(self):
        self.deck = Deck().shuffle()
        self.foundation_piles = []
        self.open_piles = []
        self.cascade_piles = []


def main():
    playing = True
    while playing:
        user_input = input('Make a move, enter q to quit\n')
        if user_input == 'q':
            playing = False
        else:
            print(f'You input {user_input}')
    print('Process complete')

if __name__ == "__main__":
    main()