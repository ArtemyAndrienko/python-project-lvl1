#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CLI functions."""

import prompt


def welcome():
    """Print welcome message"""
    print('Welcome to the Brain Games!')


def ask_name():
    """Asks user name. :return: username """
    return prompt.string('May I have your name? ')


def greet(name):
    """User greeting"""
    print('Hello, {}!'.format(name))


def get_answer():
    """:return answer"""
    return prompt.string('Your answer: ')


def run():
    """Main method. Combine all methods together"""
    welcome()
    print()
    greet(ask_name())