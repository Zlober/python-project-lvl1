#!usr/bin/env python
from brain_games.games import start_message_game
from brain_games.games.even import even_game


def main():
    message = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_message_game(even_game, message)


if __name__ == '__main__':
    main()
