from random import randint
from random import choice

DESCRIPTION = 'What is the result of the expression?'


def rule():
    a = randint(1, 100)
    b = randint(1, 100)
    expressions_list = ('+', '-', '*')
    rand_expressions = choice(expressions_list)
    question = f'Question: {a} {rand_expressions} {b}'
    correct_answer = str(expressions(a, b, rand_expressions))
    return question, correct_answer


def expressions(a, b, expression):
    return expression == '+' and a + b or \
        expression == '-' and a - b or \
        expression == '*' and a * b
