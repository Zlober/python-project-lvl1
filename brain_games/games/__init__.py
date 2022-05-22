import prompt


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ', empty=False)
    print(f'Hello, {name}!')
    return name


def start_number_game(function, message):
    name = greeting()
    print(message)
    for i in range(1, 4):
        question, correct_answer = function()
        print(f'Question: {question}')
        answer = prompt.integer('Your answer: ', empty=False)
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(.'
                  f' Correct answer was {correct_answer}.\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')


def start_message_game(function, message):
    name = greeting()
    print(message)
    for i in range(1, 4):
        question, correct_answer = function()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ', empty=False).lower()
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
