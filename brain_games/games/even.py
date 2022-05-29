from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 100)
    correct_answer = number % 2 == 0 and 'yes' or 'no'
    question = number
    return question, correct_answer
