#!usr/bin/env python
from brain_games.games import start_number_game
from brain_games.games.progression import progression


def main():
    message = 'What number is missing in the progression?'
    start_number_game(progression, message)


if __name__ == '__main__':
    main()
