import prompt
from random import randint


def even_game():
    name = prompt.string('May I have your name? ', empty=False)
    print(f'Hello, {name}!\n'
          f'Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(1, 4):
        number = randint(1, 100)
        correct_answer = number % 2 == 0 and 'yes' or 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ', empty=False).lower()
        if number % 2 == 0 and answer == 'yes' \
                or \
                number % 2 == 1 and answer == 'no':
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was '
                  f'\'{correct_answer}\'.\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    even_game()
