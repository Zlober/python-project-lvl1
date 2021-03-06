from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    a = randint(1, 100)
    b = randint(1, 100)
    correct_answer = str(evc_func(a, b))
    question = a, b
    question = ' '.join(str(string) for string in question)
    return question, correct_answer


def evc_func(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
