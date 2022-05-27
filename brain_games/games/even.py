from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def rule():
    number = randint(1, 100)
    correct_answer = number % 2 == 0 and 'yes' or 'no'
    question = f'Question: {number}'
    return question, correct_answer
