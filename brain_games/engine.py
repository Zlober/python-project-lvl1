import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ', empty=False)
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for i in range(1, 4):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ', empty=False)
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(.'
                  f' Correct answer was {correct_answer}.\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
