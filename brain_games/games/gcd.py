from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def rule():
    a = randint(1, 100)
    b = randint(1, 100)
    correct_answer = str(evc_func(a, b))
    question = f'{a} {b}'
    return question, correct_answer


def evc_func(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
