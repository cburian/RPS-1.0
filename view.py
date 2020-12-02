"""
VIEW:

- presents data to the user
- NEVER call its own methods
"""


class View:

    def print_welcome(self):
        welcome_msg = 'Welcome to'
        game_name = 'RPS'
        msg_2 = 'A game of Rock Paper Scissors and its variants!'
        print()
        self.prt_delimiter(len(msg_2), '=')
        print(f'{welcome_msg:^{len(msg_2)}}')
        print(f'{game_name:^{len(msg_2)}}')
        self.prt_delimiter(len(msg_2), '=')
        print(msg_2)
        self.prt_delimiter(len(msg_2), '=')

    def print_login_menu(self):
        title_msg = 'Chose your action:'
        print()
        self.prt_delimiter(len(title_msg), '+')
        print(title_msg)
        print('(L) Login')
        print('(R) Register')
        print('(Q) Quit game')
        self.prt_delimiter(len(title_msg), '+')

    def username_already_in_use_message(self, username):
        msg_1 = f'{username} --- already in use!'
        msg_2 = f'Please choose another or quit to main menu and login.'

        print()
        self.prt_delimiter(len(msg_2), '!')
        print(f'{msg_1:^{len(msg_2)}}')
        print(msg_2)
        self.prt_delimiter(len(msg_2), '!')

    def invalid_password_message(self):
        msg = 'Invalid password. Please try again'

        print()
        self.prt_delimiter(len(msg), '!')
        print(msg)
        self.prt_delimiter(len(msg), '!')

    def unknown_user_message(self):
        msg = 'Unknown user! Please chose another.'

        print()
        self.prt_delimiter(len(msg), '!')
        print(msg)
        self.prt_delimiter(len(msg), '!')

    @staticmethod
    def print_new_user_message():
        print()
        print('Choose a username and password.')

    @staticmethod
    def print_old_user_message(username):
        print()
        print(f'Welcome back, {username}!')

    def prt_logged_in_menu(self, game_numbers: list):

        print_continue_flag = False
        for x in game_numbers:
            if x:
                print_continue_flag = True

        action_msg = 'Chose an action: '
        continue_mgs = 'Continue a saved game:'
        game_type = ['Skirmish', 'Ranked - Easy',
                     'Ranked - Medium', 'Ranked - Hard',
                     'Ranked - Impossible']

        print()

        if print_continue_flag:

            self.prt_delimiter(len(action_msg), '+')
            print(action_msg)
            print(continue_mgs)
            for index, nr_of_games in enumerate(game_numbers):
                if nr_of_games:
                    if index == 0:
                        choice = 'S'
                    else:
                        choice = game_type[index][9]
                    msg = f'\t({choice}) {game_type[index]} game ' \
                          f'- {nr_of_games} games'
                    print(msg)
            print('Or chose: ')
        else:
            self.prt_delimiter(len(action_msg), '+')
            print(action_msg)

        print('\t(N) New game')
        print('\t(Q) Quit to main menu')
        self.prt_delimiter(len(action_msg), '+')

    def prt_new_game_menu(self):

        title_msg = 'Chose a play mode:'
        print()

        self.prt_delimiter(len(title_msg), '+')
        print(title_msg)
        print('(S) Skirmish')
        print('(E) Ranked play - Easy -------> win 2 of 10')
        print('(M) Ranked play - Medium -----> win 5 of 10')
        print('(H) Ranked play - Hard -------> win 7 of 10')
        print('(I) Ranked play - Impossible -> win 10 of 10')
        print('(Q) Quit game')
        self.prt_delimiter(len(title_msg), '+')




    def print_available_games(self, game_files: list):
        """Prints the lists of available games

            Args:
                 game_files (list(str)): list of strings with name of
                            files in the 'Rules' directory
                            ex: ['RPS-3.txt', 'RPS-5.txt', 'RPS-7.txt', ... ]

            """

        available_games_msg = 'Available games:'
        print()
        print(available_games_msg)
        self.prt_delimiter(len(available_games_msg), '-')
        for index, game in enumerate(game_files):
            msg = f'({index + 1}) {game[:-4]}'
            print(f'{msg:^{len(available_games_msg)}}')
        self.prt_delimiter(len(available_games_msg), '-')

    @staticmethod
    def print_rules(rules: str):
        """Prints the rules of the games

        Args:
             rules (str): - string with game rules
                        Ex.: 'Rock breaks scissors, \nscissors cuts paper,
                        \npaper covers rock'

        """

        print()
        print('--- Game Rules: ---')
        print(rules)

    @staticmethod
    def print_options(components: list):
        """ Prints the options to choose from.

        Args:
            components (list): - game options (components)
                        ex: ['rock', 'paper', etc.]

        """
        print()
        print('Available options: ')
        for index, k in enumerate(components):
            print(f'({index + 1}) {k}')

    @staticmethod
    def prt_delimiter(length, border: str = '-'):
        """Applies border to message - for important messages

        todo: make this into a decorator
        """
        print(border * length)

    def print_outcome(self, winning_choice: str, winning_rule: str,
                      player_1_name: str, player_2_name: str,
                      player_1_choice: str, player_2_choice: str):
        """Prints the outcome of the round

        Args:
            winning_choice (str / None): - the winning choice
                                 - can be: - str: 'rock' - rock won
                                           - None:       - draw

            winning_rule (str / None): - the rule explaining the win
                                       - can be: - str: 'Rock breaks scissors'
                                                 - None: draw

            player_1_choice (str): - player choice
                        ex: 'rock'

            player_2_choice (str): - player choice
                        ex: 'rock'

        """

        if winning_choice:
            msg = 'EEERRROOORRR'
            if player_1_choice == winning_choice:
                msg = f'{player_1_name} wins! --- {winning_rule}'
            elif player_2_choice == winning_choice:
                msg = f'{player_2_name} loses! --- {winning_rule}'
            self.prt_delimiter(msg, '=')
        else:
            self.prt_delimiter('Draw!', '=')
