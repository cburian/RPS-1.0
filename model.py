"""
MODEL

- business logic
- manages data
- defines rules and behaviours
- data can be stored in:
            - MODEL
            - database
- only MODEL has access to database

Has to do:
    - return available games
    - extract rules
"""


class Player:
    def __init__(self, username: str):
        self._username = username
        self.__score = 0
        self.__choice = ''  # game choice: 'rock'

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def choice(self):
        return self.__choice

    @choice.setter
    def choice(self, choice, valid_choices: list):
        # try:
        #     assert choice in valid_choices
        # except AssertionError:
        self.__choice = choice


class HumanPlayer(Player):
    def __init__(self, username):
        super().__init__(username)


class Round:
    def __init__(self):
        pass

def player_choice(player, options):
    while True:
        try:
            choice = int(input('Your choice:'))
            player.choice(choice, options)
        except (AssertionError, ValueError):
            print('Choose a valid option.')
        else:
            pass


p = Player('cos')
p.score = 4
print(p.score)

p2 = HumanPlayer('Mircea')
p2.score = 5
print(p2.score)
