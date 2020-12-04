from rps_exceptions import *


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
