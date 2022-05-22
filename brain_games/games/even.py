from random import randint


def even_game():
    number = randint(1, 100)
    correct_answer = number % 2 == 0 and 'yes' or 'no'
    question = number
    return question, correct_answer
