from random import randint


def progression():
    start_number = randint(1, 100)
    step = randint(1, 100)
    lens = randint(5, 10)
    numbers = [str(start_number)]
    for number in range(1, lens):
        numbers.append(str(start_number + step))
        start_number += step
    index_number = randint(0, len(numbers) - 1)
    correct_answer = int(numbers[index_number])
    numbers[index_number] = '..'
    numbers = ' '.join(numbers)
    question = numbers
    return question, correct_answer
