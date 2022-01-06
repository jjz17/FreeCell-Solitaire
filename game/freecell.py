from controller.controller import Controller


def main():
    controller = Controller()
    controller.set_up()
    # controller.play()
    controller.simple_play()


if __name__ == "__main__":
    main()