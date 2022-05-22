from brain_games.games import greeting
from brain_games.games.prime import prime


def main():
    name = greeting()
    prime(name)


if __name__ == '__main__':
    main()
