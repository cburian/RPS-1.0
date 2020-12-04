import rps_exceptions as re


def make_choice(choice_options):
    while True:
        try:
            choice = input('\n---> Your choice: ').lower()
            if choice not in choice_options:
                raise re.ChoiceError
        except re.ChoiceError:
            print('\nInvalid choice!')
        else:
            return choice


def get_users_data(users_file: str = 'users.csv') -> dict:
    """
    :param users_file: filename of users and password data
    :return user_data (dict): {username:  password}
    """
    import csv
    user_data = {}
    with open(users_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            user_data[row[0]] = row[1]
    user_data.pop('username')
    return user_data


def ask_for_username_password(password=True) -> str:

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
                    raise re.UsernameToShortException
        except re.UsernameToShortException:
            print(f'{placeholder.capitalize()} to short! '
                  f'Minimum 3 characters!')
        else:
            return player_username
