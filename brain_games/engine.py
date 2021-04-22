from brain_games import cli

MAX_ROUNDS = 3

def run(game):
    cli.welcome()
    print(game.DESCRIPTION, '\n')
    name = cli.ask_name()
    cli.greet(name)
    print()
    for _ in range(MAX_ROUNDS):
        q, a = game.make_question()
        print('Question: {}'.format(q))
        answer = cli.get_answer()
        if (answer == a):
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'".format(answer, a))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))