from brain_games.games import greeting
from brain_games.games.calc import calc


def main():
    name = greeting()
    calc(name)


if __name__ == '__main__':
    main()
