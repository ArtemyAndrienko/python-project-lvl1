"""Description: brain prime game functions."""

from random import randint
from math import sqrt, ceil

DESCRIPTION = ('Answer "yes" if given number is prime. '
               'Otherwise answer "no".')


def is_prime(number):
    """Is a prime.

    :param number:
    :return: true/false
    """
    for i in range(2, ceil(sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True


def make_question():
    """Asks question.

    :return: (expression, result)
    """
    number = randint(2, 1000)
    result = 'yes' if is_prime(number) else 'no'
    return (number, result)
