"""Description: brain gcd game functions."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    """Gcd.

    :param number1:
    :param number2:
    :return: gcd
    """
    if number2 == 0:
        return abs(number1)
    remainder = number1 % number2
    if remainder == 0:
        return abs(number2)
    return gcd(number2, remainder)


def make_question():
    """Asks question.

    :return: expression, result
    """
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    expression = '{} {}'.format(number1, number2)
    result = str(gcd(number1, number2))
    return (expression, result)
