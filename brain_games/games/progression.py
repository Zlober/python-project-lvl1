from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def rule():
    start_number = randint(1, 100)
    step = randint(1, 100)
    lens = randint(5, 10)
    numbers = [str(start_number)]
    for number in range(1, lens):
        numbers.append(str(start_number + step))
        start_number += step
    index_number = randint(0, len(numbers) - 1)
    correct_answer = str(numbers[index_number])
    numbers[index_number] = '..'
    numbers = ' '.join(numbers)
    question = f'Question: {numbers}'
    return question, correct_answer
