#!usr/bin/env python
from brain_games.games import start_number_game
from brain_games.games.gcd import gcd


def main():
    message = 'Find the greatest common divisor of given numbers.'
    start_number_game(gcd, message)


if __name__ == '__main__':
    main()
