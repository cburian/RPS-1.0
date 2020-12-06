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
    """Robot player
    """

    def __init__(self, username: str = 'Computer'):
        self._username = username
        self.__score = 0
        self._choice = ''  # game choice: 'rock'

    @property
    def username(self):
        return self._username

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, choice):
        self._choice = choice

    def make_game_choice(self, options: list) -> str:
        """Randomly chooses one component from the list

            Args:
                 options (list): - list of game options
                            ex: ['rock', 'paper', etc.]

            Returns:
                npc_choice (str): - npc choice
                            ex: 'rock'

            """
        import random
        self._choice = random.choice(options)
        return self._choice


class HumanPlayer(Player):
    def __init__(self, username='Player1'):
        super().__init__(username)

    # def _set_name(self):
    #
    #     while True:
    #         try:
    #             self._username = input('Enter username: ')
    #             # todo: use regex - username has to start with letter
    #             # todo:           - just letters and numbers allowed
    #         except ValueError:
    #             print('Username invalid!')
    #         else:
    #             break
    #
    # def _set_choice(self, options: list) -> str:
    #     """Randomly chooses one component from the list
    #
    #         Args:
    #              options (list): - list of game options
    #                         ex: ['rock', 'paper', etc.]
    #
    #         Returns:
    #             human_choice (str): - playable character choice
    #                         ex: 'rock'
    #
    #         """
    #
    #     while True:
    #         try:
    #             choice = int(input(f'\nYour choice: '))
    #             assert choice in [x for x in range(1, len(options) + 1)]
    #
    #         except (AssertionError, ValueError):
    #             print('Please choose on of the options above!')
    #
    #         else:
    #
    #             self._choice = options[choice - 1]
    #             return self._choice


class Session:
    def __init__(self):
        pass

    @staticmethod
    def get_available_games(directory: str = 'Rules') -> list:
        """Returns a list of files (game rules) in 'Rules' directory

            Returns:
                game_files (list(str)): list of strings with name of
                            files in the 'Rules' directory
                            ex: ['RPS-3.txt', 'RPS-5.txt', 'RPS-7.txt', ... ]

        """
        import os
        game_files = os.listdir(directory)
        return sorted(game_files)

    @staticmethod
    def extract_rules(game_file_name: str) -> str:
        """Function to extract game rules from txt file.

        Args:
            game_file_name (str): string with the name of the file
                        ex: 'RPS-3.txt'

        Returns:
            rules (str): - string with game rules
                        Ex.: 'Rock breaks scissors, \nscissors cuts paper,
                        \npaper covers rock'

        """
        game_file_name = 'Rules/' + game_file_name
        with open(game_file_name) as f:
            data = f.readlines()
        rules = ''.join(data)

        return rules

    @staticmethod
    def get_components_dict(rules: str) -> tuple:
        """Creates a dictionary from the game rules string

        Takes in rules (str) and extracts a dictionary with
            keys   = tuple(winner(str), looser(str))
            values = rule ex: "Rock breaks scissors"
                    ex: {('rock', 'paper') : 'Rock breaks scissors'}

        Args:
            rules (str): - rules of the game
                    ex: 'Rock breaks scissors, \n
                        scissors cuts paper, \n
                        paper covers rock'

        Return:
            components (list): - all the components of the game
                    ex: ['rock', 'paper', 'scissors')]

            win_dic (dict): - wining dictionary - with the following form:
                    {(winner, looser) : rule}
                    ex: {('rock', 'paper') : 'Rock breaks scissors'}

        """
        components = set()
        win_dic = {}

        rules_list = rules.split(', \n')
        for rule in rules_list:
            strong_component = rule.split(' ')[0].lower()
            weak_component = rule.split(' ')[-1].lower()

            if strong_component not in components:
                components.add(strong_component)

            if (strong_component, weak_component) not in win_dic.keys():
                win_dic[(strong_component, weak_component)] = rule

        return list(components), win_dic

    @staticmethod
    def determine_result(player_1: HumanPlayer, player_2: Player,
                         win_dic: dict) -> tuple:
        """Determines the winner of a RPS round

        Args:
            h_choice (str): - human answer
                    ex: 'rock'

            npc_choice (str): - npc answer
                    ex: 'scissors'

            win_dic (dict): - winning dictionary - with the following form:
                    {(winner, looser) : rule}
                    ex: {('rock', 'paper') : 'Rock breaks scissors'}

        Returns:
            winner (str / None): - the winning choice
                                 - can be: - str: 'rock' - rock won
                                           - None:       - draw

            winning_rule (str / None): - the rule explaining the win
                                       - can be: - str: 'Rock breaks scissors'
                                                 - None: draw

        """
        p1_c = player_1.choice
        p2_c = player_2.choice
        if p1_c != p2_c:

            if (p1_c, p2_c) in win_dic.keys():
                winner = p1_c
                winning_rule = win_dic[(p1_c, p2_c)]
            else:
                winner = p2_c
                winning_rule = win_dic[(p2_c, p1_c)]
            return winner, winning_rule

        return None, None,




#
# def player_choice(player, options):
#     while True:
#         try:
#             choice = int(input('Your choice:'))
#             options_index_list = [x for x in range(1, len(options) + 1)]
#             assert choice in options_index_list
#         except (AssertionError, ValueError):
#             print('Choose a valid option.')
#         else:
#             player.choice = options[choice - 1]
#             break
#
#
# p = Player('cos')
# p.score = 4
# print(p.score)
#
# p2 = HumanPlayer('Mircea')
# p2.score = 5
# print(p2.score)
#
# options = ['r', 'p', 's']
# player_choice(p, options)
# print(p.choice)
