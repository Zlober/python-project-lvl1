#!usr/bin/env python
from brain_games.games import start_message_game
from brain_games.games.prime import prime


def main():
    message = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    start_message_game(prime, message)


if __name__ == '__main__':
    main()
