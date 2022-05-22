from random import randint


def prime():
    a = randint(1, 100)
    b = a
    for i in range(2, a):
        b -= 1
        if a % b == 0 and a > 2:
            correct_answer = 'no'
            break
    else:
        correct_answer = 'yes'
    question = a
    return question, correct_answer
