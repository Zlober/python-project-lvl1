from brain_games.games import greeting
from brain_games.games.progression import progression


def main():
    name = greeting()
    progression(name)


if __name__ == '__main__':
    main()
