#!usr/bin/env python
from brain_games.games import greeting
from brain_games.games.even import even_game


def main():
    name = greeting()
    even_game(name)


if __name__ == '__main__':
    main()
