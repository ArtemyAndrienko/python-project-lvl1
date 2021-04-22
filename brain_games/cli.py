"""
    description: CLI functions.
    author: _artemy
"""

import prompt

def welcome():
    print('Welcome to the Brain Games!')


def ask_name():
    return prompt.string('May I have your name? ')


def greet(name):
    print('Hello, {}!'.format(name))


def get_answer():
    return prompt.string('Your answer: ')


def run():
    welcome()
    print()
    greet(ask_name())