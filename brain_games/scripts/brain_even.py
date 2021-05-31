#!/usr/bin/env python

"""
    description: Brain even game.
    author: _artemy
"""


from brain_games.engine import run
from brain_games.games import brain_even


def main():
    """Run even game."""
    run(brain_even)


if __name__ == '__main__':
    main()