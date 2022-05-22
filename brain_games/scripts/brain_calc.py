#!usr/bin/env python
from brain_games.games import start_number_game
from brain_games.games.calc import calc


def main():
    message = 'What is the result of the expression?'
    start_number_game(calc, message)


if __name__ == '__main__':
    main()
