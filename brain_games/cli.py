# # !/usr/bin/python3
# -*- coding: utf-8 -*-

"""CLI functions."""

import prompt


def welcome():
    """Print welcome message."""
    print('Welcome to the Brain Games!')


def ask_name():
    """Asks user name.

    :returns: username
    """
    return prompt.string('May I have your name? ')


def greet(name):
    """User greetings."""
    print('Hello, {}!'.format(name))


def get_answer():
    """Asks answer.

    :returns answer
    """
    return prompt.string('Your answer: ')


def run():
    """This is a main method. Combine all methods together."""
    welcome()
    print()
    greet(ask_name())
