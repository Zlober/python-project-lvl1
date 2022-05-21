from random import randint
from random import choice
import prompt


def calc(name):
    print('What is the result of the expression?')
    for i in range(1, 4):
        a = randint(1, 100)
        b = randint(1, 100)
        expressions_list = ('+', '-', '*')
        rand_expressions = choice(expressions_list)
        print(f'Question: {a} {rand_expressions} {b}')
        answer = prompt.integer('Your answer: ', empty=False)
        correct_answer = expressions(a, b, rand_expressions)
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(.'
                  f' Correct answer was {correct_answer}.\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')


def expressions(a, b, expression):
    return expression == '+' and a + b or \
           expression == '-' and a - b or \
           expression == '*' and a * b
