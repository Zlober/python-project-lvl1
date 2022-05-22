from brain_games.games import greeting
from brain_games.games.gcd import gcd


def main():
    name = greeting()
    gcd(name)


if __name__ == '__main__':
    main()
