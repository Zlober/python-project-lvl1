import prompt
from random import randint


def gcd(name):
    print('Find the greatest common divisor of given numbers.')
    for i in range(1, 4):
        a = randint(1, 100)
        b = randint(1, 100)
        correct_answer = evc_func(a, b)
        print(f'Question: {a} {b}')
        answer = prompt.integer('Your answer: ', empty=False)
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')


def evc_func(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
