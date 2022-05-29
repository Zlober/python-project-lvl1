from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start_number = randint(1, 100)
    step = randint(1, 100)
    lens = randint(5, 10)
    progression = list(range(start_number, (start_number + lens * step), step))
    index_number = randint(0, len(progression) - 1)
    correct_answer = str(progression[index_number])
    progression[index_number] = '..'
    progression = ' '.join(str(item) for item in progression)
    question = progression
    return question, correct_answer
