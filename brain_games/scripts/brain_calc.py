#!/usr/bin/env python

"""
    description: Brain games - Brain calc game.
    author: _artemy
"""


from brain_games.engine import run
from brain_games.games import brain_calc


def main():
    """Run calculate game."""
    run(brain_calc)


if __name__ == '__main__':
    main()