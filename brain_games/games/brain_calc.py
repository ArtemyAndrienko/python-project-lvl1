"""Description: brain calc game functions."""

from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = [('+', add), ('-', sub), ('*', mul)]


def make_question():
    """Asks question.

    :return: expression, result
    """
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    symbol, operation = choice(OPERATIONS)
    expression = '{} {} {}'.format(number1, symbol, number2)
    result = str(operation(number1, number2))
    return (expression, result)
