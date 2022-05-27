#!usr/bin/env python
from brain_games.engine import start_game
import brain_games.games.even as even


def main():
    start_game(even)


if __name__ == '__main__':
    main()
