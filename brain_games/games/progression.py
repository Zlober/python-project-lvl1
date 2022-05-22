from random import randint
import prompt


def progression(name):
    print('What number is missing in the progression?')
    for i in range(1, 4):
        start_number = randint(1, 100)
        step = randint(1, 100)
        lens = randint(5, 10)
        numbers = [str(start_number)]
        for number in range(1, lens):
            numbers.append(str(start_number + step))
            start_number += step
        index_number = randint(0, len(numbers) - 1)
        correct_answer = numbers[index_number]
        numbers[index_number] = '..'
        numbers = ' '.join(numbers)
        print(f'Question: {numbers}')
        answer = prompt.string('Your answer: ', empty=False)
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
