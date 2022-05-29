from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 100)
    question = number
    correct_answer = is_prime(number) and 'no' or 'yes'
    return question, correct_answer


def is_prime(a):
    b = a
    if a <= 1:
        return True
    for i in range(2, a):
        b -= 1
        if a % b == 0:
            return True
    else:
        return False
