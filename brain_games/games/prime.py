from random import randint
import prompt


def prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(1, 4):
        number = randint(1, 100)
        b = number
        for c in range(2, number):
            b -= 1
            if number % b == 0 and number > 2:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ', empty=False)
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
