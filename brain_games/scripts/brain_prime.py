#!/usr/bin/env python

"""
    description: Brain prime game.
    author: _artemy
"""


from brain_games.engine import run
from brain_games.games import brain_prime


def main():
    """Run prime game."""
    run(brain_prime)


if __name__ == '__main__':
    main()