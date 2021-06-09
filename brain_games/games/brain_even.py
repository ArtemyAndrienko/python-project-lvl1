"""Description: brain even game functions."""

from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    """Is even."""
    return (number % 2) == 0


def make_question():
    """Asks question.

    :return: expression, result
    """
    number = randint(0, 100)
    even = 'yes' if is_even(number) else 'no'
    return (number, even)
