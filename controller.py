"""
CONTROLLER:

- accepts user input
- delegates:
        - data representation to VIEW
        - data handling       to MODEL

"""
from view import View
from model import Session
from model import Player, HumanPlayer

import rps_exceptions as re

import controller_utils as cu


class Controller:
    def __init__(self, view: View, session: Session):
        self.session = session
        self.view = view
        self.player_1 = None
        self.player_2 = None

    def act_on_login_choice(self, choice):
        """

        :param choice: str - can be: -- l, r or q
        :return username (str / None): None / 'q' / 'username'
        """

        username = 'John Doe'
        password = 'password'

        users_data = cu.get_users_data()
        users = users_data.keys()
        passwords = users_data.values()

        # ##########
        # Quit Game:
        # ##########
        if choice == 'q':
            return None

        # ######
        # LOGIN:
        # ######
        elif choice == 'l':

            # verify if username - in database
            while True:

                username = cu.ask_for_username_password(password=False)

                if username in ['q', 'Q']:
                    return 'q'  # quit to main menu

                if username in users:
                    break  # continue to next while

                else:  # if username - not in database => unknown user message
                    self.view.unknown_user_message()

            # verify password:
            while True:

                password = cu.ask_for_username_password()

                if password in ['q', 'Q']:
                    return 'q'  # quit to main menu

                # password does not correspond to user
                if password != users_data[username]:
                    self.view.invalid_password_message()

                else:
                    break  # continue to print welcome back message

            self.view.print_old_user_message(username)

        # #########
        # Register:
        # #########
        elif choice == 'r':

            self.view.print_register_message()

            while True:
                username = cu.ask_for_username_password(password=False)

                if username in ['q', 'Q']:
                    return 'q'  # quit to main menu

                # verify if username not already in database:
                if username in users:
                    self.view.username_already_in_use_message(username)

                else:
                    break

            while True:

                password = cu.ask_for_username_password()

                if password in ['q', 'Q']:
                    return 'q'  # quit to main menu
                else:
                    break

            self.view.print_new_user_message(username)

            # todo: write on csv the new user and password

        return username

    @staticmethod
    def act_on_logged_in_menu(played_games: list, game_choices: list) -> str:
        """
        :param played_games: (list): ex: [2, 0, 0, 5, 0]
        :param game_choices: (list): ['s', 'e', 'm', 'h', 'i']

        :return: choice: (str): - one of: 's', 'e', 'm', 'h', 'i', 'n', 'q'
        """

        # verify list length match:
        if len(played_games) != len(game_choices):
            raise re.ListLengthMismatch

        # only show saved games options:
        eligible_choices_list = [x for i, x in
                                 enumerate(game_choices) if
                                 played_games[i] != 0]
        eligible_choices_list.extend(['n', 'q'])

        choice = cu.make_choice(eligible_choices_list)

        return choice




    @staticmethod
    def chose_game(game_files: list) -> str:
        """Ask user to choose a game from the list of files with game rules.
        Returns file name for chosen game.

        Args:
            game_files (list(str)): list of strings with name of
                        files in the 'Rules' directory
                        ex: ['RPS-3.txt', 'RPS-5.txt', 'RPS-7.txt', ... ]

        Returns:
            chosen_game (str): string with the name of the file
                        ex: 'RPS-3.txt'

        """

        while True:
            try:
                choice = int(input(f'Choose a game (1 '
                                   f'to {len(game_files)}): '))
                assert choice in [x for x in range(1, len(game_files) + 1)]

            except (AssertionError, ValueError):
                print('Please choose on of the options above!')

            else:

                chosen_game = game_files[choice - 1]
                return chosen_game


    def get_com_and_win_dict(self):
        """Chose game. Print rules. Get components and winning dictionary.

        :param game_type (str): type of game:
                    Can be one of the following:
                                - s - skirmish
                                - e - easy
                                - m - medium
                                - h - hard
                                - i - impossible
        :return (tuple): components, win_dict
        """

        # available games:
        # 1. get:
        available_games = self.session.get_available_games()
        # 2. print:
        self.view.print_available_games(available_games)
        # 3. chose:
        chosen_game = self.chose_game(available_games)

        # Rules for chosen game:
        # 1. extract:
        rules = self.session.extract_rules(chosen_game)
        # 2. print rules:
        self.view.print_rules(rules)

        # Game components and Winning dictionary:
        # 1. get:
        components, win_dict = self.session.get_components_dict(rules)

        return components, win_dict

    def play_round(self, components: list, win_dict: dict, player_1, player_2):

        # print game options:
        self.view.print_options(components)

    def chose_opponent(self):

        self.view.prt_opponent_choice()
        choices = ['h', 'c', 'q']
        choice = cu.make_choice(choices)

        if choice == 'c':
            self.player_2 = Player()
        elif choice == 'h':

            # login menu:
            self.view.print_login_menu()
            login_register_choice_options = ['l', 'r', 'q']
            login_choice = cu.make_choice(login_register_choice_options)
            username, password = self.act_on_login_choice(login_choice)

            self.player_2 = HumanPlayer(username)


    def login_register_loop(self):

        while True:
            # Main menu - Login / Register / Quit:
            self.view.print_login_menu()
            login_register_choice_options = ['l', 'r', 'q']
            login_choice = cu.make_choice(login_register_choice_options)
            username = self.act_on_login_choice(login_choice)

            # Validate username, password:
            # (Q) - Quit game
            if not username:
                return None

            # Return to main menu:
            elif username == 'q':
                continue

            # if username and password are accepted:
            else:
                # all saved usernames
                users = cu.get_users_data().keys()

                # ######################################
                # Logged In Menu - chose a new game,
                #                - continue a saved game
                #                - quit to main menu
                # ######################################
                if username in users:

                    # from nr of saved games -> view logged in menu:
                    played_games = [2, 0, 0, 5, 0]
                    # todo: get list from saved games

                    self.view.prt_logged_in_menu(played_games)

                    played_games_choices = ['s', 'e', 'm', 'h', 'i']

                    old_user_choice = self.act_on_logged_in_menu(
                                                played_games,
                                                played_games_choices)

                    if old_user_choice == 'q':  # return to main menu
                        continue
                    elif old_user_choice == 'n':  # new game menu
                        # TODO - go to New Game menu
                        print('TODO - go to New Game menu')
                    elif old_user_choice in played_games_choices:
                        # TODO - continue a saved game
                        print('continue a saved game')

                # #######################################
                #  Registered menu - chose a game to play
                #                  - quit to main menu
                # #######################################
                else:
                    self.view.prt_new_game_menu()
                    play_mode_choice_options = ['s', 'e', 'm', 'h', 'i', 'q']
                    game_choice = cu.make_choice(play_mode_choice_options)
                    print('new game choice ===---> ', game_choice)

                    # return to main menu:
                    if game_choice == 'q':
                        continue
                    elif game_choice == 's':
                        # TODO - play skirmish
                        print('Chosen play mode: Skirmish')
                break

        print('//// username: ', username)
        # print('//// password: ', password)

    def play_session(self):
        # A. Welcome message:
        self.view.message_welcome()

        # B. Main menu - Login / Register / Quit
        self.login_register_loop()

        # B. Enter username and password:
        # username = self.ask_for_username()
        # users = self.get_users_data()
        # self.verify_username(username, users)
        # self.player_1 = HumanPlayer(username)

        # password = self.ask_for_password()

        # C. Print Menu:

        # C.1 New Game Menu:

        # C.2 Continue game Menu - chose which game to continue
        #                        - if against human player - ask password




def main():
    c = Controller(View(), Session())
    c.play_session()

if __name__ == '__main__':
    main()
