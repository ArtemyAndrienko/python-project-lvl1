"""
    Description: Brain even game functions.
    author: _artemy
"""

from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return (number % 2) == 0


def make_question():
    number = randint(0, 100)
    even = 'yes' if is_even(number) else 'no'
    return (number, even)