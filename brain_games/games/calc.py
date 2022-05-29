from random import randint
from random import choice
import operator

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    a = randint(1, 100)
    b = randint(1, 100)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    operation = choice(list(operations.keys()))
    correct_answer = str(operations[operation](a, b))
    question = f'{a} {operation} {b}'
    return question, correct_answer
