# FreeCell Solitaire

Implementation of FreeCell Solitaire in Python

[comment]: <> ([Description]&#40;https://course.ccs.neu.edu/cs3500f16/hw_02_assignment.html&#41;)

## Card Values
Suits do not affect card values.

2 - 10 all are the same value as the card name.
A, J, Q, and K are worth 1, 11, 12, and 13, respectively.

## Gameplay
[Detailed Game Description](https://en.wikipedia.org/wiki/FreeCell)

Simply run the script to begin playing. You will have the option to customize your game in terms of the number of 
cascade and open piles that are available. The deck will automatically be shuffled and distributed into the cascade piles,
and the goal is to move all the cards to the foundation piles in the proper order. Once all cards are transferred to the
foundation piles, you have won the game! Note: This version of the game only supports single card moves currently.

[comment]: <> (**Note that for the purpose of this script is to allow the user to play a simple hand of Blackjack without some of the higher level parts of the game like betting or splitting doubles. All ties go to the player in this version of the game.)

## Demo

[comment]: <> (![image]&#40;https://user-images.githubusercontent.com/48007679/136310729-e354ab8f-c5d5-4eee-bd9c-14857be688d3.png&#41;)
![image](https://github.com/jjz17/FreeCell-Solitaire/raw/main/screenshots/initialize_game.png)
![image](https://github.com/jjz17/FreeCell-Solitaire/raw/main/screenshots/playing_game.png)

  
## Deployment

To install requirements run
```bash
pip install -r requirements.txt
```

To deploy this project run
```bash
python run.py
```

## Testing

To test this project run
```bash
python -m pytest
```

[comment]: <> (## Links)

[comment]: <> (- [Repo]&#40;https://github.com/jjz17/FreeCell-Solitaire "<project-name> Repo"&#41;)

[comment]: <> (- [Live]&#40;<Homepage url> "Live View"&#41;)

[comment]: <> (- [Bugs]&#40;https://github.com/Rohit19060/<project-name>/issues "Issues Page"&#41;)

[comment]: <> (- [API]&#40;<API Link> "API"&#41;)

[comment]: <> (## Screenshots)

[comment]: <> (![Home Page]&#40;/screenshots/1.png "Home Page"&#41;)

[comment]: <> (![]&#40;/screenshots/2.png&#41;)

## Built With

- Python

## Future Updates

- Multi-card move support

## Author

**Jason Zhang**

- [Profile](https://github.com/jjz17 "Jason Zhang")

- [Email](mailto:jasonjzhang17@gmail.com?subject=Hi "Hi!")

[comment]: <> (- [Website]&#40;"Welcome"&#41;)

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!
