from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 100)
    question = number
    correct_answer = is_prime(number) and 'yes' or 'no'
    return question, correct_answer


def is_prime(a):
    b = a
    for i in range(2, a):
        b -= 1
        if a % b == 0 and a > 2:
            return False
    else:
        return True
