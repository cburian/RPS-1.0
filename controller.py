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

class ChoiceError(Exception):
    pass

class UsernameToShortException(Exception):
    pass

class Controller:
    def __init__(self, view: View, session: Session):
        self.session = session
        self.view = view

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

    @staticmethod
    def make_choice(choice_options):
        while True:
            try:
                choice = input('\n---> Your choice: ').lower()
                if choice not in choice_options:
                    raise ChoiceError
            except ChoiceError:
                print('\nInvalid choice!')
            else:
                return choice

    def act_on_login_choice(self, choice):
        """

        :param choice: str - can be: -- l, r or q
        :return:
        """

        username = 'John Doe'
        password = 'password'

        users = self.get_users_data(password=False)
        passwords = self.get_users_data(password=True)

        # print('users:', users)
        # print('passwords:', passwords)

        # quit:
        if choice == 'q':
            return None, None

        # login:
        elif choice == 'l':

            while True:
                username = self.ask_for_username_password(password=False)
                if username in ['q', 'Q']:
                    return 'q', 'q'  # todo: quit to main menu
                elif username not in users:
                    self.view.unknown_user_message()
                else:
                    break

            while True:

                password = self.ask_for_username_password()

                user_index = users.index(username)

                if password in ['q', 'Q']:
                    return 'q', 'q'  # todo: quit to main menu
                if password not in passwords:
                    self.view.invalid_password_message()
                else:
                    password_index = passwords.index(password)
                    if password_index != user_index:
                        self.view.invalid_password_message()
                    else:
                        break

            self.view.print_old_user_message(username)

        # register:
        elif choice == 'r':
            self.view.print_new_user_message()
            while True:
                username = self.ask_for_username_password(password=False)
                if username in ['q', 'Q']:
                    return 'q', 'q'  # todo: quit to main menu
                elif username in users:
                    self.view.username_already_in_use_message(username)
                else:
                    break

            while True:

                password = self.ask_for_username_password()

                if password in ['q', 'Q']:
                    return 'q', 'q'  # todo: quit to main menu
                else:
                    break

            # todo: write on csv the new use and password

        return username, password

    @staticmethod
    def ask_for_username_password(password=True) -> str:
        placeholder = ''
        if password:
            placeholder = 'password'
        else:
            placeholder = 'username'

        while True:
            try:
                print(f'\nInput {placeholder} or Quit (Q) to main menu:')
                player_username = input(f'{placeholder.capitalize()}: ')
                if player_username not in ['q', 'Q']:
                    if len(player_username) < 3:
                        raise UsernameToShortException
            except UsernameToShortException:
                print(f'{placeholder.capitalize()} to short! '
                      f'Minimum 3 characters!')
            else:
                return player_username

    @staticmethod
    def get_users_data(users_file: str = 'users.csv', password=True) -> list:
        """

        :param users_file: filename of users and password data
        :param password: bool - if True => returns passwords
        :return: usernames or passwords
        """
        import csv
        data = []
        with open(users_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if password:
                    data.append(row[1])
                else:
                    data.append(row[0])
        return data[1:]

    def play_round(self, components: list, win_dict: dict):

        # print game options:
        self.view.print_options(components)

    def login_register_loop(self):

        while True:
            # login menu:
            self.view.print_login_menu()
            login_register_choice_options = ['l', 'r', 'q']
            login_choice = self.make_choice(login_register_choice_options)
            username, password = self.act_on_login_choice(login_choice)

            if not username:
                return None  # quit game
            elif username == 'q':
                continue  # return to main menu
            else:
                users = self.get_users_data(password=False)

                #  login:
                if username in users:

                    played_games = [2, 0, 0, 5, 0]
                    self.view.prt_logged_in_menu(played_games)

                    played_games_choices = ['s', 'e', 'm', 'h', 'i']
                    zip_nr_of_games_and_choices = zip(played_games_choices,
                                                      played_games)
                    zipped_dict = dict(zip_nr_of_games_and_choices)
                    print(zipped_dict)
                    eligible_choices_list = []
                    for k, v in zipped_dict.items():
                        if v:
                            eligible_choices_list.append(k)
                    eligible_choices_list.extend(['n', 'q'])
                    print(eligible_choices_list)
                    old_user_choice = self.make_choice(eligible_choices_list)
                    print('old user choice ===---> ', old_user_choice)
                    if old_user_choice == 'q':
                        continue

                #  register:
                else:
                    self.view.prt_new_game_menu()
                    play_mode_choice_options = ['s', 'e', 'm', 'h', 'i', 'q']
                    game_choice = self.make_choice(play_mode_choice_options)
                    print('new game choice ===---> ', game_choice)
                    if game_choice == 'q':
                        continue
                break

        print('//// username: ', username)
        print('//// password: ', password)

    def play_session(self):
        # A. Welcome message:
        self.view.print_welcome()

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

        # # available games:
        # # 1. get:
        # available_games = self.session.get_available_games()
        # # 2. print:
        # self.view.print_available_games(available_games)
        # # 3. chose:
        # chosen_game = self.chose_game(available_games)
        #
        # # Rules for chosen game:
        # # 1. extract:
        # rules = self.session.extract_rules(chosen_game)
        # # 2. print rules:
        # self.view.print_rules(rules)
        #
        # # Game components and Winning dictionary:
        # # 1. get:
        # components, win_dict = self.session.get_components_dict(rules)
        #
        # # ===== Play round loop: =====
        # # 2. print components
        # self.view.print_options(components)


def main():
    c = Controller(View(), Session())
    c.play_session()


if __name__ == '__main__':
    main()
